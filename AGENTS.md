# AGENTS.md

## Cursor Cloud specific instructions

Horizon is a Python 3.11+ CLI application (managed with **uv**) that aggregates news
from many sources (Hacker News, RSS, Reddit, Telegram, Twitter/X, GitHub, OpenBB),
scores/filters/enriches items with an AI provider, and generates bilingual Markdown
briefings. There is no GUI and no web server; it runs as a CLI, an MCP server, and a
GitHub Actions cron job.

### Toolchain / running commands
- `uv` is installed at `~/.local/bin/uv` by the startup update script. If `uv` is not
  on your `PATH`, run `export PATH="$HOME/.local/bin:$PATH"` first.
- The virtualenv lives at `.venv`; run everything through `uv run ...` (e.g.
  `uv run horizon`, `uv run pytest`, `uv run python scripts/check_mcp.py`).
- Dev/test deps (`pytest`, `pytest-cov`) are the `dev` optional extra. The update
  script installs them with `uv sync --extra dev`. Optional `openbb` and `twitter`
  extras exist but are not needed for tests or the default pipeline.

### Test / lint
- Tests: `uv run pytest` (282 tests, all offline — no network or API keys needed).
- Lint: the repo defines **no** lint config and CI runs no linter. `ruff` is only a
  transitive lockfile entry, not a project dev dependency. If you want a style pass,
  `uvx ruff@0.15.12 check src` runs with ruff defaults and reports pre-existing
  findings — do not treat those as regressions from your change.

### Running the pipeline (API keys required)
- The full `uv run horizon` pipeline needs (a) a config at `data/config.json`
  (copy `data/config.example.json` or run `uv run horizon-wizard`) and (b) at least
  one AI provider key in `.env` (e.g. `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`,
  `GOOGLE_API_KEY`, `DEEPSEEK_API_KEY`). Without an AI key it fails at the scoring step.
- `data/config.json`, `.env`, and `data/mcp-runs/` are git-ignored; safe to create for
  local runs without dirtying the tree.
- The **fetch** stage needs no AI key — only network. You can exercise core
  functionality end-to-end without secrets via the MCP service, e.g.:
  `uv run python -c "import asyncio; from src.mcp.service import HorizonPipelineService as S; print(asyncio.run(S().fetch_items(hours=72))['source_counts'])"`
  (Hacker News uses the public Firebase API and needs no token; GitHub/Reddit work
  better with `GITHUB_TOKEN`/higher limits but degrade gracefully.)
- MCP server entry point: `uv run horizon-mcp`. Quick smoke check:
  `uv run python scripts/check_mcp.py`.
