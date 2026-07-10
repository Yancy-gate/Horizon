---
layout: default
title: "Horizon Summary: 2026-07-10 (EN)"
date: 2026-07-10
lang: en
---

> From 95 items, 12 important content pieces were selected

---

1. [AI Generates Videos to Maximally Activate Specific Brain Regions](#item-1) ⭐️ 9.0/10
2. [OpenAI releases GPT-5.6 family: Luna, Terra, Sol](#item-2) ⭐️ 9.0/10
3. [Semantic Alignment Outperforms VAE for Video Tokenization in Robotics](#item-3) ⭐️ 9.0/10
4. [EU: Instagram, Facebook addictive design violates DSA](#item-4) ⭐️ 8.0/10
5. [Nature Guide Compares AI Scientist Tools for Labs](#item-5) ⭐️ 8.0/10
6. [Large Study Finds Preprints Are Reliable](#item-6) ⭐️ 8.0/10
7. [Lab-grown sperm created from stem cells in mouse kidney](#item-7) ⭐️ 8.0/10
8. [NSF plans cuts to core science programs for White House initiative](#item-8) ⭐️ 8.0/10
9. [China lands reusable rocket for first time](#item-9) ⭐️ 8.0/10
10. [GoPro Bike Camera Enables Georeferenced Road Survey](#item-10) ⭐️ 8.0/10
11. [Nilay Patel: AR Glasses Require Privacy Trade-offs](#item-11) ⭐️ 7.0/10
12. [New Infrastructure Enables AI Portability Across Robots](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI Generates Videos to Maximally Activate Specific Brain Regions](https://nevo-project.epfl.ch/) ⭐️ 9.0/10

Researchers at EPFL developed NEvo, an AI system that generates videos optimized to maximally activate a target brain region, using a digital twin model trained on fMRI data. This breakthrough provides a powerful tool for neuroscience research, enabling precise mapping of brain function and potentially leading to new therapies for neurological disorders, while also raising ethical concerns about misuse in social media or advertising. The system first trains an encoding model (digital twin) that predicts brain region responses to any video, then uses that model as a reward function to search for videos that maximize activation of a chosen region. The approach reduces experimenter bias by letting the AI discover stimuli without human preconceptions.

hackernews · smusamashah · Jul 10, 07:39 · [Discussion](https://news.ycombinator.com/item?id=48856904)

**Background**: Functional magnetic resonance imaging (fMRI) measures brain activity by detecting changes in blood flow. A digital twin is a virtual model that simulates a real system; here, it predicts how visual brain regions respond to videos. NEvo uses this twin to generate novel video stimuli, advancing beyond traditional methods that rely on pre-existing videos.

<details><summary>References</summary>
<ul>
<li><a href="https://nevo.systems/">Nevo — Self-Improving AI That Evolves With You</a></li>

</ul>
</details>

**Discussion**: Commenters expressed both excitement and concern: some highlighted the potential for abuse by social media platforms to create addictive content, while others emphasized the tool's value for unbiased neuroscience research. A few noted the similarity to recent mind-reading AI and stressed the importance of reading the paper to understand the scientific intent.

**Tags**: `#AI`, `#neuroscience`, `#video generation`, `#brain-computer interface`, `#ethics`

---

<a id="item-2"></a>
## [OpenAI releases GPT-5.6 family: Luna, Terra, Sol](https://simonwillison.net/2026/Jul/9/gpt-5-6/#atom-everything) ⭐️ 9.0/10

OpenAI released the GPT-5.6 family of models on July 9, 2026, consisting of three sizes: Luna (smallest), Terra (mid), and Sol (largest). The models feature a 1M token context window, 128K output tokens, and claim strong agentic performance on the Agents' Last Exam benchmark. This release intensifies competition with Anthropic's Claude models, especially in agentic AI capabilities, and offers tiered pricing that could make advanced AI more accessible. The new API features like programmatic tool calling and multi-agent support may reshape how developers build AI-powered applications. Pricing per 1M tokens is Luna $1/$6, Terra $2.50/$15, Sol $5/$30 (input/output). On Agents' Last Exam, Sol scored 53.6, outperforming Claude Fable 5 by 13.1 points, but on SWE-Bench Pro, Fable 5 scored 80% vs Sol's 64.6%. OpenAI also published a critique of SWE-Bench Pro, estimating ~30% of its tasks are broken.

rss · Simon Willison · Jul 9, 19:46

**Background**: GPT-5.6 is OpenAI's latest flagship model family, following GPT-5.5 released two months earlier. The models are designed for agentic tasks, where AI systems autonomously perform multi-step workflows. Agents' Last Exam is a benchmark that evaluates long-horizon, economically valuable tasks with verifiable outcomes. Reasoning tokens are internal tokens used by models to plan and reason before producing a final response, and their count can vary significantly between models for the same task, making price-per-token comparisons less straightforward.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6/">GPT - 5 . 6 : Frontier intelligence that scales with your ambition | OpenAI</a></li>
<li><a href="https://arxiv.org/abs/2606.05405">Abstract page for arXiv paper 2606.05405: Agents ' Last Exam</a></li>
<li><a href="https://snorkel.ai/leaderboard/agents-last-exam/">Agents ' Last Exam | Snorkel AI</a></li>

</ul>
</details>

**Discussion**: The article author notes that GPT-5.6 Sol is competent but not yet better than Claude Fable 5 for complex coding tasks. The community may debate the validity of benchmarks like SWE-Bench Pro, especially given OpenAI's own critique.

**Tags**: `#OpenAI`, `#GPT-5.6`, `#AI models`, `#benchmarks`, `#agentic AI`

---

<a id="item-3"></a>
## [Semantic Alignment Outperforms VAE for Video Tokenization in Robotics](https://www.reddit.com/r/computervision/comments/1ustn7f/aligning_video_latents_to_a_frozen_perception/) ⭐️ 9.0/10

A new tokenizer design for robot video-action models, which adds a semantic alignment loss to pull video latents toward a frozen perception encoder (e.g., DINOv2), achieves 86.6% average success on a 50-task bimanual benchmark, compared to 78.0% with a plain reconstruction VAE. The gap widens with longer prediction horizons, reaching 92.0% vs 67.2% at horizon 3. This result demonstrates that aligning video latents to a frozen perception encoder is a simple yet powerful alternative to reconstruction-based tokenization, significantly improving long-horizon action prediction in robotics. The recipe—freezing a strong encoder as an alignment target—could generalize to other sequential prediction tasks beyond robotics. The tokenizer retains a reconstruction objective but adds a semantic alignment loss and a latent-action term that extracts compact transition variables between frames. The 78.0 to 86.6 improvement is from simulation; real-robot clips in the paper are in-house demos, not independent evidence.

reddit · r/computervision · /u/AbbreviationsEast776 · Jul 10, 17:06

**Background**: Video tokenization is a key component in robot learning, compressing video frames into latent representations for downstream action prediction. Traditional reconstruction VAEs aim to minimize pixel-level error, but may discard semantic information crucial for long-horizon tasks. Frozen perception encoders like DINOv2 provide rich semantic features without fine-tuning, and aligning latents to them preserves that information.

<details><summary>References</summary>
<ul>
<li><a href="https://www.arxiv.org/pdf/2512.04483">DeRA: Decoupled Representation Alignment for Video Tokenization Pengbo Guo1,2</a></li>
<li><a href="https://arxiv.org/abs/2410.11758">[2410.11758] Latent Action Pretraining from Videos</a></li>
<li><a href="https://arxiv.org/pdf/2504.13181">Perception Encoder: The best visual embeddings are not at ...</a></li>

</ul>
</details>

**Discussion**: The Reddit post author notes the widening gap with horizon and asks whether the same long-horizon payoff appears outside control tasks. They also caution that the main results are from simulation and real-robot demos should be viewed as demonstrations, not independent evidence.

**Tags**: `#video tokenization`, `#representation learning`, `#robotics`, `#perception encoder`, `#VAE`

---

<a id="item-4"></a>
## [EU: Instagram, Facebook addictive design violates DSA](https://ec.europa.eu/commission/presscorner/home/en) ⭐️ 8.0/10

The European Commission has preliminarily found that Meta's Instagram and Facebook platforms violate the Digital Services Act (DSA) due to their addictive design features. This marks the first major enforcement action under the DSA targeting addictive design, potentially forcing Meta to redesign core user interfaces and setting a precedent for regulating algorithmic manipulation across the EU. The preliminary finding focuses on features like infinite scroll, personalized recommendations without adequate transparency, and notification systems that exploit psychological vulnerabilities to maximize user engagement.

hackernews · jeroenhd · Jul 10, 11:00 · [Discussion](https://news.ycombinator.com/item?id=48858292)

**Background**: The Digital Services Act (DSA) is an EU regulation that came into force in 2022, requiring large online platforms to assess and mitigate systemic risks such as addictive design. Addictive design refers to UI/UX patterns intentionally crafted to prolong user engagement, often through variable rewards and attention-grabbing notifications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_Services_Act">Digital Services Act - Wikipedia</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/digital-services-act">The Digital Services Act | Shaping Europe’s digital future</a></li>
<li><a href="https://edaa.eu/digital-services-act/">What is DSA: The Digital Services Act Explained - EDAA</a></li>

</ul>
</details>

**Discussion**: Commenters debated the enforcement approach: some argued for mandating a choice between addictive and ethical algorithms, while others supported the Commission's focus on reducing addictiveness. A user noted that Instagram's algorithm reset option can help reduce doom-scrolling, and another highlighted the mismatch between engagement-optimized surfaces and dismissible time-limit popups.

**Tags**: `#regulation`, `#social media`, `#DSA`, `#addictive design`, `#EU`

---

<a id="item-5"></a>
## [Nature Guide Compares AI Scientist Tools for Labs](https://www.nature.com/articles/d41586-026-02091-6) ⭐️ 8.0/10

Nature published a guide comparing general-purpose AI tools for scientific research, such as Claude Science, to help researchers choose the right one for their lab. This guide addresses a timely need as AI tools proliferate in research, helping labs make informed decisions to accelerate scientific discovery. Claude Science is a public beta app that integrates commonly used scientific tools and packages, produces auditable artifacts, and provides flexible compute access. Other tools like Gemini for Science also offer specialized capabilities.

rss · Nature 研究亮点 · Jul 10, 00:00

**Background**: General-purpose AI tools for science, such as Claude Science, promise to accelerate research by automating tasks like data analysis and literature review. However, researchers need guidance to navigate the growing landscape of options.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://claude.com/product/claude-science">Claude Science beta | Claude by Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#science`, `#research tools`, `#Nature`

---

<a id="item-6"></a>
## [Large Study Finds Preprints Are Reliable](https://www.nature.com/articles/d41586-026-02167-3) ⭐️ 8.0/10

A Nature-commissioned analysis of 70,000 biomedical preprints reveals that their central conclusions rarely change after peer-reviewed publication, challenging common skepticism about preprint reliability. This finding supports the use of preprints for rapid dissemination of research, especially in fast-moving fields like biomedicine, and could shift researcher and public trust in open science practices. The analysis compared preprints with their final published versions across multiple biomedical journals, focusing on changes to central conclusions rather than minor textual edits.

rss · Nature 研究亮点 · Jul 10, 00:00

**Background**: Preprints are unreviewed manuscripts posted publicly before peer review. During the COVID-19 pandemic, their use surged, raising concerns about reliability. This study provides large-scale evidence that preprints are generally trustworthy.

<details><summary>References</summary>
<ul>
<li><a href="https://casrai.org/news/preprint-vs-peer-review/">Preprint vs Peer Review : What 40 Studies Show — CASRAI</a></li>
<li><a href="https://journalistsresource.org/media/two-studies-examine-preprints/">How different are preprints from their published versions?</a></li>

</ul>
</details>

**Tags**: `#preprints`, `#biomedical research`, `#open science`, `#reproducibility`, `#peer review`

---

<a id="item-7"></a>
## [Lab-grown sperm created from stem cells in mouse kidney](https://www.nature.com/articles/d41586-026-02172-6) ⭐️ 8.0/10

Scientists have successfully generated immature human sperm cells from stem cells by implanting them into a mouse's kidney, marking a step toward in vitro spermatogenesis. 这一突破最终可能帮助因遗传疾病或癌症治疗导致不育的男性产生自己的精子，提供新的生育治疗选择。 The procedure used spermatogonial stem cells (SSCs) placed in a mouse kidney, which provided the necessary microenvironment for differentiation into immature sperm. The sperm were not yet fully mature or functional.

rss · Nature 研究亮点 · Jul 10, 00:00

**Background**: Spermatogenesis is a complex process requiring specific signals from testicular cells. In vitro spermatogenesis aims to recreate this outside the body. Previous attempts have only achieved early stages; using a living organ as a bioreactor is a novel approach.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/In_vitro_spermatogenesis">In vitro spermatogenesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spermatogonial_stem_cell">Spermatogonial stem cell - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#stem cells`, `#fertility`, `#reproductive biology`, `#biotechnology`

---

<a id="item-8"></a>
## [NSF plans cuts to core science programs for White House initiative](https://www.nature.com/articles/d41586-026-02135-x) ⭐️ 8.0/10

The US National Science Foundation (NSF) has proposed cutting funding for core science programs and clawing back already distributed research funds to finance a White House initiative, amid a severe budget squeeze and a growing backlog of grant applications. This policy shift could disrupt ongoing research projects and reduce future funding opportunities for scientists across the US, potentially weakening the nation's scientific competitiveness and innovation capacity. The proposed clawback of already distributed funds is unprecedented and comes as NSF struggles with a grant backlog and reduced staff; the agency has already relaxed some grant-review rules to cope with the backlog.

rss · Nature 研究亮点 · Jul 10, 00:00

**Background**: The National Science Foundation (NSF) is a major US government agency that funds fundamental research and education in science and engineering. It has faced budget constraints in recent years, with its FY2024 enacted budget at $9.06 billion. The agency is also dealing with a backlog of grant applications and reduced staffing, leading to changes in review processes.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/d41586-025-04067-4">NSF softens grant-review rules to cope with backlog</a></li>
<li><a href="https://www.nsf.gov/resumption-operations">Resumption of Operations at NSF | NSF - U.S. National Science Foundation</a></li>

</ul>
</details>

**Tags**: `#NSF`, `#research funding`, `#science policy`, `#US government`

---

<a id="item-9"></a>
## [China lands reusable rocket for first time](https://www.bbc.co.uk/news/articles/cm2rmmx86pdo?at_medium=RSS&at_campaign=rss) ⭐️ 8.0/10

China has successfully landed a reusable rocket for the first time, according to state media, marking a milestone in the country's space technology development. This achievement positions China among the few nations with reusable rocket technology, following SpaceX and Blue Origin, and could reduce launch costs and increase access to space. The landing follows similar achievements by US companies SpaceX and Blue Origin, but specific details about the rocket model, landing method, and date have not been disclosed.

rss · BBC World News · Jul 10, 06:44

**Background**: Reusable rockets are designed to land after launch so that their components can be recovered and reflown, significantly reducing the cost of space access. SpaceX's Falcon 9 first stage landings and Blue Origin's New Shepard suborbital landings are pioneering examples.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Reusable_launch_vehicle">Reusable launch vehicle - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_reusable_launch_system_development_program">SpaceX reusable launch system development program - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#space technology`, `#reusable rockets`, `#China`, `#aerospace`

---

<a id="item-10"></a>
## [GoPro Bike Camera Enables Georeferenced Road Survey](https://www.reddit.com/r/computervision/comments/1uslmex/turn_a_gopro_on_a_bike_into_a_georeferenced/) ⭐️ 8.0/10

A developer has created a pipeline that uses a single GoPro mounted on a bike to produce metric, georeferenced measurements of road surface defects, without LiDAR or stereo cameras. This approach dramatically lowers the cost and complexity of road condition surveying, making it accessible to municipalities and citizen scientists. It also advances monocular depth estimation for real-world metric applications. The pipeline addresses the challenge of ground plane drift in monocular depth estimation by iteratively optimizing the fit. The author notes it is not perfect but shares the current progress to encourage community feedback.

reddit · r/computervision · /u/k4meamea · Jul 10, 12:00

**Background**: Monocular depth estimation infers 3D structure from a single 2D image, but metric scale and georeferencing typically require additional sensors like LiDAR or GPS/INS. Ground plane drift occurs when the estimated ground plane gradually deviates from the true surface over time, a common issue in long-range monocular reconstruction.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2312.06021">GenDepth: Generalizing Monocular Depth Estimation for Arbitrary...</a></li>
<li><a href="https://www.emergentmind.com/topics/ground-aware-monocular-perception">Ground -Aware Monocular Perception</a></li>
<li><a href="https://www.aimodels.fyi/papers/arxiv/monopp-metric-scaled-self-supervised-monocular-depth">MonoPP: Metric-Scaled Self-Supervised Monocular Depth Estimation ...</a></li>

</ul>
</details>

**Tags**: `#computer vision`, `#monocular depth estimation`, `#road surveying`, `#georeferencing`, `#open source`

---

<a id="item-11"></a>
## [Nilay Patel: AR Glasses Require Privacy Trade-offs](https://simonwillison.net/2026/Jul/10/nilay-patel/#atom-everything) ⭐️ 7.0/10

Nilay Patel argues that practical augmented reality glasses must continuously record and send camera data to the cloud for processing, as no on-device chip can meet the power and performance requirements. He warns that this inherently invades user privacy and questions whether such products should be built at all. This commentary highlights a fundamental tension between AR innovation and privacy, affecting companies like Meta, Apple, and Google developing AR glasses. It forces a critical societal debate on whether the privacy cost of ubiquitous AR is acceptable. Patel states that current choices are either cloud-dependent glasses or a bulky device like Apple Vision Pro with an external battery pack. He emphasizes that no chip small enough to fit in a glasses stem can perform real-time processing locally.

rss · Simon Willison · Jul 10, 17:05

**Background**: Augmented reality glasses overlay digital information onto the real world, requiring continuous camera input and real-time processing. On-device processing preserves privacy but is limited by battery and thermal constraints, while cloud processing offers more power but raises privacy concerns. Companies like Meta and Apple are racing to develop lightweight AR glasses, but technical hurdles remain.

<details><summary>References</summary>
<ul>
<li><a href="https://floridareading.com/blogs/news/on-device-vs-cloud-processing-which-privacy-model-protects-your-visual-data-better">On - Device vs Cloud Processing : Which Privacy Model Protects Your...</a></li>
<li><a href="https://www.rayneo.com/blogs/news/ai-powered-smart-glasses-what-artificial-intelligence-actually-does-for-you">AI-Powered Smart Glasses : What Artificial Intelligence Actually Does...</a></li>
<li><a href="https://inairspace.com/blogs/learn-with-inair/machine-learning-vs-augmented-reality-the-silent-war-for-our-digital-future">Machine Learning vs Augmented Reality: The Silent War for Our Digital...</a></li>

</ul>
</details>

**Tags**: `#augmented reality`, `#privacy`, `#cloud computing`, `#hardware`

---

<a id="item-12"></a>
## [New Infrastructure Enables AI Portability Across Robots](https://news.google.com/rss/articles/CBMic0FVX3lxTE1JWEpNTXV2bEJhY0djZ1ZmWDRZU3ZOWGNYNFFqQU9fR09yNUNPSTgxTE5ZNGowMTZick1kSFJCLW1MS3V2MjAzV3BIbHo5Y3pfWHNnTURsaUF3OHl5amZ6eFlxNml0R2FseVNKbU1KSERiM3M?oc=5) ⭐️ 7.0/10

Researchers have developed a missing infrastructure that allows AI models to be transferred and run across different robot platforms without extensive re-engineering. This breakthrough addresses a critical bottleneck in robotics AI deployment, potentially accelerating the adoption of AI in diverse robotic systems and reducing development costs. The infrastructure likely involves standardized interfaces or middleware that abstracts hardware differences, similar to ONNX for model portability in other domains.

google_news · Tech Xplore · Jul 10, 12:20

**Background**: Currently, AI models trained for one robot often cannot be directly used on another due to differences in hardware, sensors, and control systems. This fragmentation forces developers to retrain or adapt models for each platform, slowing innovation. Model portability is a well-known challenge in AI, with solutions like ONNX emerging for general AI, but robotics has lacked a similar standard.

<details><summary>References</summary>
<ul>
<li><a href="https://aicompetence.org/modelcat-ai-announces-ai-model-portability-across-silicon-devices/">ModelCat AI Announces AI Model Portability Across Silicon Devices</a></li>
<li><a href="https://www.linkedin.com/pulse/onnx-unlock-ai-model-portability-accelerate-inference-rahim-khoja-xotuc">ONNX: Unlock AI Model Portability , Accelerate Inference, and...</a></li>
<li><a href="https://neuralwired.com/2026/04/05/agentic-ai-robotics-deployment/">Agentic AI Robotics Deployment : Why 70% Fail in 2026</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#AI`, `#model portability`, `#infrastructure`

---