---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
---

> 从 259 条内容中筛选出 32 条重要资讯。

---

## CSIG Camera 备赛雷达

> 面向 CSIG「Camera学术之星」：Diffusion 4K 增强 / 轻量模型 / 赛事动态（检索窗口约 14 天，保底 ≥1 条）

1. [MoCRA：基于秩一原子的 4K 全能视频修复](#item-1) ⭐️ 9.0/10
2. [Token Radius Attention 降低视频生成成本](#item-2) ⭐️ 8.0/10
3. [EchoCache：面向高效音频驱动视频生成的能量引导跨模态缓存](#item-3) ⭐️ 8.0/10
4. [USP-Mamba：基于解混先验的高光谱超分辨率提示框架](#item-4) ⭐️ 8.0/10
5. [Loop-Mamba：用于老照片修复的轻量级状态空间框架](#item-5) ⭐️ 8.0/10

---
<a id="item-1"></a>
## [MoCRA：基于秩一原子的 4K 全能视频修复](https://arxiv.org/abs/2608.01829v1) ⭐️ 9.0/10

MoCRA 提出了一种基于组合秩一原子的混合模型，用于全能 4K 视频修复，可同时处理雾、雨、噪声和低光，无需退化标签。同时，它推出了新的配对基准 UHV-4K-AIO，包含 100 个干净 4K 片段，以原生分辨率模拟物理退化。 这项工作解决了现实世界视频修复中的联合挑战，现有方法因逐帧退化变化和内存限制而失败。MoCRA 仅用 3.6M 参数且无需光流，就达到了最先进性能，为 4K 播放的高效部署提供了可能。 MoCRA 采用频带匹配的组合条件，将容量分配给特定退化尺度：雾和低光在降采样后仍存在，而雨和噪声需要原生分辨率。它在半秒内完成 4K 修复，而最快基线需 1.7 秒，并在十一个基线中取得了最佳任务平均 PSNR。

rss · CSIG · arXiv cs.CV（增强/恢复/Diffusion） · 8月3日 07:40

**背景**: 视频修复旨在从退化输入中恢复干净帧，但现实视频常同时遭受多种退化。传统方法分别处理每种退化或依赖降采样，这无法处理仅在原生尺度出现的雨和噪声。MoCRA 引入了新基准和轻量架构，联合解决了这些问题。

**标签**: `#4K video restoration`, `#all-in-one`, `#video enhancement`, `#benchmark`, `#MoCRA`

---

<a id="item-2"></a>
## [Token Radius Attention 降低视频生成成本](https://arxiv.org/abs/2608.02504v1) ⭐️ 8.0/10

研究人员提出了 Token Radius Attention (TRA)，这是一种无需训练的框架，通过将查询熵映射到特定于令牌的半径来稀疏化视频扩散 Transformer 中的注意力。TRA 仅保留 9-19% 的注意力交互，并在 Wan2.1、Wan2.2 和 HunyuanVideo 配置中实现了 1.56 倍至 2.05 倍的加速，同时保持有竞争力的生成质量。 这解决了视频扩散 Transformer 中二次方注意力成本这一瓶颈，使高保真视频生成在实际应用中更加可行。其无需训练的特性允许在现有模型上直接部署，可能加速研究和生产系统。 TRA 使用融合熵提取、预热重用和块稀疏掩码构建来最小化开销。它观察到保留密度与注意力熵呈对数线性相关，且主导交互形成以查询为中心的邻域，半径随令牌变化，从而无需显式键排序即可实现时间衰减半径。

rss · CSIG · arXiv cs.CV（增强/恢复/Diffusion） · 8月3日 17:05

**背景**: 视频扩散 Transformer (VDiT) 能生成高保真视频，但由于对长令牌序列进行密集的 3D 自注意力，计算成本呈二次方增长。现有的稀疏注意力方法通常在查询之间共享计算预算，忽略了令牌特定的注意力需求。TRA 利用注意力熵与令牌特定保留之间的相关性来动态分配计算，无需重新训练即可提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.01776">[2502.01776] Sparse VideoGen: Accelerating Video Diffusion ... Analysis of Attention in Video Diffusion Transformers LIN-003 002 EARIZE YOUR VIDEO DIFFUSION TRANSFORMER SLA: Beyond Sparsity in Diffusion Transformers via Fine ... VSA: Accelerating Video Diffusion Inference with Sparse ... Attention Surgery: An Efficient Recipe to Linearize Your ... ReHyAt: Recurrent Hybrid Attention for Video Diffusion ...</a></li>
<li><a href="https://arxiv.org/html/2504.10317v1">Analysis of Attention in Video Diffusion Transformers</a></li>
<li><a href="https://arxiv.org/abs/2506.19852">[2506.19852] Radial Attention: $O(n\log n)$ Sparse Attention with Energy Decay for Long Video Generation</a></li>

</ul>
</details>

**标签**: `#efficient diffusion`, `#video generation`, `#attention sparsification`, `#diffusion transformers`, `#training-free`

---

<a id="item-3"></a>
## [EchoCache：面向高效音频驱动视频生成的能量引导跨模态缓存](https://arxiv.org/abs/2608.02474v1) ⭐️ 8.0/10

EchoCache 提出了一种能量引导的跨模态缓存框架，利用音频时频能量作为显著性锚点来指导缓存更新，并引入了动态时间步-潜变量缓存机制和量化缓存管理。在 EMTD 基准上的 Wan2.2-S2V 模型中，它实现了 2.46 倍的加速，同时保持了生成质量和音视频一致性。 这项工作通过利用跨模态对齐来提高效率，解决了音频驱动视频生成（生成式 AI 中一个不断发展的领域）的高推理成本问题。它提供了一种实用的解决方案，可以使此类模型的实时或大规模部署更加可行，从而使该领域的研究人员和开发人员受益。 该框架识别了现有 A2V 缓存方法中的两个层面的错位：时间-语义错位和计算-存储错位。它利用音频时频能量作为潜变量级缓存更新的显著性锚点，并引入了带有量化缓存管理的动态时间步-潜变量缓存机制，以联合优化效率和内存使用。

rss · CSIG · arXiv cs.CV（增强/恢复/Diffusion） · 8月3日 16:42

**背景**: 音频驱动视频生成（A2V）合成与音频时间上连贯且对齐的视频，但用于此任务的扩散模型需要迭代去噪，使得推理成本高昂。现有的缓存方法利用视觉特征中的时间冗余，但忽略了音频驱动视觉生成时具有非均匀时间重要性的跨模态对齐。EchoCache 通过使用音频能量作为缓存更新的指导来解决这一问题，从而改善了延迟-质量权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2410.11795v1">Efficient Diffusion Models: A Comprehensive Survey from ...</a></li>
<li><a href="https://arxiv.org/html/2508.06160v1">Fewer Denoising Steps or Cheaper Per-Step Inference: Towards ...</a></li>
<li><a href="https://apxml.com/courses/deploying-diffusion-models-scale/chapter-2-optimizing-diffusion-models-inference">Optimize Diffusion Models for Inference Speed & Cost</a></li>

</ul>
</details>

**标签**: `#efficient diffusion`, `#audio-driven video generation`, `#caching`, `#diffusion models`, `#cross-modal`

---

<a id="item-4"></a>
## [USP-Mamba：基于解混先验的高光谱超分辨率提示框架](https://arxiv.org/abs/2608.02401v1) ⭐️ 8.0/10

该论文提出了 USP-Mamba，一种将解混导出的光谱和结构提示集成到基于 Mamba 的高光谱图像超分辨率模型中的新框架。它利用成分感知的光谱先验和图像相关的结构提示来调整 Mamba 的状态演化，在多个数据集上取得了最先进的性能。 这项工作解决了基于 Mamba 的模型在高光谱成像中的关键局限性，如空间邻接性破坏和通用状态空间参数化。通过引入解混导出的先验，它提高了重建质量，并可能惠及遥感、医学成像及其他需要高分辨率光谱数据的应用。 USP-Mamba 使用解混信息的光谱提示进行全局材料成分条件化，并使用包含空间和频率分量的特征级结构提示进行局部引导。它还采用互补的 Hilbert 和语义引导邻域扫描来保持空间连续性并加强非局部语义依赖建模。

rss · CSIG · arXiv cs.CV（增强/恢复/Diffusion） · 8月3日 15:47

**背景**: 高光谱图像超分辨率旨在重建高分辨率图像，同时保留密集的光谱信息。基于 Mamba 的模型建立在状态空间模型（SSM）之上，以线性计算复杂度捕获长距离依赖，但其因果序列建模常常破坏空间邻接性。高光谱解混是一种将混合像素分解为组成材料及其丰度的技术，提供了有用的光谱先验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2312.00752">[2312.00752] Mamba: Linear-Time Sequence Modeling with ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S3050520825000351">Advances in hyperspectral image unmixing: From algorithmic ...</a></li>
<li><a href="https://www.mdpi.com/2072-4292/17/17/2968">Conventional to Deep Learning Methods for Hyperspectral ...</a></li>

</ul>
</details>

**标签**: `#hyperspectral`, `#super-resolution`, `#Mamba`, `#image enhancement`, `#efficient models`

---

<a id="item-5"></a>
## [Loop-Mamba：用于老照片修复的轻量级状态空间框架](https://arxiv.org/abs/2608.02346v1) ⭐️ 8.0/10

Loop-Mamba 提出了一种轻量级的基于循环的状态空间框架，将老照片修复建模为渐进的状态演化，并引入了语义引导的退化估计器（SGDE）和共享结构记忆 Mamba（S2M-Mamba）。它还提出了一种新的面向任务的指标——老照片损伤恢复分数（ODRS），并在 SynOld 基准上展示了最先进的性能。 这项工作解决了老照片修复这一涉及多种耦合退化的挑战性任务，并通过利用状态空间模型提供了一种高效的替代方案，避免了迭代式 CNN 和 Transformer 方法的计算开销。其轻量级设计和出色性能可能使其在实际修复应用中具有实用性，并激发更多关于状态空间模型在图像修复领域的研究。 Loop-Mamba 利用一阶状态递归通过循环转换传播潜在修复状态，从而缓解梯度稀释并降低计算开销。SGDE 联合预测局部退化图和全局退化分数，而 S2M-Mamba 在迭代中保持持久的修复状态，轻量级的多方向扫描策略增强了方向信息聚合。

rss · CSIG · arXiv cs.CV（增强/恢复/Diffusion） · 8月3日 14:59

**背景**: 老照片常常遭受划痕、裂纹、褪色、模糊、噪声和缺失区域等退化，影响视觉质量和语义内容。传统的修复方法通常依赖迭代式 CNN 或 Transformer 架构，计算量较大。Mamba 是一种状态空间模型，通过选择性状态空间实现线性时间序列建模，适合处理长距离依赖。本文将 Mamba 应用于图像修复，采用基于循环的设计逐步优化修复状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2312.00752">Mamba : Linear-Time Sequence Modeling with Selective State Spaces</a></li>
<li><a href="https://arxiv.org/abs/2505.12630">[2505.12630] Degradation-Aware Feature Perturbation for All ... [2509.17792] Degradation-Aware All-in-One Image Restoration ... GitHub - eduardzamfir/DaAIR: GitHub repository for our ... Images Degradation-Aware Feature Perturbation for All-in-One Image ... degradation_aware_restoration/DFPIR at main · Vidit-guptaa ... DAIRNet: Degradation-aware All-in-one Image Restoration ... Degradation-Aware Residual-Conditioned Optimal Transport for ...</a></li>
<li><a href="https://arxiv.org/abs/2509.17792">[2509.17792] Degradation-Aware All-in-One Image Restoration ... GitHub - eduardzamfir/DaAIR: GitHub repository for our ... Images Degradation-Aware Feature Perturbation for All-in-One Image ... degradation_aware_restoration/DFPIR at main · Vidit-guptaa ... DAIRNet: Degradation-aware All-in-one Image Restoration ... Degradation-Aware Residual-Conditioned Optimal Transport for ...</a></li>

</ul>
</details>

**标签**: `#old photo restoration`, `#Mamba`, `#state-space model`, `#image restoration`, `#degradation-aware`

---

## 其他资讯

6. [DeepSeek V4 Flash 在单个 AMD MI300X 上运行，速度超过 150 tok/s](#item-6) ⭐️ 8.0/10
7. [Keyv 及相关 npm 包在活跃的 Shai-Hulud 供应链攻击中遭到入侵](#item-7) ⭐️ 8.0/10
8. [为自我改进而工程化智能体框架](#item-8) ⭐️ 8.0/10
9. [开放权重 AI 模型逼近前沿，安全差距依然存在](#item-9) ⭐️ 8.0/10
10. [MiniMax-H3 全模态模型移植到 MLX，支持 Apple Silicon](#item-10) ⭐️ 8.0/10
11. [阿里发布 Qwen3.8-Max：2.4 万亿参数开源权重模型](#item-11) ⭐️ 8.0/10
12. [FFmpeg 9.0 'Lei' 发布，带来新解码器和库版本升级](#item-12) ⭐️ 8.0/10
13. [Mistral 发布 Shieldstral：3B 开源多模态内容审核模型](#item-13) ⭐️ 7.0/10
14. [用于生成多样化肤色的新算法和色彩空间](#item-14) ⭐️ 7.0/10
15. [Waymo 在达拉斯向所有人开放无人驾驶打车服务](#item-15) ⭐️ 7.0/10
16. [Anthropic 与 AI 云初创公司 Volta 签署 100 亿美元协议](#item-16) ⭐️ 7.0/10
17. [英伟达开放安全 AI 联盟一周内发布 AI 代理防御提案](#item-17) ⭐️ 7.0/10
18. [LLM 让开源更实用](#item-18) ⭐️ 7.0/10
19. [玻璃基板初创公司巽霖科技融资近 2 亿元，有机基板危机加剧](#item-19) ⭐️ 7.0/10
20. [Kimi K3 与 DeepSeek V4：原生多模态的时间差](#item-20) ⭐️ 7.0/10
21. [AI 攻克传奇埃尔德什问题，塑造数学未来](#item-21) ⭐️ 7.0/10
22. [NVIDIA Alpamayo 2 Super 开放模型现已商用，助力自动驾驶](#item-22) ⭐️ 7.0/10
23. [商汤发布 SenseNova U1.5-Lite-Preview：8B 模型原生支持 4K 生成](#item-23) ⭐️ 7.0/10
24. [微软发布 Orchard：可扩展代理式 AI 开放框架](#item-24) ⭐️ 7.0/10
25. [LFM2.5-2.6B：面向本地代理的紧凑模型](#item-25) ⭐️ 6.0/10
26. [得州暂停新建数据中心，州长要求审计](#item-26) ⭐️ 6.0/10
27. [EON 计划用最快太空激光通信取代海底光缆](#item-27) ⭐️ 6.0/10
28. [AWS 将 vibe-coding 工具 Superblocks 集成到私有云中](#item-28) ⭐️ 6.0/10
29. [Moonshot PerceptionBench：多模态视觉模型新基准](#item-29) ⭐️ 6.0/10
30. [AI 转型引发菲律宾外包行业工人焦虑](#item-30) ⭐️ 5.0/10
31. [特朗普的 AI 保护主义延伸至机器人领域](#item-31) ⭐️ 5.0/10
32. [3D 视觉先驱 Marc Pollefeys 加入保加利亚 INSAIT](#item-32) ⭐️ 5.0/10

---

<a id="item-6"></a>
## [DeepSeek V4 Flash 在单个 AMD MI300X 上运行，速度超过 150 tok/s](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

一个 GitHub 项目展示了 DeepSeek V4 Flash（一个 284B 参数的 MoE 模型）在单个 AMD MI300X GPU 上以每秒超过 150 个 token 的速度运行。该实现将原本 100 万 token 的上下文长度缩减至 25.6 万 token，以适应硬件限制。 这表明大型 MoE 模型可以在单个高端 GPU 上以实用的权衡进行部署，可能降低 AI 推理的硬件门槛。它凸显了围绕 AMD MI300X 的生态系统日益壮大，以及量化和上下文长度优化对高效部署的重要性。 该模型对其 256 个 MoE 导出使用原生 MXFP4 量化，这有助于将其适配到 MI300X 的 192GB HBM3 内存中。MI300X 是 OAM 模块而非 PCIe 卡，该项目引用了之前在 2xMI300X 上的工作以及 HotAisle 等实验工具。

hackernews · zhoutong · 8月4日 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**背景**: DeepSeek V4 Flash 是一个混合专家（MoE）语言模型，总参数 284B，激活参数 13B，支持 100 万 token 的上下文。AMD MI300X 是一款数据中心 GPU，拥有 192GB HBM3 内存和 1.5TB/s 带宽，专为生成式 AI 工作负载设计。量化通过降低模型精度来减少内存占用，而缩减上下文长度也是将模型适配到有限硬件上的常用技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html">AMD Instinct™ MI300X Accelerators</a></li>
<li><a href="https://www.techpowerup.com/gpu-specs/radeon-instinct-mi300x.c4179">AMD Radeon Instinct MI300X Specs | TechPowerUp GPU Database</a></li>

</ul>
</details>

**社区讨论**: 社区评论对单个 MI300X 的实际可获得性提出担忧，指出它通常以 8-GPU 整机形式出售，价格约 25 万欧元。一些用户指出 MI350P 是 PCIe 替代品，拥有 144GB 内存，也能运行该模型。其他人讨论了缩减上下文长度的权衡，将其与 Codex 等模型比较，并质疑作者是否考虑了 DwarfStar 等替代方案。

**标签**: `#DeepSeek`, `#AMD MI300X`, `#LLM deployment`, `#quantization`, `#efficient inference`

---

<a id="item-7"></a>
## [Keyv 及相关 npm 包在活跃的 Shai-Hulud 供应链攻击中遭到入侵](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 8.0/10

Keyv 及多个相关 npm 包在名为“Shai-Hulud”的活跃供应链攻击中遭到入侵。攻击仍在进行中，恶意代码被注入这些包中，用于窃取凭据和其他敏感数据。 Keyv 是 Node.js 生态系统中广泛使用的缓存库，因此此次攻击可能影响大量应用程序和开发者。这凸显了 npm 供应链持续存在的脆弱性，以及采取更严格安全措施的必要性。 此次攻击属于 Shai-Hulud 系列，该系列此前已入侵数百个 npm 包并窃取开发者凭据。社区成员建议在 .npmrc 中设置“min-release-age=5”并禁用安装脚本以降低此类风险。

hackernews · cimi_ · 8月4日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

**背景**: npm 供应链攻击是指恶意代码被注入合法包中，通常通过入侵维护者账户或自动化发布实现。Shai-Hulud 攻击是继 s1ngularity 攻击和 Josh Junon（Qix）被入侵（其维护的 18 个包每周下载量达数十亿）之后，npm 生态的第三次重大供应链攻击。npm 安装脚本（preinstall、install、postinstall）是此类攻击的常见载体，因为它们在安装过程中会执行任意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack">Shai - Hulud npm Supply Chain Attack | Wiz Blog</a></li>
<li><a href="https://www.securityweek.com/shai-hulud-supply-chain-attack-worm-used-to-steal-secrets-180-npm-packages-hit/">Shai - Hulud Supply Chain Attack : Worm Used to... - SecurityWeek</a></li>
<li><a href="https://docs.npmjs.com/cli/v9/commands/npm-hook/?v=true">npm-hook - npm Docs</a></li>

</ul>
</details>

**社区讨论**: 社区对此感到震惊，并呼吁对安装钩子采取更严格的政策，有人建议暂停新增 pre-install/post-install 钩子。用户正在分享实用的缓解建议，例如在 .npmrc 中设置“min-release-age=5”，以及使用 grep 检查 node_modules 中是否包含被入侵的包。同时，也有人对导致这些攻击的脆弱依赖系统表示不满。

**标签**: `#supply chain attack`, `#npm security`, `#dependency management`, `#Keyv`, `#security`

---

<a id="item-8"></a>
## [为自我改进而工程化智能体框架](https://lilianweng.github.io/posts/2026-07-04-harness/) ⭐️ 8.0/10

Lilian Weng 的一篇博客文章讨论了如何通过工程化智能体框架（harness）实现自我改进，重点涉及适应度函数、工具优化和轨迹分析。该文章引发了社区讨论，获得 64 条评论和 8.0 的高分。 这很重要，因为优化智能体框架可以显著提高 AI 智能体的性能、质量和成本效率，这对于部署高效的 AI 系统至关重要。讨论中强调的实用策略可能会影响组织构建和优化基于智能体的解决方案的方式。 关键细节包括为代码库定义准确的适应度函数的重要性、利用轨迹分析来识别和修复问题，以及允许智能体编写自己的工具以减少 token 使用。社区成员还提到需要评估和验证/测试分割以防止奖励黑客行为。

hackernews · tosh · 8月4日 06:17 · [社区讨论](https://news.ycombinator.com/item?id=49164896)

**背景**: 智能体框架（agent harness）是围绕 AI 模型的软件基础设施，管理其生命周期、上下文和工具交互，使其成为可靠的自主智能体。适应度函数在优化中用于定义“好”的标准，在此上下文中，它们通过提供可衡量的目标帮助智能体自我改进。讨论还涉及训练提示词和代码而非仅训练模型权重的想法，表明优化范式的转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://harness-engineering.ai/?trk=article-ssr-frontend-pulse_little-text-block">Home | Harness Engineering</a></li>
<li><a href="https://www.linkedin.com/pulse/8-agentic-harness-engineering-patterns-you-should-know-tomer-bar-y6zqf">8 Agentic Harness Engineering Patterns You Should Know About</a></li>
<li><a href="https://qubittool.com/blog/agent-harness-evaluation-guide">Agent Harness Engineering Guide [2026]: Evaluating AI ... | QubitTool</a></li>

</ul>
</details>

**社区讨论**: 社区评论对实际实施表示热情，一位用户指出自动研究对框架的强大作用，并强调让智能体读取生产轨迹和编写自己的工具的重要性。另一位用户认为训练权重已达到顶峰，是时候转向提示词和代码的训练范式，还有人推测框架将生成自己的 RLHF/DPO 训练集以进行微调。

**标签**: `#AI agents`, `#harness engineering`, `#LLM optimization`, `#code quality`, `#efficiency`

---

<a id="item-9"></a>
## [开放权重 AI 模型逼近前沿，安全差距依然存在](https://techcrunch.com/2026/08/04/open-weight-ai-models-are-catching-up-to-the-frontier-the-safety-gap-remains/) ⭐️ 8.0/10

SaferAI 的一份新报告显示，Z.ai 的开放权重模型 GLM-5.2 接近前沿 AI 能力，但缺乏关键的安全缓解措施，重新引发了对治理的担忧。 这凸显了开放权重模型在能力与安全之间的关键差距，可能超越治理和安全保障。对研究人员、政策制定者以及更广泛的 AI 生态系统具有重要意义，因为它强调了建立强健安全框架的必要性。 报告特别指出，GLM-5.2 虽然接近前沿性能，但缺乏领先封闭模型中所标配的某些安全缓解措施。这引发了对开放权重模型负责任部署的质疑。

rss · TechCrunch AI · 8月4日 20:05

**背景**: 开放权重模型是指其训练参数（权重）公开发布的 AI 模型，允许他人下载和使用。虽然它们促进了创新和可及性，但如果没有内置安全措施，也会带来风险。前沿 AI 指的是最先进的 AI 系统，通常由拥有大量资源的领先实验室开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>
<li><a href="https://www.bearnetai.com/blog/understanding-frontier-ai/">Understanding Frontier AI | BearNetAI - Bytes to Insights</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#open-weight models`, `#GLM-5.2`, `#frontier AI`, `#governance`

---

<a id="item-10"></a>
## [MiniMax-H3 全模态模型移植到 MLX，支持 Apple Silicon](https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/#atom-everything) ⭐️ 8.0/10

MiniMax 发布了全模态生成系统 MiniMax-H3，而 PipeNetwork/minimax-h3-mlx 包将其移植到 MLX 以支持 Apple Silicon。Simon Willison 在 M5 Max MacBook Pro 上成功运行了它，根据文本提示生成了带音频的 15 秒视频片段。 这一移植使得在 Apple Silicon 上本地生成全模态内容成为可能，让 Mac 用户无需依赖云端即可使用先进的生成式 AI。这凸显了针对消费级硬件优化的高效扩散和生成模型生态系统的不断壮大。 该模型下载约 115 GB 的文件，在 M5 Max 上生成视频耗时不到 45 分钟。由于缺乏提示指导，生成的音频被描述为“奇怪的类似语音的垃圾”，但提示指南提供了获得更好结果的说明。

rss · Simon Willison · 8月4日 19:10

**背景**: MiniMax-H3 是一个通用的全模态生成系统，接受文本、图像、音频和视频输入，并可生成最长 15 秒的带音频视频片段。MLX 是 Apple 为 Apple Silicon 上的机器学习设计的数组框架，此次移植利用它实现本地执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H3: An Open Model Breaking the Boundaries Between Tasks and Modalities - MiniMax Research | MiniMax</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-H3">MiniMaxAI/MiniMax-H3 · Hugging Face</a></li>
<li><a href="https://www.marktechpost.com/2026/08/01/minimax-releases-minimax-h3-an-omni-modal-video-model-that-generates-15-second-2k-clips-with-native-stereo-audio/">MiniMax Releases MiniMax H3: An Omni-Modal Video Model That Generates 15-Second 2K Clips With Native Stereo Audio - MarkTechPost</a></li>

</ul>
</details>

**标签**: `#MiniMax-H3`, `#MLX`, `#omni-modal`, `#video generation`, `#Apple Silicon`

---

<a id="item-11"></a>
## [阿里发布 Qwen3.8-Max：2.4 万亿参数开源权重模型](https://news.google.com/rss/articles/CBMimAFBVV95cUxNZXNsNmhlZmN6ZUFOSEthcjJNTnJXdHBHQ3RSLTRjZ0UyTGFHT3BHSGRLRXN1MEEydVdrWUZGQzlld2V5eWlwMmtMSTgyMW93cDBnV0ZEWkZDeG5iYmpYSXdDU1BQbXF4bFMzdnhrTHBNbkRIYUVaT1pSaTBkVDZ2a2RmOXN2MEpxcXJYQkRjdlA2d21lOHB6OQ?oc=5) ⭐️ 8.0/10

阿里巴巴宣布推出 Qwen3.8-Max，这是一个拥有 2.4 万亿参数的混合专家模型，并承诺下周将在 Hugging Face 和 ModelScope 上发布开放权重。目前该模型已通过阿里巴巴的 Token Plan、Qoder 和 QoderWork 提供托管预览。 此次发布标志着开放权重 AI 的一个重要里程碑，因为这是阿里巴巴首个 Max 级开放权重模型，可能媲美领先的前沿模型。它有望使最先进的 AI 能力更加普及，并推动开源社区的创新。 该模型具有 100 万 token 的上下文窗口，并被描述为“当今最强大的模型之一，与领先的前沿 AI 模型兼容，仅次于 Fable 5”。然而，开放权重尚未发布，且该模型并非为消费者本地推理设计；计划于 2026 年 8 月单独发布 Qwen3.8-27B。

google_news · MLQ.ai · 8月4日 11:47

**背景**: 开放权重 AI 模型，如 Meta 和 Mistral 的模型，允许开发者下载并微调模型权重，促进透明度和定制化。阿里巴巴的 Qwen 系列一直是重要的开放权重模型家族，而 Qwen3.8-Max 代表了参数规模的显著提升，旨在与 GPT-4 和 Claude 等专有模型竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ai.joaoqueiros.com/blog/qwen3-8-max-official-guide-architecture-agents-benchmarks-open-weights">Qwen3.8 Max Official Guide: Architecture, Agents, Benchmarks ...</a></li>
<li><a href="https://we.inc/blog/qwen3-8-max-open-weights-build-apps">Qwen3.8-Max Just Dropped as Open Weights. Here Is What ...</a></li>
<li><a href="https://techsy.io/en/blog/qwen-3-8">Qwen3.8: 2.4T Parameters, Open Weights, No Benchmarks</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#Alibaba`, `#open-weight`, `#Qwen`

---

<a id="item-12"></a>
## [FFmpeg 9.0 'Lei' 发布，带来新解码器和库版本升级](https://news.google.com/rss/articles/CBMikwFBVV95cUxONTY0Z29oNHBtY0hnTzlqenE5bnQ0UDdtdUlnSU1YQkVlMm9qU2Rtc2RKSGJZUGdTeU9nS2dpU2I5UENBaW9Odk1UUG1DT1RVQjMwVVRkX0tPMi1JMUNGMmZ4X2lVRUlPOVozUkVDeWRRX2Uxd3FnNW40OUk1RWNta0szMldhZngyck1aZjdJd1JEbFE?oc=5) ⭐️ 8.0/10

FFmpeg 9.0 'Lei' 于 2026 年 8 月 4 日正式发布，作为开源多媒体框架的一次重大更新。该版本引入了新的解码器，扩展了 AMF 颜色转换器的 HDR 功能，在 MP4 封装器中增加了 LCEVC 轨道复用支持，并将所有核心库升级到新的主版本，其中 libavcodec 和 libavformat 达到 63 系列。 FFmpeg 是多媒体处理的基础工具，广泛应用于视频处理流程、AI/ML 工作流和图像增强。此次重大发布带来了显著改进，将影响依赖 FFmpeg 进行编码、解码和过滤任务的开发者和研究人员。 该版本距 FFmpeg 8.1 发布约四个月，命名为 'Lei' 以纪念雷晓华逝世十周年。所有核心库都已升级到新的主版本，开发者可能需要更新代码以保持兼容性。

google_news · 9to5Linux · 8月4日 00:20

**背景**: FFmpeg 是一个免费开源项目，提供用于处理视频、音频和其他多媒体文件及流的库和命令行工具。它广泛用于转换、编码、解码、流媒体、过滤和缩放。像 9.0 这样的主版本发布通常会引入新功能和破坏性更改，因此对开发者社区具有重要意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5linux.com/ffmpeg-9-0-lei-open-source-multimedia-framework-officially-released">FFmpeg 9.0 "Lei" Open-Source Multimedia Framework Officially ...</a></li>
<li><a href="https://www.linuxcompatible.org/story/ffmpeg-90-lei-released-library-bumps-and-dev-impact/">FFmpeg 9.0 Lei Released: Library Bumps and Dev Impact</a></li>
<li><a href="https://en.wikipedia.org/wiki/FFmpeg">FFmpeg - Wikipedia</a></li>

</ul>
</details>

**标签**: `#FFmpeg`, `#multimedia`, `#video processing`, `#open source`, `#release`

---

<a id="item-13"></a>
## [Mistral 发布 Shieldstral：3B 开源多模态内容审核模型](https://mistral.ai/news/shieldstral/) ⭐️ 7.0/10

Mistral AI 发布了 Shieldstral，这是一个 3B 参数的开源权重模型，专为多模态内容审核设计。通过将审核任务构建为策略自适应问答任务，其性能超越了高达其 7 倍规模的模型。 该发布为内容审核提供了成本效益高、可本地部署的解决方案，这对社交平台和图像分享服务至关重要。同时，这也标志着 Mistral 战略转向更小、更专业化的模型，以在实际应用中竞争。 Shieldstral 使用 LoRA 对语言模型参数进行微调，并在单个输出 token 上使用交叉熵损失。该模型在 Hugging Face 上以'mistralai/Shieldstral-1.0-3B'提供，专为设备端或边缘部署设计。

hackernews · riadsila · 8月4日 16:36 · [社区讨论](https://news.ycombinator.com/item?id=49171268)

**背景**: 多模态内容审核涉及分析文本、图像、音频和视频，以检测并移除违反政策的内容。传统的审核系统通常依赖大型集中式 API，这可能成本高昂并引发隐私问题。Shieldstral 的开源权重方法允许开发者在本地部署审核，从而降低延迟并提高数据隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/shieldstral/">Introducing Shieldstral . | Mistral AI</a></li>
<li><a href="https://arxiv.org/html/2607.25857">Shieldstral</a></li>
<li><a href="https://scalevise.com/resources/mistral-shieldstral-on-device-content-safety-model/">Mistral Shieldstral : On-Device Content Safety Model</a></li>

</ul>
</details>

**社区讨论**: 社区成员对该模型的灵活性表示好奇，质疑它是否能在不重新训练的情况下调整到任意规则集。一些人称赞 Mistral 专注于更小、更精细调整的模型，而另一些人则将其与 OpenAI 的审核 API 进行比较，并指出其作为成本效益高的第一道防线的潜力。

**标签**: `#AI safety`, `#content moderation`, `#Mistral`, `#open-weights`, `#multimodal`

---

<a id="item-14"></a>
## [用于生成多样化肤色的新算法和色彩空间](https://toneyalexander.github.io/inclusive-color-space/) ⭐️ 7.0/10

一位开发者创建了一个包容性的色彩空间和程序化生成算法，用于生成多样化的肤色，并提供了交互式演示和详细解释。该项目在专门的网页上展示，并在 Hacker News 上引起了广泛关注。 该项目解决了数字艺术和游戏开发中的一个实际挑战，使选择合理且多样化的肤色变得更加容易。它为技术领域的包容性讨论和色彩科学做出了贡献，可能影响开发者处理肤色表现的方式。 该算法基于自定义色彩空间，以直观的方式映射肤色，便于选择和生成。项目包含交互式演示和“未来工作”部分，表明还有改进空间。作者称方法“有点不稳固”，但结果广受好评。

hackernews · automatoney · 8月4日 15:16 · [社区讨论](https://news.ycombinator.com/item?id=49170165)

**背景**: 数字媒体中的肤色表现通常依赖于有限的调色板或手动选择，这可能存在偏见或不完整。RGB、HSV 和 CIELAB 等色彩空间常用于皮肤检测和分类，但可能未针对生成多样化肤色进行优化。该项目旨在通过提出一种专为肤色生成定制的新色彩空间来填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://onlinelibrary.wiley.com/doi/full/10.1002/col.70012">A New Method for Skin Color Classification Based on Global ...</a></li>
<li><a href="https://arxiv.org/pdf/1708.02694">Human Skin Detection Using RGB, HSV and YCbCr Color Models A New Method for Skin Color Classification Based on Global ... Personal color analysis using color space algorithm - Springer HUMAN-SKIN-DETECTION-USING-DIFFERENT-COLOR-SPACES - GitHub A NOVEL SKIN COLOR MODEL IN YCBCR COLOR SPACE AND ITS ... Skin Tone Estimation under Diverse Lighting Conditions - MDPI</a></li>

</ul>
</details>

**社区讨论**: 社区称赞了该项目的创意和执行，一些人指出使用 PCA 和函数拟合是巧妙的方法。其他人讨论了肤色感知的复杂性，并引用了 Pantone 肤色和 The Pudding 的化妆品色号数据等现有资源。一些用户观察到生成的某些颜色呈现绿色、蓝色或紫色，表明存在潜在局限性。

**标签**: `#color space`, `#skin tone generation`, `#computer graphics`, `#algorithm`, `#digital art`

---

<a id="item-15"></a>
## [Waymo 在达拉斯向所有人开放无人驾驶打车服务](https://waymo.com/blog/shorts/dallas-open-to-all/) ⭐️ 7.0/10

Waymo 已正式在德克萨斯州达拉斯向所有用户开放其无人驾驶打车服务，标志着其自动驾驶汽车运营的重大扩展。该服务现已向公众开放，而不仅仅是早期乘客。 此次扩张意义重大，因为它将自动驾驶打车服务带到了一个低密度、以汽车为中心的大型都会区，证明了该技术在密集城市核心区之外的可行性。它可能影响城市规划和交通政策，因为无人驾驶汽车可能减少停车需求并改变通勤模式。 Waymo 已提供超过 2000 万次出行，满意度达 93%，达拉斯上线是其 2026 年更广泛扩张的一部分，包括德克萨斯州和佛罗里达州。该服务在无人类安全驾驶员的情况下运营，依赖 Waymo 的自动驾驶技术。

hackernews · xnx · 8月4日 18:29 · [社区讨论](https://news.ycombinator.com/item?id=49172836)

**背景**: Waymo 是 Alphabet 的子公司，运营着全球首个自动驾驶打车服务。自动驾驶汽车（也称为机器人出租车）利用传感器和人工智能在无需人工输入的情况下导航。Waymo 已从凤凰城和旧金山等城市扩展到新市场，此次达拉斯上线是其扩大运营的关键一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://waymo.com/">Waymo - Self-Driving Cars - Autonomous Vehicles - Ride - Hail</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-driving_car">Self-driving car - Wikipedia</a></li>
<li><a href="https://www.techbuzz.ai/articles/waymo-doubles-down-on-2026-expansion-with-texas-and-florida-push">Waymo doubles down on 2026 expansion with Texas... | The Tech Buzz</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体积极，用户指出 Waymo 相比人类驾驶员更安全、更可预测。一些人讨论无人驾驶汽车通过减少停车需求而成为可负担住房政策的潜力，而另一些人则提出涉及自动驾驶汽车事故的责任和罚款等法律问题。

**标签**: `#autonomous vehicles`, `#Waymo`, `#transportation`, `#urban planning`

---

<a id="item-16"></a>
## [Anthropic 与 AI 云初创公司 Volta 签署 100 亿美元协议](https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/) ⭐️ 7.0/10

据报道，Anthropic 与 AI 云初创公司 Volta 签署了一项价值 100 亿美元的协议，以确保未来六年的云计算能力。Volta 在获得 Nvidia 和 Dell 支持后从隐身模式中亮相，并在同一公告中估值达 24 亿美元。 这笔交易凸显了专业 AI 云基础设施日益增长的重要性，以及领先 AI 实验室对计算资源的激烈竞争。同时，它也标志着由主要硬件供应商支持的新云初创公司的崛起，这可能会重塑 AI 基础设施的格局。 据 Volta 称，该协议为期六年，Volta 由 Ricard Boada 和 Sofia Gumuzio 于今年早些时候创立。彭博社最初报道了这笔交易，Volta 拒绝透露客户名称，但 TechCrunch 确认客户为 Anthropic。

rss · TechCrunch AI · 8月4日 19:48

**背景**: Anthropic 是一家 AI 安全和研究公司，由前 OpenAI 成员于 2021 年创立，其中包括 Daniela 和 Dario Amodei 兄妹。该公司一直在扩大其云合作伙伴关系，此前已选择 Google Cloud 作为其主要云提供商。Volta 是一家新的 AI 云初创公司，为 AI 开发者提供云计算能力，并得到了 Nvidia 和 Dell 的支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/">Anthropic signs $10B deal with AI cloud startup Volta | TechCrunch</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-04/nvidia-dell-back-ai-cloud-startup-volta-at-2-4-billion-value">Nvidia, Dell Back AI Cloud Startup Volta at $2.4 Billion... - Bloomberg</a></li>
<li><a href="https://www.anthropic.com/news/anthropic-partners-with-google-cloud">Anthropic Partners with Google Cloud \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI cloud`, `#business deal`, `#infrastructure`

---

<a id="item-17"></a>
## [英伟达开放安全 AI 联盟一周内发布 AI 代理防御提案](https://techcrunch.com/2026/08/04/nvidia-doesnt-mess-around-a-week-after-open-ai-industry-group-formed-its-already-showing-progress/) ⭐️ 7.0/10

由英伟达一周前发起、现已拥有超过 120 家成员公司的开放安全 AI 联盟，已经发布了针对 AI 代理的防御提案。这一快速进展发生在联盟于 2026 年 7 月 27 日成立之后，创始成员包括微软、CrowdStrike、思科、IBM、Palo Alto Networks 和 Red Hat。 这一进展意义重大，因为它展示了行业协同努力应对 AI 代理带来的新兴安全威胁，这些代理能够自主执行任务并引入独特的漏洞。随着超过 120 家公司的参与，联盟的提案可能为 AI 安全设定标准，并影响组织保护其 AI 系统的方式。 该联盟成立时有 37 个创始成员，此后已发展到超过 120 家公司，据报道是在 Hugging Face 事件之后。提案侧重于防御 AI 代理，这些代理是由大型语言模型驱动的自主系统，能够推理、规划、使用工具并采取行动，将攻击面扩展到传统的提示注入之外。

rss · TechCrunch AI · 8月4日 19:28

**背景**: AI 代理是自主执行任务或根据预定义目标和数据输入做出决策的软件实体。它们引入了独特的安全风险，如工具滥用和更广泛的攻击面，这与传统软件漏洞不同。开放安全 AI 联盟旨在构建和共享开放工具，以促进 AI 的负责任使用和信任，应对这些新兴威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/open-secure-ai-alliance/">Industry Leaders Unite in Open Secure AI Alliance for AI ...</a></li>
<li><a href="https://cybersecuritynews.com/open-secure-ai-alliance/">NVIDIA Launches Open Secure AI Alliance to Build Open-Source ...</a></li>
<li><a href="https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html">NVIDIA Forms 37-Member Open Secure AI Alliance and Open ...</a></li>

</ul>
</details>

**标签**: `#AI security`, `#Nvidia`, `#AI agents`, `#industry news`

---

<a id="item-18"></a>
## [LLM 让开源更实用](https://simonwillison.net/2026/Aug/3/devtools-must-be-open-source-exedev/#atom-everything) ⭐️ 7.0/10

Simon Willison 认为，LLM 降低了阅读和修改开源代码的门槛，使开源理想更易实现。他描述了使用 Claude 和 Codex 克隆并构建项目，将编译视为零时间投入。 这一转变可能增加开源参与度，因为开发者现在可以理解并修改他们以前因时间限制而回避的代码。这也凸显了 AI 在软件开发中日益重要的作用，可能改变开发者与代码库互动的方式。 Willison 指出，虽然他尚未习惯性地修改软件，但他看到了一条一年前不存在的路径。他使用 Claude Code 和 Codex 等工具来检出并构建项目，减少了编译软件的摩擦。

rss · Simon Willison · 8月3日 15:30

**背景**: 开源软件允许用户研究、修改和分发代码，但阅读和编译代码的实际障碍限制了参与。LLM 和 AI 辅助开发工具越来越擅长理解和生成代码，这可以帮助开发者快速掌握不熟悉的代码库。这一趋势反映在越来越多的 AI 编码工具和 SWE-bench 等基准测试中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-source_software">Open-source software - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI-assisted_software_development">AI-assisted software development</a></li>
<li><a href="https://benchlm.ai/coding">Best LLM for Coding (August 2026): SWE-bench... | BenchLM.ai</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论可能包含多种观点，一些人同意 LLM 减少了摩擦，而另一些人可能质疑 LLM 提供的可靠性或理解深度。有些人还可能讨论对开源维护和安全的影响。

**标签**: `#open source`, `#LLM`, `#developer tools`, `#AI-assisted development`

---

<a id="item-19"></a>
## [玻璃基板初创公司巽霖科技融资近 2 亿元，有机基板危机加剧](https://36kr.com/p/3924953058605444?f=rss) ⭐️ 7.0/10

国内玻璃基板领军企业巽霖科技宣布完成近 2 亿元 B 轮融资，这是该公司半年内完成的第三轮融资。本轮由英诺基金、千乘资本、海目星、光莆股份等新股东投资，金雨茂物等老股东持续加码。 这笔融资凸显了在 AI 需求和供应危机的推动下，半导体封装从有机基板向玻璃基板转变的加速趋势。它标志着投资者对玻璃基板技术作为解决有机材料局限性的方案信心增强，可能重塑先进封装供应链。 募集资金将用于产能扩张、封装产线建设、制程精度升级以及光通讯应用。巽霖在天津运营一座全流程玻璃基板工厂，年产能 30 万平方米，并宣称覆铜结合强度与直通良率行业领先。

rss · 36氪 · 8月4日 08:31

**背景**: 玻璃基板正成为 ABF（味之素堆积膜）和 FR-4 等有机基板的下一代替代品，后者正面临供应短缺和价格上涨。电子级玻璃纤维布（有机基板的关键成分）价格较 2025 年低点翻倍，FR-4 覆铜板涨幅超 270%，使玻璃基板越来越具有成本竞争力。英特尔和台积电等巨头正大力投资玻璃芯基板技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1915009352739325530">玻璃基板基础概念 - 知乎专栏</a></li>
<li><a href="https://xueqiu.com/8975183935/397028318">玻璃基板为什么突然站上风口？产业逻辑与核心标的全梳理 最近 " 康宁 ...</a></li>
<li><a href="https://xueqiu.com/6298220255/384359762">ABF载板深度解析：AI芯片的"骨架"与国产替代机遇 核心观点：ABF载板是...</a></li>
<li><a href="https://baike.baidu.com/item/电子布/6871946">电子布_百度百科</a></li>

</ul>
</details>

**标签**: `#glass substrate`, `#semiconductor packaging`, `#AI hardware`, `#funding`, `#supply chain`

---

<a id="item-20"></a>
## [Kimi K3 与 DeepSeek V4：原生多模态的时间差](https://36kr.com/p/3924826666301831?f=rss) ⭐️ 7.0/10

文章讨论了 Kimi K3 与 DeepSeek V4 在原生多模态能力上的时间差，强调视觉反馈在长链任务中的重要性。7 月发布的 Kimi K3 具备原生多模态能力，并以 1679 分登顶 Arena Frontend Code 榜单。 这很重要，因为随着 AI 智能体承担更长更复杂的任务，原生多模态能力对于准确的反馈和决策变得至关重要。中国 AI 实验室之间的技术路线分歧，如月之暗面对原生多模态的投入与 DeepSeek 的文本优先策略，将塑造 AI 模型的竞争格局。 Kimi K3 是一个总参数 2.8 万亿、支持 1 亿 token 上下文的 MoE 模型。它采用“视觉在环”方法，在代码和截图之间迭代以发现视觉问题。相比之下，DeepSeek、智谱和腾讯混元的最新基座模型仍以文本输入为主。

rss · 36氪 · 8月4日 06:32

**背景**: 原生多模态模型从预训练阶段就整合视觉和文本数据，使模型能够基于视觉反馈进行感知和决策。这与使用外部 OCR 或 VLM 工具将图像转换为文本的模块化方法形成对比。关于多模态对于理解世界是否必要的争论仍在继续，伊利亚·苏茨克维和杨立昆持有相反观点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.volcengine.com/articles/7423250335407276058">多 模 态 大 模 型 : 盘点&Highlights part3——Gemini...</a></li>
<li><a href="https://jimmysong.io/ai/google-gemini/">Google Gemini - Jimmy Song</a></li>
<li><a href="https://juejin.cn/post/7646986336994574376">2026...</a></li>

</ul>
</details>

**标签**: `#Kimi K3`, `#原生多模态`, `#大模型`, `#Agent`, `#Coding`

---

<a id="item-21"></a>
## [AI 攻克传奇埃尔德什问题，塑造数学未来](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) ⭐️ 7.0/10

《Quanta Magazine》报道，AI 已成功解决了传奇的埃尔德什问题集中的多个难题，该问题集包含数学家保罗·埃尔德什提出的一千多个猜想。这标志着 AI 在攻克离散数学和数论中开放问题方面取得了重要里程碑。 这一进展可能改变数学研究，表明 AI 能够助力解决长期未解的开放问题，从而加速组合学和图论等领域的发展。同时，它也促使数学家重新思考数学创造力的本质以及人类直觉的作用。 埃尔德什问题数据库包含 1217 个问题，其中许多仍未解决。AI 在涉及穷举搜索或模式识别的问题上表现尤为突出，但部分解决方案仍需人工验证以确保严谨性。

rss · Quanta Magazine · 8月3日 15:05

**背景**: 保罗·埃尔德什是 20 世纪多产的数学家，以大量猜想和合作著称，并催生了“埃尔德什数”的概念。埃尔德什问题集正是这些猜想的集合，涵盖离散数学、图论和数论等领域。AI 近期在数学上的突破，例如用新颖的证明策略解决猜想，引发了人们对机器学习如何辅助人类数学家的兴趣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Erdős_problems">Erdős problems</a></li>
<li><a href="https://teorth.github.io/erdosproblems/?status=solved">Erdős Problems Database - Interactive Table</a></li>
<li><a href="https://www.forbes.com/sites/anishasircar/2026/04/17/ai-solved-a-mathematical-problem-that-had-stumped-the-worlds-best-minds-for-decades/">AI Solved A Mathematical Problem That Had Stumped ... - Forbes</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#Erdős problems`, `#research`

---

<a id="item-22"></a>
## [NVIDIA Alpamayo 2 Super 开放模型现已商用，助力自动驾驶](https://news.google.com/rss/articles/CBMif0FVX3lxTE5KRGwtanIyNnR0dDVKaDA3djNwNUo1bS1Va3MyUlR6RTVwMV9RV0RyUjdrMFpyQWRNNWRRbXVQX1VlekNwTFJJRXFfMm1pWUpnY19qbE1yVUJwOG52a19ITFl3dlhUZVVEZFFiRGhmY0NkMEo4SGl4bUhRenRmVGM?oc=5) ⭐️ 7.0/10

NVIDIA 宣布 Alpamayo 2 Super 现已商用，这是一款面向自动驾驶和机器人出租车的领先开放推理模型。该模型现已采用开放商业许可，可供更广泛的行业采用。 此次发布标志着自动驾驶迈向生产就绪的重要一步，因为 Alpamayo 2 Super 提供了领先的推理能力和可检查的决策。它可能通过为自动驾驶社区提供强大的开放基础模型，加速 L4 级自动驾驶汽车和机器人出租车的部署。 Alpamayo 2 Super 是一个 340 亿参数的基础模型，结合了 32B VLM 主干和 2B 扩散专家。它是 Alpamayo 系列的一部分，该系列是 Hugging Face 上自动驾驶领域采用最广泛的开放推理模型，并在单一模型中支持多种与自动驾驶相关的能力。

google_news · NVIDIA Blog · 8月4日 15:08

**背景**: 自动驾驶汽车需要能够在复杂环境中安全感知、推理和行动的 AI 模型。NVIDIA 的 Alpamayo 模型被设计为开放的推理视觉-语言-动作（VLA）模型，允许开发者构建和定制自动驾驶系统。Alpamayo 2 Super 的商用化提供了一个前沿的开放模型，可用于生产环境，可能降低公司开发机器人出租车和其他自动驾驶解决方案的门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/">NVIDIA Alpamayo 2 Super, the Frontier Open Model for ...</a></li>
<li><a href="https://github.com/NVlabs/alpamayo2">GitHub - NVlabs/ alpamayo 2 : NVIDIA Alpamayo 2 Super is an open...</a></li>
<li><a href="https://huggingface.co/blog/nvidia/nvidia-alpamayo-2">Taking Alpamayo to New Heights with Driving Foundation Models and...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#autonomous vehicles`, `#AI model`, `#robotaxis`, `#open model`

---

<a id="item-23"></a>
## [商汤发布 SenseNova U1.5-Lite-Preview：8B 模型原生支持 4K 生成](https://news.google.com/rss/articles/CBMiSkFVX3lxTFBBVlVWUmZKZVhmYTFTa1RoUHdMQkRBeXJ0MU8xYUNJR1pIU2VJWll0N0E4Z0pUeVkzdk9jZ0FFUHdVODBZUFgwRUVB?oc=5) ⭐️ 7.0/10

商汤科技开源了 SenseNova U1.5-Lite-Preview，这是一个 8B-MoE 统一多模态模型，原生支持 4K 分辨率的图像生成、理解、推理和编辑。作为预览版，该模型相比前代 U1 在视觉能力上有显著提升。 此次发布推动了高分辨率 AI 图像生成的普及，因为开源 8B 模型支持原生 4K 输出，降低了开发者和创作者的使用门槛。同时，它也加剧了生成式 AI 领域的竞争，原生 4K 生成正成为新标准，如字节跳动的 Seedream 4.0。 该模型采用 NEO-Unify 架构，支持精确编辑，能复制信息图表和创意内容中的设计框架。作为预览版，训练数据和性能基准的细节有限，但官方表示在视觉理解和生成方面相比 U1 有显著改进。

google_news · AIBase · 8月3日 11:38

**背景**: SenseNova 是商汤科技的大型 AI 模型系列，其中 U 系列专注于统一多模态能力。原生 4K 生成意味着模型可以直接输出 4K 分辨率的图像，无需放大，这需要大量的计算资源。其他模型如字节跳动的 Seedream 4.0 也提供原生 4K 生成，表明 AI 图像生成正朝着更高分辨率输出的趋势发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xix.ai/live/6376">SenseTime open-sourced SenseNova U 1 . 5 - Lite - Preview , an... - xix.ai</a></li>
<li><a href="https://pandaily.com/sensetime-sensenova-u15-lite-preview-4k-open-source-jul2026">SenseTime Open-Sources SenseNova U 1 . 5 - Lite - Preview ... - Pandaily</a></li>
<li><a href="https://inf.news/en/tech/a34709ab21855ac537d6e53850f005b4.html">SenseTime releases open-source SenseNova U 1 . 5 - Lite - Preview ...</a></li>

</ul>
</details>

**标签**: `#4K image generation`, `#SenseTime`, `#generative models`, `#AI research`

---

<a id="item-24"></a>
## [微软发布 Orchard：可扩展代理式 AI 开放框架](https://news.google.com/rss/articles/CBMinAFBVV95cUxOeE41QWVkRWZIRS1JNW1UQ2ItdllValRYMk1Uby11emRxWTdzcWFORmRUWThpRk1ZY25OdFFoNVBRYlgwa3VHcWd2SExZdWlhbTZhYTRMWl90cUNXRndVZXJXd29XemVHWk5Ed3VFcThVc09DbWNoeUo4RnhOb0lFSUp3RHhfQkNZMzhzeGxoemdNamJyVlVyaHFQNDk?oc=5) ⭐️ 7.0/10

微软宣布了 Orchard，这是一个为可扩展且成本效益高的代理式 AI 研究设计的开源框架。它引入了 Orchard Env，一个可复用的环境服务，用于跨多个任务领域训练和评估代理。 Orchard 解决了限制代理式 AI 开放研究的基础设施和训练差距，代理式 AI 旨在将 LLM 转变为自主代理。通过提供共享基础，它可以加速开发并民主化先进代理系统的访问，影响 AI 生态系统中的研究人员和开发者。 Orchard 围绕 Orchard Env 构建，这是一个稳定的环境服务而非流水线的一部分，支持跨软件工程、浏览器导航、计算机使用和个人助理工作流探索代理建模配方。该框架是开源的，可在 GitHub 上获取，旨在克服对专有代码库和服务的依赖。

google_news · Microsoft · 8月3日 16:00

**背景**: 代理式 AI 指的是能够感知、思考并自主行动以实现用户定义目标的系统，超越了静态聊天机器人。这些系统通常使用大型语言模型（LLM）进行规划、推理和工具使用，并与环境进行多轮交互。然而，许多高性能代理系统依赖专有基础设施，限制了开放研究和可复现性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/blog/orchard-an-open-framework-for-scalable-agentic-ai/">Orchard: An open framework for scalable agentic AI ...</a></li>
<li><a href="https://github.com/microsoft/orchard">GitHub - microsoft/Orchard: Orchard: An Open-Source Agentic ...</a></li>
<li><a href="https://www.microsoft.com/en-us/research/publication/orchard-an-open-source-agentic-modeling-framework/">Orchard: An Open-Source Agentic Modeling Framework</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#Microsoft`, `#scalable AI`, `#open framework`

---

<a id="item-25"></a>
## [LFM2.5-2.6B：面向本地代理的紧凑模型](https://huggingface.co/blog/LiquidAI/lfm2-5-2-6b) ⭐️ 6.0/10

Liquid AI 发布了 LFM2.5-2.6B，这是一个专为本地代理部署设计的 26 亿参数紧凑型语言模型。据报道，该模型在代理基准测试中表现优于其四倍大小的模型。 此次发布对高效 AI 具有重要意义，因为它使得在设备端无需依赖云基础设施即可实现强大的代理能力。这可能降低开发者和企业在本地部署自主 AI 代理的门槛，增强隐私并减少延迟。 该模型是 LFM2 系列的一部分，采用针对设备端部署优化的混合架构。它可在 Hugging Face 上获取，并可通过 Ollama 等工具本地运行，支持工具调用和代理工作流。

rss · Hugging Face Blog · 8月4日 13:58

**背景**: 语言模型通常规模庞大，需要大量计算资源，使得本地部署具有挑战性。像 LFM2.5-2.6B 这样的紧凑模型旨在将先进的 AI 能力带到边缘设备，实现实时、私密且成本效益高的应用。代理模型旨在自主执行任务，例如调用工具或与用户交互，这对于构建 AI 代理至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chats-llm.com/en/blog/lfm2-5-2-6b-release">LFM 2 . 5 - 2 . 6 B : Liquid AI's New Agentic Open-Source Model</a></li>
<li><a href="https://ollama.com/library">Browse Ollama's library of models .</a></li>

</ul>
</details>

**标签**: `#language model`, `#local deployment`, `#efficient AI`, `#Hugging Face`

---

<a id="item-26"></a>
## [得州暂停新建数据中心，州长要求审计](https://techcrunch.com/2026/08/04/texas-halts-new-data-centers-as-governor-calls-for-audits/) ⭐️ 6.0/10

得克萨斯州已暂停批准新建数据中心，州长要求进行审计，理由是电网压力过大。 此举标志着 AI 和数据中心行业面临日益严重的基础设施和能源限制，可能影响科技公司在得州的扩张计划，并促使其他州重新考虑类似政策。 暂停适用于新建数据中心的审批，审计将检查电力使用和电网影响。摘要中未提供具体日期或数字。

rss · TechCrunch AI · 8月4日 15:42

**背景**: 数据中心需要大量电力，得州因其放松管制的能源市场和充足的电力吸引了众多数据中心。然而，快速增长给电网带来了压力，导致了这一监管措施。

**标签**: `#data centers`, `#energy`, `#infrastructure`, `#Texas`

---

<a id="item-27"></a>
## [EON 计划用最快太空激光通信取代海底光缆](https://techcrunch.com/2026/08/04/eon-wants-to-move-the-data-superhighway-from-ocean-fiber-to-space-lasers/) ⭐️ 6.0/10

今年 5 月成立的初创公司 Endeavor Optical Networks（EON）已从隐身模式中走出，获得 General Catalyst 和 Andreessen Horowitz 提供的 1075 万美元种子资金，并宣布计划发射其声称迄今最快的太空激光通信系统，目标数据传输速率达 2.4 Tbps。 这一进展可能通过提供比海底光缆更快、可能更低延迟的替代方案，对全球数据传输产生重大影响，尤其适用于数据中心互联。它凸显了利用天基光链路处理卫星和 AI 工作负载产生的爆炸性数据量的日益增长趋势。 EON 的系统旨在实现每链路 2.4 Tbps 的速率，这将是太空激光通信的纪录。该公司计划部署一个配备激光终端的卫星星座，在地面站之间传输数据，从而有效构建一个天基互联网骨干网。

rss · TechCrunch AI · 8月4日 12:00

**背景**: 传统卫星通信依赖射频（RF）链路，带宽有限且可能拥堵。激光通信，即自由空间光通信，利用红外光传输数据，提供更高带宽和更窄波束，从而减少干扰并提高安全性。NASA 等机构多年来一直在开发激光通信技术，但商业应用仍处于早期阶段。EON 的方法旨在利用该技术在太空构建高速数据高速公路，可能补充甚至替代部分海底光缆路线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Laser_communication_in_space">Laser communication in space - Wikipedia</a></li>
<li><a href="https://www.nasa.gov/communicating-with-missions/lasercomms/">Laser Communications - NASA</a></li>
<li><a href="https://thesheffieldpress.com/endeavour-optical-networks-plans-fastest-space-laser">Endeavour Optical Networks plans fastest space laser ...</a></li>

</ul>
</details>

**标签**: `#space lasers`, `#optical networks`, `#communications`, `#satellite`

---

<a id="item-28"></a>
## [AWS 将 vibe-coding 工具 Superblocks 集成到私有云中](https://techcrunch.com/2026/08/03/aws-is-helping-vibe-coding-startup-superblocks-and-the-implications-are-big/) ⭐️ 6.0/10

AWS 现在允许 vibe-coding 初创公司 Superblocks 嵌入到 AWS 客户的私有云中，这标志着向应用与 AI 模型解耦迈出了一步。 这一整合标志着 AI 辅助开发工具在企业云环境中提供的趋势日益增长，可能降低非程序员构建应用的门槛。它也突显了 vibe-coding 在云行业中的战略重要性。 此举允许 Superblocks 在 AWS 的私有云基础设施内运行，确保企业客户的数据隐私和合规性。这是行业更广泛趋势的一部分，即应用逻辑与底层 AI 模型解耦，使应用更加灵活和可移植。

rss · TechCrunch AI · 8月3日 20:00

**背景**: Vibe coding 是一种 AI 辅助的软件开发方法，开发者用自然语言提示描述任务，大语言模型生成代码。该术语由 Andrej Karpathy 于 2025 年提出，并因使业余程序员也能创建软件而流行，但批评者担心代码质量和安全性。应用-模型解耦是指将应用逻辑与其使用的 AI 模型分离，使应用可以切换模型或在不同的环境中运行而无需重大重写。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://grokipedia.com/page/Vibe_coding">Vibe coding</a></li>

</ul>
</details>

**标签**: `#AWS`, `#vibe-coding`, `#cloud`, `#AI`, `#startup`

---

<a id="item-29"></a>
## [Moonshot PerceptionBench：多模态视觉模型新基准](https://news.google.com/rss/articles/CBMi6gFBVV95cUxPLVlTQVpNcjFDazVnT2RIclJfbDBucUpYd2tRNnNFMjFjRFBDUHpBNVVHOVA0Q3FfUVpOaGlzTzB5azE1S3p6V0RWOGdWSFpxNll1aWNfMUVrZ2FRdzc5S3BJN3lRTkNZdG5rOGUtdU1ISDNqZm5YWWRKV1h6aUtJX3BnWFRqS1RGS2U5d0U2UF9Gek9vRlhkczF0S0tHX2ZxQVZjVk90d0FQN2FvSkVXUHhPTThsZ0lGUXlSMDd5TGkwLW5IbWxYTjFKWmIxWk5vTVROdmk0TFN0MTNhUTJWSVh0SEZ4ZXJhd1HSAe8BQVVfeXFMTk85MDNQZUxVRVZuX0VNcG5qWnhWMlhrZlFBekgzZ1NaVkxQaGpXcWtLTmE3S2hFMnd6NEtDWTBORWROekpnbllaTy1RSDR5V2xtLVZCX0hkQWlTYzRQVFBDenRmTndXSEVaR2lDb3RZcnFMa09NMHJaMTIwZFRnbWk4QVdRd0dCNzg5cm9hQS1lbHVEcjVJeHU2RmxEREJZYWJBTEpmZEt4YlkwajA0STJYNXFISEd1eUJtUE1zTTdIdHVvdnkwWUo3SnRTVUtMUmRfZkRhbnVseEpYVmhZNE1DaVR2Ujg4aVgxWHM0OXM?oc=5) ⭐️ 6.0/10

Moonshot AI 推出了 PerceptionBench，这是一个专门用于评估多模态大语言模型（MLLM）原子视觉感知能力的基准。MarkTechPost 的文章描述了一个统一的评估框架，支持稳健的数据加载和自动评判，包括盲先验基线、兼容 OpenAI 的 API 以及本地 Hugging Face 模型。 PerceptionBench 通过将感知与推理分离，解决了 MLLM 评估中的一个关键缺口，这对于提高模型的可靠性和可解释性至关重要。该基准可能会影响多模态模型的开发和评估方式，使计算机视觉和人工智能领域的研究人员和从业者受益。 该基准专注于原子视觉感知任务，评估框架支持基于 API 和本地模型，并通过自动评判减少人为偏差。PerceptionBench 已在 BenchLM 和 llm-stats 等平台上被跟踪，分数以 0–1 的尺度报告。

google_news · MarkTechPost · 8月3日 22:26

**背景**: 多模态大语言模型（MLLM）结合了视觉和语言能力，但现有的基准常常将感知错误与推理失败混为一谈，使得难以定位模型的弱点。PerceptionBench 旨在隔离原子感知技能，如物体识别和空间理解，以提供更清晰的诊断。稳健的数据加载和自动评判是确保跨不同模型进行一致且可扩展评估的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MoonshotAI/PerceptionBench">GitHub - MoonshotAI/PerceptionBench: PerceptionBench ...</a></li>
<li><a href="https://benchlm.ai/benchmarks/perceptionbench">PerceptionBench Leaderboard & Scores — August 2026 | BenchLM.ai</a></li>
<li><a href="https://www.marktechpost.com/2026/08/03/evaluating-multimodal-vision-models-with-moonshot-perceptionbench-using-robust-data-loading-and-automated-judging/">Evaluating Multimodal Vision Models with Moonshot ...</a></li>

</ul>
</details>

**标签**: `#multimodal vision`, `#benchmark`, `#image quality assessment`, `#AI evaluation`

---

<a id="item-30"></a>
## [AI 转型引发菲律宾外包行业工人焦虑](https://www.bbc.co.uk/news/articles/cgr7nxve05go?at_medium=RSS&at_campaign=rss) ⭐️ 5.0/10

BBC 的一篇文章指出，人工智能正在重塑菲律宾的外包行业，引发工人对失业的焦虑。报道中的工人表示，他们感觉像是“自掘坟墓”，因为自动化威胁到他们的岗位。 这很重要，因为菲律宾是全球业务流程外包（BPO）的领导者，雇佣了超过一百万人。AI 转型可能对经济和社会产生重大影响，不仅影响工人，还影响国家经济和全球外包格局。 文章聚焦于 AI 转型中的人性层面，讲述了工人的个人故事和焦虑。它强调了行业增长与就业安全之间的紧张关系，因为 AI 工具越来越有能力处理传统上由人类完成的任务。

rss · BBC World News · 8月4日 22:10

**背景**: 菲律宾的 BPO 行业一直是主要的经济驱动力，雇佣了超过一百万人，服务全球客户。AI 和自动化正在改变这一行业，创造新岗位的同时也威胁现有岗位。报告显示，该行业正在转型，AI 带来了成本节约和效率提升，但也引发了对失业的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bpoai.ai/news/the-philippine-bpo-industry-in-2026-sizing-the-ai-transition">The Philippine BPO Industry in 2026: Sizing the AI Transition</a></li>
<li><a href="https://vamasters.com/philippines-outsourcing-industry-report-2026/">Philippines Outsourcing Report 2026: $40B Market Data ...</a></li>
<li><a href="https://www.365outsource.com/public/ai-philippine-outsourcing-trends/">AI in Philippine Outsourcing: Trends 2025 - 365Outsource.com</a></li>

</ul>
</details>

**标签**: `#AI`, `#outsourcing`, `#Philippines`, `#labor`

---

<a id="item-31"></a>
## [特朗普的 AI 保护主义延伸至机器人领域](https://news.google.com/rss/articles/CBMinwFBVV95cUxPRXNQZFQyQTVMbEk4UXZRYWwwb3RaVHcyMlU5QmozdldfRVdrcVlGc1VYbDNyeXl2OGh0clJoRk1BN0VuQkxDUjU4WHdZQS1ERW5BTDdmOGtuZVpVOW0xbHM4QWRQVU01QWhpZzdFbkJtVG1HNEpuQTd2VUlJNFF6dWo3SjZ5VWcyMldDQlJvM0V5Q2pOYnBra245ZXlDNmfSAaQBQVVfeXFMTTR4N0dnSVBGNWl4NnVPWl9WQUlYLTExRXJvdXE3cHFJSThyak5tTXhHa0ZhaDBPdXhHYXJVbWRXa2xzVlo3bzN0QW1vTkJKbmQ3dFNjbGRmNkM2UWRqenVhTWFhSlcxaWczWkg2bW53Z2FKQ25yQVJPcmlsSFUzRnJzcVFqZnhDbWozOGdzUzhzZGdJRUhlS190VklEdER1WXJ2VXE?oc=5) ⭐️ 5.0/10

《麻省理工科技评论》报道，特朗普政府的 AI 保护主义政策现已针对机器人产业，可能限制外国竞争和技术转让。 此举可能重塑全球机器人供应链和创新格局，影响世界各地的企业和研究人员。这标志着技术民族主义的更广泛趋势，可能阻碍国际合作，减缓机器人和 AI 的进步。 文章强调了关税和机器人技术出口管制等具体措施，这些措施可能增加国内制造商的成本，并限制先进零部件的获取。这些政策还可能引发其他国家的报复行动，加剧贸易紧张局势。

google_news · MIT Technology Review · 8月3日 18:43

**背景**: AI 保护主义是指政府限制 AI 技术、数据和人才跨境流动以保护国内产业的政策。历史上，保护主义常用于制造业，但将其应用于 AI 和机器人等新兴技术相对较新。机器人产业高度依赖全球供应链和国际研究合作，因此特别容易受到此类政策的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/ai-protectionism-digital-tariffs-our-time-jason-davis-ys0de">AI Protectionism : The Digital Tariffs of Our Time</a></li>
<li><a href="https://techcrunch.com/2019/01/26/how-have-tariffs-impacted-robotics/">How have tariffs impacted robotics ? | TechCrunch</a></li>
<li><a href="https://cepr.net/publications/the-high-cost-of-protectionism-ai-edition/">The High Cost of Protectionism : AI Edition – CEPR</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#robotics`, `#protectionism`, `#technology regulation`

---

<a id="item-32"></a>
## [3D 视觉先驱 Marc Pollefeys 加入保加利亚 INSAIT](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQYlVIaGNCOWhid2N3TzdwUGt5Q1hKejNWVi0zWGhidXFXWE0xZmtNUnYwaFRIcU9wSTd4aUdfLTVZeHhSaWUxZ2VYQ0RLR0l2UU5EU0l4S1VTVzhlZGRHWXBpYW82U0Z6RnRzYzl6WS1yd1hxLW84RHV0LVFNMVZMcHAwbXpxUWhINlVZ?oc=5) ⭐️ 5.0/10

3D 计算机视觉和机器人领域的知名先驱 Marc Pollefeys 已加入位于保加利亚索非亚的研究机构 INSAIT。这一消息由保加利亚媒体 bnrnews.bg 和 bta.bg 报道。 此举增强了 INSAIT 作为 AI 和计算机视觉领域世界级研究中心的地位，可能吸引更多国际人才和合作。同时也凸显了保加利亚在全球科技领域日益增长的雄心。 Marc Pollefeys 是苏黎世联邦理工学院的教授，以开发首个将照片自动转换为 3D 模型的软件流程而闻名。INSAIT 专注于科学卓越、吸引国际研究人员以及培养研究生和本科生。

google_news · bnrnews.bg · 8月3日 15:48

**背景**: INSAIT（计算机科学、人工智能与技术研究所）是位于保加利亚索非亚的研究机构，其使命是开展世界级研究并吸引国际科学家。Marc Pollefeys 的研究涵盖 3D 计算机视觉、机器人、图形学和机器学习，他的加入对研究所意义重大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Institute_for_Computer_Science,_Artificial_Intelligence_and_Technology">Institute for Computer Science, Artificial Intelligence and... - Wikipedia</a></li>
<li><a href="https://insait.ai/">INSAIT | Institute for Computer Science, Artificial Intelligence and...</a></li>
<li><a href="https://people.inf.ethz.ch/pomarc/publications.html">Marc Pollefeys ' publications</a></li>

</ul>
</details>

**标签**: `#3D computer vision`, `#INSAIT`, `#research news`

---