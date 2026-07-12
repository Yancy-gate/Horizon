---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 102 条内容中筛选出 16 条重要资讯。

---

1. [Grok Build CLI 将整个仓库上传至 xAI](#item-1) ⭐️ 9.0/10
2. [RISCBoy：基于 RISC-V 的开源便携游戏机](#item-2) ⭐️ 8.0/10
3. [英伟达在 GPU 热潮中的循环融资](#item-3) ⭐️ 8.0/10
4. [智谱创始人唐杰内部信：押注编程与推理](#item-4) ⭐️ 8.0/10
5. [Meta 紧急下线争议 AI 生图功能](#item-5) ⭐️ 8.0/10
6. [中国 Orca 世界模型无需动作标签即达专业机器人水平](#item-6) ⭐️ 8.0/10
7. [中国或限制海外访问顶尖 AI 模型](#item-7) ⭐️ 8.0/10
8. [具身数据行业：97 家玩家，一年融资 44.7 亿](#item-8) ⭐️ 7.0/10
9. [Mistral AI 发布单摄像头导航模型](#item-9) ⭐️ 7.0/10
10. [蚂蚁集团开源机器人大脑，性能超越 pi0.5](#item-10) ⭐️ 7.0/10
11. [Mozilla.ai 发布开源 LLM 控制平面 Otari](#item-11) ⭐️ 7.0/10
12. [GitHub API 遭滥用：50 多个幽灵账户发起侦察行动](#item-12) ⭐️ 7.0/10
13. [Ghostcommit 攻击将恶意提示隐藏在图像中](#item-13) ⭐️ 7.0/10
14. [SK 海力士 CEO 预计 HBM 价格 2027 年翻倍](#item-14) ⭐️ 6.0/10
15. [三星将龙仁芯片工厂投产提前至 2029 年](#item-15) ⭐️ 6.0/10
16. [英伟达将机器人 AI 引入 Hugging Face](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Grok Build CLI 将整个仓库上传至 xAI](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 9.0/10

安全研究人员发现，xAI 的 Grok Build CLI 会将整个仓库内容（包括 .env 密钥和 git 历史）上传至 xAI 服务器，无论代理读取了什么。 这给使用 Grok Build 的开发者带来了严重的隐私和安全问题，因为 API 密钥和凭证等敏感数据可能在不知情的情况下被泄露。 上传内容包括每个跟踪文件和完整的 git 历史，与代理读取的内容无关，意味着即使 AI 未访问的文件也会被发送至 xAI 服务器。

hackernews · jhoho · 7月12日 01:09 · [社区讨论](https://news.ycombinator.com/item?id=48877371)

**背景**: Grok Build 是 xAI 于 2026 年 5 月推出的终端原生 AI 编码代理，旨在直接从命令行帮助开发者完成编码任务。数据泄露是一种已知的安全问题，指未经授权传输敏感数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build Beta | SpaceXAI</a></li>
<li><a href="https://attack.mitre.org/tactics/TA0010/">Exfiltration , Tactic TA0010 - Enterprise | MITRE ATT&CK</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了震惊和担忧，用户指出这种行为破坏了人们对 xAI 的信任。一些用户建议使用沙盒工具来降低风险，而另一些用户则将其与 Codex 和 Claude Code 等其他 AI 编码工具的做法进行比较。

**标签**: `#privacy`, `#security`, `#AI tools`, `#xAI`, `#data exfiltration`

---

<a id="item-2"></a>
## [RISCBoy：基于 RISC-V 的开源便携游戏机](https://github.com/Wren6991/RISCBoy) ⭐️ 8.0/10

树莓派 ASIC 设计工程师 Luke Wren 发布了 RISCBoy，这是一款从头开始使用 RISC-V 指令集架构构建的开源便携游戏机。 该项目展示了 RISC-V 在消费电子产品中的可行性，并为复古游戏爱好者和嵌入式开发者提供了一个完全开源的硬件平台。 RISCBoy 被描述为“来自 RISC-V 在 2001 年就已存在的平行宇宙的 Gameboy Advance”，并且包含了开源的 AHB/APB 总线实现，这些通常与 ARM 的专有生态系统相关。

hackernews · mariuz · 7月11日 21:58 · [社区讨论](https://news.ycombinator.com/item?id=48876245)

**背景**: RISC-V 是一种基于 RISC 原则的免费开放标准指令集架构（ISA），于 2010 年在加州大学伯克利分校开发。与 ARM 和 x86 等专有 ISA 不同，RISC-V 允许任何人无需支付版税即可设计处理器。像 RISCBoy 这样的开源硬件项目实现了硬件设计的完全透明和社区协作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-source_hardware">Open-source hardware - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，称赞 Luke Wren 的工程技能和项目的怀旧魅力。一些评论者指出开源 AHB/APB 组件的重要性，这些通常被认为是 ARM 专有的。

**标签**: `#RISC-V`, `#open-source hardware`, `#gaming console`, `#embedded systems`

---

<a id="item-3"></a>
## [英伟达在 GPU 热潮中的循环融资](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 8.0/10

一项分析显示，英伟达对 CoreWeave 和 Nebius 的投资可能涉及循环融资，即英伟达投资 GPU 云初创公司，这些公司再用资金购买英伟达硬件，可能人为推高需求。 这种模式引发了对 GPU 热潮可持续性的担忧，即需求是真实的还是被人为放大，影响投资者和更广泛的人工智能基础设施生态系统。 英伟达投资 20 亿美元获得 CoreWeave 9%的股份，而 CoreWeave 计划 2026 年资本支出 350 亿美元，英伟达的投资仅占该年支出的 5.7%，其余来自其他来源，表明循环性可能被夸大。

hackernews · adletbalzhanov · 7月11日 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48873836)

**背景**: 循环融资是指一家公司投资于客户，客户再用这些资金购买投资方的产品，形成反馈循环，可能夸大收入。在 AI 领域，英伟达对 CoreWeave 和 Nebius 等 GPU 云提供商的投资引发了关于这种做法是否人为推高 GPU 需求的争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.buildthisnow.com/blog/guide/mechanics/is-ai-a-bubble">Is AI a Bubble? ' Circular Financing ' in Plain English | Build This Now</a></li>
<li><a href="https://factually.co/fact-checks/finance/is-ai-circular-financing-inflating-a-bubble-670512">Is AI’s Circular Financing Inflating a Bubble?</a></li>

</ul>
</details>

**社区讨论**: 评论者就循环融资的重要性展开辩论：有人认为英伟达的投资相对于 CoreWeave 的总资本支出很小，而另一些人则关注每 token ROI 和企业 token 预算等盈利指标。还有讨论认为英伟达此举是对超大规模云厂商的战略对冲。

**标签**: `#GPU`, `#financing`, `#Nvidia`, `#cloud computing`, `#AI infrastructure`

---

<a id="item-4"></a>
## [智谱创始人唐杰内部信：押注编程与推理](https://36kr.com/p/3891132709206784?f=rss) ⭐️ 8.0/10

2026 年 7 月 11 日，智谱创始人唐杰发布内部信，透露公司战略转向 AI 编程与推理，这一转变使公司市值增长 10 倍，并推出了开源模型 GLM-5.2，其性能已媲美 GPT-5.5 和 Claude Opus 4.8。 这标志着 AI 行业向编程与推理作为下一前沿的重大转变，智谱的成功表明押注这些能力既能带来技术领先，也能获得商业回报。 截至 2026 年 3 月，智谱 MaaS 平台的 ARR 达到 17 亿元人民币，同比增长 60 倍。其 GLM-5.2 模型拥有 744B 参数、40B 激活参数和 100 万 token 上下文窗口，并以 MIT 许可证开源。

rss · 36氪 · 7月11日 11:28

**背景**: 智谱由清华大学教授唐杰创立，已从事大语言模型研发近十年。公司于 2026 年 1 月在港交所上市。在 2025 年初 DeepSeek R1 发布后，智谱将重心从聊天转向编程与推理，这一押注获得了回报，因为 AI 编程已成为最具商业化能力的 AI 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/GLM-5.2 · Hugging Face</a></li>
<li><a href="https://the-decoder.com/zhipu-ais-glm-5-2-closes-in-on-closed-source-leaders-in-coding-marathons/">Zhipu AI's GLM-5.2 closes in on closed-source leaders in coding marathons</a></li>
<li><a href="https://the-decoder.com/zhipu-ais-glm-5-1-can-rethink-its-own-coding-strategy-across-hundreds-of-iterations/">Zhipu AI's GLM-5.1 can rethink its own coding strategy across hundreds of iterations</a></li>

</ul>
</details>

**标签**: `#AI`, `#Coding`, `#Zhipu`, `#Strategy`, `#LLM`

---

<a id="item-5"></a>
## [Meta 紧急下线争议 AI 生图功能](https://36kr.com/newsflashes/3891995047033351?f=rss) ⭐️ 8.0/10

Meta 已下线一项新 AI 图像生成功能，该功能允许用户通过@提及引用公开的 Instagram 帖子来生成 AI 图像，此前因隐私和法律争议遭到广泛批评。 这一事件凸显了 AI 创新与用户隐私权之间日益紧张的关系，并可能影响未来关于社交媒体平台如何使用公开内容进行 AI 训练和生成的法规。 该功能对公开 Instagram 账户默认开启，用户需主动关闭才能避免其内容被使用。包括美国演员工会（SAG-AFTRA）在内的批评者担忧肖像权侵犯及潜在的犯罪滥用风险。

rss · 36氪 · 7月12日 02:20

**背景**: 像 DALL-E 和 Midjourney 这样的 AI 图像生成工具在利用公共网络数据训练时已引发隐私担忧。Meta 的功能更进一步，允许实时引用特定 Instagram 帖子，从而放大了未经授权使用个人肖像的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://petapixel.com/2026/07/10/meta-removes-ai-image-generation-feature-that-used-public-instagram-posts-following-user-backlash/">Meta Removes AI Image Generation Feature That Used Public ...</a></li>
<li><a href="https://9to5mac.com/2026/07/10/meta-removes-feature-that-let-users-generate-ai-images-from-public-instagram-posts/">Meta removes feature that let users generate AI images from public ...</a></li>
<li><a href="https://www.computing.co.uk/news/2026/meta-under-fire-over-ai-image-tool-that-uses-public-instagram-pics">Meta under fire over AI image tool that uses public Instagram pics</a></li>

</ul>
</details>

**标签**: `#AI`, `#privacy`, `#Meta`, `#social media`, `#ethics`

---

<a id="item-6"></a>
## [中国 Orca 世界模型无需动作标签即达专业机器人水平](https://news.google.com/rss/articles/CBMixgFBVV95cUxPSUFhYnBGNkJtUU1JTHhZbThBRnAxcGhlMWhiNmhEQllFTll3RFVMUTZBSHQ4TWg5SE5jaTBqLU5ITnVxUVhQRkk5dzhRZzh4a2FtUWxyTHVTMTFVb2p1UTFoZmNfYnZjR0Q2d2R3VnpodGhBdzJkRmdjZkw3QjZlOVR6ZlBQVXhBeWpoRTJmZTNkNmdNVXp3eEM5UTNSdm0xdUlYaW83RGp5MEd1VXluUWNkd09sQTk1RHB0eXk2dE1EcklNa2c?oc=5) ⭐️ 8.0/10

北京人工智能研究院（BAAI）发布了 Orca 世界模型，该模型在训练过程中从未使用动作标签，却达到了与专业机器人系统相当的性能。 这一突破减少了机器人领域昂贵且耗时的动作标注需求，有望加速通用机器人的开发，并降低 AI 研究的数据门槛。 Orca 采用下一状态预测范式，随模型大小和数据量有效扩展，产生更强的世界潜在表示，从而改进文本生成、图像预测和动作规划等下游任务。

google_news · the-decoder.com · 7月11日 09:07

**背景**: 世界模型是学习环境内部表示以预测未来状态的 AI 系统。传统机器人模型通常需要动作标签（即机器人正在执行什么动作的标注）来学习控制策略。Orca 通过仅从观测数据中学习，绕过了这一需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/orca">Orca : Unified Multimodal AI and Robotics</a></li>
<li><a href="https://hyper.ai/en/papers/2606.30534">Orca : The World is in Your Mind | Papers | HyperAI</a></li>
<li><a href="https://en.youth.cn/RightNow/202607/t20260708_16753288.htm">BAAI Releases RoboBrain Orca World Model _English__China Youth...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#world model`, `#AI`, `#machine learning`, `#China`

---

<a id="item-7"></a>
## [中国或限制海外访问顶尖 AI 模型](https://news.google.com/rss/articles/CBMidkFVX3lxTFBqaGRmWFlQdGxQcHVZOF94WTZOdEg3VERvNTMwSHlkMFhnazUyNFAwUmRyaHg5bkk4b1pGc2d6MWp3T1VfeEpYNFJySldkZ0ZnSFNqZUROR19MQmRDMXpyMktuTTlVdGktRFhWZmxsV2tZTmFtNmc?oc=5) ⭐️ 8.0/10

据《台北时报》报道，北京正在考虑限制海外访问中国顶尖 AI 模型。这一潜在政策变化可能限制全球开发者使用中国 AI 技术的能力。 此举可能通过减少跨境获取中国 AI 创新来重塑全球 AI 格局，可能减缓国际 AI 发展并加剧地缘政治技术竞争。它也可能影响依赖中国开源模型的公司和研究人员。 报道未说明哪些模型将受影响或实施时间表。该政策可能针对百度、阿里巴巴和腾讯等中国公司开发的先进 AI 模型。

google_news · Taipei Times · 7月11日 16:00

**背景**: 中国在 AI 领域快速进步，像文心一言和通义千问这样的模型已获得全球关注。目前，许多中国 AI 模型通过开源许可或 API 向国际开发者开放。限制访问将标志着向保护国内 AI 资产的重大转变。

**标签**: `#AI regulation`, `#geopolitics`, `#China`, `#AI models`, `#technology policy`

---

<a id="item-8"></a>
## [具身数据行业：97 家玩家，一年融资 44.7 亿](https://36kr.com/p/3892027841362694?f=rss) ⭐️ 7.0/10

量子位发布全面分析，统计了 97 家国内具身数据玩家，其中 15 家独立数据服务商在过去一年（2025 年 7 月至 2026 年 7 月）融资约 44.7 亿元。行业已形成四大数据采集技术路线：真机遥操、无本体采集、仿真合成和互联网视频蒸馏。 该分析首次系统梳理了中国具身数据行业图谱，表明该行业已成为独立于机器人公司的赛道。结果凸显了数据在训练具身 AI 模型中的关键作用，以及为解决数据稀缺问题而采取的多样化方法。 在 97 家玩家中，70 家专注于数据采集，27 家专注于数据基础设施。独立数据服务商是最大群体（39 家，占 40%），其次是国资数据平台（25 家，占 26%）。值得注意的是，67%的玩家是“具身原生”初创公司，33%是从 AI 数据标注或自动驾驶等领域跨界转型而来。

rss · 36氪 · 7月12日 02:16

**背景**: 具身 AI 需要大量真实世界交互数据用于训练，目前这些数据稀缺且采集成本高昂。常见采集方法包括遥操作（人类操控机器人）、无本体采集（人类佩戴传感器执行任务）、仿真合成（生成虚拟数据）以及从互联网视频中蒸馏知识。该行业仍处于早期阶段，尚无单一方法能完全满足需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://juejin.cn/post/7639399482463830026">绕不开的Ego-centric...</a></li>
<li><a href="https://www.21jingji.com/article/20260421/herald/acb40065512b137c5d49d7aac259c043.html">数 据 成机器人落地关键， 具 身 数 据 集 赛道火热 - 21经济网</a></li>
<li><a href="https://tech.ifeng.com/c/8uh5s4oHQ2h">tech.ifeng.com/c/8uh5s4oHQ2h</a></li>

</ul>
</details>

**标签**: `#embodied AI`, `#data collection`, `#robotics`, `#funding`, `#industry analysis`

---

<a id="item-9"></a>
## [Mistral AI 发布单摄像头导航模型](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBuODdfOFZITFJmb0FyNW00TkZEdUtFYzVxWnV5bWxCY1dRc3hnVjdFUVpqNHRnWDBGVUMzYXViZ1ViVEVCR216YzNOZ0lDbXZHMGNnUW93?oc=5) ⭐️ 7.0/10

Mistral AI 宣布推出 Robostral Navigate，这是一个 8B 参数的视觉-语言-动作模型，使机器人仅凭单个 RGB 摄像头和自然语言指令就能在复杂环境中导航。 这种方法降低了硬件成本并简化了机器人设计，可能加速自主机器人在仓库、家庭等不便于使用深度传感器的场景中的部署。 Robostral Navigate 在未见过的环境中实现了 76.6% 的成功率，该模型旨在遵循自然语言指令完成具身导航任务。

google_news · mistral.ai · 7月12日 03:02

**背景**: 传统机器人导航通常依赖多个摄像头或昂贵的深度传感器（如 LiDAR）。视觉-语言-动作模型将视觉感知、语言理解和运动控制整合到单个神经网络中，实现更直观的人机交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/robostral-navigate/">Robostral Navigate : single-camera AI navigation | Mistral AI</a></li>
<li><a href="https://www.youtube.com/watch?v=7dpLB9NoY1A">Introducing Robostral Navigation - YouTube</a></li>
<li><a href="https://quasa.io/media/mistral-robostral-navigate-single-camera-8b-model-transforms-robot-autonomy">Mistral Robostral Navigate : Single-Camera Robot Autonomy in 2026</a></li>

</ul>
</details>

**标签**: `#AI`, `#navigation`, `#robotics`, `#computer vision`

---

<a id="item-10"></a>
## [蚂蚁集团开源机器人大脑，性能超越 pi0.5](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOTGctdHQtSWdvbEFSVXlaWE9qSmFPUjVqWHB1d0lBMDFQWE5kcjd0OGt0WmpUVzZCRWNzVUNVX3pFYW1zc2lJaWswbmZmejlJVGNEOVdzamJGMUtlOXNZQkpNMEd4bWtxVEdpSDMwUjB0TncyU3RfWWJ3cWUzcWFBcVRnZ0lJcWtHWGFSSENvVF91WS1EU3liS21MejNHQTJZalNWZ1dFS2RiWm92M0F5ZGJwQ1FVZmhjWlZtQ1ZJMzlLT1U?oc=5) ⭐️ 7.0/10

蚂蚁集团开源了一个通用机器人大脑，在 20 种不同硬件类型上性能均超越 pi0.5，标志着具身智能领域的重要进展。 这一开源发布可能加速机器人开发，通过提供高性能、硬件无关的 AI 大脑，减少定制方案的需求，降低研究人员和开发者的入门门槛。 该机器人大脑是蚂蚁集团 Robbyant 具身 AI 栈的一部分，包含感知和通用大脑。它仅用一周时间就完成了开源，展示了快速开发能力。

google_news · Tech Times · 7月11日 15:00

**背景**: 具身智能指能够通过机器人身体与物理世界交互的 AI 系统。pi0.5 是此前最先进的机器人 AI 模型。由马云支持的蚂蚁集团正扩展至机器人领域，近期发布了 R1 人形机器人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scmp.com/tech/big-tech/article/3341842/ant-groups-open-source-push-aims-move-robots-lab-demos-real-world-work">Ant Group's open-source push aims to move robots from lab demos to real ...</a></li>
<li><a href="https://thenextweb.com/news/robbyant-ant-group-lingbot-embodied-ai-open-source">Ant Group open-sourced a whole robot brain in a week - TNW</a></li>

</ul>
</details>

**标签**: `#robotics`, `#open-source`, `#AI`, `#hardware`

---

<a id="item-11"></a>
## [Mozilla.ai 发布开源 LLM 控制平面 Otari](https://news.google.com/rss/articles/CBMimAFBVV95cUxNRWdQNjJ5VDRwNWswcWtocHN5T2t0OERrSUM3M0oyS1BFbkpDSWdobzFaeHBSLWJWS01vUTJPRi1pb3l3QkJQRkY1TmM4SlF4dEhLR29jdUdyb1VpbjU4aDc5bFFJeTFhenpXR3ZtRFRXb3FrRjlfNlBocF9scnIzYUtCV1VndWtIMzZOSVhMY1U4dXJNVWFNcw?oc=5) ⭐️ 7.0/10

Mozilla.ai 发布了 Otari，这是一个用于管理大语言模型（LLM）操作的开源控制平面，支持跨多个提供商的路由、预算、治理和部署。 Otari 填补了 LLM 流量缺乏专用控制平面的空白，使开发者和工程团队能够更高效、安全地管理 LLM 基础设施，可能加速企业对 LLM 的采用。 Otari 提供托管护栏以确保 LLM 安全、智能路由为每个请求选择最佳模型（本地或远程），以及可选的 otari.ai 代码执行。它基于 any-llm 构建，并且是开源的。

google_news · StartupHub.ai · 7月11日 19:23

**背景**: LLM 控制平面是一个集中式系统，用于管理 LLM 请求的路由、安全和治理，类似于 API 网关但专为生成式 AI 工作负载构建。此前，LLM 流量缺乏这样的专用工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mozilla.ai/product/otari">Otari : A centralized control plane for LLM operations</a></li>
<li><a href="https://blog.mozilla.ai/introducing-otari-the-open-source-llm-control-plane/">Introducing Otari : The Open-Source LLM Control Plane</a></li>
<li><a href="https://blog.mozilla.ai/what-is-an-llm-control-plane/">What is an LLM control plane ?</a></li>

</ul>
</details>

**标签**: `#Mozilla`, `#LLM`, `#control plane`, `#AI infrastructure`

---

<a id="item-12"></a>
## [GitHub API 遭滥用：50 多个幽灵账户发起侦察行动](https://news.google.com/rss/articles/CBMifkFVX3lxTE9vVF9iWmMxMFA0N0Z1U2gyUFgyWFh2ZjZUbEU0RkFpaDVCcFZHZXcyTEh5VncxVWJUMUFMcTdkZllEUWdWTUhXX25QNzlmX0J4eFZQaTc2VEpZNVJ5SDNyT1hxR1VyTElpdkw5NEJ0dGx2VHZ2b3l4UHR5TW5ndw?oc=5) ⭐️ 7.0/10

安全研究人员发现了一场大规模侦察活动，超过 50 个幽灵账户滥用 GitHub API 来发现组织的仓库和成员。 这凸显了利用 API 进行情报收集的趋势日益增长，对 GitHub 等协作平台上组织的数据隐私和安全构成风险。 这些幽灵账户以协调方式运行，抓取仓库元数据和成员列表，可能用于定向攻击或竞争情报。

google_news · SecNews.gr · 7月11日 17:49

**背景**: GitHub 是一个广泛使用的软件开发和协作平台，托管着数百万个仓库。幽灵账户是用于逃避检测的虚假或被盗账户。API 滥用涉及利用合法接口提取超出预期限制的数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.securityweek.com/ghost-accounts-abuse-github-api-in-mass-recon-campaign/">Ghost Accounts Abuse GitHub API in Mass Recon ... - SecurityWeek</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#API abuse`, `#security`, `#reconnaissance`

---

<a id="item-13"></a>
## [Ghostcommit 攻击将恶意提示隐藏在图像中](https://news.google.com/rss/articles/CBMicEFVX3lxTE1mcXBSQlU4dFpheUQtVmNCeUNaX3VTVmZIaDI3QklxYTlHU2RTSjJtVjZoWkRpQWpSdmJYelllNi0xVVNjZkFCSlF4UG5LODd0RjBBdEZjb3EtODl1MGl2X0x2a0NxN3VHMVVqTWtaX2PSAbsCQVVfeXFMT2ctQ0tfU2JmQU54NHVZMnlENE1kZHBMeEQ3dF9RRVhlYzN2SHZrSnpJSUxneVJkbnUwM3dzYU8zbGJ5MmJJcEVTQTVzTXFRS0VLekNFM3ROTFZOMXhuZ3REdDI0bHBJRkpwdEtySjFvUVIwVnFuS2FoOS1wVENXdmhvTlcwdjVMQ1Q4eDJWNHBKbkxSamtaSVJzTTRQVHhaYkVpRlNMNkN2SG80cl90ZG9zejNVNGdTdWJUenVDR3Q4MXZycGcwRHVkRi0zRnNOTnZwUHpjeWs3ejM4MWdMc3JwSkV3Ni03OHBHR0RlRmZld3ZuZTZMTVlzeUtrekVWeWluYTM3cFRjTVRwOTVzQVJkZUhKQ0VZYmloaTNxX1Fpd2lQYjBCcHFFY0JZZjZNNHAtUkxGWGFmZVVV?oc=5) ⭐️ 7.0/10

研究人员发现了一种名为 Ghostcommit 的新型供应链攻击，它利用隐写术将恶意提示注入指令隐藏在 PNG 图像中，针对 AI 代码审查员和编码代理。 这种攻击代表了利用 AI 代理的新途径，绕过了传统安全措施，可能导致 CI/CD 流水线中的秘密泄露或未经授权的操作。 该攻击将提示注入指令嵌入到 AI 代理（如代码审查员）处理的图像文件中，然后执行隐藏的命令。它凸显了 AI 安全中隐写术攻击日益增长的威胁。

google_news · CyberSecurityNews · 7月11日 16:30

**背景**: 提示注入是一种攻击类型，将恶意指令插入 AI 模型输入以改变其行为。隐写术是将数据隐藏在其他数据（如图像）中的做法。Ghostcommit 结合了这些技术，针对软件开发工作流中的 AI 代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/ghostcommit-attack-hides-prompts/">New Ghostcommit Attack Hides Malicious Prompts in Images to...</a></li>
<li><a href="https://europeanpurpose.com/news/ghostcommit-the-ai-prompt-injection-attack-hiding-inside-your-repository-s-image">Ghostcommit : The AI Prompt Injection Attack ... | European Purpose</a></li>

</ul>
</details>

**标签**: `#AI security`, `#prompt injection`, `#steganography`, `#cybersecurity`, `#adversarial attack`

---

<a id="item-14"></a>
## [SK 海力士 CEO 预计 HBM 价格 2027 年翻倍](https://36kr.com/newsflashes/3892093059873544?f=rss) ⭐️ 6.0/10

SK 海力士 CEO 郭鲁正预测，由于供应紧张和需求强劲，HBM 价格将在 2027 年翻倍，并指出客户正在寻求长期供货协议。 这一预测表明，对 AI 加速器至关重要的 HBM 内存将长期供应紧张，可能影响 AI 基础设施的成本和时间表。同时，它也凸显了中国存储厂商（如长鑫存储和长江存储）日益增长的竞争威胁。 SK 海力士控制着全球 62%的 HBM 出货量，并在 2025 年中期之前售罄了 2026 年的全部产能。该公司已承诺投资约 130 亿美元建设新工厂，并投入 100 亿美元用于美国 AI 投资部门。

rss · 36氪 · 7月12日 03:58

**背景**: 高带宽内存（HBM）是一种先进的存储技术，通过硅通孔（TSV）垂直堆叠 DRAM 芯片以实现超高带宽，对 AI 和图形处理至关重要。SK 海力士是 HBM 的主要供应商，但中国存储制造商正在快速扩大产能，这可能重塑全球存储市场格局。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.sedaily.com/finance/2026/04/23/sk-hynix-says-hbm-demand-to-outstrip-supply-for-next-3-years">SK hynix Says HBM Demand to Outstrip Supply for Next 3 Years</a></li>
<li><a href="https://nextwavesinsight.com/hbm-memory-bottleneck-ai-supply-chain-2026/">HBM 's Thermal Wall: Why One Korean... - Next Waves Insight</a></li>
<li><a href="https://www.astutegroup.com/news/memory-shortages/chinas-memory-expansion-reshapes-global-dram-and-nand-competition/">China ’s memory expansion reshapes global DRAM... - Astute Group</a></li>

</ul>
</details>

**标签**: `#HBM`, `#memory`, `#semiconductor`, `#SK Hynix`, `#supply chain`

---

<a id="item-15"></a>
## [三星将龙仁芯片工厂投产提前至 2029 年](https://36kr.com/newsflashes/3892091542288904?f=rss) ⭐️ 6.0/10

三星电子计划将其龙仁芯片集群首座工厂的投产时间提前至 2029 年，比原计划提早一至两年，以满足日益增长的人工智能芯片需求。 这一加速使三星能够更快地应对全球对人工智能芯片的激增需求，增强其在半导体市场中对台积电和 SK 海力士等竞争对手的竞争地位。 龙仁集群是三星更广泛投资计划的一部分，该计划包括对平泽和龙仁集群投资 2030 万亿韩元（约合 1.35 万亿美元），并在光州投资 400 万亿韩元建设两座新芯片工厂。

rss · 36氪 · 7月12日 03:39

**背景**: 三星电子是全球半导体制造领导者，生产存储芯片和逻辑芯片。龙仁集群是一个大型扩建项目，旨在提升先进芯片（尤其是 AI 加速器）的产能。加速时间表反映了 AI 芯片市场的激烈竞争。

**标签**: `#Samsung`, `#semiconductor`, `#AI chips`, `#manufacturing`

---

<a id="item-16"></a>
## [英伟达将机器人 AI 引入 Hugging Face](https://news.google.com/rss/articles/CBMiywFBVV95cUxONkNhcF82TzdWOUpRU2RsNGpEQTIxMnNSZko1RlhGUUwxNE9qUWFFR1N2Q1lKak5WWFFCNWRITGlwWUFCR01nNW1adjVmSDAxN0hGLTJQSnc0SnJGZGc3NEJ3VzVpNHhobGZBZGpLejJXcnFkZWZ3Z3l4dFlBX2RRWC1WVnRaOXBSUEtQQ0haMnhvbkRXSUV6VHYwWTl2X0FiWWoyVnMwcnRPUXlMeFp6ZGlqcXUtd2g4ZDVoNHFfV3Zkdk52eFJLREp4ONIB0AFBVV95cUxOQVFqX1RXN0Q5ZzJqQVJ4aUNuT1daTE5zT0xfVE5WMXZrcm91YUtXTDluOTdpaFVyUk5Sa2xKdmN3b09tWmRZcm82M0I3OTBtbnNxNXBBWERLVnpMUEd4RktGU1dELTZKcFJVcGFpVXViWHVGOWg4OUI4LTVSTjZJa1B0dzVQd05uSTRlb1RmMFZUZ1lWMmJlOThMTWZOanRmZ2U1d3hzOXFvSWZjYjRNTkdfLXpUVlRVYURpTnVMZHpqa1JBY2M0a0xTMDFyNldM?oc=5) ⭐️ 6.0/10

英伟达与 Hugging Face 合作，将其机器人 AI 能力集成到 Hugging Face 平台，同时法国对英伟达的反垄断调查也宣告结束。 这一合作使先进的机器人 AI 工具更加普及，开发者和研究人员能够利用 Hugging Face 生态系统更轻松地构建和部署 AI 驱动的机器人。 该集成可能利用了英伟达的 Isaac 平台和 Hugging Face 的 LeRobot 库，后者提供机器人 AI 的数据集和工具。法国调查的结束消除了英伟达在欧洲运营的监管不确定性。

google_news · simplywall.st · 7月11日 14:45

**背景**: Hugging Face 是一个流行的机器学习模型和数据集共享平台，最近发布了开源机器人模型 SmolVLA。英伟达提供 AI 和机器人的硬件与软件，包括用于仿真和部署的 Isaac 平台。此次合作旨在将英伟达的机器人专业知识与 Hugging Face 的社区驱动模型共享相结合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/learn/robotics-course/unit0/1">Welcome to the Robotics Course · Hugging Face</a></li>
<li><a href="https://github.com/huggingface/lerobot">GitHub - huggingface/lerobot: LeRobot: Making AI for Robotics ...</a></li>
<li><a href="https://techcrunch.com/2025/06/04/hugging-face-says-its-new-robotics-model-is-so-efficient-it-can-run-on-a-macbook/">Hugging Face says its new robotics model is so... | TechCrunch</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#Hugging Face`, `#robotics AI`, `#partnership`

---