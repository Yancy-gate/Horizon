---
layout: default
title: "Horizon Summary: 2026-07-12 (EN)"
date: 2026-07-12
lang: en
---

> From 105 items, 17 important content pieces were selected

---

1. [Grok Build CLI Uploads Entire Repo and Git History](#item-1) ⭐️ 9.0/10
2. [Chromium 148 Math.tanh Enables OS Fingerprinting](#item-2) ⭐️ 8.0/10
3. [Claude Code Uses 4.7x More Tokens Than OpenCode](#item-3) ⭐️ 8.0/10
4. [Trump Administration Threatens Decentralized Science Funding](#item-4) ⭐️ 8.0/10
5. [Apple Sues OpenAI: Major Legal Clash](#item-5) ⭐️ 8.0/10
6. [Ghostcommit Attack Hides Prompts in Images to Hijack AI Code Review](#item-6) ⭐️ 8.0/10
7. [Mistral Ships Robotics Model as Valuation Nears $23B](#item-7) ⭐️ 8.0/10
8. [Unpatched XRING Vulnerability in XQUIC Crashes HTTP/3 Servers](#item-8) ⭐️ 8.0/10
9. [NVIDIA Tile-Based GPU Programming Guide: cuTile, Triton, Flash Attention](#item-9) ⭐️ 8.0/10
10. [Anthropic Extends Fable 5 Access Amid Compute Constraints](#item-10) ⭐️ 7.0/10
11. [LVMH's Secret Hermès Stake Revealed in $15B Lawsuit](#item-11) ⭐️ 7.0/10
12. [Embodied Data Industry: 97 Players, 44.7B Yuan Funding, 10 Key Trends](#item-12) ⭐️ 7.0/10
13. [AI Boom Drives 300% Surge in Gas Turbine Prices](#item-13) ⭐️ 7.0/10
14. [Rice and NASA Launch Open-Source Space Robotics Simulator](#item-14) ⭐️ 7.0/10
15. [NVIDIA Guide on Evaluating Robot Policies](#item-15) ⭐️ 7.0/10
16. [Tencent-Backed DPU Startup Cloudbloom Files for IPO](#item-16) ⭐️ 6.0/10
17. [Anthropic Clarifies Claude Code 'Dumbness' Is About Effort, Not Model](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Grok Build CLI Uploads Entire Repo and Git History](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 9.0/10

A wire-level analysis reveals that xAI's Grok Build CLI uploads the entire repository content and git history to xAI servers, regardless of what the agent actually reads during a session. This raises serious privacy and security concerns for developers using Grok Build, as proprietary code and sensitive project history are transmitted without explicit user control or granular permission settings. The analysis shows that the upload includes every tracked file's content plus the full git history, independent of the agent's read operations. This behavior is not clearly disclosed to users.

hackernews · jhoho · Jul 12, 01:09 · [Discussion](https://news.ycombinator.com/item?id=48877371)

**Background**: Grok Build is xAI's terminal-native AI coding agent, launched in beta in May 2026. A wire-level analysis examines data exchanged at the application protocol level, revealing what information is sent over the network. This analysis uncovered the unexpected data upload behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build Beta | SpaceXAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wire_protocol">Wire protocol - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments express shock and concern, with many noting this validates their decision to avoid proprietary coding agents. Some users suggest sandboxing tools like bubblewrap to limit access, while others argue that such behavior is expected from proprietary agents and advocate for open-source alternatives like opencode.

**Tags**: `#privacy`, `#security`, `#AI agents`, `#xAI`, `#code analysis`

---

<a id="item-2"></a>
## [Chromium 148 Math.tanh Enables OS Fingerprinting](https://scrapfly.dev/posts/browser-math-os-fingerprint/) ⭐️ 8.0/10

Since Chromium 148, the Math.tanh function returns OS-specific results, allowing fingerprinting to link a browser to its underlying operating system. This introduces a new browser fingerprinting vector that can bypass traditional spoofing methods, raising significant privacy concerns for users and challenges for anti-fingerprinting tools. The fingerprinting works by calling Math.tanh with specific inputs that produce different floating-point results across operating systems due to variations in the underlying math library implementations.

hackernews · joahnn_s · Jul 12, 21:12 · [Discussion](https://news.ycombinator.com/item?id=48884853)

**Background**: Browser fingerprinting collects device information to identify users without cookies. Math.tanh is a JavaScript function that computes the hyperbolic tangent, and its implementation depends on the OS's math library, which can vary in precision and rounding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Browser_fingerprinting">Browser fingerprinting</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/tanh">Math.tanh() - JavaScript - MDN Web Docs</a></li>
<li><a href="https://fingerprint.com/blog/browser-fingerprinting-techniques/">Browser Fingerprinting Techniques: 6 Top Methods Explained</a></li>

</ul>
</details>

**Discussion**: Commenters debated the implications: some noted that this fingerprinting is limited to browser version range, while others criticized the article's AI-generated nature and the motives of the scraping company behind it. Technical discussion included the potential for correctly rounded functions to reduce such fingerprints.

**Tags**: `#browser fingerprinting`, `#privacy`, `#Chromium`, `#JavaScript`, `#security`

---

<a id="item-3"></a>
## [Claude Code Uses 4.7x More Tokens Than OpenCode](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 8.0/10

A study measured that Claude Code sends approximately 33,000 tokens per request before reading the user's prompt, while OpenCode sends only about 7,000 tokens, a 4.7x difference. The overhead is attributed to inefficient caching, 27 tool schemas, and injected scaffolding. This token inefficiency directly increases costs for users and raises concerns about design choices in popular AI coding tools. It also sparks debate about whether Anthropic benefits financially from higher token usage, potentially affecting developer trust and tool adoption. The study logged all requests between the coding tools and Anthropic's API endpoint, capturing usage blocks. One caveat mentioned is that the comparison may not account for qualitative differences in task completion, and the author plans to add deeper task analysis and qualitative results.

hackernews · systima · Jul 12, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48883275)

**Background**: AI coding agents like Claude Code and OpenCode use large language models to assist with software development. Each request to the model includes a system prompt, tool definitions, and conversation history, collectively called the 'harness' or 'overhead'. Higher overhead means more tokens consumed per interaction, directly impacting API costs.

<details><summary>References</summary>
<ul>
<li><a href="https://systima.ai/blog/claude-code-vs-opencode-token-overhead">Claude Code Sends 4.7x More Tokens Than... | Systima Blog</a></li>
<li><a href="https://daily.dev/posts/claude-code-sends-4-7x-more-tokens-than-opencode-before-reading-your-prompt-9m02iom1z">Claude Code Sends 4.7x More Tokens Than OpenCode Before...</a></li>
<li><a href="https://portkey.ai/blog/the-harness-tax/">The Harness Tax: The Dead Weight Inside Your Coding Agent</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that sub-agents in Claude Code burn tokens rapidly, with one user reporting 7 sub-agents launched for a single task. Others suspect Anthropic has a financial incentive to keep token usage high, and some users have switched to more transparent alternatives like Codex. The author of the study acknowledged a valid counterargument about measuring the right metric and committed to follow-up analysis.

**Tags**: `#AI coding tools`, `#token efficiency`, `#Claude Code`, `#OpenCode`, `#cost analysis`

---

<a id="item-4"></a>
## [Trump Administration Threatens Decentralized Science Funding](https://marginalrevolution.com/marginalrevolution/2026/07/the-trump-administrations-threat-to-scientific-research.html?utm_source=rss&utm_medium=rss&utm_campaign=the-trump-administrations-threat-to-scientific-research) ⭐️ 8.0/10

The Trump administration has proposed rewriting the Regulation for Federal Financial Assistance, which critics warn would centralize control over scientific research funding and undermine the historically successful decentralized system. This change could concentrate funding decisions in Washington, reducing the role of peer review and local expertise, potentially stifling innovation and damaging U.S. scientific leadership. The proposed rule, published in the Federal Register on May 29, 2026, by the Office of Management and Budget, aims to revise guidance for grants and cooperative agreements, but critics argue it would nationalize science funding.

rss · Marginal Revolution · Jul 12, 11:18

**Background**: The U.S. scientific research funding system is largely decentralized, with agencies like the National Science Foundation and National Institutes of Health distributing grants through peer review. This system has been credited with fostering innovation and maintaining U.S. leadership in science. The proposed regulation would centralize authority, potentially altering how research is prioritized and funded.

<details><summary>References</summary>
<ul>
<li><a href="https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance">Regulation for Federal Financial Assistance</a></li>
<li><a href="https://www.transportation.gov/regulations/federal-register-documents/2026-10817">Regulation for Federal Financial Assistance | US Department ...</a></li>
<li><a href="https://www.regulations.gov/docket/OMB-2026-0034/document">Regulation for Federal Financial Assistance</a></li>

</ul>
</details>

**Tags**: `#science policy`, `#research funding`, `#Trump administration`, `#regulation`

---

<a id="item-5"></a>
## [Apple Sues OpenAI: Major Legal Clash](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5JTS00Qi1UclZXNlMxTVdPYnE1cERrc08tSXhMNm16WWNaUEl2VXhfNVRZYVFnVUFjdG1lQ1VOVERSbkc0a2NuWko5VEFVQjViaS1LVnozbmZ4UzVsc01wOEMycVQ?oc=5) ⭐️ 8.0/10

Apple has reportedly filed a lawsuit against OpenAI, marking a significant legal confrontation between the two tech giants. This lawsuit could reshape the AI industry by affecting partnerships and setting legal precedents for AI development and data usage. The exact claims and details of the lawsuit are not yet public, but it likely involves intellectual property or contractual disputes related to AI technology.

google_news · The Neuron · Jul 12, 17:34

**Background**: Apple and OpenAI have had a complex relationship, with Apple integrating ChatGPT into its devices while also developing its own AI models. Lawsuits between major tech companies over AI are becoming more common as the technology advances.

**Tags**: `#Apple`, `#OpenAI`, `#lawsuit`, `#AI`, `#legal`

---

<a id="item-6"></a>
## [Ghostcommit Attack Hides Prompts in Images to Hijack AI Code Review](https://news.google.com/rss/articles/CBMixAFBVV95cUxPd05JLUhMTGlaZUFWdEJkTVZmZldRN1MzV1hheWhIc1dxRVBtUzBBQ2k3Mk1LZnFsTEIyLTJGamRHZ2I3NmFKYThZdllBZUdQNFIyeml3VGMwaG81MW1rd2dfV0ZJcjB1SVdPUVB6Ujd1TFJsQUJ2SGUyMXotbW44WURpV3lCSmxaM0sxTnlfRENiY2NXaTZjNEJORk5PaDN0cFNDQU9EOEdJWnk4WWw2b0FOMHRQYl9IdzZqVHpYUmhLTlBz?oc=5) ⭐️ 8.0/10

Researchers have disclosed Ghostcommit, a multimodal prompt injection attack that embeds malicious instructions inside PNG images to bypass AI code review tools and steal secrets like API keys from .env files. This attack exposes a critical supply chain risk because AI code review tools are increasingly used in software development, and multimodal injection can evade text-only defenses, potentially compromising thousands of projects. The attack works by hiding readable text inside a PNG image that instructs the AI agent to read .env files and encode the contents as integer arrays, exfiltrating secrets without triggering text-based filters.

google_news · Rescana · Jul 12, 11:12

**Background**: Prompt injection attacks exploit the way large language models (LLMs) process input, tricking them into executing unintended actions. Multimodal prompt injection extends this to images, audio, or video, which text-only filters cannot inspect. AI code review tools that accept image inputs (e.g., screenshots of code) are vulnerable to such attacks, creating a new vector for supply chain compromise.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/ghostcommit-attack-hides-prompts/">New Ghostcommit Attack Hides Malicious Prompts in Images to...</a></li>
<li><a href="https://www.probablypwned.com/article/ghostcommit-ai-prompt-injection-png-images-secret-theft">Ghostcommit Attack Hides Prompts in Images to... | ProbablyPwned</a></li>
<li><a href="https://christian-schneider.net/blog/multimodal-prompt-injection/">Multimodal prompt injection : attacks in images, audio, and video</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#prompt injection`, `#supply chain risk`, `#code review`, `#cybersecurity`

---

<a id="item-7"></a>
## [Mistral Ships Robotics Model as Valuation Nears $23B](https://news.google.com/rss/articles/CBMidEFVX3lxTFBRckZGeV9ka0M4TVZoTzBZRC0tcUtfcjlFWkN3UmRvZnZIcGpiNGVsOXRyX2x3ZGR1Nno4T2I4dDBrbE1uN0JXd2tJLTFIVHJVQ2dVT1dZdHZSNm1RbjFCTGpkdGdyQ3FpZmw4WlpLN2RVaUJq?oc=5) ⭐️ 8.0/10

Mistral AI has released a new robotics navigation model called Robostral Navigate, which uses a single RGB camera and does not require LiDAR or depth sensors. The announcement comes as the French startup's valuation approaches $23 billion. This marks Mistral's expansion into physical AI, a rapidly growing field, and signals the company's ambition to compete with other AI leaders in robotics. The high valuation reflects investor confidence in Mistral's potential to dominate both software and hardware AI applications. Robostral Navigate is designed for robotic navigation and relies solely on a single RGB camera, eliminating the need for expensive sensors like LiDAR. Mistral has also signed deals with major European industrial customers, indicating commercial traction.

google_news · tech-insider.org · Jul 12, 01:11

**Background**: Mistral AI is a French startup known for its open-weight large language models. The company has raised over $6.5 billion and achieved a $20 billion valuation earlier in 2026. Physical AI refers to AI systems that interact with the physical world, such as robots and autonomous vehicles.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-07-08/mistral-ai-releases-robotics-model-to-support-physical-ai-push">Mistral AI Releases Robotics Model to Support Physical AI Push - Bloomberg</a></li>
<li><a href="https://oodaloop.com/briefs/technology/mistral-ai-introduces-robot-navigation-model/">Mistral AI Introduces Robot Navigation Model — OODAloop</a></li>

</ul>
</details>

**Tags**: `#AI`, `#robotics`, `#Mistral`, `#valuation`, `#machine learning`

---

<a id="item-8"></a>
## [Unpatched XRING Vulnerability in XQUIC Crashes HTTP/3 Servers](https://news.google.com/rss/articles/CBMisAFBVV95cUxNcjY0dXBUSUE4eTZDanFJbm9ESkMzb1dRbW1NOUhmd1ByclF0OFd4allFcFNMdUdCVmpGSFd4U0t4cDRIeGllMEk3UGxQVlgyOE9SN055c0t0TWZfc2x4WmYydGk1UjJDUWhySVMyd21VTmdLM2hBYzdXdDRoQ2x3QzkwVklpcFZXVF9LdkdPRnhZTUt2Tk45Y0t6aExZSTBOdFdadEo1Xzh3dWtqVnA4dA?oc=5) ⭐️ 8.0/10

FoxIO disclosed XRING, an unpatched memory corruption vulnerability in Alibaba's XQUIC library that allows unauthenticated remote clients to crash HTTP/3 servers by sending only 260 bytes of legal QPACK traffic. This vulnerability poses a significant denial-of-service risk to any organization using XQUIC-based HTTP/3 infrastructure, as it is trivial to exploit and no vendor-supplied fix or CVE exists yet. The XRING vulnerability is a memory corruption flaw in the QPACK dynamic table implementation within XQUIC, where the table is managed as a ring buffer. Affected servers include those using XQUIC versions prior to any fix, and the flaw has been confirmed but not yet patched.

google_news · Rescana · Jul 12, 11:12

**Background**: XQUIC is an open-source library released by Alibaba that implements the QUIC and HTTP/3 protocols as specified by the IETF. QPACK is the header compression mechanism for HTTP/3, which uses a dynamic table shared between client and server. The XRING vulnerability exploits a flaw in how XQUIC manages this dynamic table as a ring buffer, leading to memory corruption when specially crafted QPACK frames are processed.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html">Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP ...</a></li>
<li><a href="https://www.rescana.com/post/unpatched-xring-vulnerability-in-xquic-exposes-http-3-servers-to-remote-crash-risk">Unpatched XRING Vulnerability in XQUIC Exposes HTTP/3 Servers ...</a></li>
<li><a href="https://github.com/alibaba/xquic">GitHub - alibaba/xquic: XQUIC Library released by Alibaba is ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability`, `#HTTP/3`, `#XQUIC`, `#networking`

---

<a id="item-9"></a>
## [NVIDIA Tile-Based GPU Programming Guide: cuTile, Triton, Flash Attention](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNLVk4TlRvM3g2eEpVVzg5YnZTWEhFLXhEamlSM1pfVnlZVkwxRlNSb0VoYmdhSlo3SVZpSG1VT3h1UjMweWVacHdIM2psWWQ3MGF0ZUNzVlhVclZzWExEblp3YlFTUkdUWVNJcHFKTlpmbDB6aHEyTTI0QWJmN2RkLXlYQVVKclRJdnh2ZlVFOVB5VjNwRnZ2VlBWbHdFcXJfWGFRQWI3QUg3YnRheDhURkx2Y3Rhc2U5SkprYjBQNE9vVVY1ZGQ1YUdjVmhGRUJwQnU4SVQ0a2VscWs?oc=5) ⭐️ 8.0/10

MarkTechPost published a practical coding guide covering NVIDIA's tile-based GPU programming techniques, including cuTile Python, Triton kernels, and Flash Attention. This guide helps AI/ML developers and systems programmers leverage tile-based programming to maximize GPU utilization, especially for attention mechanisms in transformers, which are critical for large language models. cuTile Python enables writing tile kernels in Python with automatic tensor core access; Triton is a Python-based language for custom DNN kernels; Flash Attention is a fast and memory-efficient attention algorithm.

google_news · MarkTechPost · Jul 12, 00:01

**Background**: Tile-based GPU programming divides data into small blocks (tiles) that can be processed in parallel on GPU cores, improving memory locality and performance. NVIDIA's CUDA Tile programming model, introduced in CUDA 13.1, simplifies this approach. Triton is an open-source language and compiler for parallel programming, widely used for writing efficient deep learning kernels. Flash Attention is a recent algorithm that reduces memory reads/writes in attention computation, significantly speeding up transformer models.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NVIDIA/cutile-python">GitHub - NVIDIA/cutile-python: cuTile is a programming model for writing parallel kernels for NVIDIA GPUs · GitHub</a></li>
<li><a href="https://developer.nvidia.com/blog/simplify-gpu-programming-with-nvidia-cuda-tile-in-python/">Simplify GPU Programming with NVIDIA CUDA Tile in Python | NVIDIA Technical Blog</a></li>
<li><a href="https://github.com/triton-lang/triton">GitHub - triton-lang/triton: Development repository for the ...</a></li>

</ul>
</details>

**Tags**: `#GPU Programming`, `#NVIDIA`, `#Triton`, `#Flash Attention`, `#AI/ML`

---

<a id="item-10"></a>
## [Anthropic Extends Fable 5 Access Amid Compute Constraints](https://simonwillison.net/2026/Jul/12/bump/#atom-everything) ⭐️ 7.0/10

Anthropic has extended access to its Fable 5 model on all paid plans through July 19, 2026, due to compute constraints, while OpenAI has temporarily removed usage limits for GPT-5.6 Sol on Plus, Business, and Pro plans. This highlights the ongoing compute challenges faced by AI labs and the strategic decisions they make to balance demand and availability, potentially influencing user adoption and competitive dynamics between Anthropic and OpenAI. Users on paid plans can use up to half of their weekly usage limit on Fable 5, after which they can continue with usage credits or switch models. OpenAI's GPT-5.6 Sol is also being made more efficient to reduce usage consumption.

rss · Simon Willison · Jul 12, 21:20

**Background**: Fable 5 is a Mythos-class model from Anthropic, representing its most capable widely released AI model, designed for demanding coding and reasoning tasks. GPT-5.6 Sol is OpenAI's flagship model in the GPT-5.6 family, also focused on advanced capabilities. Both models were released in June 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#Fable`, `#GPT-5.6`, `#compute constraints`

---

<a id="item-11"></a>
## [LVMH's Secret Hermès Stake Revealed in $15B Lawsuit](https://36kr.com/p/3892321158773251?f=rss) ⭐️ 7.0/10

LVMH has submitted a 20-page court filing in Paris, detailing its secret accumulation of Hermès shares over two decades, in response to a $15 billion lawsuit filed by Hermès heir Nicolas Puech. This case exposes the aggressive tactics used by luxury conglomerates to acquire rivals and raises questions about corporate governance and fiduciary duty, with potential implications for the entire luxury industry. LVMH used equity swaps and derivatives to secretly build a 22.6% stake in Hermès by 2012, avoiding disclosure thresholds; Puech claims his financial advisor sold 6 million shares worth $15 billion without his knowledge, allegedly to LVMH.

rss · 36氪 · Jul 12, 07:16

**Background**: Hermès is a French luxury goods manufacturer known for its Birkin bags and silk scarves, controlled by the founding family. LVMH is the world's largest luxury conglomerate, led by Bernard Arnault. In 2010, LVMH revealed a 17.1% stake in Hermès, sparking a legal battle that ended in 2014 with LVMH agreeing to divest its shares. The current lawsuit, filed in 2025, alleges that LVMH acquired shares from Puech's portfolio through his advisor without authorization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/sustainability/boards-policy-regulation/lvmh-reaffirms-it-has-never-misappropriated-hermes-heirs-shares-2025-12-03/">LVMH has never misappropriated Hermes heir's shares, company says | Reuters</a></li>
<li><a href="https://www.thefashionlaw.com/hermes-vs-lvmh-a-timeline-of-the-drama/">Hermès vs. LVMH: The Timeline Behind a Takeover Attempt - The Fashion Law</a></li>
<li><a href="https://www.forbes.com/sites/zacharyfolk/2025/12/03/herms-heir-reportedly-sues-bernard-arnault-and-lvmh-alleging-16-billion-worth-of-herms-shares-sold-without-his-knowledge/">Hermès Heir Reportedly Sues Bernard Arnault And LVMH ...</a></li>

</ul>
</details>

**Tags**: `#LVMH`, `#Hermès`, `#corporate governance`, `#luxury brands`, `#legal dispute`

---

<a id="item-12"></a>
## [Embodied Data Industry: 97 Players, 44.7B Yuan Funding, 10 Key Trends](https://36kr.com/p/3892027841362694?f=rss) ⭐️ 7.0/10

A comprehensive report by 36Kr reveals that 97 companies are now active in China's embodied data industry, with 15 independent data service providers raising a total of 44.7 billion yuan in the past year. The report identifies ten key trends, including four main data collection routes and the dominance of independent data service providers. Embodied data is a critical bottleneck for training robots, and this analysis provides a structured overview of the emerging ecosystem, helping investors and practitioners understand the competitive landscape. The findings highlight that data collection has become an independent industry, separate from robot manufacturing, signaling a maturing supply chain. Among the 97 players, 70 focus on data collection and 27 on data infrastructure. The four main collection routes are real-robot teleoperation, no-robot collection, simulation synthesis, and internet video distillation, with 43% of companies pursuing multiple routes. Independent data service providers form the largest group (40%), and 67% of all players are 'embodied-native' startups.

rss · 36氪 · Jul 12, 02:16

**Background**: Embodied AI refers to AI systems that interact with the physical world through robots. Training such systems requires massive amounts of data capturing human actions and robot interactions, which is currently scarce and expensive to collect. The industry has emerged to address this data bottleneck, with various technical approaches competing to provide cost-effective training data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.huxiu.com/article/4870304.html">具身数据采集产业链调查：被机器人采集的人-虎嗅网</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2026634205371668064">2026.3具身智能数据采集：路线、方法与规模化思考</a></li>
<li><a href="https://news.marsbit.co/20260712102912558212.html">news.marsbit.co/20260712102912558212.html</a></li>

</ul>
</details>

**Tags**: `#embodied AI`, `#robotics`, `#data collection`, `#industry analysis`, `#funding`

---

<a id="item-13"></a>
## [AI Boom Drives 300% Surge in Gas Turbine Prices](https://36kr.com/newsflashes/3892556678543880?f=rss) ⭐️ 7.0/10

Gas turbine prices have surged approximately 300% over the past three years due to soaring demand from AI data centers, with Microsoft recently purchasing seven large gas turbines from GE Vernova for its Texas data center. This price surge highlights the growing energy bottleneck for AI infrastructure, as data centers require massive and reliable power, benefiting gas turbine manufacturers like GE Vernova, Caterpillar, and Siemens. Each gas turbine costs over $250 million, and GE Vernova's stock has risen more than 70% in the past six months. Melius Research estimates the cumulative price increase at 300% over three years.

rss · 36氪 · Jul 12, 11:37

**Background**: Gas turbines are heavy-duty power generation equipment that burn natural gas to produce electricity, commonly used for large-scale, reliable power supply. AI data centers require enormous and consistent electricity, driving demand for such turbines. GE Vernova is a leading manufacturer of gas turbines, with models ranging from 34 MW to 571 MW.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gevernova.com/gas-power/products/gas-turbines">Aeroderivative and Heavy-Duty Gas Turbines | GE Vernova</a></li>
<li><a href="https://www.binance.com/en/square/post/07-12-2026-microsoft-bought-seven-ge-vernova-gas-turbines-to-power-texas-data-center-343923870976737">Microsoft Bought Seven GE Vernova Gas Turbines to Power Texas...</a></li>
<li><a href="https://pulseaugur.com/cluster/138340-ai-boom-drives-300-surge-in-gas-turbine-prices">AI boom drives 300% surge in gas turbine prices · PulseAugur</a></li>

</ul>
</details>

**Tags**: `#AI`, `#data centers`, `#energy`, `#gas turbines`, `#hardware`

---

<a id="item-14"></a>
## [Rice and NASA Launch Open-Source Space Robotics Simulator](https://news.google.com/rss/articles/CBMipAFBVV95cUxOMWprbUgzWmpGLWw3SHQtMjQwbk5LbExYaFozRXRxc2JkeF9VOFlZd1pUblhfSFhpVUFod0JMVE0tRm43X3hrQXlJMFdfczFzNmYwZ3gybGpqWUpjWlRyZlk2N01JMUtZR004bU9feENBeU5hcHFjOUhETDg2elVSVnZleVAyblV0amJKQmNES2RYVXZGei1teWRNQTBTemVmenFacg?oc=5) ⭐️ 7.0/10

Rice University and NASA have released iMETRO, the world's first open-source dynamic simulation environment for developing robots used in space vehicles and indoor space habitats. This open-source simulator democratizes access to advanced space robotics research, enabling engineers and researchers worldwide to test and develop robots for space missions without expensive proprietary software. iMETRO supports remote operation and is designed to simulate robots working inside spacecraft and space habitats, with a focus on dynamic interactions and real-time control.

google_news · AI Insider · Jul 12, 06:21

**Background**: Space robotics often requires high-fidelity simulation to test autonomous systems before deployment. Previously, such simulators were proprietary or limited in scope. iMETRO aims to fill this gap by providing a free, open-source platform that can be customized for various space robotics applications.

<details><summary>References</summary>
<ul>
<li><a href="https://news.rice.edu/news/2026/rice-and-nasa-launch-worlds-first-open-source-remote-space-robotics-simulator">Rice and NASA launch world’s first open-source remote space ...</a></li>
<li><a href="https://sciencesensei.com/rice-and-nasa-launch-world-s-first-open-source-remote-space-robotics-simulator/">Rice and NASA Release the First Open-Source Remote Space ...</a></li>
<li><a href="https://theaiinsider.tech/2026/07/12/rice-and-nasa-launch-open-source-remote-space-robotics-simulator/">Rice and NASA Launch Open-source Remote Space Robotics Simulator</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#space`, `#open-source`, `#simulation`, `#NASA`

---

<a id="item-15"></a>
## [NVIDIA Guide on Evaluating Robot Policies](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOVU50bTFobzVya1p4ZUd5b1JMMzl6VFpsZDZrQ2pFMm9yOEF2VzRVeTBVeFFVcVIyc1oyYXhOUVB3aFhiYlRxR3YyVHFKOHgwWEpxelAyODlkT0RIX1k2MS1CX2FUamJIUEFSVHhuVzh6Q1otNFRsX1ctNkptVXl0SzVpcFRVZUJDUlpXSzdDS2RRcHF0djk2aTJLd0JmVjlwNmZiaWlybHdWU28?oc=5) ⭐️ 7.0/10

NVIDIA Developer published a blog post detailing how to evaluate general-purpose robot policies for real-world deployment, emphasizing that success rate alone is insufficient. As general-purpose robot policies become more common, proper evaluation metrics are critical for safe and effective deployment in real-world environments. This guidance helps researchers and practitioners avoid misleading conclusions from simplistic metrics. The blog argues that success rate tells almost nothing about how a robot performed a task, only whether it crossed the finish line. It likely proposes alternative metrics such as robustness, efficiency, and safety for comprehensive evaluation.

google_news · NVIDIA Developer · Jul 12, 01:21

**Background**: General-purpose robot policies are AI models trained on diverse data to control various robots across different tasks and environments. Evaluating these policies for real-world deployment is challenging because traditional metrics like success rate do not capture nuanced performance aspects such as recovery from failures or energy efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/">How to Evaluate General-Purpose Robot Policies for Real-World...</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#AI`, `#deployment`, `#NVIDIA`, `#policy evaluation`

---

<a id="item-16"></a>
## [Tencent-Backed DPU Startup Cloudbloom Files for IPO](https://36kr.com/p/3892352153942530?f=rss) ⭐️ 6.0/10

Cloudbloom Intelligence, a Shenzhen-based DPU startup backed by Tencent, has filed for an IPO on the ChiNext board of the Shenzhen Stock Exchange, aiming to become China's first publicly traded DPU company. This IPO filing highlights the growing importance of DPUs in AI and cloud infrastructure, and could pave the way for more Chinese semiconductor startups to go public, especially under ChiNext's new listing rules that accommodate unprofitable tech firms. Cloudbloom's self-developed DPU SoC chip achieves 400Gbps network bandwidth, with 4x performance improvement and over 50% power reduction compared to traditional solutions. The company is still unprofitable, with net losses of 6.67 billion yuan in 2023, 6 billion yuan in 2024, and 11.9 billion yuan in 2025.

rss · 36氪 · Jul 12, 07:59

**Background**: A DPU (Data Processing Unit) is a specialized processor designed to handle data movement and processing in data centers, offloading tasks from CPUs and GPUs. NVIDIA CEO Jensen Huang has described DPU as one of the three pillars of future computing, alongside CPU and GPU. Cloudbloom was founded in 2020 by Dr. Xiao Qiyang, a Stanford PhD, and has raised multiple rounds from investors including Tencent, which holds a 19.78% stake as the largest shareholder.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/660108879">什么是DPU？一文带你搞懂！ - 知乎</a></li>
<li><a href="https://www.jaguarmicro.com/">云 豹 智 能 【 云 豹 智 能 】专注于 云 计算和数据处理器 DPU 芯片与解决方案</a></li>
<li><a href="https://global.chinadaily.com.cn/a/202604/11/WS69d9b077a310d6866eb42d4e.html">China unveils ChiNext reforms to bolster innovation, broaden ...</a></li>

</ul>
</details>

**Tags**: `#DPU`, `#IPO`, `#semiconductor`, `#Tencent`, `#startup`

---

<a id="item-17"></a>
## [Anthropic Clarifies Claude Code 'Dumbness' Is About Effort, Not Model](https://36kr.com/p/3892222176574211?f=rss) ⭐️ 6.0/10

Anthropic published a blog post explaining that many users mistakenly blame Claude Code's poor performance on the model size, when the real culprit is often the 'Effort' setting. In March, Anthropic quietly lowered the default Effort from high to medium to reduce latency, causing widespread complaints about degraded quality. This clarification helps developers optimize their use of Claude Code by understanding that a smaller model with high Effort can outperform a larger model with low Effort, potentially saving costs and improving results. It also highlights the importance of configuration settings in AI coding tools, which are often overlooked. Effort controls how many tokens Claude spends on reasoning, tool calls, and verification, not just thinking time. A high Effort prompt can generate up to 7 times more tokens than a low Effort one, with the extra tokens used for reading files, running tests, and multi-step task completion.

rss · 36氪 · Jul 12, 05:47

**Background**: Claude Code offers two main settings: Model (e.g., Sonnet, Opus, Fable) which determines the underlying frozen weights and knowledge, and Effort (low, medium, high, max) which controls how thoroughly the model works on a task. Many users assumed that upgrading the model alone would improve performance, but the Effort setting has a significant impact on output quality and behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/blog/claude-model-and-effort-level-in-claude-code">Choosing a Claude model and effort level in Claude Code ...</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/effort">Effort - Claude Platform Docs</a></li>
<li><a href="https://www.mindstudio.ai/blog/claude-code-effort-levels-explained">Claude Code Effort Levels Explained: When to Use Low, Medium ...</a></li>

</ul>
</details>

**Tags**: `#Claude`, `#AI`, `#Anthropic`, `#coding tools`, `#misconceptions`

---