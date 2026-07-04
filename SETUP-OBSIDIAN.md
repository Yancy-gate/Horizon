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

## 你需要完成的 3 步

### 1. Fork 并推送（约 2 分钟）

在终端执行（若 gh 未登录，先完成浏览器授权）：

```powershell
gh auth login -h github.com -p https -w
gh repo fork Thysrael/Horizon --clone=false
cd C:\Users\hproy\Projects\Horizon
git remote rename origin upstream
git remote add origin https://github.com/<你的用户名>/Horizon.git
git push -u origin main
```

### 2. 配置 GitHub Secrets

进入 **你 Fork 的仓库** → Settings → Secrets and variables → Actions：

| Secret | 说明 |
|--------|------|
| `DEEPSEEK_API_KEY` | 推荐。DeepSeek 便宜且稳定 |
| 或 `OPENAI_API_KEY` | 需账户有余额（当前本地 key 已超额） |

可选（Obsidian 全自动同步）：

| 名称 | 类型 | 值 |
|------|------|-----|
| `OBSIDIAN_SYNC_TOKEN` | Secret | GitHub PAT，对 `obsidian_cloud` 有写权限 |
| `OBSIDIAN_SYNC_ENABLED` | Variable | `true` |

### 3. 启用 Actions

Fork 仓库 → Actions → 允许工作流 → 手动 Run `Daily Horizon Summary` 测试。

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
