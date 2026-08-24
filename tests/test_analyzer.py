import asyncio
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest

import src.ai.analyzer as analyzer_module
from src.ai.analyzer import AnalysisError, ContentAnalyzer
from src.ai.scoring import passes_ai_score_threshold
from src.models import ContentItem, SourceType


def _make_item(item_id: str) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=f"Item {item_id}",
        url="https://example.com/item",
        published_at=datetime(2026, 4, 26, tzinfo=timezone.utc),
    )


def test_analyze_batch_does_not_sleep_by_default(monkeypatch):
    analyzer = ContentAnalyzer(SimpleNamespace())
    items = [_make_item("rss:test:1"), _make_item("rss:test:2")]
    sleep_calls = []

    async def fake_analyze_item(item):
        item.ai_score = 8.0

    async def fake_sleep(seconds):
        sleep_calls.append(seconds)

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)
    monkeypatch.setattr(analyzer_module.asyncio, "sleep", fake_sleep)

    result = asyncio.run(analyzer.analyze_batch(items))

    assert len(result) == 2
    assert sleep_calls == []


def test_analyze_batch_sleeps_between_items_when_throttle_configured(monkeypatch):
    client = SimpleNamespace(config=SimpleNamespace(throttle_sec=1.5))
    analyzer = ContentAnalyzer(client)
    items = [_make_item("rss:test:1"), _make_item("rss:test:2"), _make_item("rss:test:3")]
    sleep_calls = []

    async def fake_analyze_item(item):
        item.ai_score = 8.0

    async def fake_sleep(seconds):
        sleep_calls.append(seconds)

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)
    monkeypatch.setattr(analyzer_module.asyncio, "sleep", fake_sleep)

    asyncio.run(analyzer.analyze_batch(items))

    assert sleep_calls == [1.5, 1.5]


def test_analyze_batch_concurrent_processing(monkeypatch):
    """Verify that higher concurrency allows overlapping item processing."""
    client = SimpleNamespace(config=SimpleNamespace(analysis_concurrency=3))
    analyzer = ContentAnalyzer(client)
    items = [_make_item(f"rss:test:{i}") for i in range(5)]
    active_count = 0
    max_active = 0

    async def fake_analyze_item(item):
        nonlocal active_count, max_active
        active_count += 1
        max_active = max(max_active, active_count)
        await asyncio.sleep(0.05)  # Small delay to allow overlap
        active_count -= 1

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    asyncio.run(analyzer.analyze_batch(items))

    assert max_active == 3
    assert all(item.ai_score is None for item in items)  # None because fake_analyze_item doesn't set it


def test_analyze_batch_concurrent_preserves_order(monkeypatch):
    """Verify that analyze_batch preserves input order in results."""
    client = SimpleNamespace(config=SimpleNamespace(analysis_concurrency=3))
    analyzer = ContentAnalyzer(client)
    items = [_make_item(f"rss:test:{i}") for i in range(5)]

    async def fake_analyze_item(item):
        item.ai_score = float(item.id.split(":")[-1]) * 10

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    result = asyncio.run(analyzer.analyze_batch(items))

    assert [item.id for item in result] == [item.id for item in items]


def test_analyze_batch_allows_failures_at_configured_ratio(monkeypatch):
    client = SimpleNamespace(
        config=SimpleNamespace(max_analysis_failure_ratio=0.2)
    )
    analyzer = ContentAnalyzer(client)
    items = [_make_item(f"rss:test:{i}") for i in range(5)]

    async def fake_analyze_item(item):
        if item.id.endswith(":0"):
            raise RuntimeError("provider unavailable")
        item.ai_score = 8.0

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    result = asyncio.run(analyzer.analyze_batch(items))

    assert len(result) == 5
    assert result[0].ai_score is None
    assert result[0].ai_reason == "Unscored: analysis failed"


def test_analyze_batch_marks_parse_failures_as_unscored(monkeypatch):
    client = SimpleNamespace(
        config=SimpleNamespace(max_analysis_failure_ratio=1.0)
    )
    analyzer = ContentAnalyzer(client)
    items = [_make_item("rss:test:0")]

    async def fake_analyze_item(item):
        raise AnalysisError("response parse failed")

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    result = asyncio.run(analyzer.analyze_batch(items))

    assert result[0].ai_score is None
    assert result[0].ai_reason == "Unscored: response parse failed"


def test_passes_ai_score_threshold_allows_unscored_items():
    item = _make_item("rss:test:1")
    item.ai_score = None
    item.ai_reason = "Unscored: analysis failed"

    assert passes_ai_score_threshold(item, 7.0) is True


def test_passes_ai_score_threshold_rejects_low_scores():
    item = _make_item("rss:test:1")
    item.ai_score = 4.0
    item.ai_reason = "Low relevance"

    assert passes_ai_score_threshold(item, 5.0) is False


def test_passes_ai_score_threshold_rejects_unanalyzed_items():
    item = _make_item("rss:test:1")

    assert passes_ai_score_threshold(item, 5.0) is False


def test_analyze_item_truncates_content_and_comments():
    client = SimpleNamespace()

    async def fake_complete(*, system, user):
        fake_complete.captured_user = user
        return '{"score": 8, "reason": "ok", "summary": "s", "tags": []}'

    client.complete = fake_complete
    analyzer = ContentAnalyzer(client)
    long_body = "A" * 2000
    long_comments = "C" * 2500
    item = ContentItem(
        id="rss:test:long",
        source_type=SourceType.RSS,
        title="Long item",
        url="https://example.com/long",
        published_at=datetime(2026, 4, 26, tzinfo=timezone.utc),
        content=f"{long_body}\n\n--- Top Comments ---\n{long_comments}",
    )

    asyncio.run(analyzer._analyze_item(item))

    user_prompt = fake_complete.captured_user
    assert f"Content: {'A' * 1500}" in user_prompt
    assert f"Community Comments:\n{'C' * 2000}" in user_prompt
    assert "A" * 1501 not in user_prompt


def test_analyze_batch_stops_when_failure_ratio_exceeds_limit(monkeypatch):
    client = SimpleNamespace(
        config=SimpleNamespace(max_analysis_failure_ratio=0.2)
    )
    analyzer = ContentAnalyzer(client)
    items = [_make_item(f"rss:test:{i}") for i in range(5)]

    async def fake_analyze_item(item):
        if item.id.endswith((":0", ":1")):
            raise RuntimeError("provider unavailable")
        item.ai_score = 8.0

    monkeypatch.setattr(analyzer, "_analyze_item", fake_analyze_item)

    with pytest.raises(
        RuntimeError,
        match=r"2/5 \(40\.0%\) > 20\.0%",
    ):
        asyncio.run(analyzer.analyze_batch(items))
