"""Daily summary generation — pure programmatic rendering."""

import re
from typing import List, Optional

from ..models import ContentItem
from ..preference_radar.models import HUST_RESEARCH_CATEGORY, PREFERENCE_RADAR_CATEGORY


LEGACY_HUST_RESEARCH_CATEGORY = "hust-aia"
HUST_RESEARCH_CATEGORIES = {HUST_RESEARCH_CATEGORY, LEGACY_HUST_RESEARCH_CATEGORY}


_CJK = r"[\u4e00-\u9fff\u3400-\u4dbf]"
_ASCII = r"[A-Za-z0-9]"


def _pangu(text: str) -> str:
    """Insert a space between CJK and ASCII letters/digits (Pangu spacing)."""
    text = re.sub(rf"({_CJK})({_ASCII})", r"\1 \2", text)
    text = re.sub(rf"({_ASCII})({_CJK})", r"\1 \2", text)
    return text


LABELS = {
    "en": {
        "header": "Horizon Daily",
        "source": "Source",
        "background": "Background",
        "discussion": "Discussion",
        "references": "References",
        "tags": "Tags",
        "selected_items": "From {total} items, {selected} important content pieces were selected",
        "empty_analyzed": "Analyzed {total} items, but none met the importance threshold.",
        "empty_body": (
            "No significant developments today. This might indicate:\n"
            "- A quiet day in your tracked sources\n"
            "- The AI score threshold is too high\n"
            "- Your information sources need expansion\n\n"
            "Consider:\n"
            "1. Lowering the `ai_score_threshold` in config.json\n"
            "2. Adding more diverse information sources\n"
            "3. Checking if the AI model is working correctly\n"
        ),
        "preference_section_title": "Preference Radar",
        "preference_section_blurb": (
            "Personalized picks from your maintained preference profile "
            "(data/preference-radar/profile.json)."
        ),
        "preference_section_empty": "No preference-matched updates today.",
        "hust_section_title": "HUST Research Directions",
        "hust_section_blurb": (
            "Research highlights matched to public faculty directions at HUST's "
            "School of Artificial Intelligence and Automation."
        ),
        "match_reason": "Match",
        "related_faculty": "Related faculty",
        "general_toc_title": "Other highlights",
    },
    "zh": {
        "header": "Horizon 每日速递",
        "source": "来源",
        "background": "背景",
        "discussion": "社区讨论",
        "references": "参考链接",
        "tags": "标签",
        "selected_items": "从 {total} 条内容中筛选出 {selected} 条重要资讯。",
        "empty_analyzed": "已分析 {total} 条内容，但没有达到重要性阈值的条目。",
        "empty_body": (
            "今日暂无重要动态，可能原因：\n"
            "- 今天关注的信息源较平静\n"
            "- AI 评分阈值设置过高\n"
            "- 信息源种类有待扩充\n\n"
            "建议：\n"
            "1. 在 config.json 中降低 `ai_score_threshold`\n"
            "2. 添加更多多样化的信息源\n"
            "3. 检查 AI 模型是否正常工作\n"
        ),
        "preference_section_title": "偏好雷达",
        "preference_section_blurb": (
            "基于你维护的偏好档案（data/preference-radar/profile.json）"
            "独立筛选的个性化内容。"
        ),
        "preference_section_empty": "今日暂无符合偏好的更新。",
        "hust_section_title": "华科老师研究方向",
        "hust_section_blurb": "依据学院教师公开研究方向与论文关键词筛选。",
        "match_reason": "匹配依据",
        "related_faculty": "关联教师",
        "general_toc_title": "其他资讯",
    },
}


class DailySummarizer:
    """Generates daily Markdown summaries from pre-analyzed content items."""

    def __init__(self):
        pass

    @staticmethod
    def _split_sidecar_items(
        items: List[ContentItem],
    ) -> tuple[List[ContentItem], List[ContentItem], List[ContentItem]]:
        """Split main digest items from preference and HUST sidecar items."""
        preference: List[ContentItem] = []
        hust: List[ContentItem] = []
        rest: List[ContentItem] = []
        for item in items:
            category = item.metadata.get("category")
            if category == PREFERENCE_RADAR_CATEGORY:
                preference.append(item)
            elif category in HUST_RESEARCH_CATEGORIES:
                hust.append(item)
            else:
                rest.append(item)
        return preference, hust, rest

    def _toc_line(self, item: ContentItem, language: str, index: int) -> str:
        _t = item.metadata.get(f"title_{language}") or item.title
        t = str(_t).replace("[", "(").replace("]", ")")
        if language == "zh":
            t = _pangu(t)
        score = item.ai_score or "?"
        return f"{index}. [{t}](#item-{index}) \u2b50\ufe0f {score}/10"

    def _render_section(
        self,
        *,
        title_key: str,
        blurb_key: str,
        empty_key: str,
        section_items: List[ContentItem],
        labels: dict,
        language: str,
        start_index: int,
        always_show: bool = False,
        section_slug: str = "other",
    ) -> tuple[str, int]:
        """Render a named digest section; returns markdown and next index."""
        if not section_items and not always_show:
            return "", start_index

        lines = [
            f"## {labels[title_key]}",
            "",
            f"> {labels[blurb_key]}",
            "",
        ]
        if not section_items:
            lines.append(labels[empty_key])
            lines.append("")
            lines.append("---")
            lines.append("")
            return "\n".join(lines), start_index

        toc_entries = [
            self._toc_line(item, language, start_index + i)
            for i, item in enumerate(section_items)
        ]
        lines.extend(toc_entries)
        lines.append("")
        lines.append("---")
        lines.append("")
        body = "".join(
            self._format_item(
                item,
                labels,
                language,
                start_index + i,
                section_slug=section_slug,
            )
            for i, item in enumerate(section_items)
        )
        return "\n".join(lines) + body, start_index + len(section_items)

    async def generate_summary(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
        *,
        preference_items: Optional[List[ContentItem]] = None,
        hust_items: Optional[List[ContentItem]] = None,
    ) -> str:
        """Generate daily summary in Markdown format.

        Layout:
        1. Preference radar (sidecar pipeline)
        2. HUST research directions (external pipeline; hidden when empty)
        3. Other highlights (main balanced digest)

        Args:
            items: Main digest items (already enriched)
            date: Date string (YYYY-MM-DD)
            total_fetched: Total number of items fetched before filtering
            language: Output language, either "en" or "zh"
            preference_items: Optional override for preference radar block
            hust_items: Optional override for HUST research block

        Returns:
            str: Markdown formatted summary
        """
        labels = LABELS.get(language, LABELS["en"])

        embedded_preference, embedded_hust, rest_items = self._split_sidecar_items(items)
        pref_items = preference_items if preference_items is not None else embedded_preference
        hust_section_items = hust_items if hust_items is not None else embedded_hust

        selected_count = len(pref_items) + len(hust_section_items) + len(rest_items)

        header = (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['selected_items'].format(total=total_fetched, selected=selected_count)}\n\n"
            "---\n\n"
        )

        next_index = 1
        pref_md, next_index = self._render_section(
            title_key="preference_section_title",
            blurb_key="preference_section_blurb",
            empty_key="preference_section_empty",
            section_items=pref_items,
            labels=labels,
            language=language,
            start_index=next_index,
            always_show=True,
            section_slug=PREFERENCE_RADAR_CATEGORY,
        )
        hust_md, next_index = self._render_section(
            title_key="hust_section_title",
            blurb_key="hust_section_blurb",
            empty_key="preference_section_empty",
            section_items=hust_section_items,
            labels=labels,
            language=language,
            start_index=next_index,
            always_show=False,
            section_slug=HUST_RESEARCH_CATEGORY,
        )

        if not items and not pref_items and not hust_section_items:
            return (
                f"# {labels['header']} - {date}\n\n"
                f"> {labels['empty_analyzed'].format(total=total_fetched)}\n\n"
                "---\n\n"
                + pref_md
                + labels["empty_body"]
            )

        if not rest_items:
            return header + pref_md + hust_md

        toc_entries = [
            self._toc_line(item, language, next_index + i)
            for i, item in enumerate(rest_items)
        ]
        toc = (
            f"## {labels['general_toc_title']}\n\n"
            + "\n".join(toc_entries)
            + "\n\n---\n\n"
        )
        parts = [
            self._format_item(
                item,
                labels,
                language,
                next_index + i,
                section_slug="other",
            )
            for i, item in enumerate(rest_items)
        ]

        return header + pref_md + hust_md + toc + "".join(parts)

    def generate_webhook_overview(
        self,
        items: List[ContentItem],
        date: str,
        total_fetched: int,
        language: str = "en",
    ) -> str:
        """Generate a compact overview for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        if not items:
            return self._generate_empty_summary(date, total_fetched, labels)

        if language == "zh":
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> 从 {total_fetched} 条内容中筛选出 {len(items)} 条重要资讯。\n\n"
                "下面会按新闻逐条发送详情，你可以只看感兴趣的标题。\n\n"
            )
        else:
            header = (
                f"# {labels['header']} - {date}\n\n"
                f"> Selected {len(items)} important items from {total_fetched} fetched items.\n\n"
                "Details will be sent item by item so you can read only the topics you care about.\n\n"
            )

        entries = []
        for i, item in enumerate(items, start=1):
            title = str(item.metadata.get(f"title_{language}") or item.title).replace("[", "(").replace("]", ")")
            if language == "zh":
                title = _pangu(title)
            score = item.ai_score or "?"
            entries.append(f"{i}. [{title}]({item.url}) \u2b50\ufe0f {score}/10")

        return header + "\n".join(entries)

    def generate_webhook_item(
        self,
        item: ContentItem,
        language: str,
        index: int,
        total: int,
    ) -> str:
        """Generate one item message for multi-message webhook delivery."""
        labels = LABELS.get(language, LABELS["en"])
        prefix = f"第 {index}/{total} 条\n\n" if language == "zh" else f"Item {index}/{total}\n\n"
        return prefix + self._format_item(item, labels, language, index).rstrip("-\n ")

    def _format_item(
        self,
        item: ContentItem,
        labels: dict,
        language: str,
        index: int,
        *,
        section_slug: str = "other",
    ) -> str:
        """Format a single ContentItem into Markdown."""
        _title = item.metadata.get(f"title_{language}") or item.title
        title = str(_title).replace("[", "(").replace("]", ")")
        url = str(item.url)
        score = item.ai_score or "?"
        meta = item.metadata
        tag_list = item.ai_tags or []
        tags_attr = ",".join(tag.replace('"', "") for tag in tag_list)
        title_attr = str(_title).replace('"', "&quot;")

        summary = (
            meta.get(f"detailed_summary_{language}")
            or meta.get("detailed_summary")
            or item.ai_summary
            or ""
        )
        background = meta.get(f"background_{language}") or meta.get("background") or ""
        discussion = (
            meta.get(f"community_discussion_{language}")
            or meta.get("community_discussion")
            or ""
        )

        if language == "zh":
            title = _pangu(title)
            summary = _pangu(summary)
            background = _pangu(background)
            discussion = _pangu(discussion)

        # Source line with parts joined by " · ", link appended at end
        source_type = item.source_type.value
        source_parts = [source_type]
        if meta.get("subreddit"):
            source_parts.append(f"r/{meta['subreddit']}")
        if meta.get("feed_name"):
            source_parts.append(meta["feed_name"])
        else:
            source_parts.append(item.author or "unknown")
        if item.published_at:
            if language == "zh":
                source_parts.append(
                    f"{item.published_at.month}月{item.published_at.day}日 "
                    f"{item.published_at:%H:%M}"
                )
            else:
                day = item.published_at.strftime("%d").lstrip("0")
                source_parts.append(item.published_at.strftime(f"%b {day}, %H:%M"))
        source_line = " \u00b7 ".join(source_parts)  # ·

        discussion_url = meta.get("discussion_url")
        if discussion_url:
            discussion_url = str(discussion_url)
            if discussion_url != url:
                source_line += f' · [{labels["discussion"]}]({discussion_url})'

        lines = [
            (
                f'<a id="item-{index}" class="hz-item-anchor" '
                f'data-hz-url="{url}" data-hz-title="{title_attr}" '
                f'data-hz-tags="{tags_attr}" data-hz-section="{section_slug}"></a>'
            ),
            f"## [{title}]({url}) \u2b50\ufe0f {score}/10",  # ⭐️
            "",
            summary,
            "",
            source_line,
        ]

        if meta.get("category") in HUST_RESEARCH_CATEGORIES:
            direction = str(meta.get("research_direction") or "")
            if direction:
                matched = str(meta.get("matched_paper_keyword") or "").strip()
                if matched:
                    reason = (
                        f"Paper keyword **{matched}** matched under **{direction}**."
                        if language == "en"
                        else f"论文关键词命中 **{matched}**（{direction}）。"
                    )
                else:
                    reason = (
                        f"Targeted research feed matched **{direction}**."
                        if language == "en"
                        else f"定向研究检索命中 **{direction}**。"
                    )
                lines.extend(["", f"**{labels['match_reason']}**: {reason}"])
            teachers = [str(name) for name in meta.get("related_teachers", [])]
            if teachers:
                visible = teachers[:8]
                separator = ", " if language == "en" else "、"
                teacher_text = separator.join(visible)
                remaining = len(teachers) - len(visible)
                if remaining:
                    teacher_text += (
                        f" and {remaining} more"
                        if language == "en"
                        else f" 等共 {len(teachers)} 人"
                    )
                lines.extend(["", f"**{labels['related_faculty']}**: {teacher_text}"])

        if background:            lines.append("")
            lines.append(f"**{labels['background']}**: {background}")

        sources = meta.get("sources") or []
        if sources:
            items_html = "".join(f'<li><a href="{s["url"]}">{s["title"]}</a></li>\n' for s in sources)
            lines += [
                "",
                f'<details><summary>{labels["references"]}</summary>\n<ul>\n{items_html}\n</ul>\n</details>',
            ]

        if discussion:
            lines.append("")
            lines.append(f"**{labels['discussion']}**: {discussion}")

        if item.ai_tags:
            tags_str = ", ".join([f"`#{t}`" for t in item.ai_tags])
            lines.append("")
            lines.append(f"**{labels['tags']}**: {tags_str}")

        lines.append("")
        lines.append("---")

        return "\n".join(lines) + "\n\n"

    def _generate_empty_summary(self, date: str, total_fetched: int, labels: dict) -> str:
        """Generate summary when no high-scoring items were found."""
        return (
            f"# {labels['header']} - {date}\n\n"
            f"> {labels['empty_analyzed'].format(total=total_fetched)}\n\n"
            + labels["empty_body"]
        )
