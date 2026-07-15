---
layout: default
title: "Horizon Summary: 2026-07-16 (EN)"
date: 2026-07-16
lang: en
---

> From 145 items, 21 important content pieces were selected

---

1. [Hugging Face Transformers v5.14.0 Adds Inkling, a 975B Open Multimodal Model](#item-1) ⭐️ 9.0/10
2. [AsyncAPI npm Supply Chain Attack Delivers Miasma Botnet](#item-2) ⭐️ 9.0/10
3. [Stripe and Advent Jointly Bid to Acquire PayPal](#item-3) ⭐️ 8.0/10
4. [Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon](#item-4) ⭐️ 8.0/10
5. [Model Routing: Simple Concept, Complex Reality](#item-5) ⭐️ 8.0/10
6. [Hugging Face Launches Real World VoiceEQ Benchmark for Voice AI](#item-6) ⭐️ 8.0/10
7. [Hack reveals Suno AI music generator scraped YouTube audio](#item-7) ⭐️ 8.0/10
8. [Apple Intelligence Approved in China via Alibaba's Qwen AI](#item-8) ⭐️ 8.0/10
9. [Vint Cerf Develops Standard to Identify AI Agents Online](#item-9) ⭐️ 8.0/10
10. [OpenAI researcher Miles Wang in talks to launch $2B AI drug discovery startup](#item-10) ⭐️ 8.0/10
11. [Claude web_fetch bypass enables memory exfiltration](#item-11) ⭐️ 8.0/10
12. [Mianbi's MiniCPM On-Device AI to Debut on Samsung Phones](#item-12) ⭐️ 8.0/10
13. [Thermodynamic Computers Harness Random Energy Fluctuations](#item-13) ⭐️ 8.0/10
14. [Auditing Dutch Risk Algorithm with Unsupervised Bias Tool](#item-14) ⭐️ 8.0/10
15. [White House May Regulate Open-Source AI Models](#item-15) ⭐️ 8.0/10
16. [Xiaomi Open-Sources 38B-Parameter Embodied AI Model Robotics-U0](#item-16) ⭐️ 8.0/10
17. [Video Generation Pre-Training Unifies Six Vision Tasks](#item-17) ⭐️ 8.0/10
18. [Google Releases LiteRT.js for WebGPU ML Inference](#item-18) ⭐️ 8.0/10
19. [Lessons from Building Shippy AI Agent](#item-19) ⭐️ 7.0/10
20. [AI coding tools make software disposable](#item-20) ⭐️ 7.0/10
21. [RK3576 NPU support added to open-source Rocket driver](#item-21) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Hugging Face Transformers v5.14.0 Adds Inkling, a 975B Open Multimodal Model](https://github.com/huggingface/transformers/releases/tag/v5.14.0) ⭐️ 9.0/10

Hugging Face Transformers v5.14.0 integrates Inkling, a massive open-weight multimodal model from Thinking Machines Lab with 975B total parameters (41B active), supporting text, image, and audio inputs and generating text outputs. Inkling is one of the largest open-weight multimodal models available, enabling developers to build agentic systems, coding assistants, and chatbots with advanced multimodal understanding. Its inclusion in Transformers lowers the barrier for researchers and enterprises to experiment with and fine-tune a frontier-level model. Inkling uses a Mixture-of-Experts (MoE) transformer architecture with a 1M-token context window and was pretrained on 45 trillion tokens of text, images, audio, and video. The release also includes TIPSv2 models, performance improvements like Flash Attention fixes, and new generation features such as Multi-Token Prediction (MTP) support.

github · ArthurZucker · Jul 15, 19:02

**Background**: Hugging Face Transformers is a widely-used open-source library for natural language processing and multimodal AI, providing thousands of pretrained models. Inkling is developed by Thinking Machines Lab, an AI startup founded by former OpenAI CTO Mira Murati, which raised $2 billion in funding. Open-weight models allow researchers and developers to inspect, fine-tune, and deploy models freely, fostering innovation and transparency.

<details><summary>References</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://en.wikipedia.org/wiki/Thinking_Machines_Lab">Thinking Machines Lab</a></li>
<li><a href="https://www.baseten.co/library/inkling/">Inkling | Model library</a></li>

</ul>
</details>

**Discussion**: Community members expressed excitement about Inkling's multimodal capabilities, especially audio support, and noted its potential for agentic applications. Some highlighted that Thinking Machines Lab could become a key open-weight competitor, similar to DeepSeek or Z.ai, while others appreciated the business model of offering fine-tuning on Tinker.

**Tags**: `#transformers`, `#multimodal`, `#open-weights`, `#AI`, `#model-release`

---

<a id="item-2"></a>
## [AsyncAPI npm Supply Chain Attack Delivers Miasma Botnet](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNQUJWWGM1MGRzdlJsT3RCb1RyVXFabXJidFNIdXBtUHcxWDE4bVB1QkdMemFnQVNnT0p1WmlyNlp1Tk13OXNPMlVwaU5SdlZFbXNzOGNnUEg1X1VaZXpScDZzVVpvMWktdFVpNW52aWp6QnFUR3NuMmpueWpOcUNUWFhmOC1PVmNkNFNlaE4wbjRuOW5lMC1Pa1NYMGY4OVpfQ2tOZXBjQUF3eVczdGpLNjVLcWRFejNIX1pZRTZVbUtEZ2wyVlhSQ0IyNW13ZTFoRzNYbE1nU1l4dFlmeFlMMkNSTQ?oc=5) ⭐️ 9.0/10

An active supply chain attack on the AsyncAPI npm package has been discovered, where compromised GitHub Actions were used to publish malicious versions of AsyncAPI packages that deliver a multi-stage Miasma botnet. The attack was first detected on July 14, 2026, and involves at least five malicious package versions. This attack compromises the software supply chain, potentially affecting thousands of developers and organizations that rely on AsyncAPI for API documentation and code generation. The use of compromised CI/CD pipelines (GitHub Actions) to distribute malware represents a sophisticated and dangerous escalation in supply chain threats. The malicious packages were published through the project's legitimate GitHub Actions release workflow, indicating that the attackers gained access to the repository's secrets or tokens. The Miasma botnet includes credential-stealing capabilities and a remote access trojan, and the malware executes when the library is loaded, not just on install.

google_news · Rescana · Jul 15, 11:57

**Background**: AsyncAPI is an open-source specification for describing event-driven APIs, similar to OpenAPI for REST APIs. The npm packages are used to generate code and documentation from AsyncAPI definitions. Supply chain attacks on npm have become increasingly common, but compromising GitHub Actions to inject malware into legitimate releases is a more advanced technique that bypasses typical security checks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions">AsyncAPI Supply Chain Compromise via GitHub Actions | Wiz Blog</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/-asyncapi-npm-packages-infected-with-credential-stealing-malware/">AsyncAPI npm packages infected with credential-stealing malware</a></li>
<li><a href="https://www.stepsecurity.io/blog/compromised-next-branch-pushes-malicious-asyncapi-generator-generator-helpers-and-generator-components-to-npm">Coordinated AsyncAPI Supply Chain Attack: Miasma RAT ...</a></li>

</ul>
</details>

**Tags**: `#supply chain attack`, `#npm`, `#botnet`, `#GitHub Actions`, `#security`

---

<a id="item-3"></a>
## [Stripe and Advent Jointly Bid to Acquire PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 8.0/10

Stripe and private equity firm Advent International have reportedly made a joint offer to acquire PayPal for over $53 billion, according to sources familiar with the matter. This acquisition would consolidate major payment platforms—Stripe, PayPal, Venmo, Braintree, and Xoom—under one umbrella, raising significant antitrust concerns and potentially reshaping the online payments industry. The deal values PayPal at over $53 billion, and if completed, would combine Stripe's developer-friendly payment infrastructure with PayPal's vast user base and bank charter, potentially enabling Stripe to offer new financial services.

hackernews · rvz · Jul 15, 03:32 · [Discussion](https://news.ycombinator.com/item?id=48915953)

**Background**: Stripe is a leading online payment processor known for its developer tools, while PayPal is a widely used digital wallet and payment platform. Advent International is a global private equity firm with experience in fintech investments. The acquisition would face intense antitrust scrutiny due to market concentration in online card-not-present transactions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stripe,_Inc.">Stripe , Inc. - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advent_International">Advent International - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members expressed concerns about reduced competition, potential fee increases, and Stripe's restrictive policies on certain industries (e.g., cannabis, adult) that PayPal currently allows. Some noted the antitrust hurdles and the possibility that Stripe could leverage PayPal's bank charter to expand its services.

**Tags**: `#acquisition`, `#payments`, `#antitrust`, `#fintech`, `#Stripe`

---

<a id="item-4"></a>
## [Running Gemma 4 26B at 5 tokens/sec on a 13-year-old Xeon](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) ⭐️ 8.0/10

A technical blog post demonstrates running Google's Gemma 4 26B A4B model at 5 tokens per second on a 13-year-old Intel Xeon CPU without any GPU, using extreme optimization techniques. This shows that large language models can be run on extremely old and low-cost hardware, potentially democratizing access to AI and reducing reliance on expensive GPUs. The Gemma 4 26B model uses a Mixture-of-Experts (MoE) architecture with 26B total parameters and 4B active parameters per token, which enables efficient inference on CPU. The blog likely employs quantization, memory optimization, and efficient token generation to achieve 5 tokens/sec.

hackernews · neomindryan · Jul 15, 15:34 · [Discussion](https://news.ycombinator.com/item?id=48922434)

**Background**: Large language models typically require powerful GPUs for inference due to their massive size and computational demands. However, techniques like quantization, pruning, and efficient architectures (e.g., MoE) can reduce resource requirements. Running such models on CPU is challenging but possible with aggressive optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/google/gemma-4-26B-A4B-it">google/gemma-4-26B-A4B-it · Hugging Face</a></li>
<li><a href="https://deepmind.google/models/gemma/gemma-4/">Gemma 4 — Google DeepMind</a></li>
<li><a href="https://community.intel.com/t5/Blogs/Tech-Innovation/Artificial-Intelligence-AI/Intel-Xeon-is-all-you-need-for-AI-inference-Performance/post/1506083">Intel Xeon is all you need for AI inference: Performance Leadership on Real World Applications - Intel Community</a></li>

</ul>
</details>

**Discussion**: Commenters debate the cost efficiency of local inference vs. cloud APIs, noting that electricity costs for old CPUs may exceed API prices. Some share their own benchmarks on similar hardware, reporting 8-12 tokens/sec, while others predict that by mid-2027, 200B+ MoE models will run on consumer hardware.

**Tags**: `#LLM inference`, `#hardware optimization`, `#local AI`, `#cost analysis`, `#open source`

---

<a id="item-5"></a>
## [Model Routing: Simple Concept, Complex Reality](https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt) ⭐️ 8.0/10

A new blog post from IBM Research on Hugging Face explores the hidden complexities and trade-offs in building effective model routing systems for large language models, revealing that what seems straightforward is fraught with challenges. As organizations deploy multiple LLMs to balance cost, latency, and quality, model routing becomes critical for efficient inference; understanding its nuances helps practitioners avoid pitfalls and build more robust AI systems. The article likely discusses challenges such as routing accuracy, dynamic model performance, and the overhead of routing decisions, emphasizing that simple heuristics often fail in production environments.

rss · Hugging Face Blog · Jul 15, 17:27

**Background**: Model routing is a technique where a system selects the most appropriate LLM from a pool for each incoming prompt, aiming to minimize cost while maintaining quality. It is a key component of multi-LLM serving systems, which are increasingly used to optimize inference trade-offs between throughput, latency, and cost.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ulab-uiuc/LLMRouter">GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source Library for LLM Routing · GitHub</a></li>
<li><a href="https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/">Multi-LLM routing strategies for generative AI applications on AWS | Artificial Intelligence</a></li>
<li><a href="https://arxiv.org/abs/2502.08773">[2502.08773] Universal Model Routing for Efficient LLM Inference</a></li>

</ul>
</details>

**Tags**: `#model routing`, `#LLM`, `#inference`, `#systems`, `#AI engineering`

---

<a id="item-6"></a>
## [Hugging Face Launches Real World VoiceEQ Benchmark for Voice AI](https://huggingface.co/blog/real-world-voiceeq) ⭐️ 8.0/10

Hugging Face, in collaboration with Hume AI, introduced Real World VoiceEQ, a benchmark designed to evaluate voice AI systems on human-perceived quality rather than purely technical accuracy. This benchmark addresses a critical gap in current voice AI evaluation, where standard metrics often fail to capture whether a system sounds natural or responds appropriately, potentially driving improvements in user experience across voice applications. The benchmark includes 785,000 TTS ratings and 48,000 STS ratings, making it one of the largest human evaluations of voice AI to date, and it evaluates models across ASR, TTS, speech-to-speech, and speech understanding tasks.

rss · Hugging Face Blog · Jul 15, 00:00

**Background**: Voice AI systems are typically evaluated using technical metrics like word error rate (WER) for ASR or mean opinion score (MOS) for TTS, but these often fail to capture human perception of naturalness, emotion, or appropriateness. Real World VoiceEQ aims to measure qualities such as tone, emotion, speaker identity, and background context that transcripts alone cannot convey.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hume.ai/blog/introducing-real-world-voiceeq-measuring-the-human-quality-of-voice-ai">Introducing Real World VoiceEQ: Measuring the Human Quality ...</a></li>
<li><a href="https://www.zal-group.com/news/product-model-releases/hugging-face-real-world-voiceeq-voice-ai-benchmark">Hugging Face Launches Real World VoiceEQ Benchmark for Voice AI</a></li>
<li><a href="https://andresseo.expert/ai/humeai-real-world-voiceeq-benchmark-exposes-voice-ais-blind-spots-in-human-interaction/">Real World VoiceEQ: Benchmarking Voice AI's Human Quality</a></li>

</ul>
</details>

**Tags**: `#voice AI`, `#benchmark`, `#speech technology`, `#AI evaluation`

---

<a id="item-7"></a>
## [Hack reveals Suno AI music generator scraped YouTube audio](https://techcrunch.com/2026/07/15/hack-suggests-ai-music-generator-suno-scraped-youtube-for-training-data/) ⭐️ 8.0/10

A hacker used an employee's credentials to access Suno's source code, revealing that the AI music generator scraped decades of YouTube audio for training data. This discovery has significant implications for AI training data ethics and copyright law, potentially affecting legal frameworks and public trust in AI companies. The hack provided concrete evidence of scraping YouTube, which Suno had not publicly disclosed. The incident also highlights security vulnerabilities in AI companies.

rss · TechCrunch AI · Jul 15, 17:00

**Background**: Suno is an AI music generator that creates songs from text prompts. Training such models typically requires large datasets of audio recordings, and many AI companies scrape publicly available data from the internet, often raising copyright concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://suno.com/l/ai-music-app">Suno: The AI Music App for Every Creator</a></li>
<li><a href="https://suno.com/l/ai-music-generator">AI Music Generator: Turn Your Ideas into Tracks That Slap</a></li>

</ul>
</details>

**Tags**: `#AI`, `#music generation`, `#data scraping`, `#copyright`, `#security`

---

<a id="item-8"></a>
## [Apple Intelligence Approved in China via Alibaba's Qwen AI](https://techcrunch.com/2026/07/15/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/) ⭐️ 8.0/10

Apple's AI platform, Apple Intelligence, has been officially approved for launch in China through a partnership with Alibaba's Qwen AI (Tongyi Qianwen). This confirms earlier rumors and marks a major step for Apple's AI ambitions in the Chinese market. This partnership is significant because it allows Apple to offer AI features in China, a key market where foreign AI services often face regulatory hurdles. It also strengthens Alibaba's position in the AI race and intensifies competition with other AI providers in China. Apple Intelligence is available on iPhone 15 Pro and later models, integrating large language models into Siri and other apps. The partnership with Alibaba likely involves using Qwen models to comply with Chinese regulations while delivering AI capabilities.

rss · TechCrunch AI · Jul 15, 15:29

**Background**: Apple Intelligence is Apple's personal intelligence system powered by next-generation foundation models, bringing AI capabilities to iPhone, iPad, Mac, and other devices. Qwen (Tongyi Qianwen) is a family of large language models developed by Alibaba Cloud, some of which are open-source. China requires foreign AI services to partner with local companies to operate legally, making this deal necessary for Apple's AI launch in the country.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IOS_18">iOS 18 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>
<li><a href="https://www.apple.com/apple-intelligence/">Apple Intelligence and Siri - Apple</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Alibaba`, `#Qwen AI`, `#AI`, `#China`

---

<a id="item-9"></a>
## [Vint Cerf Develops Standard to Identify AI Agents Online](https://techcrunch.com/2026/07/15/vint-cerf-is-working-on-a-plan-to-unleash-ai-agents-on-the-open-internet/) ⭐️ 8.0/10

Vint Cerf, co-creator of TCP/IP, is leading an initiative to create identification protocols for AI agents on the open internet, aiming to ensure transparency and accountability. This standard could enable AI agents to interoperate safely across the open web, moving beyond proprietary systems and shaping future internet governance and AI interoperability. Cerf joins other internet luminaries in this effort, which comes shortly after his retirement from Google after 21 years as chief internet evangelist.

rss · TechCrunch AI · Jul 15, 12:00

**Background**: AI agents are software programs that perform tasks autonomously, but most currently operate within closed, proprietary systems. Vint Cerf is known for co-designing TCP/IP, the foundational protocol of the internet. This initiative aims to create open standards for identifying AI agents, similar to how IP addresses identify devices.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/15/vint-cerf-is-working-on-a-plan-to-unleash-ai-agents-on-the-open-internet/">Vint Cerf is working on a plan to unleash AI agents on the ...</a></li>
<li><a href="https://www.techtimes.com/articles/320264/20260712/vint-cerf-retires-google-warning-ai-agents-need-real-protocols.htm">Vint Cerf Retires From Google With A Warning: AI Agents Need ...</a></li>
<li><a href="https://explore.n1n.ai/blog/vint-cerf-ai-agent-standards-open-internet-2026-07-15">Vint Cerf Proposes New Standards for AI Agents on the Open ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#internet standards`, `#Vint Cerf`, `#AI governance`, `#protocols`

---

<a id="item-10"></a>
## [OpenAI researcher Miles Wang in talks to launch $2B AI drug discovery startup](https://techcrunch.com/2026/07/14/openai-researcher-miles-wang-in-talks-to-launch-ai-drug-discovery-startup-valued-at-2b/) ⭐️ 8.0/10

OpenAI researcher Miles Wang is reportedly in discussions to launch an AI-powered drug discovery startup with a valuation of $2 billion, reflecting strong investor enthusiasm for applying AI to life sciences. This news underscores the growing trend of AI talent moving into biotech, potentially accelerating drug development and reducing costs, which could transform the pharmaceutical industry. The startup is still in early-stage talks, and no official name or specific focus has been disclosed; the $2 billion valuation is reportedly based on investor interest rather than proven technology.

rss · TechCrunch AI · Jul 15, 00:27

**Background**: AI drug discovery uses machine learning to identify disease targets, generate candidate compounds, and predict safety, potentially shortening the typical 10-15 year drug development timeline. Companies like Insilico Medicine and Recursion Pharmaceuticals have already attracted significant investment in this space.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41591-024-03434-4">Artificial intelligence in drug development | Nature Medicine</a></li>
<li><a href="https://www.weforum.org/stories/all/how-ai-is-reshaping-drug-discovery/">Here’s how AI is reshaping drug discovery | World Economic Forum</a></li>

</ul>
</details>

**Tags**: `#AI`, `#drug discovery`, `#startup`, `#biotech`, `#investment`

---

<a id="item-11"></a>
## [Claude web_fetch bypass enables memory exfiltration](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

Researcher Ayush Paul discovered a bypass in Claude's web_fetch tool that allowed data exfiltration of user memories by crafting a honeypot website that tricked the agent into following nested links. Anthropic has since closed the loophole by preventing web_fetch from navigating to links within fetched content. This attack demonstrates a novel bypass of Anthropic's data exfiltration protections, highlighting the persistent challenge of securing LLM agents against prompt injection. It underscores the need for robust isolation between private data, untrusted content, and external communication channels. The attack exploited a loophole where web_fetch could follow URLs embedded in previously fetched pages, allowing a multi-step exfiltration chain. The honeypot site only served the malicious prompt to clients with a 'Claude-User' user-agent to evade detection.

rss · Simon Willison · Jul 15, 14:21

**Background**: LLM agents like Claude face a 'lethal trifecta' risk when they have access to private data, process untrusted content, and can communicate externally. Prompt injection attacks can trick the model into exfiltrating sensitive information by embedding it in URLs. Anthropic had previously restricted web_fetch to only navigate to user-provided or search-returned URLs, but the new attack found a way around this by chaining through fetched page links.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Docs</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and external communication</a></li>
<li><a href="https://www.osohq.com/learn/lethal-trifecta-ai-agent-security">Understanding the Lethal Trifecta of AI Agents</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion likely expressed concern over the ease of the bypass and frustration that Anthropic did not pay a bug bounty, though some may have acknowledged the company's internal discovery. The attack reinforces calls for more fundamental architectural safeguards against prompt injection.

**Tags**: `#AI safety`, `#LLM security`, `#data exfiltration`, `#Claude`, `#prompt injection`

---

<a id="item-12"></a>
## [Mianbi's MiniCPM On-Device AI to Debut on Samsung Phones](https://36kr.com/p/3896830362601351?f=rss) ⭐️ 8.0/10

Mianbi Intelligence has partnered with Samsung to integrate its MiniCPM series on-device models into several flagship Samsung phones, coinciding with Chinese regulatory approval of seven on-device generative AI services including Apple Intelligence and MiniCPM. This marks a major milestone for on-device AI, moving from concept to large-scale deployment on smartphones, and signals a shift toward specialized AI model providers supplying phone makers rather than relying solely on in-house development. Mianbi's MiniCPM5-1B model with only 1 billion parameters outperforms larger open-source models on the Artificial Analysis Intelligence Index, while MiniCPM-V 4.6 runs on just 6GB of memory. The company has raised over 5 billion RMB cumulatively by mid-2026, with a valuation exceeding 20 billion RMB.

rss · 36氪 · Jul 15, 11:47

**Background**: On-device AI runs models directly on smartphones rather than in the cloud, offering lower latency and better privacy. Mianbi Intelligence, spun off from Tsinghua University's NLP lab, pioneered the 'Densing Law' which states that the parameter count needed for a given intelligence level halves every 3.5 months, enabling powerful models to run on resource-constrained devices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cac.gov.cn/2026-07/15/c_1785861480767004.htm">关于发布7款提供手机端侧生成式人工智能服务已备案信息的公告_中央网...</a></li>
<li><a href="https://modelbest.cn/">ModelBest - 面壁智能</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/1961168095851819213">端上大模型（面壁智能）：MiniCPM4、MiniCPM-V、MiniCPM-V 4.5、AgentCPM-GUI - 知乎</a></li>

</ul>
</details>

**Tags**: `#on-device AI`, `#smartphone`, `#generative AI`, `#China`, `#partnership`

---

<a id="item-13"></a>
## [Thermodynamic Computers Harness Random Energy Fluctuations](https://www.quantamagazine.org/thermodynamic-computers-go-with-the-energy-flow-20260715/) ⭐️ 8.0/10

A new computing paradigm called thermodynamic computing proposes to use random energy fluctuations for computation instead of fighting them, potentially revolutionizing energy efficiency in computers. This approach could dramatically reduce the energy consumption of computing, addressing a critical bottleneck in modern hardware, especially for AI and large-scale data centers. Thermodynamic computers would operate by harnessing natural thermal fluctuations, turning noise into a resource rather than a problem to be mitigated.

rss · Quanta Magazine · Jul 15, 15:24

**Background**: Conventional computers require precise control and error correction to avoid random energy fluctuations that can cause errors. Thermodynamic computing flips this by designing systems that inherently use these fluctuations to perform computations, inspired by principles from statistical mechanics and thermodynamics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.quantamagazine.org/thermodynamic-computers-go-with-the-energy-flow-20260715/">Thermodynamic Computers Go With the ( Energy )... | Quanta Magazine</a></li>
<li><a href="https://extropic.ai/writing/thermodynamic-computing-from-zero-to-one">Thermodynamic Computing: From Zero to One | Extropic</a></li>
<li><a href="https://arxiv.org/abs/1911.01968">[1911.01968] Thermodynamic Computing</a></li>

</ul>
</details>

**Tags**: `#thermodynamic computing`, `#energy efficiency`, `#computer architecture`, `#physics of computation`

---

<a id="item-14"></a>
## [Auditing Dutch Risk Algorithm with Unsupervised Bias Tool](https://news.google.com/rss/articles/CBMiZ0FVX3lxTFBVZ1hGNGJ3aFh6Zm9tMlQtMzVwNm1CT3liVTZYRFZMQTJIeldpVjNRUzE0bkNCdmUybnhGWjQ2M0hFMUJKcS1aM0FVVFg3ZFN6MkxMMV9JclVFMllObUQ0bUYxUGJpb0E?oc=5) ⭐️ 8.0/10

Researchers audited a Dutch public sector risk profiling algorithm (DUO) using an unsupervised bias detection tool that identifies unfairly treated groups via clustering. The tool detected statistically significant disparities in misclassification rates across student groups. This work demonstrates a practical, model-agnostic approach to auditing algorithmic fairness in high-stakes public sector decisions. It provides a template for regulators and auditors to detect intersectional bias without requiring sensitive demographic labels. The tool uses hierarchical clustering to find groups with elevated misclassification rates, then tests for statistical significance. The audit focused on DUO's risk profiling for student financial aid, which differentiated by education type (MBO, HBO, WO).

google_news · The Association for the Advancement of Artificial Intelligence · Jul 15, 12:40

**Background**: Algorithmic bias in public sector risk profiling can lead to unfair treatment of citizens. Traditional bias audits often require labeled sensitive attributes (e.g., race, gender), which may be unavailable or legally restricted. Unsupervised bias detection tools use clustering to identify potentially disadvantaged groups without such labels, making them suitable for privacy-preserving audits.

<details><summary>References</summary>
<ul>
<li><a href="https://oecd.ai/en/catalogue/tools/unsupervised-bias-detection-tool">Unsupervised bias detection tool - OECD.AI</a></li>
<li><a href="https://github.com/NGO-Algorithm-Audit/unsupervised-bias-detection">GitHub - NGO-Algorithm-Audit/unsupervised-bias-detection: Unsupervised bias detection tool for binary AI classifiers. Including qualitative approach to assess quantitative disparities. · GitHub</a></li>
<li><a href="https://arxiv.org/pdf/2502.01713">Auditing a Dutch Public Sector Risk Profiling Algorithm Using an...</a></li>

</ul>
</details>

**Tags**: `#algorithmic bias`, `#AI fairness`, `#public sector`, `#unsupervised learning`, `#auditing`

---

<a id="item-15"></a>
## [White House May Regulate Open-Source AI Models](https://news.google.com/rss/articles/CBMiowFBVV95cUxNWkotcmhYOVRZUGU4MjFHS3hrU2x0ekNxNTBWNkpMczBUVTZLNDU5OVVSQUxQZjR2aXExbnduRERxTWJZcmIwUnNGNkU1X2NHbVg2SjQwQXZlZ0tsRmlHQ3d2UUdsZVlWZ08yY3ZNVE9EQk53Tkl1RjdzbGZHVXlZYW4yUjc0dWZqaFlRX05yeVF2RXhrYmlEWWw4RmlUZmI5WVcw?oc=5) ⭐️ 8.0/10

The White House has indicated it is not ruling out potential actions regarding open-source AI models, signaling a possible shift toward regulation of these widely used systems. This could impact the development and deployment of open-source AI, affecting researchers, startups, and large tech companies that rely on these models, and may shape global AI policy. The White House has not specified what actions it might take, but the statement comes amid broader discussions on AI regulation, including a voluntary regulatory framework for frontier AI models.

google_news · Semafor · Jul 15, 09:17

**Background**: Open-source AI models are publicly available systems that anyone can use, modify, and distribute. They have driven innovation but also raised concerns about misuse, such as generating harmful content or enabling disinformation. The White House has previously urged Congress to take a light-touch approach to AI regulation, but this new signal suggests a potential tightening.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnn.com/2026/03/20/tech/white-house-ai-framework">The White House just laid out how it wants to regulate AI</a></li>
<li><a href="https://apnews.com/article/white-house-donald-trump-artificial-intelligence-479eb3d0a50fe7237678a9bfb146ac7a">White House urges Congress to take a light touch on AI ...</a></li>
<li><a href="https://www.crowell.com/en/insights/client-alerts/executive-order-creates-voluntary-regulatory-regime-of-frontier-ai-models">Executive Order Creates Voluntary Regulatory Regime of ...</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open-source`, `#regulation`, `#White House`

---

<a id="item-16"></a>
## [Xiaomi Open-Sources 38B-Parameter Embodied AI Model Robotics-U0](https://news.google.com/rss/articles/CBMic0FVX3lxTE5odUpqMEVaT2wxbkhXa2puWG5KOGRlZmRpalVQNHB6cDJEQnh4RDAyeEpSR1FxYUxqQVpYSHZYTW0zSDh0TWNIcm9BTkVISG1udGFpQ2ozOGRxeURKd2RGN1NJUUVGaWE5WFFKOUFKNlgwM0E?oc=5) ⭐️ 8.0/10

Xiaomi has open-sourced Robotics-U0, a 38-billion-parameter embodied generative model that unifies four robot tasks: scene generation, embodied transfer, video generation, and text-to-image. The model can generate robot training data up to 83 times faster than existing methods. This release addresses the critical bottleneck of scarce real robot interaction data in embodied AI, potentially accelerating robot training and development. As an open-source model, it lowers the barrier for researchers and developers to advance robotics and embodied intelligence. Robotics-U0 is a multimodal autoregressive world foundation model with 38 billion parameters, designed to unify multiple robot tasks within a single architecture. It was released by the Xiaomi Robotics Team on July 15, 2026, and is available as open-source.

google_news · Pandaily · Jul 15, 07:53

**Background**: Embodied AI refers to AI systems that can perceive, reason, and act in the physical world, such as robots. Generative models in this context can create synthetic training data, reducing the need for costly real-world data collection. Xiaomi's model is among the largest open-source embodied AI models, combining generative capabilities with task unification.

<details><summary>References</summary>
<ul>
<li><a href="https://robottoday.com/industry-briefing/xiaomi-launches-robotics-u0-a-unified-38b-parameter-generative-model-for-robotics/8654">Xiaomi Launches Robotics-U0: A Unified 38B-Parameter ...</a></li>
<li><a href="https://happyrock.cloud/blog/2026-07-15_xiaomi_robotics_u0_38b_world_model_embodied_ai_data_engine_en/">Xiaomi-Robotics-U0 Deep Dive: 38B Parameter World Model ...</a></li>
<li><a href="https://edgen.beta.edgen.tech/zh/news/post/xiaomi-open-sources-38b-parameter-robotics-model-to-mass-produce-robot-training-data">Xiaomi open-sources 38B-parameter robotics model to mass ...</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#AI`, `#open-source`, `#embodied AI`, `#Xiaomi`

---

<a id="item-17"></a>
## [Video Generation Pre-Training Unifies Six Vision Tasks](https://news.google.com/rss/articles/CBMi0wFBVV95cUxPejlnMDhlc243a2JzRjViZzNtQU1BMDJ5THZxLVE1Zkx6ck9jMi1rVlJQTVF4LVZhSlZuWm15Vjhtd25Tbzd2WklpOVRnbWF2YnBrOVF4QnJ3VE5ETVAycXotNmFLLWJEdGlFZDhOVkxSNnM0WnhkR1h2a1h1MzBkZnJRTTFoWGhRUjZuRGZ5YmZGdGV5bWp1d0oydm9mMEk1MDN3QlljVDNqM2toTk8tRzNlVm4welZJeU1lMm1GOVJUUHpZUXVwVlg2UDRXMHdRN2t3?oc=5) ⭐️ 8.0/10

Google DeepMind's GenCeption, presented at ECCV 2026, shows that a single video diffusion model pre-trained on video generation can match or beat specialist models on depth estimation, normal prediction, pose estimation, segmentation, and other vision tasks using up to 90% less data. This breakthrough suggests that video generation pre-training can serve as a general-purpose visual learner, potentially reducing the need for task-specific architectures and large labeled datasets in computer vision. The model is steered by text instructions and operates in a feed-forward manner, without task-specific fine-tuning. It unifies six tasks: depth, normals, pose, segmentation, edge detection, and object detection.

google_news · Tech Times · Jul 15, 13:07

**Background**: Traditional computer vision relies on separate specialist models for each task, each requiring its own architecture and labeled data. Video generation models like diffusion models learn rich spatiotemporal representations from large-scale video datasets. GenCeption repurposes such a pre-trained generative model as a unified vision encoder, demonstrating that generative pre-training can transfer to discriminative tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/320556/20260715/video-generation-pre-training-unifies-six-vision-tasks-beats-specialists-less-data.htm">Video Generation Pre-Training Unifies Six Vision Tasks, Beats ...</a></li>
<li><a href="https://genception.github.io/">Video Generation Models are General-Purpose Vision Learners</a></li>

</ul>
</details>

**Tags**: `#computer vision`, `#pre-training`, `#video generation`, `#AI research`

---

<a id="item-18"></a>
## [Google Releases LiteRT.js for WebGPU ML Inference](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNVHhUbUJZekhlMW5zenUtYkhVRGg1dUxEM2lJOUd5cnhMUjJCM0VPS1JnUHd0aWEzejN3T09hSlc4NW5pemJiWHNjVTRiWHFIYW5pUTRNb2RJbk1FUHpUU2ZaYWF4TEd5dmQtTDd3Z3ZuT1A0RGItd1g4QVV4d2w2RlJaV2xLbVlIQnhGLTZQQUhhdWoxV2JmTjRmenl3UXgzRVJYYnhUM1pSbURRVl81alp0UElScC1rVFlYVHpqMnVUS3M5MUdJeEpKcThUTW1mV3RpMlUwcVROOWFV?oc=5) ⭐️ 8.0/10

Google has released LiteRT.js, a JavaScript binding of LiteRT that enables running .tflite machine learning models directly in web browsers using the WebGPU API for hardware acceleration. This brings high-performance on-device AI inference to web applications, allowing developers to deploy models across Android, iOS, and web from a shared ecosystem without manual platform tuning, enhancing privacy and responsiveness. LiteRT.js is part of Google AI Edge and supports multi-framework models, including simplified conversion from PyTorch. It abstracts hardware-level optimizations, leveraging WebGPU for GPU acceleration in browsers.

google_news · MarkTechPost · Jul 15, 07:36

**Background**: LiteRT is Google's lightweight runtime for on-device machine learning, previously known as TensorFlow Lite. WebGPU is a modern web standard that provides low-level GPU access, superseding WebGL. .tflite is the model format used by TensorFlow Lite and LiteRT.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.googleblog.com/litertjs-googles-high-performance-web-ai-inference/">LiteRT . js , Google's high performance Web AI Inference</a></li>
<li><a href="https://ai.google.dev/edge/litert/web?trk=article-ssr-frontend-pulse_little-text-block">LiteRT for Web with LiteRT . js | Google AI Edge | Google AI for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU</a></li>

</ul>
</details>

**Tags**: `#Google`, `#LiteRT.js`, `#WebGPU`, `#Machine Learning`, `#JavaScript`

---

<a id="item-19"></a>
## [Lessons from Building Shippy AI Agent](https://huggingface.co/blog/allenai/shippy-tech-blog) ⭐️ 7.0/10

Ai2 published a blog post detailing the design decisions, challenges, and lessons learned from building Shippy, an AI agent for maritime domain awareness. This provides practical, real-world insights for AI/ML practitioners on building reliable agents, emphasizing that deterministic tools and guardrails matter more than the model itself. Shippy is built on Ai2's Skylight ocean-monitoring platform and answers plain-language questions using live vessel data. The blog highlights that reliable agents depend on deterministic tools, explicit guardrails, isolated infrastructure, and evaluations grounded in real-world workflows.

rss · Hugging Face Blog · Jul 15, 17:29

**Background**: AI agents are software systems that use large language models to autonomously perform tasks by calling tools and reasoning. Building production-grade agents involves challenges like reliability, safety, and integration with live data sources. Shippy is a free AI agent for maritime analysts, launched by the Allen Institute for AI.

<details><summary>References</summary>
<ul>
<li><a href="https://allenai.org/blog/shippy-deep-dive">What building Shippy taught us about building agents | Ai2</a></li>
<li><a href="https://www.geekwire.com/2026/ai2s-skylight-project-launches-shippy-an-ai-agent-that-dives-into-ocean-data/">Ai2’s Skylight project launches ‘Shippy,’ an AI agent that ...</a></li>
<li><a href="https://skylight.global/news/shippy-launch">Meet Shippy: Agent Built for Ocean Intelligence</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#practical insights`, `#Hugging Face`, `#software engineering`, `#machine learning`

---

<a id="item-20"></a>
## [AI coding tools make software disposable](https://seths.blog/2026/07/disposable-software/) ⭐️ 7.0/10

Seth Godin argues that AI coding assistants like Claude Code are transforming software from long-lived durable assets into quickly built and discarded artifacts, a shift he calls 'disposable software'. This shift could fundamentally change software engineering practices, project economics, and the role of developers, as the cost of creating software drops and the emphasis moves from maintenance to rapid iteration. Godin's post specifically mentions Claude Code, Anthropic's agentic coding tool, as a key enabler of this trend, but the argument applies broadly to AI-assisted development tools that can generate, modify, and deploy code with minimal human effort.

rss · Seth Godin · Jul 15, 09:03

**Background**: Traditionally, software was considered a durable asset because it required significant time and expertise to build and maintain. AI coding assistants like Claude Code, which can understand codebases, edit files, and run commands, dramatically reduce the effort needed to create and modify software, making it feasible to build and discard applications quickly.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#software engineering`, `#software lifecycle`, `#Claude Code`

---

<a id="item-21"></a>
## [RK3576 NPU support added to open-source Rocket driver](https://news.google.com/rss/articles/CBMizwFBVV95cUxOUVNsUHIxeXZLV1dZU0k0dG0xMzJlQU5PNGJpMVBQZmJ2dXVTam4tbUpiWlJzS0ZZMXpHUGI1SGwwM0pvcWVpS1RlTXFNWkNmdXBzdE9fRy1XSFBYdS1mS20zLUxEMkJzazVGbUZmakJ0Uk91N3NfQlN3RG1NQzhLeURtd1l4cTJpRmlwR1BKam9mR1JYd3dYOEJUU0RRWi1paDRBVjVMY195cGhjY29KR1ZuZm1NMVJRMkZlc0VmUlloNmRzZHR0MmdwZDNTYmfSAdcBQVVfeXFMTU1DZWM5MGg5LWNweW05YmE4NDhLaGFJR2dIMFl5QmNwSFlKc1FxYy1mZk5jRnNMVG8tYVpzTnROc0JnOTNQYVlOMFNQM21LdUlubHFWaFFJVHBEWVg4S05lRHBTb1l6Y1RpalFZWGRKOGx0amllc0ZCTGpvYm90RVBaU3FYN2N5SDR4bldmdEZmTmhOMnZ4QnpJN2xXeTg2dXVmT01DSTgwTWlJY01Ic1VDM0NYOEJBR3FXeUc2VWRuVXNsQ3gySl9JeldjdUJMdHZKVU1kQ1k?oc=5) ⭐️ 7.0/10

Reverse-engineering efforts have enabled Neural Processing Unit (NPU) support for the Rockchip RK3576 system-on-chip in the open-source Rocket driver for mainline Linux. This brings open-source NPU acceleration to the RK3576, enabling efficient AI inference on edge devices running mainline Linux without proprietary drivers. The RK3576 NPU delivers up to 6 TOPS of AI performance, and the Rocket driver now supports it through reverse-engineered code, allowing use of frameworks like TensorFlow and PyTorch.

google_news · CNX Software · Jul 15, 05:01

**Background**: The Rocket driver is an open-source Linux kernel driver for Rockchip NPUs, originally developed for older chips like RK3399Pro and RK3588. The RK3576 is a newer SoC with a 6 TOPS NPU, but lacked mainline Linux support until this reverse-engineering effort. Reverse-engineering was necessary because Rockchip did not provide open documentation for the NPU.

<details><summary>References</summary>
<ul>
<li><a href="https://wiki.t-firefly.com/en/Core-3576JD4/usage_npu.html">2. NPU — Firefly Wiki</a></li>

</ul>
</details>

**Tags**: `#Linux`, `#NPU`, `#reverse-engineering`, `#open-source`, `#RK3576`

---