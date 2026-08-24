from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

from src.models import RSSSourceConfig
from src.scrapers.rss import RSSScraper, match_source_content_filters


def test_rss_ids_are_deterministic() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>entry-1</guid>
        <title>Item 1</title>
        <link>https://example.com/item-1</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
        <description>Hello</description>
      </item>
    </channel></rss>
    """
    response = MagicMock()
    response.text = feed
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], client)
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    first = asyncio.run(scraper.fetch(since))[0].id
    second = asyncio.run(scraper.fetch(since))[0].id

    assert first == second
    assert first == "rss:example.com_feed.xml:5e2d5d1e58e94d76"


def test_rss_source_metadata_is_copied_to_items() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>entry-1</guid>
        <title>Robot control paper</title>
        <link>https://example.com/item-1</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
      </item>
    </channel></rss>
    """
    response = MagicMock()
    response.text = feed
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(
        name="Faculty radar",
        url="https://example.com/feed.xml",
        category="hust-aia",
        metadata={
            "research_direction": "机器人与自主智能",
            "related_teachers": ["何顶新"],
        },
    )

    item = asyncio.run(
        RSSScraper([source], client).fetch(
            datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)
        )
    )[0]

    assert item.metadata["research_direction"] == "机器人与自主智能"
    assert item.metadata["related_teachers"] == ["何顶新"]
    assert item.metadata["category"] == "hust-aia"


def test_match_source_content_filters_requires_paper_keyword() -> None:
    metadata = {
        "content_match_keywords": ["infrared small target", "人群计数", "scene text"]
    }

    assert (
        match_source_content_filters(
            "Infrared Small Target Detection via Nested U-Net",
            "A new method for dim target detection.",
            metadata,
        )
        == "infrared small target"
    )
    assert (
        match_source_content_filters(
            "Generic object detection benchmark released",
            "YOLO beats two-stage detectors again.",
            metadata,
        )
        is None
    )
    assert match_source_content_filters("Anything", "body", {}) == ""


def test_rss_drops_items_missing_paper_keywords() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>keep-1</guid>
        <title>Scene text recognition with a new decoder</title>
        <link>https://example.com/keep</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
      </item>
      <item>
        <guid>drop-1</guid>
        <title>Computer vision object detection survey</title>
        <link>https://example.com/drop</link>
        <pubDate>Fri, 24 Apr 2026 13:00:00 GMT</pubDate>
      </item>
    </channel></rss>
    """
    response = MagicMock()
    response.text = feed
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(
        name="Faculty radar",
        url="https://example.com/feed.xml",
        category="hust-aia",
        metadata={
            "research_direction": "计算机视觉与多模态感知",
            "content_match_keywords": ["scene text", "crowd counting"],
        },
    )

    items = asyncio.run(
        RSSScraper([source], client).fetch(
            datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)
        )
    )

    assert [item.title for item in items] == [
        "Scene text recognition with a new decoder"
    ]
    assert items[0].metadata["matched_paper_keyword"] == "scene text"
