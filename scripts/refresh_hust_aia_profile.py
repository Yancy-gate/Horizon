"""Refresh the HUST AIA faculty research profile and radar mappings."""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path

from src.services.hust_aia_profile import refresh_profile_files


def main() -> None:
    parser = argparse.ArgumentParser()
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
    args = parser.parse_args()

    profile = asyncio.run(
        refresh_profile_files(args.config, args.profile)
    )
    print(
        "HUST AIA profile refreshed: "
        f"{profile['included_teacher_count']} included, "
        f"{profile['excluded_without_direction_count']} excluded, "
        f"next review {profile['next_review_due']}"
    )


if __name__ == "__main__":
    main()
