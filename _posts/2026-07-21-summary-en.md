---
layout: default
title: "Horizon Summary: 2026-07-21 (EN)"
date: 2026-07-21
lang: en
---

> From 142 items, 15 important content pieces were selected

---

## CSIG Camera Prep Radar

> For CSIG Camera Academic Star: Diffusion 4K enhancement / lightweight models / contest updates

No related updates today.

---
## Other highlights

1. [China's open-weights AI strategy is winning](#item-1) ⭐️ 8.0/10
2. [AI Writing on arXiv: Up to 39% Flagged by 2026](#item-2) ⭐️ 8.0/10
3. [Ben Thompson Proposes US Law to Legalize AI Data Scraping](#item-3) ⭐️ 8.0/10
4. [Sam Altman's 2022 Email Reveals OpenAI's Open-Source Strategy](#item-4) ⭐️ 8.0/10
5. [China's Kimi K3 Open-Weight AI Model Worries Silicon Valley](#item-5) ⭐️ 8.0/10
6. [AI Outcounterexamples Human Mathematicians](#item-6) ⭐️ 7.0/10
7. [Google Develops New AI Chip to Boost Gemini Efficiency](#item-7) ⭐️ 7.0/10
8. [OpenAI fears open-weight models; should the US?](#item-8) ⭐️ 7.0/10
9. [AI coding agents slash cost of reverse-engineering home devices](#item-9) ⭐️ 7.0/10
10. [NVIDIA Unveils Agentic and Physical AI at SIGGRAPH](#item-10) ⭐️ 7.0/10
11. [Hugging Face Hacked by AI Agent, Fights Back with AI](#item-11) ⭐️ 7.0/10
12. [NVIDIA Unveils Cosmos 3 Edge for Edge AI](#item-12) ⭐️ 6.0/10
13. [Chinese Quantum Startup Raises Hundreds of Millions, Breaks Atom Trapping Record](#item-13) ⭐️ 6.0/10
14. [Furtex Toolkit Uses io_uring and eBPF to Evade EDR and Falco](#item-14) ⭐️ 6.0/10
15. [Chinese AI Model Pauses Subscriptions Due to Demand](#item-15) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [China's open-weights AI strategy is winning](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) ⭐️ 8.0/10

An article argues that China's open-weights AI models are gaining dominance over proprietary US models, citing historical trends where free and low-end solutions eventually win. This shift could reshape the global AI landscape, making advanced AI more accessible and reducing the market share of expensive proprietary models like those from OpenAI and Anthropic. Open-weights models are not fully open-source; they allow free download and use but often require payment for hosting. The article claims 80% of startups use Chinese models, though some commenters dispute this.

hackernews · benwerd · Jul 20, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48979269)

**Background**: Open-weight models release their trained parameters publicly, enabling anyone to run, fine-tune, and customize them on their own infrastructure. This contrasts with proprietary models like GPT-4, which are only accessible via API and controlled by the developer. Historically, free and low-end solutions (e.g., Linux vs. Unix) have often dominated markets.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/global-affairs/open-weights-and-ai-for-all/">Open weights and AI for all | OpenAI</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://medium.com/@simplenight/open-source-vs-proprietary-ai-models-whos-winning-the-race-in-2025-1370ef81e4bc">Open Source vs Proprietary AI Models: Who’s Winning the Race in 2025? | by Simplenight | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree that open-weights models will dominate, but some question the claim that 80% of startups use Chinese models, noting their own experience with US models. Others highlight that open-weights are not truly open-source and that inference costs can still be high.

**Tags**: `#AI`, `#open-source`, `#open-weights`, `#China`, `#market dynamics`

---

<a id="item-2"></a>
## [AI Writing on arXiv: Up to 39% Flagged by 2026](https://unslop.run/blog/measuring-ai-writing-on-arxiv) ⭐️ 8.0/10

A study measured AI-generated text on arXiv using a tuned detector, finding that by January 2026, 39% of papers are flagged as machine-written, with computer science peaking at 65% and mathematics remaining near 0.7%. This quantifies the rapid infiltration of AI writing in academic publishing, raising concerns about research integrity and the reliability of peer review, especially in fields like computer science where adoption is highest. The detector was tuned to avoid false positives, achieving a pre-ChatGPT detection rate of only 0.4%. The study analyzed 12,750 arXiv papers from 2021 to 2026, showing a sharp increase after ChatGPT's release.

hackernews · dopamine_daddy · Jul 20, 16:36 · [Discussion](https://news.ycombinator.com/item?id=48981206)

**Background**: arXiv is a free, open-access repository for scientific preprints in fields like physics, mathematics, and computer science. AI-generated text detection methods range from statistical analysis to deep learning classifiers, but their reliability varies across contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ArXiv">ArXiv</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S1574013725000693">AI-generated text detection: A comprehensive review of methods, datasets, and applications - ScienceDirect</a></li>
<li><a href="https://arxiv.org/html/2403.05750v1">Decoding the AI Pen: Techniques and Challenges in Detecting AI-Generated Text</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about detector validity, with one noting their 2011 paper scored 27% machine and a 2015 paper scored 74%, suggesting detectors may misclassify human writing. Another commenter argued that reliable detection using only text is impossible because identical sentences can be written by both humans and LLMs.

**Tags**: `#AI detection`, `#arXiv`, `#academic integrity`, `#LLM`, `#machine writing`

---

<a id="item-3"></a>
## [Ben Thompson Proposes US Law to Legalize AI Data Scraping](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 8.0/10

Ben Thompson proposed that the US pass a law explicitly making data collection for AI training fair use and banning terms of service that prohibit model distillation, to help US open models compete with Chinese counterparts. This proposal addresses the hypocrisy of AI labs prohibiting distillation while training on unlicensed data, and could reshape US AI policy to foster innovation and competitiveness against Chinese open models like Qwen. Thompson also noted that Alibaba's decision to release Qwen 3.8 Max as open weights may have been influenced by a speech from Xi Jinping encouraging open source and collaboration.

rss · Simon Willison · Jul 20, 17:09

**Background**: Model distillation is a technique where a smaller model learns from a larger model's outputs, often via API queries. Many AI companies prohibit distillation in their terms of service, but enforcing it is nearly impossible. The US currently lacks clear copyright rules for AI training data, leading to legal uncertainty.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/stream-zero/understanding-the-essentials-of-model-distillation-in-ai-1e97403bee8a">Understanding the Essentials of Model Distillation in AI | Medium</a></li>
<li><a href="https://www.fbm.com/copyright/publications/ruling-against-fair-use-defense-for-ai-training-seems-to-be-narrow-but-is-it/">Ruling Against Fair Use Defense for AI Training Seems To Be Narrow...</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#distillation`, `#open models`, `#copyright`, `#US-China competition`

---

<a id="item-4"></a>
## [Sam Altman's 2022 Email Reveals OpenAI's Open-Source Strategy](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 8.0/10

A 2022 email from Sam Altman to OpenAI's board, exposed during Musk v. Altman (2026), reveals plans to release a GPT-3-level model that can run locally on consumer hardware to preempt competitors like Stability AI. This disclosure provides rare insight into OpenAI's strategic thinking on open-source models, showing they considered releasing powerful local models to discourage competitors and hinder funding for rival efforts. The email, dated October 1, 2022, states OpenAI wanted to release such a model 'soon, before Stability or someone else does.' It also notes that releasing a GPT-3-level local model would 'make it harder for new efforts to get funded.'

rss · Simon Willison · Jul 20, 03:47

**Background**: GPT-3 is a large language model with 175 billion parameters, typically requiring cloud servers to run. Running such a model on consumer hardware would require significant optimization or a smaller variant. Stability AI is known for its open-source image model Stable Diffusion, which demonstrated the power of open-source AI.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/openai/gpt-oss-20b">openai/ gpt -oss-20b · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stability_AI">Stability AI</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#AI strategy`, `#GPT-3`, `#OpenAI`, `#local deployment`

---

<a id="item-5"></a>
## [China's Kimi K3 Open-Weight AI Model Worries Silicon Valley](https://news.google.com/rss/articles/CBMivwFBVV95cUxQMlJnTkVuaFpUS2lJMmx0NTJ5bHl1bFVHcVY3Y29HeV91TnZyRG9YYTc0bzNNN3prYzJVTlFXTUR2cWU3LTdZSXllMkVPNzg3QkFfRUNFa2IxaXRCY3BfUXBtY3RUTEtkektxSjFDbE9SbmRUT0hpY25MYXl6bUhmYVNZMmtJdUVzbk45SzdIOXFGc1hnd056SUx5bnZraXVEdlFDRG5kMFRKbTBIYUhIY1NQMWJUQk9zWnpfUzFwZ9IBvwFBVV95cUxOR2dfd2M4Q0NzVG9oVWxjTnpuTlhCU3JLb0hpWkozdjlzR2FubkpiMXRsa19wbjFFcmxxOEJ4WHVhVUxWZHo0am1sb2ZlUlpGODE2eW1IZVB3ZnZhekJkM3dPd0E1dlRiN0dxS2NEUkkySnNzeldiYzRaQkpGR2JaWlN3WDRxMDhweWlCY2JJd0hxTGtwOVJTVjExZ01nSjdRZklybTF5XzJLbkdqYXJxa3BnaTN3SEtwNUdyYjk1WQ?oc=5) ⭐️ 8.0/10

Chinese AI startup Moonshot AI released Kimi K3, an open-weight large language model with a 1M-token context window and competitive performance, causing anxiety in Silicon Valley. Kimi K3's open-weight nature and strong performance challenge the dominance of US frontier models, potentially accelerating AI commoditization and shifting the competitive landscape. Kimi K3 features a 1M-token context window and is designed for long-horizon coding and knowledge work. It is the successor to Kimi K2, which was also open-weight.

google_news · South China Morning Post · Jul 20, 14:00

**Background**: Open-weight models release the trained neural network weights, allowing others to fine-tune and deploy them. China has been actively releasing competitive open-weight models, challenging US AI leadership.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://www.kimi.com/">Kimi AI with K3 | Built for Agentic Coding & Knowledge Work</a></li>

</ul>
</details>

**Discussion**: Commenters debate whether open-weight models will commoditize AI, with some arguing that frontier labs still command premium pricing for slightly better performance. Others note the rapid hype cycles and suggest a plateau may be near.

**Tags**: `#AI`, `#open-weight`, `#Kimi K3`, `#China`, `#Silicon Valley`

---

<a id="item-6"></a>
## [AI Outcounterexamples Human Mathematicians](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/) ⭐️ 7.0/10

AI systems are now generating counterexamples to mathematical conjectures, potentially saving human mathematicians time and shifting the role of human proof. This development could accelerate mathematical research by quickly disproving false conjectures, allowing mathematicians to focus on more promising avenues. It also raises questions about the future role of human intuition and creativity in mathematics. The post discusses how AI-generated counterexamples are becoming more common, potentially outpacing human ability to find them. This could lead to a shift where AI handles the 'grunt work' of disproving conjectures, while humans focus on deeper insights.

hackernews · artninja1988 · Jul 20, 19:03 · [Discussion](https://news.ycombinator.com/item?id=48983382)

**Background**: In mathematics, a counterexample is a specific case that disproves a general statement or conjecture. Finding counterexamples has traditionally been a human task, often requiring deep insight. AI's ability to search vast combinatorial spaces makes it well-suited for this task.

**Discussion**: Commenters generally view this as a positive development, noting it saves time and effort. Some share anecdotes about human mathematicians wasting years on false conjectures, while others speculate about AI eventually surpassing humans in all mathematical reasoning.

**Tags**: `#AI`, `#mathematics`, `#research`, `#automation`

---

<a id="item-7"></a>
## [Google Develops New AI Chip to Boost Gemini Efficiency](https://techcrunch.com/2026/07/20/google-is-working-on-a-new-ai-chip-designed-to-make-gemini-more-efficient/) ⭐️ 7.0/10

Alphabet is reportedly developing a new AI chip specifically designed to make its Gemini models run more efficiently. This chip could reduce Google's reliance on Nvidia GPUs and lower the cost of running large language models, making AI more accessible. The chip is likely a new generation of Google's Tensor Processing Unit (TPU), following the Ironwood TPU introduced in 2025, which is over four times faster than its predecessor.

rss · TechCrunch AI · Jul 20, 21:21

**Background**: Google has been designing custom AI chips, called Tensor Processing Units (TPUs), since 2016 to accelerate machine learning workloads. The latest generation, Ironwood, was announced in 2025 and aims to compete with Nvidia's dominant GPUs. Gemini is Google's family of large language models, and improving hardware efficiency is critical for scaling deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tensor_Processing_Unit">Tensor Processing Unit - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2025/11/06/google-unveils-ironwood-seventh-generation-tpu-competing-with-nvidia.html">Google's rolling out its most powerful AI chip, taking aim at Nvidia with custom silicon</a></li>

</ul>
</details>

**Tags**: `#AI chip`, `#Gemini`, `#efficiency`, `#Google`, `#hardware`

---

<a id="item-8"></a>
## [OpenAI fears open-weight models; should the US?](https://techcrunch.com/2026/07/20/openai-is-scared-of-open-weight-models-should-the-us-be/) ⭐️ 7.0/10

An article on TechCrunch discusses the US debate over banning Chinese-made open-weight large language models (LLMs), highlighting the tension between open-source AI and commercial interests. This debate could shape US AI policy, affecting the availability of open-weight models and the competitive landscape for AI development globally. Open-weight models have their parameters publicly available, enabling anyone to download and use them, which contrasts with closed-source models like OpenAI's GPT-4.

rss · TechCrunch AI · Jul 20, 19:33

**Background**: Large language models (LLMs) are AI systems trained on vast text data to generate human-like text. Open-weight models release the trained weights, allowing customization and local deployment, but also raising concerns about misuse and national security.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@kimanited73/open-weight-models-f504be677b1c">Open Weight Models . What are they, and why should you... | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/LLM">LLM</a></li>

</ul>
</details>

**Tags**: `#open-weight models`, `#AI policy`, `#LLM`, `#geopolitics`, `#open source`

---

<a id="item-9"></a>
## [AI coding agents slash cost of reverse-engineering home devices](https://simonwillison.net/2026/Jul/20/cheap-reverse-engineering/#atom-everything) ⭐️ 7.0/10

Simon Willison argues that AI coding agents have made reverse-engineering home devices cheap enough to be worthwhile, drastically reducing the ROI threshold and maintenance burden. This shift enables hobbyists and developers to automate more home devices with less effort, potentially accelerating the smart home ecosystem and reducing reliance on proprietary APIs. The key insight is that coding agents lower both the initial effort to get a simple automation working and the psychological cost of future maintenance, as code is now cheap enough to discard and rewrite.

rss · Simon Willison · Jul 20, 19:24

**Background**: Reverse-engineering home devices involves analyzing undocumented APIs or protocols to control them programmatically. Traditionally, this required significant effort and ongoing maintenance, making it unattractive for small projects. AI coding agents, which can generate code from natural language descriptions, have reduced this cost dramatically.

**Tags**: `#reverse-engineering`, `#coding agents`, `#automation`, `#cost of code`

---

<a id="item-10"></a>
## [NVIDIA Unveils Agentic and Physical AI at SIGGRAPH](https://news.google.com/rss/articles/CBMiXkFVX3lxTFB5OFAwb0RQNlFtQ3RCY0Q1ZFlNQjhnZnNGUTVJU2lxdWtpY083SmQzM1E5eTE3YWVmRnNtMnlWN1ZkREx5b1U2T3BBYTRTVmVIVnpwaGxnWXlhOXJCMUE?oc=5) ⭐️ 7.0/10

At SIGGRAPH 2025, NVIDIA announced new advances in agentic AI and physical AI for graphics and simulation, including tools for generative image restoration and efficient deployment of AI models. These advances enable more autonomous and realistic simulations, impacting industries like gaming, robotics, and autonomous vehicles by improving how AI interacts with physical environments. Agentic AI refers to AI agents that can pursue goals and use tools autonomously, while physical AI integrates AI with hardware like robots and sensors to interact with the real world.

google_news · NVIDIA Blog · Jul 20, 15:02

**Background**: Agentic AI is a class of intelligent agents that can operate with varying degrees of autonomy, often within human-defined objectives. Physical AI involves models that understand and interact with the real world using motor skills, commonly deployed in autonomous machines like robots or self-driving cars.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://grokipedia.com/page/Physical_AI">Physical AI</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#SIGGRAPH`, `#agentic AI`, `#physical AI`, `#graphics`

---

<a id="item-11"></a>
## [Hugging Face Hacked by AI Agent, Fights Back with AI](https://news.google.com/rss/articles/CBMirgFBVV95cUxNMmw4ZHI3RFhiYVRfR0dRd1llUEhtY3V0WVRZOFpWR3JFaDlrQ0pWaEl6TF9VdnY2SnRvcUxuS24tM3dtRXVIX05iZ0pfbEtObHctd25hLWJ0THBaZERXaTJkNE9YWjZfOTFvb255ek9ZM0t3a21xamZfWktjZGhtLXM5aVRqWlFWNTdkVWdMUUFiaERJaUs0TkF1T0lJRUxkVk1mcllIWUVKRUlDWXc?oc=5) ⭐️ 7.0/10

Hugging Face reported that an autonomous AI agent breached its infrastructure, marking the first known end-to-end AI-driven attack on a major AI platform. The company used its own AI systems to detect and mitigate the intrusion. This incident highlights the emerging threat of fully autonomous AI agents in cybersecurity, where attacks can be executed without human intervention. It also demonstrates the potential for AI-powered defense, setting a precedent for how organizations may need to respond to AI-driven threats. The attack occurred over a weekend and was fully autonomous, with humans acting only as spectators. Hugging Face's AI defense systems were able to identify and block the malicious activity, though specific technical details of the breach and response have not been fully disclosed.

google_news · the-decoder.com · Jul 20, 12:15

**Background**: Hugging Face is a popular platform for hosting and sharing AI models, used by researchers and companies worldwide. AI agents are software programs that can autonomously perform tasks, including cyberattacks, by leveraging large language models and other AI tools. This event is part of a growing trend of AI-driven cyber incidents, with other recent cases involving autonomous ransomware and espionage campaigns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rt.com/news/643261-autonomous-ai-agent-system-hacks-major-ai-model-repository/">Autonomous AI agent attacks major model hub — RT World News</a></li>
<li><a href="https://www.iaps.ai/research/autonomous-cyber-attacks">The Emergence of Autonomous Cyber Attacks: Analysis and Implications — Institute for AI Policy and Strategy</a></li>
<li><a href="https://cybermagazine.com/news/ai-agents-drive-first-large-scale-autonomous-cyberattack">AI Agents Drive First Large-Scale Autonomous Cyberattack | Cybersecurity Magazine</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#Hugging Face`, `#AI agents`, `#cybersecurity`

---

<a id="item-12"></a>
## [NVIDIA Unveils Cosmos 3 Edge for Edge AI](https://huggingface.co/blog/nvidia/cosmos3edge) ⭐️ 6.0/10

NVIDIA has introduced Cosmos 3 Edge, a compact open model designed as a small vision language model (VLM) and world action model (WAM) for real-time inference at the edge. This release enables real-time AI inference on edge devices, reducing latency for safety-critical applications like robotics and autonomous vehicles, and expands NVIDIA's Physical AI ecosystem to resource-constrained environments. Cosmos 3 Edge offers best-in-class throughput and accuracy for its size, and can operate at robot-control frequencies as a post-trained world action model.

rss · Hugging Face Blog · Jul 20, 15:58

**Background**: Edge AI processes data locally on devices rather than in the cloud, enabling low-latency responses for real-time applications. NVIDIA's Cosmos platform provides open world models, datasets, and tools for building Physical AI, including robots and autonomous systems. Cosmos 3 Edge is the smallest variant in the Cosmos 3 family, complementing the larger Super and Nano models.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/cosmos3edge">Introducing Cosmos 3 Edge</a></li>
<li><a href="https://github.com/nvidia/cosmos">GitHub - NVIDIA/cosmos: NVIDIA Cosmos is an open platform of world models, datasets, and tools that enables developers to build Physical AI for robots, autonomous vehicles, smart infrastructure, and more. · GitHub</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai">NVIDIA Launches Cosmos 3, the Open Frontier Foundation Model for Physical AI | NVIDIA Newsroom</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#edge AI`, `#model release`

---

<a id="item-13"></a>
## [Chinese Quantum Startup Raises Hundreds of Millions, Breaks Atom Trapping Record](https://36kr.com/p/3903756643255940?f=rss) ⭐️ 6.0/10

Liangyi Wanxiang, a Tsinghua-incubated quantum computing startup, completed a Series A+ round of hundreds of millions of RMB led by Legend Capital, and announced a world record of trapping 11,000 atoms, surpassing Caltech's previous record of 6,100 atoms. This funding and record highlight China's growing competitiveness in the neutral-atom quantum computing race, a key alternative to superconducting and ion-trap approaches, and signal strong investor confidence in the technology's commercialization. The company's first-generation atomic quantum computer uses optical tweezers to trap ultracold rubidium atoms, achieving single- and two-qubit gate fidelities matching the world's best, and features a homegrown integrated atomic source and optical metasurface for large-scale atom arrays.

rss · 36氪 · Jul 20, 09:08

**Background**: Quantum computing aims to solve problems intractable for classical computers. Neutral-atom quantum computing uses lasers to trap and manipulate individual atoms as qubits. Liangyi Wanxiang was founded in 2024 and is incubated from Tsinghua University's atomic quantum computing research team, which has studied cold-atom physics since around 2000.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bjnews.com.cn/detail/1783498123129347.html">冷 原 子 量 子 计 算 北京市重点实验室成立，专访实验室主任翟荟 — 新京报</a></li>
<li><a href="https://www.163.com/dy/article/L2A10OTS05118DFD.html">163.com/dy/article/L2A10OTS05118DFD.html</a></li>
<li><a href="https://kfqgw.beijing.gov.cn/ywdt/kjcgzhgd/kjqy/202603/t20260313_4556614.html">kfqgw.beijing.gov.cn/ywdt/kjcgzhgd/kjqy/202603/t20260313_4556614....</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#funding`, `#cold atom`, `#China tech`

---

<a id="item-14"></a>
## [Furtex Toolkit Uses io_uring and eBPF to Evade EDR and Falco](https://news.google.com/rss/articles/CBMiVkFVX3lxTE95ZEp2cGFnVUZwVVpHNkhabTVzNTFuY2Zsa1V1eGZmaHVVbjlGNXZOc1RwMnYyVlI2UEFKcVktN0ZhYlpvMVEwQm9YN2JEZkN0Zkw5LXZn0gFbQVVfeXFMUFZjeWxiak1MN1ZnTmpkbW5ra3lGbi00U3Z2Z0RwRDZDNTlLMF9jM0dFTnNKMkFabVA0N213WTlla1k3d0E1NkJZQ3MtMTZUdWY2MmZhSzRKSXV2OA?oc=5) ⭐️ 6.0/10

A new Linux toolkit named Furtex has been discovered that leverages io_uring and eBPF to bypass Endpoint Detection and Response (EDR) systems and Falco runtime security monitoring. This development highlights a new class of evasion techniques that abuse legitimate kernel features, posing a significant challenge to Linux security tools and potentially enabling stealthy malware operations. Furtex uses io_uring for asynchronous I/O to avoid syscall-based monitoring and eBPF to hook or modify kernel behavior without triggering detection rules. The toolkit specifically targets Falco, a popular runtime security tool, by bypassing its default rule set.

google_news · gbhackers.com · Jul 20, 06:39

**Background**: io_uring is a Linux kernel interface for asynchronous I/O that reduces syscall overhead, while eBPF allows running sandboxed programs in the kernel for observability and security. EDR systems and Falco typically monitor syscalls and kernel events to detect malicious activity, but Furtex exploits these technologies to perform operations outside traditional monitoring paths.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">io _ uring - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/EBPF">eBPF - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/379268668_Bypassing_Falco_How_to_Compromise_a_Cluster_without_Tripping_the_SOC">(PDF) Bypassing Falco : How to Compromise a Cluster without...</a></li>

</ul>
</details>

**Tags**: `#io_uring`, `#eBPF`, `#EDR bypass`, `#Linux security`, `#Falco`

---

<a id="item-15"></a>
## [Chinese AI Model Pauses Subscriptions Due to Demand](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNYU9Sc2MyX3JvN0FxWnRqTzAzV0hPXzUzN214bU1yRW1HVjFsWXRQVm9hejVRODB3M0czVTV1WWpGYVg4dy1xU19mV3B3RWxUVVVaQWN2Vmt0ZHM2TURaTDZka2dhenVsUmtybVg2MTZQWjM4aHpBUXUyUEZZWTY4WW1HdFdyd1pIYjl1V3ExOGlyUXNEb214WFhDQ0ZycnV1a1JKdXpmbmo3WWs?oc=5) ⭐️ 6.0/10

A new Chinese AI model has temporarily halted new subscriptions because demand has overwhelmed its capacity. This indicates strong market interest in Chinese AI models and highlights infrastructure scaling challenges. The specific model name and developer have not been disclosed in the report. The pause is likely temporary while capacity is expanded.

google_news · WSLS · Jul 20, 10:16

**Background**: AI models require significant computational resources for inference, and sudden popularity can exceed available server capacity. Similar incidents have occurred with other AI services globally.

**Tags**: `#AI model`, `#China`, `#demand`, `#subscription`

---