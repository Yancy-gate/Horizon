# obsidian-retrospective 使用说明

## 1. 最简单的调用方式

在 Cursor 中直接说：

```text
把刚才解决的问题沉淀成复盘，写入今天的每日自主学习，
补充知识点、简历表述和复习路径。
```

Skill 会完成：

1. 获取上海时区当天日期。
2. 从日志、命令和测试中整理证据。
3. 生成带编号的复盘。
4. 写入或更新当天日志。
5. 校验知识库表格和复习路径。
6. 只把对应文件同步到本地。

## 2. 默认路径

Vault：

```text
D:\Data\旧的不去新的不来
```

当天日志：

```text
D:\Data\旧的不去新的不来\其他\每日自主学习\YYYY-MM-DD.md
```

## 3. 常用场景

### 新建复盘

```text
用 obsidian-retrospective 把这次 Bug 修复写成今天的复盘。
```

结果：在当天文件中追加下一个 `# N` 条目。

### 更新同一篇复盘

```text
更新今天的 Horizon 复盘，追加并发控制、Git 分叉和幂等知识点。
```

结果：按稳定标题找到原条目，保留原编号并原位更新。

### 生成简历与面试素材

```text
把这次排障整理成 STAR 项目描述、90 秒项目介绍和面试追问。
```

### 只同步对应文件

```text
只把今天这篇每日自主学习同步到本地，不要拉取整个 Obsidian 库。
```

## 4. 本地直接写入

准备一个复盘源文件，第一行必须是：

```markdown
# {{ENTRY_NUMBER}}
```

执行：

```powershell
python ".cursor\skills\obsidian-retrospective\scripts\upsert_daily_learning.py" `
  --vault "D:\Data\旧的不去新的不来" `
  --source "C:\path\to\retrospective.md"
```

### 写入前预览

```powershell
python ".cursor\skills\obsidian-retrospective\scripts\upsert_daily_learning.py" `
  --vault "D:\Data\旧的不去新的不来" `
  --source "C:\path\to\retrospective.md" `
  --dry-run
```

### 补写指定日期

```powershell
python ".cursor\skills\obsidian-retrospective\scripts\upsert_daily_learning.py" `
  --vault "D:\Data\旧的不去新的不来" `
  --source "C:\path\to\retrospective.md" `
  --date 2026-08-24
```

只有用户明确要求补写历史日期时才使用 `--date`。

## 5. 从远端只同步一篇日志

Git 没有真正的单文件 `pull`。本 Skill 使用 partial fetch 获取远端元数据，再只导出指定文件。

同步当天学习日志：

```powershell
$date = Get-Date -Format yyyy-MM-dd
python ".cursor\skills\obsidian-retrospective\scripts\sync_remote_file.py" `
  --vault "D:\Data\旧的不去新的不来" `
  --path "其他/每日自主学习/$date.md"
```

同步某天 Horizon 日报：

```powershell
$date = Get-Date -Format yyyy-MM-dd
python ".cursor\skills\obsidian-retrospective\scripts\sync_remote_file.py" `
  --vault "D:\Data\旧的不去新的不来" `
  --path "其他/内参日报/horizon-$date-zh.md"
```

这两条命令都不会：

- 合并整个远端分支。
- 修改其他笔记。
- 改变本地 `HEAD`。
- 执行 `reset --hard`。

## 6. 云端 Agent 发布方式

云端不能访问 Windows 的 `D:\`，因此使用：

1. partial clone，只获取仓库元数据。
2. sparse checkout，只检出 `其他/每日自主学习`。
3. upsert 脚本更新对应日期文件。
4. GitHub Actions Secret 推送远端。
5. 用户本地运行单文件同步脚本。

云端不得输出、读取或复制 Secret 值。

## 7. 源文件必备结构

```markdown
# {{ENTRY_NUMBER}}

## 稳定且唯一的标题

正文……

## .raw Wikilink 表

## Wiki source/entity 表

## 可读核心要点

## 复习路径
```

稳定标题是更新键。修改标题会被视为新条目。

## 8. 常见问题

| 现象 | 原因 | 处理 |
|---|---|---|
| 生成重复条目 | 标题发生变化 | 使用原来的二级标题 |
| 报缺少必备章节 | 源文件结构不完整 | 补齐四个必备标题 |
| 远端没有目标文件 | 发布任务未完成或日期错误 | 检查 Action 和上海时区日期 |
| 单文件同步报路径错误 | 使用绝对路径或包含 `..` | 传仓库内相对路径 |
| 本地目标文件被覆盖 | 同时编辑了自动生成文件 | 先复制本地修改，再人工合并 |
| Git 鉴权失败 | 本地凭据无权访问远端 | 先用 `git fetch origin master` 验证 |

## 9. 推荐口令

完整沉淀：

```text
用 obsidian-retrospective 沉淀这次问题：
写清现象、证据、根因、修复、验证、知识点、简历表述和复习路径；
写入今天的每日自主学习；只同步对应文件。
```

仅更新知识点：

```text
用 obsidian-retrospective 更新今天同标题复盘，
补充这次涉及的底层知识和不适用场景，不新增条目。
```
