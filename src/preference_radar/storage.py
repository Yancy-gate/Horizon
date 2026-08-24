"""Filesystem storage for preference radar profile, sources, drafts, and changelog."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import List

from .models import (
    PreferenceChangelogEntry,
    PreferenceIngestDraft,
    PreferenceProfile,
    PreferenceSourcesConfig,
)


class PreferenceRadarStorage:
    """Read/write preference radar data under ``data/preference-radar/``."""

    def __init__(self, base_dir: str | Path = "data/preference-radar") -> None:
        self.base_dir = Path(base_dir)
        self.profile_path = self.base_dir / "profile.json"
        self.sources_path = self.base_dir / "sources.json"
        self.inbox_dir = self.base_dir / "inbox"
        self.processed_dir = self.inbox_dir / "processed"
        self.drafts_dir = self.base_dir / "drafts"
        self.changelog_path = self.base_dir / "changelog.jsonl"

    def ensure_layout(self) -> None:
        """Create directory layout if missing."""
        self.inbox_dir.mkdir(parents=True, exist_ok=True)
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        self.drafts_dir.mkdir(parents=True, exist_ok=True)

    def load_profile(self) -> PreferenceProfile:
        if not self.profile_path.exists():
            return PreferenceProfile()
        data = json.loads(self.profile_path.read_text(encoding="utf-8"))
        return PreferenceProfile.model_validate(data)

    def save_profile(self, profile: PreferenceProfile) -> None:
        self.ensure_layout()
        self.profile_path.write_text(
            profile.model_dump_json(indent=2, exclude_none=True) + "\n",
            encoding="utf-8",
        )

    def load_sources(self) -> PreferenceSourcesConfig:
        if not self.sources_path.exists():
            return PreferenceSourcesConfig()
        data = json.loads(self.sources_path.read_text(encoding="utf-8"))
        return PreferenceSourcesConfig.model_validate(data)

    def save_sources(self, sources: PreferenceSourcesConfig) -> None:
        self.ensure_layout()
        self.sources_path.write_text(
            sources.model_dump_json(indent=2, exclude_none=True) + "\n",
            encoding="utf-8",
        )

    def list_inbox_files(self) -> List[Path]:
        self.ensure_layout()
        return sorted(
            p
            for p in self.inbox_dir.iterdir()
            if p.is_file() and not p.name.startswith(".")
        )

    def save_draft(self, draft: PreferenceIngestDraft) -> Path:
        self.ensure_layout()
        path = self.drafts_dir / f"{draft.draft_id}.json"
        path.write_text(
            draft.model_dump_json(indent=2, exclude_none=True) + "\n",
            encoding="utf-8",
        )
        return path

    def load_draft(self, draft_id: str) -> PreferenceIngestDraft:
        path = self.drafts_dir / f"{draft_id}.json"
        if not path.exists():
            raise FileNotFoundError(f"Draft not found: {draft_id}")
        return PreferenceIngestDraft.model_validate(
            json.loads(path.read_text(encoding="utf-8"))
        )

    def list_drafts(self) -> List[Path]:
        self.ensure_layout()
        return sorted(self.drafts_dir.glob("*.json"))

    def append_changelog(self, entry: PreferenceChangelogEntry) -> None:
        self.ensure_layout()
        with self.changelog_path.open("a", encoding="utf-8") as handle:
            handle.write(entry.model_dump_json(exclude_none=True) + "\n")

    def archive_inbox_file(self, source_path: Path) -> Path:
        self.ensure_layout()
        dest = self.processed_dir / source_path.name
        if dest.exists():
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
            dest = self.processed_dir / f"{source_path.stem}-{stamp}{source_path.suffix}"
        source_path.rename(dest)
        return dest

    @staticmethod
    def utc_now_iso() -> str:
        return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
