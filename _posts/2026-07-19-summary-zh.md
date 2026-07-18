---
layout: default
title: "Horizon Summary: 2026-07-19 (ZH)"
date: 2026-07-19
lang: zh
---

> 从 76 条内容中筛选出 12 条重要资讯。

---

1. [LG 显示器通过 Windows Update 静默安装软件](#item-1) ⭐️ 9.0/10
2. [GPT-5.6 Sol Pro 解决凸优化领域 30 年猜想](#item-2) ⭐️ 8.0/10
3. [Kimi K3 通过蒸馏技术达到美国前沿模型水平](#item-3) ⭐️ 8.0/10
4. [Anthropic 改变决定，永久保留 Claude Fable 5](#item-4) ⭐️ 8.0/10
5. [印奇在 WAIC 2026：智能体进入物理世界](#item-5) ⭐️ 8.0/10
6. [SQLite 查询解释器：交互式 LLM 驱动工具](#item-6) ⭐️ 7.0/10
7. [自进化 Agent Harness 性能提升 104%](#item-7) ⭐️ 7.0/10
8. [腾讯发布具身智能全栈方案及 ADP 4.0 海外版](#item-8) ⭐️ 7.0/10
9. [诉讼律师游说反对自动驾驶汽车](#item-9) ⭐️ 7.0/10
10. [Skyroot Aerospace 发射印度首枚私营轨道火箭](#item-10) ⭐️ 7.0/10
11. [风投 Neil Rimer：AI 财富必须重新分配](#item-11) ⭐️ 6.0/10
12. [罕见生长障碍或为癌症预防提供关键线索](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [LG 显示器通过 Windows Update 静默安装软件](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 9.0/10

LG 显示器在未经用户同意的情况下，通过 Windows Update 静默安装软件包，Gamers Nexus 使用 LG UltraGear 34GX900A-B 确认了此行为。当通过 HDMI 连接显示器时，软件会自动安装，即使之前已拥有旧款 LG 显示器也是如此。 这带来了严重的安全和隐私风险，因为该软件在系统启动时运行，拥有完全的系统访问权限和网络访问权限，且没有沙盒隔离。它破坏了用户对自己系统的信任和控制，影响了大量 LG 显示器用户。 该软件通过 Windows Update 的驱动程序分发机制交付，该机制会自动安装制造商提供的软件包。用户可以通过组策略或设备安装设置禁用此行为，但默认设置允许静默安装。

hackernews · baranul · 7月18日 10:21 · [社区讨论](https://news.ycombinator.com/item?id=48956688)

**背景**: Windows Update 会自动为硬件设备（包括显示器）提供驱动程序和软件更新，以确保兼容性和功能性。然而，制造商可能滥用此机制，在未经用户同意的情况下推送无关软件。此问题凸显了 Windows 驱动程序许可模式的更广泛问题，即用户对安装内容控制有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent">LG monitors silently install software through Windows Update without user consent - VideoCardz.com</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows-hardware/drivers/dashboard/understanding-windows-update-automatic-and-optional-rules-for-driver-distribution">Understanding Windows Update rules for driver distribution - Windows drivers | Microsoft Learn</a></li>

</ul>
</details>

**社区讨论**: 社区对此高度批评，许多用户称此为类似恶意软件的行为，并指责 LG 和微软。一些用户提供了通过组策略或设备安装设置的解决方法，而另一些用户则认为微软应彻底改革其驱动程序许可模式以防止此类滥用。

**标签**: `#security`, `#privacy`, `#Windows`, `#LG`, `#software distribution`

---

<a id="item-2"></a>
## [GPT-5.6 Sol Pro 解决凸优化领域 30 年猜想](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 8.0/10

一位用户使用 GPT-5.6 Sol Pro 给出了凸优化领域一个长期未解猜想的证明，填补了该领域 30 年的空白。该结果在 Reddit 上分享，并被认可为真正的数学贡献。 这标志着 AI 辅助数学研究的一个重要里程碑，表明大型语言模型能够对非平凡的理论问题做出贡献。它暗示 AI 可能通过处理以前被视为中等难度的问题来加速数学和理论计算机科学的进展。 该猜想涉及在球域上对凸 Lipschitz 函数求解优化问题的时间复杂度，而通过变量替换，球域本质上等价于任何有界域。该证明使用了 GPT-5.6 Sol Pro——OpenAI 面向复杂推理和科学工作的最高能力模型，而非 Ultra 版本。

hackernews · mbustamanter · 7月18日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48957779)

**背景**: 凸优化是数学优化的一个子领域，研究在凸集上最小化凸函数的问题，广泛应用于机器学习、工程和经济学。本新闻涉及的猜想与凸优化的查询复杂度有关，这是一个关于需要多少次函数评估才能找到近似解的基本问题。GPT-5.6 Sol Pro 是 OpenAI 的 GPT-5.6 模型系列中的一个层级，专为需要深度推理和长时间运行工作流的艰巨任务而设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt">GPT - 5 . 6 in ChatGPT | OpenAI Help Center</a></li>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区普遍赞扬了这一成就，评论者指出虽然该猜想较为小众，但代表了真正的贡献。一些人讨论了这对研究者的影响，认为数学和理论计算机科学中的低垂果实甚至中等难度问题可能被自动化，从而推动研究者转向更具创新性的问题。其他人则将这种方法与暴力数学逻辑相比较，并指出了 Sol Pro 和 Ultra 模型之间的区别。

**标签**: `#AI`, `#mathematics`, `#convex optimization`, `#LLM`, `#research`

---

<a id="item-3"></a>
## [Kimi K3 通过蒸馏技术达到美国前沿模型水平](https://stephen.bochinski.dev/blog/2026/07/18/the-kimi-k3-moment/) ⭐️ 8.0/10

中国 AI 公司月之暗面发布了 Kimi K3，一个拥有 2.8 万亿参数的模型，通过知识蒸馏技术达到了与 GPT-5.6 和 Opus 4.8 等美国前沿模型相当的性能。 这标志着一个重要里程碑：中国模型以更低成本达到了美国顶级 AI 能力，加剧了关于 AI 领导地位、国家安全以及出口管制有效性的地缘政治辩论。 Kimi K3 拥有 2.8 万亿参数、100 万 token 上下文窗口，支持文本和图像输入。其定价（输入/输出每百万 token $3/$15）低于 GPT-5.6 Sol（$5/$30）和 Opus 4.8（$5/$25），但部分用户反映它在某些任务上消耗更多计算资源。

hackernews · sbochins · 7月18日 17:32 · [社区讨论](https://news.ycombinator.com/item?id=48960218)

**背景**: 知识蒸馏是一种技术，让较小的学生模型从较大的教师模型的输出中学习，从而实现更便宜、更快的推理。前沿 AI 模型指 AI 研究中最先进、能力最强的模型。Kimi K3 基于 Kimi Delta Attention（KDA）构建，这是一种混合线性注意力机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://artificialanalysis.ai/models/kimi-k3">Kimi K3 - Intelligence, Performance & Price Analysis</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：有人认为蒸馏技术不可避免，前沿实验室的护城河正在消失；另一些人质疑 K3 在实际中是否真正匹配美国模型，指出其计算消耗更高。还有人担忧使用此类模型可能面临国家安全限制。

**标签**: `#AI`, `#LLM`, `#distillation`, `#geopolitics`, `#open-source`

---

<a id="item-4"></a>
## [Anthropic 改变决定，永久保留 Claude Fable 5](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 8.0/10

Anthropic 宣布，自 7 月 20 日起，Claude Fable 5 将永久包含在 Max 和 Team Premium 订阅计划中，推翻了此前移除该模型的计划。这一变化是在 OpenAI 的 GPT-5.6 Sol 和 Moonshot AI 的 Kimi 3 的竞争压力下做出的。 这一决定表明，AI 行业的竞争态势正迫使公司将最优秀的模型保留给订阅用户，而非限制在昂贵的 API 专属访问中。这也缓解了用户对失去 Anthropic 最强模型访问权限的焦虑。 Max 和 Team Premium 订阅用户将获得 Fable 5 使用额度的一半，而 Pro 和 Team Standard 用户将继续通过使用积分访问，并获得一次性 100 美元积分。每月 20 美元的计划仍然不包含 Fable 5。

rss · Simon Willison · 7月18日 06:00

**背景**: Claude Fable 5 是 Anthropic 推出的 Mythos 级大型语言模型，专为自主知识工作和编程设计。Anthropic 最初因计算能力问题计划将 Fable 5 从订阅中移除，但 OpenAI 和 Moonshot AI 的竞争性发布使该计划难以维持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，对“Fable 末日”结束感到宽慰。一些用户指出，每月 20 美元的计划仍然没有 Fable 5，这可能会促使预算有限的用户升级或考虑竞争对手。

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#pricing`, `#competition`

---

<a id="item-5"></a>
## [印奇在 WAIC 2026：智能体进入物理世界](https://36kr.com/p/3900439867147909?f=rss) ⭐️ 8.0/10

在 WAIC 2026 上，阶跃星辰与千里科技董事长印奇发表了题为《当智能体进入物理世界》的主题演讲，指出 2026 年模型能力正在跨越关键临界点，智能体已能独立工作数十小时。他阐述了智能体浪潮推动的三大结构性变革：Agentic OS、新终端载体和 A2A 网络。 这标志着 AI 从聊天工具向物理世界中生产力单元的范式转变，将影响系统、设备和网络的设计方式。演讲强调了智能体获得自主性后治理框架的迫切需求，将对开发者、企业乃至整个社会产生深远影响。 印奇指出了三大结构性变革：Agentic OS 作为新系统层连接模型与数据、工具和设备；终端从以人为本走向人机共生；A2A 网络赋予智能体身份、能力和信用以实现自主协作。他还强调了需要新的治理机制来确保身份可信、权限可控和行为可追溯。

rss · 36氪 · 7月18日 00:53

**背景**: AI 智能体是能够感知、推理并采取行动以实现目标的自主系统。Agentic OS 是协调智能体并将其连接到数据和应用的运行层，而 A2A（智能体对智能体）网络则使智能体之间能够通信和协作。WAIC（世界人工智能大会）是每年在上海举办的全球性 AI 盛会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://slack.com/blog/productivity/what-is-an-agentic-os">What Is an Agentic OS? A Practical Guide | Slack</a></li>
<li><a href="https://arxiv.org/abs/2501.08944">[2501.08944] Physical AI Agents: Integrating Cognitive Intelligence with Real-World Action</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#AGI`, `#Human-AI Collaboration`, `#Agentic OS`, `#A2A Networks`

---

<a id="item-6"></a>
## [SQLite 查询解释器：交互式 LLM 驱动工具](https://simonwillison.net/2026/Jul/18/sqlite-query-explainer/#atom-everything) ⭐️ 7.0/10

Simon Willison 构建了一个交互式 SQLite 查询解释器，通过 Pyodide 和 WebAssembly 完全在浏览器中运行，利用 LLM 生成 EXPLAIN 和 EXPLAIN QUERY PLAN 输出的通俗英语解释。 该工具让难以阅读查询计划的开发者能够理解 SQLite 查询计划，有望提升整个社区对数据库性能的理解和优化能力。 该工具通过 Pyodide 在 WebAssembly 中运行 Python 版 SQLite，并使用 Anthropic 的 Claude Fable（或类似 LLM）添加解释。作者提醒，他无法完全验证 LLM 输出的准确性。

rss · Simon Willison · 7月18日 17:19

**背景**: SQLite 的 EXPLAIN QUERY PLAN 提供了查询执行方式的高级描述，但其输出可能难以理解。Pyodide 是基于 WebAssembly 的浏览器 Python 发行版，允许 Python 代码在客户端运行。LLM 可以将技术输出翻译成自然语言，使其更易于理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pyodide.org/">Pyodide — Version 314.0.2</a></li>
<li><a href="https://www.sqlite.org/eqp.html">Explain query plan</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**标签**: `#sqlite`, `#query-plan`, `#pyodide`, `#webassembly`, `#llm`

---

<a id="item-7"></a>
## [自进化 Agent Harness 性能提升 104%](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247904823&idx=3&sn=af8b10819641ba1f59492acb8aa9ebd4) ⭐️ 7.0/10

上海人工智能实验室开发了一种自进化的 Agent Harness，在不改变底层模型的情况下，将任务性能提升了 104%。该工作已获得顶级 Agent 社区的认可，并赢得了世界人工智能大会最高奖。 这一突破表明，通过改进智能体基础设施（Harness）而非模型本身，可以实现显著的性能提升，从而可能减少昂贵的模型重新训练需求。它可能通过使 AI 智能体更具适应性和效率，加速其在现实世界应用中的采用。 自进化 Harness 能够自主修改自身代码和配置，随时间推移提升性能，无需人工干预。104%的提升是在标准智能体基准测试上测量的，但公告中未披露具体的基准和模型细节。

rss · 量子位 · 7月18日 07:45

**背景**: Agent Harness 是使大型语言模型能够作为 AI 智能体运行的软件基础设施，管理工具使用、记忆和多步骤任务。传统智能体依赖人类设计的固定 Harness，而自进化 Harness 能够自主适应和改进，代表了智能体开发的新范式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness</a></li>
<li><a href="https://github.com/EvoAgentX/Awesome-Self-Evolving-Agents">GitHub - EvoAgentX/Awesome- Self - Evolving - Agents : [Survey]...</a></li>
<li><a href="https://arxiv.org/pdf/2508.07407">A Comprehensive Survey of Self - Evolving AI Agents : A New...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Agent`, `#Self-Evolution`, `#Machine Learning`, `#Shanghai AI Lab`

---

<a id="item-8"></a>
## [腾讯发布具身智能全栈方案及 ADP 4.0 海外版](https://36kr.com/newsflashes/3900908700436103?f=rss) ⭐️ 7.0/10

在 2026 年 WAIC 上，腾讯升级发布了贯穿云底座、模型层、平台层与应用层的具身智能全栈方案，并正式上线企业级智能体开发平台 ADP 4.0 海外版。同时面向个人用户推出 WorkBuddy 独立 App，支持 iOS、Android 和鸿蒙三端。 此举标志着腾讯在具身智能和企业智能体生态的战略布局，有望加速机器人开发和企业 AI 落地。跨平台的 WorkBuddy App 也标志着向普及个人 AI 助手迈出一步。 具身智能全栈方案涵盖云底座、基础模型、平台工具和应用服务，旨在帮助机器人开发商提质提效。ADP 4.0 海外版是“十大行业百大场景”生态计划的一部分，已落地 30 多个行业，覆盖智能客服、知识管理、媒体生产等场景。

rss · 36氪 · 7月18日 09:30

**背景**: 具身智能指能够通过身体（如机器人）与物理世界交互的 AI 系统。腾讯的全栈方案提供了从云到应用的所有必要组件，降低了机器人开发门槛。ADP 是腾讯的企业级智能体开发平台，4.0 版本专注于 AgentOps，支持大规模管理 AI 智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.163.com/dy/article/L25O53N705506BEH.html?clickfrom=w_tech">163.com/dy/article/L25O53N705506BEH.html?clickfrom=w_tech</a></li>
<li><a href="https://www.jiemian.com/article/14788666.html">闪电快讯｜腾讯升级发布 具 身 智 能 全 栈 方 案 ，WorkBuddy推出App...</a></li>
<li><a href="https://www.yangtse.com/news/ch/202607/t20260718_373627.html">聚焦WAIC｜腾讯升级发布 具 身 智 能 全 栈 方 案 ，ADP 4.0海外版正式上线</a></li>

</ul>
</details>

**标签**: `#具身智能`, `#智能体`, `#腾讯`, `#WAIC`, `#企业级AI`

---

<a id="item-9"></a>
## [诉讼律师游说反对自动驾驶汽车](https://marginalrevolution.com/marginalrevolution/2026/07/trial-lawyers-lobby-against-autonomous-vehicles.html?utm_source=rss&utm_medium=rss&utm_campaign=trial-lawyers-lobby-against-autonomous-vehicles) ⭐️ 7.0/10

尽管 Waymo 和 Swiss Re 的 2200 万英里实际数据显示无人驾驶比人类驾驶安全得多，但诉讼律师仍在游说反对自动驾驶汽车。 这种政治反对可能延迟自动驾驶汽车的采用，而自动驾驶汽车仅在美国每年就有潜力挽救数万人的生命。 游说活动针对的是可能减少车祸诉讼数量的责任法律，这威胁到诉讼律师的收入。Waymo 的数据显示，与人类驾驶员相比，严重碰撞事故显著减少。

rss · Marginal Revolution · 7月18日 11:18

**背景**: 自动驾驶汽车使用摄像头、激光雷达和雷达等传感器在无需人类输入的情况下导航。该领域的领导者 Waymo 发布了安全数据，显示其车辆造成的事故少于人类驾驶员。诉讼律师从事故诉讼中收取费用，因此有经济动机反对减少事故的法律。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://coverager.com/waymo-releases-new-study-with-swiss-re/">Waymo releases new study with Swiss Re</a></li>
<li><a href="https://www.linkedin.com/posts/fhadi_opinion-the-data-on-self-driving-cars-is-activity-7401654006496092162-Iun-">Waymo just released nearly 100 million miles of driverless safety data ...</a></li>
<li><a href="https://waymo.com/">Waymo - Self-Driving Cars - Autonomous Vehicles - Ride-Hail</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#AI safety`, `#transportation policy`, `#Waymo`, `#lobbying`

---

<a id="item-10"></a>
## [Skyroot Aerospace 发射印度首枚私营轨道火箭](https://www.bbc.co.uk/news/articles/clyekv7rld3o?at_medium=RSS&at_campaign=rss) ⭐️ 7.0/10

2026 年 7 月 18 日，Skyroot Aerospace 成功发射了 Vikram-1，这是印度首枚为轨道任务设计的商业火箭，使印度成为继美国和中国之后第三个拥有私营轨道发射能力的国家。 这一里程碑标志着印度私营航天工业的重大飞跃，为商业卫星发射开辟了新机遇，并减少了对 ISRO 等政府机构的依赖。 Vikram-1 是一种小型运载火箭，可承载高达 350 公斤的有效载荷，其成功轨道飞行是在 2022 年 11 月 Vikram-S 亚轨道测试之后进行的。

rss · BBC World News · 7月18日 07:05

**背景**: Skyroot Aerospace 由前 ISRO 科学家 Pawan Kumar Chandana 和 Naga Bharath Daka 创立，旨在提供响应迅速、可靠且经济的太空访问。Vikram 火箭系列以印度太空计划之父 Vikram Sarabhai 的名字命名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Skyroot_Aerospace">Skyroot Aerospace</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vikram_(rocket_family)">Vikram (rocket family)</a></li>
<li><a href="https://www.bbc.com/news/articles/clyekv7rld3o">Vikram - 1 : India's first private space rocket by Skyroot to carry...</a></li>

</ul>
</details>

**标签**: `#space`, `#rocket`, `#India`, `#commercial launch`, `#Skyroot Aerospace`

---

<a id="item-11"></a>
## [风投 Neil Rimer：AI 财富必须重新分配](https://techcrunch.com/2026/07/17/neil-rimer-thinks-the-ai-money-is-coming-back-out/) ⭐️ 6.0/10

Index Ventures 联合创始人 Neil Rimer 预测，AI 在硅谷创造的巨额财富将需要以自愿或非自愿的方式进行重新分配。 这位知名风投家的观点凸显了人们对 AI 加剧财富不平等的担忧，可能影响科技行业的政策辩论和投资策略。 Rimer 未具体说明重新分配的机制，但他的言论反映了关于 AI 的经济利益应如何在社会中共享的更广泛讨论。

rss · TechCrunch AI · 7月18日 04:47

**背景**: AI 为硅谷的公司和投资者创造了巨额财富，但批评者认为利益集中在少数人手中，加剧了不平等。像 Rimer 这样的风投家越来越直言不讳地主张重新分配以维持社会稳定。

**标签**: `#AI`, `#venture capital`, `#wealth redistribution`, `#Silicon Valley`

---

<a id="item-12"></a>
## [罕见生长障碍或为癌症预防提供关键线索](https://www.bbc.co.uk/news/articles/c8jnlmek8reo?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

研究人员发现，患有罕见生长障碍——拉伦综合征的人群，其癌症发病率显著低于普通人群。 这一发现可能通过靶向生长激素/IGF-1 通路，为癌症预防疗法开辟新途径，从而惠及数百万癌症高风险人群。 拉伦综合征由生长激素受体基因突变引起，导致 IGF-1 缺乏。患者还表现出较低的糖尿病风险和更长的寿命。

rss · BBC World News · 7月17日 23:24

**背景**: 拉伦综合征是一种常染色体隐性遗传病，特征为身材矮小和生长激素抵抗。全球约有 250-350 人患病，最大群体在厄瓜多尔。该病导致尽管生长激素水平高，但 IGF-1 水平低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Laron_syndrome">Laron syndrome</a></li>
<li><a href="https://medlineplus.gov/genetics/condition/laron-syndrome/">Laron syndrome : MedlinePlus Genetics</a></li>

</ul>
</details>

**标签**: `#cancer research`, `#genetics`, `#Laron syndrome`, `#medical discovery`

---