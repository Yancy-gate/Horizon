---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 105 条内容中筛选出 17 条重要资讯。

---

1. [Grok Build CLI 上传整个仓库和 Git 历史](#item-1) ⭐️ 9.0/10
2. [Chromium 148 的 Math.tanh 可识别操作系统](#item-2) ⭐️ 8.0/10
3. [Claude Code 的 Token 消耗是 OpenCode 的 4.7 倍](#item-3) ⭐️ 8.0/10
4. [特朗普政府威胁分散式科学资助体系](#item-4) ⭐️ 8.0/10
5. [苹果起诉 OpenAI：重大法律冲突](#item-5) ⭐️ 8.0/10
6. [Ghostcommit 攻击将恶意指令隐藏在图片中劫持 AI 代码审查](#item-6) ⭐️ 8.0/10
7. [Mistral 发布机器人模型，估值逼近 230 亿美元](#item-7) ⭐️ 8.0/10
8. [XQUIC 未修补漏洞 XRING 可致 HTTP/3 服务器崩溃](#item-8) ⭐️ 8.0/10
9. [NVIDIA 基于块的 GPU 编程指南：cuTile、Triton 与 Flash Attention](#item-9) ⭐️ 8.0/10
10. [Anthropic 因计算限制延长 Fable 5 访问权限](#item-10) ⭐️ 7.0/10
11. [LVMH 秘密增持爱马仕股份案曝光，涉 150 亿美元诉讼](#item-11) ⭐️ 7.0/10
12. [具身数据行业：97 家玩家，融资 447 亿，十大趋势](#item-12) ⭐️ 7.0/10
13. [AI 热潮推高燃气轮机价格 300%](#item-13) ⭐️ 7.0/10
14. [莱斯大学与 NASA 发布开源太空机器人模拟器](#item-14) ⭐️ 7.0/10
15. [NVIDIA 机器人策略评估指南](#item-15) ⭐️ 7.0/10
16. [腾讯重仓 DPU 初创公司云豹智能冲刺 IPO](#item-16) ⭐️ 6.0/10
17. [Anthropic 澄清 Claude Code 变笨是 Effort 设置问题，非模型问题](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Grok Build CLI 上传整个仓库和 Git 历史](https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547) ⭐️ 9.0/10

一项网络级分析显示，xAI 的 Grok Build CLI 会将整个仓库内容和 Git 历史上传到 xAI 服务器，无论代理在会话中实际读取了什么。 这给使用 Grok Build 的开发者带来了严重的隐私和安全问题，因为专有代码和敏感的项目历史会在没有明确用户控制或细粒度权限设置的情况下被传输。 分析显示，上传内容包括每个被跟踪文件的内容以及完整的 Git 历史，与代理的读取操作无关。这种行为并未向用户明确披露。

hackernews · jhoho · 7月12日 01:09 · [社区讨论](https://news.ycombinator.com/item?id=48877371)

**背景**: Grok Build 是 xAI 于 2026 年 5 月推出的终端原生 AI 编码代理。网络级分析检查应用协议层交换的数据，揭示通过网络发送了哪些信息。该分析发现了这种意外的数据上传行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/cli">Grok Build Beta | SpaceXAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wire_protocol">Wire protocol - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了震惊和担忧，许多人指出这验证了他们避免使用专有编码代理的决定。一些用户建议使用 bubblewrap 等沙盒工具来限制访问，而另一些人则认为这种行为在专有代理中是意料之中的，并提倡使用 opencode 等开源替代方案。

**标签**: `#privacy`, `#security`, `#AI agents`, `#xAI`, `#code analysis`

---

<a id="item-2"></a>
## [Chromium 148 的 Math.tanh 可识别操作系统](https://scrapfly.dev/posts/browser-math-os-fingerprint/) ⭐️ 8.0/10

自 Chromium 148 起，Math.tanh 函数返回因操作系统而异的结果，使得指纹识别能够将浏览器与其底层操作系统关联起来。 这引入了一种新的浏览器指纹识别途径，可以绕过传统的伪装方法，给用户隐私带来重大担忧，也给反指纹识别工具带来挑战。 该指纹识别通过使用特定输入调用 Math.tanh 实现，由于底层数学库实现的差异，不同操作系统会产生不同的浮点结果。

hackernews · joahnn_s · 7月12日 21:12 · [社区讨论](https://news.ycombinator.com/item?id=48884853)

**背景**: 浏览器指纹识别收集设备信息以在无 cookie 情况下识别用户。Math.tanh 是计算双曲正切的 JavaScript 函数，其实现依赖于操作系统的数学库，不同库在精度和舍入上存在差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Browser_fingerprinting">Browser fingerprinting</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/tanh">Math.tanh() - JavaScript - MDN Web Docs</a></li>
<li><a href="https://fingerprint.com/blog/browser-fingerprinting-techniques/">Browser Fingerprinting Techniques: 6 Top Methods Explained</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了其影响：有人指出这种指纹识别仅限于浏览器版本范围，也有人批评文章由 AI 生成以及背后抓取公司的动机。技术讨论包括正确舍入函数可能减少此类指纹的可能性。

**标签**: `#browser fingerprinting`, `#privacy`, `#Chromium`, `#JavaScript`, `#security`

---

<a id="item-3"></a>
## [Claude Code 的 Token 消耗是 OpenCode 的 4.7 倍](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 8.0/10

一项研究发现，Claude Code 在读取用户提示前每次请求发送约 33,000 个 token，而 OpenCode 仅发送约 7,000 个 token，相差 4.7 倍。开销源于低效的缓存、27 个工具模式以及注入的脚手架代码。 这种 token 低效直接增加了用户成本，并引发了对流行 AI 编码工具设计选择的质疑。同时引发了关于 Anthropic 是否从更高 token 消耗中获利的讨论，可能影响开发者信任和工具采用。 该研究记录了编码工具与 Anthropic API 端点之间的所有请求，捕获了使用情况。一个注意事项是，比较可能未考虑任务完成的定性差异，作者计划增加更深入的任务分析和定性结果。

hackernews · systima · 7月12日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48883275)

**背景**: 像 Claude Code 和 OpenCode 这样的 AI 编码代理使用大语言模型辅助软件开发。每次向模型发送的请求都包含系统提示、工具定义和对话历史，统称为“框架”或“开销”。更高的开销意味着每次交互消耗更多 token，直接影响 API 成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://systima.ai/blog/claude-code-vs-opencode-token-overhead">Claude Code Sends 4.7x More Tokens Than... | Systima Blog</a></li>
<li><a href="https://daily.dev/posts/claude-code-sends-4-7x-more-tokens-than-opencode-before-reading-your-prompt-9m02iom1z">Claude Code Sends 4.7x More Tokens Than OpenCode Before...</a></li>
<li><a href="https://portkey.ai/blog/the-harness-tax/">The Harness Tax: The Dead Weight Inside Your Coding Agent</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，Claude Code 中的子代理会快速消耗 token，有用户报告单个任务启动了 7 个子代理。其他人怀疑 Anthropic 有财务动机保持高 token 消耗，一些用户已转向更透明的替代方案如 Codex。研究作者承认了关于衡量正确指标的有效反驳，并承诺进行后续分析。

**标签**: `#AI coding tools`, `#token efficiency`, `#Claude Code`, `#OpenCode`, `#cost analysis`

---

<a id="item-4"></a>
## [特朗普政府威胁分散式科学资助体系](https://marginalrevolution.com/marginalrevolution/2026/07/the-trump-administrations-threat-to-scientific-research.html?utm_source=rss&utm_medium=rss&utm_campaign=the-trump-administrations-threat-to-scientific-research) ⭐️ 8.0/10

特朗普政府提议改写《联邦财政援助条例》，批评者警告这将集中控制科研资助，破坏历史上成功的分散式体系。 这一变化可能将资助决策集中在华盛顿，削弱同行评审和地方专家的作用，可能抑制创新并损害美国的科学领导地位。 该拟议规则由管理和预算办公室于 2026 年 5 月 29 日在《联邦公报》上发布，旨在修订拨款和合作协议的指导方针，但批评者认为这将使科学资助国有化。

rss · Marginal Revolution · 7月12日 11:18

**背景**: 美国科研资助体系高度分散，由美国国家科学基金会和美国国立卫生研究院等机构通过同行评审分配拨款。这一体系被认为促进了创新并维持了美国的科学领导地位。拟议的法规将集中权力，可能改变研究优先级的设定和资助方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.federalregister.gov/documents/2026/05/29/2026-10817/regulation-for-federal-financial-assistance">Regulation for Federal Financial Assistance</a></li>
<li><a href="https://www.transportation.gov/regulations/federal-register-documents/2026-10817">Regulation for Federal Financial Assistance | US Department ...</a></li>
<li><a href="https://www.regulations.gov/docket/OMB-2026-0034/document">Regulation for Federal Financial Assistance</a></li>

</ul>
</details>

**标签**: `#science policy`, `#research funding`, `#Trump administration`, `#regulation`

---

<a id="item-5"></a>
## [苹果起诉 OpenAI：重大法律冲突](https://news.google.com/rss/articles/CBMiZEFVX3lxTE5JTS00Qi1UclZXNlMxTVdPYnE1cERrc08tSXhMNm16WWNaUEl2VXhfNVRZYVFnVUFjdG1lQ1VOVERSbkc0a2NuWko5VEFVQjViaS1LVnozbmZ4UzVsc01wOEMycVQ?oc=5) ⭐️ 8.0/10

据报道，苹果已对 OpenAI 提起诉讼，标志着两家科技巨头之间的重大法律对抗。 这场诉讼可能通过影响合作关系和为 AI 开发及数据使用设定法律先例，从而重塑 AI 行业。 诉讼的具体指控和细节尚未公开，但可能涉及与 AI 技术相关的知识产权或合同纠纷。

google_news · The Neuron · 7月12日 17:34

**背景**: 苹果与 OpenAI 关系复杂，苹果既将 ChatGPT 集成到其设备中，也在开发自己的 AI 模型。随着 AI 技术的发展，大型科技公司之间的诉讼正变得越来越常见。

**标签**: `#Apple`, `#OpenAI`, `#lawsuit`, `#AI`, `#legal`

---

<a id="item-6"></a>
## [Ghostcommit 攻击将恶意指令隐藏在图片中劫持 AI 代码审查](https://news.google.com/rss/articles/CBMixAFBVV95cUxPd05JLUhMTGlaZUFWdEJkTVZmZldRN1MzV1hheWhIc1dxRVBtUzBBQ2k3Mk1LZnFsTEIyLTJGamRHZ2I3NmFKYThZdllBZUdQNFIyeml3VGMwaG81MW1rd2dfV0ZJcjB1SVdPUVB6Ujd1TFJsQUJ2SGUyMXotbW44WURpV3lCSmxaM0sxTnlfRENiY2NXaTZjNEJORk5PaDN0cFNDQU9EOEdJWnk4WWw2b0FOMHRQYl9IdzZqVHpYUmhLTlBz?oc=5) ⭐️ 8.0/10

研究人员披露了 Ghostcommit 攻击，这是一种多模态提示注入攻击，将恶意指令嵌入 PNG 图片中，以绕过 AI 代码审查工具，并从.env 文件中窃取 API 密钥等机密。 该攻击暴露了严重的供应链风险，因为 AI 代码审查工具在软件开发中日益普及，而多模态注入可以绕过纯文本防御，可能危及数千个项目。 该攻击的工作原理是将可读文本隐藏在 PNG 图片中，指示 AI 代理读取.env 文件并将内容编码为整数数组，从而在不触发基于文本的过滤器的情况下窃取机密。

google_news · Rescana · 7月12日 11:12

**背景**: 提示注入攻击利用大型语言模型（LLM）处理输入的方式，诱骗它们执行非预期的操作。多模态提示注入将这种攻击扩展到图像、音频或视频，纯文本过滤器无法检查这些内容。接受图像输入（例如代码截图）的 AI 代码审查工具容易受到此类攻击，从而为供应链入侵创造了新途径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/ghostcommit-attack-hides-prompts/">New Ghostcommit Attack Hides Malicious Prompts in Images to...</a></li>
<li><a href="https://www.probablypwned.com/article/ghostcommit-ai-prompt-injection-png-images-secret-theft">Ghostcommit Attack Hides Prompts in Images to... | ProbablyPwned</a></li>
<li><a href="https://christian-schneider.net/blog/multimodal-prompt-injection/">Multimodal prompt injection : attacks in images, audio, and video</a></li>

</ul>
</details>

**标签**: `#AI security`, `#prompt injection`, `#supply chain risk`, `#code review`, `#cybersecurity`

---

<a id="item-7"></a>
## [Mistral 发布机器人模型，估值逼近 230 亿美元](https://news.google.com/rss/articles/CBMidEFVX3lxTFBRckZGeV9ka0M4TVZoTzBZRC0tcUtfcjlFWkN3UmRvZnZIcGpiNGVsOXRyX2x3ZGR1Nno4T2I4dDBrbE1uN0JXd2tJLTFIVHJVQ2dVT1dZdHZSNm1RbjFCTGpkdGdyQ3FpZmw4WlpLN2RVaUJq?oc=5) ⭐️ 8.0/10

Mistral AI 发布了一款名为 Robostral Navigate 的新型机器人导航模型，该模型仅使用单个 RGB 摄像头，无需激光雷达或深度传感器。这一消息发布之际，这家法国初创公司的估值正接近 230 亿美元。 这标志着 Mistral 向物理 AI 这一快速增长领域的扩张，并表明该公司在机器人领域与其他 AI 领导者竞争的雄心。高估值反映了投资者对 Mistral 在软件和硬件 AI 应用领域占据主导地位的信心。 Robostral Navigate 专为机器人导航设计，仅依赖单个 RGB 摄像头，无需激光雷达等昂贵传感器。Mistral 还与欧洲主要工业客户签署了协议，显示出商业吸引力。

google_news · tech-insider.org · 7月12日 01:11

**背景**: Mistral AI 是一家以开源权重大型语言模型闻名的法国初创公司。该公司已融资超过 65 亿美元，并在 2026 年初达到 200 亿美元估值。物理 AI 指的是与物理世界交互的 AI 系统，例如机器人和自动驾驶汽车。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-07-08/mistral-ai-releases-robotics-model-to-support-physical-ai-push">Mistral AI Releases Robotics Model to Support Physical AI Push - Bloomberg</a></li>
<li><a href="https://oodaloop.com/briefs/technology/mistral-ai-introduces-robot-navigation-model/">Mistral AI Introduces Robot Navigation Model — OODAloop</a></li>

</ul>
</details>

**标签**: `#AI`, `#robotics`, `#Mistral`, `#valuation`, `#machine learning`

---

<a id="item-8"></a>
## [XQUIC 未修补漏洞 XRING 可致 HTTP/3 服务器崩溃](https://news.google.com/rss/articles/CBMisAFBVV95cUxNcjY0dXBUSUE4eTZDanFJbm9ESkMzb1dRbW1NOUhmd1ByclF0OFd4allFcFNMdUdCVmpGSFd4U0t4cDRIeGllMEk3UGxQVlgyOE9SN055c0t0TWZfc2x4WmYydGk1UjJDUWhySVMyd21VTmdLM2hBYzdXdDRoQ2x3QzkwVklpcFZXVF9LdkdPRnhZTUt2Tk45Y0t6aExZSTBOdFdadEo1Xzh3dWtqVnA4dA?oc=5) ⭐️ 8.0/10

FoxIO 披露了 XRING 漏洞，这是阿里巴巴 XQUIC 库中一个未修补的内存损坏漏洞，未认证的远程客户端仅需发送 260 字节的合法 QPACK 流量即可使 HTTP/3 服务器崩溃。 该漏洞对任何使用基于 XQUIC 的 HTTP/3 基础设施的组织构成严重的拒绝服务风险，因为利用方式简单，且目前尚无供应商提供的补丁或 CVE 编号。 XRING 漏洞是 XQUIC 中 QPACK 动态表实现的内存损坏缺陷，该表以环形缓冲区方式管理。受影响的服务器包括使用任何未修复版本的 XQUIC 的服务器，该缺陷已被确认但尚未修补。

google_news · Rescana · 7月12日 11:12

**背景**: XQUIC 是阿里巴巴发布的开源库，实现了 IETF 规定的 QUIC 和 HTTP/3 协议。QPACK 是 HTTP/3 的头部压缩机制，使用客户端和服务器共享的动态表。XRING 漏洞利用了 XQUIC 将动态表作为环形缓冲区管理时的缺陷，在处理特制的 QPACK 帧时导致内存损坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/07/unpatched-xring-flaw-in-xquic-lets.html">Unpatched XRING Flaw in XQUIC Lets Remote Clients Crash HTTP ...</a></li>
<li><a href="https://www.rescana.com/post/unpatched-xring-vulnerability-in-xquic-exposes-http-3-servers-to-remote-crash-risk">Unpatched XRING Vulnerability in XQUIC Exposes HTTP/3 Servers ...</a></li>
<li><a href="https://github.com/alibaba/xquic">GitHub - alibaba/xquic: XQUIC Library released by Alibaba is ...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#HTTP/3`, `#XQUIC`, `#networking`

---

<a id="item-9"></a>
## [NVIDIA 基于块的 GPU 编程指南：cuTile、Triton 与 Flash Attention](https://news.google.com/rss/articles/CBMi2wFBVV95cUxNLVk4TlRvM3g2eEpVVzg5YnZTWEhFLXhEamlSM1pfVnlZVkwxRlNSb0VoYmdhSlo3SVZpSG1VT3h1UjMweWVacHdIM2psWWQ3MGF0ZUNzVlhVclZzWExEblp3YlFTUkdUWVNJcHFKTlpmbDB6aHEyTTI0QWJmN2RkLXlYQVVKclRJdnh2ZlVFOVB5VjNwRnZ2VlBWbHdFcXJfWGFRQWI3QUg3YnRheDhURkx2Y3Rhc2U5SkprYjBQNE9vVVY1ZGQ1YUdjVmhGRUJwQnU4SVQ0a2VscWs?oc=5) ⭐️ 8.0/10

MarkTechPost 发布了一篇实用编码指南，涵盖 NVIDIA 基于块的 GPU 编程技术，包括 cuTile Python、Triton 内核和 Flash Attention。 该指南帮助 AI/ML 开发者和系统程序员利用基于块的编程来最大化 GPU 利用率，特别是对于 Transformer 中的注意力机制，这对大型语言模型至关重要。 cuTile Python 允许用 Python 编写块内核并自动访问张量核心；Triton 是一种基于 Python 的语言，用于编写自定义 DNN 内核；Flash Attention 是一种快速且内存高效的注意力算法。

google_news · MarkTechPost · 7月12日 00:01

**背景**: 基于块的 GPU 编程将数据划分为小块（tiles），这些块可以在 GPU 核心上并行处理，从而提高内存局部性和性能。NVIDIA 在 CUDA 13.1 中引入的 CUDA Tile 编程模型简化了这种方法。Triton 是一种开源的并行编程语言和编译器，广泛用于编写高效的深度学习内核。Flash Attention 是一种最新的算法，通过减少注意力计算中的内存读写，显著加速了 Transformer 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVIDIA/cutile-python">GitHub - NVIDIA/cutile-python: cuTile is a programming model for writing parallel kernels for NVIDIA GPUs · GitHub</a></li>
<li><a href="https://developer.nvidia.com/blog/simplify-gpu-programming-with-nvidia-cuda-tile-in-python/">Simplify GPU Programming with NVIDIA CUDA Tile in Python | NVIDIA Technical Blog</a></li>
<li><a href="https://github.com/triton-lang/triton">GitHub - triton-lang/triton: Development repository for the ...</a></li>

</ul>
</details>

**标签**: `#GPU Programming`, `#NVIDIA`, `#Triton`, `#Flash Attention`, `#AI/ML`

---

<a id="item-10"></a>
## [Anthropic 因计算限制延长 Fable 5 访问权限](https://simonwillison.net/2026/Jul/12/bump/#atom-everything) ⭐️ 7.0/10

Anthropic 因计算资源限制，将 Fable 5 模型在所有付费计划中的访问权限延长至 2026 年 7 月 19 日；与此同时，OpenAI 暂时取消了 Plus、Business 和 Pro 计划中 GPT-5.6 Sol 的使用限制。 这凸显了 AI 实验室面临的计算资源挑战及其在需求与可用性之间平衡的战略决策，可能影响用户选择以及 Anthropic 与 OpenAI 之间的竞争格局。 付费计划用户每周可将最多一半的使用额度用于 Fable 5，超出后可使用积分继续使用或切换模型。OpenAI 也在提升 GPT-5.6 Sol 的效率以减少用量消耗。

rss · Simon Willison · 7月12日 21:20

**背景**: Fable 5 是 Anthropic 的 Mythos 级模型，代表其最强大的广泛发布 AI 模型，专为高要求的编码和推理任务设计。GPT-5.6 Sol 是 OpenAI GPT-5.6 系列中的旗舰模型，同样专注于高级能力。这两个模型均于 2026 年 6 月发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Fable`, `#GPT-5.6`, `#compute constraints`

---

<a id="item-11"></a>
## [LVMH 秘密增持爱马仕股份案曝光，涉 150 亿美元诉讼](https://36kr.com/p/3892321158773251?f=rss) ⭐️ 7.0/10

LVMH 向巴黎法院提交了一份 20 页的答辩文件，详细披露了其二十多年来秘密增持爱马仕股份的过程，以回应爱马仕继承人尼古拉·皮埃什提起的 150 亿美元诉讼。 此案揭露了奢侈品集团收购竞争对手的激进策略，并引发了对公司治理和受托责任的质疑，可能对整个奢侈品行业产生影响。 LVMH 利用股权互换和衍生品，在 2012 年前秘密积累了爱马仕 22.6%的股份，规避了信息披露门槛；皮埃什声称其财务顾问在未经其知情的情况下出售了价值 150 亿美元的 600 万股股份，据称卖给了 LVMH。

rss · 36氪 · 7月12日 07:16

**背景**: 爱马仕是一家以铂金包和丝巾闻名的法国奢侈品制造商，由创始家族控制。LVMH 是全球最大的奢侈品集团，由贝尔纳·阿尔诺领导。2010 年，LVMH 披露持有爱马仕 17.1%的股份，引发法律纠纷，最终于 2014 年达成和解，LVMH 同意剥离其股份。当前的诉讼于 2025 年提起，指控 LVMH 通过皮埃什的顾问未经授权从其投资组合中收购股份。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/sustainability/boards-policy-regulation/lvmh-reaffirms-it-has-never-misappropriated-hermes-heirs-shares-2025-12-03/">LVMH has never misappropriated Hermes heir's shares, company says | Reuters</a></li>
<li><a href="https://www.thefashionlaw.com/hermes-vs-lvmh-a-timeline-of-the-drama/">Hermès vs. LVMH: The Timeline Behind a Takeover Attempt - The Fashion Law</a></li>
<li><a href="https://www.forbes.com/sites/zacharyfolk/2025/12/03/herms-heir-reportedly-sues-bernard-arnault-and-lvmh-alleging-16-billion-worth-of-herms-shares-sold-without-his-knowledge/">Hermès Heir Reportedly Sues Bernard Arnault And LVMH ...</a></li>

</ul>
</details>

**标签**: `#LVMH`, `#Hermès`, `#corporate governance`, `#luxury brands`, `#legal dispute`

---

<a id="item-12"></a>
## [具身数据行业：97 家玩家，融资 447 亿，十大趋势](https://36kr.com/p/3892027841362694?f=rss) ⭐️ 7.0/10

36 氪的一份全面报告显示，目前有 97 家公司活跃在中国具身数据行业，其中 15 家独立数据服务商在过去一年共融资 447 亿元。报告识别了十大关键趋势，包括四种主要数据采集路线和独立数据服务商的主导地位。 具身数据是训练机器人的关键瓶颈，这项分析提供了新兴生态系统的结构化概述，帮助投资者和从业者了解竞争格局。研究结果强调，数据采集已成为独立于机器人制造的行业，标志着供应链的成熟。 在 97 家玩家中，70 家专注于数据采集，27 家专注于数据基础设施。四种主要采集路线是真机遥操、无本体采集、仿真合成和互联网视频蒸馏，43%的公司采用多条路线。独立数据服务商是最大的群体（占 40%），67%的玩家是“具身原生”初创公司。

rss · 36氪 · 7月12日 02:16

**背景**: 具身 AI 指的是通过机器人与物理世界交互的 AI 系统。训练这类系统需要大量捕捉人类动作和机器人交互的数据，目前这些数据稀缺且采集成本高昂。该行业应运而生，旨在解决这一数据瓶颈，各种技术路线竞相提供成本效益高的训练数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huxiu.com/article/4870304.html">具身数据采集产业链调查：被机器人采集的人-虎嗅网</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/2026634205371668064">2026.3具身智能数据采集：路线、方法与规模化思考</a></li>
<li><a href="https://news.marsbit.co/20260712102912558212.html">news.marsbit.co/20260712102912558212.html</a></li>

</ul>
</details>

**标签**: `#embodied AI`, `#robotics`, `#data collection`, `#industry analysis`, `#funding`

---

<a id="item-13"></a>
## [AI 热潮推高燃气轮机价格 300%](https://36kr.com/newsflashes/3892556678543880?f=rss) ⭐️ 7.0/10

由于 AI 数据中心需求激增，过去三年燃气轮机价格累计上涨约 300%，微软近期向 GE Vernova 采购了 7 台大型燃气轮机用于其得州数据中心。 这一价格飙升凸显了 AI 基础设施面临的能源瓶颈，数据中心需要大量稳定电力，使 GE Vernova、卡特彼勒和西门子等燃气轮机制造商受益。 每台燃气轮机售价超过 2.5 亿美元，GE Vernova 股价过去六个月上涨超 70%。Melius Research 估计三年累计涨幅达 300%。

rss · 36氪 · 7月12日 11:37

**背景**: 燃气轮机是燃烧天然气发电的重型发电设备，常用于大规模、可靠的电力供应。AI 数据中心需要巨大且稳定的电力，推动了对这类涡轮机的需求。GE Vernova 是领先的燃气轮机制造商，其产品功率范围从 34 兆瓦到 571 兆瓦。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gevernova.com/gas-power/products/gas-turbines">Aeroderivative and Heavy-Duty Gas Turbines | GE Vernova</a></li>
<li><a href="https://www.binance.com/en/square/post/07-12-2026-microsoft-bought-seven-ge-vernova-gas-turbines-to-power-texas-data-center-343923870976737">Microsoft Bought Seven GE Vernova Gas Turbines to Power Texas...</a></li>
<li><a href="https://pulseaugur.com/cluster/138340-ai-boom-drives-300-surge-in-gas-turbine-prices">AI boom drives 300% surge in gas turbine prices · PulseAugur</a></li>

</ul>
</details>

**标签**: `#AI`, `#data centers`, `#energy`, `#gas turbines`, `#hardware`

---

<a id="item-14"></a>
## [莱斯大学与 NASA 发布开源太空机器人模拟器](https://news.google.com/rss/articles/CBMipAFBVV95cUxOMWprbUgzWmpGLWw3SHQtMjQwbk5LbExYaFozRXRxc2JkeF9VOFlZd1pUblhfSFhpVUFod0JMVE0tRm43X3hrQXlJMFdfczFzNmYwZ3gybGpqWUpjWlRyZlk2N01JMUtZR004bU9feENBeU5hcHFjOUhETDg2elVSVnZleVAyblV0amJKQmNES2RYVXZGei1teWRNQTBTemVmenFacg?oc=5) ⭐️ 7.0/10

莱斯大学与美国国家航空航天局（NASA）联合发布了 iMETRO，这是全球首个用于开发航天器及室内太空栖息地机器人的开源动态仿真环境。 该开源模拟器使全球工程师和研究人员无需昂贵的专有软件即可测试和开发太空任务机器人，从而推动了先进太空机器人研究的普及。 iMETRO 支持远程操作，专为模拟在航天器和太空栖息地内工作的机器人而设计，重点关注动态交互和实时控制。

google_news · AI Insider · 7月12日 06:21

**背景**: 太空机器人通常需要高保真仿真来测试自主系统，而此前这类模拟器多为专有或功能有限。iMETRO 旨在通过提供免费、开源且可定制的平台来填补这一空白，适用于多种太空机器人应用场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.rice.edu/news/2026/rice-and-nasa-launch-worlds-first-open-source-remote-space-robotics-simulator">Rice and NASA launch world’s first open-source remote space ...</a></li>
<li><a href="https://sciencesensei.com/rice-and-nasa-launch-world-s-first-open-source-remote-space-robotics-simulator/">Rice and NASA Release the First Open-Source Remote Space ...</a></li>
<li><a href="https://theaiinsider.tech/2026/07/12/rice-and-nasa-launch-open-source-remote-space-robotics-simulator/">Rice and NASA Launch Open-source Remote Space Robotics Simulator</a></li>

</ul>
</details>

**标签**: `#robotics`, `#space`, `#open-source`, `#simulation`, `#NASA`

---

<a id="item-15"></a>
## [NVIDIA 机器人策略评估指南](https://news.google.com/rss/articles/CBMiqwFBVV95cUxOVU50bTFobzVya1p4ZUd5b1JMMzl6VFpsZDZrQ2pFMm9yOEF2VzRVeTBVeFFVcVIyc1oyYXhOUVB3aFhiYlRxR3YyVHFKOHgwWEpxelAyODlkT0RIX1k2MS1CX2FUamJIUEFSVHhuVzh6Q1otNFRsX1ctNkptVXl0SzVpcFRVZUJDUlpXSzdDS2RRcHF0djk2aTJLd0JmVjlwNmZiaWlybHdWU28?oc=5) ⭐️ 7.0/10

NVIDIA Developer 发布了一篇博客文章，详细介绍了如何评估用于实际部署的通用机器人策略，强调仅凭成功率是不够的。 随着通用机器人策略日益普及，正确的评估指标对于在实际环境中安全有效地部署至关重要。该指南帮助研究人员和从业者避免因简单指标而得出误导性结论。 该博客认为，成功率几乎无法说明机器人如何执行任务，只能说明它是否完成了任务。它可能提出了替代指标，如鲁棒性、效率和安全性的全面评估。

google_news · NVIDIA Developer · 7月12日 01:21

**背景**: 通用机器人策略是在多样化数据上训练的人工智能模型，用于控制不同任务和环境中的各种机器人。评估这些策略的实际部署具有挑战性，因为传统指标（如成功率）无法捕捉细微的性能方面，例如从故障中恢复或能源效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/">How to Evaluate General-Purpose Robot Policies for Real-World...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#AI`, `#deployment`, `#NVIDIA`, `#policy evaluation`

---

<a id="item-16"></a>
## [腾讯重仓 DPU 初创公司云豹智能冲刺 IPO](https://36kr.com/p/3892352153942530?f=rss) ⭐️ 6.0/10

深圳云豹智能股份有限公司（Cloudbloom Intelligence）已向深交所创业板提交 IPO 申请，目标成为“国产 DPU 第一股”，该公司由腾讯重仓支持。 此次 IPO 申请凸显了 DPU 在 AI 和云基础设施中日益增长的重要性，并可能为更多中国半导体初创公司上市铺平道路，尤其是在创业板新上市规则允许未盈利科技企业上市的背景下。 云豹智能自主研发的 DPU SoC 芯片网络带宽达 400Gbps，相比传统方案性能提升 4 倍、功耗降低 50%以上。公司目前仍处于亏损状态，2023 年、2024 年、2025 年净亏损分别为 6.67 亿元、6 亿元、11.9 亿元。

rss · 36氪 · 7月12日 07:59

**背景**: DPU（数据处理单元）是一种专用处理器，用于处理数据中心的数据移动和处理，从而减轻 CPU 和 GPU 的负担。英伟达 CEO 黄仁勋曾将 DPU 描述为未来计算的三大支柱之一，与 CPU 和 GPU 并列。云豹智能由斯坦福博士萧启阳于 2020 年创立，已进行多轮融资，其中腾讯持股 19.78%，为第一大股东。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/660108879">什么是DPU？一文带你搞懂！ - 知乎</a></li>
<li><a href="https://www.jaguarmicro.com/">云 豹 智 能 【 云 豹 智 能 】专注于 云 计算和数据处理器 DPU 芯片与解决方案</a></li>
<li><a href="https://global.chinadaily.com.cn/a/202604/11/WS69d9b077a310d6866eb42d4e.html">China unveils ChiNext reforms to bolster innovation, broaden ...</a></li>

</ul>
</details>

**标签**: `#DPU`, `#IPO`, `#semiconductor`, `#Tencent`, `#startup`

---

<a id="item-17"></a>
## [Anthropic 澄清 Claude Code 变笨是 Effort 设置问题，非模型问题](https://36kr.com/p/3892222176574211?f=rss) ⭐️ 6.0/10

Anthropic 发布博文解释，许多用户错误地将 Claude Code 的性能不佳归咎于模型大小，而真正的问题往往是“Effort”设置。今年 3 月，Anthropic 为降低延迟悄悄将默认 Effort 从 high 降为 medium，引发了大量关于质量下降的投诉。 这一澄清帮助开发者优化 Claude Code 的使用：小模型配合高 Effort 可能胜过大型模型配合低 Effort，从而节省成本并提升效果。它也凸显了 AI 编程工具中配置设置的重要性——这些设置常被忽视。 Effort 控制 Claude 在推理、工具调用和验证上花费的 token 数量，而不仅仅是思考时间。高 Effort 的提示可能比低 Effort 多生成多达 7 倍的 token，多出的 token 用于读取文件、运行测试和完成多步骤任务。

rss · 36氪 · 7月12日 05:47

**背景**: Claude Code 提供两个主要设置：Model（如 Sonnet、Opus、Fable）决定底层的冻结权重和知识，Effort（low、medium、high、max）控制模型处理任务的彻底程度。许多用户认为仅升级模型就能提升性能，但 Effort 设置对输出质量和行为有显著影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/claude-model-and-effort-level-in-claude-code">Choosing a Claude model and effort level in Claude Code ...</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/effort">Effort - Claude Platform Docs</a></li>
<li><a href="https://www.mindstudio.ai/blog/claude-code-effort-levels-explained">Claude Code Effort Levels Explained: When to Use Low, Medium ...</a></li>

</ul>
</details>

**标签**: `#Claude`, `#AI`, `#Anthropic`, `#coding tools`, `#misconceptions`

---