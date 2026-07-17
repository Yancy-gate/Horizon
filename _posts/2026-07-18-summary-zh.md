---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 146 条内容中筛选出 23 条重要资讯。

---

1. [Firefox 编译为 WebAssembly 并在浏览器中运行](#item-1) ⭐️ 9.0/10
2. [Ultralytics v8.4.97 新增直接 Hailo HEF 导出](#item-2) ⭐️ 8.0/10
3. [首次在宜居带岩石系外行星发现大气层](#item-3) ⭐️ 8.0/10
4. [Kimi K3 与鹈鹕基准测试：隐藏提示与评估局限](#item-4) ⭐️ 8.0/10
5. [模感科技获数千万元天使轮融资，研发机器人全身触觉皮肤](#item-5) ⭐️ 8.0/10
6. [前蔚来、华为智驾核心成员获数亿元融资，打造具身世界模型](#item-6) ⭐️ 8.0/10
7. [MIT 研究修正 20 世纪美国 GDP 增长](#item-7) ⭐️ 8.0/10
8. [火星车仪器无需样本返回即可探测生物特征](#item-8) ⭐️ 8.0/10
9. [习近平将公布全球 AI 愿景，华为推出英伟达竞品](#item-9) ⭐️ 8.0/10
10. [NVIDIA NeMo Automodel 与 Hugging Face Diffusers 实现可扩展微调](#item-10) ⭐️ 7.0/10
11. [Patreon 从 robots.txt 转向主动拦截 AI 爬虫](#item-11) ⭐️ 7.0/10
12. [GPU 融资方转向推理芯片，达成 4 亿美元交易](#item-12) ⭐️ 7.0/10
13. [阿里 1688 推出 AI 对 AI B2B 交易协议 UTP](#item-13) ⭐️ 7.0/10
14. [线粒体心智理论提出](#item-14) ⭐️ 7.0/10
15. [未来属于 AI 狂热者](#item-15) ⭐️ 7.0/10
16. [乌克兰巡航导弹采用业余无人机硬件](#item-16) ⭐️ 7.0/10
17. [Kimi K3：2.8 万亿参数开源 AI 模型发布](#item-17) ⭐️ 7.0/10
18. [商汤开源统一视觉模型，终结拼凑怪兽时代](#item-18) ⭐️ 7.0/10
19. [蚂蚁集团开源 SingGuard-NSFA，保障 AI 智能体安全](#item-19) ⭐️ 7.0/10
20. [书评：手机即奶牛](#item-20) ⭐️ 6.0/10
21. [英伟达发布全新机器人 AI 模型](#item-21) ⭐️ 6.0/10
22. [没有单一 AI 模型在漏洞检测中占优](#item-22) ⭐️ 6.0/10
23. [德勤使用 Claude AI 加速开源补丁管理](#item-23) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Firefox 编译为 WebAssembly 并在浏览器中运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter 将完整的 Firefox 浏览器编译为 WebAssembly，使其能够在 Chrome 等另一个浏览器中运行。该演示加载了 233MB 的 gecko.wasm 二进制文件，并使用 Wisp 协议进行网络代理。 这是一项突破性的技术成就，展示了在另一个浏览器中运行完整浏览器的可行性，为跨平台执行和隔离开辟了可能性。该项目还展示了 AI 辅助编程的强大能力，因为它使用了价值约 25,000 美元的 Claude Opus 和 Fable 代币。 该项目选择 Firefox/Gecko 是因为其强大的单进程支持。所有网络流量都通过 WebSocket 上的 Wisp 协议经由 Puter 的服务器代理，团队不得不扩展服务器以处理 Hacker News 带来的流量。

rss · Simon Willison · 7月16日 23:34

**背景**: WebAssembly (WASM) 是一种低级二进制指令格式，可在现代浏览器中以接近原生的速度运行。将 Firefox 这样的完整浏览器编译为 WASM 极具挑战性，因为浏览器引擎非常复杂，但 Firefox 的单进程模式简化了任务。Wisp 协议是一种低开销协议，用于通过单个 WebSocket 连接代理多个 TCP/UDP 套接字。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/ wisp - protocol : Wisp is a low-overhead...</a></li>
<li><a href="https://claude.com/pricing">Plans & Pricing | Claude by Anthropic</a></li>
<li><a href="https://support.claude.com/en/articles/11049741-what-is-the-max-plan">What is the Max plan ? | Claude Help Center</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论对该演示表达了兴奋和惊叹，许多人称赞其工程努力。一些人担心通过 Puter 服务器代理所有流量的成本，团队确认他们不得不扩展基础设施以应对负载。

**标签**: `#WebAssembly`, `#Firefox`, `#browser engineering`, `#cross-platform`, `#demo`

---

<a id="item-2"></a>
## [Ultralytics v8.4.97 新增直接 Hailo HEF 导出](https://github.com/ultralytics/ultralytics/releases/tag/v8.4.97) ⭐️ 8.0/10

Ultralytics 8.4.97 引入了对 YOLOv8、YOLO11 和 YOLO26 检测模型的直接 Hailo HEF 导出功能，用户只需一条命令即可为 Hailo 边缘加速器编译模型。 这简化了边缘 AI 部署，用精简的导出流程取代了冗长的手动 ONNX 到 DFC 工作流，使从业者更容易在 Hailo 硬件上部署 YOLO 模型。 导出支持 Hailo-8、Hailo-8L、Hailo-10H、Hailo-15H 和 Hailo-15L 加速器，使用 INT8 量化，并建议至少使用 1024 张代表性校准图像以保证生产精度。

github · github-actions[bot] · 7月17日 01:18

**背景**: Hailo HEF（Hailo 可执行格式）是一种用于在 Hailo 边缘 AI 加速器上部署神经网络的二进制文件格式。此前，将 YOLO 模型转换为 HEF 需要多步手动流程，涉及 ONNX 和 Hailo 的 Dataflow Compiler。本次更新将该工作流直接集成到 Ultralytics 中，降低了复杂性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.ultralytics.com/integrations/hailo">Hailo Export for Ultralytics YOLO Models</a></li>
<li><a href="https://github.com/hailo-ai/hailo_model_zoo">GitHub - hailo-ai/hailo_model_zoo: The Hailo Model Zoo ... Hailo Platform | luxonis/modelconverter | DeepWiki Guide step-by-step how to compile custom models to HEF ultralytics/docs/en/integrations/hailo.md at main ... - GitHub Creating Custom Hef using DFC/Model Zoo - Guides - Hailo ...</a></li>
<li><a href="https://hailo.ai/">Hailo AI on the Edge Processors | Edge AI Chip Solutions</a></li>

</ul>
</details>

**标签**: `#YOLO`, `#edge AI`, `#Hailo`, `#model export`, `#Ultralytics`

---

<a id="item-3"></a>
## [首次在宜居带岩石系外行星发现大气层](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

詹姆斯·韦伯太空望远镜确认了位于 48 光年外宜居带内的岩石系外行星 LHS 1140b 拥有大气层，排除了其是迷你海王星的可能性。 这是首次在宜居带岩石行星上探测到大气层，挑战了红矮星行星因恒星剥离而无法保持大气层的假设。 LHS 1140b 是一颗质量为地球 5.6 倍的超级地球，每 24.7 天绕一颗 M 型红矮星运行。其大气中含有氦气，表明该行星具有很高的逃逸速度。

hackernews · neversaydie · 7月17日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=48947560)

**背景**: 红矮星比太阳更冷且更活跃，其宜居带非常靠近恒星。那里的行星面临强烈的恒星辐射，可能剥离大气层。LHS 1140b 于 2017 年被发现，JWST 的发射光谱学现已确认其拥有大气层，使其成为研究宜居性的首选目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LHS_1140_b">LHS 1140 b - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/exoplanet-catalog/lhs-1140-b/">LHS 1140 b - NASA Science</a></li>
<li><a href="https://www.theguardian.com/science/2026/jul/16/atmosphere-lhs-1140b-exoplanet-could-water-scientists">Earth-like exoplanet found to have an atmosphere | Space | The Guardian</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，红矮星行星通常难以保持大气层，但 JWST 数据排除了迷你海王星的可能性。一些人讨论了在几个世纪内到达该行星的推进方法，而另一些人则强调氦气的探测意味着高逃逸速度，使得生命难以离开。

**标签**: `#exoplanets`, `#JWST`, `#astronomy`, `#atmosphere`, `#habitable zone`

---

<a id="item-4"></a>
## [Kimi K3 与鹈鹕基准测试：隐藏提示与评估局限](https://simonwillison.net/2026/Jul/16/kimi-k3/) ⭐️ 8.0/10

Simon Willison 对 Kimi K3 的分析揭示了鹈鹕基准测试（要求模型生成骑自行车的鹈鹕的 SVG）存在重大局限，包括可能的训练数据污染，以及发现 Kimi K3 中隐藏了一个 85 token 的系统提示。 这很重要，因为它揭示了流行 LLM 基准测试的缺陷，引发了对数据污染的担忧，同时暴露了影响模型行为和评估公平性的隐藏系统提示。 Kimi K3 是一个 2.8 万亿参数的开源模型，鹈鹕基准测试的简单性（单一提示）使其容易受到记忆的影响；隐藏提示可能控制推理努力。社区还指出，Kimi K3 是近期模型中最便宜但最慢的。

hackernews · droidjj · 7月17日 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48947717)

**背景**: 鹈鹕基准测试由 Simon Willison 于 2024 年底创建，是一个非正式测试，要求 LLM 生成骑自行车的鹈鹕的 SVG。它因能快速比较模型能力而流行。系统提示提取是一种揭示塑造模型行为的隐藏指令的技术，常用于安全分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark)</a></li>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/system_prompts_leaks: Extracted system ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论讨论了鹈鹕图像是否在训练数据中，一位用户指出其公司博客内容在六个月内出现在 LLM 中。另一位评论者通过计算 token 数量推断隐藏提示，还有用户创建了成本-速度比较，显示 Kimi K3 最便宜但最慢。

**标签**: `#AI`, `#LLM`, `#benchmarking`, `#Kimi K3`, `#system prompt`

---

<a id="item-5"></a>
## [模感科技获数千万元天使轮融资，研发机器人全身触觉皮肤](https://36kr.com/p/3899128277452681?f=rss) ⭐️ 8.0/10

由港科大博士创立的模感科技（MoSense）近日完成数千万元天使轮融资，投资方包括红杉中国、高瓴创投及智元机器人，用于研发基于电磁超构力学技术的全身多模态触觉系统 MoSkin。 本轮融资凸显了全身触觉感知在人形机器人领域日益增长的重要性，解决了真实场景部署的关键瓶颈。模感科技的技术可通过提供全面的触觉反馈，使机器人能够执行物流搬运、养老护理等需要物理交互的复杂任务。 MoSkin 覆盖机器人手部、四肢、躯干和足底，将刚性物理边界转化为连续的六维力场感知。公司还同步研发基于多模态隐空间融合门控机制的世界动作触觉预测模型，以缩小仿真与真实环境之间的差距。

rss · 36氪 · 7月17日 02:39

**背景**: 目前大多数机器人触觉方案仅局限于指尖或夹爪，缺乏全身反馈。电磁超构材料是一种人工结构，可操控电磁波，从而实现新型传感能力。Sim-to-Real（仿真到现实）鸿沟是指由于物理和感知差异，在仿真环境中训练的策略难以直接部署到真实机器人上的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://36kr.com/p/3899128277452681">36...</a></li>
<li><a href="https://news.pedaily.cn/202607/566450.shtml">news.pedaily.cn/202607/566450.shtml</a></li>

</ul>
</details>

**标签**: `#robotics`, `#tactile sensing`, `#humanoid robot`, `#funding`, `#AI`

---

<a id="item-6"></a>
## [前蔚来、华为智驾核心成员获数亿元融资，打造具身世界模型](https://36kr.com/p/3899081603483525?f=rss) ⭐️ 8.0/10

由前蔚来和华为自动驾驶核心成员创立的日冕开物（Rikor Robotics）完成了连续两轮种子轮融资，合计金额达数亿元人民币，用于其具身世界模型 LaMPA 的研发。该公司旨在打造一个能够理解物理世界、预测环境变化并驱动机器人执行任务的基础模型，实现跨场景泛化。 这笔融资表明投资者对具身智能世界模型的高度信心，这是迈向能够适应复杂非结构化环境的通用机器人的关键一步。团队来自领先自动驾驶公司的背景，预示着在连接仿真与现实部署方面可能取得突破。 LaMPA 引入了三重表征体系（环境、本体、经验）和块扩散架构，并配备了世界奖励模型以加速强化学习。该公司已与远图未来合作，进入高精度服务器制造装配场景。

rss · 36氪 · 7月17日 01:52

**背景**: 具身智能旨在赋予机器人在物理世界中感知、推理和行动的能力。世界模型是一种关键方法，使机器人能够模拟未来状态并规划动作。Yann LeCun 提出的 JEPA 理论为学习世界的抽象表征提供了理论基础，但实际实现需要解决如何表征物理世界以及高效学习因果关系的问题。

**标签**: `#embodied intelligence`, `#world model`, `#robotics`, `#autonomous driving`, `#funding`

---

<a id="item-7"></a>
## [MIT 研究修正 20 世纪美国 GDP 增长](https://marginalrevolution.com/marginalrevolution/2026/07/cataloging-growth-a-re-evaluation-of-1900-1990.html?utm_source=rss&utm_medium=rss&utm_campaign=cataloging-growth-a-re-evaluation-of-1900-1990) ⭐️ 8.0/10

MIT 研究员 Verónica Bäcker-Peral 和 Benjamin Wittenbrink 利用 510 万条产品清单，构建了 1900 年至 1990 年美国消费品的质量调整价格指数。 这一新指数可能大幅修正历史实际 GDP 增长估算，因为它系统性地考虑了官方价格指数在 20 世纪大部分时间里基本忽略的质量变化。 该数据集包含 510 万条产品清单，能够使用特征质量调整方法将价格变化与质量改进分离，这对于准确测量实际 GDP 至关重要。

rss · Marginal Revolution · 7月17日 15:33

**背景**: 实际 GDP 增长衡量的是经通胀调整后生产的商品和服务的价值。然而，传统的价格指数（如 CPI）往往未能充分考虑质量改进（如更快的计算机或更耐用的服装），可能导致通胀被高估、实际增长被低估。特征质量调整是一种统计技术，通过估算特定产品特征的价值来分离纯粹的价格变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bls.gov/cpi/quality-adjustment/">Quality Adjustment in the CPI - U.S. Bureau of Labor Statistics</a></li>
<li><a href="https://www.bls.gov/cpi/quality-adjustment/questions-and-answers.htm">Frequently Asked Questions about Hedonic Quality Adjustment ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S030440762500106X">Hedonic prices and quality adjusted price indices powered by ...</a></li>

</ul>
</details>

**标签**: `#economics`, `#price index`, `#GDP measurement`, `#quality adjustment`, `#data science`

---

<a id="item-8"></a>
## [火星车仪器无需样本返回即可探测生物特征](https://news.google.com/rss/articles/CBMi9AFBVV95cUxQRWNCdXI1QTlsSUh2X3p4YVdhWTJYV01aTGpLOVRUTzNwVGpZaFlfaDBwREZtcHRQMnBrZjMwa28zWFYtWU1YWDItOVRGc3hwc0lZQ1hwcVRyVjBUOVhQUi1LZVM0STdIME9uZzRDajhPb2p2aWZuNmlFUGJmMVZzZ3MxVFd3NWdDNnhBSlVBanNKNzlZZnA0ZFpYNURySVVkUEdLSDhCQ1RhUHRhUXQtV3VsQVgxaElNbmFsVllSalZPUTZWbmVUcTFzZEtnS2tVN0V6RmhpZlpLdjcxTnhMcGJvU2NpeUdoOVdFM25rREVfS3Bk?oc=5) ⭐️ 8.0/10

科学家们证明，火星车上的现有仪器可以探测外星生物特征，可能无需样本返回任务。 这一突破可以利用现有火星车能力加速寻找火星生命，相比样本返回任务节省时间和成本。 该方法利用光谱学和原位分析来识别有机分子或同位素异常等生物特征，借助毅力号火星车上的 SHERLOC 和 PIXL 等仪器。

google_news · The Debrief · 7月17日 12:49

**背景**: 生物特征是指任何能提供过去或现在生命科学证据的物质或现象。传统上，确凿的探测需要将样本送回地球。这种新方法表明火星车可以在现场进行此类分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Biosignature">Biosignature - Wikipedia</a></li>
<li><a href="https://www.nasa.gov/news-release/nasa-says-mars-rover-discovered-potential-biosignature-last-year/">NASA Says Mars Rover Discovered Potential Biosignature ... - NASA</a></li>

</ul>
</details>

**标签**: `#Mars`, `#biosignatures`, `#space exploration`, `#astrobiology`, `#NASA`

---

<a id="item-9"></a>
## [习近平将公布全球 AI 愿景，华为推出英伟达竞品](https://news.google.com/rss/articles/CBMitwFBVV95cUxOVlJMUmJnREpFMGdvd21veTNUdkwtUEhhVE5YOV81Z2dINXl1VG1CbWc4VFE0NGNudUY1QXdtcFNBMkJIOWVhRjRxTnh5bDcyNjR6WmhNOHlmSzlYN000TDdQYWRCb01LcWNOa2o5b3ZpNllNZ0tLbldPcFIwRmZkRFBuQTRUWUVaazJUU0RsWERjSHQxLWdmUEc2NGw5emtDU0RXa0QxSDRrWllEbHdwYjZrSzU2X0k?oc=5) ⭐️ 8.0/10

中国国家主席习近平将在上海峰会上公布全球人工智能战略，同时华为推出 Ascend 950PR 芯片，作为英伟达产品的竞品。 这标志着中国在 AI 和半导体技术领域挑战美国主导地位的重要地缘政治举措，可能重塑全球 AI 治理和供应链。 华为 Ascend 950PR 提供 1.56 petaflops 的 AI 推理性能，FP4 性能是英伟达 H20 的 2.8 倍，计划 2026 年生产 75 万颗，并已获得字节跳动 56 亿美元订单。

google_news · Tekedia · 7月17日 07:26

**背景**: 美国对华实施先进 AI 芯片出口管制，促使中国企业开发本土替代品。华为 Ascend 系列是中国推动半导体自给自足的关键部分。习近平的愿景强调开源、以人为本的全球 AI 秩序，与美国主导的框架形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tech-insider.org/huawei-ascend-950pr-ai-chip-nvidia-china-2026/">Huawei Ascend 950PR: The 1.56 PFLOP AI Chip vs Nvidia [2026]</a></li>
<li><a href="https://www.bitrue.com/blog/huawei-vs-nvidia-ascend-chip-performance-2025">Huawei Ascend Chips vs NVIDIA: A 2025 AI Performance Comparison</a></li>
<li><a href="https://abhs.in/blog/huawei-ascend-910c-china-nvidia-alternative-2026">Huawei Ascend 910C: China Plans 600,000 AI Chips in 2026</a></li>

</ul>
</details>

**标签**: `#AI`, `#China`, `#Huawei`, `#Nvidia`, `#Geopolitics`

---

<a id="item-10"></a>
## [NVIDIA NeMo Automodel 与 Hugging Face Diffusers 实现可扩展微调](https://huggingface.co/blog/nvidia/scale-diffusers-finetuning-nemo-automodel) ⭐️ 7.0/10

NVIDIA 与 Hugging Face 宣布了一项新集成，允许使用 NeMo Automodel 和 Diffusers 库对视频和图像扩散模型进行大规模微调。这使得从业者能够直接利用 NeMo 的分布式训练能力与 Hugging Face 的模型生态系统。 这一集成显著降低了扩散模型大规模微调的门槛，而扩散模型计算密集。它使 AI/ML 从业者无需编写自定义分布式训练代码即可训练更大模型或处理更多数据，加速了研究和生产部署。 NeMo Automodel 是一个基于 PyTorch DTensor 的原生 SPMD 训练库，支持 LLM、VLM、扩散模型和检索模型。该集成通过直接将任何 Hugging Face 模型加载到 NeMo Automodel 中，消除了检查点转换或样板代码的需要。

rss · Hugging Face Blog · 7月17日 15:57

**背景**: 扩散模型是一类生成模型，通过逐步去噪随机噪声来创建图像或视频。针对特定任务或数据集微调这些模型通常需要大量计算资源和分布式训练专业知识。NeMo Automodel 通过提供自动处理并行化和优化的分布式训练框架简化了这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.nvidia.com/nemo/automodel/">NeMo AutoModel Documentation | NVIDIA NeMo AutoModel</a></li>
<li><a href="https://github.com/NVIDIA-NeMo/Automodel">GitHub - NVIDIA-NeMo/Automodel: Pytorch Distributed native ...</a></li>
<li><a href="https://huggingface.co/docs/diffusers/index">Diffusers · Hugging Face</a></li>

</ul>
</details>

**标签**: `#fine-tuning`, `#NVIDIA NeMo`, `#Diffusers`, `#AI/ML`, `#scalability`

---

<a id="item-11"></a>
## [Patreon 从 robots.txt 转向主动拦截 AI 爬虫](https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/) ⭐️ 7.0/10

Patreon 宣布与 Cloudflare 合作，主动拦截未经许可抓取创作者内容用于训练的 AI 爬虫，不再仅依赖 robots.txt。 这一转变标志着行业从被动防御转向主动防御，以应对未经授权的 AI 训练，保护创作者在日益增长的 AI 经济中的收入和内容权益。 Patreon 正在使用 Cloudflare 的机器人管理解决方案，该方案可拦截被归类为“训练”或“代理”的爬虫，并在显示广告的页面上生效，新默认设置将于 2026 年 9 月生效。

rss · TechCrunch AI · 7月17日 15:21

**背景**: Robots.txt 是一种依赖网络爬虫自愿遵守的标准，但恶意爬虫常常忽略它。Cloudflare 提供主动的机器人检测和拦截能力，为抵御未经授权的抓取提供了更强大的防御。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Robots.txt">Robots.txt</a></li>
<li><a href="https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/">Block AI Bots · Cloudflare bot solutions docs</a></li>

</ul>
</details>

**标签**: `#AI scraping`, `#content protection`, `#Patreon`, `#Cloudflare`, `#creator economy`

---

<a id="item-12"></a>
## [GPU 融资方转向推理芯片，达成 4 亿美元交易](https://techcrunch.com/2026/07/17/why-the-first-gpu-financiers-are-turning-to-inference-chips-in-a-400-million-deal/) ⭐️ 7.0/10

General Compute 从 Upper90 获得了 4 亿美元芯片担保贷款，这是首个专门针对 AI 推理硬件而非训练 GPU 的重大融资交易。 这标志着 AI 基础设施融资从以训练为主的 GPU 转向推理优化芯片，反映了行业向大规模部署 AI 模型的转变。它可能为推理初创公司解锁新资本，并重塑硬件投资格局。 该贷款以芯片本身为担保，类似于 CoreWeave 早期的 GPU 担保贷款，但这次聚焦于推理硬件。General Compute 是推理芯片领域相对较新的参与者。

rss · TechCrunch AI · 7月17日 12:00

**背景**: AI 推理是运行已训练好的 AI 模型进行预测的过程，与需要大量算力的训练不同。推理芯片是专用硬件，旨在比通用 GPU 更节能、更具成本效益地完成此任务。首批 GPU 融资方（如 CoreWeave）开创了以 GPU 为抵押的芯片担保贷款，但这笔交易是首个针对推理芯片的此类贷款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/17/why-the-first-gpu-financiers-are-turning-to-inference-chips-in-a-400-million-deal/">Why the first GPU financiers are turning to inference chips ...</a></li>
<li><a href="https://creati.ai/ai-news/2026-07-17/general-computes-400m-chip-backed-loan-signals-a-new-financing-market-for-ai-inference-hardware/">General Compute’s $400M chip-backed loan signals a new ...</a></li>
<li><a href="https://www.naddod.com/ai-insights/inference-chip-guide-the-foundation-of-scalable-ai-applications">Inference Chip Guide: The Foundation of Scalable AI ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#inference chips`, `#GPU financing`, `#venture capital`, `#hardware`

---

<a id="item-13"></a>
## [阿里 1688 推出 AI 对 AI B2B 交易协议 UTP](https://36kr.com/p/3896564485572489?f=rss) ⭐️ 7.0/10

阿里 1688 宣布将于 2026 年 7 月底推出通用交易协议（UTP），这是一套面向 AI 对 AI B2B 交易的标准，使买家 AI 智能体可直接对接工厂 AI 智能体自动完成交易。 UTP 旨在成为 A2A（智能体对智能体）全球贸易的基础设施，有望标准化智能体间的商业活动，加速从人工驱动的 B2B 向全自动 AI 驱动交易的转变。 该协议旨在解决 B2B 场景中不同 AI 智能体之间缺乏通用通信标准的问题。UTP 将是一个开放标准，支持跨不同平台和 AI 框架的互操作性。

rss · 36氪 · 7月17日 13:01

**背景**: B2B 电子商务传统上涉及人工买家和卖家进行谈判和交易。随着能够自主做出采购决策的 AI 智能体的兴起，一种称为 A2A（智能体对智能体）的新范式正在出现，其中 AI 智能体代表买家和卖家。然而，这些智能体通常使用专有协议，阻碍了跨平台交易。UTP 是一个开放标准，使不同的 AI 智能体能够无缝通信和交易，类似于 HTTP 标准化网络通信的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://a2a-protocol.org/latest/">A 2 A Protocol</a></li>

</ul>
</details>

**标签**: `#AI`, `#B2B`, `#protocol`, `#e-commerce`, `#Alibaba`

---

<a id="item-14"></a>
## [线粒体心智理论提出](https://www.quantamagazine.org/martin-picards-mitochondrial-theory-of-mind-20260717/) ⭐️ 7.0/10

生物学家 Martin Picard 提出了一个“线粒体心智理论”，将线粒体定位为细胞能量、健康和意识体验之间的基本联系。 该理论通过将意识扎根于细胞能量学，挑战了传统的意识观点，可能为理解心理健康和治疗神经系统疾病开辟新途径。 Picard 是哥伦比亚大学线粒体心理生物学实验室主任，他创造了“线粒体心理生物学”这一术语，研究心理状态如何影响线粒体功能以及反之亦然。

rss · Quanta Magazine · 7月17日 14:31

**背景**: 线粒体是细胞器，以 ATP 形式产生细胞大部分能量。Picard 的“生命能量观”表明，线粒体动力学——它们的形状、运动和能量输出——直接塑造我们的思想、情感和自我意识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.quantamagazine.org/martin-picards-mitochondrial-theory-of-mind-20260717/">Martin Picard’s Mitochondrial Theory of Mind - Quanta Magazine</a></li>
<li><a href="https://www.neurology.columbia.edu/news/martin-picard-exploring-mind-mitochondria-connection">Martin Picard: Exploring the Mind-Mitochondria Connection</a></li>
<li><a href="https://www.metabolicmind.org/resources/news-views/podcasts/metabolic-mind-podcast/how-mitochondria-shape-your-mind-mood-mental-health-with-dr-martin-picard/">How Mitochondria Shape Your Mind, Mood, & Mental Health with ...</a></li>

</ul>
</details>

**标签**: `#mitochondria`, `#consciousness`, `#biology`, `#neuroscience`, `#theory of mind`

---

<a id="item-15"></a>
## [未来属于 AI 狂热者](https://marginalrevolution.com/marginalrevolution/2026/07/the-future-belongs-to-ai-maniacs.html?utm_source=rss&utm_medium=rss&utm_campaign=the-future-belongs-to-ai-maniacs) ⭐️ 7.0/10

泰勒·考恩在《自由新闻》专栏中提出，未来属于“AI 狂热者”——那些痴迷于掌握最新 AI 模型以优化工作流程和提高生产力的人。 这一观点凸显了深度参与 AI 者与不参与 AI 者之间日益扩大的差距，可能重塑职业成功和经济生产力。 考恩将 AI 狂热者定义为立即尝试新模型、花费数小时掌握它们，并利用它们来调节工作流程和生产力的人。

rss · Marginal Revolution · 7月17日 04:11

**背景**: 该专栏是经济学家泰勒·考恩在 Marginal Revolution 上发表的观点文章，反映了关于 AI 采用和劳动力技能发展的持续讨论。

**标签**: `#AI`, `#productivity`, `#future of work`, `#opinion`

---

<a id="item-16"></a>
## [乌克兰巡航导弹采用业余无人机硬件](https://news.google.com/rss/articles/CBMijwJBVV95cUxNM3FPY2NOQ20tVk1ZMlZTbG01Rk1MM1NNdG1lVGpoWHpKRU14LWpMUi1zWGFKWHJRdzRycEdrVnF4MDN6dktVeldzSnBTQ1RCNkRwLTA0NDNwWWhQZmpaSXpZLVRYX1pCaUVXeXJ1azBhZGlaZ0hSckFiN2JMSXMyM2U1MWswWmMtc21ocHRHWWQySDZFQXVWNS1QaVNpd0NKY0dadnZpT1RtQWhka2NvRXNRMXNSMWhJcnhZeUtaWHBmRm5HMDVFeWhaWmp5NlJHUWZCZHhmUG5laEJVMjNYQXRDN0pnYW96S0lTWFNpa3o1cExVQmNDZ0c4Qm9MVklreHd5MFdSTmRKOXBHS0VN?oc=5) ⭐️ 7.0/10

据《新科学家》报道，乌克兰最新的巡航导弹 S8000 Banderol 采用了消费级无人机中常见的开源飞行控制系统。 这表明廉价的商用现成技术正在使先进军事硬件更易获取，可能降低国家和组织开发精确打击能力的门槛。 飞行控制器是业余无人机常用的开源设计，使导弹能够自主导航。这种民用组件的重新利用突显了冲突地区快速创新的趋势。

google_news · New Scientist · 7月17日 10:00

**背景**: 巡航导弹通常需要复杂的制导系统，但乌克兰采用了低成本、广泛可用的无人机电子设备来承担这一角色。S8000 Banderol 是 R-360 海王星反舰导弹的对地攻击改型，射程超过 1000 公里。业余无人机组件越来越多地被用于军事用途，例如战争中使用的 FPV 无人机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.newscientist.com/article/2580002-why-a-ukrainian-cruise-missile-is-flying-with-hobby-drone-hardware/">Why a Ukrainian cruise missile is flying with hobby drone ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/R-360_Neptune">R-360 Neptune - Wikipedia</a></li>
<li><a href="https://war-sanctions.gur.gov.ua/en/page-s8000-banderol">S8000 Banderol cruise missile</a></li>

</ul>
</details>

**标签**: `#military technology`, `#drone hardware`, `#defense`, `#innovation`

---

<a id="item-17"></a>
## [Kimi K3：2.8 万亿参数开源 AI 模型发布](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBGLW5OUXd5MWZyRENvd1A1VWNLVDBfYXhZeWlqdGFQSDhoZFFRdzRCdkdMOEM2bi1DdmY0VnlNWTZCUTNfeXdHX3ZHT0ItU3U3NnlKYkVzT1NBbTFFSkNZ?oc=5) ⭐️ 7.0/10

Moonshot AI 开源了 Kimi K3，这是一个 2.8 万亿参数的混合专家模型，成为全球首个开源的三万亿参数级别模型。 此次发布使前沿规模 AI 的访问更加民主化，让研究人员和开发者能够研究并基于一个此前仅限专有系统拥有的模型进行构建。 Kimi K3 拥有 100 万 token 的上下文窗口、原生视觉能力，并基于定制的 Kimi Delta Attention (KDA) 混合线性注意力机制和 Attention Residuals 构建。

google_news · The Neuron · 7月17日 19:49

**背景**: 像 GPT-4 和 Llama 3 这样的大型语言模型推动了 AI 进步，但大多数顶级模型仍保持闭源。开源模型允许更广泛的社区使用、检查和改进。Kimi K3 在 Modified MIT 许可证下的开源发布，代表了向开放前沿 AI 迈出的重要一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://github.com/47thtechcorner/Kimi-K3/tree/main">GitHub - 47thtechcorner/Kimi-K3: Kimi K3: The 3 Trillion Open ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#machine learning`

---

<a id="item-18"></a>
## [商汤开源统一视觉模型，终结拼凑怪兽时代](https://news.google.com/rss/articles/CBMidkFVX3lxTFB3TXRuMHN0M0gyZEhJb3R1RTh1eHdsczBpa2p4aE9kWVNoZ1B3OWV2UldTX1hJRW55RTdJcHlWUjJMc0trcTBOVWVNdmJlZldFY3FKOTN2X0Q1Wkd4N2p3UVc2VHBnN0dIN2VWbGdJU21tdkFOYXc?oc=5) ⭐️ 7.0/10

商汤科技发布并完全开源了 SenseNova-Vision，这是一个统一的视觉大模型，能够在单一架构中处理检测、分割、深度预测和 3D 重建等任务。 这标志着需要将多个任务特定模型拼接在一起的“拼凑怪兽”时代的终结，有望降低视觉 AI 应用的复杂性并提高效率。 该模型是商汤 SenseNova 基础模型系列的一部分，旨在处理目标检测、光学字符识别、关键点定位和图像分割等任务。

google_news · Pandaily · 7月17日 02:06

**背景**: 传统的视觉 AI 系统通常针对不同任务使用单独的模型，导致复杂且低效的“拼凑怪兽”方法。统一视觉模型将多种能力集成到一个架构中，简化了部署并可能提升性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pandaily.com/sensetime-sensenova-vision-open-source-jul2026">China Visual AI Leader SenseTime Declares End of... - Pandaily</a></li>
<li><a href="https://technode.com/2026/07/14/sensetime-open-sources-sensenova-vision-unified-vision-model/">SenseTime open-sources SenseNova- Vision unified vision model ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Computer Vision`, `#Open Source`, `#SenseTime`

---

<a id="item-19"></a>
## [蚂蚁集团开源 SingGuard-NSFA，保障 AI 智能体安全](https://news.google.com/rss/articles/CBMiggFBVV95cUxQckFQakgwNU83Y2JZc0VKS0NUeU5PdldpUzVnUUdVaFo5X2pIYTRCNTdWT3VtRWlqQk5Sai1TNGdoMGZLNkRFUkJMZ0x1d2c5Z2xrVFN2Z0l2NnlnaDc4Y0hZUEJzV05SM3lSZ0M5Rk1KejVGYVJTYmlmNHlIbU1GeTNB?oc=5) ⭐️ 7.0/10

蚂蚁集团开源了 SingGuard-NSFA，这是一个为自主 AI 智能体设计的护栏框架，用于防范提示注入、工具滥用等威胁。 随着自主 AI 智能体日益普及，像 SingGuard-NSFA 这样的安全框架对于防止恶意利用和确保企业安全部署至关重要。 SingGuard-NSFA 可检测查询端和响应端威胁，涵盖 7 个一级领域、28 个二级风险和 185 个三级变体，并在不同模型规模上优于同类护栏方案。

google_news · AOL.com · 7月17日 07:25

**背景**: 自主 AI 智能体可以独立执行任务，因此容易受到提示注入、敏感数据提取等攻击。像 SingGuard-NSFA 这样的护栏框架提供了安全层，用于监控和阻止有害输入与输出，确保智能体在预期边界内运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/inclusionAI/SingGuard-NSFA">GitHub - inclusionAI/SingGuard-NSFA</a></li>
<li><a href="https://arxiv.org/abs/2607.13081">[2607.13081] SingGuard-NSFA: Extensible Guardrails for ...</a></li>
<li><a href="https://arxiv.org/html/2607.13081v1">SingGuard-NSFA: Extensible Guardrails for Agentic AI</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Open Source`, `#Autonomous Agents`, `#Ant Group`

---

<a id="item-20"></a>
## [书评：手机即奶牛](https://marginalrevolution.com/marginalrevolution/2026/07/a-phone-is-a-cow.html?utm_source=rss&utm_medium=rss&utm_campaign=a-phone-is-a-cow) ⭐️ 6.0/10

菲利普·奥尔斯瓦尔德的新书《手机即奶牛》将手机发展史、伊克巴尔·卡迪尔将手机引入孟加拉国的传记以及经济增长理论融为一体。 这本书通过将历史叙事与引人入胜的商业故事相结合，提供了关于移动技术如何推动经济发展（尤其是在低收入国家）的独特视角。 这本书被描述为“三合一”，在各个方面都取得了成功，涵盖了手机历史、伊克巴尔·卡迪尔与 Grameenphone 的创业历程以及更广泛的经济增长理论。

rss · Marginal Revolution · 7月17日 11:20

**背景**: 伊克巴尔·卡迪尔受格莱珉银行小额信贷模式的启发，于 1997 年在孟加拉国创立了 Grameenphone，旨在为农村地区提供移动通信服务。书名隐喻性地表明，在发展中经济体中，手机可以像奶牛一样有价值，成为一种生产性资产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iqbal_Quadir">Iqbal Quadir - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grameenphone">Grameenphone - Wikipedia</a></li>

</ul>
</details>

**标签**: `#book review`, `#mobile phones`, `#economic development`, `#technology history`

---

<a id="item-21"></a>
## [英伟达发布全新机器人 AI 模型](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQQjZNUDFLOXBTSTZNZmFmbFU4bktkM2ZPTE53cDdvLVBTX2F0Vmw3ay1FV2dQUHp4STJzUUFZeklqaS1mcHYyWVIwMG9hcUsyWHFhQlpjYUsxUWh2bnh1OGl6aDJSMnhoZXVreE5KS0NQNEFodWVYRzBQM1RqOGJBVjFZekFqZXJycjBEejdsNFRuREViVnZsVGVKcHdvT3NvQTFVSmo1SG8zQUVSVjNSaFhnV3NFV1RyOFJrV1FJT0ZSOTJWOUpfSVV1MHFhOW96S1hYMw?oc=5) ⭐️ 6.0/10

英伟达发布了一款面向机器人的生成式世界基础模型，基于其 Isaac GR00T 和 Cosmos 模型系列，旨在增强机器人的推理能力和自主性。 此次发布可能成为机器人行业的重要催化剂，使机器人更智能、更自主，能够处理复杂任务，有望加速在制造、物流和服务领域的应用。 新模型基于英伟达的 Cosmos-Reason 模型，该模型在响应前进行推理，并且是开放的 Isaac GR00T 基础模型的一部分，为机器人带来类人推理能力。

google_news · 24/7 Wall St. · 7月17日 12:49

**背景**: 英伟达一直在开发用于机器人的 Isaac 平台，包括仿真工具和 GR00T N1 等基础模型，GR00T N1 是一种视觉-语言-动作（VLA）模型。Cosmos 模型系列专注于物理 AI 的世界理解和推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Accelerates-Robotics-Research-and-Development-With-New-Open-Models-and-Simulation-Libraries/default.aspx">NVIDIA Corporation - NVIDIA Accelerates Robotics Research and ...</a></li>
<li><a href="https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots">NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid ...</a></li>
<li><a href="https://247wallst.com/investing/2026/07/17/nvidia-just-released-a-seriously-impressive-ai-model-for-robots-this-could-be-the-big-catalyst/">NVIDIA Just Released a Seriously Impressive AI Model for ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI`, `#robotics`, `#machine learning`

---

<a id="item-22"></a>
## [没有单一 AI 模型在漏洞检测中占优](https://news.google.com/rss/articles/CBMinwFBVV95cUxQeEZXbFZMMmdURGYxRGREVGU4TUZkNXVHSmpCdVFtNGl4NzQ0ckdRcUQ4bmRGb1lkcjZMNWZOTjlhTmlPX1gzZl8wcjk2S2R0SllGcU4tS3VYaUwybzdGcEJ0U1pBVWFLZ2ZBWlFCYzltZjdOWEpWUEhVeG5QVkI0NHBEMkYweXZVa2FLVTd6NzRDV0p1dXZneF9pT3lsejg?oc=5) ⭐️ 6.0/10

一项最新研究发现，没有单一 AI 模型能在软件漏洞检测中持续优于其他模型，这挑战了存在通用最佳模型的观念。 这一发现强调了在 AI 驱动的网络安全中需要采用定制化或集成方法，因为依赖单一模型可能会留下漏洞覆盖的空白。 该研究比较了多种 AI 模型，包括大型语言模型（LLM）和深度学习系统，在多个漏洞检测基准测试中，发现性能因漏洞类型和代码库的不同而有显著差异。

google_news · The News International · 7月17日 07:33

**背景**: 漏洞检测是网络安全中的关键任务，旨在在攻击者利用之前识别软件中的安全缺陷。AI 模型，尤其是大型语言模型，越来越多地被用于自动化这一过程，但它们的相对有效性一直不明确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.bswen.com/blog/2026-03-26-ai-security-vulnerability-detection/">How Do AI Models Compare for Security Vulnerability Detection?</a></li>
<li><a href="https://www.mdpi.com/2504-4990/8/1/19">AI-Powered Vulnerability Detection and Patch Management in ...</a></li>
<li><a href="https://www.mdpi.com/2079-9292/14/22/4449">Modern Approaches to Software Vulnerability Detection: A ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#vulnerability detection`, `#cybersecurity`, `#machine learning`

---

<a id="item-23"></a>
## [德勤使用 Claude AI 加速开源补丁管理](https://news.google.com/rss/articles/CBMinwFBVV95cUxQdllGNE9nancydkR2R1QwaGtjY19odmRuc1B0UU9DSUdVNFprWDJNb2lXdmNFeTJuTGw4RUdGRmpxbkR1cHVCcmF3NUFwUjljNk9XS1NQcmNpdzNxVUVHVHVGalRDSUpYcU1xZnlRZ2JkTjVsbGdYRXRZOElGUlc2WTZKOElFRmoxOHozV21TZVl4dnNPYmFURVoxejhod2c?oc=5) ⭐️ 6.0/10

德勤已采用 Anthropic 的 Claude AI 来加速开源软件依赖项的补丁管理流程，减少了人工工作量并提高了对安全漏洞的响应速度。 这展示了大型语言模型在 DevOps 和安全领域的实际企业应用，可能为其他组织自动化补丁管理、减少开源漏洞暴露树立先例。 Claude AI 用于分析漏洞报告、识别受影响的依赖项并建议或应用补丁，从而简化了通常耗时的手动流程。具体使用的模型或集成细节尚未披露。

google_news · Open Source For You · 7月17日 08:11

**背景**: 开源补丁管理是更新软件项目中的第三方库和组件以修复安全漏洞的过程。这是一项关键但通常劳动密集型的企业任务，因为未能及时打补丁可能导致安全漏洞。Claude 是 Anthropic 开发的大型语言模型，通过宪法 AI 训练以优先考虑安全性和准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="https://opensource.google/documentation/reference/releasing">Releasing Code | Google Open Source</a></li>

</ul>
</details>

**标签**: `#AI`, `#DevOps`, `#Open Source`, `#Security`

---