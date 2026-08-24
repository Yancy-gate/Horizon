#!/usr/bin/env python3
"""Append one feedback entry from FEEDBACK_ENTRY env (GitHub Actions dispatch)."""

from __future__ import annotations

import json
import os
import sys

from src.preference_radar.models import PreferenceFeedbackEntry
from src.preference_radar.storage import PreferenceRadarStorage


def main() -> int:
    raw = os.environ.get("FEEDBACK_ENTRY", "").strip()
    if not raw:
        print("FEEDBACK_ENTRY is empty", file=sys.stderr)
        return 1

    entry = PreferenceFeedbackEntry.model_validate(json.loads(raw))
    storage = PreferenceRadarStorage()
    storage.ensure_layout()
    storage.append_feedback_entries([entry])
    print(f"Appended feedback for {entry.url} ({entry.rating})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
