"""Tests for the quarterly HUST AIA faculty profile refresh."""

import json
from datetime import date
from pathlib import Path

from src.models import Config
from src.services.hust_aia_profile import (
    assign_research_groups,
    discover_listing_pages,
    extract_research_direction,
    main,
    parse_faculty_cards,
    profile_is_due,
)


def test_extract_research_direction_from_college_profile() -> None:
    text = (
        "研究方向：工业互联网、工业人工智能、数字孪生 "
        "个人简介 周某长期从事相关研究"
    )

    assert (
        extract_research_direction(text)
        == "工业互联网、工业人工智能、数字孪生"
    )


def test_extract_research_direction_from_faculty_homepage() -> None:
    text = (
        "研究方向 Research focus 计算机视觉 导航与制导 智能医学 "
        "团队成员 查看更多"
    )

    assert (
        extract_research_direction(text)
        == "计算机视觉 导航与制导 智能医学"
    )


def test_parse_cards_and_discover_pagination() -> None:
    html = """
    <a href="zzznyznkzx/1.htm">尾页</a>
    <a href="../../../info/1599/10423.htm">
      <h2>邓忠华</h2>
      <div class="zhai">研究方向：智能控制 个人简介</div>
    </a>
    """
    base = (
        "https://aia.hust.edu.cn/szdw/xysz/axlb/"
        "zzznyznkzx.htm"
    )

    pages = discover_listing_pages(html, base)
    cards = parse_faculty_cards(html, base, "自主智能与智能控制系")

    assert pages == [
        base,
        "https://aia.hust.edu.cn/szdw/xysz/axlb/zzznyznkzx/1.htm",
    ]
    assert cards[0].name == "邓忠华"
    assert cards[0].profile_url == (
        "https://aia.hust.edu.cn/info/1599/10423.htm"
    )


def test_assign_research_groups_uses_configured_keywords() -> None:
    sources = [
        {
            "metadata": {
                "research_group": "robotics",
                "match_keywords": ["机器人", "无人系统"],
            }
        },
        {
            "metadata": {
                "research_group": "vision",
                "match_keywords": ["计算机视觉", "图像"],
            }
        },
    ]

    assert assign_research_groups(
        "机器人控制、无人系统计算机视觉导航", sources
    ) == ["robotics", "vision"]


def test_extract_research_direction_rejects_affiliation_noise() -> None:
    text = "研究方向 社会兼职 Social Affiliations 暂无内容 团队成员 查看更多"

    assert extract_research_direction(text) is None


def test_profile_is_due_uses_stored_review_date(tmp_path: Path) -> None:
    missing = tmp_path / "missing.json"
    due_file = tmp_path / "due.json"
    due_file.write_text(
        json.dumps({"next_review_due": "2026-11-22"}), encoding="utf-8"
    )

    assert profile_is_due(missing, today=date(2026, 8, 24)) is True
    assert profile_is_due(due_file, today=date(2026, 11, 21)) is False
    assert profile_is_due(due_file, today=date(2026, 11, 22)) is True


def test_main_skips_refresh_before_due_date(tmp_path: Path, capsys) -> None:
    profile = tmp_path / "profile.json"
    profile.write_text(
        json.dumps({"next_review_due": "2099-01-01"}), encoding="utf-8"
    )

    assert (
        main(
            [
                "--profile",
                str(profile),
                "--config",
                "data/config.github.json",
            ]
        )
        == 0
    )
    assert "not due yet" in capsys.readouterr().out


def test_github_config_loads_hust_radar_without_csig() -> None:
    config = Config.model_validate(
        json.loads(Path("data/config.github.json").read_text(encoding="utf-8"))
    )
    hust = [source for source in config.sources.rss if source.category == "hust-aia"]

    assert len(hust) == 8
    assert all(source.metadata.get("related_teachers") for source in hust)
    assert all(source.category != "csig-camera" for source in config.sources.rss)
    assert "hust-aia" in config.filtering.category_groups["hust_aia"].categories
    assert "csig_camera" not in config.filtering.category_groups
