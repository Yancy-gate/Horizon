"""Data models for the preference radar sidecar."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


PREFERENCE_RADAR_CATEGORY = "preference-radar"
HUST_RESEARCH_CATEGORY = "hust-research"


class PreferenceProfile(BaseModel):
    """Long-lived user preference profile (maintained via ingest workflow)."""

    schema_version: int = 1
    interests: List[str] = Field(default_factory=list)
    persona_summary: str = ""
    negative_interests: List[str] = Field(default_factory=list)
    raw_keywords: List[str] = Field(default_factory=list)
    source_doc_count: int = 0
    generated_at: Optional[str] = None
    extraction_mode: str = "curated"


class PreferenceSearchQuery(BaseModel):
    """One Google News search query owned by the preference radar."""

    query: str
    language: str = "zh"
    country: str = "CN"
    max_results: int = 20
    enabled: bool = True


class PreferenceSourcesConfig(BaseModel):
    """Runtime knobs and independent search sources for preference radar."""

    enabled: bool = True
    score_threshold: float = 7.0
    max_items: int = 5
    time_window_hours: Optional[int] = None
    google_news_queries: List[PreferenceSearchQuery] = Field(default_factory=list)


class PreferenceDraftAddition(BaseModel):
    interests: List[str] = Field(default_factory=list)
    negative_interests: List[str] = Field(default_factory=list)
    raw_keywords: List[str] = Field(default_factory=list)
    google_news_queries: List[PreferenceSearchQuery] = Field(default_factory=list)
    persona_summary_append: str = ""


class PreferenceIngestDraft(BaseModel):
    """AI-generated draft awaiting user confirmation."""

    draft_id: str
    created_at: str
    source_path: str
    summary: str
    proposed: PreferenceDraftAddition
    persona_summary_after: str = ""


class PreferenceChangelogEntry(BaseModel):
    """Audit log entry after a draft is applied."""

    applied_at: str
    draft_id: str
    source_path: str
    summary: str
    interests_added: List[str] = Field(default_factory=list)
    keywords_added: List[str] = Field(default_factory=list)
    queries_added: List[str] = Field(default_factory=list)


class PreferenceFeedbackEntry(BaseModel):
    """One user rating from the daily digest UI or an imported export file."""

    url: str
    title: str = ""
    tags: List[str] = Field(default_factory=list)
    rating: str  # "up" | "down"
    section: str = "other"
    lang: str = "zh"
    created_at: str
    source: str = "web"


class PreferenceFeedbackExport(BaseModel):
    """Browser export bundle dropped into feedback-inbox."""

    exported_at: str
    entries: List[PreferenceFeedbackEntry] = Field(default_factory=list)


class PreferenceFeedbackState(BaseModel):
    """Aggregated feedback signals applied to scoring and profile."""

    schema_version: int = 1
    processed_keys: List[str] = Field(default_factory=list)
    liked_urls: List[str] = Field(default_factory=list)
    disliked_urls: List[str] = Field(default_factory=list)
    liked_tags: dict[str, int] = Field(default_factory=dict)
    disliked_tags: dict[str, int] = Field(default_factory=dict)
    last_applied_at: Optional[str] = None
