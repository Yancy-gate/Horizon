"""Tests for preference feedback apply logic."""

from datetime import datetime, timezone

from src.models import ContentItem, SourceType
from src.preference_radar.feedback import FeedbackService, feedback_entry_key
from src.preference_radar.models import PreferenceFeedbackEntry
from src.preference_radar.storage import PreferenceRadarStorage


def _entry(url: str, rating: str, tags: list[str] | None = None) -> PreferenceFeedbackEntry:
    return PreferenceFeedbackEntry(
        url=url,
        title="Sample title",
        tags=tags or ["robotics"],
        rating=rating,
        section="other",
        lang="zh",
        created_at="2026-08-24T07:00:00+00:00",
    )


def test_apply_upvote_adds_keywords_and_liked_url(tmp_path):
    storage = PreferenceRadarStorage(tmp_path / "preference-radar")
    storage.ensure_layout()
    storage.append_feedback_entries([_entry("https://example.com/a", "up", ["VLA"])])

    result = FeedbackService(storage).apply_pending()

    profile = storage.load_profile()
    state = storage.load_feedback_state()
    assert result.applied == 1
    assert "vla" in [k.lower() for k in profile.raw_keywords]
    assert "example.com/a" in state.liked_urls[0]


def test_apply_downvote_adds_negative_interest_and_disliked_url(tmp_path):
    storage = PreferenceRadarStorage(tmp_path / "preference-radar")
    storage.ensure_layout()
    storage.append_feedback_entries([_entry("https://example.com/b", "down", ["crypto"])])

    FeedbackService(storage).apply_pending()

    profile = storage.load_profile()
    state = storage.load_feedback_state()
    assert "crypto" in profile.negative_interests
    assert any("example.com/b" in url for url in state.disliked_urls)


def test_score_adjustment_boosts_liked_and_penalizes_disliked(tmp_path):
    storage = PreferenceRadarStorage(tmp_path / "preference-radar")
    storage.ensure_layout()
    service = FeedbackService(storage)
    storage.append_feedback_entries([_entry("https://example.com/liked", "up", ["slam"])])
    service.apply_pending()

    liked_item = ContentItem(
        id="rss:1",
        source_type=SourceType.RSS,
        title="SLAM benchmark",
        url="https://example.com/liked",
        published_at=datetime(2026, 8, 24, tzinfo=timezone.utc),
        ai_tags=["slam"],
        ai_score=7.0,
    )
    storage.append_feedback_entries(
        [_entry("https://example.com/disliked", "down", ["spam"])]
    )
    service.apply_pending()

    assert service.score_adjustment(liked_item) >= 1.0
    assert service.should_exclude_url("https://example.com/disliked")


def test_feedback_entry_key_is_stable():
    entry = _entry("https://www.example.com/x/", "up")
    assert feedback_entry_key(entry) == "example.com/x|up|2026-08-24T07:00:00+00:00"
