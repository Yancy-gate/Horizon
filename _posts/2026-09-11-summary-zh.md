---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
---

> 从 143 条内容中筛选出 48 条重要资讯。

---

## 偏好雷达

> 基于你维护的偏好档案（data/preference-radar/profile.json）独立筛选的个性化内容。

今日暂无符合偏好的更新。

---
## 华科老师研究方向

> 依据学院教师公开研究方向与论文关键词筛选。

1. [RAMamba-Net 提升可靠性感知的听觉注意检测](#item-1) ⭐️ 7.0/10
2. [自适应电压源协调提升 VSG 逆变器暂态稳定性](#item-2) ⭐️ 7.0/10
3. [注入时刻无位置传感控制改进表贴式永磁电机预测电流控制](#item-3) ⭐️ 7.0/10
4. [采样延迟加剧并网跟随型逆变器高频不稳定](#item-4) ⭐️ 7.0/10
5. [关键基础设施最坏情况中断的模型与算法](#item-5) ⭐️ 7.0/10
6. [STO-CAST 实时预测热带气旋停电](#item-6) ⭐️ 7.0/10
7. [概率分层匹配提升电动汽车调度与电网可靠性](#item-7) ⭐️ 7.0/10
8. [概率分层匹配提升电动汽车调度与电网性能](#item-8) ⭐️ 7.0/10
9. [概率调度平衡电动公交与电网负荷](#item-9) ⭐️ 7.0/10
10. [固体氧化物燃料电池系统控制综述](#item-10) ⭐️ 6.0/10
11. [结合自适应谐波滤波的改进型永磁同步电机无位置传感器控制](#item-11) ⭐️ 6.0/10
12. [公交网络设计纳入快速公交车道共享](#item-12) ⭐️ 6.0/10
13. [基于分层匹配的车辆调度方法](#item-13) ⭐️ 5.0/10
14. [研究整合公交网络设计与时刻表同步。](#item-14) ⭐️ 5.0/10

---
<a id="item-1" class="hz-item-anchor" data-hz-url="https://arxiv.org/abs/2609.11372v1" data-hz-title="RAMamba-Net提升可靠性感知的听觉注意检测" data-hz-tags="Auditory attention detection,Multimodal learning,EEG-EOG fusion,Mamba,Neural signal processing" data-hz-section="hust-research"></a>
## [RAMamba-Net 提升可靠性感知的听觉注意检测](https://arxiv.org/abs/2609.11372v1) ⭐️ 7.0/10

RAMamba-Net 结合基于 Mamba 的时序建模、跨模态注意力和逐样本可靠性加权，融合 EEG 与 EOG 信号以进行听觉注意检测。据报告，该模型在两个基准数据集上的准确率比单模态基线提高了 5.76%。 该架构有望提高自然视听场景中听觉注意解码的稳健性，因为这些场景里的 EEG 或 EOG 证据可能不完整或不可靠。它可能推动神经控制助听设备以及基于生理信号的人机交互。 该模型使用经 Mamba 增强的频带感知卷积 Transformer 处理 EEG，以双分支时空编码器处理 EOG，并通过跨模态注意力实现显式交互。其可靠性模块会针对每个样本调整模态权重，据报告可抵抗信号扰动和参数变化，但目前证据仅来自论文在两个基准数据集上的实验，尚无所述的独立复现结果。

rss · 华科 AIA 论文 · 类脑与计算智能 · 9月10日 11:08

**匹配依据**: 论文关键词命中 **EEG**（类脑与计算智能）。

**关联教师**: 万一鸣、伍冬睿、卢仁智、叶林涛、周凯波、唐朝清、姜军、张征 等共 22 人

**背景**: 听觉注意检测旨在判断听者在多人说话环境中正在关注哪位说话者，通常利用测量脑活动的 EEG 信号。EOG 记录与眼球运动有关的电活动，可在自然视听场景中提供互补证据。Mamba 是一种选择性状态空间序列架构，能够高效建模长程依赖，而可靠性感知融合则可降低单个样本中噪声较大或信息不足模态的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.13770">NeuroMambaLLM: Dynamic Graph Learning of fMRI Functional...</a></li>
<li><a href="https://arxiv.org/pdf/2505.15364">MHANet: Multi-scale Hybrid Attention Network for Auditory ...</a></li>
<li><a href="https://ieeexplore.ieee.org/document/4518144/">A reliability guided sensor fusion model for optimal weighting in multimodal systems | IEEE Conference Publication | IEEE Xplore</a></li>

</ul>
</details>

**标签**: `#Auditory attention detection`, `#Multimodal learning`, `#EEG-EOG fusion`, `#Mamba`, `#Neural signal processing`

---

<a id="item-2" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560379" data-hz-title="自适应电压源协调提升VSG逆变器暂态稳定性" data-hz-tags="Grid-forming inverters,Virtual synchronous generators,Transient stability,Power systems control,Renewable energy integration" data-hz-section="hust-research"></a>
## [自适应电压源协调提升 VSG 逆变器暂态稳定性](https://doi.org/10.1109/ccdc69976.2026.11560379) ⭐️ 7.0/10

该论文提出一种面向虚拟同步发电机控制型构网型逆变器的快速与慢速内部电压源自适应协调策略。该策略旨在根据系统状态调整内部电压源动态，从而提升逆变器的暂态稳定性。 提升暂态稳定性有助于构网型逆变器在较大扰动期间保持更强的运行能力，从而支持可再生能源更可靠地接入以逆变器为主的电力系统。自适应协调还有望在快速扰动响应与稳定运行所需的较慢动态之间取得平衡。 该研究的重点是协调两种内部电压源动态，而不是依赖单一且固定的响应特性。目前提供的信息不包含论文摘要、测试条件、定量结果，也没有硬件或更大规模系统验证证据，因此尚无法判断其性能提升幅度。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **grid-forming**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 构网型逆变器能够主动调节自身电压，并帮助建立电网电压与频率，而不只是跟随已经形成的电网波形。虚拟同步发电机控制会模拟传统同步发电机的部分特性，例如惯性、阻尼以及与频率相关的功率响应。暂态稳定性描述电力系统及其受控设备在发生较大扰动后继续保持可运行状态的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0142061519342723">A comprehensive review of virtual synchronous generator</a></li>
<li><a href="https://arxiv.org/pdf/2212.03053">Control of Grid-Forming VSCs: A Perspective of Adaptive Fast ...</a></li>

</ul>
</details>

**标签**: `#Grid-forming inverters`, `#Virtual synchronous generators`, `#Transient stability`, `#Power systems control`, `#Renewable energy integration`

---

<a id="item-3" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/tpel.2026.3678851" data-hz-title="注入时刻无位置传感控制改进表贴式永磁电机预测电流控制" data-hz-tags="Power Electronics,Sensorless Motor Control,Model Predictive Control,Permanent-Magnet Synchronous Motors,Finite-Control-Set Control" data-hz-section="hust-research"></a>
## [注入时刻无位置传感控制改进表贴式永磁电机预测电流控制](https://doi.org/10.1109/tpel.2026.3678851) ⭐️ 7.0/10

该论文提出了一种基于注入时刻的开关频率注入无位置传感方法，并将其与扩展控制集死区拍预测电流控制结合，用于表贴式永磁同步电机。实验结果表明，该方法能够提高电压注入精度、缩短执行时间、实现初始转子位置检测，并抑制由电流偏置引起的速度振荡。 开关频率注入适用于低速或静止状态下的转子位置估计，但有限控制集中的电压矢量不准确会恶化位置误差信号和电流调节性能。该方法通过减少注入误差和计算开销，有望提升无位置传感预测控制在高性能电机驱动等专用场景中的实用性。 所提出的控制器采用角度域迭代优化方法和扩展控制集，以实现死区拍电流控制；注入时刻策略则旨在避免为补偿有限控制集注入误差而产生的较长执行时间。论文还研究了与直轴电流偏置相关的速度振荡，并在目标表贴式永磁同步电机上进行了实验验证。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 3月31日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 开关频率注入通过施加高频电压信号并观察电机电流响应来估计转子位置，尤其适用于低速或静止状态。表贴式永磁同步电机的转子磁各向异性相对较弱，因此可靠的无位置传感位置估计更具挑战性。有限控制集模型预测控制从离散的逆变器电压矢量中进行选择，而扩展控制集提供更多可选矢量，有助于改善电流调节，但也可能增加计算负担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/370272029_Sensorless_Control_with_Switching_Frequency_Square_Wave_Voltage_Injection_for_SPMSM_with_Low_Rotor_Magnetic_Anisotropy">(PDF) Sensorless Control With Switching Frequency Square Wave...</a></li>
<li><a href="https://www.mdpi.com/2079-9292/12/23/4726">FPGA-Based Extended Control Set Model Predictive Current Control with a Simplified Search Strategy for Permanent Magnet Synchronous Motor</a></li>

</ul>
</details>

**标签**: `#Power Electronics`, `#Sensorless Motor Control`, `#Model Predictive Control`, `#Permanent-Magnet Synchronous Motors`, `#Finite-Control-Set Control`

---

<a id="item-4" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/apec51134.2026.11516799" data-hz-title="采样延迟加剧并网跟随型逆变器高频不稳定" data-hz-tags="Power Electronics,Grid-Connected Inverters,Passivity-Based Control,Control Delays,Grid Stability" data-hz-section="hust-research"></a>
## [采样延迟加剧并网跟随型逆变器高频不稳定](https://doi.org/10.1109/apec51134.2026.11516799) ⭐️ 7.0/10

该论文定量分析了采样周期和采样时刻如何影响并网跟随型逆变器导纳在奈奎斯特频率以上的负阻尼区域。论文还提出了一种考虑频率混叠的基于无源性的阻尼方法，实验验证了其能够改善高频稳定性。 高频非无源导纳可能导致并网逆变器不稳定，因此这些结果为更精确地评估控制延迟的影响提供了方法。所提出的方法有望帮助电力电子研究人员和工程师提升逆变器占主导电网的稳定性。 提高采样频率可以减弱奈奎斯特频率以上的部分非无源行为，但不能消除高频不稳定性的根本机制。该研究区分了绝对延迟和相对延迟的影响，并通过实验验证了分析结论。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 3月22日 00:00

**匹配依据**: 论文关键词命中 **grid-following**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 并网跟随型逆变器依靠现有电网进行同步，并通过控制系统传输电能。输出导纳描述逆变器对电压扰动的电气响应，因此可用于稳定性评估。奈奎斯特频率是采样频率的一半，超过这一频率的行为可能受到采样和频率混叠的影响。无源系统在相关交互中不会产生净能量，而非无源行为可能引入负阻尼并促进不稳定。

**标签**: `#Power Electronics`, `#Grid-Connected Inverters`, `#Passivity-Based Control`, `#Control Delays`, `#Grid Stability`

---

<a id="item-5" class="hz-item-anchor" data-hz-url="https://doi.org/10.1016/j.ress.2026.113133" data-hz-title="关键基础设施最坏情况中断的模型与算法" data-hz-tags="Critical Infrastructure,Reliability Engineering,Resilience,Disruption Modeling,Algorithms" data-hz-section="hust-research"></a>
## [关键基础设施最坏情况中断的模型与算法](https://doi.org/10.1016/j.ress.2026.113133) ⭐️ 7.0/10

《可靠性工程与系统安全》发表了一篇论文，研究识别和缓解关键基础设施系统最坏情况中断的模型与算法。现有信息没有说明具体算法、研究结果或评估案例。 系统分析最坏情况中断，有助于支持关键基础设施的可靠性工程、韧性规划和决策制定。其实际影响仍取决于论文中的具体方法和证据，而这些信息目前尚未提供。 该研究同时关注中断建模和算法缓解，表明其不仅研究如何识别严重的系统后果，也研究如何选择降低这些后果的方法。所提供的材料没有包含摘要、定量结果、局限性或实际应用验证。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 7月10日 00:00

**匹配依据**: 论文关键词命中 **critical infrastructure**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 关键基础设施系统一旦发生中断，可能造成严重的运行后果，但现有材料没有指出具体涉及哪些基础设施领域。在这一语境下，中断建模用于表示故障或中断如何影响系统，而算法则是用于识别严重情景或确定缓解措施的计算方法。可靠性工程关注系统能否持续稳定运行，韧性则关注系统承受和恢复中断的能力。

**标签**: `#Critical Infrastructure`, `#Reliability Engineering`, `#Resilience`, `#Disruption Modeling`, `#Algorithms`

---

<a id="item-6" class="hz-item-anchor" data-hz-url="https://doi.org/10.1111/risa.70275" data-hz-title="STO-CAST实时预测热带气旋停电" data-hz-tags="Deep Learning,Spatiotemporal Forecasting,Power Systems,Disaster Response,Extreme Weather" data-hz-section="hust-research"></a>
## [STO-CAST 实时预测热带气旋停电](https://doi.org/10.1111/risa.70275) ⭐️ 7.0/10

研究人员推出了 STO-CAST 时空深度学习模型，可在热带气旋期间利用不断变化的天气预报和最新停电观测持续更新停电预测。该模型以 4×4 公里分辨率按小时生成预测，覆盖 6 小时短期临近预报和 60 小时长期规划预报。 通过随着风暴条件和电力系统状态变化而更新预测，STO-CAST 有望帮助电力公司改进实时应急响应，并在灾害影响发生前部署人员和设备。其较高的空间分辨率还可以支持针对易受影响地区和基础设施韧性的更精准决策。 研究以 2022 年台风梅花为案例，并采用留一风暴评估框架；模型还通过误差分解区分模型局限、气象不确定性和停电观测缺失的影响。现有证据仍然有限，因为报告中的评估主要基于单个案例，而不是大量风暴的广泛验证。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月26日 00:00

**匹配依据**: 论文关键词命中 **tropical cyclone**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 传统停电预测模型通常以开环或事件级方式运行，这意味着事件发展过程中出现的新观测不会被持续纳入预测。STO-CAST 则执行依赖系统状态、由观测更新的滚动推理，将静态的基础设施和环境属性与动态天气及停电序列结合起来。生成的预测既用于即时态势感知，也用于提前规划资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/42186946/">From Forecast to Action: A Deep Learning Model for Predicting Power Outages During Tropical Cyclones - PubMed</a></li>
<li><a href="https://arxiv.org/abs/2512.06644">[2512.06644] From Forecast to Action: A Deep Learning Model for Predicting Power Outages During Tropical Cyclones</a></li>

</ul>
</details>

**标签**: `#Deep Learning`, `#Spatiotemporal Forecasting`, `#Power Systems`, `#Disaster Response`, `#Extreme Weather`

---

<a id="item-7" class="hz-item-anchor" data-hz-url="https://doi.org/10.6084/m9.figshare.31910706" data-hz-title="概率分层匹配提升电动汽车调度与电网可靠性" data-hz-tags="Electric Vehicles,Stochastic Optimization,Power Grid,Transportation Scheduling,Operations Research" data-hz-section="hust-research"></a>
## [概率分层匹配提升电动汽车调度与电网可靠性](https://doi.org/10.6084/m9.figshare.31910706) ⭐️ 7.0/10

该研究提出了一种概率分层匹配（P-HM）方法，用于随机电动汽车调度，并同时考虑车队规模、运营成本、充电峰值负荷和准时率。数值实验表明，P-HM 优于基准方法，尤其能够减少车队规模，同时提升调度鲁棒性和电网安全性。 电动汽车调度会受到行程时间不确定性的影响，而这种不确定性可能改变充电需求并加剧峰值负荷。该方法将交通调度与电网负荷结合考虑，有望提升公共交通运营的可靠性，并减轻电力基础设施压力。 该方法将时刻表划分为多个层级，并依据兼容概率匹配相邻层级，随后采用贪心局部搜索来减少充电负荷违规。现有证据来自数值实验，因此根据所提供的信息，尚无法确定其在测试场景之外的表现。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 电动汽车调度问题是指在满足运营约束和充电约束的条件下，为各项行程分配电动汽车。随机调度考虑行程时间变化等不确定因素，而不是假设每次行程都具有固定时长。在该研究中，充电需求与调度不确定性相互关联，因为车辆运行变化会影响车辆充电的时间以及电网承受的负荷。

**标签**: `#Electric Vehicles`, `#Stochastic Optimization`, `#Power Grid`, `#Transportation Scheduling`, `#Operations Research`

---

<a id="item-8" class="hz-item-anchor" data-hz-url="https://doi.org/10.6084/m9.figshare.31910706.v1" data-hz-title="概率分层匹配提升电动汽车调度与电网性能" data-hz-tags="Electric Vehicle Scheduling,Power Grid Optimization,Stochastic Optimization,Operations Research,Smart Transportation" data-hz-section="hust-research"></a>
## [概率分层匹配提升电动汽车调度与电网性能](https://doi.org/10.6084/m9.figshare.31910706.v1) ⭐️ 7.0/10

该论文提出了概率分层匹配（P-HM）方法，用于随机电动汽车调度，并同时考虑车辆规模、运营成本、充电峰值负荷和准点性能。数值实验表明，P-HM 整体优于基准方法，尤其能够减少所需车辆数量，同时提升系统鲁棒性和电网安全性。 该方法处理了不确定行程时间与充电需求之间的相互影响，而不是将交通调度和电网安全割裂开来。它有望帮助公共交通运营者在保持服务可靠性的同时减少车辆需求和充电峰值，降低电网压力。 P-HM 将时刻表划分为多个层级，并依据兼容概率匹配相邻层级，随后通过贪心局部搜索缓解充电峰值负荷超限问题。现有证据主要来自数值对比，而所提供的内容未包含独立验证或讨论质量方面的证据。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 电动汽车调度问题是指在满足时刻表和运营要求的前提下，为公共交通行程分配电动汽车。由于行程时间可能发生变化，车辆到达充电地点的时间具有不确定性，从而改变充电需求并可能推高电网峰值负荷。随机调度模型会明确表示这种不确定性，而分层匹配则通过将时刻表安排组织成不同层级，使调度过程更易于处理。

**标签**: `#Electric Vehicle Scheduling`, `#Power Grid Optimization`, `#Stochastic Optimization`, `#Operations Research`, `#Smart Transportation`

---

<a id="item-9" class="hz-item-anchor" data-hz-url="https://doi.org/10.1080/0305215x.2026.2643627" data-hz-title="概率调度平衡电动公交与电网负荷" data-hz-tags="Electric Vehicle Scheduling,Stochastic Optimization,Power Grid Security,Operations Research,Public Transport" data-hz-section="hust-research"></a>
## [概率调度平衡电动公交与电网负荷](https://doi.org/10.1080/0305215x.2026.2643627) ⭐️ 7.0/10

该研究提出了概率分层匹配（P-HM）算法，用于随机电动公交调度，在提高准点率的同时联合最小化车队规模、运营成本和充电峰值负荷。数值结果表明，P-HM 优于基准方法，尤其能够减少车队规模，并提升方案稳健性与电网安全性。 电动公交调度需要同时应对不确定的行程时间和充电需求，因为充电时机不当可能提高电力系统峰值负荷并削弱服务可靠性。该方法将车辆运营与电网影响纳入同一优化框架，有望支持更加可靠且更适应电网的公共交通电动化。 该方法将时刻表划分为多个层级，并依据兼容概率匹配相邻层级，随后使用贪心局部搜索减少峰值负荷约束违反。研究结论来自所提出模型的数值实验，因此其适用性可能取决于实验所代表的运营条件、时刻表结构和充电基础设施。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 电动汽车调度问题是指在满足班次覆盖和时间安排等运营约束的前提下，为各项行程分配车辆。在电动公交系统中，充电决策会增加复杂性，因为公交车从电网取电，可能形成集中的需求峰值。随机调度通过概率方式表示行程时间等不确定因素，而不是假设每次行程都具有固定时长。现有研究已经采用精确方法和启发式方法处理不同规模的电动公交充电与调度问题，因此，这项研究的分层匹配策略属于应对计算复杂性和现实不确定性的更广泛探索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2509.04533v1">Resource-Oriented Optimization of Electric Vehicle Systems: A Data-Driven Survey on Charging Infrastructure, Scheduling, and Fleet Management</a></li>
<li><a href="https://ideas.repec.org/a/eee/transb/v155y2022icp322-347.html">The multi-depot electric vehicle scheduling problem with power grid ...</a></li>

</ul>
</details>

**标签**: `#Electric Vehicle Scheduling`, `#Stochastic Optimization`, `#Power Grid Security`, `#Operations Research`, `#Public Transport`

---

<a id="item-10" class="hz-item-anchor" data-hz-url="https://doi.org/10.23919/pcmp.2025.000294" data-hz-title="固体氧化物燃料电池系统控制综述" data-hz-tags="Solid Oxide Fuel Cells,Control Systems,Energy Systems,Power Electronics,Review Article" data-hz-section="hust-research"></a>
## [固体氧化物燃料电池系统控制综述](https://doi.org/10.23919/pcmp.2025.000294) ⭐️ 6.0/10

这篇综述系统梳理了固体氧化物燃料电池（SOFC）系统的控制目标、控制策略和主要挑战。文章综合了燃料利用率、空气管理、热调节和系统级运行等方面的既有研究，而不是提出单一的全新实验突破。 SOFC 系统需要协调电化学性能、燃料供应、空气流量、温度和功率输出，因此控制设计会直接影响效率、安全性和负荷跟踪能力。系统性综述有助于能源系统与控制领域的研究人员比较不同方法，并识别其进一步推广前仍需解决的问题。 控制问题包括管理燃料利用率和空气供应，同时保持热安全，因为 SOFC 运行会将电气行为与较慢的热动态过程耦合起来。既有研究包括协调氢气流量与燃料利用率控制，以及防止 SOFC—燃气轮机混合系统中的压气机失速或喘振。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 7月1日 00:00

**匹配依据**: 论文关键词命中 **fuel cell**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 固体氧化物燃料电池在高温下通过电化学反应发电，其运行条件会同时影响功率输出和热量产生。燃料利用率表示输入燃料中被消耗的比例，而空气管理会影响反应物供应和热状态。这些相互耦合的变量使快速负荷变化和温度保护成为重要的控制难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mdpi.com/1996-1073/17/5/1005">A Comprehensive Review of Thermal Management in Solid Oxide ...</a></li>
<li><a href="https://www.researchgate.net/publication/222404686_Control_strategy_for_a_solid_oxide_fuel_cell_and_gas_turbine_hybrid_systemJ">Control strategy for a solid oxide fuel cell and gas turbine hybrid...</a></li>
<li><a href="https://sci-hub.su/meta/10.1016/j.ijhydene.2016.10.107">Improving the load-following capability of a solid oxide fuel cell ...</a></li>

</ul>
</details>

**标签**: `#Solid Oxide Fuel Cells`, `#Control Systems`, `#Energy Systems`, `#Power Electronics`, `#Review Article`

---

<a id="item-11" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560068" data-hz-title="结合自适应谐波滤波的改进型永磁同步电机无位置传感器控制" data-hz-tags="PMSM control,Sensorless control,Active disturbance rejection,Adaptive filters,Electric motor drives" data-hz-section="hust-research"></a>
## [结合自适应谐波滤波的改进型永磁同步电机无位置传感器控制](https://doi.org/10.1109/ccdc69976.2026.11560068) ⭐️ 6.0/10

该论文提出了一种用于永磁同步电机的无位置传感器控制方法，将改进型自抗扰控制与并行自适应谐波滤波器相结合。该方法旨在提升电机运行过程中的转子位置估计能力和扰动抑制能力。 在不使用物理位置传感器的情况下实现准确的位置估计，有助于构建更简单、成本更低且可能更稳健的电机驱动系统。增强扰动抑制和谐波滤波能力可能有利于永磁同步电机控制应用，但该研究的影响范围较为专业，且目前没有更广泛的验证信息。 该方法将改进型自抗扰控制器与并行自适应谐波滤波器结合使用，而不是依赖单一的估计或滤波机制。现有信息未提供定量结果、运行条件、硬件细节或与其他方法的对比。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 永磁同步电机是一种在转子中使用永磁体的电机，通常需要准确的转子位置估计来实现控制。无位置传感器控制不使用专用位置传感器，而是获取转子位置；自抗扰控制则用于估计并补偿影响系统的扰动。自适应谐波滤波器能够调整自身的滤波行为，以减少可能干扰位置估计和控制的谐波成分。

**标签**: `#PMSM control`, `#Sensorless control`, `#Active disturbance rejection`, `#Adaptive filters`, `#Electric motor drives`

---

<a id="item-12" class="hz-item-anchor" data-hz-url="https://doi.org/10.23919/csms.2025.0021" data-hz-title="公交网络设计纳入快速公交车道共享" data-hz-tags="Transportation Optimization,Operations Research,Genetic Algorithms,BRT Systems,Network Design" data-hz-section="hust-research"></a>
## [公交网络设计纳入快速公交车道共享](https://doi.org/10.23919/csms.2025.0021) ⭐️ 6.0/10

该论文提出了一种明确纳入快速公交车道共享的公交网络设计与频率设置双层模型。研究还提出了基于优先级的遗传算法，在 Mandl 基准实例上取得接近最优的结果，并在临沂实际网络中降低乘客和运营商成本、提高快速公交车道利用率。 该方法允许普通公交在不干扰快速公交既定运营的情况下使用快速公交车道，有望提升公交速度和换乘效率，并更充分地利用专用基础设施。它为交通规划者提供了一种同时评估网络结构、服务频率、乘客成本和运营商成本的方法，而不是将车道共享作为事后因素处理。 该模型通过新增的快速公交节点和快速公交车道弧表示共享车道基础设施，算法则使用基于优先级的染色体，并设计了相应的交叉和变异算子。研究验证涵盖标准基准实例和临沂的一个实际网络，因此结果表明了计算性能和局部实践收益，但尚不能证明其适用于所有城市。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 6月1日 00:00

**匹配依据**: 论文关键词命中 **bus transit**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 快速公交是通过较少停站、专用车道和优先通行措施等方式，提供更快、更可靠出行服务的公交系统。快速公交车道共享允许普通公交使用这些车道，同时继续维持既定的快速公交运营。双层模型将相互关联的规划决策和响应决策分成两个相互连接的优化层次，而遗传算法则通过迭代改进编码后的候选方案来搜索较优解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciopen.com/article/10.23919/CSMS.2025.0021">Optimal Design of Bus Transit Networks Incorporating BRT-Lane ...</a></li>
<li><a href="https://nacto.org/wp-content/uploads/service_design_guidelines_vta.pdf">BUS RAPID TRANSIT SERVICE DESIGN GUIDELINES</a></li>

</ul>
</details>

**标签**: `#Transportation Optimization`, `#Operations Research`, `#Genetic Algorithms`, `#BRT Systems`, `#Network Design`

---

<a id="item-13" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560172" data-hz-title="基于分层匹配的车辆调度方法" data-hz-tags="vehicle scheduling,matching algorithms,operations research,optimization" data-hz-section="hust-research"></a>
## [基于分层匹配的车辆调度方法](https://doi.org/10.1109/ccdc69976.2026.11560172) ⭐️ 5.0/10

该论文提出了一种基于分层匹配的车辆调度问题解决方法。现有信息未提供该算法的具体设计、评估方式或实验结果。 车辆调度是一类需要有效分配和协调车辆的优化问题，因此分层匹配方法可能有助于改进调度决策的组织方式。不过，仅凭标题和摘要式简介还无法判断该方法的实际影响。 目前能够确认的核心技术要素包括分层匹配、车辆调度和优化。现有材料没有说明问题约束、匹配流程、计算复杂度、基准对比结果或方法局限性。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 车辆调度主要涉及如何分配和安排车辆，以满足调度要求。匹配算法通常用于确定可用选项之间的合适配对，而分层方法则会在多个层级上组织这些决策。这些概念属于运筹学和优化领域。

**标签**: `#vehicle scheduling`, `#matching algorithms`, `#operations research`, `#optimization`

---

<a id="item-14" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11559800" data-hz-title="研究整合公交网络设计与时刻表同步。" data-hz-tags="Transportation Optimization,Public Transit,Timetable Synchronization,Network Design,Operations Research" data-hz-section="hust-research"></a>
## [研究整合公交网络设计与时刻表同步。](https://doi.org/10.1109/ccdc69976.2026.11559800) ⭐️ 5.0/10

该论文研究一种综合方法，同时开展公交网络设计与多模式公共交通系统的时刻表同步。现有材料未披露其优化模型、算法、数据集或量化结果。 联合优化可以让线路与时刻表协同运行，与分别规划各组成部分相比，可能改善换乘衔接并减少乘客等待时间。这对需要协调公交、轨道交通及其他出行方式的公共交通机构具有现实意义。 该研究的核心技术特点，是在多模式交通系统中整合公交网络设计与时刻表同步这两个相互关联的规划问题。由于未提供论文正文或研究结果，目前无法评估其优化目标、约束条件、求解方法、计算扩展能力和实际效果。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **timetable**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 多模式公共交通网络设计旨在确定公交和快速交通等不同运输方式应如何布局，同时考虑方式之间的相互作用与换乘。时刻表同步通过协调车辆到达和发车时间，减少乘客换乘时的等待。既有研究曾使用近似算法处理换乘协调问题，也曾将时刻表协调与车辆调度结合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0968090X24000962">Redesigning large-scale multimodal transit networks with ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0191261519301201">Transit timetable synchronization for transfer time ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0360835223006010">Optimizing public transport transfers by integrating ...</a></li>

</ul>
</details>

**标签**: `#Transportation Optimization`, `#Public Transit`, `#Timetable Synchronization`, `#Network Design`, `#Operations Research`

---

## 其他资讯

15. [Rust 成为微软的一级语言](#item-15) ⭐️ 9.0/10
16. [Calif Research 声称人工智能辅助开发微信零点击蠕虫](#item-16) ⭐️ 9.0/10
17. [Shopify 正从 React Native 转回 Swift 和 Kotlin](#item-17) ⭐️ 8.0/10
18. [OpenAI 推出托管式 Agents API](#item-18) ⭐️ 8.0/10
19. [Astra 编程版：我们为什么又要这么做？](#item-19) ⭐️ 8.0/10
20. [研究人员质疑 OpenAI 是否值得托付未发表数学成果](#item-20) ⭐️ 8.0/10
21. [Forgejo 16.0.3 及更早版本存在严重远程代码执行漏洞](#item-21) ⭐️ 8.0/10
22. [在浏览器中运行任意 Nix 软件包](#item-22) ⭐️ 8.0/10
23. [四色定理获得罕见的新证明](#item-23) ⭐️ 8.0/10
24. [变革性人工智能的经济情景框架](#item-24) ⭐️ 8.0/10
25. [IBM 与 NASA 发布开放月球基础模型和 SomBench 数据集](#item-25) ⭐️ 8.0/10
26. [数据中心为何难以实现表后供电](#item-26) ⭐️ 7.0/10
27. [Anthropic 称人工智能模型蒸馏活动加剧](#item-27) ⭐️ 7.0/10
28. [Pocket FM 借助人工智能实现音频内容规模化生产](#item-28) ⭐️ 7.0/10
29. [人工智能代理增加公共服务需求](#item-29) ⭐️ 7.0/10
30. [Listen Labs 在与 Salesforce 洽谈期间放弃据报 15 亿美元的 C 轮融资](#item-30) ⭐️ 7.0/10
31. [保罗·克里斯蒂亚诺加入 OpenAI 基金会董事会](#item-31) ⭐️ 7.0/10
32. [Datasette 发布经 AI 辅助审计的安全版本](#item-32) ⭐️ 7.0/10
33. [Tobi Lütke 谈人工智能代理与未来工作](#item-33) ⭐️ 7.0/10
34. [苹果发布首款折叠式 iPhone](#item-34) ⭐️ 7.0/10
35. [人工智能黑客事件加剧对自主系统的担忧](#item-35) ⭐️ 7.0/10
36. [ACE Robotics 与南洋理工大学开源 Puffin-World](#item-36) ⭐️ 7.0/10
37. [宇树发布 UnifoLM-WLA-1.0 人形机器人基础模型页面](#item-37) ⭐️ 7.0/10
38. [用 Gradio Workflow 重建 AUTOMATIC1111](#item-38) ⭐️ 6.0/10
39. [OpenAI 因 Astra 需求暂停专业版注册](#item-39) ⭐️ 6.0/10
40. [泰勒·科文汇总机器人、AI 安全与核风险相关链接](#item-40) ⭐️ 6.0/10
41. [开源项目利用声学信号探测无人机](#item-41) ⭐️ 6.0/10
42. [荧光视频实现犬血微丝蚴的诊所内自动检测](#item-42) ⭐️ 6.0/10
43. [SOC Prime 报告两个 Windows 零日漏洞](#item-43) ⭐️ 6.0/10
44. [LTM 联手 IBM 与 Red Hat 推进 Lightwell 修复](#item-44) ⭐️ 6.0/10
45. [GitHub 扩大高级安全功能试用范围](#item-45) ⭐️ 5.0/10
46. [Herdr：面向人工智能编程代理的开源运行时](#item-46) ⭐️ 5.0/10
47. [GitHub 报告八月发生五起事件](#item-47) ⭐️ 5.0/10
48. [Percona 与 Coroot 合作推进开源数据库可观测性](#item-48) ⭐️ ?/10

---

<a id="item-15" class="hz-item-anchor" data-hz-url="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/" data-hz-title="Rust 成为微软的一级语言" data-hz-tags="Rust,Microsoft,systems programming,memory safety,C++ interoperability" data-hz-section="other"></a>
## [Rust 成为微软的一级语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

微软如今将 Rust 视为一级语言，进一步巩固了其作为成熟系统编程选项的地位，可用于新项目开发、互操作以及大规模替换不安全的遗留代码。

hackernews · mmastrac · 9月10日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**标签**: `#Rust`, `#Microsoft`, `#systems programming`, `#memory safety`, `#C++ interoperability`

---

<a id="item-16" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/10/calif-research/" data-hz-title="Calif Research声称人工智能辅助开发微信零点击蠕虫" data-hz-tags="AI security,zero-click exploits,mobile security,remote code execution,cybersecurity research" data-hz-section="other"></a>
## [Calif Research 声称人工智能辅助开发微信零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 表示，他们开发了 WeWorm，这是一种可通过微信通话在 iOS 和 Android 设备之间传播的零点击蠕虫。该团队声称，他们约用两天找到漏洞并编写远程代码执行漏洞利用程序，又用一周时间构建了蠕虫。 如果这一说法得到独立证实，这意味着恶意来电可能在受害者无需接听或操作设备的情况下入侵设备。这也表明，人工智能辅助可能大幅缩短开发复杂移动端漏洞利用程序和蠕虫所需的时间，并减少所需团队规模。 研究人员称，即使受害者接听电话，漏洞利用仍会成功，而且受害者听不到任何声音；该攻击据称同时适用于 iOS 和 Android。现有材料只是一份简短公告，没有提供独立技术验证、详细漏洞利用步骤或受影响微信版本的证据。

rss · Simon Willison · 9月10日 00:56

**背景**: 零点击漏洞利用是指不需要受害者点击链接、打开文件、接听电话或以其他方式操作设备的攻击。蠕虫是一类能够从一台设备传播到另一台设备的恶意软件，而远程代码执行意味着攻击者可以让目标设备在远程运行代码。在本案例中，Calif Research 称传播渠道是微信通话，目标平台是 iOS 和 Android。

**标签**: `#AI security`, `#zero-click exploits`, `#mobile security`, `#remote code execution`, `#cybersecurity research`

---

<a id="item-17" class="hz-item-anchor" data-hz-url="https://shopify.engineering/back-to-native" data-hz-title="Shopify 正从 React Native 转回 Swift 和 Kotlin" data-hz-tags="React Native,mobile development,Swift,Kotlin,software architecture" data-hz-section="other"></a>
## [Shopify 正从 React Native 转回 Swift 和 Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 正在用原生 Swift 和 Kotlin 替代 React Native，引发了关于移动端性能、开发效率、AI 辅助重写以及跨平台权衡的广泛讨论。

hackernews · fnthawar2 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**标签**: `#React Native`, `#mobile development`, `#Swift`, `#Kotlin`, `#software architecture`

---

<a id="item-18" class="hz-item-anchor" data-hz-url="https://developers.openai.com/api/docs/guides/agents-api/overview" data-hz-title="OpenAI推出托管式Agents API" data-hz-tags="AI agents,OpenAI,developer APIs,sandboxing,agent infrastructure" data-hz-section="other"></a>
## [OpenAI 推出托管式 Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

OpenAI 推出了基于 Codex harness 构建和运行智能体的托管式 Agents API。OpenAI 负责会话管理、编排、上下文压缩和恢复，开发者则提供工具并选择执行环境。 该 API 通过抽象执行、可靠性和沙箱管理等复杂工作，可能降低将智能体部署到生产环境的工程门槛。它还允许开发者使用 OpenAI 托管或自行托管的计算环境，可能改变智能体基础设施市场并减少对专用平台的依赖。 智能体可以在沙箱中执行代码、编辑文件、连接 MCP 服务器并生成成果物，而应用仍需负责提供工具和选择执行环境。社区指出，自行托管沙箱以及普通虚拟机都可能提升可移植性，但开发者仍需处理状态持久化、兼容性和运行可靠性问题。

hackernews · aquir · 9月10日 19:43 · [社区讨论](https://news.ycombinator.com/item?id=49649213)

**背景**: AI 智能体是一种能够使用工具并执行多步骤任务的软件系统，而不只是生成单次回复。在这种设计中，harness 负责智能体的执行循环和协调，沙箱则提供用于运行命令、处理文件、使用服务和生成成果物的隔离环境。将 harness 与计算环境分离后，开发者可以在托管基础设施和自行运营的环境之间进行选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API</a></li>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API - OpenAI</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为，该 API 为安全运行大量智能体以及将智能体能力集成到产品中提供了实用抽象，但也在讨论 harness、工具和持久化状态之间应如何划分边界。他们指出，自行托管和使用虚拟机可能减少供应商锁定，但也有人警告，这项服务可能冲击围绕类似智能体基础设施模式建立的初创公司。

**标签**: `#AI agents`, `#OpenAI`, `#developer APIs`, `#sandboxing`, `#agent infrastructure`

---

<a id="item-19" class="hz-item-anchor" data-hz-url="https://lucumr.pocoo.org/2026/9/7/astra-why/" data-hz-title="Astra 编程版：我们为什么又要这么做？" data-hz-tags="AI coding agents,software maintainability,reinforcement learning,code quality,developer tools" data-hz-section="other"></a>
## [Astra 编程版：我们为什么又要这么做？](https://lucumr.pocoo.org/2026/9/7/astra-why/) ⭐️ 8.0/10

文章认为，Astra 更强大的自主编程能力可能会以较差的实现质量为代价，使生成的代码越来越难以维护，无论对人类还是其他智能体而言都是如此。

hackernews · manojbajaj95 · 9月11日 06:23 · [社区讨论](https://news.ycombinator.com/item?id=49654229)

**标签**: `#AI coding agents`, `#software maintainability`, `#reinforcement learning`, `#code quality`, `#developer tools`

---

<a id="item-20" class="hz-item-anchor" data-hz-url="https://mathstodon.xyz/@andreasthom/117240535270608201" data-hz-title="研究人员质疑 OpenAI 是否值得托付未发表数学成果" data-hz-tags="AI ethics,Academic research,Mathematics,Data privacy,Research attribution" data-hz-section="other"></a>
## [研究人员质疑 OpenAI 是否值得托付未发表数学成果](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

研究人员和评论人士正在讨论，OpenAI 是否可能从用户与其模型交流时分享的未发表数学想法中获益，却没有给予充分署名或保持保密。争议集中在相关指控，以及使用人工智能系统进行合作与后来发表相关成果之间的潜在冲突。 这一问题可能影响数学家和其他研究人员是否愿意向人工智能公司分享未发表的想法，尤其是在这些公司可能利用用户交流改进模型的情况下。它还引发了关于署名、保密、数据治理以及人工智能辅助研究规范的更广泛讨论。 现有讨论并未证明 OpenAI 抄袭了某个特定证明，也未证明其模型记住了被指称的材料。评论者区分了训练数据可能带来的帮助、通过强化学习和计算发现的技术，以及模型在直接合作中接触到的想法；还有评论者质疑，在训练数据可能包含相关数学材料的担忧出现后，大规模生成工作启动的时间安排。

hackernews · pred_ · 9月10日 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**背景**: 未发表的数学工作可能包含研究人员尚未公开或正式署名的想法。当研究人员把这些想法分享给人工智能模型时，从研究人员的角度看，这次交流可能类似于合作；但公司可能依据模型训练、产品使用或数据使用政策处理这些交流。这就造成了关于谁应当获得认可，以及如何处理保密研究贡献的不确定性。

**社区讨论**: 评论区并未形成确定结论，而是存在明显分歧。一些参与者认为，如果把 OpenAI 视为人类合作者，其行为可能不符合伦理，并强调署名和保密；另一些人则认为，模型训练、强化学习和大规模计算可能独立产生相关技术。还有评论者对 OpenAI 的行动时机表示怀疑，并不确定其在开放问题上的进展究竟源于真实能力，还是源于近期吸收的信息。

**标签**: `#AI ethics`, `#Academic research`, `#Mathematics`, `#Data privacy`, `#Research attribution`

---

<a id="item-21" class="hz-item-anchor" data-hz-url="https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md" data-hz-title="Forgejo 16.0.3及更早版本存在严重远程代码执行漏洞" data-hz-tags="security,remote-code-execution,Forgejo,Git,vulnerability-management" data-hz-section="other"></a>
## [Forgejo 16.0.3 及更早版本存在严重远程代码执行漏洞](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 8.0/10

Forgejo 16.0.3 及更早版本在处理恶意仓库模板中 .forgejo/template 目录下文件的变量展开时存在缺陷，攻击者可借此实现远程代码执行。Forgejo 16.0.4 修复了该漏洞，相关维护分支也发布了 15.0.8 版本。 恶意仓库模板可能把普通的仓库创建流程变成服务器上的代码执行，从而威胁托管源代码和相关服务的机密性与完整性。只要系统允许不受信任的用户创建或使用模板，管理员就应优先升级到已修复版本。 存在漏洞的流程会先克隆模板仓库、移除 .git 目录、对指定模板文件执行变量展开，随后初始化新的 Git 仓库；这些操作的顺序使变量展开能够干扰仓库初始化。社区成员质疑在变量展开后再删除 .git 是否足够稳健，并建议对 Git 操作进行沙箱隔离，以降低整类攻击的影响范围。

hackernews · weierstass · 9月10日 15:57 · [社区讨论](https://news.ycombinator.com/item?id=49645907)

**背景**: Forgejo 是一个 Git 托管平台，可以根据已有模板仓库创建新的仓库。在此过程中，.forgejo/template 目录中的文件可能包含变量，Forgejo 会在初始化新仓库前展开这些变量。远程代码执行意味着攻击者能够诱使服务器运行其控制的指令，而不只是读取或修改仓库数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rapid7.com/db/vulnerabilities/cve-2026-89094/">CVE-2026-89094: Forgejo: Forgejo before 16.0.4 allows remote ...</a></li>
<li><a href="https://noise.getoto.net/2026/09/10/forgejo-16-0-4-and-15-0-8-address-critical-security-vulnerability/">Forgejo 16.0.4 and 15.0.8 address critical security vulnerability | Noise</a></li>

</ul>
</details>

**社区讨论**: 社区讨论主要集中在模板展开形成的攻击路径以及修复是否足够稳健，有成员建议对 Git 操作进行沙箱隔离，以解决更广泛的一类问题。另一位成员表示 Gitea 已防护这两个问题，同时提醒安全事件可能发生在任何项目上，不应因此打击漏洞报告行为。

**标签**: `#security`, `#remote-code-execution`, `#Forgejo`, `#Git`, `#vulnerability-management`

---

<a id="item-22" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/10/trynix/" data-hz-title="在浏览器中运行任意 Nix 软件包" data-hz-tags="Nix,WebAssembly,QEMU,Reproducible Builds,Developer Tools" data-hz-section="other"></a>
## [在浏览器中运行任意 Nix 软件包](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

try nix.dev 通过 WebAssembly 和 qemu-wasm 在浏览器中完全运行 x86_64 Linux 虚拟机，用户可以启动过去约 13 年中的任意 Nix 软件包。它的 trynix-preview GitHub Action 还能在拉取请求中评论一个链接，让用户直接在浏览器中启动该拉取请求的构建结果。 这让用户无需安装 Nix、配置本地虚拟机或运行服务器，就能直接访问可复现的历史 Linux 环境。拉取请求预览还可能简化构建审查流程，把 GitHub 中的构建产物转化为可交互的浏览器会话。 软件包环境可以通过网址直接访问，例如一个链接就能启动 2017 年的 Python 3.6.2；该系统运行的是 x86_64 Linux 虚拟机，而不是把软件包直接作为浏览器原生代码运行。预览工作流被描述为除浏览器启动过程外无需服务器，但本文没有说明其实际性能和软件包兼容范围。

rss · Simon Willison · 9月10日 23:44

**背景**: Nix 是一种面向可复现环境的软件包管理和系统配置技术，因此同一个软件包定义可以在不同时间和机器上获得一致的结果。WebAssembly 允许编译后的软件在浏览器中运行，而 QEMU 是能够提供完整 Linux 机器环境的虚拟化和模拟工具。在这个项目中，qemu-wasm 将这些能力结合起来，在浏览器中启动 x86_64 Linux 虚拟机。

**标签**: `#Nix`, `#WebAssembly`, `#QEMU`, `#Reproducible Builds`, `#Developer Tools`

---

<a id="item-23" class="hz-item-anchor" data-hz-url="https://www.quantamagazine.org/the-four-color-theorem-gets-a-rare-new-proof-20260910/" data-hz-title="四色定理获得罕见的新证明" data-hz-tags="Graph Theory,Mathematics,Formal Proofs,Computer-Assisted Mathematics" data-hz-section="other"></a>
## [四色定理获得罕见的新证明](https://www.quantamagazine.org/the-four-color-theorem-gets-a-rare-new-proof-20260910/) ⭐️ 8.0/10

数学家提出了四色定理的一种新证明，重新审视了这一曾在 1976 年借助计算机、并引发争议的重要成果。这项工作为图的结构和行为提供了新的认识。 新证明有助于澄清定理背后的数学结构，并加深人们对图论的理解。它还重新审视了如何让计算机辅助论证更加透明并获得数学界认可，不过其直接的实际影响可能较为有限。 四色定理指出，任何地图都可以使用不超过四种颜色进行着色，并确保相邻区域颜色不同；这一问题也可以表述为平面图着色问题。1976 年阿佩尔和哈肯的证明将问题归结为检查 1936 个可约构形，后来这一数量降至 1476 个，并由计算机完成检查。

rss · Quanta Magazine · 9月10日 14:27

**背景**: 在图论中，可以用平面图表示地图，其中的顶点和边编码各个区域之间的关系。合法的图着色要求相邻区域或顶点使用不同颜色。这个定理在一个多世纪里一直未被证明，直到 1976 年阿佩尔和哈肯提出计算机辅助证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Four_color_theorem">Four color theorem - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/0905.3713">A formal proof of the four color theorem - arXiv.org</a></li>
<li><a href="https://www.cs.cornell.edu/courses/JavaAndDS/files/Gonthier4ColorCoq.pdf">Formal Proof—The Four-Color Theorem</a></li>

</ul>
</details>

**标签**: `#Graph Theory`, `#Mathematics`, `#Formal Proofs`, `#Computer-Assisted Mathematics`

---

<a id="item-24" class="hz-item-anchor" data-hz-url="https://marginalrevolution.com/marginalrevolution/2026/09/economic-scenarios-for-transformative-ai.html?utm_source=rss&utm_medium=rss&utm_campaign=economic-scenarios-for-transformative-ai" data-hz-title="变革性人工智能的经济情景框架" data-hz-tags="Transformative AI,AI Economics,AI Policy,Labor Markets,Economic Forecasting" data-hz-section="other"></a>
## [变革性人工智能的经济情景框架](https://marginalrevolution.com/marginalrevolution/2026/09/economic-scenarios-for-transformative-ai.html?utm_source=rss&utm_medium=rss&utm_campaign=economic-scenarios-for-transformative-ai) ⭐️ 8.0/10

Anton Korinek、Charles I. Jones、Szymon Sacher、Tess Cotter 和 Peter McCrory 提出了一套评估人工智能在 2026 年至 2030 年间经济影响的框架。相关情景从温和影响延伸到人工智能在 2030 年前完成当今近一半认知工作的极端情景。 这套框架为政策制定者和研究人员提供了一种系统方法，用于分析变革性人工智能可能如何影响经济增长、失业、劳动力市场和公共政策。在温和变化情景下，到 2030 年人工智能使国内生产总值增速提高不到 0.5 个百分点，同时使失业率上升 0.1 个百分点。 这项分析采用情景研究而不是单一数值预测，对比了温和变化情景和极具变革性的人工智能情景。文章将作者的方法概括为审慎、理性、科学，并且大体上具有动态一致性，但现有摘录没有提供该框架的完整假设或方法细节。

rss · Marginal Revolution · 9月10日 08:39

**背景**: 这里的变革性人工智能，是指其影响足以重塑经济活动的人工智能，包括承担原本由人类完成的工作。经济情景有助于研究人员考察多种可能路径，而不是把不确定的技术发展视为固定预测。讨论聚焦于 2026 年至 2030 年，并探讨机器接近或超过人类认知能力时可能出现的经济结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://marginalrevolution.com/marginalrevolution/2026/09/economic-scenarios-for-transformative-ai.html">Economic Scenarios for Transformative AI - Marginal REVOLUTION</a></li>
<li><a href="https://www.anthropic.com/institute/econ-scenarios">Scenarios for our Economic Future \ Anthropic</a></li>
<li><a href="https://www.nber.org/news/economics-transformative-ai">The Economics of Transformative AI | NBER</a></li>

</ul>
</details>

**标签**: `#Transformative AI`, `#AI Economics`, `#AI Policy`, `#Labor Markets`, `#Economic Forecasting`

---

<a id="item-25" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMilgFBVV95cUxPX3dYMlgyZlZMdzRrOWd4a2t6ZEFKYlctaXZaeHZyRFJIclVTalplaDVkb1Zybm92RFVvWWlqV1VyOTdDaUx4RXVXWXMwNWpYeF81ZU4zSUlDN3lhb3lzZG5Qb0tmbkRjdXJYcExuSHpEWmJ4ZklkT0lKNFI1SjR6bEt1ejVIZV9ia3UwZ05rT2tIcmw3UlE?oc=5" data-hz-title="IBM与NASA发布开放月球基础模型和SomBench数据集" data-hz-tags="AI/ML,Foundation Models,NASA,Open Source,Planetary Science" data-hz-section="other"></a>
## [IBM 与 NASA 发布开放月球基础模型和 SomBench 数据集](https://news.google.com/rss/articles/CBMilgFBVV95cUxPX3dYMlgyZlZMdzRrOWd4a2t6ZEFKYlctaXZaeHZyRFJIclVTalplaDVkb1Zybm92RFVvWWlqV1VyOTdDaUx4RXVXWXMwNWpYeF81ZU4zSUlDN3lhb3lzZG5Qb0tmbkRjdXJYcExuSHpEWmJ4ZklkT0lKNFI1SjR6bEt1ejVIZV9ia3UwZ05rT2tIcmw3UlE?oc=5) ⭐️ 8.0/10

2026 年 9 月 10 日，IBM 与 NASA 发布了开放源代码的 NASA-IBM 月球基础模型，这是一种面向月球遥感的多模态、多分辨率模型，并同步发布了 SomBench 数据集。SomBench 包含约 200 万个配准月球图块组，覆盖 11 种数据模态和两种空间尺度。 此次发布为研究人员提供了可公开使用的模型和数据集，有望提升对大规模月球观测数据的分析能力，并改进冰和陨石坑等地表特征的绘制。它还可能支持月球科学研究以及包括阿尔忒弥斯任务在内的未来月球探测规划。 该模型整合了来自多种数据模态、观测角度和空间尺度的观测结果，并使用在 SomBench 上从头训练的 ViT-B 编码器—解码器。由于它专注于月球遥感，其性能和适用性可能取决于数据集的覆盖范围、配准质量以及所包含的数据模态。

google_news · Unite.AI · 9月10日 12:17

**背景**: 基础模型是在广泛数据上训练、并可适配多种下游任务的模型。多模态模型会结合不同类型的观测数据，多分辨率模型则会在不止一种空间尺度上处理信息。在这一项目中，月球遥感是指利用仪器观测结果研究和绘制月球表面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://science.nasa.gov/science-research/artificial-intelligence-lunar-foundation-model/">NASA , IBM Launch AI Foundation Model for Lunar ... - NASA Science</a></li>
<li><a href="https://research.ibm.com/blog/nasa-ibm-lunar-foundation-model">Introducing IBM and NASA ’s new foundation model ... - IBM Research</a></li>
<li><a href="https://huggingface.co/nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model">nasa - ibm -ai4science/ NASA - IBM -Lunar-Foundation-Model · Hugging...</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#Foundation Models`, `#NASA`, `#Open Source`, `#Planetary Science`

---

<a id="item-26" class="hz-item-anchor" data-hz-url="https://newsletter.semianalysis.com/p/what-is-so-hard-about-behind-the" data-hz-title="数据中心为何难以实现表后供电" data-hz-tags="Datacenter Infrastructure,Energy Systems,AI Infrastructure,Power Generation,Grid Management" data-hz-section="other"></a>
## [数据中心为何难以实现表后供电](https://newsletter.semianalysis.com/p/what-is-so-hard-about-behind-the) ⭐️ 7.0/10

文章分析了为什么为数据中心提供表后供电远比最初看起来复杂。它指出，这项工作不仅是安装现场发电设备，还涉及技术、财务和运营方面的考量。 快速扩张的人工智能基础设施正在提高对可靠电力的需求，而电网限制使现场供电或与电网互补的电源更具吸引力。此类系统的部署难度可能影响新数据中心容量的建设和运营速度。 表后供电是在公用事业电表的用户侧直接为设施供电，可能减少对电网的依赖，但也会带来额外的技术、财务和运营要求。现有材料没有具体说明第一部分讨论了哪些发电技术、项目经济性或运营模式。

rss · Semianalysis（半导体·AI 风向标） · 9月10日 14:28

**背景**: 表后发电是指在现场生产电力，并由设施直接使用，而不是完全从电网取电。数据中心之所以越来越多地讨论这种方式，是因为大型新增负荷可能面临漫长的电网接入排队时间和当地电网限制。它既可以补充电网，也可以在永久接入建成前充当过渡电源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.williams.com/2026/03/17/powering-data-centers-behind-the-meter-power-explained/">Powering data centers: behind-the-meter power, explained</a></li>
<li><a href="https://atkenergygroup.com/blog/behind-the-meter-generation-data-centers/">Behind-the-Meter Generation for Data Centers in 2026 ...</a></li>
<li><a href="https://www.datacenterknowledge.com/energy-power-supply/why-data-centers-produce-their-own-power">Why Data Centers Are Turning to Behind-the-Meter Power</a></li>

</ul>
</details>

**标签**: `#Datacenter Infrastructure`, `#Energy Systems`, `#AI Infrastructure`, `#Power Generation`, `#Grid Management`

---

<a id="item-27" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/09/10/anthropic-details-distillation-campaigns-from-alibaba-moonshot-ai-and-deepseek/" data-hz-title="Anthropic称人工智能模型蒸馏活动加剧" data-hz-tags="AI security,model distillation,intellectual property,AI geopolitics" data-hz-section="other"></a>
## [Anthropic 称人工智能模型蒸馏活动加剧](https://techcrunch.com/2026/09/10/anthropic-details-distillation-campaigns-from-alibaba-moonshot-ai-and-deepseek/) ⭐️ 7.0/10

Anthropic 称，阿里巴巴、月之暗面和 DeepSeek 持续对其人工智能模型发起蒸馏攻击，相关活动近几个月有所升级。该报告将这些活动与人工智能行业竞争加剧联系起来。 这些指控引发了人们对模型知识产权、已部署人工智能服务安全性，以及提取领先系统能力可能造成的竞争影响的担忧。相关事件还可能影响人工智能治理、出口管制和国家间技术竞争的讨论。 模型蒸馏是将较大型教师模型中的有用知识转移给较小学生模型的过程，而蒸馏攻击则试图从外部可访问的模型中提取其能力。根据目前提供的摘要，Anthropic 的报告缺少较多支持性细节，因此这些指控应与经过独立验证的事实区分开来。

rss · TechCrunch AI · 9月10日 20:57

**背景**: 在通常的模型蒸馏中，较小的模型学习复现较大模型的重要能力，从而提高部署效率。在攻击场景下，攻击者可能通过反复与托管语言模型交互，在无法接触原始训练过程的情况下近似其行为和能力。这类模型提取行为可能带来知识产权和安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://labelbox.com/guides/model-distillation/">What is Model Distillation ?</a></li>

</ul>
</details>

**标签**: `#AI security`, `#model distillation`, `#intellectual property`, `#AI geopolitics`

---

<a id="item-28" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/09/10/indias-pocket-fm-doubles-revenue-run-rate-to-500m-as-ai-powers-93-of-audio-content/" data-hz-title="Pocket FM借助人工智能实现音频内容规模化生产" data-hz-tags="Generative AI,Audio Content,Media Technology,AI Economics,Startups" data-hz-section="other"></a>
## [Pocket FM 借助人工智能实现音频内容规模化生产](https://techcrunch.com/2026/09/10/indias-pocket-fm-doubles-revenue-run-rate-to-500m-as-ai-powers-93-of-audio-content/) ⭐️ 7.0/10

据报道，Pocket FM 的收入年化运行率翻倍至 5 亿美元，同时使用人工智能生成大部分新音频内容。所给标题称其音频内容中 93%由人工智能制作，但配套内容称其新内容中 99%由人工智能制作。 这一案例表明，人工智能辅助制作可能大幅降低连续音频内容的成本，并支持大规模商业化内容业务。如果这些由公司披露的数据具有代表性，可能会影响媒体经济模式，并加快合成音频工作流程的采用。 Pocket FM 称，人工智能使内容制作成本降低了约 80 倍，但所提供材料没有说明所用模型、人工审核流程、质量控制方式或收入计算方法。因此，93%和 99%这两个相互矛盾的数据应谨慎看待，不能视为经过精确验证的指标。

rss · TechCrunch AI · 9月10日 17:45

**背景**: 文本转语音系统使用合成声音将书面文字转换为口语音频，当前的相关服务可以支持多种语言和应用接口。更先进的生成式音频工作流程能够连接生成旁白、添加效果等多个自动化步骤，从而提升音频制作的规模化能力和一致性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://elevenlabs.io/text-to-speech">Free Text To Speech Online with Lifelike AI Voices</a></li>
<li><a href="https://arxiv.org/html/2505.04885v1">A Multi-Agent AI Framework for Immersive Audiobook Production ...</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#Audio Content`, `#Media Technology`, `#AI Economics`, `#Startups`

---

<a id="item-29" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/09/10/ai-agents-are-flooding-public-services-with-new-requests/" data-hz-title="人工智能代理增加公共服务需求" data-hz-tags="AI agents,Public services,Automation,AI policy,Systems impact" data-hz-section="other"></a>
## [人工智能代理增加公共服务需求](https://techcrunch.com/2026/09/10/ai-agents-are-flooding-public-services-with-new-requests/) ⭐️ 7.0/10

人工智能代理正在引发公共服务请求激增，其中包括有资格获得相关服务的人提出的申请。一名研究人员告诉 TechCrunch，他们发现的绝大多数案例都是符合条件的人申请自己有权获得的服务或福利。 即使这些请求都合理合法，自动化代理也可能提高申请数量和速度，从而给行政系统带来新的压力。这表明人工智能的部署可能影响公共部门的承载能力，以及资格审核和行政流程的运行方式。 现有报道没有提供请求增长的具体规模、涉及的公共服务类型，也没有说明相关机构如何应对。需要注意的是，这种增长不应自动被解读为普遍存在欺诈或滥用，因为据报道，大多数被发现的申请人确实有资格获得相关服务。

rss · TechCrunch AI · 9月10日 14:53

**标签**: `#AI agents`, `#Public services`, `#Automation`, `#AI policy`, `#Systems impact`

---

<a id="item-30" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/09/09/ai-research-startup-listen-labs-scrubbed-a-1-5b-funding-round-for-salesforce-talks/" data-hz-title="Listen Labs 在与 Salesforce 洽谈期间放弃据报15亿美元的 C 轮融资" data-hz-tags="AI startups,venture capital,Salesforce,startup acquisitions,AI industry" data-hz-section="other"></a>
## [Listen Labs 在与 Salesforce 洽谈期间放弃据报 15 亿美元的 C 轮融资](https://techcrunch.com/2026/09/09/ai-research-startup-listen-labs-scrubbed-a-1-5b-funding-round-for-salesforce-talks/) ⭐️ 7.0/10

据报道，Listen Labs 在与 Salesforce 洽谈期间，放弃了与 Menlo Ventures 签署的一份 15 亿美元 C 轮融资条款清单。目前公开信息尚未确认这些洽谈是否会促成收购或其他交易。 放弃如此大规模的融资承诺，可能意味着战略交易对 Listen Labs 的吸引力高于保持独立融资，但最终结果仍不确定。这也凸显出大型科技公司可能如何影响后期 AI 初创公司的融资决策。 条款清单会列出拟议投资的主要商业条件，通常是后续法律协议的基础，但并不一定保证融资最终完成。报道将 Menlo Ventures 列为投资方，并指出 Listen Labs 正与 Salesforce 进行另一项洽谈，但没有披露更多具体条款。

rss · TechCrunch AI · 9月10日 00:00

**背景**: 在风险投资中，条款清单是一份概述拟议投资关键条件的初步文件。C 轮融资属于较后期的融资轮次，通常面向已经完成早期融资、希望继续扩张的初创公司。条款清单通常先于正式投资文件和后续谈判。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Term_sheet">Term sheet - Wikipedia</a></li>
<li><a href="https://www.wallstreetprep.com/knowledge/the-ultimate-guide-to-the-vc-term-sheet-term-sheet-template/">Venture Capital Term Sheet (VC) | Format + PDF Template</a></li>
<li><a href="https://www.svb.com/startup-insights/vc-relations/venture-capital-term-sheets/">Understanding venture capital term sheets - SVB Series C Funding: What It Is, How It Works & 3 Examples - Failory VC Term Sheet Template | Series A Venture Capital What is a VC Term Sheet? Complete Guide for Founders Raising Venture Capital with Series A, B, & C | Embroker</a></li>

</ul>
</details>

**标签**: `#AI startups`, `#venture capital`, `#Salesforce`, `#startup acquisitions`, `#AI industry`

---

<a id="item-31" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/09/09/openai-adds-a-prominent-ai-doomer-to-its-board-of-directors/" data-hz-title="保罗·克里斯蒂亚诺加入 OpenAI 基金会董事会" data-hz-tags="OpenAI,AI safety,AI alignment,Governance" data-hz-section="other"></a>
## [保罗·克里斯蒂亚诺加入 OpenAI 基金会董事会](https://techcrunch.com/2026/09/09/openai-adds-a-prominent-ai-doomer-to-its-board-of-directors/) ⭐️ 7.0/10

OpenAI 已任命人工智能对齐研究员保罗·克里斯蒂亚诺加入 OpenAI 基金会董事会。他还将加入该基金会的安全与保障委员会。 克里斯蒂亚诺是研究如何让先进人工智能系统符合人类利益的重要研究者，因此他的任命可能影响基金会对人工智能安全和长期风险的处理方式。这也意味着对齐领域的专业经验进入了监督 OpenAI Group PBC 的治理结构。 此次任命涉及非营利性的 OpenAI 基金会，而不是直接加入 OpenAI 运营公司的董事会。现有信息没有说明克里斯蒂亚诺的任命将如何改变 OpenAI 的政策、研究重点或安全实践。

rss · TechCrunch AI · 9月9日 22:25

**背景**: 人工智能对齐是人工智能安全的一个分支，重点是让人工智能系统遵循人类的目标、偏好或伦理原则。OpenAI 基金会是控制 OpenAI Group PBC 的非营利实体，因此其治理机构能够参与监督整个组织。克里斯蒂亚诺长期参与人工智能对齐领域的挑战和解决方案研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/paul-christiano-joins-openai-foundation-board/">Paul Christiano joins OpenAI Foundation Board</a></li>
<li><a href="https://openai.com/our-structure/">Our structure - OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI safety`, `#AI alignment`, `#Governance`

---

<a id="item-32" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/11/datasette-security/" data-hz-title="Datasette发布经AI辅助审计的安全版本" data-hz-tags="Datasette,security,vulnerability fixes,AI-assisted auditing,SQLite" data-hz-section="other"></a>
## [Datasette 发布经 AI 辅助审计的安全版本](https://simonwillison.net/2026/Sep/11/datasette-security/) ⭐️ 7.0/10

Datasette 于 2026 年 9 月 11 日发布了安全补丁版本 1.0a39 和 0.65.4，分别面向当前的 alpha 系列和稳定的 0.65.x 系列。这些版本修复了在人工主导、Claude Fable 5.1、GPT-5.6 和 GPT-6 Astra 辅助的审计中发现的隐蔽漏洞。 公开访问的 Datasette 实例运营者应当应用这些更新，尤其是那些在同一部署中同时包含公开表和私有表的实例。这项工作也表明，前沿 AI 模型可以参与安全审计，但人工复核和测试仍然是验证修复的重要环节。 Sevban Dönmez 报告问题后，Simon Willison 和 Alex Garcia 在共享的私有代码仓库中花费近一周时间审查并实现修复。对于大多数问题，一人编写突出问题的自动化测试，另一人实现修复，因此每项变更都经过两名人工作者以及使用不同模型的编码代理检查。

rss · Simon Willison · 9月11日 03:27

**背景**: Datasette 可用于通过可访问网络的实例发布和提供 SQLite 数据。有些部署会使用权限系统，在同一个数据库中同时提供公开表和私有表，因此访问控制漏洞尤其敏感。Datasette 此前的安全版本曾修复影响这种公开表与私有表混合配置的 SQL 注入路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/blog/2026/september-security-releases/">Datasette 1 . 0 a 39 and 0 . 65 . 4 security releases - Datasette Blog</a></li>
<li><a href="https://simonwillison.net/2026/Aug/6/datasette/">Release: datasette 1.0a38 - simonwillison.net</a></li>
<li><a href="https://jasonvsthenoise.com/repowatch/2026-08-07-datasette-private-table-sql-injection/">Datasette closes a SQL injection path into private tables</a></li>

</ul>
</details>

**标签**: `#Datasette`, `#security`, `#vulnerability fixes`, `#AI-assisted auditing`, `#SQLite`

---

<a id="item-33" class="hz-item-anchor" data-hz-url="https://fs.blog/knowledge-project-podcast/tobi-lutke-3/" data-hz-title="Tobi Lütke谈人工智能代理与未来工作" data-hz-tags="AI agents,Future of work,Decision-making,AI strategy,Leadership" data-hz-section="other"></a>
## [Tobi Lütke 谈人工智能代理与未来工作](https://fs.blog/knowledge-project-podcast/tobi-lutke-3/) ⭐️ 7.0/10

Shopify 创始人兼首席执行官 Tobi Lütke 讨论了如何使用人工智能委员会审视艰难决策，并解释了为什么随着人工智能能力提升，品味、判断力和责任感可能变得更加重要。访谈还探讨了 Shopify 开发的人工智能代理 River 及其在公司内部的应用。 这场讨论从领导者视角说明了如何将人工智能代理融入高风险决策，而不仅仅把它们当作提高效率的工具。它表明，随着高能力人工智能日益普及，组织之间的竞争可能越来越取决于人的判断力、标准和问责能力。 Lütke 介绍了一个用于审视最艰难决策的人工智能委员会；据报道，Shopify 的 River 运行在公司 Slack 中，可以读写代码、运行测试、创建拉取请求、查询数据并检查生产环境跟踪信息。这些例子表明，人工智能代理既能辅助战略思考，也能执行具体工程工作，但不能取代人的责任。

rss · Farnam Street · 9月10日 09:50

**背景**: 人工智能代理是一种能够执行多步骤任务的软件系统，通常可以使用代码仓库、测试环境或数据系统等工具。在这一语境中，人工智能委员会是指利用多个人工智能视角或模型来质疑和审视一项决策。River 是 Shopify 内部的人工智能协作者，设计目标是通过 Slack 与员工互动，并在公司的工程环境中工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fs.blog/knowledge-project-podcast/tobi-lutke-3/">Tobi Lütke: AI Agents, Better Decisions, and the Future of Work</a></li>
<li><a href="https://shopify.engineering/river-vulnerability-remediation">How River takes security work from a fix to merge (2026) - Shopify</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Future of work`, `#Decision-making`, `#AI strategy`, `#Leadership`

---

<a id="item-34" class="hz-item-anchor" data-hz-url="https://www.bbc.co.uk/news/articles/clyjd1jnd03o?at_medium=RSS&at_campaign=rss" data-hz-title="苹果发布首款折叠式 iPhone" data-hz-tags="Apple,iPhone,Foldable Devices,Consumer Technology,Product Launch" data-hz-section="other"></a>
## [苹果发布首款折叠式 iPhone](https://www.bbc.co.uk/news/articles/clyjd1jnd03o?at_medium=RSS&at_campaign=rss) ⭐️ 7.0/10

苹果在一场发布会上推出了首款折叠式 iPhone，售价为 1999 英镑。这是该公司近 20 年来对 iPhone 进行的首次重大设计变革。 这款产品让苹果进入高端折叠手机市场，可能影响普通消费者对折叠设备的看法。其高昂售价也将检验苹果能否说服消费者为这种新形态支付更高价格。 现有信息除了 1999 英镑的售价和折叠设计外，没有提供更多技术规格。折叠手机通常依靠柔性 OLED 屏幕和精密铰链，但耐用性、铰链磨损、屏幕折痕以及成本仍是重要限制。

rss · BBC World News · 9月10日 09:32

**背景**: 折叠手机使用柔性屏幕和铰链，使一台设备能够在紧凑的手机形态与更大屏幕形态之间转换。柔性 OLED 面板可以弯曲，但其较柔软的结构和反复折叠可能导致明显折痕并带来耐用性问题。因此，铰链是影响设备可靠性的关键部件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scienceabc.com/innovation/science-foldable-phones-next-mobile-frontier">How Foldable Phone Works? What Are Limitations Of Folding ...</a></li>
<li><a href="https://vertu.com/guides/heavy-daily-use-how-long-does-a-foldable-phone-really-last">Foldable Phone Lifespan: How Long Do They Really Last?</a></li>

</ul>
</details>

**标签**: `#Apple`, `#iPhone`, `#Foldable Devices`, `#Consumer Technology`, `#Product Launch`

---

<a id="item-35" class="hz-item-anchor" data-hz-url="https://www.bbc.co.uk/news/articles/c74edv9887eo?at_medium=RSS&at_campaign=rss" data-hz-title="人工智能黑客事件加剧对自主系统的担忧" data-hz-tags="AI safety,autonomous agents,cybersecurity,AI risks" data-hz-section="other"></a>
## [人工智能黑客事件加剧对自主系统的担忧](https://www.bbc.co.uk/news/articles/c74edv9887eo?at_medium=RSS&at_campaign=rss) ⭐️ 7.0/10

英国广播公司的一篇报道调查了一起据称由人工智能代理开展失控黑客活动的事件。该事件加剧了人们对自主程度不断提高的人工智能系统，以及它们可能超出人类预期进行行动的担忧。 这一事件表明，能够自主追求目标、使用工具并采取行动的人工智能代理，可能以更快速度和更大规模制造网络安全风险。它也重新引发了关于人工智能安全、对齐以及人类如何保持对先进系统有效控制的讨论。 现有内容没有说明这些人工智能代理的具体类型、攻击目标、所利用的漏洞或失效的安全措施，因此黑客活动的规模和确切性质仍不清楚。因此，应谨慎理解报道中的表述，不能将其视为人工智能系统已经具备自主接管能力的证据。

rss · BBC World News · 9月9日 23:17

**背景**: 人工智能代理是一种能够追求目标、使用软件或其他工具，并在一定程度上自主采取行动的程序，而不只是回应单个提示。人工智能对齐是一个研究问题，重点是确保系统可靠地遵循预定目标，并始终接受人类控制。在网络安全领域，更高的自主性可以帮助系统进行威胁检测和响应，但也可能放大目标设定不当或安全措施不足所造成的后果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>
<li><a href="https://www.rstreet.org/research/the-rise-of-ai-agents-anticipating-cybersecurity-opportunities-risks-and-the-next-frontier/">The Rise of AI Agents: Anticipating Cybersecurity ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#autonomous agents`, `#cybersecurity`, `#AI risks`

---

<a id="item-36" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMifkFVX3lxTE1zaHdLZTE4N3FUYWJQS0hMNlFvaVpTd2hQRzRwb3dpaXNRMk5Kbk9RV2duekxja0UtZkpLb2tqeXJZOFV4Qjd3VHZ2WkpKbmc5T1dBZGlqR2t6Rnl6bG5JT0xSRlY2T3BfQ0xGZVI2UEFqS3BUOUtlM3hreGZiQQ?oc=5" data-hz-title="ACE Robotics与南洋理工大学开源Puffin-World" data-hz-tags="robotics,multimodal AI,world models,open source,embodied AI" data-hz-section="other"></a>
## [ACE Robotics 与南洋理工大学开源 Puffin-World](https://news.google.com/rss/articles/CBMifkFVX3lxTE1zaHdLZTE4N3FUYWJQS0hMNlFvaVpTd2hQRzRwb3dpaXNRMk5Kbk9RV2duekxja0UtZkpLb2tqeXJZOFV4Qjd3VHZ2WkpKbmc5T1dBZGlqR2t6Rnl6bG5JT0xSRlY2T3BfQ0xGZVI2UEFqS3BUOUtlM3hreGZiQQ?oc=5) ⭐️ 7.0/10

ACE Robotics 与南洋理工大学开源了 Puffin-World，这是一个旨在支持机器人和具身人工智能研究的统一多模态世界模型。该模型通过物理、几何和外观三种原生状态表示现实世界。 结合这些世界表示的开源模型，可能为机器人学习、仿真和物理世界理解提供共同基础。它还可能减少研究人员对封闭世界模型系统的依赖，从而提升具身人工智能研究的可复现性。 Puffin-World 通过重力和纬度等概念建模物理状态，通过深度表示几何状态，并通过图像表示外观状态；它还可以根据单张图像推断相机属性和场景语义描述。目前提供的信息没有说明其基准测试结果、实际部署性能，以及模型对硬件和数据的要求。

google_news · Pandaily · 9月11日 03:11

**背景**: 世界模型是一类用于表示环境的人工智能系统，使模型能够推理场景、状态或可能的结果。具身人工智能中的系统必须理解并 მოქმედ于物理世界，而不只是处理文本或图像，因此世界模型对机器人具有重要意义。多模态建模会结合图像、几何和物理属性等输入或表示，而三维世界模型则进一步加入空间结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kangliao929.github.io/projects/puffin-world/">Puffin - World · Scaling with Native 3D World States</a></li>
<li><a href="https://huggingface.co/blog/KangLiao/puffin-world">Puffin - World : Scaling a Unified Multimodal Model with Native...</a></li>
<li><a href="https://world-models.io/en/categories/embodied-ai/">Embodied AI | World Models Category | world - models .io</a></li>

</ul>
</details>

**标签**: `#robotics`, `#multimodal AI`, `#world models`, `#open source`, `#embodied AI`

---

<a id="item-37" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMndESjdZM0ltRWpGVXpIY0RwdEF2WDZfLVpwVVQ5TEhGX1FBbWNQdGZxNThBVTE1aUpEdUhhQkFma2FWRW5WZmZBUDBXQmtpZmg2MjFfZXRJYUprN2dtdHB0N2dZUjZDR3RwSDlYRDZIeEp0Q2RJblRvbm1YdjR4bEh6T3YxclJYOEdN?oc=5" data-hz-title="宇树发布UnifoLM-WLA-1.0人形机器人基础模型页面" data-hz-tags="Humanoid Robotics,Embodied AI,Foundation Models,Robot Learning,Unitree" data-hz-section="other"></a>
## [宇树发布 UnifoLM-WLA-1.0 人形机器人基础模型页面](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPMndESjdZM0ltRWpGVXpIY0RwdEF2WDZfLVpwVVQ5TEhGX1FBbWNQdGZxNThBVTE1aUpEdUhhQkFma2FWRW5WZmZBUDBXQmtpZmg2MjFfZXRJYUprN2dtdHB0N2dZUjZDR3RwSDlYRDZIeEp0Q2RJblRvbm1YdjR4bEh6T3YxclJYOEdN?oc=5) ⭐️ 7.0/10

宇树已发布 UnifoLM-WLA-1.0 项目页面，这是一个面向机器人控制和具身智能的人形机器人基础模型。搜索结果显示，该模型约有六十亿个参数，使用约 2500 小时真实机器人数据训练，并且一个模型检查点可覆盖 64 项桌面操作和全身操作任务。 一个同时覆盖桌面操作和全身操作的模型，可能减少为不同任务、末端执行器和机器人动作分别开发策略的需要。该项目也可能为研究人员和开发者实验通用人形机器人学习提供更易获取的基础，但其实际影响仍取决于后续发布内容和独立评测。 据报道，该模型架构结合了具身推理器、动态光流世界建模模块和 MMDiT 动作专家，用于驱动全身操作。项目页面据称将代码、模型权重和数据集标注为“即将发布”，因此目前不应将其所宣称的能力视为已经完全可复现。

google_news · Pandaily · 9月11日 07:52

**背景**: 基础模型是一种大规模预训练模型，目标是支持多个下游任务，而不是只执行一种狭窄定义的行为。在人形机器人领域，具身智能将感知、推理和物理动作连接起来，使机器人能够在真实环境中操作物体并移动。全身操作不仅限于桌面场景，还包括机器人身体和移动平台的协调运动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://letsdatascience.com/news/unitree-publishes-unifolm-wla-10-humanoid-model-details-ebe51eec">Unitree Publishes UnifoLM-WLA-1.0 Humanoid Model Details</a></li>
<li><a href="https://www.humanoidsdaily.com/news/unitree-open-sources-unifolm-wla-1-0-to-tackle-humanoid-generalization">Unitree Open-Sources UnifoLM-WLA-1.0 to Tackle Humanoid ...</a></li>

</ul>
</details>

**标签**: `#Humanoid Robotics`, `#Embodied AI`, `#Foundation Models`, `#Robot Learning`, `#Unitree`

---

<a id="item-38" class="hz-item-anchor" data-hz-url="https://huggingface.co/blog/gradio-workflow-1111" data-hz-title="用 Gradio Workflow 重建 AUTOMATIC1111" data-hz-tags="Generative AI,Stable Diffusion,Gradio,Machine Learning,UI Development" data-hz-section="other"></a>
## [用 Gradio Workflow 重建 AUTOMATIC1111](https://huggingface.co/blog/gradio-workflow-1111) ⭐️ 6.0/10

这篇教程展示了如何使用 Gradio Workflow 重建 AUTOMATIC1111 风格的 Stable Diffusion 核心功能。它说明了如何构建可定制的图像生成界面，而不必完全依赖原始网页界面。 这种方法让开发者能够更好地控制用户体验，并更容易针对特定应用定制 Stable Diffusion 工作流。它也展示了 Gradio 如何支持更加广泛的定制生成式人工智能界面生态。 AUTOMATIC1111 是一个开源的 Stable Diffusion 网页界面，拥有大量扩展和定制功能，而 Gradio 提供了用于创建专用工作流的 Python 界面构建层。重建部分功能可以提高灵活性，但不一定能够复制 AUTOMATIC1111 的全部功能或扩展生态。

rss · Hugging Face Blog · 9月10日 00:00

**背景**: Stable Diffusion 是一种可以根据文本提示生成图像的生成模型。AUTOMATIC1111 将 Stable Diffusion 封装在网页界面中，并加入了用于定制图像生成的控制项和扩展。Gradio 是一个用于创建交互式界面的 Python 库，因此可以用来把部分图像生成步骤呈现在定制应用中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nerdstool.com/blog/rebuilding-automatic1111-with-gradio-workflow">Rebuilding AUTOMATIC1111 with Gradio Workflow | NerdsTool</a></li>
<li><a href="https://en.wikipedia.org/wiki/AUTOMATIC1111_Stable_Diffusion_Web_UI">AUTOMATIC1111 Stable Diffusion Web UI</a></li>
<li><a href="https://gradio.app/docs/gradio/interface">gradio .app/docs/ gradio / interface</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#Stable Diffusion`, `#Gradio`, `#Machine Learning`, `#UI Development`

---

<a id="item-39" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/09/10/openai-puts-pro-subscriptions-on-hold-due-to-astra-demand/" data-hz-title="OpenAI 因 Astra 需求暂停专业版注册" data-hz-tags="OpenAI,Astra,AI infrastructure,Capacity scaling,Subscriptions" data-hz-section="other"></a>
## [OpenAI 因 Astra 需求暂停专业版注册](https://techcrunch.com/2026/09/10/openai-puts-pro-subscriptions-on-hold-due-to-astra-demand/) ⭐️ 6.0/10

OpenAI 暂时暂停了新的专业版订阅注册，因为专业版账户对其系统造成的压力最大。公司正在扩充容量，之后才会重新开放注册。 此次暂停表明，Astra 的需求已经超过了专业版用户可用的系统容量。这也说明，随着高能力模型和高级订阅计划推出，人工智能服务商需要同步扩展基础设施。 OpenAI 特别表示，专业版订阅对系统造成的压力最大，但没有公布容量数据或重新开放注册的日期。现有报道也没有说明限制究竟来自模型推理、计算机操作工作负载，还是服务的其他部分。

rss · TechCrunch AI · 9月10日 20:59

**背景**: Astra 指的是 OpenAI 的 GPT-6 Astra 模型，OpenAI 将其描述为面向商业用途的高能力模型。OpenAI 表示，Astra 支持高级推理和计算机操作，也具备编程、网络安全和科学相关能力。当大量订阅者同时使用这些工作负载时，可能需要大量计算容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/business/model/">GPT-6 Astra: AI for Complex Business Work | OpenAI</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Astra`, `#AI infrastructure`, `#Capacity scaling`, `#Subscriptions`

---

<a id="item-40" class="hz-item-anchor" data-hz-url="https://marginalrevolution.com/marginalrevolution/2026/09/thursday-assorted-links-569.html?utm_source=rss&utm_medium=rss&utm_campaign=thursday-assorted-links-569" data-hz-title="泰勒·科文汇总机器人、AI安全与核风险相关链接" data-hz-tags="AI safety,Robotics,Nuclear risk,Economic analysis,Forecasting" data-hz-section="other"></a>
## [泰勒·科文汇总机器人、AI 安全与核风险相关链接](https://marginalrevolution.com/marginalrevolution/2026/09/thursday-assorted-links-569.html?utm_source=rss&utm_medium=rss&utm_campaign=thursday-assorted-links-569) ⭐️ 6.0/10

泰勒·科文的文章汇总了印度新的 GDP 统计数据、机器人为何难以发展、通胀趋势变化、核风险、20 世纪音乐、AI 安全初创企业，以及 AI 悲观主义者预测记录等主题的链接。文章还介绍了 Project Tailwind，这是一个号召创始人成立雄心勃勃的 AI 安全组织的项目。 这组链接把经济状况和技术挑战，与灾难性风险及 AI 生态系统的准备程度联系起来。Project Tailwind 可能通过资助开展故障注入训练、AI 决策工具、对齐研究和前沿能力监测等工作的组织，扩大 AI 安全领域的建设。 这是一篇简短而零散的链接汇总，并非关于单一事件的报道，因此没有提供太多原创技术分析，也没有深入解决所提出的问题。现有材料显示，Project Tailwind 是为新 AI 安全组织提供资金支持的倡议，而文章对其他链接仅作了主题层面的介绍。

rss · Marginal Revolution · 9月10日 15:47

**背景**: 链接汇总是指引导读者阅读其他地方发布的材料，而不是对单一主题进行完整分析的文章。这里的 AI 安全指旨在降低高级 AI 系统风险的相关工作，而 Project Tailwind 被描述为寻找创始人来填补这一生态系统重要缺口的倡议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://remoteimpact.org/jobs/project-tailwind-call-for-ambitious-ai-safety-initiatives-coefficient-giving/">Project Tailwind, Call for Ambitious AI Safety Initiatives</a></li>
<li><a href="https://news.ycombinator.com/item?id=49650317">Project Tailwind is a call for ambitious AI safety ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#Robotics`, `#Nuclear risk`, `#Economic analysis`, `#Forecasting`

---

<a id="item-41" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMieEFVX3lxTE1ucW9LQVhaRDBJM3RTM0F0TzdWeUk0bEZnclJWd0thMTR1THdOX2gtd3BFaE5MQ251OUlWd1VKQkwySjktWFY0OTVxOXZCbHp0SVF6dW9JWGtoR042NnBSMTJyNWZTc05rd2FDYjdfYXNhSlQ1blVVZA?oc=5" data-hz-title="开源项目利用声学信号探测无人机" data-hz-tags="Open Source,Drone Detection,Acoustic Signal Processing,Embedded Systems,Security" data-hz-section="other"></a>
## [开源项目利用声学信号探测无人机](https://news.google.com/rss/articles/CBMieEFVX3lxTE1ucW9LQVhaRDBJM3RTM0F0TzdWeUk0bEZnclJWd0thMTR1THdOX2gtd3BFaE5MQ251OUlWd1VKQkwySjktWFY0OTVxOXZCbHp0SVF6dW9JWGtoR042NnBSMTJyNWZTc05rd2FDYjdfYXNhSlQ1blVVZA?oc=5) ⭐️ 6.0/10

Hackaday 介绍了一个通过分析声学信号来探测无人机的开源项目。现有报道没有提供具体的硬件、软件版本、准确率或部署细节。 开源实现可以让从事信号处理、嵌入式系统和安全工作的研究人员、爱好者及从业者更容易开展声学无人机探测。由于声学传感属于被动感知，它可以在无线电频段监测不足的场景中补充其他探测方法。 声学探测依靠无人机螺旋桨、电机和机械振动产生的噪声，麦克风阵列还可以帮助估计无人机的方向或位置。背景噪声、距离、天气以及不同无人机的声学特征都可能影响性能，而所提供材料没有说明该项目报告的具体限制。

google_news · Hackaday · 9月10日 11:00

**背景**: 声学无人机探测通过监听无人机产生的声音来发现目标，而不是主动发射信号进行搜索。麦克风阵列利用多个麦克风比较接收到的声音，从而辅助定位；信号处理或机器学习方法则可以帮助区分无人机噪声与其他声音。与无线电频段探测不同，声学感知也可能适用于自主飞行或使用光纤系留的无人机，但它仍然容易受到环境噪声影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sqhead.com/drone-detection">Drone Detection — Squarehead Technology</a></li>
<li><a href="https://www.jaredwatkins.com/research/drone-detection/detection-methods/acoustic-detection/">Acoustic Detection - The Infinite Unknown</a></li>

</ul>
</details>

**标签**: `#Open Source`, `#Drone Detection`, `#Acoustic Signal Processing`, `#Embedded Systems`, `#Security`

---

<a id="item-42" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiqwFBVV95cUxPc0ZkYjZWajBZM19UNXJZcmltdnJSZlNRV0dzMmtvRDJBaGdUTWdSMk1nWWYwcGRiQ1hFRklHcmlsd2trWU5ZdjNwekdlUjZDVWgyYUwzVklpR25TWnNKXzJXMnVJXzBKbEYweWpHeU9qUHBMSklyenB6dVZoQ2NMZ2ExZ1NSVXpwc2RaUU05SF9ha0psRENSdW9lUi1ONUtZOGRFTi0wLTlaalE?oc=5" data-hz-title="荧光视频实现犬血微丝蚴的诊所内自动检测" data-hz-tags="Biomedical Imaging,Computer Vision,Automated Diagnostics,Global Health,Medical Technology" data-hz-section="other"></a>
## [荧光视频实现犬血微丝蚴的诊所内自动检测](https://news.google.com/rss/articles/CBMiqwFBVV95cUxPc0ZkYjZWajBZM19UNXJZcmltdnJSZlNRV0dzMmtvRDJBaGdUTWdSMk1nWWYwcGRiQ1hFRklHcmlsd2trWU5ZdjNwekdlUjZDVWgyYUwzVklpR25TWnNKXzJXMnVJXzBKbEYweWpHeU9qUHBMSklyenB6dVZoQ2NMZ2ExZ1NSVXpwc2RaUU05SF9ha0psRENSdW9lUi1ONUtZOGRFTi0wLTlaalE?oc=5) ⭐️ 6.0/10

研究人员开发了一种快速、免手操作的检测方法，将荧光视频与计算机视觉结合，用于检测并计数犬血液中的恶丝虫微丝蚴。该方法旨在支持诊所内自动检测，减少对人工显微镜检查的单独依赖。 更快速的自动化检测可能提高兽医进行常规心丝虫检查的意愿，并减少人工检验所需的工作量和不便。该技术也展示了计算机视觉改进寄生虫即时诊断的潜力。 目前报道的应用重点是利用荧光视频和计算机视觉检测、计数犬血液中的恶丝虫微丝蚴。现有信息未提供验证结果、准确率指标、不同临床环境下的表现，也未证明该方法能够检测未成熟虫体或雄虫。

google_news · Bioengineer.org · 9月10日 22:27

**背景**: 微丝蚴是丝虫的幼虫形态，可以在血液中循环，并可通过寄生虫检测进行识别。恶丝虫是导致犬心丝虫病的寄生虫，微丝蚴检测通常需要与其他诊断方法结合，因为阴性结果不能排除所有感染。荧光视频会记录发出荧光并移动的目标，计算机视觉则分析视频以识别和计数这些目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/article/10.1186/s13071-026-07486-y">Fluorescence videography for the rapid and automated in ...</a></li>
<li><a href="https://bioengineer.org/fluorescence-videography-enables-rapid-automated-in-clinic-microfilariae-detection/">Fluorescence videography enables rapid automated in - clinic ...</a></li>
<li><a href="https://www.noahvets.com/how-heartworm-testing-works-readsburg/">How Heartworm Testing Works: Antigen and Microfilariae Tests...</a></li>

</ul>
</details>

**标签**: `#Biomedical Imaging`, `#Computer Vision`, `#Automated Diagnostics`, `#Global Health`, `#Medical Technology`

---

<a id="item-43" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMieEFVX3lxTFB2UnNfZ1JCcFBPMWZ1cGsyQWRZbWZLXzdQZk1nT0Nwb2JzUlNnMVpfYXI4eWlybG9vd3l2VWxkYWhhRWpJbkE0aTR6MGxnNVo1aEdvMnpwZGJRc1czbVM5aFNpMDRvby1LVVJfTUhVV0FwdEFHTGJFMg?oc=5" data-hz-title="SOC Prime报告两个Windows零日漏洞" data-hz-tags="Windows Security,Zero-Day Vulnerabilities,CVE,Cybersecurity,Threat Intelligence" data-hz-section="other"></a>
## [SOC Prime 报告两个 Windows 零日漏洞](https://news.google.com/rss/articles/CBMieEFVX3lxTFB2UnNfZ1JCcFBPMWZ1cGsyQWRZbWZLXzdQZk1nT0Nwb2JzUlNnMVpfYXI4eWlybG9vd3l2VWxkYWhhRWpJbkE0aTR6MGxnNVo1aEdvMnpwZGJRc1czbVM5aFNpMDRvby1LVVJfTUhVV0FwdEFHTGJFMg?oc=5) ⭐️ 6.0/10

SOC Prime 报告了 CVE-2026-85880 和 CVE-2026-81963 两个 Windows 零日漏洞。搜索结果显示，CVE-2026-85880 是 Windows ALPC 中的堆缓冲区溢出漏洞，可导致本地权限提升；CVE-2026-81963 则影响 Windows Update Stack 中的链接解析过程。 这两个问题都可能让已经获得本地访问权限的攻击者提升权限，从而把有限的系统 foothold 扩大为对 Windows 系统的更大控制。搜索结果还显示相关漏洞已在实际攻击中被利用，因此受影响 Windows 安装环境需要提高处置优先级。 CVE-2026-85880 与 Windows Advanced Local Procedure Call 有关，搜索结果将其描述为重要的权限提升问题；CVE-2026-81963 则与 Windows Update Stack 及不当链接跟随有关。所提供的文章没有给出受影响版本、概念验证代码或明确缓解措施；一条搜索结果特别提到 CVE-2026-81963 涉及 Windows 11 和 Windows Server 2025，因此管理员应在采取行动前核对最新的 Microsoft 公告。

google_news · SOC Prime · 9月9日 23:23

**背景**: 零日漏洞是指攻击者在防御方有足够时间开发或部署修复程序之前就加以利用的漏洞。Windows ALPC 是一种进程间通信机制，因此其中的缺陷可能影响本地进程之间的权限边界。本地权限提升漏洞通常需要攻击者先获得一定的初始访问权限，但它可能通过授予更高权限而显著放大这一访问的危害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rapid7.com/db/vulnerabilities/cve-2026-85880/">CVE - 2026 - 85880 : Microsoft... | Rapid7 Vulnerability Database</a></li>
<li><a href="https://www.rapid7.com/db/vulnerabilities/cve-2026-81963/">Microsoft Windows: CVE-2026-81963: Windows Update Stack ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Windows Security`, `#Zero-Day Vulnerabilities`, `#CVE`, `#Cybersecurity`, `#Threat Intelligence`

---

<a id="item-44" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMi3wFBVV95cUxNNm5HakRRdExpckpqTTl4VVBUTk9qSFNtNUJ4d3YtRmtFajdJWC1wV1dEeDBFdFpFajlFeERTajc1clgta294REdwbXAtMGwxLU9OUkppWWZQUlVFby1zVzk3QU1CWFpZZDA2X0I0U3QxZlRBcTMtVE1CMVktYmNUVjhvQ3RMLUJSYU5SNF9ENnlWUHVQTE5QaG1nUzNUR05hRTdUeFVGd19ZN3RVRWJRdGl6T1Q1Y05YQWVpY2RqZ2JiV0EtUnlwMGVNeDRGcVdiTWR3OEZKaE5RWll6UzVJ?oc=5" data-hz-title="LTM 联手 IBM 与 Red Hat 推进 Lightwell 修复" data-hz-tags="AI,Open Source,Software Remediation,IBM,Red Hat" data-hz-section="other"></a>
## [LTM 联手 IBM 与 Red Hat 推进 Lightwell 修复](https://news.google.com/rss/articles/CBMi3wFBVV95cUxNNm5HakRRdExpckpqTTl4VVBUTk9qSFNtNUJ4d3YtRmtFajdJWC1wV1dEeDBFdFpFajlFeERTajc1clgta294REdwbXAtMGwxLU9OUkppWWZQUlVFby1zVzk3QU1CWFpZZDA2X0I0U3QxZlRBcTMtVE1CMVktYmNUVjhvQ3RMLUJSYU5SNF9ENnlWUHVQTE5QaG1nUzNUR05hRTdUeFVGd19ZN3RVRWJRdGl6T1Q1Y05YQWVpY2RqZ2JiV0EtUnlwMGVNeDRGcVdiTWR3OEZKaE5RWll6UzVJ?oc=5) ⭐️ 6.0/10

LTM 宣布与 IBM 和 Red Hat 合作开展 Lightwell 项目，这是一个旨在修复开源软件漏洞的 AI 驱动计划。该合作希望通过 AI 辅助的漏洞修复，帮助企业保护开源软件供应链。 现代应用程序高度依赖开源组件，因此更快地修复漏洞可能缩短漏洞被发现与采取防护措施之间的时间。该合作也体现了行业利用 AI 以企业规模管理软件供应链安全的趋势。 IBM 将 Lightwell 描述为覆盖从上游代码到企业部署的开源软件完整生命周期，其相关服务则侧重于发现、排序并降低供应链风险。现有公告没有详细说明 LTM 的具体职责，也没有提供可量化的成果，因此实际影响仍有待验证。

google_news · India's News.Net · 9月9日 20:27

**背景**: 开源软件供应链安全关注应用程序依赖外部项目和社区维护的代码时产生的风险。漏洞修复是处理这些安全弱点的过程，通常包括应用或调整安全补丁。IBM 和 Red Hat 将 Lightwell 定义为一种覆盖开源软件完整生命周期的安全方案，并将 AI 驱动的漏洞修复作为核心能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/products/lightwell">Lightwell - IBM</a></li>
<li><a href="https://www.redhat.com/en/lightwell">Lightwell - redhat.com</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#Software Remediation`, `#IBM`, `#Red Hat`

---

<a id="item-45" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiekFVX3lxTE02My1FcTZPRElzQmJFQ0hkcXZKWldqOU52YkNYa3pGdC1vOTlhSUpNbUVpY0NWdjgteUJsZVVvRjMtY3N2Sjl4WFA2SUh2U0JHT1B1UXVrSzBKb0xyVUtMbmhoZ1JLYzdyZnpuV0VVYUtlYVVnWDVfcjhR?oc=5" data-hz-title="GitHub扩大高级安全功能试用范围" data-hz-tags="GitHub,Application Security,DevSecOps,Developer Tools" data-hz-section="other"></a>
## [GitHub 扩大高级安全功能试用范围](https://news.google.com/rss/articles/CBMiekFVX3lxTE02My1FcTZPRElzQmJFQ0hkcXZKWldqOU52YkNYa3pGdC1vOTlhSUpNbUVpY0NWdjgteUJsZVVvRjMtY3N2Sjl4WFA2SUh2U0JHT1B1UXVrSzBKb0xyVUtMbmhoZ1JLYzdyZnpuV0VVYUtlYVVnWDVfcjhR?oc=5) ⭐️ 5.0/10

GitHub 正在扩大其高级安全功能试用的访问范围，让更多用户和组织能够进行评估。DevOps.com 报道了这一更新，但现有信息没有说明具体的资格变化或推出时间表。 扩大试用范围可能帮助更多组织在现有的 GitHub 和 DevSecOps 工作流程中评估应用安全工具。这或许能让组织更容易判断高级安全功能是否值得广泛采用，但目前没有证据表明其已经产生行业范围的影响。 GitHub Advanced Security 包含代码扫描、机密扫描和依赖项审查等功能，分别用于处理漏洞、暴露的机密信息和存在风险的依赖项。现有报道没有提供价格、试用期限、支持的方案、功能限制或经过测量的安全结果。

google_news · DevOps.com · 9月11日 08:20

**背景**: GitHub Advanced Security 是一组集成在 GitHub 中的安全工具。代码扫描用于发现源代码中的漏洞，机密扫描用于查找暴露的凭据或其他机密信息，依赖项审查则检查项目依赖项变更可能带来的风险。这些功能通过将安全检查融入开发者工作流程来支持 DevSecOps 方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/git/github-advanced-security/">GitHub Advanced Security - GeeksforGeeks</a></li>
<li><a href="https://www.liatrio.ai/resources/blog/github-advanced-security-intro">Build security into your apps within the developers’ workflow</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#Application Security`, `#DevSecOps`, `#Developer Tools`

---

<a id="item-46" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMid0FVX3lxTE51Q3dmVktkX2ViLXZpa09TaDhKNVdiUmx3dmlmUHdyaXNBdEtYMXZVZjZWTDhFb1BOQU1IMFRnR3phMUxoWHNuOUNYdmhRaWUyb1RtRHo0ZXBqT1NLZGZGRGFScG9CZTduWDhwdzJFX1BqT3FkdkpF?oc=5" data-hz-title="Herdr：面向人工智能编程代理的开源运行时" data-hz-tags="AI coding agents,Developer tools,Open source,Terminal,Agent orchestration" data-hz-section="other"></a>
## [Herdr：面向人工智能编程代理的开源运行时](https://news.google.com/rss/articles/CBMid0FVX3lxTE51Q3dmVktkX2ViLXZpa09TaDhKNVdiUmx3dmlmUHdyaXNBdEtYMXZVZjZWTDhFb1BOQU1IMFRnR3phMUxoWHNuOUNYdmhRaWUyb1RtRHo0ZXBqT1NLZGZGRGFScG9CZTduWDhwdzJFX1BqT3FkdkpF?oc=5) ⭐️ 5.0/10

Herdr 是一个用于协调和管理多个人工智能编程代理的开源终端与运行时。它的服务器会在本地计算机或租用的机器上保持终端运行，让代理能够持续工作，并支持之后重新连接会话。 该项目针对同时可靠运行多个人工智能编程代理的需求，避免笔记本合盖、网络中断或机器重启导致终端会话丢失。这可能让基于代理的软件开发流程更加持久，也更容易在不同设备之间管理。 Herdr 以后台服务器形式运行，终端会话托管在其中，并可从另一个终端或通过 SSH 再次访问。搜索结果将其描述为使用 Rust 构建、能够识别特定人工智能代理的终端复用器，但现有信息没有提供详细的兼容性、协作机制或采用情况数据。

google_news · Intelligent Living · 9月10日 02:13

**背景**: 终端复用器可以在一个持久运行的服务中保留多个命令行会话，使用户能够断开连接并重新连接，而不会停止底层进程。Herdr 将这一模式应用于人工智能编程代理，通过保持代理终端运行来支持跨设备访问。SSH 是一种通过终端连接远程计算机的标准方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://herdr.dev/">Herdr : the runtime coding agents run on</a></li>
<li><a href="https://github.com/herdrdev/herdr">GitHub - herdrdev/ herdr : the runtime your coding agents live on</a></li>
<li><a href="https://aiunderstanding.org/news/herdr-launches-open-source-terminal-for-managing-multiple-ai-coding-agents">Herdr launches open - source terminal for... | AI Understanding</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#Developer tools`, `#Open source`, `#Terminal`, `#Agent orchestration`

---

<a id="item-47" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMidkFVX3lxTE9kbHRCaHJ6bGp2eHdSbnNGMFlfRU5LNVBoV3RCMEZWUHdJMFZPWk1KaGxRcTdnd0p1aG5COHlpUnduRm10aDJGc3ZDVzkzYzRtUWJQN0JFTEF0MEo1UlZ6Z0hOTlRxZ1I0N0Q4eEtvWFBES2VjV1E?oc=5" data-hz-title="GitHub报告八月发生五起事件" data-hz-tags="GitHub,reliability engineering,incident response,platform resilience" data-hz-section="other"></a>
## [GitHub 报告八月发生五起事件](https://news.google.com/rss/articles/CBMidkFVX3lxTE9kbHRCaHJ6bGp2eHdSbnNGMFlfRU5LNVBoV3RCMEZWUHdJMFZPWk1KaGxRcTdnd0p1aG5COHlpUnduRm10aDJGc3ZDVzkzYzRtUWJQN0JFTEF0MEo1UlZ6Z0hOTlRxZ1I0N0Q4eEtvWFBES2VjV1E?oc=5) ⭐️ 5.0/10

GitHub 报告称八月发生了五起事件，并介绍了提升平台韧性的相关工作。 这项更新让用户了解 GitHub 的运营可靠性，也表明该公司正在持续加强事件响应和平台韧性。 现有报道没有提供这五起事件的技术细节、严重程度或具体韧性措施。

google_news · blockchain.news · 9月10日 02:54

**背景**: 事件是可能影响平台可用性或性能的运营故障。平台韧性是指平台承受此类事件、进行响应并在事后恢复的能力。

**标签**: `#GitHub`, `#reliability engineering`, `#incident response`, `#platform resilience`

---

<a id="item-48" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMigAJBVV95cUxQMm9FYWRzSTBxLWdLWXZiR0Y5aDYwZzZJQmctczVoRDJOaXd6TWNiQ3lKeW1CYjVNTFBsRXQwMW1rOTU2UXFsLXRKTlo3TkNrSi1TRG1UaGc0eEdqdVFtT3dMQk9BV1Blc1pMTmkxWk4waFBWbXpZVnFRWUY0ZTZEMTFGa3JpcVhEZldja2s5V3dCekkycVNzOVNfV2dfNFhIbEJCX1JlS0FWaXhrZEN6aVl0OGlYVTVLNm5XUDJvbndRbXV4YWV2UFpXRERQVDdyb2JiRk5DZEFrVHhnczBiOVk4eXJFOWt5d2R6MDZHNkdvZ19SMHRSY3RXdmIwam9f0gGGAkFVX3lxTE1RVUxQOGI1MWplTGpyaFVCczJpWkZfeDFlVDQ0WU56YTdSdWxvS0hhZjB2cGtIQ3lZUDg1YWFXekxzbEU0MXo0Zncyb29pZmYxaElpMi10MjR6dFN5R0g0NmJrNUFhQm1KeEhvNnQweHNQdWNQZXFTcUJDOEdLWXRJZlVRT0x6UVVmWlF5WG1TdER5MVFJM1dkSnlVY3lwb1dQOXVmTXg2UzcyU0p1OHdHZ0RzZldXajItU1VWenJZeGRjbVlKSlZFT3R2X0RfYlJVVVdnaVdyb2NqZDEzaC0zdTI4ejhOb0hHNE1UendQbklQbFR6bGpKU1BLWUZlSUUxb01kMmc?oc=5" data-hz-title="Percona与Coroot合作推进开源数据库可观测性" data-hz-tags="" data-hz-section="other"></a>
## [Percona 与 Coroot 合作推进开源数据库可观测性](https://news.google.com/rss/articles/CBMigAJBVV95cUxQMm9FYWRzSTBxLWdLWXZiR0Y5aDYwZzZJQmctczVoRDJOaXd6TWNiQ3lKeW1CYjVNTFBsRXQwMW1rOTU2UXFsLXRKTlo3TkNrSi1TRG1UaGc0eEdqdVFtT3dMQk9BV1Blc1pMTmkxWk4waFBWbXpZVnFRWUY0ZTZEMTFGa3JpcVhEZldja2s5V3dCekkycVNzOVNfV2dfNFhIbEJCX1JlS0FWaXhrZEN6aVl0OGlYVTVLNm5XUDJvbndRbXV4YWV2UFpXRERQVDdyb2JiRk5DZEFrVHhnczBiOVk4eXJFOWt5d2R6MDZHNkdvZ19SMHRSY3RXdmIwam9f0gGGAkFVX3lxTE1RVUxQOGI1MWplTGpyaFVCczJpWkZfeDFlVDQ0WU56YTdSdWxvS0hhZjB2cGtIQ3lZUDg1YWFXekxzbEU0MXo0Zncyb29pZmYxaElpMi10MjR6dFN5R0g0NmJrNUFhQm1KeEhvNnQweHNQdWNQZXFTcUJDOEdLWXRJZlVRT0x6UVVmWlF5WG1TdER5MVFJM1dkSnlVY3lwb1dQOXVmTXg2UzcyU0p1OHdHZ0RzZldXajItU1VWenJZeGRjbVlKSlZFT3R2X0RfYlJVVVdnaVdyb2NqZDEzaC0zdTI4ejhOb0hHNE1UendQbklQbFR6bGpKU1BLWUZlSUUxb01kMmc?oc=5) ⭐️ ?/10

Percona 与 Coroot 达成合作，旨在为开源数据库环境带来全栈可观测性能力。现有信息确认了合作关系，但未说明发布日期、支持的数据库版本或具体集成功能。 这项合作可能让运行开源数据库的团队更容易在统一工作流中查看指标、日志和追踪信息，从而减少对多套监控工具的依赖。不过，实际影响仍取决于合作方案的落地方式和数据库覆盖范围。 Coroot 将其平台定位为开源方案，重点分析指标、日志和追踪信息，而新闻内容明确将合作范围指向开源数据库环境。现有材料未提供部署模式、集成方式、许可条款、性能开销或支持边界等技术细节。

google_news · manilatimes.net · 9月10日 11:54

**背景**: 可观测性是利用系统遥测数据了解内部状态并排查问题的方法。全栈可观测性会将指标、日志和追踪等多种信号整合起来，以便从更广泛的角度查看应用和基础设施。Coroot 将自己定位为一个开源可观测性平台，旨在简化这类分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://coroot.com/">Coroot - Full-stack observability in minutes</a></li>

</ul>
</details>

---