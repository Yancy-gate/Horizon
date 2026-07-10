# Horizon → Obsidian 部署说明

本目录为 Horizon 的本地工作副本，已按你的 Obsidian 库定制。

## 已完成

- 个性化 `data/config.github.json`（AI/ML 信息源、中文+英文、每日最多 15 条）
- 增强 `.github/workflows/daily-summary.yml`：
  - 运行后自动 commit `data/summaries/*.md`
  - 可选：直接推送到 Obsidian 库 `其他/内参日报/`
- Obsidian 目录：`D:\Tools\editor\Obsidian\临时\其他\内参日报\`
- Obsidian Git 插件：已写入自动 Pull（60 分钟）+ 启动时 Pull
- 本地同步脚本：`scripts/sync-to-obsidian.ps1`

## 你需要完成的 1 步（关键）

### 配置 AI API Key

进入 [Yancy-gate/Horizon Settings → Secrets](https://github.com/Yancy-gate/Horizon/settings/secrets/actions)：

| Secret | 说明 |
|--------|------|
| `DEEPSEEK_API_KEY` | **必填**。在 [platform.deepseek.com](https://platform.deepseek.com/) 创建，约 ¥10 可用很久 |

本地设置：

```powershell
gh secret set DEEPSEEK_API_KEY -R Yancy-gate/Horizon --body "sk-你的密钥"
gh workflow run "Daily Horizon Summary" -R Yancy-gate/Horizon
```

### 已自动配置（无需再改）

| 项 | 状态 |
|----|------|
| `OBSIDIAN_SYNC_TOKEN` | ✅ 已设置 |
| `OBSIDIAN_SYNC_ENABLED` | ✅ `true` |
| `OBSIDIAN_REPO` | ✅ `Yancy-gate/obsidian_cloud` |
| `OBSIDIAN_SUMMARY_DIR` | ✅ `其他/内参日报` |
| Obsidian Git 自动 Pull | ✅ 每 60 分钟 |
| Windows 定时同步 | ✅ 每天 7:30（备用） |

## 为什么之前没推送？

1. **从未运行过 Actions**（workflow 运行次数为 0）
2. **缺少 `DEEPSEEK_API_KEY`** — AI 步骤直接失败，后续 Obsidian 同步被跳过
3. **Obsidian 直推开关未开** — 现已开启 `OBSIDIAN_SYNC_ENABLED=true`

## 自定义抓取

见 [`docs/自定义抓取指南.md`](docs/自定义抓取指南.md)

## 本地运行

```powershell
cd C:\Users\hproy\Projects\Horizon
$env:PYTHONUTF8='1'
# 在 .env 中设置 DEEPSEEK_API_KEY 或 OPENAI_API_KEY
uv run horizon --hours 24
.\scripts\sync-to-obsidian.ps1
```

## Windows 定时同步（备用）

若不用 GitHub→Obsidian 直推，可每天 7:30 运行 `scripts\sync-to-obsidian.cmd`（任务计划程序）。

## 自定义信息源

```powershell
uv run horizon-wizard
```

生成后把 `data/config.json` 内容合并进 `data/config.github.json` 并 push。
