---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 102 items, 16 important content pieces were selected

---

1. [Grok Build CLI Uploads Entire Repos to xAI](#item-1) ⭐️ 9.0/10
2. [RISCBoy: Open-Source RISC-V Portable Game Console](#item-2) ⭐️ 8.0/10
3. [Nvidia's Circular Financing in GPU Boom](#item-3) ⭐️ 8.0/10
4. [Zhipu Founder Tang Jie's Internal Letter: Pivot to Coding and Reasoning](#item-4) ⭐️ 8.0/10
5. [Meta Shuts Down Controversial AI Image Feature](#item-5) ⭐️ 8.0/10
6. [China's Orca World Model Matches Specialized Robotics Without Action Labels](#item-6) ⭐️ 8.0/10
7. [China may restrict overseas access to top AI models](#item-7) ⭐️ 8.0/10
8. [Embodied Data Industry: 97 Players, 4.47B Funding in One Year](#item-8) ⭐️ 7.0/10
9. [Mistral AI Launches Single-Camera Navigation Model](#item-9) ⭐️ 7.0/10
10. [Ant Group Open-Sources Robot Brain Outperforming pi0.5](#item-10) ⭐️ 7.0/10
11. [Mozilla.ai Launches Otari, Open-Source LLM Control Plane](#item-11) ⭐️ 7.0/10
12. [GitHub API Abuse: 50+ Ghost Accounts in Recon Operation](#item-12) ⭐️ 7.0/10
13. [Ghostcommit Attack Hides Malicious Prompts in Images](#item-13) ⭐️ 7.0/10
14. [SK Hynix CEO Predicts HBM Prices to Double by 2027](#item-14) ⭐️ 6.0/10
15. [Samsung Advances Yongin Chip Fab Launch to 2029](#item-15) ⭐️ 6.0/10
16. [Nvidia Brings Robotics AI to Hugging Face](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Grok Build CLI Uploads Entire Repos to xAI](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 9.0/10

A security researcher discovered that xAI's Grok Build CLI uploads the entire repository contents, including .env secrets and git history, to xAI servers regardless of what the agent reads. This raises serious privacy and security concerns for developers using Grok Build, as sensitive data like API keys and credentials could be exfiltrated without their knowledge. The upload includes every tracked file and the full git history, independent of what the agent reads, meaning even files not accessed by the AI are sent to xAI servers.

hackernews · jhoho · Jul 12, 01:09 · [Discussion](https://news.ycombinator.com/item?id=48877371)

**Background**: Grok Build is xAI's terminal-native AI coding agent launched in beta in May 2026. It is designed to assist developers with coding tasks directly from the command line. Data exfiltration is a known security concern where sensitive data is transferred without authorization.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build Beta | SpaceXAI</a></li>
<li><a href="https://attack.mitre.org/tactics/TA0010/">Exfiltration , Tactic TA0010 - Enterprise | MITRE ATT&CK</a></li>

</ul>
</details>

**Discussion**: Community comments express shock and concern, with users noting that this behavior undermines trust in xAI. Some users suggest sandboxing tools to mitigate risks, while others compare this to practices of other AI coding tools like Codex and Claude Code.

**Tags**: `#privacy`, `#security`, `#AI tools`, `#xAI`, `#data exfiltration`

---

<a id="item-2"></a>
## [RISCBoy: Open-Source RISC-V Portable Game Console](https://github.com/Wren6991/RISCBoy) ⭐️ 8.0/10

Luke Wren, an ASIC design engineer at Raspberry Pi, has released RISCBoy, an open-source portable game console built from scratch using the RISC-V instruction set architecture. This project demonstrates the viability of RISC-V in consumer electronics and provides a fully open-source hardware platform for retro gaming enthusiasts and embedded developers. RISCBoy is described as a 'Gameboy Advance from a parallel universe where RISC-V existed in 2001,' and it includes open-source AHB/APB bus implementations, which are typically associated with ARM's proprietary ecosystem.

hackernews · mariuz · Jul 11, 21:58 · [Discussion](https://news.ycombinator.com/item?id=48876245)

**Background**: RISC-V is a free and open standard instruction set architecture (ISA) based on RISC principles, developed at UC Berkeley in 2010. Unlike proprietary ISAs like ARM and x86, RISC-V allows anyone to design processors without paying royalties. Open-source hardware projects like RISCBoy enable full transparency and community collaboration in hardware design.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V_architecture">RISC-V architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open-source_hardware">Open-source hardware - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community is highly positive, praising Luke Wren's engineering skills and the project's nostalgic appeal. Some commenters noted the significance of open-sourcing AHB/APB components, which are usually considered ARM-proprietary.

**Tags**: `#RISC-V`, `#open-source hardware`, `#gaming console`, `#embedded systems`

---

<a id="item-3"></a>
## [Nvidia's Circular Financing in GPU Boom](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 8.0/10

An analysis reveals that Nvidia's investments in CoreWeave and Nebius may involve circular financing, where Nvidia invests in GPU cloud startups that then use the funds to buy Nvidia hardware, potentially inflating demand. This pattern raises concerns about the sustainability of the GPU boom and whether demand is genuine or artificially amplified, affecting investors and the broader AI infrastructure ecosystem. Nvidia invested $2 billion for a 9% stake in CoreWeave, while CoreWeave plans $35 billion in CapEx in 2026, meaning Nvidia's investment covers only 5.7% of that year's spending. The rest comes from other sources, suggesting the circularity may be overstated.

hackernews · adletbalzhanov · Jul 11, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48873836)

**Background**: Circular financing occurs when a company invests in customers who then use the funds to buy the investor's products, creating a feedback loop that can inflate revenue. In AI, Nvidia's investments in GPU cloud providers like CoreWeave and Nebius have sparked debate about whether this practice is artificially boosting GPU demand.

<details><summary>References</summary>
<ul>
<li><a href="https://www.buildthisnow.com/blog/guide/mechanics/is-ai-a-bubble">Is AI a Bubble? ' Circular Financing ' in Plain English | Build This Now</a></li>
<li><a href="https://factually.co/fact-checks/finance/is-ai-circular-financing-inflating-a-bubble-670512">Is AI’s Circular Financing Inflating a Bubble?</a></li>

</ul>
</details>

**Discussion**: Commenters debate the significance of circular financing: some argue Nvidia's investment is small relative to CoreWeave's total CapEx, while others focus on profitability metrics like ROI per token and enterprise token budgets. There is also discussion about Nvidia's strategic hedging against hyperscalers.

**Tags**: `#GPU`, `#financing`, `#Nvidia`, `#cloud computing`, `#AI infrastructure`

---

<a id="item-4"></a>
## [Zhipu Founder Tang Jie's Internal Letter: Pivot to Coding and Reasoning](https://36kr.com/p/3891132709206784?f=rss) ⭐️ 8.0/10

Zhipu AI founder Tang Jie published an internal letter on July 11, 2026, revealing the company's strategic pivot to AI Coding and Reasoning, which led to a 10x market cap increase and the release of the open-source GLM-5.2 model that rivals GPT-5.5 and Claude Opus 4.8. This signals a major shift in the AI industry towards coding and reasoning as the next frontier, with Zhipu's success demonstrating that betting on these capabilities can yield both technical leadership and commercial returns. Zhipu's MaaS platform ARR reached 1.7 billion RMB by March 2026, a 60x increase year-over-year. The company's GLM-5.2 model has 744B parameters with 40B active and a 1M-token context window, and is open-sourced under MIT license.

rss · 36氪 · Jul 11, 11:28

**Background**: Zhipu AI, founded by Tsinghua professor Tang Jie, has been developing large language models for nearly a decade. The company went public on the Hong Kong Stock Exchange in January 2026. After DeepSeek R1's release in early 2025, Zhipu shifted focus from chat to coding and reasoning, a bet that paid off as AI coding became the most commercializable AI capability.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/GLM-5.2 · Hugging Face</a></li>
<li><a href="https://the-decoder.com/zhipu-ais-glm-5-2-closes-in-on-closed-source-leaders-in-coding-marathons/">Zhipu AI's GLM-5.2 closes in on closed-source leaders in coding marathons</a></li>
<li><a href="https://the-decoder.com/zhipu-ais-glm-5-1-can-rethink-its-own-coding-strategy-across-hundreds-of-iterations/">Zhipu AI's GLM-5.1 can rethink its own coding strategy across hundreds of iterations</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Coding`, `#Zhipu`, `#Strategy`, `#LLM`

---

<a id="item-5"></a>
## [Meta Shuts Down Controversial AI Image Feature](https://36kr.com/newsflashes/3891995047033351?f=rss) ⭐️ 8.0/10

Meta has removed a new AI image generation feature that allowed users to reference public Instagram posts via @mentions to create AI-generated images, following widespread backlash over privacy and legal concerns. This incident highlights the growing tension between AI innovation and user privacy rights, and could influence future regulations on how social media platforms use public content for AI training and generation. The feature was enabled by default for public Instagram accounts, meaning users had to proactively opt out to prevent their content from being used. Critics, including SAG-AFTRA, raised concerns about likeness rights and potential criminal misuse.

rss · 36氪 · Jul 12, 02:20

**Background**: AI image generation tools like DALL-E and Midjourney have raised privacy concerns when trained on public web data. Meta's feature went a step further by allowing real-time referencing of specific Instagram posts, amplifying risks of unauthorized use of individuals' likenesses.

<details><summary>References</summary>
<ul>
<li><a href="https://petapixel.com/2026/07/10/meta-removes-ai-image-generation-feature-that-used-public-instagram-posts-following-user-backlash/">Meta Removes AI Image Generation Feature That Used Public ...</a></li>
<li><a href="https://9to5mac.com/2026/07/10/meta-removes-feature-that-let-users-generate-ai-images-from-public-instagram-posts/">Meta removes feature that let users generate AI images from public ...</a></li>
<li><a href="https://www.computing.co.uk/news/2026/meta-under-fire-over-ai-image-tool-that-uses-public-instagram-pics">Meta under fire over AI image tool that uses public Instagram pics</a></li>

</ul>
</details>

**Tags**: `#AI`, `#privacy`, `#Meta`, `#social media`, `#ethics`

---

<a id="item-6"></a>
## [China's Orca World Model Matches Specialized Robotics Without Action Labels](https://news.google.com/rss/articles/CBMixgFBVV95cUxPSUFhYnBGNkJtUU1JTHhZbThBRnAxcGhlMWhiNmhEQllFTll3RFVMUTZBSHQ4TWg5SE5jaTBqLU5ITnVxUVhQRkk5dzhRZzh4a2FtUWxyTHVTMTFVb2p1UTFoZmNfYnZjR0Q2d2R3VnpodGhBdzJkRmdjZkw3QjZlOVR6ZlBQVXhBeWpoRTJmZTNkNmdNVXp3eEM5UTNSdm0xdUlYaW83RGp5MEd1VXluUWNkd09sQTk1RHB0eXk2dE1EcklNa2c?oc=5) ⭐️ 8.0/10

The Beijing Institute of Artificial Intelligence (BAAI) unveiled the Orca world model, which achieves performance comparable to specialized robotics systems without ever using action labels during training. This breakthrough reduces the need for expensive and time-consuming action annotation in robotics, potentially accelerating the development of general-purpose robots and lowering data barriers for AI research. Orca uses a next-state prediction paradigm that scales effectively with model size and data, yielding a stronger world latent that improves downstream tasks like text generation, image prediction, and action planning.

google_news · the-decoder.com · Jul 11, 09:07

**Background**: World models are AI systems that learn an internal representation of the environment to predict future states. Traditional robotics models often require action labels—annotations of what action the robot is performing—to learn control policies. Orca bypasses this by learning purely from observational data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/orca">Orca : Unified Multimodal AI and Robotics</a></li>
<li><a href="https://hyper.ai/en/papers/2606.30534">Orca : The World is in Your Mind | Papers | HyperAI</a></li>
<li><a href="https://en.youth.cn/RightNow/202607/t20260708_16753288.htm">BAAI Releases RoboBrain Orca World Model _English__China Youth...</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#world model`, `#AI`, `#machine learning`, `#China`

---

<a id="item-7"></a>
## [China may restrict overseas access to top AI models](https://news.google.com/rss/articles/CBMidkFVX3lxTFBqaGRmWFlQdGxQcHVZOF94WTZOdEg3VERvNTMwSHlkMFhnazUyNFAwUmRyaHg5bkk4b1pGc2d6MWp3T1VfeEpYNFJySldkZ0ZnSFNqZUROR19MQmRDMXpyMktuTTlVdGktRFhWZmxsV2tZTmFtNmc?oc=5) ⭐️ 8.0/10

Beijing is considering curbing overseas access to China's top AI models, according to a Taipei Times report. This potential policy change could limit global developers' ability to use Chinese AI technologies. This move could reshape the global AI landscape by reducing cross-border access to Chinese AI innovations, potentially slowing international AI development and intensifying geopolitical tech competition. It may also affect companies and researchers who rely on Chinese open-source models. The report does not specify which models would be affected or the timeline for implementation. The policy would likely target advanced AI models developed by Chinese companies like Baidu, Alibaba, and Tencent.

google_news · Taipei Times · Jul 11, 16:00

**Background**: China has been rapidly advancing in AI, with models like Ernie Bot and Qwen gaining global attention. Currently, many Chinese AI models are available to international developers via open-source licenses or APIs. Restricting access would mark a significant shift toward protecting domestic AI assets.

**Tags**: `#AI regulation`, `#geopolitics`, `#China`, `#AI models`, `#technology policy`

---

<a id="item-8"></a>
## [Embodied Data Industry: 97 Players, 4.47B Funding in One Year](https://36kr.com/p/3892027841362694?f=rss) ⭐️ 7.0/10

A comprehensive analysis by QuantumBit reveals 97 domestic embodied data players, with 15 independent data service providers raising approximately 4.47 billion yuan in the past year (July 2025 to July 2026). The industry has matured into four main data collection technical routes: real-robot teleoperation, no-robot collection, simulation synthesis, and internet video distillation. This analysis marks the first systematic mapping of China's embodied data industry, showing it has become an independent track separate from robotics companies. The findings highlight the critical role of data in training embodied AI models and the diverse approaches being pursued to solve the data scarcity problem. Among the 97 players, 70 focus on data collection and 27 on data infrastructure. Independent data service providers form the largest group (39 companies, 40%), followed by state-owned data platforms (25, 26%). Notably, 67% of players are 'embodied-native' startups, while 33% are cross-sector transformers from fields like AI data labeling or autonomous driving.

rss · 36氪 · Jul 12, 02:16

**Background**: Embodied AI requires vast amounts of real-world interaction data for training, which is currently scarce and expensive to collect. Common collection methods include teleoperation (humans controlling robots), no-robot collection (humans performing tasks with sensors), simulation (generating synthetic data), and distilling knowledge from internet videos. The industry is still in its early stages, with no single method proving sufficient.

<details><summary>References</summary>
<ul>
<li><a href="https://juejin.cn/post/7639399482463830026">绕不开的Ego-centric...</a></li>
<li><a href="https://www.21jingji.com/article/20260421/herald/acb40065512b137c5d49d7aac259c043.html">数 据 成机器人落地关键， 具 身 数 据 集 赛道火热 - 21经济网</a></li>
<li><a href="https://tech.ifeng.com/c/8uh5s4oHQ2h">tech.ifeng.com/c/8uh5s4oHQ2h</a></li>

</ul>
</details>

**Tags**: `#embodied AI`, `#data collection`, `#robotics`, `#funding`, `#industry analysis`

---

<a id="item-9"></a>
## [Mistral AI Launches Single-Camera Navigation Model](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBuODdfOFZITFJmb0FyNW00TkZEdUtFYzVxWnV5bWxCY1dRc3hnVjdFUVpqNHRnWDBGVUMzYXViZ1ViVEVCR216YzNOZ0lDbXZHMGNnUW93?oc=5) ⭐️ 7.0/10

Mistral AI has announced Robostral Navigate, an 8B vision-language-action model that enables robots to navigate complex environments using only a single RGB camera and natural language instructions. This approach reduces hardware costs and simplifies robot design, potentially accelerating the deployment of autonomous robots in warehouses, homes, and other settings where depth sensors are impractical. Robostral Navigate achieves a 76.6% success rate on unseen environments, and the model is designed to follow plain-language instructions for embodied navigation tasks.

google_news · mistral.ai · Jul 12, 03:02

**Background**: Traditional robot navigation often relies on multiple cameras or expensive depth sensors like LiDAR. Vision-language-action models combine visual perception, language understanding, and motor control into a single neural network, enabling more intuitive human-robot interaction.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/news/robostral-navigate/">Robostral Navigate : single-camera AI navigation | Mistral AI</a></li>
<li><a href="https://www.youtube.com/watch?v=7dpLB9NoY1A">Introducing Robostral Navigation - YouTube</a></li>
<li><a href="https://quasa.io/media/mistral-robostral-navigate-single-camera-8b-model-transforms-robot-autonomy">Mistral Robostral Navigate : Single-Camera Robot Autonomy in 2026</a></li>

</ul>
</details>

**Tags**: `#AI`, `#navigation`, `#robotics`, `#computer vision`

---

<a id="item-10"></a>
## [Ant Group Open-Sources Robot Brain Outperforming pi0.5](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOTGctdHQtSWdvbEFSVXlaWE9qSmFPUjVqWHB1d0lBMDFQWE5kcjd0OGt0WmpUVzZCRWNzVUNVX3pFYW1zc2lJaWswbmZmejlJVGNEOVdzamJGMUtlOXNZQkpNMEd4bWtxVEdpSDMwUjB0TncyU3RfWWJ3cWUzcWFBcVRnZ0lJcWtHWGFSSENvVF91WS1EU3liS21MejNHQTJZalNWZ1dFS2RiWm92M0F5ZGJwQ1FVZmhjWlZtQ1ZJMzlLT1U?oc=5) ⭐️ 7.0/10

Ant Group has open-sourced a universal robot brain that outperforms pi0.5 across 20 different hardware types, marking a significant step in embodied AI. This open-source release could accelerate robotics development by providing a high-performing, hardware-agnostic AI brain, reducing the need for custom solutions and lowering barriers to entry for researchers and developers. The robot brain is part of Ant Group's Robbyant embodied-AI stack, which includes perception and a universal brain. It was open-sourced in just a week, showcasing rapid development.

google_news · Tech Times · Jul 11, 15:00

**Background**: Embodied AI refers to AI systems that can interact with the physical world through a robot body. pi0.5 is a previous state-of-the-art robot AI model. Ant Group, backed by Jack Ma, has been expanding into robotics, recently unveiling the R1 humanoid robot.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scmp.com/tech/big-tech/article/3341842/ant-groups-open-source-push-aims-move-robots-lab-demos-real-world-work">Ant Group's open-source push aims to move robots from lab demos to real ...</a></li>
<li><a href="https://thenextweb.com/news/robbyant-ant-group-lingbot-embodied-ai-open-source">Ant Group open-sourced a whole robot brain in a week - TNW</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#open-source`, `#AI`, `#hardware`

---

<a id="item-11"></a>
## [Mozilla.ai Launches Otari, Open-Source LLM Control Plane](https://news.google.com/rss/articles/CBMimAFBVV95cUxNRWdQNjJ5VDRwNWswcWtocHN5T2t0OERrSUM3M0oyS1BFbkpDSWdobzFaeHBSLWJWS01vUTJPRi1pb3l3QkJQRkY1TmM4SlF4dEhLR29jdUdyb1VpbjU4aDc5bFFJeTFhenpXR3ZtRFRXb3FrRjlfNlBocF9scnIzYUtCV1VndWtIMzZOSVhMY1U4dXJNVWFNcw?oc=5) ⭐️ 7.0/10

Mozilla.ai has launched Otari, an open-source control plane for managing large language model (LLM) operations, including routing, budgets, governance, and deployment across multiple providers. Otari addresses the lack of a dedicated control plane for LLM traffic, enabling developers and engineering teams to manage LLM infrastructure more efficiently and safely, which could accelerate enterprise adoption of LLMs. Otari provides hosted guardrails for LLM safety, smart routing to choose the best model (local or remote) per request, and optional code execution on otari.ai. It is built on top of any-llm and is open-source.

google_news · StartupHub.ai · Jul 11, 19:23

**Background**: An LLM control plane is a centralized system that manages routing, security, and governance for LLM requests, similar to API gateways but purpose-built for generative AI workloads. Until now, no such dedicated tool existed for LLM traffic.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mozilla.ai/product/otari">Otari : A centralized control plane for LLM operations</a></li>
<li><a href="https://blog.mozilla.ai/introducing-otari-the-open-source-llm-control-plane/">Introducing Otari : The Open-Source LLM Control Plane</a></li>
<li><a href="https://blog.mozilla.ai/what-is-an-llm-control-plane/">What is an LLM control plane ?</a></li>

</ul>
</details>

**Tags**: `#Mozilla`, `#LLM`, `#control plane`, `#AI infrastructure`

---

<a id="item-12"></a>
## [GitHub API Abuse: 50+ Ghost Accounts in Recon Operation](https://news.google.com/rss/articles/CBMifkFVX3lxTE9vVF9iWmMxMFA0N0Z1U2gyUFgyWFh2ZjZUbEU0RkFpaDVCcFZHZXcyTEh5VncxVWJUMUFMcTdkZllEUWdWTUhXX25QNzlmX0J4eFZQaTc2VEpZNVJ5SDNyT1hxR1VyTElpdkw5NEJ0dGx2VHZ2b3l4UHR5TW5ndw?oc=5) ⭐️ 7.0/10

Security researchers have uncovered a large-scale reconnaissance campaign where over 50 ghost accounts abused the GitHub API to discover organizations' repositories and members. This highlights a growing trend of API abuse for intelligence gathering, posing risks to organizations' data privacy and security on collaborative platforms like GitHub. The ghost accounts operated in a coordinated manner to scrape repository metadata and member lists, potentially for targeted attacks or competitive intelligence.

google_news · SecNews.gr · Jul 11, 17:49

**Background**: GitHub is a widely used platform for software development and collaboration, hosting millions of repositories. Ghost accounts are fake or compromised accounts used to evade detection. API abuse involves exploiting legitimate interfaces to extract data beyond intended limits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.securityweek.com/ghost-accounts-abuse-github-api-in-mass-recon-campaign/">Ghost Accounts Abuse GitHub API in Mass Recon ... - SecurityWeek</a></li>

</ul>
</details>

**Tags**: `#GitHub`, `#API abuse`, `#security`, `#reconnaissance`

---

<a id="item-13"></a>
## [Ghostcommit Attack Hides Malicious Prompts in Images](https://news.google.com/rss/articles/CBMicEFVX3lxTE1mcXBSQlU4dFpheUQtVmNCeUNaX3VTVmZIaDI3QklxYTlHU2RTSjJtVjZoWkRpQWpSdmJYelllNi0xVVNjZkFCSlF4UG5LODd0RjBBdEZjb3EtODl1MGl2X0x2a0NxN3VHMVVqTWtaX2PSAbsCQVVfeXFMT2ctQ0tfU2JmQU54NHVZMnlENE1kZHBMeEQ3dF9RRVhlYzN2SHZrSnpJSUxneVJkbnUwM3dzYU8zbGJ5MmJJcEVTQTVzTXFRS0VLekNFM3ROTFZOMXhuZ3REdDI0bHBJRkpwdEtySjFvUVIwVnFuS2FoOS1wVENXdmhvTlcwdjVMQ1Q4eDJWNHBKbkxSamtaSVJzTTRQVHhaYkVpRlNMNkN2SG80cl90ZG9zejNVNGdTdWJUenVDR3Q4MXZycGcwRHVkRi0zRnNOTnZwUHpjeWs3ejM4MWdMc3JwSkV3Ni03OHBHR0RlRmZld3ZuZTZMTVlzeUtrekVWeWluYTM3cFRjTVRwOTVzQVJkZUhKQ0VZYmloaTNxX1Fpd2lQYjBCcHFFY0JZZjZNNHAtUkxGWGFmZVVV?oc=5) ⭐️ 7.0/10

Researchers have discovered a novel supply chain attack called Ghostcommit that uses steganography to embed malicious prompt-injection instructions within PNG images, targeting AI code reviewers and coding agents. This attack represents a new vector for exploiting AI agents, bypassing traditional security measures and potentially leading to secret leakage or unauthorized actions in CI/CD pipelines. The attack embeds prompt-injection instructions in image files that are processed by AI agents, such as code reviewers, which then execute the hidden commands. It highlights the growing threat of steganographic attacks in AI security.

google_news · CyberSecurityNews · Jul 11, 16:30

**Background**: Prompt injection is a type of attack where malicious instructions are inserted into AI model inputs to alter its behavior. Steganography is the practice of hiding data within other data, such as images. Ghostcommit combines these techniques to target AI agents in software development workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/ghostcommit-attack-hides-prompts/">New Ghostcommit Attack Hides Malicious Prompts in Images to...</a></li>
<li><a href="https://europeanpurpose.com/news/ghostcommit-the-ai-prompt-injection-attack-hiding-inside-your-repository-s-image">Ghostcommit : The AI Prompt Injection Attack ... | European Purpose</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#prompt injection`, `#steganography`, `#cybersecurity`, `#adversarial attack`

---

<a id="item-14"></a>
## [SK Hynix CEO Predicts HBM Prices to Double by 2027](https://36kr.com/newsflashes/3892093059873544?f=rss) ⭐️ 6.0/10

SK Hynix CEO Kwak Noh-jung predicted that HBM prices will double by 2027 due to supply constraints and strong demand, and noted that customers are seeking long-term supply agreements. This forecast signals a prolonged tight supply for HBM memory critical for AI accelerators, potentially impacting AI infrastructure costs and timelines. It also highlights the growing competitive threat from Chinese memory makers like ChangXin Memory Technologies (CXMT) and YMTC. SK Hynix controls 62% of global HBM shipments and sold out its entire 2026 production by mid-2025. The company has committed approximately $13 billion for a new plant and $10 billion for a U.S.-based AI investment arm.

rss · 36氪 · Jul 12, 03:58

**Background**: High Bandwidth Memory (HBM) is an advanced memory technology that stacks DRAM dies vertically using Through-Silicon Vias (TSVs) to achieve ultra-high bandwidth, essential for AI and graphics workloads. SK Hynix is the leading supplier of HBM, but Chinese memory manufacturers are rapidly expanding production capacity, which could reshape the global memory market.

<details><summary>References</summary>
<ul>
<li><a href="https://en.sedaily.com/finance/2026/04/23/sk-hynix-says-hbm-demand-to-outstrip-supply-for-next-3-years">SK hynix Says HBM Demand to Outstrip Supply for Next 3 Years</a></li>
<li><a href="https://nextwavesinsight.com/hbm-memory-bottleneck-ai-supply-chain-2026/">HBM 's Thermal Wall: Why One Korean... - Next Waves Insight</a></li>
<li><a href="https://www.astutegroup.com/news/memory-shortages/chinas-memory-expansion-reshapes-global-dram-and-nand-competition/">China ’s memory expansion reshapes global DRAM... - Astute Group</a></li>

</ul>
</details>

**Tags**: `#HBM`, `#memory`, `#semiconductor`, `#SK Hynix`, `#supply chain`

---

<a id="item-15"></a>
## [Samsung Advances Yongin Chip Fab Launch to 2029](https://36kr.com/newsflashes/3892091542288904?f=rss) ⭐️ 6.0/10

Samsung Electronics plans to accelerate the production start of its first chip factory in Yongin to 2029, one to two years earlier than originally scheduled, to meet growing AI chip demand. This acceleration allows Samsung to respond faster to the surging global demand for AI chips, strengthening its competitive position in the semiconductor market against rivals like TSMC and SK Hynix. The Yongin cluster is part of Samsung's broader investment plan, which includes 2,030 trillion won (about $1.35 trillion) for Pyeongtaek and Yongin clusters, plus 400 trillion won for two new fabs in Gwangju.

rss · 36氪 · Jul 12, 03:39

**Background**: Samsung Electronics is a global leader in semiconductor manufacturing, producing memory chips and logic chips. The Yongin cluster is a major expansion project aimed at boosting production capacity for advanced chips, especially AI accelerators. Accelerating the timeline reflects the intense competition in the AI chip market.

**Tags**: `#Samsung`, `#semiconductor`, `#AI chips`, `#manufacturing`

---

<a id="item-16"></a>
## [Nvidia Brings Robotics AI to Hugging Face](https://news.google.com/rss/articles/CBMiywFBVV95cUxONkNhcF82TzdWOUpRU2RsNGpEQTIxMnNSZko1RlhGUUwxNE9qUWFFR1N2Q1lKak5WWFFCNWRITGlwWUFCR01nNW1adjVmSDAxN0hGLTJQSnc0SnJGZGc3NEJ3VzVpNHhobGZBZGpLejJXcnFkZWZ3Z3l4dFlBX2RRWC1WVnRaOXBSUEtQQ0haMnhvbkRXSUV6VHYwWTl2X0FiWWoyVnMwcnRPUXlMeFp6ZGlqcXUtd2g4ZDVoNHFfV3Zkdk52eFJLREp4ONIB0AFBVV95cUxOQVFqX1RXN0Q5ZzJqQVJ4aUNuT1daTE5zT0xfVE5WMXZrcm91YUtXTDluOTdpaFVyUk5Sa2xKdmN3b09tWmRZcm82M0I3OTBtbnNxNXBBWERLVnpMUEd4RktGU1dELTZKcFJVcGFpVXViWHVGOWg4OUI4LTVSTjZJa1B0dzVQd05uSTRlb1RmMFZUZ1lWMmJlOThMTWZOanRmZ2U1d3hzOXFvSWZjYjRNTkdfLXpUVlRVYURpTnVMZHpqa1JBY2M0a0xTMDFyNldM?oc=5) ⭐️ 6.0/10

Nvidia has partnered with Hugging Face to integrate its robotics AI capabilities into the Hugging Face platform, coinciding with the conclusion of a French antitrust probe into Nvidia. This partnership democratizes access to advanced robotics AI tools, enabling developers and researchers to build and deploy AI-powered robots more easily using Hugging Face's ecosystem. The integration likely leverages Nvidia's Isaac platform and Hugging Face's LeRobot library, which provides datasets and tools for robotics AI. The French probe's end removes regulatory uncertainty for Nvidia's operations in Europe.

google_news · simplywall.st · Jul 11, 14:45

**Background**: Hugging Face is a popular platform for sharing machine learning models and datasets, and it recently released SmolVLA, an open-source robotics model. Nvidia provides hardware and software for AI and robotics, including the Isaac platform for simulation and deployment. The partnership aims to combine Nvidia's robotics expertise with Hugging Face's community-driven model sharing.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/learn/robotics-course/unit0/1">Welcome to the Robotics Course · Hugging Face</a></li>
<li><a href="https://github.com/huggingface/lerobot">GitHub - huggingface/lerobot: LeRobot: Making AI for Robotics ...</a></li>
<li><a href="https://techcrunch.com/2025/06/04/hugging-face-says-its-new-robotics-model-is-so-efficient-it-can-run-on-a-macbook/">Hugging Face says its new robotics model is so... | TechCrunch</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#Hugging Face`, `#robotics AI`, `#partnership`

---