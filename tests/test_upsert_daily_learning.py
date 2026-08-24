import importlib.util
from pathlib import Path

import pytest


SCRIPT_PATH = (
    Path(__file__).parents[1]
    / ".cursor"
    / "skills"
    / "obsidian-retrospective"
    / "scripts"
    / "upsert_daily_learning.py"
)
SPEC = importlib.util.spec_from_file_location("upsert_daily_learning", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def _source(body: str = "正文") -> str:
    return f"""# {{{{ENTRY_NUMBER}}}}

## 唯一复盘标题

{body}

## .raw Wikilink 表

| Wikilink |
|---|
| [[原始资料]] |

## Wiki source/entity 表

| Source | Entity |
|---|---|
| [[来源]] | [[实体]] |

## 可读核心要点

| 概念 | 要点 |
|---|---|
| 幂等 | 重复执行结果一致 |

## 复习路径

1. 复述根因。
"""


def test_upsert_creates_next_numbered_entry():
    existing = "# 1\n\n## 旧条目\n\n旧内容\n"

    updated, number, action = MODULE.upsert_entry(existing, _source())

    assert action == "created"
    assert number == 2
    assert updated.startswith(existing + "\n# 2\n")
    assert "{{ENTRY_NUMBER}}" not in updated


def test_upsert_updates_matching_entry_and_preserves_following_entries():
    existing = (
        "# 1\n\n## 唯一复盘标题\n\n旧正文\n\n"
        "# 2\n\n## 后续条目\n\n必须保留\n"
    )

    updated, number, action = MODULE.upsert_entry(existing, _source("新正文"))

    assert action == "updated"
    assert number == 1
    assert "新正文" in updated
    assert "旧正文" not in updated
    assert "# 2\n\n## 后续条目\n\n必须保留" in updated
    assert updated.count("## 唯一复盘标题") == 1


def test_upsert_is_idempotent_for_same_source():
    first, _, _ = MODULE.upsert_entry("", _source())
    second, number, action = MODULE.upsert_entry(first, _source())

    assert action == "updated"
    assert number == 1
    assert second == first


def test_validate_source_requires_knowledge_base_sections():
    with pytest.raises(ValueError, match="missing required sections"):
        MODULE.upsert_entry("", "# {{ENTRY_NUMBER}}\n\n## 标题\n")
