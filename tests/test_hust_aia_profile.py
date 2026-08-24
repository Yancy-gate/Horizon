"""Tests for the quarterly HUST AIA faculty profile refresh."""

from src.services.hust_aia_profile import (
    assign_research_groups,
    discover_listing_pages,
    extract_research_direction,
    parse_faculty_cards,
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
