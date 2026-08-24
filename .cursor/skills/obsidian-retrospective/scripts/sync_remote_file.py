#!/usr/bin/env python3
"""Fetch one file from a remote Git revision without updating the worktree."""

from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path, PurePosixPath


def validate_relative_path(value: str) -> PurePosixPath:
    normalized = value.replace("\\", "/")
    path = PurePosixPath(normalized)
    if path.is_absolute() or not path.parts or ".." in path.parts:
        raise ValueError("path must be a safe repository-relative path")
    return path


def run_git(vault: Path, *args: str, capture: bool = False) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(vault), *args],
        check=False,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {message}")
    return result.stdout if capture else b""


def atomic_write_bytes(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("wb", dir=path.parent, delete=False) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    temporary.replace(path)


def sync_remote_file(
    vault: Path,
    relative_path: str,
    *,
    remote: str = "origin",
    branch: str = "master",
) -> Path:
    if not (vault / ".git").exists():
        raise ValueError(f"vault is not a Git repository: {vault}")

    repo_path = validate_relative_path(relative_path)
    run_git(
        vault,
        "fetch",
        "--filter=blob:none",
        "--no-tags",
        remote,
        branch,
    )
    content = run_git(vault, "show", f"FETCH_HEAD:{repo_path.as_posix()}", capture=True)
    target = vault.joinpath(*repo_path.parts)
    atomic_write_bytes(target, content)
    return target


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch and materialize one remote file without pulling unrelated "
            "vault changes into the local worktree."
        )
    )
    parser.add_argument("--vault", required=True, type=Path)
    parser.add_argument("--path", required=True)
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", default="master")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = sync_remote_file(
        args.vault,
        args.path,
        remote=args.remote,
        branch=args.branch,
    )
    print(f"updated only {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
