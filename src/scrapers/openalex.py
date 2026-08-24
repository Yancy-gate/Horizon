"""OpenAlex works scraper for faculty journal papers.

IEEE / Elsevier papers rarely appear on arXiv. OpenAlex indexes those
venues without an API key, so Horizon can follow specific faculty
author IDs and keep only items that hit configured paper keywords.
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone
from typing import Any, List, Optional

import httpx

from ..models import ContentItem, OpenAlexConfig, SourceType
from .base import BaseScraper
from .rss import match_source_content_filters

logger = logging.getLogger(__name__)


def reconstruct_abstract(inverted: dict[str, Any] | None) -> str:
    """Rebuild abstract text from OpenAlex's inverted index."""
    if not inverted:
        return ""
    positions: list[tuple[int, str]] = []
    for word, indexes in inverted.items():
        if not isinstance(indexes, list):
            continue
        for index in indexes:
            try:
                positions.append((int(index), str(word)))
            except (TypeError, ValueError):
                continue
    positions.sort()
    return " ".join(word for _, word in positions)


class OpenAlexScraper(BaseScraper):
    """Scraper backed by the OpenAlex works API."""

    SOURCE_TYPE = SourceType.OPENALEX
    BASE_URL = "https://api.openalex.org/works"

    def __init__(self, config: OpenAlexConfig, http_client: httpx.AsyncClient):
        super().__init__({"openalex": config}, http_client)
        self.cfg = config

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.cfg.enabled:
            return []

        items: list[ContentItem] = []
        seen: set[str] = set()
        now = datetime.now(timezone.utc)

        for query in self.cfg.queries:
            query_since = since
            if query.time_window_hours:
                query_since = now - timedelta(hours=query.time_window_hours)
            for item in await self._fetch_query(query, query_since):
                fingerprint = (
                    str(item.metadata.get("doi") or "").casefold()
                    or item.title.casefold()
                )
                if item.id in seen or fingerprint in seen:
                    continue
                seen.add(item.id)
                seen.add(fingerprint)
                items.append(item)
        return items

    async def _fetch_query(
        self, query, since: datetime
    ) -> list[ContentItem]:
        author_filter = "|".join(query.author_ids)
        params = {
            "filter": (
                f"author.id:{author_filter},"
                f"from_publication_date:{since.date().isoformat()},"
                "is_retracted:false"
            ),
            "sort": "publication_date:desc",
            "per_page": min(50, max(query.max_items * 2, 10)),
            "select": (
                "id,doi,display_name,publication_date,authorships,"
                "primary_location,abstract_inverted_index,type"
            ),
        }
        headers = {"Accept": "application/json"}
        user_agent = "Horizon/1.0"
        if self.cfg.mailto:
            user_agent += f" (mailto:{self.cfg.mailto})"
        headers["User-Agent"] = user_agent

        try:
            response = await self.client.get(
                self.BASE_URL, params=params, headers=headers, timeout=30.0
            )
            response.raise_for_status()
            payload = response.json()
        except (httpx.HTTPError, ValueError) as exc:
            logger.warning("OpenAlex fetch failed for %s: %s", query.name, exc)
            return []

        kept: list[ContentItem] = []
        for row in payload.get("results") or []:
            item = self._row_to_item(row, query)
            if item is None or item.published_at < since:
                continue
            hay = f"{item.title}\n{item.content or ''}"
            matched = match_source_content_filters(hay, "", query.metadata)
            if matched is None:
                continue
            if matched:
                item.metadata["matched_paper_keyword"] = matched
            kept.append(item)
            if len(kept) >= query.max_items:
                break
        return kept

    def _row_to_item(self, row: dict[str, Any], query) -> Optional[ContentItem]:
        title = (row.get("display_name") or "").strip()
        published = self._parse_date(row.get("publication_date"))
        url = self._item_url(row)
        if not title or published is None or not url:
            return None

        authors = []
        for authorship in row.get("authorships") or []:
            name = ((authorship.get("author") or {}).get("display_name") or "").strip()
            if name:
                authors.append(name)
        venue = (
            ((row.get("primary_location") or {}).get("source") or {}).get("display_name")
            or ""
        )
        abstract = reconstruct_abstract(row.get("abstract_inverted_index"))
        content_parts = [part for part in (venue, abstract) if part]

        work_id = str(row.get("id") or "").rsplit("/", 1)[-1]
        metadata = {
            **query.metadata,
            "feed_name": query.name,
            "category": query.category,
            "venue": venue,
            "doi": row.get("doi"),
            "openalex_id": row.get("id"),
            "authors": authors,
            "source_kind": "openalex-papers",
        }
        return ContentItem(
            id=self._generate_id(self.SOURCE_TYPE.value, "work", work_id or title),
            source_type=self.SOURCE_TYPE,
            title=title,
            url=url,
            content="\n\n".join(content_parts) or None,
            author=authors[0] if authors else query.name,
            published_at=published,
            metadata=metadata,
        )

    @staticmethod
    def _parse_date(value: Any) -> datetime | None:
        if not value or not isinstance(value, str):
            return None
        try:
            if len(value) == 4:
                return datetime(int(value), 1, 1, tzinfo=timezone.utc)
            return datetime.fromisoformat(value).replace(tzinfo=timezone.utc)
        except ValueError:
            return None

    @staticmethod
    def _item_url(row: dict[str, Any]) -> str | None:
        location = row.get("primary_location") or {}
        for candidate in (
            location.get("landing_page_url"),
            row.get("doi"),
            row.get("id"),
        ):
            if candidate:
                return str(candidate)
        return None
