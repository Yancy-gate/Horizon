"""Document ingestion: AI draft → user confirm → profile update."""

from __future__ import annotations

import re
from pathlib import Path

from ..ai.client import create_ai_client
from ..ai.utils import parse_json_response
from ..models import Config
from .models import (
    PreferenceDraftAddition,
    PreferenceIngestDraft,
    PreferenceProfile,
    PreferenceSearchQuery,
    PreferenceSourcesConfig,
    PreferenceChangelogEntry,
)
from .prompts import PREFERENCE_INGEST_SYSTEM, PREFERENCE_INGEST_USER
from .storage import PreferenceRadarStorage


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", value.strip().lower())
    return slug.strip("-")[:48] or "doc"


def _dedupe_strings(existing: list[str], additions: list[str]) -> list[str]:
    seen = {item.strip().lower() for item in existing}
    merged = list(existing)
    for item in additions:
        key = item.strip()
        if not key:
            continue
        lower = key.lower()
        if lower in seen:
            continue
        seen.add(lower)
        merged.append(key)
    return merged


class PreferenceIngestService:
    """Generate and apply preference update drafts."""

    def __init__(
        self,
        config: Config,
        storage: PreferenceRadarStorage | None = None,
    ) -> None:
        self.config = config
        self.storage = storage or PreferenceRadarStorage()

    async def create_draft_from_text(
        self,
        *,
        filename: str,
        content: str,
        source_path: str,
    ) -> PreferenceIngestDraft:
        ai_client = create_ai_client(self.config.ai)
        response = await ai_client.complete(
            system=PREFERENCE_INGEST_SYSTEM,
            user=PREFERENCE_INGEST_USER.format(
                filename=filename,
                content=content[:12000],
            ),
            temperature=0.2,
        )
        parsed = parse_json_response(response) or {}
        proposed = PreferenceDraftAddition(
            interests=list(parsed.get("interests") or []),
            negative_interests=list(parsed.get("negative_interests") or []),
            raw_keywords=list(parsed.get("raw_keywords") or []),
            google_news_queries=[
                PreferenceSearchQuery.model_validate(entry)
                for entry in (parsed.get("google_news_queries") or [])
                if isinstance(entry, dict)
            ],
            persona_summary_append=str(parsed.get("persona_summary_append") or "").strip(),
        )
        profile = self.storage.load_profile()
        persona_after = profile.persona_summary
        if proposed.persona_summary_append:
            persona_after = (
                f"{persona_after} {proposed.persona_summary_append}".strip()
                if persona_after
                else proposed.persona_summary_append
            )

        stamp = self.storage.utc_now_iso().replace(":", "").replace("+", "")
        draft_id = f"{stamp}-{_slugify(Path(filename).stem)}"
        draft = PreferenceIngestDraft(
            draft_id=draft_id,
            created_at=self.storage.utc_now_iso(),
            source_path=source_path,
            summary=str(parsed.get("summary") or "Preference update draft"),
            proposed=proposed,
            persona_summary_after=persona_after,
        )
        self.storage.save_draft(draft)
        return draft

    async def create_draft_from_file(self, path: Path) -> PreferenceIngestDraft:
        content = path.read_text(encoding="utf-8")
        return await self.create_draft_from_text(
            filename=path.name,
            content=content,
            source_path=str(path),
        )

    async def process_inbox(self) -> list[PreferenceIngestDraft]:
        drafts: list[PreferenceIngestDraft] = []
        for path in self.storage.list_inbox_files():
            drafts.append(await self.create_draft_from_file(path))
        return drafts

    def apply_draft(self, draft_id: str, *, archive_source: bool = True) -> PreferenceChangelogEntry:
        draft = self.storage.load_draft(draft_id)
        profile = self.storage.load_profile()
        sources = self.storage.load_sources()

        interests_added = [
            item
            for item in draft.proposed.interests
            if item.strip().lower() not in {x.lower() for x in profile.interests}
        ]
        keywords_added = [
            item
            for item in draft.proposed.raw_keywords
            if item.strip().lower() not in {x.lower() for x in profile.raw_keywords}
        ]

        profile.interests = _dedupe_strings(profile.interests, draft.proposed.interests)
        profile.negative_interests = _dedupe_strings(
            profile.negative_interests,
            draft.proposed.negative_interests,
        )
        profile.raw_keywords = _dedupe_strings(profile.raw_keywords, draft.proposed.raw_keywords)
        if draft.persona_summary_after:
            profile.persona_summary = draft.persona_summary_after
        profile.source_doc_count += 1
        profile.generated_at = self.storage.utc_now_iso()

        existing_queries = {entry.query.strip().lower() for entry in sources.google_news_queries}
        queries_added: list[str] = []
        for query in draft.proposed.google_news_queries:
            key = query.query.strip().lower()
            if not key or key in existing_queries:
                continue
            existing_queries.add(key)
            sources.google_news_queries.append(query)
            queries_added.append(query.query)

        self.storage.save_profile(profile)
        self.storage.save_sources(sources)

        source_path = Path(draft.source_path)
        if archive_source and source_path.exists() and source_path.parent == self.storage.inbox_dir:
            self.storage.archive_inbox_file(source_path)

        entry = PreferenceChangelogEntry(
            applied_at=self.storage.utc_now_iso(),
            draft_id=draft.draft_id,
            source_path=draft.source_path,
            summary=draft.summary,
            interests_added=interests_added,
            keywords_added=keywords_added,
            queries_added=queries_added,
        )
        self.storage.append_changelog(entry)
        return entry
