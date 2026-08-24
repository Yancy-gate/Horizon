---
name: obsidian-retrospective
description: "把已完成的问题解决过程沉淀成可复习、可用于简历和面试的 Obsidian 每日学习日志。用户说“沉淀日志”“写复盘”“加入每日自主学习”“总结成简历素材”或要求更新同一篇复盘时使用。"
---

# Obsidian 问题复盘沉淀

把一次真实的问题解决过程转换为有证据、有知识点、有复习路径的长期学习资产，并安全写入当天 Obsidian 日志。

## 适用场景

- 完成功能、修复 Bug、排查线上或自动化故障后写复盘。
- 用户要求“把过程写进每日自主学习”。
- 用户想把项目经历整理成简历或面试素材。
- 已有复盘需要追加知识点，且不能重复创建条目。

不适用于纯摘录文章；文章入库应使用专门的 wiki-ingest 流程。

## 必须遵守

1. 先用系统命令取得 `Asia/Shanghai` 当天日期，禁止沿用上下文中的旧日期。
2. 目标固定为 `<vault>/其他/每日自主学习/YYYY-MM-DD.md`。
3. 当日编号使用 `# 1`、`# 2` 递增；更新同标题复盘时保留原编号。
4. 不记录 API Key、Token、Cookie、账号密码或完整认证 URL。
5. 所有事实都要能追溯到命令输出、日志、测试、提交或用户提供的证据。
6. 不把推测写成根因；未验证内容标为“待验证”。
7. 写入后必须验证目标路径、编号、必备章节和 Git 状态。
8. 同步到本地时只物化对应日志文件，不得对整个 vault 执行 `git pull`。

## 工作步骤

### 1. 确认日期与目标

Linux/macOS：

```bash
TZ=Asia/Shanghai date +%F
```

Windows PowerShell：

```powershell
Get-Date -Format yyyy-MM-dd
```

同时确认实际 vault 根目录和 Git 远端，避免写入旧仓库或旧路径。

### 2. 建立证据清单

至少收集：

| 证据 | 示例 |
|---|---|
| 用户表象 | 看不到日报、内容为空、任务未执行 |
| 运行证据 | Action 日志、退出码、请求状态 |
| 数据证据 | 条目数、文件行数、提交 SHA |
| 配置证据 | 模型名、Base URL、并发、目标仓库 |
| 验证证据 | 单元测试、全量测试、真实 smoke test |

### 3. 写复盘源文件

源文件必须以占位编号开头：

```markdown
# {{ENTRY_NUMBER}}

## 唯一且稳定的复盘标题
```

正文推荐结构：

1. 一句话结论。
2. 故障链路或系统流程图。
3. 问题、证据、根因、修复表。
4. 最终配置与验证结果。
5. 关键命令。
6. 工程方法总结。
7. 简历项目表述。
8. 面试展开要点。
9. 解决问题涉及的知识点。
10. 必备知识库表和复习路径。

### 4. 写清知识点

知识点不能只是名词列表。每个主题至少回答：

- 它是什么？
- 为什么在本次问题中重要？
- 如何验证？
- 常见失败模式是什么？
- 什么情况下不应使用？

优先覆盖可迁移能力，例如：

- 端到端链路与边界验证。
- API 协议兼容与 smoke test。
- Secret 生命周期与泄露处理。
- 批处理失败率、熔断和假成功。
- 并发、吞吐、限流和指数退避。
- 幂等与重复执行安全。
- Git 分叉、rebase、autostash 和冲突。
- 退出码、日志和可观测性。
- 定时任务身份、路径、补跑和验证。
- UTC 与业务时区一致性。

### 5. 加入必备知识库区块

每篇复盘必须包含以下四个标题：

```markdown
## .raw Wikilink 表
## Wiki source/entity 表
## 可读核心要点
## 复习路径
```

`.raw Wikilink 表` 链接原始材料和相关笔记；`Wiki source/entity 表` 描述来源、实体及关系；核心要点使用可读表格；复习路径给出按分钟或间隔复习的顺序。

### 6. 写入或更新当天日志

使用随 Skill 提供的脚本：

```bash
python .cursor/skills/obsidian-retrospective/scripts/upsert_daily_learning.py \
  --vault "/path/to/vault" \
  --source "/path/to/retrospective.md"
```

脚本行为：

- 当天文件不存在：自动创建。
- 标题首次出现：使用当日下一个编号追加。
- 相同标题已存在：原位更新并保留编号。
- 文件中有后续条目：完整保留。
- 写入使用临时文件替换，减少中断导致的半写入风险。

先预览但不写入：

```bash
python .cursor/skills/obsidian-retrospective/scripts/upsert_daily_learning.py \
  --vault "/path/to/vault" \
  --source "/path/to/retrospective.md" \
  --dry-run
```

指定补写日期：

```bash
python .cursor/skills/obsidian-retrospective/scripts/upsert_daily_learning.py \
  --vault "/path/to/vault" \
  --source "/path/to/retrospective.md" \
  --date 2026-08-24
```

仅在用户明确要求补写历史日期时使用 `--date`；默认必须使用当天日期。

### 7. 云端 Agent 无法访问本地 vault 时

1. 把复盘源文件提交到当前工作分支。
2. 使用 `git clone --filter=blob:none --no-checkout` 克隆仓库元数据。
3. 用 sparse checkout 只检出 `其他/每日自主学习`。
4. 使用已有 Obsidian 同步 Secret，并在 Action 内调用同一个 upsert 脚本。
5. 提交并推送目标日志。
6. 验证目标路径、编号、变更行数和远端 commit。
7. 删除一次性 push 触发，只保留安全的手动入口。
8. 让用户只同步对应的当天日志，不拉取整个 vault。

示例：

```bash
git clone --filter=blob:none --no-checkout "$OBSIDIAN_REPO_URL" obsidian-vault
git -C obsidian-vault sparse-checkout init --cone
git -C obsidian-vault sparse-checkout set "其他/每日自主学习"
git -C obsidian-vault checkout master
```

不得尝试读取或输出 GitHub Secret 的值。

### 8. 只同步对应文件到本地

Git 没有“pull 单文件”命令。`git pull` 会合并整个分支，因此此 Skill 禁止用它接收单篇复盘。

使用目标文件同步脚本：

```powershell
python ".cursor\skills\obsidian-retrospective\scripts\sync_remote_file.py" `
  --vault "D:\Data\旧的不去新的不来" `
  --path "其他/每日自主学习/2026-08-24.md"
```

脚本执行两步：

1. `git fetch --filter=blob:none` 更新远端提交和树信息。
2. 从 `FETCH_HEAD` 读取指定 blob，原子写入对应本地路径。

结果：

- 只改目标日志文件。
- 不 checkout、不 merge、不 rebase。
- 不改变本地 `HEAD`。
- 不覆盖其他本地笔记。

限制：

- Git 仍需获取少量提交和目录树元数据，但不会把其他文件写入本地工作区。
- 适合由自动化生成、用户只读的日志。
- 若用户会同时编辑同一目标文件，应先比较差异，不可直接覆盖。
- 路径必须是仓库内相对路径，脚本会拒绝绝对路径和 `..`。

## 完成检查

- [ ] 日期来自实际命令。
- [ ] 路径是当天 `其他/每日自主学习/YYYY-MM-DD.md`。
- [ ] 编号在当日文件内递增，更新时未变号。
- [ ] 根因均有证据。
- [ ] 没有敏感信息。
- [ ] 包含四个必备知识库区块。
- [ ] 包含知识点、简历表述和复习路径。
- [ ] 重复执行不会生成重复条目。
- [ ] 测试或 dry-run 通过。
- [ ] 本地或远端 Git 写入已验证。
- [ ] 本地接收只更新对应日志，没有拉取整个 vault。

## 用户调用方式

自然语言即可：

```text
把刚才解决 Horizon 日报问题的过程沉淀成日志，加入今天的每日自主学习。
```

```text
用 obsidian-retrospective 更新今天那篇复盘，追加 Git rebase 和批处理熔断知识点。
```

```text
把这次 Bug 修复整理成复盘和简历素材，写进我的 Obsidian。
```

```text
只把今天这篇复盘同步到本地，不要拉取其他 Obsidian 文件。
```

若用户没有给 vault 路径，且仓库中也无法可靠推断，只问一个问题：

```text
你的 Obsidian vault 根目录是什么？
```

更完整的命令示例和故障处理见同目录 `USAGE.md`。
