#!/usr/bin/env python3
"""Create or update one numbered entry in an Obsidian daily learning note."""

from __future__ import annotations

import argparse
import re
import tempfile
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


REQUIRED_SECTIONS = (
    "## .raw Wikilink 表",
    "## Wiki source/entity 表",
    "## 可读核心要点",
    "## 复习路径",
)


def current_shanghai_date() -> str:
    return datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")


def extract_heading(source: str) -> str:
    match = re.search(r"(?m)^## .+$", source)
    if not match:
        raise ValueError("source must contain a level-2 heading used as its identity")
    return match.group(0)


def validate_source(source: str) -> None:
    if not source.startswith("# {{ENTRY_NUMBER}}\n"):
        raise ValueError("source must start with '# {{ENTRY_NUMBER}}'")
    missing = [section for section in REQUIRED_SECTIONS if section not in source]
    if missing:
        raise ValueError(f"source is missing required sections: {', '.join(missing)}")


def entry_pattern(heading: str) -> re.Pattern[str]:
    return re.compile(
        rf"(?ms)^# (?P<number>\d+)[^\S\r\n]*\r?\n\r?\n"
        rf"(?={re.escape(heading)}[^\S\r\n]*$)"
        rf".*?(?=^# \d+[^\S\r\n]*$|\Z)"
    )


def upsert_entry(existing: str, source: str) -> tuple[str, int, str]:
    validate_source(source)
    heading = extract_heading(source)
    match = entry_pattern(heading).search(existing)

    if match:
        number = int(match.group("number"))
        rendered = source.replace("{{ENTRY_NUMBER}}", str(number), 1).rstrip()
        tail = existing[match.end():]
        separator = "\n\n" if tail else "\n"
        updated = existing[: match.start()] + rendered + separator + tail
        return updated, number, "updated"

    numbers = [int(value) for value in re.findall(r"(?m)^# (\d+)\s*$", existing)]
    number = max(numbers, default=0) + 1
    rendered = source.replace("{{ENTRY_NUMBER}}", str(number), 1).rstrip()
    separator = "\n\n" if existing and not existing.endswith("\n\n") else ""
    return existing + separator + rendered + "\n", number, "created"


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
    ) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    temporary.replace(path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upsert a numbered retrospective into an Obsidian daily note."
    )
    parser.add_argument("--vault", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--date", default=current_shanghai_date())
    parser.add_argument("--target-dir", default="其他/每日自主学习")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.read_text(encoding="utf-8")
    target = args.vault / args.target_dir / f"{args.date}.md"
    existing = target.read_text(encoding="utf-8") if target.exists() else ""
    updated, number, action = upsert_entry(existing, source)

    if args.dry_run:
        print(f"dry-run: would {action} entry #{number} in {target}")
        return 0

    atomic_write(target, updated)
    print(f"{action} entry #{number} in {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
