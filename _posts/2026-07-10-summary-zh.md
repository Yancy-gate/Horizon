---
layout: default
title: "Horizon Summary: 2026-07-10 (ZH)"
date: 2026-07-10
lang: zh
---

> 从 95 条内容中筛选出 12 条重要资讯。

---

1. [AI 生成视频以最大程度激活特定脑区](#item-1) ⭐️ 9.0/10
2. [OpenAI 发布 GPT-5.6 系列：Luna、Terra、Sol](#item-2) ⭐️ 9.0/10
3. [语义对齐在机器人视频分词中超越 VAE](#item-3) ⭐️ 9.0/10
4. [欧盟：Instagram 和 Facebook 的成瘾设计违反 DSA](#item-4) ⭐️ 8.0/10
5. [《自然》指南对比 AI 科学家工具，助力实验室选型](#item-5) ⭐️ 8.0/10
6. [大规模研究发现预印本可靠](#item-6) ⭐️ 8.0/10
7. [实验室用小鼠肾脏培育出干细胞来源精子](#item-7) ⭐️ 8.0/10
8. [NSF 计划削减核心科学项目以资助白宫倡议](#item-8) ⭐️ 8.0/10
9. [中国首次成功着陆可重复使用火箭](#item-9) ⭐️ 8.0/10
10. [GoPro 自行车相机实现地理参考道路检测](#item-10) ⭐️ 8.0/10
11. [Nilay Patel：AR 眼镜需要隐私权衡](#item-11) ⭐️ 7.0/10
12. [新基础设施实现 AI 在机器人间的迁移](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI 生成视频以最大程度激活特定脑区](https://nevo-project.epfl.ch/) ⭐️ 9.0/10

EPFL 的研究人员开发了 NEvo，这是一个 AI 系统，利用基于 fMRI 数据训练的数字孪生模型，生成优化以最大程度激活特定脑区的视频。 这一突破为神经科学研究提供了强大工具，能够精确绘制脑功能图谱，并可能带来神经系统疾病的新疗法，同时也引发了关于在社交媒体或广告中滥用的伦理担忧。 该系统首先训练一个编码模型（数字孪生），预测任何视频对脑区的响应，然后以该模型作为奖励函数，搜索能最大程度激活选定脑区的视频。该方法通过让 AI 在没有人类先入为主观念的情况下发现刺激，减少了实验者偏差。

hackernews · smusamashah · 7月10日 07:39 · [社区讨论](https://news.ycombinator.com/item?id=48856904)

**背景**: 功能性磁共振成像（fMRI）通过检测血流变化来测量大脑活动。数字孪生是一个模拟真实系统的虚拟模型；在这里，它预测视觉脑区对视频的响应。NEvo 利用这个孪生模型生成新颖的视频刺激，超越了依赖现有视频的传统方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nevo.systems/">Nevo — Self-Improving AI That Evolves With You</a></li>

</ul>
</details>

**社区讨论**: 评论者既兴奋又担忧：一些人强调了社交媒体平台可能滥用该技术制作成瘾性内容，而另一些人则强调该工具对无偏神经科学研究的价值。少数人指出这与最近的读心 AI 相似，并强调阅读论文以理解科学意图的重要性。

**标签**: `#AI`, `#neuroscience`, `#video generation`, `#brain-computer interface`, `#ethics`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT-5.6 系列：Luna、Terra、Sol](https://simonwillison.net/2026/Jul/9/gpt-5-6/#atom-everything) ⭐️ 9.0/10

OpenAI 于 2026 年 7 月 9 日发布了 GPT-5.6 系列模型，包括三个尺寸：Luna（最小）、Terra（中等）和 Sol（最大）。这些模型拥有 100 万 token 的上下文窗口、12.8 万输出 token，并在 Agents' Last Exam 基准测试中宣称具有强大的智能体性能。 此次发布加剧了与 Anthropic 的 Claude 模型在智能体 AI 能力上的竞争，并提供了分层定价，可能使先进 AI 更易获取。新的 API 功能（如编程式工具调用和多智能体支持）可能重塑开发者构建 AI 应用的方式。 每百万 token 定价为 Luna $1/$6、Terra $2.50/$15、Sol $5/$30（输入/输出）。在 Agents' Last Exam 上，Sol 得分为 53.6，比 Claude Fable 5 高 13.1 分；但在 SWE-Bench Pro 上，Fable 5 得分为 80%，而 Sol 为 64.6%。OpenAI 还发表了对 SWE-Bench Pro 的批评，估计约 30% 的任务存在缺陷。

rss · Simon Willison · 7月9日 19:46

**背景**: GPT-5.6 是 OpenAI 最新的旗舰模型系列，继两个月前发布的 GPT-5.5 之后推出。这些模型专为智能体任务设计，即 AI 系统自主执行多步骤工作流。Agents' Last Exam 是一个评估长期、具有经济价值且结果可验证任务的基准测试。推理 token 是模型在生成最终响应前用于规划和推理的内部 token，其数量在不同模型间可能差异很大，使得每 token 价格比较变得不那么直接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6/">GPT - 5 . 6 : Frontier intelligence that scales with your ambition | OpenAI</a></li>
<li><a href="https://arxiv.org/abs/2606.05405">Abstract page for arXiv paper 2606.05405: Agents ' Last Exam</a></li>
<li><a href="https://snorkel.ai/leaderboard/agents-last-exam/">Agents ' Last Exam | Snorkel AI</a></li>

</ul>
</details>

**社区讨论**: 文章作者指出，GPT-5.6 Sol 能力不错，但在复杂编码任务上尚未超越 Claude Fable 5。社区可能会讨论 SWE-Bench Pro 等基准测试的有效性，尤其是考虑到 OpenAI 自身的批评。

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI models`, `#benchmarks`, `#agentic AI`

---

<a id="item-3"></a>
## [语义对齐在机器人视频分词中超越 VAE](https://www.reddit.com/r/computervision/comments/1ustn7f/aligning_video_latents_to_a_frozen_perception/) ⭐️ 9.0/10

一种新的机器人视频-动作模型分词器设计，通过添加语义对齐损失将视频潜在表示拉向冻结的感知编码器（如 DINOv2），在 50 任务双臂基准测试中平均成功率达到 86.6%，而普通重建 VAE 为 78.0%。随着预测时间跨度增加，差距扩大，在时间跨度 3 时达到 92.0%对 67.2%。 这一结果表明，将视频潜在表示与冻结的感知编码器对齐是一种简单而强大的替代重建式分词的方法，显著提升了机器人领域的长期动作预测能力。这种将强编码器冻结作为对齐目标的方法可能推广到机器人之外的其它序列预测任务。 该分词器保留了重建目标，但增加了语义对齐损失和一个潜在动作项，用于提取帧间的紧凑过渡变量。78.0 到 86.6 的提升来自仿真环境；论文中的真实机器人视频是内部演示，并非独立证据。

reddit · r/computervision · /u/AbbreviationsEast776 · 7月10日 17:06

**背景**: 视频分词是机器人学习中的关键组件，它将视频帧压缩成潜在表示以供下游动作预测。传统的重建 VAE 旨在最小化像素级误差，但可能丢弃对长期任务至关重要的语义信息。像 DINOv2 这样的冻结感知编码器无需微调即可提供丰富的语义特征，将潜在表示与之对齐可以保留这些信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.arxiv.org/pdf/2512.04483">DeRA: Decoupled Representation Alignment for Video Tokenization Pengbo Guo1,2</a></li>
<li><a href="https://arxiv.org/abs/2410.11758">[2410.11758] Latent Action Pretraining from Videos</a></li>
<li><a href="https://arxiv.org/pdf/2504.13181">Perception Encoder: The best visual embeddings are not at ...</a></li>

</ul>
</details>

**社区讨论**: Reddit 帖子作者注意到随着时间跨度增加差距扩大，并询问在控制任务之外是否也能获得同样的长期收益。他们还提醒主要结果来自仿真，真实机器人演示应视为展示而非独立证据。

**标签**: `#video tokenization`, `#representation learning`, `#robotics`, `#perception encoder`, `#VAE`

---

<a id="item-4"></a>
## [欧盟：Instagram 和 Facebook 的成瘾设计违反 DSA](https://ec.europa.eu/commission/presscorner/home/en) ⭐️ 8.0/10

欧盟委员会初步认定，Meta 旗下的 Instagram 和 Facebook 平台因其成瘾性设计功能违反了《数字服务法案》（DSA）。 这标志着 DSA 首次针对成瘾性设计采取重大执法行动，可能迫使 Meta 重新设计核心用户界面，并为欧盟范围内监管算法操纵树立先例。 初步认定聚焦于无限滚动、缺乏充分透明度的个性化推荐，以及利用心理弱点最大化用户参与度的通知系统等功能。

hackernews · jeroenhd · 7月10日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=48858292)

**背景**: 《数字服务法案》（DSA）是 2022 年生效的欧盟法规，要求大型在线平台评估并缓解成瘾性设计等系统性风险。成瘾性设计指故意延长用户参与度的 UI/UX 模式，通常通过可变奖励和吸引注意力的通知来实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_Services_Act">Digital Services Act - Wikipedia</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/digital-services-act">The Digital Services Act | Shaping Europe’s digital future</a></li>
<li><a href="https://edaa.eu/digital-services-act/">What is DSA: The Digital Services Act Explained - EDAA</a></li>

</ul>
</details>

**社区讨论**: 评论者就执法方式展开辩论：一些人主张强制用户在成瘾性算法和道德算法之间做出选择，而另一些人则支持委员会降低成瘾性的重点。有用户指出 Instagram 的算法重置选项有助于减少无意识滚动，还有人强调以参与度优化的界面与可关闭的时间限制弹窗之间存在不匹配。

**标签**: `#regulation`, `#social media`, `#DSA`, `#addictive design`, `#EU`

---

<a id="item-5"></a>
## [《自然》指南对比 AI 科学家工具，助力实验室选型](https://www.nature.com/articles/d41586-026-02091-6) ⭐️ 8.0/10

《自然》杂志发布了一份指南，比较了如 Claude Science 等通用 AI 科研工具，帮助研究人员为实验室选择合适的工具。 随着 AI 工具在研究领域的普及，这份指南满足了及时需求，帮助实验室做出明智选择，加速科学发现。 Claude Science 是一个公开测试版应用，集成了常用的科学工具和包，生成可审计的产物，并提供灵活的计算资源访问。其他工具如 Gemini for Science 也提供专门功能。

rss · Nature 研究亮点 · 7月10日 00:00

**背景**: 通用 AI 科研工具（如 Claude Science）通过自动化数据分析和文献综述等任务，有望加速研究。然而，研究人员需要指导来应对日益增多的选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://claude.com/product/claude-science">Claude Science beta | Claude by Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#science`, `#research tools`, `#Nature`

---

<a id="item-6"></a>
## [大规模研究发现预印本可靠](https://www.nature.com/articles/d41586-026-02167-3) ⭐️ 8.0/10

一项由《自然》杂志委托、对 7 万篇生物医学预印本的分析发现，这些预印本的核心结论在经同行评审发表后很少发生变化，这挑战了人们对预印本可靠性的普遍怀疑。 这一发现支持了使用预印本快速传播研究成果的做法，尤其是在生物医学等快速发展的领域，并可能改变研究人员和公众对开放科学实践的信任。 该分析将预印本与其最终发表版本进行了比较，重点关注核心结论的变化，而非细微的文字编辑。

rss · Nature 研究亮点 · 7月10日 00:00

**背景**: 预印本是在同行评审前公开发布的未经评审的手稿。在 COVID-19 大流行期间，其使用量激增，引发了对其可靠性的担忧。这项研究提供了大规模证据，表明预印本通常是可信的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://casrai.org/news/preprint-vs-peer-review/">Preprint vs Peer Review : What 40 Studies Show — CASRAI</a></li>
<li><a href="https://journalistsresource.org/media/two-studies-examine-preprints/">How different are preprints from their published versions?</a></li>

</ul>
</details>

**标签**: `#preprints`, `#biomedical research`, `#open science`, `#reproducibility`, `#peer review`

---

<a id="item-7"></a>
## [实验室用小鼠肾脏培育出干细胞来源精子](https://www.nature.com/articles/d41586-026-02172-6) ⭐️ 8.0/10

科学家通过将干细胞植入小鼠肾脏，成功培育出未成熟的人类精子细胞，标志着体外精子生成研究迈出一步。 该过程将精原干细胞（SSCs）置于小鼠肾脏中，肾脏提供了分化所需的微环境，使其发育为未成熟精子。这些精子尚未完全成熟或具备功能。

rss · Nature 研究亮点 · 7月10日 00:00

**背景**: 精子发生是一个复杂过程，需要睾丸细胞提供特定信号。体外精子生成旨在体外重现这一过程。先前尝试仅达到早期阶段；使用活体器官作为生物反应器是一种新方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/In_vitro_spermatogenesis">In vitro spermatogenesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spermatogonial_stem_cell">Spermatogonial stem cell - Wikipedia</a></li>

</ul>
</details>

**标签**: `#stem cells`, `#fertility`, `#reproductive biology`, `#biotechnology`

---

<a id="item-8"></a>
## [NSF 计划削减核心科学项目以资助白宫倡议](https://www.nature.com/articles/d41586-026-02135-x) ⭐️ 8.0/10

美国国家科学基金会（NSF）提议削减核心科学项目的资金，并收回已分配的研究经费，以资助一项白宫倡议，此时该机构正面临严重的预算压力和不断增加的拨款申请积压。 这一政策转变可能扰乱正在进行的研究项目，并减少美国科学家未来的资助机会，可能削弱国家的科学竞争力和创新能力。 拟议中的收回已分配资金的做法史无前例，此时 NSF 正面临拨款积压和人员减少的困境；该机构已放宽了一些拨款审查规则以应对积压。

rss · Nature 研究亮点 · 7月10日 00:00

**背景**: 美国国家科学基金会（NSF）是美国政府资助科学和工程基础研究与教育的主要机构。近年来，该机构面临预算限制，其 2024 财年预算为 90.6 亿美元。同时，NSF 还在应对拨款申请积压和人员减少的问题，因此调整了审查流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/d41586-025-04067-4">NSF softens grant-review rules to cope with backlog</a></li>
<li><a href="https://www.nsf.gov/resumption-operations">Resumption of Operations at NSF | NSF - U.S. National Science Foundation</a></li>

</ul>
</details>

**标签**: `#NSF`, `#research funding`, `#science policy`, `#US government`

---

<a id="item-9"></a>
## [中国首次成功着陆可重复使用火箭](https://www.bbc.co.uk/news/articles/cm2rmmx86pdo?at_medium=RSS&at_campaign=rss) ⭐️ 8.0/10

据官方媒体报道，中国首次成功着陆了一枚可重复使用火箭，标志着该国航天技术发展的一个里程碑。 这一成就使中国成为继 SpaceX 和蓝色起源之后少数掌握可重复使用火箭技术的国家之一，有望降低发射成本并增加进入太空的机会。 此次着陆紧随美国公司 SpaceX 和蓝色起源的类似成就之后，但关于火箭型号、着陆方式和日期的具体细节尚未披露。

rss · BBC World News · 7月10日 06:44

**背景**: 可重复使用火箭旨在发射后着陆，以便回收其部件并再次飞行，从而大幅降低进入太空的成本。SpaceX 的猎鹰 9 号一级着陆和蓝色起源的新谢泼德亚轨道着陆是开创性范例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Reusable_launch_vehicle">Reusable launch vehicle - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_reusable_launch_system_development_program">SpaceX reusable launch system development program - Wikipedia</a></li>

</ul>
</details>

**标签**: `#space technology`, `#reusable rockets`, `#China`, `#aerospace`

---

<a id="item-10"></a>
## [GoPro 自行车相机实现地理参考道路检测](https://www.reddit.com/r/computervision/comments/1uslmex/turn_a_gopro_on_a_bike_into_a_georeferenced/) ⭐️ 8.0/10

一位开发者创建了一个流程，仅使用安装在自行车上的单个 GoPro 相机，无需 LiDAR 或立体相机，即可生成道路表面缺陷的度量级地理参考测量。 这种方法大幅降低了道路状况检测的成本和复杂性，使市政部门和公民科学家都能使用。它同时也推动了单目深度估计在实际度量应用中的进展。 该流程通过迭代优化拟合，解决了单目深度估计中地平面漂移的挑战。作者指出它并不完美，但分享当前进展以鼓励社区反馈。

reddit · r/computervision · /u/k4meamea · 7月10日 12:00

**背景**: 单目深度估计从单个 2D 图像推断 3D 结构，但度量尺度和地理参考通常需要 LiDAR 或 GPS/INS 等额外传感器。地平面漂移是指估计的地平面随时间逐渐偏离真实表面，这是长距离单目重建中的常见问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2312.06021">GenDepth: Generalizing Monocular Depth Estimation for Arbitrary...</a></li>
<li><a href="https://www.emergentmind.com/topics/ground-aware-monocular-perception">Ground -Aware Monocular Perception</a></li>
<li><a href="https://www.aimodels.fyi/papers/arxiv/monopp-metric-scaled-self-supervised-monocular-depth">MonoPP: Metric-Scaled Self-Supervised Monocular Depth Estimation ...</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#monocular depth estimation`, `#road surveying`, `#georeferencing`, `#open source`

---

<a id="item-11"></a>
## [Nilay Patel：AR 眼镜需要隐私权衡](https://simonwillison.net/2026/Jul/10/nilay-patel/#atom-everything) ⭐️ 7.0/10

Nilay Patel 认为，实用的增强现实眼镜必须持续记录并将摄像头数据发送到云端处理，因为目前没有设备端芯片能满足功耗和性能要求。他警告这本质上侵犯了用户隐私，并质疑是否应该制造这类产品。 这一评论凸显了 AR 创新与隐私之间的根本矛盾，影响了 Meta、苹果和谷歌等开发 AR 眼镜的公司。它迫使社会进行关键辩论：无处不在的 AR 的隐私代价是否可接受。 Patel 指出，当前的选择要么是依赖云端的眼镜，要么是像 Apple Vision Pro 那样带有外部电池组的笨重设备。他强调，没有足够小的芯片能放入眼镜腿中实现本地实时处理。

rss · Simon Willison · 7月10日 17:05

**背景**: 增强现实眼镜将数字信息叠加到现实世界，需要持续的摄像头输入和实时处理。设备端处理保护隐私但受限于电池和散热，而云端处理功能更强但引发隐私担忧。Meta 和苹果等公司正在竞相开发轻量级 AR 眼镜，但技术障碍依然存在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://floridareading.com/blogs/news/on-device-vs-cloud-processing-which-privacy-model-protects-your-visual-data-better">On - Device vs Cloud Processing : Which Privacy Model Protects Your...</a></li>
<li><a href="https://www.rayneo.com/blogs/news/ai-powered-smart-glasses-what-artificial-intelligence-actually-does-for-you">AI-Powered Smart Glasses : What Artificial Intelligence Actually Does...</a></li>
<li><a href="https://inairspace.com/blogs/learn-with-inair/machine-learning-vs-augmented-reality-the-silent-war-for-our-digital-future">Machine Learning vs Augmented Reality: The Silent War for Our Digital...</a></li>

</ul>
</details>

**标签**: `#augmented reality`, `#privacy`, `#cloud computing`, `#hardware`

---

<a id="item-12"></a>
## [新基础设施实现 AI 在机器人间的迁移](https://news.google.com/rss/articles/CBMic0FVX3lxTE1JWEpNTXV2bEJhY0djZ1ZmWDRZU3ZOWGNYNFFqQU9fR09yNUNPSTgxTE5ZNGowMTZick1kSFJCLW1MS3V2MjAzV3BIbHo5Y3pfWHNnTURsaUF3OHl5amZ6eFlxNml0R2FseVNKbU1KSERiM3M?oc=5) ⭐️ 7.0/10

研究人员开发了一种缺失的基础设施，使得 AI 模型能够在不同机器人平台之间迁移和运行，无需大量重新工程。 这一突破解决了机器人 AI 部署的关键瓶颈，可能加速 AI 在多样化机器人系统中的采用，并降低开发成本。 该基础设施可能涉及标准化接口或中间件，以抽象硬件差异，类似于其他领域中用于模型可移植性的 ONNX。

google_news · Tech Xplore · 7月10日 12:20

**背景**: 目前，为一个机器人训练的 AI 模型通常无法直接用于另一个机器人，因为硬件、传感器和控制系统存在差异。这种碎片化迫使开发者为每个平台重新训练或调整模型，拖慢了创新。模型可移植性是 AI 领域公认的挑战，通用 AI 领域已出现 ONNX 等解决方案，但机器人领域一直缺乏类似标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aicompetence.org/modelcat-ai-announces-ai-model-portability-across-silicon-devices/">ModelCat AI Announces AI Model Portability Across Silicon Devices</a></li>
<li><a href="https://www.linkedin.com/pulse/onnx-unlock-ai-model-portability-accelerate-inference-rahim-khoja-xotuc">ONNX: Unlock AI Model Portability , Accelerate Inference, and...</a></li>
<li><a href="https://neuralwired.com/2026/04/05/agentic-ai-robotics-deployment/">Agentic AI Robotics Deployment : Why 70% Fail in 2026</a></li>

</ul>
</details>

**标签**: `#robotics`, `#AI`, `#model portability`, `#infrastructure`

---