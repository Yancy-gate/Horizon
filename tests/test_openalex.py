from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock, MagicMock

from src.models import OpenAlexAuthorQuery, OpenAlexConfig
from src.scrapers.openalex import OpenAlexScraper, reconstruct_abstract

SINCE = datetime(2026, 7, 1, tzinfo=timezone.utc)


def _mock_client(payload: dict) -> AsyncMock:
    response = MagicMock()
    response.json.return_value = payload
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    return client


def _query() -> OpenAlexAuthorQuery:
    return OpenAlexAuthorQuery(
        name="华科 AIA 期刊 · 能源电子与智能制造",
        author_ids=["A5082169962", "A5102832799"],
        category="hust-aia",
        metadata={
            "research_direction": "能源电子与智能制造",
            "content_match_keywords": ["PMSM", "sensorless", "microgrid"],
        },
        max_items=10,
    )


def test_reconstruct_abstract_orders_tokens() -> None:
    assert (
        reconstruct_abstract({"sensorless": [1], "PMSM": [0], "control": [2]})
        == "PMSM sensorless control"
    )


def test_openalex_keeps_faculty_ieee_paper_and_drops_off_topic() -> None:
    payload = {
        "results": [
            {
                "id": "https://openalex.org/W111",
                "doi": "https://doi.org/10.1109/tec.2026.1",
                "display_name": "Minimum-Delay Deadbeat Predictive Current Control for SPMSM Drives",
                "publication_date": "2026-08-01",
                "authorships": [
                    {"author": {"display_name": "Anwen Shen"}},
                    {"author": {"display_name": "Qipeng Tang"}},
                ],
                "primary_location": {
                    "landing_page_url": "https://doi.org/10.1109/tec.2026.1",
                    "source": {"display_name": "IEEE JESTPE"},
                },
                "abstract_inverted_index": {
                    "SPMSM": [0],
                    "sensorless": [1],
                    "control": [2],
                },
            },
            {
                "id": "https://openalex.org/W333",
                "doi": "https://doi.org/10.1109/tec.2026.1",
                "display_name": "Duplicate DOI of the SPMSM paper",
                "publication_date": "2026-08-01",
                "authorships": [{"author": {"display_name": "Anwen Shen"}}],
                "primary_location": {
                    "landing_page_url": "https://doi.org/10.1109/tec.2026.1"
                },
                "abstract_inverted_index": {"PMSM": [0]},
            },
            {
                "id": "https://openalex.org/W222",
                "doi": "https://doi.org/10.1016/unrelated",
                "display_name": "Peritoneal remodeling in patients with liver cirrhosis",
                "publication_date": "2026-08-02",
                "authorships": [{"author": {"display_name": "Quan Yin"}}],
                "primary_location": {
                    "landing_page_url": "https://doi.org/10.1016/unrelated"
                },
            },
        ]
    }
    client = _mock_client(payload)
    scraper = OpenAlexScraper(OpenAlexConfig(enabled=True, queries=[_query()]), client)

    items = asyncio.run(scraper.fetch(SINCE))

    assert [item.title for item in items] == [
        "Minimum-Delay Deadbeat Predictive Current Control for SPMSM Drives"
    ]
    assert items[0].metadata["matched_paper_keyword"] == "PMSM"
    assert items[0].metadata["category"] == "hust-aia"
    params = client.get.call_args.kwargs["params"]
    assert "author.id:A5082169962|A5102832799" in params["filter"]
    assert "from_publication_date:2026-07-01" in params["filter"]


def test_openalex_disabled_returns_empty() -> None:
    client = _mock_client({"results": []})
    scraper = OpenAlexScraper(
        OpenAlexConfig(enabled=False, queries=[_query()]), client
    )
    assert asyncio.run(scraper.fetch(SINCE)) == []
    client.get.assert_not_called()
