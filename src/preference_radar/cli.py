"""CLI for preference radar document ingestion."""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

from ..models import Config
from ..storage.manager import ConfigError, StorageManager
from .ingest import PreferenceIngestService
from .feedback import FeedbackService
from .storage import PreferenceRadarStorage


console = Console()


def _load_config(data_dir: Path) -> Config:
    storage = StorageManager(data_dir=str(data_dir))
    return storage.load_config()


def _print_draft_summary(draft) -> None:
    console.print(f"\n[bold cyan]Draft[/bold cyan] [dim]{draft.draft_id}[/dim]")
    console.print(f"Summary: {draft.summary}")
    if draft.proposed.interests:
        console.print("Interests:", ", ".join(draft.proposed.interests))
    if draft.proposed.raw_keywords:
        console.print("Keywords:", ", ".join(draft.proposed.raw_keywords))
    if draft.proposed.google_news_queries:
        console.print(
            "Queries:",
            "; ".join(q.query for q in draft.proposed.google_news_queries),
        )
    if draft.persona_summary_after:
        console.print(f"Persona after apply: {draft.persona_summary_after}")
    console.print(
        f"\nReview draft file, then apply:\n"
        f"  [cyan]uv run horizon-preference-ingest --apply {draft.draft_id}[/cyan]\n"
    )


async def _run_async(args: argparse.Namespace) -> int:
    config = _load_config(Path("data"))
    storage = PreferenceRadarStorage()
    storage.ensure_layout()
    service = PreferenceIngestService(config, storage)

    if args.apply_feedback:
        result = FeedbackService(storage).apply_pending()
        console.print(
            f"[green]Applied {result.applied} feedback entries[/green] — "
            f"+{result.interests_added} interests, "
            f"+{result.keywords_added} keywords, "
            f"+{result.negative_added} negative."
        )
        return 0

    if args.import_feedback_inbox:
        imported = FeedbackService(storage).import_inbox_exports()
        result = FeedbackService(storage).apply_pending()
        console.print(
            f"[green]Imported {imported} feedback entries[/green], "
            f"applied {result.applied}."
        )
        return 0

    if args.import_feedback:
        path = Path(args.import_feedback)
        if not path.exists():
            console.print(f"[red]File not found: {path}[/red]")
            return 1
        imported = FeedbackService(storage).import_file(str(path))
        result = FeedbackService(storage).apply_pending()
        console.print(
            f"[green]Imported {imported} feedback entries[/green], "
            f"applied {result.applied}."
        )
        return 0

    if args.list_drafts:
        drafts = storage.list_drafts()
        if not drafts:
            console.print("No pending drafts.")
            return 0
        table = Table("Draft ID", "Path")
        for path in drafts:
            table.add_row(path.stem, str(path))
        console.print(table)
        return 0

    if args.apply:
        entry = service.apply_draft(args.apply)
        console.print(
            f"[green]Applied draft {entry.draft_id}[/green] — "
            f"+{len(entry.interests_added)} interests, "
            f"+{len(entry.keywords_added)} keywords, "
            f"+{len(entry.queries_added)} queries."
        )
        return 0

    if args.inbox:
        drafts = await service.process_inbox()
        if not drafts:
            console.print("Inbox is empty.")
            return 0
        for draft in drafts:
            _print_draft_summary(draft)
        return 0

    if args.file:
        path = Path(args.file)
        if not path.exists():
            console.print(f"[red]File not found: {path}[/red]")
            return 1
        draft = await service.create_draft_from_file(path)
        _print_draft_summary(draft)
        return 0

    if args.text:
        draft = await service.create_draft_from_text(
            filename="chat-input.txt",
            content=args.text,
            source_path="chat",
        )
        _print_draft_summary(draft)
        return 0

    console.print(
        "Use --inbox, --file, --text, --apply, --list-drafts, "
        "--import-feedback, --import-feedback-inbox, or --apply-feedback."
    )
    return 1


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Horizon preference radar ingest — draft preference updates from documents",
    )
    parser.add_argument("--inbox", action="store_true", help="Process all files in data/preference-radar/inbox/")
    parser.add_argument("--file", type=str, help="Process one document file")
    parser.add_argument("--text", type=str, help="Process inline text (chat-style input)")
    parser.add_argument("--apply", type=str, metavar="DRAFT_ID", help="Apply a confirmed draft")
    parser.add_argument("--list-drafts", action="store_true", help="List pending drafts")
    parser.add_argument(
        "--import-feedback",
        type=str,
        metavar="FILE",
        help="Import a browser feedback export JSON into feedback.jsonl and apply",
    )
    parser.add_argument(
        "--import-feedback-inbox",
        action="store_true",
        help="Import all JSON files from data/preference-radar/feedback-inbox/",
    )
    parser.add_argument(
        "--apply-feedback",
        action="store_true",
        help="Apply pending rows from feedback.jsonl to profile.json",
    )
    args = parser.parse_args()

    try:
        raise SystemExit(asyncio.run(_run_async(args)))
    except ConfigError as exc:
        console.print(f"[red]Config error: {exc}[/red]")
        raise SystemExit(1) from exc
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted[/yellow]")
        raise SystemExit(130)


if __name__ == "__main__":
    main()
