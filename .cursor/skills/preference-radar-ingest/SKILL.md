---
name: preference-radar-ingest
description: >-
  维护 Horizon 偏好雷达：从文档/聊天文本生成 preference-radar 草案，批处理 inbox，
  并在用户确认后写入 data/preference-radar/profile.json 与 sources.json。
---

# Preference Radar Ingest

## 何时使用

- 用户说「更新偏好雷达」「preference ingest」「把这篇文档加入偏好」
- 用户丢来一篇研究笔记、方向说明、链接摘要，希望纳入个性化雷达
- 用户要求处理 `data/preference-radar/inbox/` 里的待处理文档

## 目录结构

```
data/preference-radar/
├── profile.json          # 长期兴趣、persona、关键词
├── sources.json          # score_threshold、max_items、独立 Google News 查询
├── inbox/                # 用户批量投放文档（不自动改 JSON）
├── inbox/processed/      # 确认应用后归档
├── drafts/               # AI 生成的待确认草案
└── changelog.jsonl       # 已应用变更审计日志
```

## 工作流（必须遵守：先草案，后确认）

### 聊天即时（单篇）

1. 读取用户提供的文档/粘贴文本
2. 运行：
   ```bash
   uv run horizon-preference-ingest --text "<用户文本>"
   ```
   或先把内容写入临时文件再 `--file path`
3. 向用户展示草案摘要（新增 interests / keywords / queries / persona）
4. **等用户明确说「确认 / apply」** 后再执行：
   ```bash
   uv run horizon-preference-ingest --apply <draft_id>
   ```

### Inbox 批处理

1. 列出 inbox：
   ```bash
   ls data/preference-radar/inbox/
   ```
2. 批量生成草案：
   ```bash
   uv run horizon-preference-ingest --inbox
   ```
3. 展示每个 draft_id 与变更摘要，等用户确认要应用哪些
4. 逐条 `--apply <draft_id>`

### 查看待确认草案

```bash
uv run horizon-preference-ingest --list-drafts
```

## 与主 Horizo​​n 的关系

- **原板块**（`config.json` → `filtering` + `category_groups`）不要改
- 偏好雷达是**独立 sidecar 流水线**，读 `data/preference-radar/`
- 日报结构：偏好雷达（置顶）→ 华科研究方向（外部流水线，`hust-research`）→ 其他资讯

## 反馈闭环（阅读 👍 / 👎）

日报 GitHub Pages 每条资讯下方有 **👍 有用 / 👎 不太相关**：

1. 浏览器 localStorage 即时记录
2. 点右下角 **导出偏好反馈** 下载 JSON
3. 放入 `data/preference-radar/feedback-inbox/`
4. 导入并回写 profile：
   ```bash
   uv run horizon-preference-ingest --import-feedback-inbox
   ```
   或指定文件 `--import-feedback path/to/export.json`

下次 `horizon` 日报跑时会 **自动** 导入 inbox + 应用 feedback.jsonl：
- 👍 → `raw_keywords` / `interests`
- 👎 → `negative_interests`，并在全流程跳过该 URL

## 禁止事项

- 不要跳过草案直接改 `profile.json` / `sources.json`（除非用户明确要求紧急覆盖且已知情）
- 不要把 CSIG / 旧 `interest_profile.json` 内容自动写回 config
- 应用草案前不要删除 inbox 原文件（apply 会自动归档到 `processed/`）

## 维护 sources.json 阈值

用户可在 `sources.json` 调整：

- `score_threshold`（默认 7.0）
- `max_items`（默认 5）
- `google_news_queries[]`（独立搜索，宜精准）

## 输出给用户

应用成功后报告：

- 新增 interests / keywords / queries 数量
- draft_id 与 changelog 条目
- 提醒下次日报顶部「偏好雷达」会生效
