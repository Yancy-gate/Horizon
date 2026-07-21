---
layout: default
title: "Horizon Summary: 2026-07-21 (EN)"
date: 2026-07-21
lang: en
---

> From 204 items, 14 important content pieces were selected

---

## CSIG Camera Prep Radar

> For CSIG Camera Academic Star: Diffusion 4K enhancement / lightweight models / contest updates (≈14-day window, ≥1 item floor)

1. [DiMOO-SR: Rarity-Aware Discrete Diffusion for Super-Resolution](#item-1) ⭐️ 9.0/10
2. [Generative Tracker Paints Persistent Identity Colors](#item-2) ⭐️ 9.0/10
3. [Google Research Demystifies Creativity in Diffusion Models](#item-3) ⭐️ 8.0/10
4. [Three-Body Scattering for One-Step Generative Models](#item-4) ⭐️ 8.0/10
5. [Edge AI Accelerator Enables 15x Faster On-Device Model Adaptation](#item-5) ⭐️ 8.0/10

---
<a id="item-1"></a>
## [DiMOO-SR: Rarity-Aware Discrete Diffusion for Super-Resolution](https://arxiv.org/abs/2607.17612v1) ⭐️ 9.0/10

Researchers propose DiMOO-SR, a rarity-aware discrete diffusion framework for photo-realistic image super-resolution that introduces Inverse Frequency Sampling (IFS) during training and Spatial Consistency Ranking (SCR) during inference to address long-tailed token distribution and parallel decoding artifacts. This work bridges discrete diffusion and image super-resolution, enabling efficient parallel decoding while preserving rare but perceptually critical textures, potentially advancing generative image restoration in multimodal models. DiMOO-SR achieves competitive perceptual quality with only a few parallel decoding steps on real-world SR benchmarks. The code will be released upon publication.

rss · CSIG · arXiv cs.CV（增强/恢复/Diffusion） · Jul 20, 07:01

**Background**: Continuous diffusion models dominate image super-resolution but rely on signal-level denoising and external conditioning. Discrete diffusion models operate on discrete visual tokens, enabling non-causal parallel prediction, but face challenges like long-tailed token distribution and spatial inconsistency in parallel decoding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Discrete_diffusion_model">Discrete diffusion model</a></li>
<li><a href="https://arxiv.org/abs/2310.16834">Discrete Diffusion Modeling by Estimating the Ratios of the Data ...</a></li>
<li><a href="https://medium.com/@cartelgouabou/mastering-long-tailed-distribution-in-deep-learning-for-image-classification-solutions-unveiled-63e00d2a1924">Mastering Long - Tailed Distribution in Deep Learning for... | Medium</a></li>

</ul>
</details>

**Tags**: `#diffusion image enhancement`, `#generative image restoration`, `#image super-resolution`, `#discrete diffusion`, `#visual tokens`

---

<a id="item-2"></a>
## [Generative Tracker Paints Persistent Identity Colors](https://arxiv.org/abs/2607.17120v1) ⭐️ 9.0/10

Researchers fine-tuned a 22B text-to-video diffusion model (LTX-2.3) with in-context LoRA to perform multi-object tracking by painting each person a distinct, persistent color, eliminating traditional detection and association modules. On DanceTrack, it achieves 40.3 HOTA with an association score (AssA 44.1) exceeding all original benchmark trackers. This work introduces a novel paradigm for multi-object tracking by leveraging generative video models, potentially unifying tracking and video generation. Its unique error profile—strong association but weak detection—highlights a new direction for improving tracking systems. The model generates long videos via chained windows, conditioned on the cleaned tail of the previous window, enabling identity persistence without a tracker or motion model. On 383 mined occlusion events, the generator re-acquires identities after gaps at a 42% conditional rate, outperforming appearance-embedding baselines that score zero.

rss · CSIG · arXiv cs.CV（增强/恢复/Diffusion） · Jul 19, 08:11

**Background**: Multi-object tracking (MOT) traditionally separates detection and association, using external state like track buffers and motion models. Diffusion models generate videos by iteratively denoising random noise, and LoRA is a parameter-efficient fine-tuning method. DanceTrack is a benchmark focusing on tracking humans with uniform appearance and dynamic motion, where association is particularly challenging.

<details><summary>References</summary>
<ul>
<li><a href="https://ltx.io/model/ltx-2-3">LTX-2.3: Introducing LTX's Latest AI Video Model | LTX</a></li>
<li><a href="https://dancetrack.github.io/">DanceTrack : Multi - Object Tracking in Uniform Appearance and...</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#multi-object tracking`, `#generative tracking`, `#video generation`, `#computer vision`

---

<a id="item-3"></a>
## [Google Research Demystifies Creativity in Diffusion Models](https://news.google.com/rss/articles/CBMijgFBVV95cUxNY3VzM3I2Y2VHTUM4WG1ydm1uaVI1Q1RSRW05blFtTVZwNVd0bmJoR2EzSTc0OTlpdUk1TXhrbl9QWUNOUE5FZV9uR2VjX090QlNJWE9rX3lCMTJnWHZ5clE2MllZcmFOemhxV3hrOVpPWGVwSmM5emFWMXRUTHJKWXAtU2I3aE9pMmlnTUZn?oc=5) ⭐️ 8.0/10

Google Research has published a study titled 'Towards demystifying the creativity of diffusion models,' aiming to understand how these models generate novel and creative outputs beyond simple replication. This work sheds light on the creative capabilities of diffusion models, which are central to modern generative AI, potentially leading to more controllable and innovative applications in art, design, and science. The study likely analyzes the generative process of diffusion models, identifying factors that contribute to creativity such as noise scheduling, model architecture, and training data diversity.

rss · CSIG · Diffusion / 生成式图像恢复 · Jul 15, 18:07

**Background**: Diffusion models are a class of generative AI that create data by gradually denoising random noise into coherent samples. They have achieved state-of-the-art results in image, video, and audio generation. Understanding their creativity is key to advancing AI's role in creative fields.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_model">Diffusion model - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/what-are-diffusion-models/">What are Diffusion Models? - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#generative AI`, `#Google Research`, `#creativity`, `#image generation`

---

<a id="item-4"></a>
## [Three-Body Scattering for One-Step Generative Models](https://arxiv.org/abs/2607.18198v1) ⭐️ 8.0/10

Researchers propose Three-Body Scattering Modeling (TBSM), a novel one-step generative method that uses distributional energy to induce sample-level motion, achieving FID=2.23 on ImageNet-256 with pixel-space PixelDiT-XL and FID=1.63 with latent-space DiT-XL at NFE=1. TBSM offers a new paradigm for one-step generation, reducing noise compared to all-pairs methods like Drifting Models, and could enable faster, more efficient high-quality image synthesis without iterative sampling. TBSM turns the energy distance into a constant-size per-projectile interaction: each projectile is attracted to one real source and repelled from one independently generated source, using O(B) sample-level losses instead of minibatch-wide all-pairs fields.

rss · CSIG · arXiv cs.CV（增强/恢复/Diffusion） · Jul 20, 17:38

**Background**: Generative models like diffusion models typically require many iterative steps to produce high-quality samples. One-step generation aims to produce samples in a single forward pass, which is faster but often less accurate. Energy distance is a statistical metric that measures the difference between two probability distributions. The three-body problem in physics describes the motion of three point masses under mutual gravitational attraction, and TBSM borrows this concept to model interactions between a generated sample, a real sample, and a reference sample.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Three-body_problem">Three-body problem - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Energy_distance">Energy distance</a></li>
<li><a href="https://lizhidan00.github.io/files/optimization/B-Wasserstein+gradient+flow.pdf">Lecture B. Wasserstein Gradient Flow</a></li>

</ul>
</details>

**Tags**: `#generative modeling`, `#one-step generation`, `#Wasserstein gradient flow`, `#energy distance`, `#efficient diffusion`

---

<a id="item-5"></a>
## [Edge AI Accelerator Enables 15x Faster On-Device Model Adaptation](https://arxiv.org/abs/2607.18101v1) ⭐️ 8.0/10

Researchers propose a heterogeneous adaptation pipeline that repurposes the Hailo-8L edge AI accelerator for frozen-backbone feature extraction, achieving up to 15.4x faster training and reduced energy consumption on a Raspberry Pi 5. This work makes on-device model adaptation practical for resource-constrained edge devices, enabling lifelong personalization without cloud dependency. It demonstrates that inference-only accelerators can be repurposed for efficient training, opening new possibilities for edge AI. The pipeline partitions the model: the quantized INT8 backbone runs on the Hailo-8L accelerator, while a lightweight FP32 classification head is fine-tuned on the host CPU. Post-training quantization restoration is critical to preserve feature quality and mitigate accuracy loss in quantization-sensitive architectures.

rss · CSIG · arXiv cs.CV（增强/恢复/Diffusion） · Jul 20, 16:02

**Background**: On-device model adaptation allows AI models to personalize over time on edge devices, but traditional end-to-end backpropagation is too compute-intensive for resource-constrained hardware. The Hailo-8L is a low-cost, DRAM-free edge AI accelerator designed for efficient inference. Frozen-backbone feature extraction uses a pre-trained model's early layers as fixed feature extractors, reducing training cost.

<details><summary>References</summary>
<ul>
<li><a href="https://hailo.ai/products/ai-accelerators/hailo-8l-ai-accelerator-for-ai-light-applications/">Hailo-8L AI Accelerator | Low-Cost DRAM-Free Edge AI Chip</a></li>
<li><a href="https://link.springer.com/article/10.1007/s00371-026-04378-1">Enhancing RGB-IR object detection: a frozen backbone approach with multi-receptive field attention | The Visual Computer | Springer Nature Link</a></li>
<li><a href="https://arxiv.org/pdf/2204.00484">Proper Reuse of Image Classification Features Improves Object Detection</a></li>

</ul>
</details>

**Tags**: `#edge AI`, `#on-device adaptation`, `#model efficiency`, `#Hailo-8L`, `#heterogeneous computing`

---

## Other highlights

6. [Chinese Open-Source AI Models Threaten Western Valuations](#item-6) ⭐️ 8.0/10
7. [AI Outpaces Humans in Finding Mathematical Counterexamples](#item-7) ⭐️ 8.0/10
8. [Hacker wipes Romania's entire land registry database](#item-8) ⭐️ 8.0/10
9. [China's open-weight Kimi K3 AI model worries Silicon Valley](#item-9) ⭐️ 8.0/10
10. [NVIDIA Unveils Cosmos 3 Edge for On-Device AI](#item-10) ⭐️ 7.0/10
11. [Google Developing New AI Chip for Gemini Efficiency](#item-11) ⭐️ 7.0/10
12. [OpenAI fears open-weight models; US debates ban](#item-12) ⭐️ 7.0/10
13. [AI coding agents slash reverse-engineering costs](#item-13) ⭐️ 7.0/10
14. [Furtex Linux Toolkit Evades EDR and Falco with io_uring and eBPF](#item-14) ⭐️ 6.0/10

---

<a id="item-6"></a>
## [Chinese Open-Source AI Models Threaten Western Valuations](https://stratechery.com/2026/whos-afraid-of-chinese-models/) ⭐️ 8.0/10

Chinese labs are releasing high-quality open-source AI models for free, undercutting the premium API pricing strategies of Western labs like OpenAI and Anthropic. This forces a race to the bottom in pricing, threatening the astronomical valuations of Western AI labs (e.g., Anthropic at $1.2T, OpenAI targeting $850B) that rely on premium pricing. The article highlights that user stickiness for tools like Claude Code and Codex may be lower than assumed, as users can switch easily, reducing competitive moats.

hackernews · mfiguiere · Jul 20, 11:05 · [Discussion](https://news.ycombinator.com/item?id=48977128)

**Background**: Open-source AI models are models whose source code and weights are publicly available, allowing anyone to use, modify, and distribute them. Chinese labs have been releasing competitive open-source models, challenging the closed-source, premium-pricing model of Western AI companies.

**Discussion**: Commenters express fear that Chinese models could be used for geopolitical influence and data security risks, while others debate the stickiness of coding tools and the impact on VC valuations.

**Tags**: `#Chinese AI`, `#open-source models`, `#AI market`, `#geopolitics`, `#valuation`

---

<a id="item-7"></a>
## [AI Outpaces Humans in Finding Mathematical Counterexamples](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/) ⭐️ 8.0/10

A blog post on the Xena Project reports that AI systems are increasingly capable of generating counterexamples to mathematical conjectures, sometimes outperforming human mathematicians. This trend is reshaping how mathematical research is conducted. This development could save mathematicians significant time by quickly disproving false conjectures, allowing them to focus on more promising avenues. It also raises questions about the future role of human intuition and creativity in mathematics. The post mentions that some graduate students pay $200 per month to access AI models like Sol and Fable for counterexample generation. The AI's ability to find counterexamples is seen as a complement to formal proof assistants like Lean.

hackernews · artninja1988 · Jul 20, 19:03 · [Discussion](https://news.ycombinator.com/item?id=48983382)

**Background**: In mathematics, a counterexample is a specific instance that disproves a conjecture or statement. Finding a counterexample is often easier than proving a conjecture true, as it only requires one valid counterexample. AI models trained on mathematical data can now generate plausible conjectures and test them, accelerating the discovery of counterexamples.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Counterexample">Counterexample - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2506.22005">[2506.22005] LeanConjecturer: Automatic Generation of ... Lean Conjecturer: Revolutionizing Mathematics Research LeanConjecturer: Automatic Generation of Mathematical ... Top Stories OpenAI's AI Didn't Solve A Math Problem—It Broke A Theory An OpenAI model has disproved a central conjecture in ... A New Breakthrough in AI Solving Mathematical Conjectures ... AI Solved A Mathematical Problem That Had Stumped ... - Forbes</a></li>

</ul>
</details>

**Discussion**: Commenters generally view this as a positive development, noting that it saves time and effort. One commenter draws a parallel to the folk tale of John Henry, questioning whether humans can still outperform machines in delivering elegant proofs. Another shares a cautionary anecdote about a mathematician whose career suffered due to a flawed conjecture, suggesting AI could prevent such tragedies.

**Tags**: `#AI`, `#mathematics`, `#research methodology`, `#counterexamples`

---

<a id="item-8"></a>
## [Hacker wipes Romania's entire land registry database](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/) ⭐️ 8.0/10

A hacker breached Romania's National Agency for Cadastre and Real Estate Advertising (ANCPI) and wiped the entire land registry database following a failed extortion attempt, halting all property transactions nationwide. This incident paralyzes Romania's real estate market and threatens property ownership records, highlighting the critical need for offline backups and secure government IT systems. Officials are restoring from an offline backup and migrating applications to Romania's Government Cloud, coordinated by the Special Telecommunications Service (STS), with completion expected by July 22, 2026.

hackernews · speckx · Jul 20, 13:28 · [Discussion](https://news.ycombinator.com/item?id=48978605)

**Background**: ANCPI operates e-Terra, the system underpinning every property transaction in Romania. The hacker, identified as Zakaria Mahdjoub from Algeria, claimed to have deleted backups as well, but an offline copy survived. Algeria has an extradition treaty with Romania.

<details><summary>References</summary>
<ul>
<li><a href="https://cybernews.com/security/hacker-deletes-romanian-land-registry-database/">Hacker deletes country’s entire land registry database after ...</a></li>
<li><a href="https://byteiota.com/romania-land-registry-hack-wipe/">Romania’s Land Registry Was Wiped. One Backup Saved It.</a></li>
<li><a href="https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/">Hacker wipes Romania's entire land registry database</a></li>

</ul>
</details>

**Discussion**: Commenters expressed relief that an offline backup existed, preventing societal chaos over land ownership. Some Romanian users attributed the breach to corruption in government IT contracts, while others noted the hacker's identity and extradition implications.

**Tags**: `#cybersecurity`, `#data breach`, `#infrastructure`, `#hacking`, `#Romania`

---

<a id="item-9"></a>
## [China's open-weight Kimi K3 AI model worries Silicon Valley](https://news.google.com/rss/articles/CBMivwFBVV95cUxQMlJnTkVuaFpUS2lJMmx0NTJ5bHl1bFVHcVY3Y29HeV91TnZyRG9YYTc0bzNNN3prYzJVTlFXTUR2cWU3LTdZSXllMkVPNzg3QkFfRUNFa2IxaXRCY3BfUXBtY3RUTEtkektxSjFDbE9SbmRUT0hpY25MYXl6bUhmYVNZMmtJdUVzbk45SzdIOXFGc1hnd056SUx5bnZraXVEdlFDRG5kMFRKbTBIYUhIY1NQMWJUQk9zWnpfUzFwZ9IBvwFBVV95cUxOR2dfd2M4Q0NzVG9oVWxjTnpuTlhCU3JLb0hpWkozdjlzR2FubkpiMXRsa19wbjFFcmxxOEJ4WHVhVUxWZHo0am1sb2ZlUlpGODE2eW1IZVB3ZnZhekJkM3dPd0E1dlRiN0dxS2NEUkkySnNzeldiYzRaQkpGR2JaWlN3WDRxMDhweWlCY2JJd0hxTGtwOVJTVjExZ01nSjdRZklybTF5XzJLbkdqYXJxa3BnaTN3SEtwNUdyYjk1WQ?oc=5) ⭐️ 8.0/10

Chinese AI startup Moonshot AI released the open-weight Kimi K3 model in July 2026, which features 2.8 trillion parameters and a 1-million-token context window. Kimi K3's competitive performance and open-weight nature allow anyone to download and run it locally, challenging the dominance of US tech giants and raising concerns about AI safety and geopolitical competition. Kimi K3 uses a hybrid linear attention mechanism called Kimi Delta Attention (KDA) and Attention Residuals, enabling efficient processing of long contexts. It is designed for agentic coding and knowledge work.

google_news · South China Morning Post · Jul 20, 14:00

**Background**: Open-weight models release the trained neural network weights publicly, allowing users to run the model on their own hardware. Unlike closed models like GPT-4, open-weight models enable customization and offline use, but also raise concerns about misuse. Kimi K3 is the latest in a series of Chinese AI models that have achieved performance comparable to leading US models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K3">Kimi K3</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-weight model`, `#China`, `#Silicon Valley`, `#Kimi K3`

---

<a id="item-10"></a>
## [NVIDIA Unveils Cosmos 3 Edge for On-Device AI](https://huggingface.co/blog/nvidia/cosmos3edge) ⭐️ 7.0/10

NVIDIA announced Cosmos 3 Edge, a small language model with 4 billion parameters optimized for real-time inference on edge devices such as robots and autonomous vehicles. This release enables powerful physical AI reasoning directly on resource-constrained hardware, reducing latency and enhancing privacy by keeping data on-device, which is critical for autonomous systems and robotics. Cosmos 3 Edge is part of the Cosmos 3 family and targets compute-constrained modules that must perceive, reason, and act without datacenter dependency, achieving first-token latency as low as 5-15 milliseconds.

rss · Hugging Face Blog · Jul 20, 15:58

**Background**: Small language models (SLMs) are language models typically ranging from 0.5 billion to 14 billion parameters, designed to run efficiently on consumer hardware or edge devices. On-device inference eliminates network hops, improving response time and data privacy. NVIDIA's Cosmos 3 is an open frontier foundation model for physical AI, grounding language in images and video for deeper physical reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://research.nvidia.com/labs/cosmos-lab/cosmos3/">Cosmos 3 — Cosmos Lab - research.nvidia.com</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai">NVIDIA Launches Cosmos 3, the Open Frontier Foundation Model ...</a></li>
<li><a href="https://kie.ai/blog/what-is-cosmos-3-edge">What Is Cosmos 3 Edge? NVIDIA's 4B Robot Model - kie.ai</a></li>

</ul>
</details>

**Tags**: `#edge AI`, `#small language model`, `#NVIDIA`, `#efficient deployment`

---

<a id="item-11"></a>
## [Google Developing New AI Chip for Gemini Efficiency](https://techcrunch.com/2026/07/20/google-is-working-on-a-new-ai-chip-designed-to-make-gemini-more-efficient/) ⭐️ 7.0/10

Alphabet is reportedly developing a new AI chip specifically designed to make its Gemini models run more efficiently. This chip could significantly reduce the computational cost and energy consumption of running Gemini, making advanced AI more accessible and sustainable. The chip is tailored for Gemini's architecture, potentially offering performance gains over general-purpose hardware like GPUs.

rss · TechCrunch AI · Jul 20, 21:21

**Background**: Google's Gemini is a family of multimodal large language models competing with OpenAI's GPT-4. Custom AI chips, like Google's TPU, are designed to accelerate machine learning workloads more efficiently than general-purpose processors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model) - Wikipedia</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models">Models | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Tags**: `#AI chip`, `#Gemini`, `#hardware efficiency`, `#Google`

---

<a id="item-12"></a>
## [OpenAI fears open-weight models; US debates ban](https://techcrunch.com/2026/07/20/openai-is-scared-of-open-weight-models-should-the-us-be/) ⭐️ 7.0/10

A TechCrunch article reports that the US is debating whether to ban Chinese-made open-weight large language models, highlighting tensions between AI safety concerns and business interests. This debate could reshape global AI development by restricting access to powerful open-weight models, impacting researchers, startups, and enterprises that rely on self-hosted LLMs. Open-weight models allow users to download and run AI models locally, unlike closed APIs. The article suggests OpenAI, which profits from its proprietary models, may support restrictions on open-weight competitors.

rss · TechCrunch AI · Jul 20, 19:33

**Background**: Open-weight models are AI models with publicly available weights, enabling anyone to run them on their own hardware. They contrast with closed models like OpenAI's GPT-4, which are only accessible via API. The US government is considering a ban on Chinese open-weight LLMs due to national security concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://github.com/xigh/open-weight-models">GitHub - xigh/open-weight-models: Curated list of open-weight ...</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open-weight models`, `#LLMs`, `#geopolitics`

---

<a id="item-13"></a>
## [AI coding agents slash reverse-engineering costs](https://simonwillison.net/2026/Jul/20/cheap-reverse-engineering/#atom-everything) ⭐️ 7.0/10

Coding agents powered by large language models have dramatically reduced the cost and effort required to reverse-engineer and automate home devices, making projects that were previously uneconomical now viable. This shift lowers the barrier for individuals and small teams to automate their environments, potentially accelerating the adoption of smart home automation and custom integrations. It also reduces the psychological burden of maintaining fragile, undocumented APIs, as code can be cheaply rewritten. The key insight is that the return-on-investment calculus for reverse-engineering has changed: the initial effort and ongoing maintenance costs are now low enough that even short-lived automations are worthwhile. The author notes that coding agents make it cheap to try and fail, removing the fear of wasted effort.

rss · Simon Willison · Jul 20, 19:24

**Background**: Reverse-engineering involves analyzing a device or software to understand its internal workings, often to create custom integrations or automations. Traditionally, this required significant manual effort and expertise, and the resulting code often relied on undocumented APIs that could break with updates, leading to high maintenance costs. Coding agents—AI tools that can generate, debug, and refactor code—automate much of this analysis and code generation, drastically reducing the time and skill required.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/GeoloeG-IsT/agents-reverse-engineer">GitHub - GeoloeG-IsT/agents-reverse-engineer: Reverse engineer your codebase to let your agents work efficiently · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2601.18381">[2601.18381] AI Agent for Reverse-Engineering Legacy Finite-Difference Code and Translating to Devito</a></li>

</ul>
</details>

**Tags**: `#reverse-engineering`, `#coding agents`, `#automation`, `#AI-assisted development`

---

<a id="item-14"></a>
## [Furtex Linux Toolkit Evades EDR and Falco with io_uring and eBPF](https://news.google.com/rss/articles/CBMiVkFVX3lxTE95ZEp2cGFnVUZwVVpHNkhabTVzNTFuY2Zsa1V1eGZmaHVVbjlGNXZOc1RwMnYyVlI2UEFKcVktN0ZhYlpvMVEwQm9YN2JEZkN0Zkw5LXZn0gFbQVVfeXFMUFZjeWxiak1MN1ZnTmpkbW5ra3lGbi00U3Z2Z0RwRDZDNTlLMF9jM0dFTnNKMkFabVA0N213WTlla1k3d0E1NkJZQ3MtMTZUdWY2MmZhSzRKSXV2OA?oc=5) ⭐️ 6.0/10

A new Linux toolkit called Furtex uses io_uring and eBPF to bypass Endpoint Detection and Response (EDR) systems and the Falco runtime security tool. It was reported by gbhackers.com. This toolkit demonstrates a novel evasion technique that exploits low-level kernel interfaces, potentially undermining the effectiveness of widely-used security monitoring tools. It highlights the ongoing arms race between attackers and defenders in Linux security. Furtex leverages io_uring for asynchronous I/O and eBPF for kernel-level programmability, both of which can be used to hide malicious activity from user-space monitoring tools. The toolkit specifically targets Falco, a cloud-native runtime security tool that relies on kernel events.

google_news · gbhackers.com · Jul 20, 06:39

**Background**: io_uring is a Linux kernel interface for asynchronous I/O that reduces context switches, while eBPF allows sandboxed programs to run in the kernel for observability and security. Falco uses eBPF or kernel modules to monitor system calls and generate security alerts. By using these same technologies, Furtex can evade detection by operating at a lower level or by manipulating event data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">io_uring - Wikipedia</a></li>
<li><a href="https://ebpf.io/what-is-ebpf/">What is eBPF ? An Introduction and Deep Dive into the eBPF ...</a></li>
<li><a href="https://falco.org/">Falco</a></li>

</ul>
</details>

**Tags**: `#security`, `#eBPF`, `#io_uring`, `#Linux`, `#EDR evasion`

---