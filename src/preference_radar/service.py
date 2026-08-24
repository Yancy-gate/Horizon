"""Preference radar pipeline: reuse main fetch + independent search."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable, List, Set

import httpx
from rich.console import Console

from ..ai.analyzer import ContentAnalyzer
from ..ai.client import create_ai_client
from ..models import Config, ContentItem, GoogleNewsConfig
from ..scrapers.google_news import GoogleNewsScraper
from .models import (
    PREFERENCE_RADAR_CATEGORY,
    PreferenceProfile,
    PreferenceSourcesConfig,
)
from .feedback import FeedbackService
from .storage import PreferenceRadarStorage


from .utils import normalize_url


def collect_keywords(profile: PreferenceProfile) -> List[str]:
    seen: Set[str] = set()
    keywords: List[str] = []
    for value in [*profile.interests, *profile.raw_keywords]:
        key = value.strip().lower()
        if key and key not in seen:
            seen.add(key)
            keywords.append(value.strip())
    return keywords


def item_matches_keywords(item: ContentItem, keywords: Iterable[str]) -> bool:
    if not keywords:
        return False
    tags = " ".join(item.ai_tags or [])
    haystack = f"{item.title} {item.content or ''} {tags}".lower()
    return any(keyword.lower() in haystack for keyword in keywords)


def interests_as_prompt_string(profile: PreferenceProfile) -> str | None:
    if not profile.interests:
        return None
    return ", ".join(profile.interests)


class PreferenceRadarService:
    """Independent sidecar pipeline driven by ``data/preference-radar/``."""

    def __init__(
        self,
        config: Config,
        storage: PreferenceRadarStorage | None = None,
        console: Console | None = None,
    ) -> None:
        self.config = config
        self.storage = storage or PreferenceRadarStorage()
        self.console = console or Console()
        self.feedback = FeedbackService(self.storage)

    def is_active(self) -> bool:
        sources = self.storage.load_sources()
        profile = self.storage.load_profile()
        if not sources.enabled:
            return False
        return bool(profile.interests or profile.raw_keywords or sources.google_news_queries)

    async def run(
        self,
        analyzed_items: List[ContentItem],
        since: datetime,
        http_client: httpx.AsyncClient,
    ) -> List[ContentItem]:
        profile = self.storage.load_profile()
        sources = self.storage.load_sources()
        if not sources.enabled:
            return []

        keywords = collect_keywords(profile)
        if not keywords and not sources.google_news_queries:
            self.console.print("[dim]Preference radar skipped (empty profile).[/dim]\n")
            return []

        self.console.print("[bold magenta]🎯 Preference radar — selecting personalized items...[/bold magenta]")

        candidates: List[ContentItem] = []
        seen_urls: Set[str] = set()

        for item in analyzed_items:
            if item_matches_keywords(item, keywords):
                key = normalize_url(str(item.url))
                if key not in seen_urls:
                    seen_urls.add(key)
                    candidates.append(item.model_copy(deep=True))

        independent = await self._fetch_independent_queries(sources, since, http_client)
        for item in independent:
            key = normalize_url(str(item.url))
            if key not in seen_urls:
                seen_urls.add(key)
                candidates.append(item)

        if not candidates:
            self.console.print("   No preference candidates found.\n")
            return []

        ai_client = create_ai_client(self.config.ai)
        analyzer = ContentAnalyzer(
            ai_client,
            user_interests=interests_as_prompt_string(profile),
            negative_interests=profile.negative_interests or None,
            persona_summary=profile.persona_summary or None,
        )
        scored = await analyzer.analyze_batch(candidates)
        feedback_state = self.storage.load_feedback_state()

        threshold = sources.score_threshold
        selected: List[ContentItem] = []
        for item in scored:
            if self.feedback.should_exclude_url(str(item.url), feedback_state):
                continue
            adjusted = (item.ai_score or 0) + self.feedback.score_adjustment(item, feedback_state)
            if adjusted >= threshold:
                item.ai_score = round(min(adjusted, 10.0), 1)
                selected.append(item)

        selected.sort(key=lambda item: item.ai_score or 0, reverse=True)
        selected = selected[: sources.max_items]

        for item in selected:
            item.metadata["category"] = PREFERENCE_RADAR_CATEGORY
            item.metadata["preference_radar"] = True

        self.console.print(
            f"   Selected {len(selected)} preference items (threshold ≥ {threshold}).\n"
        )
        return selected

    async def _fetch_independent_queries(
        self,
        sources: PreferenceSourcesConfig,
        since: datetime,
        http_client: httpx.AsyncClient,
    ) -> List[ContentItem]:
        items: List[ContentItem] = []
        for query_cfg in sources.google_news_queries:
            if not query_cfg.enabled or not query_cfg.query.strip():
                continue
            gn_config = GoogleNewsConfig(
                enabled=True,
                query=query_cfg.query.strip(),
                language=query_cfg.language,
                country=query_cfg.country,
                max_results=query_cfg.max_results,
                category=PREFERENCE_RADAR_CATEGORY,
            )
            scraper = GoogleNewsScraper(gn_config, http_client)
            fetched = await scraper.fetch(since)
            items.extend(fetched)
        return items

    @staticmethod
    def excluded_urls(items: List[ContentItem]) -> Set[str]:
        return {normalize_url(str(item.url)) for item in items}

    @staticmethod
    def filter_out_urls(items: List[ContentItem], excluded: Set[str]) -> List[ContentItem]:
        if not excluded:
            return items
        return [
            item
            for item in items
            if normalize_url(str(item.url)) not in excluded
        ]
