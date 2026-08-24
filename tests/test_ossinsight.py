from datetime import datetime, timedelta, timezone
from types import SimpleNamespace
from unittest.mock import MagicMock

from src.models import OSSInsightConfig
from src.scrapers.ossinsight import OSSInsightScraper


def test_row_to_item_uses_period_start_for_published_at(monkeypatch):
    fixed_now = datetime(2026, 8, 24, 12, 0, tzinfo=timezone.utc)
    monkeypatch.setattr(
        "src.scrapers.ossinsight.datetime",
        SimpleNamespace(now=lambda tz=None: fixed_now, timezone=timezone),
    )

    scraper = OSSInsightScraper(
        OSSInsightConfig(enabled=True, period="past_24_hours"),
        MagicMock(),
    )
    item = scraper._row_to_item(
        {
            "repo_name": "org/repo",
            "repo_id": 1,
            "stars": 42,
            "description": "vision toolkit",
        },
        "Python",
    )

    assert item is not None
    assert item.published_at == fixed_now - timedelta(hours=24)


def test_period_start_falls_back_to_24_hours_for_unknown_period(monkeypatch):
    fixed_now = datetime(2026, 8, 24, 12, 0, tzinfo=timezone.utc)
    monkeypatch.setattr(
        "src.scrapers.ossinsight.datetime",
        SimpleNamespace(now=lambda tz=None: fixed_now, timezone=timezone),
    )

    scraper = OSSInsightScraper(
        OSSInsightConfig(enabled=True, period="unknown_period"),
        MagicMock(),
    )

    assert scraper._period_start() == fixed_now - timedelta(hours=24)
