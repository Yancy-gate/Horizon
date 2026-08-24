import importlib.util
import subprocess
from pathlib import Path

import pytest


SCRIPT_PATH = (
    Path(__file__).parents[1]
    / ".cursor"
    / "skills"
    / "obsidian-retrospective"
    / "scripts"
    / "sync_remote_file.py"
)
SPEC = importlib.util.spec_from_file_location("sync_remote_file", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def _git(cwd: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(cwd), *args], check=True, capture_output=True)


def test_validate_relative_path_accepts_windows_separators():
    result = MODULE.validate_relative_path(r"其他\每日自主学习\2026-08-24.md")

    assert result.as_posix() == "其他/每日自主学习/2026-08-24.md"


@pytest.mark.parametrize("value", ["/absolute.md", "../escape.md", "a/../../escape.md"])
def test_validate_relative_path_rejects_unsafe_paths(value):
    with pytest.raises(ValueError, match="safe repository-relative"):
        MODULE.validate_relative_path(value)


def test_sync_remote_file_changes_only_requested_worktree_file(tmp_path):
    remote = tmp_path / "remote.git"
    author = tmp_path / "author"
    vault = tmp_path / "vault"
    remote.mkdir()
    author.mkdir()

    _git(remote, "init", "--bare", "--initial-branch=master")
    _git(author, "init", "--initial-branch=master")
    _git(author, "config", "user.name", "Test")
    _git(author, "config", "user.email", "test@example.com")
    (author / "target.md").write_text("version 1\n", encoding="utf-8")
    (author / "unrelated.md").write_text("remote 1\n", encoding="utf-8")
    _git(author, "add", ".")
    _git(author, "commit", "-m", "initial")
    _git(author, "remote", "add", "origin", str(remote))
    _git(author, "push", "-u", "origin", "master")
    subprocess.run(
        ["git", "clone", str(remote), str(vault)],
        check=True,
        capture_output=True,
    )

    (author / "target.md").write_text("version 2\n", encoding="utf-8")
    (author / "unrelated.md").write_text("remote 2\n", encoding="utf-8")
    _git(author, "add", ".")
    _git(author, "commit", "-m", "update both")
    _git(author, "push", "origin", "master")

    (vault / "unrelated.md").write_text("local private edit\n", encoding="utf-8")

    target = MODULE.sync_remote_file(vault, "target.md")

    assert target.read_text(encoding="utf-8") == "version 2\n"
    assert (vault / "unrelated.md").read_text(encoding="utf-8") == "local private edit\n"
    assert subprocess.run(
        ["git", "-C", str(vault), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout != subprocess.run(
        ["git", "-C", str(vault), "rev-parse", "origin/master"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
