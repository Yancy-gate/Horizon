"""Apply digest feedback to preference profile and scoring signals."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Set

from ..models import ContentItem
from .ingest import _dedupe_strings
from .models import PreferenceFeedbackEntry, PreferenceFeedbackExport, PreferenceFeedbackState
from .utils import normalize_url
from .storage import PreferenceRadarStorage


@dataclass
class FeedbackApplyResult:
    imported: int = 0
    applied: int = 0
    interests_added: int = 0
    keywords_added: int = 0
    negative_added: int = 0


def feedback_entry_key(entry: PreferenceFeedbackEntry) -> str:
    return f"{normalize_url(entry.url)}|{entry.rating}|{entry.created_at}"


def _normalize_tag(tag: str) -> str:
    return tag.strip().lstrip("#").lower()


class FeedbackService:
    """Import browser feedback and write signals back to profile.json."""

    LIKED_TAG_TO_INTEREST = 2
    UP_KEYWORD_TAGS = 1
    DOWN_NEGATIVE_TAGS = 1

    def __init__(self, storage: PreferenceRadarStorage | None = None) -> None:
        self.storage = storage or PreferenceRadarStorage()

    def disliked_urls(self) -> Set[str]:
        state = self.storage.load_feedback_state()
        return {normalize_url(url) for url in state.disliked_urls}

    def import_inbox_exports(self) -> int:
        """Load JSON exports from feedback-inbox/ into feedback.jsonl."""
        imported = 0
        for path in self.storage.list_feedback_inbox_files():
            payload = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(payload, list):
                entries = [PreferenceFeedbackEntry.model_validate(item) for item in payload]
            else:
                export = PreferenceFeedbackExport.model_validate(payload)
                entries = export.entries
            imported += self.storage.append_feedback_entries(entries)
            self.storage.archive_feedback_inbox_file(path)
        return imported

    def import_file(self, path: str) -> int:
        payload = json.loads(Path(path).read_text(encoding="utf-8"))
        if isinstance(payload, list):
            entries = [PreferenceFeedbackEntry.model_validate(item) for item in payload]
        else:
            export = PreferenceFeedbackExport.model_validate(payload)
            entries = export.entries
        return self.storage.append_feedback_entries(entries)

    def apply_pending(self) -> FeedbackApplyResult:
        """Merge unprocessed feedback.jsonl rows into profile + feedback_state."""
        result = FeedbackApplyResult()
        state = self.storage.load_feedback_state()
        profile = self.storage.load_profile()
        processed = set(state.processed_keys)

        interests_before = len(profile.interests)
        keywords_before = len(profile.raw_keywords)
        negative_before = len(profile.negative_interests)

        for entry in self.storage.load_feedback_entries():
            key = feedback_entry_key(entry)
            if key in processed:
                continue

            url_key = normalize_url(entry.url)
            tags = [_normalize_tag(tag) for tag in entry.tags if _normalize_tag(tag)]

            if entry.rating == "up":
                if url_key not in state.liked_urls:
                    state.liked_urls.append(url_key)
                if url_key in state.disliked_urls:
                    state.disliked_urls.remove(url_key)
                for tag in tags:
                    state.liked_tags[tag] = state.liked_tags.get(tag, 0) + 1
                    if state.liked_tags[tag] >= self.UP_KEYWORD_TAGS:
                        profile.raw_keywords = _dedupe_strings(profile.raw_keywords, [tag])
                    if state.liked_tags[tag] >= self.LIKED_TAG_TO_INTEREST:
                        profile.interests = _dedupe_strings(profile.interests, [tag])
            elif entry.rating == "down":
                if url_key not in state.disliked_urls:
                    state.disliked_urls.append(url_key)
                if url_key in state.liked_urls:
                    state.liked_urls.remove(url_key)
                for tag in tags:
                    state.disliked_tags[tag] = state.disliked_tags.get(tag, 0) + 1
                    if state.disliked_tags[tag] >= self.DOWN_NEGATIVE_TAGS:
                        profile.negative_interests = _dedupe_strings(
                            profile.negative_interests,
                            [tag],
                        )
                if entry.title and not tags:
                    topic = entry.title.strip()[:80]
                    if topic:
                        profile.negative_interests = _dedupe_strings(
                            profile.negative_interests,
                            [topic],
                        )
            else:
                continue

            processed.add(key)
            result.applied += 1

        state.processed_keys = sorted(processed)
        state.last_applied_at = self.storage.utc_now_iso()
        profile.generated_at = state.last_applied_at

        self.storage.save_feedback_state(state)
        self.storage.save_profile(profile)

        result.interests_added = len(profile.interests) - interests_before
        result.keywords_added = len(profile.raw_keywords) - keywords_before
        result.negative_added = len(profile.negative_interests) - negative_before
        return result

    def score_adjustment(self, item: ContentItem, state: PreferenceFeedbackState | None = None) -> float:
        """Return additive score delta from historical feedback signals."""
        if state is None:
            state = self.storage.load_feedback_state()

        url_key = normalize_url(str(item.url))
        if url_key in {normalize_url(u) for u in state.disliked_urls}:
            return -10.0

        delta = 0.0
        if url_key in {normalize_url(u) for u in state.liked_urls}:
            delta += 1.0

        item_tags = {_normalize_tag(tag) for tag in (item.ai_tags or [])}
        for tag in item_tags:
            if state.liked_tags.get(tag, 0) >= self.UP_KEYWORD_TAGS:
                delta += 0.5
            if state.disliked_tags.get(tag, 0) >= self.DOWN_NEGATIVE_TAGS:
                delta -= 1.0

        return max(min(delta, 2.0), -3.0)

    def should_exclude_url(self, url: str, state: PreferenceFeedbackState | None = None) -> bool:
        if state is None:
            state = self.storage.load_feedback_state()
        url_key = normalize_url(url)
        return url_key in {normalize_url(u) for u in state.disliked_urls}

    @staticmethod
    def filter_disliked_items(
        items: Iterable[ContentItem],
        disliked_urls: Set[str],
    ) -> List[ContentItem]:
        if not disliked_urls:
            return list(items)
        return [
            item
            for item in items
            if normalize_url(str(item.url)) not in disliked_urls
        ]
