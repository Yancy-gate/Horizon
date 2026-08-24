"""Tests for preference radar helpers and ingest merge logic."""

from datetime import datetime, timezone

from src.models import ContentItem, SourceType
from src.preference_radar.ingest import _dedupe_strings
from src.preference_radar.models import PreferenceProfile
from src.preference_radar.service import collect_keywords, item_matches_keywords
from src.preference_radar.utils import normalize_url


def _item(title: str, content: str = "") -> ContentItem:
    return ContentItem(
        id="rss:test",
        source_type=SourceType.RSS,
        title=title,
        url="https://example.com/test",
        content=content,
        published_at=datetime(2026, 4, 25, tzinfo=timezone.utc),
    )


def test_collect_keywords_deduplicates_case_insensitive():
    profile = PreferenceProfile(
        interests=["Diffusion", "diffusion"],
        raw_keywords=["4K", "4k"],
    )
    assert collect_keywords(profile) == ["Diffusion", "4K"]


def test_item_matches_keywords_uses_title_and_content():
    profile = PreferenceProfile(interests=["robotics vision"])
    keywords = collect_keywords(profile)
    assert item_matches_keywords(_item("New robotics vision benchmark"), keywords)
    assert not item_matches_keywords(_item("Unrelated finance news"), keywords)


def test_normalize_url_strips_www_and_trailing_slash():
    assert normalize_url("https://www.example.com/path/") == "example.com/path"


def test_dedupe_strings_preserves_first_casing():
    merged = _dedupe_strings(["Alpha"], ["alpha", "Beta"])
    assert merged == ["Alpha", "Beta"]
