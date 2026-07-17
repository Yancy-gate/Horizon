---
layout: default
title: "Horizon Summary: 2026-07-18 (EN)"
date: 2026-07-18
lang: en
---

> From 146 items, 23 important content pieces were selected

---

1. [Firefox compiled to WebAssembly runs inside a browser](#item-1) ⭐️ 9.0/10
2. [Ultralytics v8.4.97 Adds Direct Hailo HEF Export](#item-2) ⭐️ 8.0/10
3. [First Atmosphere Found on Rocky Exoplanet in Habitable Zone](#item-3) ⭐️ 8.0/10
4. [Kimi K3 and Pelican Benchmark: Hidden Prompts and Evaluation Limits](#item-4) ⭐️ 8.0/10
5. [MoSense Raises Millions for Full-Body Robot Tactile Skin](#item-5) ⭐️ 8.0/10
6. [Ex-NIO, Huawei AI Leads Raise Millions for Embodied World Model](#item-6) ⭐️ 8.0/10
7. [MIT Study Revises 20th Century US GDP Growth](#item-7) ⭐️ 8.0/10
8. [Mars Rover Instruments Can Detect Biosignatures Without Sample Return](#item-8) ⭐️ 8.0/10
9. [Xi to Unveil Global AI Vision as Huawei Debuts Nvidia Rival](#item-9) ⭐️ 8.0/10
10. [NVIDIA NeMo Automodel & Hugging Face Diffusers for Scalable Fine-Tuning](#item-10) ⭐️ 7.0/10
11. [Patreon shifts from robots.txt to active AI bot blocking](#item-11) ⭐️ 7.0/10
12. [GPU Financiers Shift to Inference Chips in $400M Deal](#item-12) ⭐️ 7.0/10
13. [Alibaba 1688 Unveils UTP Protocol for AI-to-AI B2B Trade](#item-13) ⭐️ 7.0/10
14. [Mitochondrial Theory of Mind Proposed](#item-14) ⭐️ 7.0/10
15. [The Future Belongs to AI Maniacs](#item-15) ⭐️ 7.0/10
16. [Ukrainian cruise missile uses hobby drone hardware](#item-16) ⭐️ 7.0/10
17. [Kimi K3: 2.8T-Parameter Open-Source AI Model Released](#item-17) ⭐️ 7.0/10
18. [SenseTime Open-Sources Unified Vision Model, Ending Stitch-Monster Era](#item-18) ⭐️ 7.0/10
19. [Ant Group Open-Sources SingGuard-NSFA for AI Agent Security](#item-19) ⭐️ 7.0/10
20. [Book Review: A Phone is a Cow](#item-20) ⭐️ 6.0/10
21. [NVIDIA Releases New AI Model for Robots](#item-21) ⭐️ 6.0/10
22. [No single AI model dominates vulnerability detection](#item-22) ⭐️ 6.0/10
23. [Deloitte Uses Claude AI to Speed Open Source Patching](#item-23) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Firefox compiled to WebAssembly runs inside a browser](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter compiled the full Firefox browser to WebAssembly, enabling it to run inside another browser like Chrome. The demo loads a 233MB gecko.wasm binary and uses the Wisp protocol for network proxying. This is a groundbreaking technical achievement that demonstrates the feasibility of running a full browser inside another browser, opening possibilities for cross-platform execution and isolation. It also showcases the power of AI-assisted programming, as the project used an estimated $25,000 worth of Claude Opus and Fable tokens. The project chose Firefox/Gecko because of its strong single-process support. All network traffic is proxied through Puter's server via the Wisp protocol over WebSocket, and the team had to scale up servers to handle Hacker News traffic.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (WASM) is a low-level binary instruction format that runs in modern web browsers at near-native speed. Compiling a full browser like Firefox to WASM is extremely challenging due to the complexity of browser engines, but Firefox's single-process mode simplifies the task. The Wisp protocol is a low-overhead protocol for proxying multiple TCP/UDP sockets over a single WebSocket connection.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/ wisp - protocol : Wisp is a low-overhead...</a></li>
<li><a href="https://claude.com/pricing">Plans & Pricing | Claude by Anthropic</a></li>
<li><a href="https://support.claude.com/en/articles/11049741-what-is-the-max-plan">What is the Max plan ? | Claude Help Center</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion expressed excitement and amazement at the demo, with many praising the engineering effort. Some raised concerns about the cost of proxying all traffic through Puter's servers, and the team confirmed they had to scale up infrastructure to handle the load.

**Tags**: `#WebAssembly`, `#Firefox`, `#browser engineering`, `#cross-platform`, `#demo`

---

<a id="item-2"></a>
## [Ultralytics v8.4.97 Adds Direct Hailo HEF Export](https://github.com/ultralytics/ultralytics/releases/tag/v8.4.97) ⭐️ 8.0/10

Ultralytics 8.4.97 introduces direct Hailo HEF export for YOLOv8, YOLO11, and YOLO26 detection models, allowing users to compile models for Hailo edge accelerators with a single command. This simplifies edge AI deployment by replacing a lengthy manual ONNX-to-DFC workflow with a streamlined export process, making it easier for practitioners to deploy YOLO models on Hailo hardware. The export supports Hailo-8, Hailo-8L, Hailo-10H, Hailo-15H, and Hailo-15L accelerators, uses INT8 quantization, and recommends at least 1,024 representative calibration images for production accuracy.

github · github-actions[bot] · Jul 17, 01:18

**Background**: Hailo HEF (Hailo Executable Format) is a binary file format for deploying neural networks on Hailo edge AI accelerators. Previously, converting YOLO models to HEF required a multi-step manual process using ONNX and Hailo's Dataflow Compiler. This update integrates that workflow directly into Ultralytics, reducing complexity.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.ultralytics.com/integrations/hailo">Hailo Export for Ultralytics YOLO Models</a></li>
<li><a href="https://github.com/hailo-ai/hailo_model_zoo">GitHub - hailo-ai/hailo_model_zoo: The Hailo Model Zoo ... Hailo Platform | luxonis/modelconverter | DeepWiki Guide step-by-step how to compile custom models to HEF ultralytics/docs/en/integrations/hailo.md at main ... - GitHub Creating Custom Hef using DFC/Model Zoo - Guides - Hailo ...</a></li>
<li><a href="https://hailo.ai/">Hailo AI on the Edge Processors | Edge AI Chip Solutions</a></li>

</ul>
</details>

**Tags**: `#YOLO`, `#edge AI`, `#Hailo`, `#model export`, `#Ultralytics`

---

<a id="item-3"></a>
## [First Atmosphere Found on Rocky Exoplanet in Habitable Zone](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

JWST has confirmed an atmosphere on the rocky exoplanet LHS 1140b, located 48 light-years away in its star's habitable zone, ruling out the possibility that it is a mini-Neptune. This is the first detection of an atmosphere on a rocky planet in the habitable zone, challenging assumptions that red dwarf planets cannot retain atmospheres due to stellar stripping. LHS 1140b is a super-Earth with 5.6 Earth masses, orbiting an M-type red dwarf every 24.7 days. The atmosphere contains helium, suggesting a high escape velocity.

hackernews · neversaydie · Jul 17, 14:06 · [Discussion](https://news.ycombinator.com/item?id=48947560)

**Background**: Red dwarfs are cooler and more active than the Sun, making their habitable zones much closer. Planets there face intense stellar radiation that can strip away atmospheres. LHS 1140b was discovered in 2017, and JWST's emission spectroscopy now confirms it has an atmosphere, making it a prime candidate for studying habitability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LHS_1140_b">LHS 1140 b - Wikipedia</a></li>
<li><a href="https://science.nasa.gov/exoplanet-catalog/lhs-1140-b/">LHS 1140 b - NASA Science</a></li>
<li><a href="https://www.theguardian.com/science/2026/jul/16/atmosphere-lhs-1140b-exoplanet-could-water-scientists">Earth-like exoplanet found to have an atmosphere | Space | The Guardian</a></li>

</ul>
</details>

**Discussion**: Commenters noted that red dwarf planets typically struggle to retain atmospheres, but JWST data rules out a mini-Neptune. Some discussed propulsion methods to reach the planet within centuries, while others highlighted that helium detection implies high escape velocity, making it hard for life to leave.

**Tags**: `#exoplanets`, `#JWST`, `#astronomy`, `#atmosphere`, `#habitable zone`

---

<a id="item-4"></a>
## [Kimi K3 and Pelican Benchmark: Hidden Prompts and Evaluation Limits](https://simonwillison.net/2026/Jul/16/kimi-k3/) ⭐️ 8.0/10

Simon Willison's analysis of Kimi K3 reveals that the Pelican benchmark, which asks models to generate an SVG of a pelican riding a bicycle, has significant limitations, including potential training data contamination and the discovery of an 85-token hidden system prompt in Kimi K3. This matters because it highlights flaws in popular LLM benchmarks and raises concerns about data contamination, while also exposing hidden system prompts that affect model behavior and evaluation fairness. Kimi K3 is a 2.8 trillion parameter open model, and the Pelican benchmark's simplicity (a single prompt) makes it susceptible to memorization; the hidden prompt likely controls reasoning effort. The community also noted that Kimi K3 is the cheapest but slowest among recent models.

hackernews · droidjj · Jul 17, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48947717)

**Background**: The Pelican benchmark, created by Simon Willison in late 2024, is an informal test that asks LLMs to generate an SVG of a pelican riding a bicycle. It gained popularity as a quick way to compare model capabilities. System prompt extraction is a technique to reveal hidden instructions that shape model behavior, often used for security analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark)</a></li>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/system_prompts_leaks: Extracted system ...</a></li>

</ul>
</details>

**Discussion**: Community comments debated whether pelican images are in training data, with one user noting that their company blog content appears in LLMs within six months. Another commenter calculated token counts to infer hidden prompts, and a user created a cost-speed comparison showing Kimi K3 is cheapest but slowest.

**Tags**: `#AI`, `#LLM`, `#benchmarking`, `#Kimi K3`, `#system prompt`

---

<a id="item-5"></a>
## [MoSense Raises Millions for Full-Body Robot Tactile Skin](https://36kr.com/p/3899128277452681?f=rss) ⭐️ 8.0/10

MoSense, a startup founded by HKUST PhDs, has raised tens of millions of yuan in angel funding from Sequoia China, Hillhouse, and Zhiyuan Robot to develop MoSkin, a full-body multimodal tactile sensing system for robots based on electromagnetic metamaterial technology. This funding highlights the growing importance of full-body tactile sensing in humanoid robotics, addressing a critical bottleneck for real-world deployment. MoSense's technology could enable robots to perform complex tasks requiring physical interaction, such as logistics and elderly care, by providing comprehensive touch feedback. MoSkin covers the robot's hands, limbs, torso, and soles, converting the rigid physical boundary into a continuous six-dimensional force field perception. The company is also developing a world-action-tactile prediction model using a multimodal latent space fusion gating mechanism to bridge the sim-to-real gap.

rss · 36氪 · Jul 17, 02:39

**Background**: Most current tactile solutions for robots are limited to fingertips or grippers, lacking full-body feedback. Electromagnetic metamaterials are engineered structures that can manipulate electromagnetic waves, enabling novel sensing capabilities. The sim-to-real gap refers to the difficulty of transferring policies trained in simulation to real robots due to differences in physics and perception.

<details><summary>References</summary>
<ul>
<li><a href="https://36kr.com/p/3899128277452681">36...</a></li>
<li><a href="https://news.pedaily.cn/202607/566450.shtml">news.pedaily.cn/202607/566450.shtml</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#tactile sensing`, `#humanoid robot`, `#funding`, `#AI`

---

<a id="item-6"></a>
## [Ex-NIO, Huawei AI Leads Raise Millions for Embodied World Model](https://36kr.com/p/3899081603483525?f=rss) ⭐️ 8.0/10

Rikor Robotics, founded by former NIO and Huawei autonomous driving core members, completed two seed funding rounds totaling hundreds of millions of RMB for its embodied world model LaMPA. The company aims to build a foundation model that understands physics, predicts changes, and drives robots to perform tasks across diverse scenarios. This funding signals strong investor confidence in world models for embodied intelligence, a critical step toward general-purpose robots that can adapt to complex, unstructured environments. The team's pedigree from leading autonomous driving companies suggests potential breakthroughs in bridging simulation and real-world deployment. LaMPA introduces a triple representation system (environment, ego, experience) and a block diffusion architecture, along with a world reward model to accelerate reinforcement learning. The company has partnered with Yuantu Future to enter high-precision server manufacturing assembly scenarios.

rss · 36氪 · Jul 17, 01:52

**Background**: Embodied intelligence aims to give robots the ability to perceive, reason, and act in the physical world. World models are a key approach, enabling robots to simulate future states and plan actions. Yann LeCun's JEPA theory provides a theoretical foundation for learning abstract representations of the world, but practical implementations require solving how to represent the physical world and learn causal relationships efficiently.

**Tags**: `#embodied intelligence`, `#world model`, `#robotics`, `#autonomous driving`, `#funding`

---

<a id="item-7"></a>
## [MIT Study Revises 20th Century US GDP Growth](https://marginalrevolution.com/marginalrevolution/2026/07/cataloging-growth-a-re-evaluation-of-1900-1990.html?utm_source=rss&utm_medium=rss&utm_campaign=cataloging-growth-a-re-evaluation-of-1900-1990) ⭐️ 8.0/10

MIT researchers Verónica Bäcker-Peral and Benjamin Wittenbrink used 5.1 million product listings to construct a quality-adjusted price index for U.S. consumer goods from 1900 to 1990. This new index could significantly revise historical real GDP growth estimates, as it systematically accounts for quality changes that official price indexes largely ignore for most of the 20th century. The dataset includes 5.1 million product listings, enabling hedonic quality adjustment methods to separate price changes from quality improvements, which is crucial for accurate real GDP measurement.

rss · Marginal Revolution · Jul 17, 15:33

**Background**: Real GDP growth measures the value of goods and services produced, adjusted for inflation. However, traditional price indexes like the CPI often fail to fully account for quality improvements, such as faster computers or more durable clothing, leading to potential overestimation of inflation and underestimation of real growth. Hedonic quality adjustment is a statistical technique that estimates the value of specific product features to isolate pure price changes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bls.gov/cpi/quality-adjustment/">Quality Adjustment in the CPI - U.S. Bureau of Labor Statistics</a></li>
<li><a href="https://www.bls.gov/cpi/quality-adjustment/questions-and-answers.htm">Frequently Asked Questions about Hedonic Quality Adjustment ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S030440762500106X">Hedonic prices and quality adjusted price indices powered by ...</a></li>

</ul>
</details>

**Tags**: `#economics`, `#price index`, `#GDP measurement`, `#quality adjustment`, `#data science`

---

<a id="item-8"></a>
## [Mars Rover Instruments Can Detect Biosignatures Without Sample Return](https://news.google.com/rss/articles/CBMi9AFBVV95cUxQRWNCdXI1QTlsSUh2X3p4YVdhWTJYV01aTGpLOVRUTzNwVGpZaFlfaDBwREZtcHRQMnBrZjMwa28zWFYtWU1YWDItOVRGc3hwc0lZQ1hwcVRyVjBUOVhQUi1LZVM0STdIME9uZzRDajhPb2p2aWZuNmlFUGJmMVZzZ3MxVFd3NWdDNnhBSlVBanNKNzlZZnA0ZFpYNURySVVkUEdLSDhCQ1RhUHRhUXQtV3VsQVgxaElNbmFsVllSalZPUTZWbmVUcTFzZEtnS2tVN0V6RmhpZlpLdjcxTnhMcGJvU2NpeUdoOVdFM25rREVfS3Bk?oc=5) ⭐️ 8.0/10

Scientists have demonstrated that existing instruments on the Mars rover can detect extraterrestrial biosignatures, potentially eliminating the need for sample-return missions. This breakthrough could accelerate the search for life on Mars by using current rover capabilities, saving time and cost compared to sample-return missions. The method uses spectroscopy and in-situ analysis to identify biosignatures like organic molecules or isotopic anomalies, leveraging instruments such as SHERLOC and PIXL on the Perseverance rover.

google_news · The Debrief · Jul 17, 12:49

**Background**: A biosignature is any substance or phenomenon that provides scientific evidence of past or present life. Traditionally, definitive detection required returning samples to Earth. This new approach shows that rovers can perform such analyses on-site.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Biosignature">Biosignature - Wikipedia</a></li>
<li><a href="https://www.nasa.gov/news-release/nasa-says-mars-rover-discovered-potential-biosignature-last-year/">NASA Says Mars Rover Discovered Potential Biosignature ... - NASA</a></li>

</ul>
</details>

**Tags**: `#Mars`, `#biosignatures`, `#space exploration`, `#astrobiology`, `#NASA`

---

<a id="item-9"></a>
## [Xi to Unveil Global AI Vision as Huawei Debuts Nvidia Rival](https://news.google.com/rss/articles/CBMitwFBVV95cUxOVlJMUmJnREpFMGdvd21veTNUdkwtUEhhVE5YOV81Z2dINXl1VG1CbWc4VFE0NGNudUY1QXdtcFNBMkJIOWVhRjRxTnh5bDcyNjR6WmhNOHlmSzlYN000TDdQYWRCb01LcWNOa2o5b3ZpNllNZ0tLbldPcFIwRmZkRFBuQTRUWUVaazJUU0RsWERjSHQxLWdmUEc2NGw5emtDU0RXa0QxSDRrWllEbHdwYjZrSzU2X0k?oc=5) ⭐️ 8.0/10

Chinese President Xi Jinping is set to announce a global AI strategy at a Shanghai summit, while Huawei unveils the Ascend 950PR chip, a competitor to Nvidia's offerings. This marks a significant geopolitical move as China challenges US dominance in AI and semiconductor technology, potentially reshaping global AI governance and supply chains. Huawei's Ascend 950PR delivers 1.56 petaflops of AI inference performance, 2.8 times the FP4 performance of Nvidia's H20, with 750,000 units planned for 2026 and a $5.6 billion order from ByteDance.

google_news · Tekedia · Jul 17, 07:26

**Background**: The US has imposed export controls on advanced AI chips to China, prompting Chinese firms to develop domestic alternatives. Huawei's Ascend series is a key part of China's push for semiconductor self-sufficiency. Xi's vision emphasizes an open-source, people-centered global AI order, contrasting with US-led frameworks.

<details><summary>References</summary>
<ul>
<li><a href="https://tech-insider.org/huawei-ascend-950pr-ai-chip-nvidia-china-2026/">Huawei Ascend 950PR: The 1.56 PFLOP AI Chip vs Nvidia [2026]</a></li>
<li><a href="https://www.bitrue.com/blog/huawei-vs-nvidia-ascend-chip-performance-2025">Huawei Ascend Chips vs NVIDIA: A 2025 AI Performance Comparison</a></li>
<li><a href="https://abhs.in/blog/huawei-ascend-910c-china-nvidia-alternative-2026">Huawei Ascend 910C: China Plans 600,000 AI Chips in 2026</a></li>

</ul>
</details>

**Tags**: `#AI`, `#China`, `#Huawei`, `#Nvidia`, `#Geopolitics`

---

<a id="item-10"></a>
## [NVIDIA NeMo Automodel & Hugging Face Diffusers for Scalable Fine-Tuning](https://huggingface.co/blog/nvidia/scale-diffusers-finetuning-nemo-automodel) ⭐️ 7.0/10

NVIDIA and Hugging Face have announced a new integration that enables fine-tuning of video and image diffusion models at scale using NeMo Automodel and the Diffusers library. This allows practitioners to leverage NeMo's distributed training capabilities directly with Hugging Face's model ecosystem. This integration significantly lowers the barrier for scaling fine-tuning of diffusion models, which are computationally intensive. It enables AI/ML practitioners to train larger models or handle more data without writing custom distributed training code, accelerating research and production deployment. NeMo Automodel is a PyTorch DTensor-native SPMD training library that supports LLMs, VLMs, diffusion models, and retrieval models. The integration works by loading any Hugging Face model directly into NeMo Automodel, eliminating the need for checkpoint conversion or boilerplate code.

rss · Hugging Face Blog · Jul 17, 15:57

**Background**: Diffusion models are a class of generative models that create images or videos by gradually denoising random noise. Fine-tuning these models for specific tasks or datasets typically requires significant computational resources and expertise in distributed training. NeMo Automodel simplifies this by providing a distributed training framework that automatically handles parallelism and optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.nvidia.com/nemo/automodel/">NeMo AutoModel Documentation | NVIDIA NeMo AutoModel</a></li>
<li><a href="https://github.com/NVIDIA-NeMo/Automodel">GitHub - NVIDIA-NeMo/Automodel: Pytorch Distributed native ...</a></li>
<li><a href="https://huggingface.co/docs/diffusers/index">Diffusers · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#fine-tuning`, `#NVIDIA NeMo`, `#Diffusers`, `#AI/ML`, `#scalability`

---

<a id="item-11"></a>
## [Patreon shifts from robots.txt to active AI bot blocking](https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/) ⭐️ 7.0/10

Patreon announced it is partnering with Cloudflare to actively block AI scraping bots that train on creators' content without permission, moving away from relying solely on robots.txt. This shift represents a significant industry move from passive to active defense against unauthorized AI training, protecting creator revenue and content rights in the growing AI economy. Patreon is using Cloudflare's bot management solutions, which can block bots classified as 'Training' or 'Agent' on pages displaying ads, with new defaults set for September 2026.

rss · TechCrunch AI · Jul 17, 15:21

**Background**: Robots.txt is a standard that relies on voluntary compliance by web crawlers, but malicious bots often ignore it. Cloudflare provides active bot detection and blocking capabilities, offering a more robust defense against unauthorized scraping.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Robots.txt">Robots.txt</a></li>
<li><a href="https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/">Block AI Bots · Cloudflare bot solutions docs</a></li>

</ul>
</details>

**Tags**: `#AI scraping`, `#content protection`, `#Patreon`, `#Cloudflare`, `#creator economy`

---

<a id="item-12"></a>
## [GPU Financiers Shift to Inference Chips in $400M Deal](https://techcrunch.com/2026/07/17/why-the-first-gpu-financiers-are-turning-to-inference-chips-in-a-400-million-deal/) ⭐️ 7.0/10

General Compute secured a $400 million chip-backed loan from Upper90, marking the first major financing deal specifically for AI inference hardware rather than training GPUs. This signals a shift in AI infrastructure financing from training-focused GPUs to inference-optimized chips, reflecting the industry's move toward deploying AI models at scale. It could unlock new capital for inference startups and reshape the hardware investment landscape. The loan is backed by the chips themselves, similar to earlier GPU-backed loans from CoreWeave, but this time focused on inference hardware. General Compute is a relatively new player in the inference chip space.

rss · TechCrunch AI · Jul 17, 12:00

**Background**: AI inference is the process of running a trained AI model to make predictions, as opposed to training which requires massive compute. Inference chips are specialized hardware designed to be more power-efficient and cost-effective for this task than general-purpose GPUs. The first GPU financiers, like CoreWeave, pioneered chip-backed loans using GPUs as collateral, but this deal marks the first such loan for inference chips.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/17/why-the-first-gpu-financiers-are-turning-to-inference-chips-in-a-400-million-deal/">Why the first GPU financiers are turning to inference chips ...</a></li>
<li><a href="https://creati.ai/ai-news/2026-07-17/general-computes-400m-chip-backed-loan-signals-a-new-financing-market-for-ai-inference-hardware/">General Compute’s $400M chip-backed loan signals a new ...</a></li>
<li><a href="https://www.naddod.com/ai-insights/inference-chip-guide-the-foundation-of-scalable-ai-applications">Inference Chip Guide: The Foundation of Scalable AI ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#inference chips`, `#GPU financing`, `#venture capital`, `#hardware`

---

<a id="item-13"></a>
## [Alibaba 1688 Unveils UTP Protocol for AI-to-AI B2B Trade](https://36kr.com/p/3896564485572489?f=rss) ⭐️ 7.0/10

Alibaba 1688 announced it will launch the Universal Trade Protocol (UTP) at the end of July 2026, a standard for AI-to-AI B2B transactions, enabling buyer AI agents to directly connect with factory AI agents to complete trades automatically. UTP aims to become the foundational infrastructure for A2A (Agent-to-Agent) global trade, potentially standardizing inter-agent commerce and accelerating the shift from human-driven B2B to fully automated AI-driven transactions. The protocol is designed to address the lack of a universal communication standard among different AI agents in B2B scenarios. UTP will be an open standard, allowing interoperability across various platforms and AI frameworks.

rss · 36氪 · Jul 17, 13:01

**Background**: B2B e-commerce traditionally involves human buyers and sellers negotiating and transacting. With the rise of AI agents capable of autonomously making purchasing decisions, a new paradigm called A2A (Agent-to-Agent) is emerging, where AI agents represent buyers and sellers. However, these agents often use proprietary protocols, hindering cross-platform trade. UTP is an open standard that enables different AI agents to communicate and transact seamlessly, similar to how HTTP standardizes web communication.

<details><summary>References</summary>
<ul>
<li><a href="https://a2a-protocol.org/latest/">A 2 A Protocol</a></li>

</ul>
</details>

**Tags**: `#AI`, `#B2B`, `#protocol`, `#e-commerce`, `#Alibaba`

---

<a id="item-14"></a>
## [Mitochondrial Theory of Mind Proposed](https://www.quantamagazine.org/martin-picards-mitochondrial-theory-of-mind-20260717/) ⭐️ 7.0/10

Biologist Martin Picard has proposed a 'mitochondrial theory of mind' that positions mitochondria as the fundamental link between cellular energy, health, and conscious experience. This theory challenges traditional views of consciousness by grounding it in cellular energetics, potentially opening new avenues for understanding mental health and treating neurological disorders. Picard, director of the Mitochondrial Psychobiology Lab at Columbia University, coined the term 'mitochondrial psychobiology' to study how psychological states influence mitochondrial function and vice versa.

rss · Quanta Magazine · Jul 17, 14:31

**Background**: Mitochondria are organelles that produce most of the cell's energy in the form of ATP. Picard's 'energetic view of life' suggests that mitochondrial dynamics—their shape, movement, and energy output—directly shape our thoughts, emotions, and sense of self.

<details><summary>References</summary>
<ul>
<li><a href="https://www.quantamagazine.org/martin-picards-mitochondrial-theory-of-mind-20260717/">Martin Picard’s Mitochondrial Theory of Mind - Quanta Magazine</a></li>
<li><a href="https://www.neurology.columbia.edu/news/martin-picard-exploring-mind-mitochondria-connection">Martin Picard: Exploring the Mind-Mitochondria Connection</a></li>
<li><a href="https://www.metabolicmind.org/resources/news-views/podcasts/metabolic-mind-podcast/how-mitochondria-shape-your-mind-mood-mental-health-with-dr-martin-picard/">How Mitochondria Shape Your Mind, Mood, & Mental Health with ...</a></li>

</ul>
</details>

**Tags**: `#mitochondria`, `#consciousness`, `#biology`, `#neuroscience`, `#theory of mind`

---

<a id="item-15"></a>
## [The Future Belongs to AI Maniacs](https://marginalrevolution.com/marginalrevolution/2026/07/the-future-belongs-to-ai-maniacs.html?utm_source=rss&utm_medium=rss&utm_campaign=the-future-belongs-to-ai-maniacs) ⭐️ 7.0/10

Tyler Cowen argues in a Free Press column that the future belongs to 'AI maniacs'—people who obsessively master the latest AI models to enhance their workflows and productivity. This perspective highlights a growing divide between those who deeply engage with AI and those who do not, potentially reshaping career success and economic productivity. Cowen defines an AI maniac as someone who tries new models immediately, spends hours mastering them, and uses them to regulate workflows and productivity.

rss · Marginal Revolution · Jul 17, 04:11

**Background**: The column is an opinion piece by economist Tyler Cowen, published on Marginal Revolution. It reflects ongoing debates about AI adoption and skill development in the workforce.

**Tags**: `#AI`, `#productivity`, `#future of work`, `#opinion`

---

<a id="item-16"></a>
## [Ukrainian cruise missile uses hobby drone hardware](https://news.google.com/rss/articles/CBMijwJBVV95cUxNM3FPY2NOQ20tVk1ZMlZTbG01Rk1MM1NNdG1lVGpoWHpKRU14LWpMUi1zWGFKWHJRdzRycEdrVnF4MDN6dktVeldzSnBTQ1RCNkRwLTA0NDNwWWhQZmpaSXpZLVRYX1pCaUVXeXJ1azBhZGlaZ0hSckFiN2JMSXMyM2U1MWswWmMtc21ocHRHWWQySDZFQXVWNS1QaVNpd0NKY0dadnZpT1RtQWhka2NvRXNRMXNSMWhJcnhZeUtaWHBmRm5HMDVFeWhaWmp5NlJHUWZCZHhmUG5laEJVMjNYQXRDN0pnYW96S0lTWFNpa3o1cExVQmNDZ0c4Qm9MVklreHd5MFdSTmRKOXBHS0VN?oc=5) ⭐️ 7.0/10

Ukraine's latest cruise missile, the S8000 Banderol, incorporates an open-source flight-control system commonly found in consumer drones, as reported by New Scientist. This demonstrates how cheap, commercial off-the-shelf technology is making advanced military hardware more accessible, potentially lowering the barrier for nations and groups to develop precision strike capabilities. The flight controller is an open-source design typically used in hobbyist drones, enabling the missile to navigate autonomously. This repurposing of civilian components highlights a trend of rapid innovation in conflict zones.

google_news · New Scientist · Jul 17, 10:00

**Background**: Cruise missiles typically require sophisticated guidance systems, but Ukraine has adapted low-cost, widely available drone electronics to fulfill this role. The S8000 Banderol is a land-attack variant of the R-360 Neptune anti-ship missile, with a range over 1,000 km. Hobby drone components have been increasingly used in military applications, as seen in FPV drones used in the war.

<details><summary>References</summary>
<ul>
<li><a href="https://www.newscientist.com/article/2580002-why-a-ukrainian-cruise-missile-is-flying-with-hobby-drone-hardware/">Why a Ukrainian cruise missile is flying with hobby drone ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/R-360_Neptune">R-360 Neptune - Wikipedia</a></li>
<li><a href="https://war-sanctions.gur.gov.ua/en/page-s8000-banderol">S8000 Banderol cruise missile</a></li>

</ul>
</details>

**Tags**: `#military technology`, `#drone hardware`, `#defense`, `#innovation`

---

<a id="item-17"></a>
## [Kimi K3: 2.8T-Parameter Open-Source AI Model Released](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBGLW5OUXd5MWZyRENvd1A1VWNLVDBfYXhZeWlqdGFQSDhoZFFRdzRCdkdMOEM2bi1DdmY0VnlNWTZCUTNfeXdHX3ZHT0ItU3U3NnlKYkVzT1NBbTFFSkNZ?oc=5) ⭐️ 7.0/10

Moonshot AI has open-sourced Kimi K3, a 2.8 trillion-parameter Mixture-of-Experts model, making it the world's first open-source model in the 3-trillion-parameter class. This release democratizes access to frontier-scale AI, enabling researchers and developers to study and build upon a model with capabilities previously limited to proprietary systems. Kimi K3 features a 1-million-token context window, native vision capabilities, and is built on the custom Kimi Delta Attention (KDA) hybrid linear attention mechanism with Attention Residuals.

google_news · The Neuron · Jul 17, 19:49

**Background**: Large language models like GPT-4 and Llama 3 have driven AI progress, but most top-tier models remain closed-source. Open-source models allow broader community use, inspection, and improvement. Kimi K3's open-source release under a Modified MIT license represents a significant step toward open frontier AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://github.com/47thtechcorner/Kimi-K3/tree/main">GitHub - 47thtechcorner/Kimi-K3: Kimi K3: The 3 Trillion Open ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#machine learning`

---

<a id="item-18"></a>
## [SenseTime Open-Sources Unified Vision Model, Ending Stitch-Monster Era](https://news.google.com/rss/articles/CBMidkFVX3lxTFB3TXRuMHN0M0gyZEhJb3R1RTh1eHdsczBpa2p4aE9kWVNoZ1B3OWV2UldTX1hJRW55RTdJcHlWUjJMc0trcTBOVWVNdmJlZldFY3FKOTN2X0Q1Wkd4N2p3UVc2VHBnN0dIN2VWbGdJU21tdkFOYXc?oc=5) ⭐️ 7.0/10

SenseTime has released and fully open-sourced SenseNova-Vision, a unified visual large model that handles detection, segmentation, depth prediction, and 3D reconstruction within a single architecture. This marks the end of the 'stitch-monster' era where multiple task-specific models were stitched together, potentially reducing complexity and improving efficiency in visual AI applications. The model is part of SenseTime's SenseNova foundation model suite and is designed to tackle object detection, optical character recognition, keypoint localization, and image segmentation.

google_news · Pandaily · Jul 17, 02:06

**Background**: Traditional visual AI systems often relied on separate models for different tasks, leading to a 'stitch-monster' approach that was complex and inefficient. A unified vision model integrates multiple capabilities into one architecture, simplifying deployment and potentially improving performance.

<details><summary>References</summary>
<ul>
<li><a href="https://pandaily.com/sensetime-sensenova-vision-open-source-jul2026">China Visual AI Leader SenseTime Declares End of... - Pandaily</a></li>
<li><a href="https://technode.com/2026/07/14/sensetime-open-sources-sensenova-vision-unified-vision-model/">SenseTime open-sources SenseNova- Vision unified vision model ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Computer Vision`, `#Open Source`, `#SenseTime`

---

<a id="item-19"></a>
## [Ant Group Open-Sources SingGuard-NSFA for AI Agent Security](https://news.google.com/rss/articles/CBMiggFBVV95cUxQckFQakgwNU83Y2JZc0VKS0NUeU5PdldpUzVnUUdVaFo5X2pIYTRCNTdWT3VtRWlqQk5Sai1TNGdoMGZLNkRFUkJMZ0x1d2c5Z2xrVFN2Z0l2NnlnaDc4Y0hZUEJzV05SM3lSZ0M5Rk1KejVGYVJTYmlmNHlIbU1GeTNB?oc=5) ⭐️ 7.0/10

Ant Group has open-sourced SingGuard-NSFA, a guardrail framework designed to secure autonomous AI agents against threats like prompt injection and tool misuse. As autonomous AI agents become more prevalent, security frameworks like SingGuard-NSFA are critical to prevent malicious exploitation and ensure safe deployment in enterprises. SingGuard-NSFA detects both query-side and response-side threats, organized into 7 Level-1 domains, 28 Level-2 risks, and 185 Level-3 variants, and outperforms competing guardrails across model sizes.

google_news · AOL.com · Jul 17, 07:25

**Background**: Autonomous AI agents can independently execute tasks, making them vulnerable to attacks such as prompt injection and sensitive data extraction. Guardrail frameworks like SingGuard-NSFA provide a safety layer to monitor and block harmful inputs and outputs, ensuring agents operate within intended boundaries.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/inclusionAI/SingGuard-NSFA">GitHub - inclusionAI/SingGuard-NSFA</a></li>
<li><a href="https://arxiv.org/abs/2607.13081">[2607.13081] SingGuard-NSFA: Extensible Guardrails for ...</a></li>
<li><a href="https://arxiv.org/html/2607.13081v1">SingGuard-NSFA: Extensible Guardrails for Agentic AI</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Open Source`, `#Autonomous Agents`, `#Ant Group`

---

<a id="item-20"></a>
## [Book Review: A Phone is a Cow](https://marginalrevolution.com/marginalrevolution/2026/07/a-phone-is-a-cow.html?utm_source=rss&utm_medium=rss&utm_campaign=a-phone-is-a-cow) ⭐️ 6.0/10

Philip Auerswald's new book 'A Phone is a Cow' weaves together the history of mobile phones, the biography of Iqbal Quadir who brought cell phones to Bangladesh, and a theory of economic growth. This book offers a unique perspective on how mobile technology can drive economic development, especially in low-income countries, by combining historical narrative with a compelling business story. The book is described as 'three books in one' and succeeds on all fronts, covering mobile phone history, Iqbal Quadir's entrepreneurial journey with Grameenphone, and a broader theory of economic growth.

rss · Marginal Revolution · Jul 17, 11:20

**Background**: Iqbal Quadir founded Grameenphone in Bangladesh in 1997, inspired by the Grameen Bank microcredit model, aiming to provide mobile access to rural areas. The book's title metaphorically suggests that a phone can be as valuable as a cow in a developing economy, serving as a productive asset.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iqbal_Quadir">Iqbal Quadir - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Grameenphone">Grameenphone - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#book review`, `#mobile phones`, `#economic development`, `#technology history`

---

<a id="item-21"></a>
## [NVIDIA Releases New AI Model for Robots](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQQjZNUDFLOXBTSTZNZmFmbFU4bktkM2ZPTE53cDdvLVBTX2F0Vmw3ay1FV2dQUHp4STJzUUFZeklqaS1mcHYyWVIwMG9hcUsyWHFhQlpjYUsxUWh2bnh1OGl6aDJSMnhoZXVreE5KS0NQNEFodWVYRzBQM1RqOGJBVjFZekFqZXJycjBEejdsNFRuREViVnZsVGVKcHdvT3NvQTFVSmo1SG8zQUVSVjNSaFhnV3NFV1RyOFJrV1FJT0ZSOTJWOUpfSVV1MHFhOW96S1hYMw?oc=5) ⭐️ 6.0/10

NVIDIA has released a generative world foundation model for robots, building on its Isaac GR00T and Cosmos model families to enhance robot reasoning and autonomy. This release could serve as a major catalyst for the robotics industry, enabling more intelligent and autonomous robots that can handle complex tasks, potentially accelerating adoption across manufacturing, logistics, and service sectors. The new model is based on NVIDIA's Cosmos-Reason model, which uses reasoning before responding, and is part of the open Isaac GR00T foundation model that brings humanlike reasoning to robots.

google_news · 24/7 Wall St. · Jul 17, 12:49

**Background**: NVIDIA has been developing the Isaac platform for robotics, including simulation tools and foundation models like GR00T N1, a Vision-Language-Action (VLA) model. The Cosmos model family focuses on world understanding and reasoning for physical AI.

<details><summary>References</summary>
<ul>
<li><a href="https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Accelerates-Robotics-Research-and-Development-With-New-Open-Models-and-Simulation-Libraries/default.aspx">NVIDIA Corporation - NVIDIA Accelerates Robotics Research and ...</a></li>
<li><a href="https://research.nvidia.com/publication/2025-03_nvidia-isaac-gr00t-n1-open-foundation-model-humanoid-robots">NVIDIA Isaac GR00T N1: An Open Foundation Model for Humanoid ...</a></li>
<li><a href="https://247wallst.com/investing/2026/07/17/nvidia-just-released-a-seriously-impressive-ai-model-for-robots-this-could-be-the-big-catalyst/">NVIDIA Just Released a Seriously Impressive AI Model for ...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#AI`, `#robotics`, `#machine learning`

---

<a id="item-22"></a>
## [No single AI model dominates vulnerability detection](https://news.google.com/rss/articles/CBMinwFBVV95cUxQeEZXbFZMMmdURGYxRGREVGU4TUZkNXVHSmpCdVFtNGl4NzQ0ckdRcUQ4bmRGb1lkcjZMNWZOTjlhTmlPX1gzZl8wcjk2S2R0SllGcU4tS3VYaUwybzdGcEJ0U1pBVWFLZ2ZBWlFCYzltZjdOWEpWUEhVeG5QVkI0NHBEMkYweXZVa2FLVTd6NzRDV0p1dXZneF9pT3lsejg?oc=5) ⭐️ 6.0/10

A recent study has found that no single AI model consistently outperforms others in detecting software vulnerabilities, challenging the notion of a universal best model for this task. This finding underscores the need for tailored or ensemble approaches in AI-driven cybersecurity, as relying on a single model may leave gaps in vulnerability coverage. The study compared various AI models, including large language models (LLMs) and deep learning systems, across multiple vulnerability detection benchmarks, revealing significant performance variability depending on the type of vulnerability and codebase.

google_news · The News International · Jul 17, 07:33

**Background**: Vulnerability detection is a critical task in cybersecurity, aiming to identify security flaws in software before attackers exploit them. AI models, particularly LLMs, have been increasingly applied to automate this process, but their relative effectiveness has been unclear.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.bswen.com/blog/2026-03-26-ai-security-vulnerability-detection/">How Do AI Models Compare for Security Vulnerability Detection?</a></li>
<li><a href="https://www.mdpi.com/2504-4990/8/1/19">AI-Powered Vulnerability Detection and Patch Management in ...</a></li>
<li><a href="https://www.mdpi.com/2079-9292/14/22/4449">Modern Approaches to Software Vulnerability Detection: A ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#vulnerability detection`, `#cybersecurity`, `#machine learning`

---

<a id="item-23"></a>
## [Deloitte Uses Claude AI to Speed Open Source Patching](https://news.google.com/rss/articles/CBMinwFBVV95cUxQdllGNE9nancydkR2R1QwaGtjY19odmRuc1B0UU9DSUdVNFprWDJNb2lXdmNFeTJuTGw4RUdGRmpxbkR1cHVCcmF3NUFwUjljNk9XS1NQcmNpdzNxVUVHVHVGalRDSUpYcU1xZnlRZ2JkTjVsbGdYRXRZOElGUlc2WTZKOElFRmoxOHozV21TZVl4dnNPYmFURVoxejhod2c?oc=5) ⭐️ 6.0/10

Deloitte has adopted Anthropic's Claude AI to accelerate the process of patching open source software dependencies, reducing manual effort and improving response times for security vulnerabilities. This demonstrates a practical enterprise application of large language models in DevOps and security, potentially setting a precedent for other organizations to automate patching and reduce exposure to open source vulnerabilities. Claude AI is used to analyze vulnerability reports, identify affected dependencies, and suggest or apply patches, streamlining what is typically a time-consuming manual process. The specific models or integration details have not been disclosed.

google_news · Open Source For You · Jul 17, 08:11

**Background**: Open source patching is the process of updating third-party libraries and components in software projects to fix security vulnerabilities. It is a critical but often labor-intensive task for enterprises, as failing to patch promptly can lead to breaches. Claude is a large language model developed by Anthropic, trained with constitutional AI to prioritize safety and accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="https://opensource.google/documentation/reference/releasing">Releasing Code | Google Open Source</a></li>

</ul>
</details>

**Tags**: `#AI`, `#DevOps`, `#Open Source`, `#Security`

---