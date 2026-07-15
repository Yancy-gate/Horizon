---
layout: default
title: "Horizon Summary: 2026-07-16 (ZH)"
date: 2026-07-16
lang: zh
---

> 从 145 条内容中筛选出 21 条重要资讯。

---

1. [Hugging Face Transformers v5.14.0 新增 Inkling，一个 975B 参数的开源多模态模型](#item-1) ⭐️ 9.0/10
2. [AsyncAPI npm 供应链攻击传播 Miasma 僵尸网络](#item-2) ⭐️ 9.0/10
3. [Stripe 与 Advent 联合竞购 PayPal](#item-3) ⭐️ 8.0/10
4. [在 13 年前的 Xeon 上以 5 tokens/秒运行 Gemma 4 26B](#item-4) ⭐️ 8.0/10
5. [模型路由：概念简单，现实复杂](#item-5) ⭐️ 8.0/10
6. [Hugging Face 推出 Real World VoiceEQ 语音 AI 基准测试](#item-6) ⭐️ 8.0/10
7. [黑客揭露 Suno AI 音乐生成器抓取 YouTube 音频](#item-7) ⭐️ 8.0/10
8. [苹果智能获准在华推出，采用阿里通义千问](#item-8) ⭐️ 8.0/10
9. [Vint Cerf 制定标准以识别在线 AI 代理](#item-9) ⭐️ 8.0/10
10. [OpenAI 研究员 Miles Wang 洽谈创办 20 亿美元 AI 药物发现初创公司](#item-10) ⭐️ 8.0/10
11. [Claude web_fetch 漏洞导致记忆数据泄露](#item-11) ⭐️ 8.0/10
12. [面壁智能 MiniCPM 端侧模型将搭载三星手机上市](#item-12) ⭐️ 8.0/10
13. [热力学计算机利用随机能量波动进行计算](#item-13) ⭐️ 8.0/10
14. [用无监督偏见检测工具审计荷兰风险算法](#item-14) ⭐️ 8.0/10
15. [白宫可能监管开源 AI 模型](#item-15) ⭐️ 8.0/10
16. [小米开源 380 亿参数具身 AI 模型 Robotics-U0](#item-16) ⭐️ 8.0/10
17. [视频生成预训练统一六项视觉任务](#item-17) ⭐️ 8.0/10
18. [谷歌发布 LiteRT.js，通过 WebGPU 在浏览器运行 ML 模型](#item-18) ⭐️ 8.0/10
19. [构建 Shippy AI 智能体的经验教训](#item-19) ⭐️ 7.0/10
20. [AI 编程工具让软件变得可丢弃](#item-20) ⭐️ 7.0/10
21. [RK3576 NPU 支持加入开源 Rocket 驱动](#item-21) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Hugging Face Transformers v5.14.0 新增 Inkling，一个 975B 参数的开源多模态模型](https://github.com/huggingface/transformers/releases/tag/v5.14.0) ⭐️ 9.0/10

Hugging Face Transformers v5.14.0 集成了来自 Thinking Machines Lab 的 Inkling 模型，这是一个拥有 975B 总参数（41B 激活参数）的大型开源多模态模型，支持文本、图像和音频输入，并生成文本输出。 Inkling 是最大的开源多模态模型之一，使开发者能够构建具有高级多模态理解能力的智能体系统、编程助手和聊天机器人。将其纳入 Transformers 降低了研究人员和企业实验及微调前沿级模型的门槛。 Inkling 采用混合专家（MoE）Transformer 架构，支持 100 万 token 的上下文窗口，并在 45 万亿 token 的文本、图像、音频和视频数据上进行了预训练。该版本还包括 TIPSv2 模型、Flash Attention 修复等性能改进，以及多 token 预测（MTP）支持等新生成特性。

github · ArthurZucker · 7月15日 19:02

**背景**: Hugging Face Transformers 是一个广泛使用的开源库，用于自然语言处理和多模态 AI，提供了数千个预训练模型。Inkling 由 Thinking Machines Lab 开发，这是一家由前 OpenAI CTO Mira Murati 创立的 AI 初创公司，已融资 20 亿美元。开源权重模型允许研究人员和开发者自由检查、微调和部署模型，促进创新和透明度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://en.wikipedia.org/wiki/Thinking_Machines_Lab">Thinking Machines Lab</a></li>
<li><a href="https://www.baseten.co/library/inkling/">Inkling | Model library</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 Inkling 的多模态能力，尤其是音频支持表示兴奋，并指出其在智能体应用中的潜力。一些人强调 Thinking Machines Lab 可能成为类似 DeepSeek 或 Z.ai 的关键开源权重竞争者，而另一些人则赞赏在 Tinker 上提供微调的商业模型。

**标签**: `#transformers`, `#multimodal`, `#open-weights`, `#AI`, `#model-release`

---

<a id="item-2"></a>
## [AsyncAPI npm 供应链攻击传播 Miasma 僵尸网络](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNQUJWWGM1MGRzdlJsT3RCb1RyVXFabXJidFNIdXBtUHcxWDE4bVB1QkdMemFnQVNnT0p1WmlyNlp1Tk13OXNPMlVwaU5SdlZFbXNzOGNnUEg1X1VaZXpScDZzVVpvMWktdFVpNW52aWp6QnFUR3NuMmpueWpOcUNUWFhmOC1PVmNkNFNlaE4wbjRuOW5lMC1Pa1NYMGY4OVpfQ2tOZXBjQUF3eVczdGpLNjVLcWRFejNIX1pZRTZVbUtEZ2wyVlhSQ0IyNW13ZTFoRzNYbE1nU1l4dFlmeFlMMkNSTQ?oc=5) ⭐️ 9.0/10

发现一起针对 AsyncAPI npm 包的活跃供应链攻击，攻击者利用被攻陷的 GitHub Actions 发布恶意版本的 AsyncAPI 包，这些包会传播多阶段 Miasma 僵尸网络。该攻击于 2026 年 7 月 14 日首次被发现，涉及至少五个恶意包版本。 此次攻击破坏了软件供应链，可能影响数千名依赖 AsyncAPI 进行 API 文档和代码生成的开发者和组织。利用被攻陷的 CI/CD 管道（GitHub Actions）分发恶意软件，代表了供应链威胁的复杂且危险的升级。 恶意包是通过项目合法的 GitHub Actions 发布工作流发布的，表明攻击者获取了仓库的密钥或令牌。Miasma 僵尸网络具有窃取凭证的能力，并包含远程访问木马，恶意软件在库加载时执行，而不仅仅在安装时。

google_news · Rescana · 7月15日 11:57

**背景**: AsyncAPI 是一个用于描述事件驱动 API 的开源规范，类似于 REST API 的 OpenAPI。其 npm 包用于从 AsyncAPI 定义生成代码和文档。针对 npm 的供应链攻击日益常见，但通过攻陷 GitHub Actions 将恶意软件注入合法发布版本是一种更高级的技术，能够绕过常规安全检查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions">AsyncAPI Supply Chain Compromise via GitHub Actions | Wiz Blog</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/-asyncapi-npm-packages-infected-with-credential-stealing-malware/">AsyncAPI npm packages infected with credential-stealing malware</a></li>
<li><a href="https://www.stepsecurity.io/blog/compromised-next-branch-pushes-malicious-asyncapi-generator-generator-helpers-and-generator-components-to-npm">Coordinated AsyncAPI Supply Chain Attack: Miasma RAT ...</a></li>

</ul>
</details>

**标签**: `#supply chain attack`, `#npm`, `#botnet`, `#GitHub Actions`, `#security`

---

<a id="item-3"></a>
## [Stripe 与 Advent 联合竞购 PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 8.0/10

据知情人士透露，Stripe 与私募股权公司 Advent International 已联合提出以超过 530 亿美元收购 PayPal。 此次收购将把 Stripe、PayPal、Venmo、Braintree 和 Xoom 等主要支付平台整合到同一旗下，引发重大反垄断担忧，并可能重塑在线支付行业格局。 该交易对 PayPal 的估值超过 530 亿美元，若完成，将把 Stripe 对开发者友好的支付基础设施与 PayPal 庞大的用户群及银行牌照相结合，可能使 Stripe 能够提供新的金融服务。

hackernews · rvz · 7月15日 03:32 · [社区讨论](https://news.ycombinator.com/item?id=48915953)

**背景**: Stripe 是一家以开发者工具闻名的领先在线支付处理商，而 PayPal 是广泛使用的数字钱包和支付平台。Advent International 是一家全球私募股权公司，在金融科技投资方面经验丰富。由于在线非面对面交易市场的集中度，该收购将面临严格的反垄断审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stripe,_Inc.">Stripe , Inc. - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advent_International">Advent International - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员对竞争减少、潜在费用上涨以及 Stripe 对某些行业（如大麻、成人内容）的限制性政策表示担忧，而 PayPal 目前允许这些行业。一些人指出了反垄断障碍，以及 Stripe 可能利用 PayPal 的银行牌照来扩展其服务的可能性。

**标签**: `#acquisition`, `#payments`, `#antitrust`, `#fintech`, `#Stripe`

---

<a id="item-4"></a>
## [在 13 年前的 Xeon 上以 5 tokens/秒运行 Gemma 4 26B](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) ⭐️ 8.0/10

一篇技术博客展示了通过极端优化技术，在没有任何 GPU 的 13 年前 Intel Xeon CPU 上，以每秒 5 个 token 的速度运行 Google 的 Gemma 4 26B A4B 模型。 这表明大型语言模型可以在极其老旧且低成本的硬件上运行，可能使 AI 的获取更加民主化，并减少对昂贵 GPU 的依赖。 Gemma 4 26B 模型采用混合专家（MoE）架构，总参数 260 亿，每个 token 激活 40 亿参数，这使得在 CPU 上进行高效推理成为可能。该博客可能采用了量化、内存优化和高效 token 生成等技术来实现每秒 5 个 token 的速度。

hackernews · neomindryan · 7月15日 15:34 · [社区讨论](https://news.ycombinator.com/item?id=48922434)

**背景**: 大型语言模型通常需要强大的 GPU 进行推理，因为其规模庞大且计算需求高。然而，量化、剪枝和高效架构（如 MoE）等技术可以降低资源需求。在 CPU 上运行此类模型具有挑战性，但通过激进优化是可能的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/google/gemma-4-26B-A4B-it">google/gemma-4-26B-A4B-it · Hugging Face</a></li>
<li><a href="https://deepmind.google/models/gemma/gemma-4/">Gemma 4 — Google DeepMind</a></li>
<li><a href="https://community.intel.com/t5/Blogs/Tech-Innovation/Artificial-Intelligence-AI/Intel-Xeon-is-all-you-need-for-AI-inference-Performance/post/1506083">Intel Xeon is all you need for AI inference: Performance Leadership on Real World Applications - Intel Community</a></li>

</ul>
</details>

**社区讨论**: 评论者就本地推理与云 API 的成本效率展开辩论，指出旧 CPU 的电力成本可能超过 API 价格。一些人分享了他们在类似硬件上的基准测试，报告速度为 8-12 tokens/秒，而另一些人预测到 2027 年中，200B+参数的 MoE 模型将能在消费级硬件上运行。

**标签**: `#LLM inference`, `#hardware optimization`, `#local AI`, `#cost analysis`, `#open source`

---

<a id="item-5"></a>
## [模型路由：概念简单，现实复杂](https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt) ⭐️ 8.0/10

IBM Research 在 Hugging Face 上发表了一篇新博客，探讨了构建大型语言模型有效路由系统时隐藏的复杂性和权衡，揭示了看似简单的事情其实充满挑战。 随着组织部署多个 LLM 以平衡成本、延迟和质量，模型路由对于高效推理变得至关重要；理解其细微差别有助于从业者避免陷阱，构建更稳健的 AI 系统。 文章可能讨论了路由准确性、动态模型性能以及路由决策开销等挑战，强调简单的启发式方法在生产环境中常常失效。

rss · Hugging Face Blog · 7月15日 17:27

**背景**: 模型路由是一种技术，系统从模型池中为每个输入提示选择最合适的 LLM，旨在在保持质量的同时最小化成本。它是多 LLM 服务系统的关键组成部分，这类系统越来越多地被用于优化吞吐量、延迟和成本之间的推理权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ulab-uiuc/LLMRouter">GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source Library for LLM Routing · GitHub</a></li>
<li><a href="https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/">Multi-LLM routing strategies for generative AI applications on AWS | Artificial Intelligence</a></li>
<li><a href="https://arxiv.org/abs/2502.08773">[2502.08773] Universal Model Routing for Efficient LLM Inference</a></li>

</ul>
</details>

**标签**: `#model routing`, `#LLM`, `#inference`, `#systems`, `#AI engineering`

---

<a id="item-6"></a>
## [Hugging Face 推出 Real World VoiceEQ 语音 AI 基准测试](https://huggingface.co/blog/real-world-voiceeq) ⭐️ 8.0/10

Hugging Face 与 Hume AI 合作推出了 Real World VoiceEQ，这是一个旨在评估语音 AI 系统在人类感知质量而非纯粹技术准确性方面的基准测试。 该基准测试填补了当前语音 AI 评估中的关键空白，因为标准指标往往无法捕捉系统是否听起来自然或响应恰当，从而可能推动语音应用用户体验的改进。 该基准测试包含 785,000 个 TTS 评分和 48,000 个 STS 评分，使其成为迄今为止最大规模的语音 AI 人类评估之一，并评估了 ASR、TTS、语音到语音以及语音理解任务中的模型。

rss · Hugging Face Blog · 7月15日 00:00

**背景**: 语音 AI 系统通常使用技术指标进行评估，例如 ASR 的词错误率（WER）或 TTS 的平均意见得分（MOS），但这些指标往往无法捕捉人类对自然度、情感或恰当性的感知。Real World VoiceEQ 旨在衡量语调、情感、说话者身份和背景语境等仅靠文本无法传达的品质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hume.ai/blog/introducing-real-world-voiceeq-measuring-the-human-quality-of-voice-ai">Introducing Real World VoiceEQ: Measuring the Human Quality ...</a></li>
<li><a href="https://www.zal-group.com/news/product-model-releases/hugging-face-real-world-voiceeq-voice-ai-benchmark">Hugging Face Launches Real World VoiceEQ Benchmark for Voice AI</a></li>
<li><a href="https://andresseo.expert/ai/humeai-real-world-voiceeq-benchmark-exposes-voice-ais-blind-spots-in-human-interaction/">Real World VoiceEQ: Benchmarking Voice AI's Human Quality</a></li>

</ul>
</details>

**标签**: `#voice AI`, `#benchmark`, `#speech technology`, `#AI evaluation`

---

<a id="item-7"></a>
## [黑客揭露 Suno AI 音乐生成器抓取 YouTube 音频](https://techcrunch.com/2026/07/15/hack-suggests-ai-music-generator-suno-scraped-youtube-for-training-data/) ⭐️ 8.0/10

一名黑客利用员工凭证访问了 Suno 的源代码，发现该 AI 音乐生成器抓取了数十年的 YouTube 音频作为训练数据。 这一发现对 AI 训练数据伦理和版权法具有重大影响，可能影响法律框架和公众对 AI 公司的信任。 此次黑客攻击提供了抓取 YouTube 的具体证据，而 Suno 此前并未公开披露。该事件也凸显了 AI 公司的安全漏洞。

rss · TechCrunch AI · 7月15日 17:00

**背景**: Suno 是一款 AI 音乐生成器，可根据文本提示创作歌曲。训练此类模型通常需要大量音频数据集，许多 AI 公司会从互联网抓取公开数据，这常常引发版权问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://suno.com/l/ai-music-app">Suno: The AI Music App for Every Creator</a></li>
<li><a href="https://suno.com/l/ai-music-generator">AI Music Generator: Turn Your Ideas into Tracks That Slap</a></li>

</ul>
</details>

**标签**: `#AI`, `#music generation`, `#data scraping`, `#copyright`, `#security`

---

<a id="item-8"></a>
## [苹果智能获准在华推出，采用阿里通义千问](https://techcrunch.com/2026/07/15/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/) ⭐️ 8.0/10

苹果的 AI 平台 Apple Intelligence 已通过与阿里巴巴的通义千问合作，正式获批在中国推出。这证实了此前的传闻，标志着苹果在中国市场的 AI 雄心迈出重要一步。 这一合作意义重大，因为它使苹果能够在中国这个关键市场提供 AI 功能，而外国 AI 服务在此常面临监管障碍。同时，这也巩固了阿里巴巴在 AI 竞赛中的地位，并加剧了与中国其他 AI 提供商的竞争。 Apple Intelligence 可在 iPhone 15 Pro 及后续机型上使用，将大语言模型集成到 Siri 和其他应用中。与阿里巴巴的合作很可能涉及使用通义千问模型，以在遵守中国法规的同时提供 AI 功能。

rss · TechCrunch AI · 7月15日 15:29

**背景**: Apple Intelligence 是苹果的个性化智能系统，由下一代基础模型驱动，为 iPhone、iPad、Mac 等设备带来 AI 能力。通义千问是阿里云开发的一系列大语言模型，部分为开源。中国要求外国 AI 服务与本地公司合作才能合法运营，因此这笔交易对苹果在华推出 AI 至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IOS_18">iOS 18 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri - Apple</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Alibaba`, `#Qwen AI`, `#AI`, `#China`

---

<a id="item-9"></a>
## [Vint Cerf 制定标准以识别在线 AI 代理](https://techcrunch.com/2026/07/15/vint-cerf-is-working-on-a-plan-to-unleash-ai-agents-on-the-open-internet/) ⭐️ 8.0/10

TCP/IP 联合创始人 Vint Cerf 正牵头制定一项计划，为开放互联网上的 AI 代理创建识别协议，以确保透明度和问责制。 该标准可能使 AI 代理能够在开放网络上安全地互操作，超越专有系统，并影响未来的互联网治理和 AI 互操作性。 Cerf 与其他互联网知名人士共同参与这项工作，此前他刚从 Google 退休，担任首席互联网布道师 21 年。

rss · TechCrunch AI · 7月15日 12:00

**背景**: AI 代理是自主执行任务的软件程序，但目前大多数在封闭的专有系统中运行。Vint Cerf 以共同设计互联网基础协议 TCP/IP 而闻名。该计划旨在为识别 AI 代理创建开放标准，类似于 IP 地址识别设备的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/15/vint-cerf-is-working-on-a-plan-to-unleash-ai-agents-on-the-open-internet/">Vint Cerf is working on a plan to unleash AI agents on the ...</a></li>
<li><a href="https://www.techtimes.com/articles/320264/20260712/vint-cerf-retires-google-warning-ai-agents-need-real-protocols.htm">Vint Cerf Retires From Google With A Warning: AI Agents Need ...</a></li>
<li><a href="https://explore.n1n.ai/blog/vint-cerf-ai-agent-standards-open-internet-2026-07-15">Vint Cerf Proposes New Standards for AI Agents on the Open ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#internet standards`, `#Vint Cerf`, `#AI governance`, `#protocols`

---

<a id="item-10"></a>
## [OpenAI 研究员 Miles Wang 洽谈创办 20 亿美元 AI 药物发现初创公司](https://techcrunch.com/2026/07/14/openai-researcher-miles-wang-in-talks-to-launch-ai-drug-discovery-startup-valued-at-2b/) ⭐️ 8.0/10

据报道，OpenAI 研究员 Miles Wang 正在洽谈创办一家估值 20 亿美元的 AI 驱动药物发现初创公司，这反映了投资者对将 AI 应用于生命科学领域的强烈热情。 这一消息凸显了 AI 人才向生物技术领域流动的趋势，可能加速药物开发并降低成本，从而改变制药行业。 该初创公司仍处于早期洽谈阶段，尚未披露官方名称或具体重点；据报道，20 亿美元的估值是基于投资者的兴趣，而非成熟的技术。

rss · TechCrunch AI · 7月15日 00:27

**背景**: AI 药物发现利用机器学习来识别疾病靶点、生成候选化合物并预测安全性，有可能缩短通常 10-15 年的药物开发周期。像 Insilico Medicine 和 Recursion Pharmaceuticals 这样的公司已经在这一领域吸引了大量投资。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41591-024-03434-4">Artificial intelligence in drug development | Nature Medicine</a></li>
<li><a href="https://www.weforum.org/stories/all/how-ai-is-reshaping-drug-discovery/">Here’s how AI is reshaping drug discovery | World Economic Forum</a></li>

</ul>
</details>

**标签**: `#AI`, `#drug discovery`, `#startup`, `#biotech`, `#investment`

---

<a id="item-11"></a>
## [Claude web_fetch 漏洞导致记忆数据泄露](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

研究员 Ayush Paul 发现 Claude 的 web_fetch 工具存在一个绕过漏洞，通过构造一个蜜罐网站诱使代理跟随嵌套链接，从而窃取用户记忆数据。Anthropic 已通过禁止 web_fetch 导航到获取内容中的链接来修复此漏洞。 该攻击展示了一种绕过 Anthropic 数据泄露防护的新方法，凸显了保护 LLM 代理免受提示注入攻击的持续挑战。它强调了在私有数据、不可信内容和外部通信渠道之间建立强隔离的必要性。 该攻击利用了 web_fetch 可以跟随先前获取页面中嵌入的 URL 这一漏洞，实现了多步数据窃取链。蜜罐网站仅对带有 'Claude-User' 用户代理的客户端提供恶意提示，以逃避检测。

rss · Simon Willison · 7月15日 14:21

**背景**: 像 Claude 这样的 LLM 代理在能够访问私有数据、处理不可信内容并具有外部通信能力时，面临“致命三重奏”风险。提示注入攻击可以通过将敏感信息嵌入 URL 来诱骗模型泄露数据。Anthropic 此前限制 web_fetch 只能导航到用户提供或搜索返回的 URL，但新攻击通过利用获取页面中的链接链找到了绕过方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Docs</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and external communication</a></li>
<li><a href="https://www.osohq.com/learn/lethal-trifecta-ai-agent-security">Understanding the Lethal Trifecta of AI Agents</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论可能对绕过漏洞的简易性表示担忧，并对 Anthropic 未支付漏洞赏金感到失望，尽管也有人认可该公司已内部发现该问题。该攻击进一步呼吁采取更根本的架构性防护措施来抵御提示注入。

**标签**: `#AI safety`, `#LLM security`, `#data exfiltration`, `#Claude`, `#prompt injection`

---

<a id="item-12"></a>
## [面壁智能 MiniCPM 端侧模型将搭载三星手机上市](https://36kr.com/p/3896830362601351?f=rss) ⭐️ 8.0/10

面壁智能与三星达成合作，将其 MiniCPM 系列端侧模型搭载于多款三星旗舰手机上市；同日，包括 Apple 智能和 MiniCPM 在内的七款手机端侧生成式 AI 服务获得中国网信部门备案批准。 这标志着端侧 AI 从概念演示进入规模化落地阶段，并表明手机厂商正从完全自研转向与专业 AI 模型公司合作，端侧模型的市场化分工正在形成。 面壁智能的 MiniCPM5-1B 模型仅 10 亿参数，在 Artificial Analysis Intelligence Index 上超越多款更大参数的开源模型；MiniCPM-V 4.6 仅需 6GB 内存即可运行。截至 2026 年上半年，面壁智能累计融资超 50 亿元，估值突破 200 亿元。

rss · 36氪 · 7月15日 11:47

**背景**: 端侧 AI 指直接在手机上运行模型而非云端，具有低延迟、保护隐私等优势。面壁智能孵化自清华大学自然语言处理实验室，提出“大模型密度定律”——达到特定智能水平所需的参数量每 3.5 个月减半，使得强大模型能在资源受限的设备上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cac.gov.cn/2026-07/15/c_1785861480767004.htm">关于发布7款提供手机端侧生成式人工智能服务已备案信息的公告_中央网...</a></li>
<li><a href="https://modelbest.cn/">ModelBest - 面壁智能</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1961168095851819213">端上大模型（面壁智能）：MiniCPM4、MiniCPM-V、MiniCPM-V 4.5、AgentCPM-GUI - 知乎</a></li>

</ul>
</details>

**标签**: `#on-device AI`, `#smartphone`, `#generative AI`, `#China`, `#partnership`

---

<a id="item-13"></a>
## [热力学计算机利用随机能量波动进行计算](https://www.quantamagazine.org/thermodynamic-computers-go-with-the-energy-flow-20260715/) ⭐️ 8.0/10

这种方法可能大幅降低计算能耗，解决现代硬件（尤其是 AI 和大型数据中心）的关键瓶颈。 热力学计算机通过利用自然热波动运行，将噪声转化为资源而非需要抑制的问题。

rss · Quanta Magazine · 7月15日 15:24

**背景**: 传统计算机需要精确控制和纠错以避免随机能量波动导致错误。热力学计算则反其道而行之，设计系统固有地利用这些波动进行计算，其灵感来自统计力学和热力学原理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.quantamagazine.org/thermodynamic-computers-go-with-the-energy-flow-20260715/">Thermodynamic Computers Go With the ( Energy )... | Quanta Magazine</a></li>
<li><a href="https://extropic.ai/writing/thermodynamic-computing-from-zero-to-one">Thermodynamic Computing: From Zero to One | Extropic</a></li>
<li><a href="https://arxiv.org/abs/1911.01968">[1911.01968] Thermodynamic Computing</a></li>

</ul>
</details>

**标签**: `#thermodynamic computing`, `#energy efficiency`, `#computer architecture`, `#physics of computation`

---

<a id="item-14"></a>
## [用无监督偏见检测工具审计荷兰风险算法](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBVZ1hGNGJ3aFh6Zm9tMlQtMzVwNm1CT3liVTZYRFZMQTJIeldpVjNRUzE0bkNCdmUybnhGWjQ2M0hFMUJKcS1aM0FVVFg3ZFN6MkxMMV9JclVFMllObUQ0bUYxUGJpb0E?oc=5) ⭐️ 8.0/10

研究人员使用一种无监督偏见检测工具审计了荷兰公共部门的风险画像算法（DUO），该工具通过聚类识别出受到不公平对待的群体。该工具检测到不同学生群体在误分类率上存在统计显著的差异。 这项工作展示了一种实用且与模型无关的方法，用于审计高风险公共部门决策中的算法公平性。它为监管机构和审计人员提供了一种无需敏感人口标签即可检测交叉性偏见的模板。 该工具使用层次聚类来发现误分类率较高的群体，然后进行统计显著性检验。审计聚焦于 DUO 针对学生助学金的画像算法，该算法按教育类型（MBO、HBO、WO）进行区分。

google_news · The Association for the Advancement of Artificial Intelligence · 7月15日 12:40

**背景**: 公共部门风险画像中的算法偏见可能导致对公民的不公平对待。传统的偏见审计通常需要标记的敏感属性（如种族、性别），但这些属性可能不可用或受法律限制。无监督偏见检测工具通过聚类来识别潜在的不利群体，无需此类标签，因此适用于隐私保护的审计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oecd.ai/en/catalogue/tools/unsupervised-bias-detection-tool">Unsupervised bias detection tool - OECD.AI</a></li>
<li><a href="https://github.com/NGO-Algorithm-Audit/unsupervised-bias-detection">GitHub - NGO-Algorithm-Audit/unsupervised-bias-detection: Unsupervised bias detection tool for binary AI classifiers. Including qualitative approach to assess quantitative disparities. · GitHub</a></li>
<li><a href="https://arxiv.org/pdf/2502.01713">Auditing a Dutch Public Sector Risk Profiling Algorithm Using an...</a></li>

</ul>
</details>

**标签**: `#algorithmic bias`, `#AI fairness`, `#public sector`, `#unsupervised learning`, `#auditing`

---

<a id="item-15"></a>
## [白宫可能监管开源 AI 模型](https://news.google.com/rss/articles/CBMiowFBVV95cUxNWkotcmhYOVRZUGU4MjFHS3hrU2x0ekNxNTBWNkpMczBUVTZLNDU5OVVSQUxQZjR2aXExbnduRERxTWJZcmIwUnNGNkU1X2NHbVg2SjQwQXZlZ0tsRmlHQ3d2UUdsZVlWZ08yY3ZNVE9EQk53Tkl1RjdzbGZHVXlZYW4yUjc0dWZqaFlRX05yeVF2RXhrYmlEWWw4RmlUZmI5WVcw?oc=5) ⭐️ 8.0/10

白宫表示不排除对开源 AI 模型采取行动的可能性，这标志着可能转向对这些广泛使用的系统进行监管。 这可能会影响开源 AI 的开发与部署，波及依赖这些模型的研究人员、初创公司及大型科技企业，并可能塑造全球 AI 政策。 白宫尚未明确可能采取何种行动，但此番表态正值关于 AI 监管的更广泛讨论之际，包括针对前沿 AI 模型的自愿监管框架。

google_news · Semafor · 7月15日 09:17

**背景**: 开源 AI 模型是公开可用的系统，任何人都可以使用、修改和分发。它们推动了创新，但也引发了滥用担忧，例如生成有害内容或助长虚假信息。白宫此前曾敦促国会对 AI 采取轻触式监管，但这一新信号表明可能收紧监管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnn.com/2026/03/20/tech/white-house-ai-framework">The White House just laid out how it wants to regulate AI</a></li>
<li><a href="https://apnews.com/article/white-house-donald-trump-artificial-intelligence-479eb3d0a50fe7237678a9bfb146ac7a">White House urges Congress to take a light touch on AI ...</a></li>
<li><a href="https://www.crowell.com/en/insights/client-alerts/executive-order-creates-voluntary-regulatory-regime-of-frontier-ai-models">Executive Order Creates Voluntary Regulatory Regime of ...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open-source`, `#regulation`, `#White House`

---

<a id="item-16"></a>
## [小米开源 380 亿参数具身 AI 模型 Robotics-U0](https://news.google.com/rss/articles/CBMic0FVX3lxTE5odUpqMEVaT2wxbkhXa2puWG5KOGRlZmRpalVQNHB6cDJEQnh4RDAyeEpSR1FxYUxqQVpYSHZYTW0zSDh0TWNIcm9BTkVISG1udGFpQ2ozOGRxeURKd2RGN1NJUUVGaWE5WFFKOUFKNlgwM0E?oc=5) ⭐️ 8.0/10

小米开源了 Robotics-U0，这是一个 380 亿参数的具身生成模型，统一了场景生成、具身迁移、视频生成和文本到图像四项机器人任务。该模型生成机器人训练数据的速度比现有方法快达 83 倍。 此次发布解决了具身 AI 中真实机器人交互数据稀缺的关键瓶颈，有望加速机器人训练和开发。作为开源模型，它降低了研究人员和开发者推进机器人技术与具身智能的门槛。 Robotics-U0 是一个 380 亿参数的多模态自回归世界基础模型，旨在单一架构内统一多项机器人任务。该模型由小米机器人团队于 2026 年 7 月 15 日发布，并以开源形式提供。

google_news · Pandaily · 7月15日 07:53

**背景**: 具身 AI 指能够感知、推理并在物理世界中行动的 AI 系统，例如机器人。在此背景下，生成模型可以创建合成训练数据，减少对昂贵的真实世界数据收集的需求。小米的模型是最大的开源具身 AI 模型之一，结合了生成能力与任务统一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://robottoday.com/industry-briefing/xiaomi-launches-robotics-u0-a-unified-38b-parameter-generative-model-for-robotics/8654">Xiaomi Launches Robotics-U0: A Unified 38B-Parameter ...</a></li>
<li><a href="https://happyrock.cloud/blog/2026-07-15_xiaomi_robotics_u0_38b_world_model_embodied_ai_data_engine_en/">Xiaomi-Robotics-U0 Deep Dive: 38B Parameter World Model ...</a></li>
<li><a href="https://edgen.beta.edgen.tech/zh/news/post/xiaomi-open-sources-38b-parameter-robotics-model-to-mass-produce-robot-training-data">Xiaomi open-sources 38B-parameter robotics model to mass ...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#AI`, `#open-source`, `#embodied AI`, `#Xiaomi`

---

<a id="item-17"></a>
## [视频生成预训练统一六项视觉任务](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPejlnMDhlc243a2JzRjViZzNtQU1BMDJ5THZxLVE1Zkx6ck9jMi1rVlJQTVF4LVZhSlZuWm15Vjhtd25Tbzd2WklpOVRnbWF2YnBrOVF4QnJ3VE5ETVAycXotNmFLLWJEdGlFZDhOVkxSNnM0WnhkR1h2a1h1MzBkZnJRTTFoWGhRUjZuRGZ5YmZGdGV5bWp1d0oydm9mMEk1MDN3QlljVDNqM2toTk8tRzNlVm4welZJeU1lMm1GOVJUUHpZUXVwVlg2UDRXMHdRN2t3?oc=5) ⭐️ 8.0/10

Google DeepMind 在 ECCV 2026 上提出的 GenCeption 表明，一个经过视频生成预训练的视频扩散模型，在深度估计、法线预测、姿态估计、分割等视觉任务上，能够匹配甚至超越专用模型，且使用的数据量最多减少 90%。 这一突破表明，视频生成预训练可以作为通用视觉学习器，可能减少计算机视觉中对特定任务架构和大量标注数据的需求。 该模型通过文本指令引导，以前馈方式运行，无需针对特定任务进行微调。它统一了六项任务：深度估计、法线预测、姿态估计、分割、边缘检测和目标检测。

google_news · Tech Times · 7月15日 13:07

**背景**: 传统计算机视觉为每个任务依赖单独的专用模型，每个模型需要自己的架构和标注数据。像扩散模型这样的视频生成模型从大规模视频数据集中学习丰富的时空表征。GenCeption 将这样一个预训练的生成模型重新用作统一的视觉编码器，证明了生成式预训练可以迁移到判别性任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/320556/20260715/video-generation-pre-training-unifies-six-vision-tasks-beats-specialists-less-data.htm">Video Generation Pre-Training Unifies Six Vision Tasks, Beats ...</a></li>
<li><a href="https://genception.github.io/">Video Generation Models are General-Purpose Vision Learners</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#pre-training`, `#video generation`, `#AI research`

---

<a id="item-18"></a>
## [谷歌发布 LiteRT.js，通过 WebGPU 在浏览器运行 ML 模型](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNVHhUbUJZekhlMW5zenUtYkhVRGg1dUxEM2lJOUd5cnhMUjJCM0VPS1JnUHd0aWEzejN3T09hSlc4NW5pemJiWHNjVTRiWHFIYW5pUTRNb2RJbk1FUHpUU2ZaYWF4TEd5dmQtTDd3Z3ZuT1A0RGItd1g4QVV4d2w2RlJaV2xLbVlIQnhGLTZQQUhhdWoxV2JmTjRmenl3UXgzRVJYYnhUM1pSbURRVl81alp0UElScC1rVFlYVHpqMnVUS3M5MUdJeEpKcThUTW1mV3RpMlUwcVROOWFV?oc=5) ⭐️ 8.0/10

谷歌发布了 LiteRT.js，这是 LiteRT 的 JavaScript 绑定，允许通过 WebGPU API 在网页浏览器中直接运行.tflite 机器学习模型，实现硬件加速。 这为 Web 应用带来了高性能的端侧 AI 推理能力，开发者无需手动调整平台即可在 Android、iOS 和 Web 上共享模型，提升隐私性和响应速度。 LiteRT.js 是 Google AI Edge 的一部分，支持多框架模型，包括从 PyTorch 的简化转换。它抽象了硬件级优化，利用 WebGPU 在浏览器中实现 GPU 加速。

google_news · MarkTechPost · 7月15日 07:36

**背景**: LiteRT 是谷歌的轻量级端侧机器学习运行时，前身为 TensorFlow Lite。WebGPU 是一种现代 Web 标准，提供底层 GPU 访问，取代了 WebGL。.tflite 是 TensorFlow Lite 和 LiteRT 使用的模型格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.googleblog.com/litertjs-googles-high-performance-web-ai-inference/">LiteRT . js , Google's high performance Web AI Inference</a></li>
<li><a href="https://ai.google.dev/edge/litert/web?trk=article-ssr-frontend-pulse_little-text-block">LiteRT for Web with LiteRT . js | Google AI Edge | Google AI for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU</a></li>

</ul>
</details>

**标签**: `#Google`, `#LiteRT.js`, `#WebGPU`, `#Machine Learning`, `#JavaScript`

---

<a id="item-19"></a>
## [构建 Shippy AI 智能体的经验教训](https://huggingface.co/blog/allenai/shippy-tech-blog) ⭐️ 7.0/10

Ai2 发布了一篇博客文章，详细介绍了构建 Shippy（一个用于海洋领域感知的 AI 智能体）的设计决策、挑战和经验教训。 这为 AI/ML 从业者提供了构建可靠智能体的实用、真实世界见解，强调确定性工具和护栏比模型本身更重要。 Shippy 基于 Ai2 的 Skylight 海洋监测平台构建，使用实时船只数据回答自然语言问题。博客强调，可靠智能体依赖于确定性工具、显式护栏、隔离基础设施以及基于真实工作流的评估。

rss · Hugging Face Blog · 7月15日 17:29

**背景**: AI 智能体是使用大语言模型通过调用工具和推理来自主执行任务的软件系统。构建生产级智能体面临可靠性、安全性和与实时数据源集成等挑战。Shippy 是由艾伦人工智能研究所为海洋分析师推出的免费 AI 智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://allenai.org/blog/shippy-deep-dive">What building Shippy taught us about building agents | Ai2</a></li>
<li><a href="https://www.geekwire.com/2026/ai2s-skylight-project-launches-shippy-an-ai-agent-that-dives-into-ocean-data/">Ai2’s Skylight project launches ‘Shippy,’ an AI agent that ...</a></li>
<li><a href="https://skylight.global/news/shippy-launch">Meet Shippy: Agent Built for Ocean Intelligence</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#practical insights`, `#Hugging Face`, `#software engineering`, `#machine learning`

---

<a id="item-20"></a>
## [AI 编程工具让软件变得可丢弃](https://seths.blog/2026/07/disposable-software/) ⭐️ 7.0/10

Seth Godin 认为，像 Claude Code 这样的 AI 编程助手正在将软件从长期耐用的资产转变为快速构建并丢弃的产物，他将这一转变称为“可丢弃软件”。 这一转变可能从根本上改变软件工程实践、项目经济以及开发者的角色，因为创建软件的成本下降，重点从维护转向快速迭代。 Godin 的文章特别提到 Anthropic 的代理式编码工具 Claude Code 是这一趋势的关键推动者，但这一论点广泛适用于能够以最少人力生成、修改和部署代码的 AI 辅助开发工具。

rss · Seth Godin · 7月15日 09:03

**背景**: 传统上，软件被视为耐用资产，因为构建和维护需要大量时间和专业知识。像 Claude Code 这样的 AI 编程助手能够理解代码库、编辑文件并运行命令，大幅减少了创建和修改软件所需的工作量，使得快速构建和丢弃应用程序变得可行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#software engineering`, `#software lifecycle`, `#Claude Code`

---

<a id="item-21"></a>
## [RK3576 NPU 支持加入开源 Rocket 驱动](https://news.google.com/rss/articles/CBMizwFBVV95cUxOUVNsUHIxeXZLV1dZU0k0dG0xMzJlQU5PNGJpMVBQZmJ2dXVTam4tbUpiWlJzS0ZZMXpHUGI1SGwwM0pvcWVpS1RlTXFNWkNmdXBzdE9fRy1XSFBYdS1mS20zLUxEMkJzazVGbUZmakJ0Uk91N3NfQlN3RG1NQzhLeURtd1l4cTJpRmlwR1BKam9mR1JYd3dYOEJUU0RRWi1paDRBVjVMY195cGhjY29KR1ZuZm1NMVJRMkZlc0VmUlloNmRzZHR0MmdwZDNTYmfSAdcBQVVfeXFMTU1DZWM5MGg5LWNweW05YmE4NDhLaGFJR2dIMFl5QmNwSFlKc1FxYy1mZk5jRnNMVG8tYVpzTnROc0JnOTNQYVlOMFNQM21LdUlubHFWaFFJVHBEWVg4S05lRHBTb1l6Y1RpalFZWGRKOGx0amllc0ZCTGpvYm90RVBaU3FYN2N5SDR4bldmdEZmTmhOMnZ4QnpJN2xXeTg2dXVmT01DSTgwTWlJY01Ic1VDM0NYOEJBR3FXeUc2VWRuVXNsQ3gySl9JeldjdUJMdHZKVU1kQ1k?oc=5) ⭐️ 7.0/10

通过逆向工程，开源 Rocket 驱动已为主线 Linux 中的 Rockchip RK3576 芯片添加了神经网络处理器（NPU）支持。 这为 RK3576 带来了开源 NPU 加速，使得运行主线 Linux 的边缘设备无需专有驱动即可高效进行 AI 推理。 RK3576 的 NPU 提供高达 6 TOPS 的 AI 性能，Rocket 驱动通过逆向工程代码支持该 NPU，从而允许使用 TensorFlow 和 PyTorch 等框架。

google_news · CNX Software · 7月15日 05:01

**背景**: Rocket 驱动是一个用于 Rockchip NPU 的开源 Linux 内核驱动，最初为 RK3399Pro 和 RK3588 等旧芯片开发。RK3576 是一款较新的 SoC，配备 6 TOPS NPU，但在此之前缺乏主线 Linux 支持。由于 Rockchip 未提供 NPU 的开放文档，因此需要进行逆向工程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wiki.t-firefly.com/en/Core-3576JD4/usage_npu.html">2. NPU — Firefly Wiki</a></li>

</ul>
</details>

**标签**: `#Linux`, `#NPU`, `#reverse-engineering`, `#open-source`, `#RK3576`

---