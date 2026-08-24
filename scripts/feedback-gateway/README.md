# Horizon Feedback Gateway

一次部署后，日报页面 **👍/👎 点击即自动回写** `data/preference-radar/profile.json`，无需手动导出 JSON。

## 架构

```
GitHub Pages (horizon.js)
    │ POST
    ▼
Cloudflare Worker（worker.js）
    │ repository_dispatch: horizon-feedback
    ▼
GitHub Actions (.github/workflows/horizon-feedback.yml)
    │ append → apply → commit
    ▼
main 分支 preference-radar 更新
```

## 一次性部署（约 5 分钟）

1. 安装 [Wrangler](https://developers.cloudflare.com/workers/wrangler/) 并登录 Cloudflare
2. 在 GitHub 创建 fine-grained PAT：Contents + Actions（Read and write）
3. 部署：

```bash
cd scripts/feedback-gateway
npx wrangler deploy worker.js --name horizon-feedback
npx wrangler secret put GITHUB_TOKEN
npx wrangler secret put GITHUB_REPO       # 例: Yancy-gate/Horizon
npx wrangler secret put ALLOWED_ORIGINS   # 例: https://thysrael.github.io
```

4. 仓库 Variables 新增 `HORIZON_FEEDBACK_ENDPOINT` = Worker URL

## 离线

无 endpoint 或传失败时暂存 localStorage，恢复后自动补传。
