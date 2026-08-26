"""Quarterly research-profile refresh for HUST AIA faculty radar."""

from __future__ import annotations

import argparse
import asyncio
import json
import re
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse, urlunparse

import httpx
from bs4 import BeautifulSoup


FACULTY_INDEXES = {
    "自主智能与智能控制系": "https://aia.hust.edu.cn/szdw/xysz/axlb/zzznyznkzx.htm",
    "智能感知与测量科学系": "https://aia.hust.edu.cn/szdw/xysz/axlb/zngzyclkxx.htm",
    "智能系统与系统工程系": "https://aia.hust.edu.cn/szdw/xysz/axlb/znxtyxtgcx.htm",
    "图像识别与智能科学系": "https://aia.hust.edu.cn/szdw/xysz/axlb/txsbyznkxx.htm",
}

_STOP_HEADINGS = (
    "团队成员",
    "个人简介",
    "个人基本情况",
    "教育经历",
    "工作经历",
    "招生",
    "研究成果",
    "论文成果",
    "科学研究",
    "社会兼职",
    "主持",
    "发表",
    "入选",
    "地址：",
    "邮政编码",
    "访问量",
)


@dataclass(frozen=True)
class FacultyCard:
    name: str
    department: str
    profile_url: str
    summary: str = ""


def _compact(text: str) -> str:
    return " ".join(text.replace("\xa0", " ").split())


def _http_faculty_url(url: str) -> str:
    """The faculty site is substantially more reliable over plain HTTP."""
    parsed = urlparse(url)
    if parsed.hostname == "faculty.hust.edu.cn":
        return urlunparse(parsed._replace(scheme="http"))
    return url


def extract_research_direction(text: str) -> str | None:
    """Extract the public research-direction field from a profile or card."""
    text = _compact(text)
    patterns = (
        r"研究方向\s*(?:Research focus\s*)?[：:]?\s*(.+?)\s*(?="
        + "|".join(map(re.escape, _STOP_HEADINGS))
        + r"|$)",
        r"主要研究方向\s*[：:]?\s*(.+?)\s*(?="
        + "|".join(map(re.escape, _STOP_HEADINGS))
        + r"|$)",
    )
    candidates: list[str] = []
    for pattern in patterns:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            value = _compact(match.group(1)).strip("：:，,；;。 ")
            value = value.removeprefix("为").strip()
            invalid = (
                len(value) < 4
                or value in {"暂无内容", "无"}
                or value.startswith(
                    (
                        "社会兼职",
                        "研究方向",
                        "主要研究方向",
                        "团队成员",
                        "Research",
                    )
                )
                or ("发邮件" in value and "研究生" in value)
            )
            if value and not invalid:
                candidates.append(value[:600])
    if not candidates:
        return None
    return min(candidates, key=len)


def parse_faculty_cards(
    html: str, page_url: str, department: str
) -> list[FacultyCard]:
    """Parse faculty cards from one official department listing page."""
    soup = BeautifulSoup(html, "html.parser")
    cards: list[FacultyCard] = []
    for heading in soup.find_all("h2"):
        name = _compact(heading.get_text(" ", strip=True))
        link = heading.find_parent("a", href=True)
        if not link or not (2 <= len(name) <= 8):
            continue
        profile_url = _http_faculty_url(urljoin(page_url, link["href"]))
        summary_node = link.select_one(".zhai")
        summary = (
            _compact(summary_node.get_text(" ", strip=True))
            if summary_node
            else ""
        )
        cards.append(FacultyCard(name, department, profile_url, summary))
    return cards


def discover_listing_pages(html: str, base_url: str) -> list[str]:
    """Return the base listing plus all numbered pagination URLs."""
    soup = BeautifulSoup(html, "html.parser")
    slug = Path(urlparse(base_url).path).stem
    pages = {base_url}
    pattern = re.compile(rf"(?:^|/){re.escape(slug)}/\d+\.htm$")
    for link in soup.select("a[href]"):
        candidate = urljoin(base_url, link["href"])
        if pattern.search(urlparse(candidate).path):
            pages.add(candidate)
    return sorted(pages)


def _research_sources(config: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        source
        for source in config.get("sources", {}).get("rss", [])
        if source.get("category") == "hust-aia"
        and source.get("metadata", {}).get("research_group")
    ]


def assign_research_groups(
    direction: str, sources: list[dict[str, Any]]
) -> list[str]:
    """Assign one public direction to configured radar groups.

    Homepage ``match_keywords`` decide which group a teacher belongs to.
    Item-level ``content_match_keywords`` are not used here; they filter
    fetched news/papers in the RSS scraper.
    """
    normalized = direction.casefold()
    matches = []
    for source in sources:
        metadata = source["metadata"]
        keywords = metadata.get("match_keywords", [])
        if any(str(keyword).casefold() in normalized for keyword in keywords):
            matches.append(str(metadata["research_group"]))
    return matches


def profile_is_due(
    profile_path: Path, today: date | None = None
) -> bool:
    """Return whether a stored profile has reached its next review date."""
    if not profile_path.exists():
        return True
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    due_text = profile.get("next_review_due")
    if not due_text:
        return True
    return (today or datetime.now(timezone.utc).date()) >= date.fromisoformat(
        due_text
    )


class HustAiaProfileRefresher:
    """Scrape official public profiles and update radar teacher mappings."""

    def __init__(self, timeout: float = 15.0, concurrency: int = 8):
        self.timeout = timeout
        self.semaphore = asyncio.Semaphore(concurrency)
        self.headers = {"User-Agent": "Horizon faculty research monitor/1.0"}

    async def _get(self, client: httpx.AsyncClient, url: str) -> str:
        async with self.semaphore:
            last_error: Exception | None = None
            for attempt in range(3):
                try:
                    response = await client.get(url, follow_redirects=True)
                    response.raise_for_status()
                    response.encoding = "utf-8"
                    return response.text
                except (httpx.HTTPError, httpx.TimeoutException) as exc:
                    last_error = exc
                    if attempt < 2:
                        await asyncio.sleep(0.5 * (attempt + 1))
            assert last_error is not None
            raise last_error

    async def _collect_cards(
        self, client: httpx.AsyncClient
    ) -> list[FacultyCard]:
        cards_by_url: dict[str, FacultyCard] = {}
        for department, base_url in FACULTY_INDEXES.items():
            base_html = await self._get(client, base_url)
            pages = discover_listing_pages(base_html, base_url)
            page_html = await asyncio.gather(
                *(self._get(client, page) for page in pages)
            )
            for page, html in zip(pages, page_html):
                for card in parse_faculty_cards(html, page, department):
                    cards_by_url[card.profile_url] = card
        return sorted(cards_by_url.values(), key=lambda card: card.name)

    async def _research_teacher(
        self, client: httpx.AsyncClient, card: FacultyCard
    ) -> dict[str, Any] | None:
        direction = extract_research_direction(card.summary)
        if direction is None:
            try:
                html = await self._get(client, card.profile_url)
            except (httpx.HTTPError, httpx.TimeoutException):
                return None
            text = BeautifulSoup(html, "html.parser").get_text(" ", strip=True)
            direction = extract_research_direction(text)
        if direction is None:
            return None
        return {
            "name": card.name,
            "department": card.department,
            "research_direction": direction,
            "profile_url": card.profile_url,
        }

    async def build_profile(
        self, config: dict[str, Any], now: datetime | None = None
    ) -> dict[str, Any]:
        sources = _research_sources(config)
        if not sources:
            raise ValueError("config has no RSS sources in category 'hust-aia'")

        async with httpx.AsyncClient(
            timeout=self.timeout, headers=self.headers
        ) as client:
            cards = await self._collect_cards(client)
            results = await asyncio.gather(
                *(self._research_teacher(client, card) for card in cards)
            )

        teachers = [teacher for teacher in results if teacher is not None]
        if len(teachers) < 20:
            raise RuntimeError(
                f"only {len(teachers)} faculty research profiles were parsed; "
                "refusing to replace the existing profile"
            )

        group_members: dict[str, list[str]] = {
            source["metadata"]["research_group"]: [] for source in sources
        }
        for teacher in teachers:
            groups = assign_research_groups(
                teacher["research_direction"], sources
            )
            teacher["research_groups"] = groups
            for group in groups:
                group_members[group].append(teacher["name"])

        groups = []
        for source in sources:
            metadata = source["metadata"]
            group_id = metadata["research_group"]
            names = sorted(set(group_members[group_id]))
            metadata["related_teachers"] = names
            groups.append(
                {
                    "id": group_id,
                    "name": metadata["research_direction"],
                    "query": metadata.get("search_query", ""),
                    "match_keywords": metadata.get("match_keywords", []),
                    "teachers": names,
                }
            )

        researched_at = now or datetime.now(timezone.utc)
        return {
            "schema_version": 1,
            "institution": "华中科技大学人工智能与自动化学院",
            "selection_rule": "学院官网中具有公开研究主页且可提取研究方向的教学科研人员",
            "official_index_urls": list(FACULTY_INDEXES.values()),
            "researched_at": researched_at.isoformat(),
            "review_interval_days": 90,
            "next_review_due": (
                researched_at + timedelta(days=90)
            ).date().isoformat(),
            "listed_profile_count": len(cards),
            "included_teacher_count": len(teachers),
            "excluded_without_direction_count": len(cards) - len(teachers),
            "research_groups": groups,
            "teachers": teachers,
        }


async def refresh_profile_files(
    config_path: Path, profile_path: Path, now: datetime | None = None
) -> dict[str, Any]:
    """Refresh profile JSON and teacher metadata in the production config."""
    config = json.loads(config_path.read_text(encoding="utf-8"))
    profile = await HustAiaProfileRefresher().build_profile(config, now=now)
    config_path.write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    profile_path.write_text(
        json.dumps(profile, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return profile


def main(argv: list[str] | None = None) -> int:
    """CLI for the 90-day HUST AIA faculty research refresh."""
    parser = argparse.ArgumentParser(
        description="Refresh the HUST AIA faculty research profile"
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("data/config.github.json"),
    )
    parser.add_argument(
        "--profile",
        type=Path,
        default=Path("data/hust_aia_research_profile.json"),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Refresh even if the 90-day review date has not arrived",
    )
    args = parser.parse_args(argv)

    if not args.force and not profile_is_due(args.profile):
        print(
            "HUST AIA profile is not due yet; skip. "
            "Use --force to refresh now."
        )
        return 0

    profile = asyncio.run(refresh_profile_files(args.config, args.profile))
    print(
        "HUST AIA profile refreshed: "
        f"{profile['included_teacher_count']} included, "
        f"{profile['excluded_without_direction_count']} excluded, "
        f"next review {profile['next_review_due']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
