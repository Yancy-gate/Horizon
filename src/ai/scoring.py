"""Shared helpers for AI score filtering and unscored pass-through."""

from __future__ import annotations

from ..models import ContentItem

UNSCORED_PREFIX = "Unscored:"


def mark_unscored(item: ContentItem, reason: str) -> None:
    """Mark an item as unscored so it can pass threshold filtering."""
    item.ai_score = None
    item.ai_reason = f"{UNSCORED_PREFIX} {reason}"
    item.ai_summary = item.title
    item.ai_tags = []


def is_unscored_failure(item: ContentItem) -> bool:
    """Return True when analysis failed and the item was marked unscored."""
    return bool(item.ai_reason and item.ai_reason.startswith(UNSCORED_PREFIX))


def passes_ai_score_threshold(item: ContentItem, threshold: float) -> bool:
    """Return True if an item should pass score-based filtering."""
    if item.ai_score is not None:
        return item.ai_score >= threshold
    return is_unscored_failure(item)
