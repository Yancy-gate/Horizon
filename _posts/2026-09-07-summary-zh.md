---
layout: default
title: "Horizon Summary: 2026-09-07 (ZH)"
date: 2026-09-07
lang: zh
---

> 从 105 条内容中筛选出 44 条重要资讯。

---

## 偏好雷达

> 基于你维护的偏好档案（data/preference-radar/profile.json）独立筛选的个性化内容。

今日暂无符合偏好的更新。

---
## 华科老师研究方向

> 依据学院教师公开研究方向与论文关键词筛选。

1. [STO-CAST 预测热带气旋期间的停电](#item-1) ⭐️ 8.0/10
2. [自适应电压协调提升 VSG 逆变器暂态稳定性](#item-2) ⭐️ 7.0/10
3. [注入时段无传感器控制改进 SPMSM 预测驱动](#item-3) ⭐️ 7.0/10
4. [评估并网跟随型逆变器奈奎斯特频率以上的延迟](#item-4) ⭐️ 7.0/10
5. [关键基础设施最坏情况中断的模型与算法](#item-5) ⭐️ 7.0/10
6. [融入共享快速公交车道的公交网络优化设计](#item-6) ⭐️ 7.0/10
7. [概率分层匹配改进电动汽车调度](#item-7) ⭐️ 7.0/10
8. [面向电网负荷的概率分层匹配电动汽车调度](#item-8) ⭐️ 7.0/10
9. [固体氧化物燃料电池系统控制目标与挑战综述](#item-9) ⭐️ 6.0/10
10. [结合改进 ADRC 与自适应谐波滤波的 PMSM 无位置传感器控制](#item-10) ⭐️ 6.0/10
11. [概率层级匹配优化电动汽车调度与电网负荷](#item-11) ⭐️ 6.0/10
12. [用于永磁同步电机动态切换的级联双代价函数模型预测控制](#item-12) ⭐️ 5.0/10
13. [车辆调度的层级匹配方法](#item-13) ⭐️ 5.0/10
14. [公交网络与时刻表协同设计](#item-14) ⭐️ 5.0/10

---
<a id="item-1" class="hz-item-anchor" data-hz-url="https://doi.org/10.1111/risa.70275" data-hz-title="STO-CAST预测热带气旋期间的停电" data-hz-tags="Deep Learning,Spatiotemporal Forecasting,Power Systems,Disaster Response,Climate Risk" data-hz-section="hust-research"></a>
## [STO-CAST 预测热带气旋期间的停电](https://doi.org/10.1111/risa.70275) ⭐️ 8.0/10

研究人员提出了 STO-CAST，这是一种时空深度学习模型，能够在热带气旋期间结合不断变化的气象预测和新观测到的停电数据，持续更新每小时停电预测。该模型以 4×4 公里分辨率提供 6 小时临近预报和 60 小时规划预报，并使用 2022 年台风梅花案例进行了评估。 更及时且空间细致的停电预测可以帮助电力企业和应急机构识别不断变化的停电热点，提前部署人员与设备，并改善实时响应。基于观测更新的设计弥补了开环模型的重要不足，因为开环模型无法随着风暴条件和电力系统状态变化而调整。 STO-CAST 将静态环境与基础设施属性，同动态气象和停电序列结合起来，并在整个风暴事件中进行滚动推理。其诊断性误差分解能够区分模型局限、气象不确定性和观测缺失的影响，但目前报告的证据主要来自一次风暴案例，并采用留一风暴交叉评估。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月26日 00:00

**匹配依据**: 论文关键词命中 **tropical cyclone**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 时空模型会同时分析不同地点和不同时间的条件变化，这一点很重要，因为热带气旋造成的损害和停电会在事件过程中移动并演变。6 小时临近预报有助于掌握即时态势，而 60 小时预测则为电力企业提前规划和部署资源提供更多时间。基于观测更新的推理意味着，新收到的停电报告可以修正后续预测，而不是让最初的预测保持不变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/42186946/">From Forecast to Action: A Deep Learning Model for Predicting Power Outages During Tropical Cyclones - PubMed</a></li>
<li><a href="https://arxiv.org/abs/2512.06644">[2512.06644] From Forecast to Action: A Deep Learning Model for Predicting Power Outages During Tropical Cyclones</a></li>

</ul>
</details>

**标签**: `#Deep Learning`, `#Spatiotemporal Forecasting`, `#Power Systems`, `#Disaster Response`, `#Climate Risk`

---

<a id="item-2" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560379" data-hz-title="自适应电压协调提升VSG逆变器暂态稳定性" data-hz-tags="Grid-forming inverters,Transient stability,Virtual synchronous generators,Power systems,Renewable energy integration" data-hz-section="hust-research"></a>
## [自适应电压协调提升 VSG 逆变器暂态稳定性](https://doi.org/10.1109/ccdc69976.2026.11560379) ⭐️ 7.0/10

该论文提出在虚拟同步发电机控制的构网型逆变器中，自适应协调快速和慢速内部电压源。该方法旨在提升逆变器应对严重电网扰动时的暂态稳定性。 随着可再生能源渗透率提高，构网型逆变器需要在保持建立和调节电网电压、频率能力的同时维持稳定。更好的暂态稳定性有助于逆变器型可再生能源资源在更严峻的扰动条件下接入电网。 搜索结果指出，现有措施存在权衡：冻结功率控制环可以抑制功角发散，但可能削弱构网能力；基于虚拟阻抗的限流方案则通过不同机制应对扰动。现有信息未报告该协调方法的数值性能结果、运行边界或实验验证情况。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **grid-forming**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 虚拟同步发电机是一种控制策略，使逆变器模拟传统同步发电机的特性，包括下垂响应、惯性和阻尼。构网型逆变器可以利用这类控制帮助调节电网电压和频率，而不是完全依赖外部已经建立的电网波形。暂态稳定性描述受大扰动后，受控逆变器能否保持同步并恢复稳定运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/topics/engineering/virtual-synchronous-generator">Virtual Synchronous Generator - an overview | ScienceDirect Topics</a></li>
<li><a href="https://ieeexplore.ieee.org/abstract/document/11560379">Adaptive Fast/Slow Internal Voltage Source Coordination for ...</a></li>
<li><a href="https://ieeexplore.ieee.org/document/10105459">Control of Grid-Forming VSCs: A Perspective of Adaptive Fast ...</a></li>

</ul>
</details>

**标签**: `#Grid-forming inverters`, `#Transient stability`, `#Virtual synchronous generators`, `#Power systems`, `#Renewable energy integration`

---

<a id="item-3" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/tpel.2026.3678851" data-hz-title="注入时段无传感器控制改进SPMSM预测驱动" data-hz-tags="Sensorless Control,Model Predictive Control,Permanent-Magnet Motors,Power Electronics,Motor Drives" data-hz-section="hust-research"></a>
## [注入时段无传感器控制改进 SPMSM 预测驱动](https://doi.org/10.1109/tpel.2026.3678851) ⭐️ 7.0/10

该论文提出了一种基于注入时段的开关频率注入无传感器控制策略，并将其与扩展控制集死区预测电流控制结合，用于表面式永磁同步电机。实验结果表明，该方法能够减少有限控制集控制中的电压注入误差，提高位置估计精度，并显著缩短执行时间。 准确的转子位置估计对于无传感器电机驱动十分重要，而注入误差和较长的计算时间会限制有限控制集预测控制的实际应用。该方法有望提升表面式永磁同步电机驱动的实用性能，对电机驱动和电力电子研究具有参考价值。 该方法采用基于扩展控制集的角域迭代优化方法，并利用直轴电流偏置进行位置估计，同时提出了简便的初始位置检测方法。论文还分析了电流偏置引起的速度振荡，并通过实验验证了所提方法。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 3月31日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 开关频率注入通过向电机注入信号并观察电流响应来估计转子位置。有限控制集模型预测控制需要从可用的逆变器开关状态中进行选择，但离散控制动作可能造成电压注入不准确。死区预测电流控制试图快速将预测电流驱动到目标值，而扩展控制集则提供更多可选的控制动作。

**标签**: `#Sensorless Control`, `#Model Predictive Control`, `#Permanent-Magnet Motors`, `#Power Electronics`, `#Motor Drives`

---

<a id="item-4" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/apec51134.2026.11516799" data-hz-title="评估并网跟随型逆变器奈奎斯特频率以上的延迟" data-hz-tags="Power Electronics,Grid-Connected Inverters,Control Systems,Passivity-Based Stability,Frequency Aliasing" data-hz-section="hust-research"></a>
## [评估并网跟随型逆变器奈奎斯特频率以上的延迟](https://doi.org/10.1109/apec51134.2026.11516799) ⭐️ 7.0/10

该论文量化了采样周期和采样时刻如何影响并网跟随型逆变器在奈奎斯特频率以上的输出导纳。论文还提出了一种考虑频率混叠的基于无源性的阻尼方法，实验验证了其能够改善高频稳定性。 研究结果阐明了采样相关延迟如何形成或加深负阻尼区域，并可能在高频下导致并网逆变器失稳。这为电力电子和控制研究人员设计阻尼控制提供了更精确的依据，尤其适用于高频相互作用显著的系统。 提高采样频率可以减轻奈奎斯特频率以上的部分非无源行为，但不能消除非无源性，而非无源性仍是高频失稳的重要原因。该分析区分了绝对延迟和相对延迟对负阻尼区域深度与带宽的影响。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 3月22日 00:00

**匹配依据**: 论文关键词命中 **grid-following**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 并网跟随型逆变器依靠控制环路与现有电网同步运行，并与电网交换电能。其输出导纳描述注入电流如何响应电压变化，因此可用于频域稳定性评估。奈奎斯特频率是采样频率的一半，超过这一上限的信号在采样后可能被错误表示，这种现象称为频率混叠。基于无源性的分析用于判断逆变器是否会向可能导致失稳的相互作用注入能量，而阻尼控制则用于减弱这类相互作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ieeexplore.ieee.org/document/11516799/">Passive-Based Assessment of Control Delays on Grid-Following ...</a></li>
<li><a href="https://www.tek.com/en/support/faqs/what-aliasing-and-how-do-i-detect-it-and-fix-it-my-oscilloscope">What is Aliasing? | Tektronix</a></li>

</ul>
</details>

**标签**: `#Power Electronics`, `#Grid-Connected Inverters`, `#Control Systems`, `#Passivity-Based Stability`, `#Frequency Aliasing`

---

<a id="item-5" class="hz-item-anchor" data-hz-url="https://doi.org/10.1016/j.ress.2026.113133" data-hz-title="关键基础设施最坏情况中断的模型与算法" data-hz-tags="Critical Infrastructure,Reliability Engineering,Resilience,Risk Analysis,Algorithms" data-hz-section="hust-research"></a>
## [关键基础设施最坏情况中断的模型与算法](https://doi.org/10.1016/j.ress.2026.113133) ⭐️ 7.0/10

该论文提出了用于识别和缓解关键基础设施系统最坏情况中断的模型与算法。现有信息未说明具体涉及哪些基础设施领域、采用了哪些算法或取得了怎样的评估结果。 最坏情况中断分析可以帮助可靠性工程师和基础设施规划者研究严重风险并制定缓解策略。这类方法可能支持韧性规划和风险分析，但根据现有的有限信息，尚无法评估论文的实际影响。 现有描述仅指出该研究围绕中断识别与缓解的模型和算法展开，未提供技术规格、假设、定量结果或局限性。该研究发表于《可靠性工程与系统安全》期刊。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 7月10日 00:00

**匹配依据**: 论文关键词命中 **critical infrastructure**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 关键基础设施系统是指其中断可能造成严重运行或社会后果的系统。可靠性工程研究系统持续运行的可能性，而韧性和风险分析关注系统如何承受中断及应对其后果。最坏情况分析重点研究特别严重的中断场景，而不仅是平均或典型事件。

**标签**: `#Critical Infrastructure`, `#Reliability Engineering`, `#Resilience`, `#Risk Analysis`, `#Algorithms`

---

<a id="item-6" class="hz-item-anchor" data-hz-url="https://doi.org/10.23919/csms.2025.0021" data-hz-title="融入共享快速公交车道的公交网络优化设计" data-hz-tags="Public Transit Optimization,BRT Lane Sharing,Network Design,Genetic Algorithms,Operations Research" data-hz-section="hust-research"></a>
## [融入共享快速公交车道的公交网络优化设计](https://doi.org/10.23919/csms.2025.0021) ⭐️ 7.0/10

该论文提出了一个显式纳入快速公交（BRT）车道共享的公交网络设计与频率设置双层模型，并设计了用于求解的基于优先级的遗传算法（PBGA）。在 Mandl 基准算例和临沂真实网络上的测试表明，该方法能够获得接近最优的结果，降低乘客和运营商成本，并提高 BRT 车道利用率。 通过允许普通公交在不干扰既有 BRT 运营的情况下使用 BRT 车道，该方法有望提升网络效率、运行速度、换乘便利性和资源利用率，同时降低成本。它将公交优化方法扩展到能够更准确反映现有 BRT 基础设施运营价值的场景。 研究通过新增 BRT 节点和 BRT 车道弧描述共享车道基础设施，并在 PBGA 中使用基于优先级的染色体、交叉算子和变异算子。论文结论来自基准网络和临沂网络实验，因此实际效果可能取决于当地网络结构、客流需求、运营规则以及模型假设。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 6月1日 00:00

**匹配依据**: 论文关键词命中 **bus transit**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 快速公交（BRT）是一种以公交车为基础、旨在提供更快速和高效服务的公共交通系统，通常会使用专用车道及其他优先通行设施。车道共享允许普通公交使用 BRT 车道，在保持既定 BRT 运营的同时提高基础设施利用率。公交双层设计模型通常将网络和班次决策与乘客路径选择或运营响应区分开来，从而共同描述这些相互影响的决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.transit.dot.gov/research-innovation/bus-rapid-transit">Bus Rapid Transit | FTA</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0191261514000812">Transit route and frequency design: Bi-level modeling and ...</a></li>

</ul>
</details>

**标签**: `#Public Transit Optimization`, `#BRT Lane Sharing`, `#Network Design`, `#Genetic Algorithms`, `#Operations Research`

---

<a id="item-7" class="hz-item-anchor" data-hz-url="https://doi.org/10.6084/m9.figshare.31910706" data-hz-title="概率分层匹配改进电动汽车调度" data-hz-tags="Electric vehicle scheduling,Optimization,Stochastic modeling,Smart grids,Transportation systems" data-hz-section="hust-research"></a>
## [概率分层匹配改进电动汽车调度](https://doi.org/10.6084/m9.figshare.31910706) ⭐️ 7.0/10

该文章提出了概率分层匹配（P-HM）方法，用于同时考虑行程时间不确定性和电网负荷的随机电动汽车调度。该方法将时刻表分层、基于兼容概率的匹配与贪心局部搜索相结合，以减少峰值负荷违规。 该方法同时优化车队规模、运营成本、充电峰值负荷和准点性能，处理了交通可靠性与用电需求之间的相互影响。这可能帮助公共交通运营商部署电动车队，同时减轻电网压力。 数值结果显示，P-HM 相比基准方法表现更好，尤其能够减少所需车队规模，同时该综合模型还能提升鲁棒性和电网安全性。现有内容未提供更广泛的验证细节，例如在多种网络、需求模式或真实运营环境中的测试结果。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 电动汽车调度问题是指在满足时刻表和车辆可用性等运营要求的同时，为各项行程分配电动汽车。在这一场景中，随机行程时间会改变车辆返回和充电的时间，可能导致充电需求在繁忙时段进一步增加。因此，电网负荷是重要因素，因为集中充电可能造成峰值负荷风险，相关电动公交调度研究也指出了这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/0305215X.2026.2643627">Probability-based hierarchical matching approach for ...</a></li>
<li><a href="https://ideas.repec.org/a/eee/transb/v155y2022icp322-347.html">The multi-depot electric vehicle scheduling problem with power grid ...</a></li>

</ul>
</details>

**标签**: `#Electric vehicle scheduling`, `#Optimization`, `#Stochastic modeling`, `#Smart grids`, `#Transportation systems`

---

<a id="item-8" class="hz-item-anchor" data-hz-url="https://doi.org/10.6084/m9.figshare.31910706.v1" data-hz-title="面向电网负荷的概率分层匹配电动汽车调度" data-hz-tags="Electric vehicles,Stochastic optimization,Power grid scheduling,Operations research,Transportation systems" data-hz-section="hust-research"></a>
## [面向电网负荷的概率分层匹配电动汽车调度](https://doi.org/10.6084/m9.figshare.31910706.v1) ⭐️ 7.0/10

该研究提出了概率分层匹配（P-HM）算法，用于同时考虑行程时间不确定性和电网负荷的随机电动汽车调度。其模型在提升准点表现的同时，联合优化车辆规模、运营成本和充电峰值负荷；数值实验显示，该方法优于基准方法。 该方法将不确定的行程时间与充电需求联系起来，弥补了将交通运营和电网安全割裂处理的调度模型的不足。它有望帮助公共交通运营者降低车辆规模和峰值负荷压力，同时提高调度方案对电力系统的可靠性。 P-HM 将时刻表划分为多个层级，并依据兼容概率匹配相邻层级，随后使用贪心局部搜索减少峰值负荷约束违规。现有证据主要来自数值实验，因此该方法在不同交通网络、充电设施和真实需求模式下的实际表现仍有待验证。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 随机电动汽车调度会考虑车辆行程时间等事件的不确定性，而不是假设每次行程都具有固定时长。这些不确定性可能改变车辆到达时间和充电需求，从而造成更高的用电峰值。分层匹配方法将时刻表元素组织成多个层级，并在相邻层级之间寻找兼容匹配；考虑电网的充电约束则有助于避免调度方案加重电力系统负荷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/290789277_A_probabilistic_model_for_vehicle_scheduling_based_on_stochastic_trip_times">A probabilistic model for vehicle scheduling based on stochastic ...</a></li>
<li><a href="https://ideas.repec.org/a/eee/transb/v102y2017icp55-82.html">A two-stage stochastic optimization model for scheduling electric vehicle charging loads to relieve distribution-system constraints</a></li>

</ul>
</details>

**标签**: `#Electric vehicles`, `#Stochastic optimization`, `#Power grid scheduling`, `#Operations research`, `#Transportation systems`

---

<a id="item-9" class="hz-item-anchor" data-hz-url="https://doi.org/10.23919/pcmp.2025.000294" data-hz-title="固体氧化物燃料电池系统控制目标与挑战综述" data-hz-tags="Solid Oxide Fuel Cells,Control Systems,Energy Systems,Power Engineering,Review Article" data-hz-section="hust-research"></a>
## [固体氧化物燃料电池系统控制目标与挑战综述](https://doi.org/10.23919/pcmp.2025.000294) ⭐️ 6.0/10

这篇综述研究了固体氧化物燃料电池系统运行中的控制目标、控制策略和开放性挑战。文章系统梳理了这一能源系统技术面临的控制问题。 有效的控制对于管理固体氧化物燃料电池系统的运行并支持其用于发电十分重要。这篇综述可以帮助研究人员比较能源系统控制和电力工程中的不同方法，但其与软件工程和人工智能的联系较为间接。 这篇论文关注系统级控制，而不是提出一种单一的新型控制器或展示一项实验性突破。相关控制问题包括管理能够产生电力和可用热能、采用固体陶瓷电解质，并作为一体化能源系统运行的燃料电池系统。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 7月1日 00:00

**匹配依据**: 论文关键词命中 **fuel cell**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 固体氧化物燃料电池不依赖电池内部燃烧，而是将燃料直接转化为电力和可用热能。它使用固体陶瓷电解质，氧离子会通过该电解质从空气电极，也就是阴极，移动到燃料电极，也就是阳极，并在那里与燃料发生反应。由于燃料电池属于一体化能源系统的一部分，控制策略需要协调其运行条件和整个系统的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gelanpetro.com/blog/what-is-sofc/">What Is a Solid Oxide Fuel Cell ( SOFC )? How It Works , Components...</a></li>
<li><a href="https://www.researchgate.net/publication/224254262_Control_of_an_energy_integrated_solid_oxide_fuel_cell_system">(PDF) Control of an energy integrated solid oxide fuel cell system</a></li>

</ul>
</details>

**标签**: `#Solid Oxide Fuel Cells`, `#Control Systems`, `#Energy Systems`, `#Power Engineering`, `#Review Article`

---

<a id="item-10" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560068" data-hz-title="结合改进ADRC与自适应谐波滤波的PMSM无位置传感器控制" data-hz-tags="PMSM control,Sensorless control,Active disturbance rejection control,Adaptive harmonic filtering,Motor drives" data-hz-section="hust-research"></a>
## [结合改进 ADRC 与自适应谐波滤波的 PMSM 无位置传感器控制](https://doi.org/10.1109/ccdc69976.2026.11560068) ⭐️ 6.0/10

该论文提出了一种永磁同步电机（PMSM）无位置传感器控制方法，将改进的自抗扰控制（ADRC）与并行自适应谐波滤波器相结合。该方法旨在不依赖机械转子位置传感器的情况下提升电机控制性能。 无位置传感器运行可以省去机械位置传感器，从而降低硬件成本并提高可靠性；ADRC 则用于实时估计和补偿综合扰动。如果经过实际驱动系统验证，这种组合方法可能改善 PMSM 控制系统的鲁棒性和跟踪性能，但现有信息尚不足以证明其具有广泛的产业影响。 该方法的主要技术组合是改进的 ADRC 与并行自适应谐波滤波，目标是抑制无位置传感器电机控制中的扰动及谐波相关影响。所提供的材料没有给出实验条件、量化结果、运行转速范围或与其他无位置传感器方法的对比，因此目前无法评估其性能提升幅度。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: PMSM 的转子使用永磁体，通常需要转子位置信息来实现控制。无位置传感器控制通过电气测量值估算转子位置，而不是使用专用机械传感器，这可以降低成本并减少潜在故障点，但也会增加位置估算难度。ADRC 将未建模动态和外部扰动视为综合扰动，并在控制过程中对其进行估计和补偿。自适应谐波滤波器用于识别或抑制变化的谐波成分，而并行结构可以同时处理多个与谐波相关的成分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mdpi.com/2032-6653/14/8/212">Overview of Position-Sensorless Technology for Permanent ...</a></li>
<li><a href="https://ieeexplore.ieee.org/document/10629494">Active Disturbance Rejection Control Of Permanent Magnet ...</a></li>
<li><a href="https://www.researchgate.net/publication/325403230_Decreasing_Harmonics_via_Three_Phase_Parallel_Active_Power_Filter_Using_Online_Adaptive_Harmonic_Injection_Algorithm">(PDF) Decreasing Harmonics via Three Phase Parallel Active Power...</a></li>

</ul>
</details>

**标签**: `#PMSM control`, `#Sensorless control`, `#Active disturbance rejection control`, `#Adaptive harmonic filtering`, `#Motor drives`

---

<a id="item-11" class="hz-item-anchor" data-hz-url="https://doi.org/10.1080/0305215x.2026.2643627" data-hz-title="概率层级匹配优化电动汽车调度与电网负荷" data-hz-tags="Electric Vehicles,Stochastic Optimization,Power Grid Security,Transportation Scheduling,Operations Research" data-hz-section="hust-research"></a>
## [概率层级匹配优化电动汽车调度与电网负荷](https://doi.org/10.1080/0305215x.2026.2643627) ⭐️ 6.0/10

该论文提出一种考虑电网负荷的随机电动汽车调度概率层级匹配（P-HM）方法，联合优化车队规模、运营成本、充电峰值负荷和准时性。该方法将时刻表划分为多个层级，依据兼容概率匹配相邻层级，并结合贪心局部搜索减少峰值负荷违规。 通过将不确定的行程时间与充电需求联系起来，该模型处理了可能降低公共交通调度可靠性并加剧电网峰值负荷的相互影响。论文结果表明，协调调度有望在减少车队规模的同时提升系统稳健性和电网安全性。 研究报告称，P-HM 在多个基准方法中表现更好，尤其是在减少车队规模方面；贪心局部搜索则用于处理充电峰值负荷违规。现有摘要没有给出具体基准数值、测试网络特征或计算运行时间，因此目前无法独立评估改进幅度及其普适性。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 电动汽车调度问题是指为计划行程分配电动汽车，同时确保车辆能够完成路线并在需要时充电。随机调度使用概率表示可变行程时间等不确定情况，而不是把这些因素视为固定值。如果大量车辆在同一时间充电，就可能形成需求峰值，给电网带来压力，并限制可行的交通调度方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/0305215X.2026.2643627">Probability-based hierarchical matching approach for ...</a></li>
<li><a href="https://www.osti.gov/pages/biblio/1362132">A two-stage stochastic optimization model for scheduling electric vehicle charging loads to relieve distribution-system constraints (Journal Article) | OSTI.GOV</a></li>

</ul>
</details>

**标签**: `#Electric Vehicles`, `#Stochastic Optimization`, `#Power Grid Security`, `#Transportation Scheduling`, `#Operations Research`

---

<a id="item-12" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560295" data-hz-title="用于永磁同步电机动态切换的级联双代价函数模型预测控制" data-hz-tags="Model Predictive Control,Permanent Magnet Synchronous Motors,Motor Control,Power Electronics" data-hz-section="hust-research"></a>
## [用于永磁同步电机动态切换的级联双代价函数模型预测控制](https://doi.org/10.1109/ccdc69976.2026.11560295) ⭐️ 5.0/10

该论文提出了一种面向永磁同步电机、结合动态切换的级联双代价函数模型预测控制策略。该方法将两个依次执行的代价函数与控制模式或控制目标之间的切换结合起来。 改进代价函数设计和切换逻辑，有望帮助基于模型预测控制的永磁同步电机驱动系统更有效地平衡动态响应、转矩性能和控制目标。该成果主要与高性能电机控制和电力电子应用相关，对更广泛的软件生态影响有限。 相关的永磁同步电机双代价函数研究会依次使用两个级联代价函数，而预测控制则通过在电机模型上优化代价函数来选择控制动作。现有信息没有提供该论文的定量结果、硬件验证细节、切换判据或计算复杂度测量结果。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 永磁同步电机是一种利用永磁体产生转子磁场的电机，常用于需要高效、精确驱动控制的场景。模型预测控制会预测电机的未来行为，并通过优化预先定义的代价函数来选择控制动作。双代价函数设计会依次应用两个控制目标，而动态切换则根据运行状态改变当前采用的控制决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/342760225_Dual_Cost_Function_Model_Predictive_Direct_Speed_Control_with_Duty_Ratio_Optimization_for_PMSM_Drives">(PDF) Dual Cost Function Model Predictive Direct Speed Control ...</a></li>
<li><a href="https://ieeexplore.ieee.org/document/10396018">Model Predictive Control For Permanent Magnet Synchronous ...</a></li>

</ul>
</details>

**标签**: `#Model Predictive Control`, `#Permanent Magnet Synchronous Motors`, `#Motor Control`, `#Power Electronics`

---

<a id="item-13" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560172" data-hz-title="车辆调度的层级匹配方法" data-hz-tags="vehicle scheduling,matching algorithms,operations research,optimization,transportation systems" data-hz-section="hust-research"></a>
## [车辆调度的层级匹配方法](https://doi.org/10.1109/ccdc69976.2026.11560172) ⭐️ 5.0/10

该论文提出了一种基于层级匹配的车辆调度问题求解方法。现有信息未说明该算法的具体实现、评估设置或报告的性能。 车辆调度需要将车辆分配给预先确定的行程，同时控制资本成本和运营成本，因此更好的匹配方法可能有助于提升交通规划效率。不过，仅凭现有摘要信息还无法判断该论文的实际影响。 相关车辆调度研究曾将部分单车场变体建模为非对称分配模型，而更广泛的路径规划与调度问题可能具有较高的计算难度，并需要采用近似方法。现有信息没有说明该层级结构是否改善了解的质量、运行时间、可扩展性或鲁棒性。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 车辆调度是将车辆分配给一组预先确定的行程，这些行程具有固定的开始和结束时间。其常见目标包括最小化资本成本和运营成本。车辆调度不同于车辆路径规划，后者通常更明确地关注行驶顺序和路线设计，并经常受到时间窗等约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubsonline.informs.org/doi/abs/10.1287/trsc.35.2.165.10135">Models and Algorithms for Single-Depot Vehicle Scheduling</a></li>

</ul>
</details>

**标签**: `#vehicle scheduling`, `#matching algorithms`, `#operations research`, `#optimization`, `#transportation systems`

---

<a id="item-14" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11559800" data-hz-title="公交网络与时刻表协同设计" data-hz-tags="Transportation Optimization,Public Transit,Timetable Scheduling,Network Design,Operations Research" data-hz-section="hust-research"></a>
## [公交网络与时刻表协同设计](https://doi.org/10.1109/ccdc69976.2026.11559800) ⭐️ 5.0/10

该研究考察了一种综合方法，将公交网络设计与多模式公共交通系统中的时刻表同步结合起来。其目标是改善不同交通方式之间的协调。 协调公交线路与其他交通方式的时刻表，有望减少换乘衔接问题并提高公共交通规划的整体效率。该研究主要适用于交通管理机构和运筹学实践者，对一般软件或人工智能开发的直接影响较为有限。 现有信息没有提供该论文的具体优化模型、数据集、算法或性能提升指标。相关的多模式公共交通研究通常会将网络设计与时刻表同步视为相互关联的规划决策，但在没有全文的情况下，不能将这些细节归因于本研究。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **timetable**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 多模式公共交通系统将公交车和地铁等不同公共交通方式结合起来。网络设计决定线路和连接方式，时刻表同步则协调车辆的出发与到达时间，使不同交通方式之间的换乘更加顺畅。将这些决策整合起来，意味着要同时考虑公交网络的结构和服务运行时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1366554524004010">Resilience enhancement of multi-modal public transportation ...</a></li>

</ul>
</details>

**标签**: `#Transportation Optimization`, `#Public Transit`, `#Timetable Scheduling`, `#Network Design`, `#Operations Research`

---

## 其他资讯

15. [伊萨尔航天第二次飞行成功入轨](#item-15) ⭐️ 9.0/10
16. [Anubis 用一年时间交付兼容性 WebAssembly](#item-16) ⭐️ 8.0/10
17. [OpenAI 探索用人工智能代理自动化研究](#item-17) ⭐️ 8.0/10
18. [Asahi Linux 正式支持 Apple M3 Mac](#item-18) ⭐️ 8.0/10
19. [人工智能可能比我们想象的更难控制](#item-19) ⭐️ 8.0/10
20. [使用大语言模型写作可能暴露你的思想缺口](#item-20) ⭐️ 8.0/10
21. [OpenAI 研究人员的编码代理支出激增](#item-21) ⭐️ 8.0/10
22. [GPT-6 Astra 提升提示理解与三维模型生成能力](#item-22) ⭐️ 8.0/10
23. [Axis Robotics 开源大型 Franka 仿真数据集](#item-23) ⭐️ 8.0/10
24. [加州大学伯克利分校发布开放平台 CUA-Lite](#item-24) ⭐️ 8.0/10
25. [IFM 发布 K2 Horizon 开放模型系列](#item-25) ⭐️ 8.0/10
26. [新通用顶级域名暴露大规模诈骗问题](#item-26) ⭐️ 7.0/10
27. [据报道 Kimsuky 利用人工智能编程代理批量生产恶意软件](#item-27) ⭐️ 7.0/10
28. [Kimsuky 被指利用人工智能代理发动韩国网络攻击](#item-28) ⭐️ 7.0/10
29. [NVIDIA 为开源 Nova 驱动加入 vGPU 支持](#item-29) ⭐️ 7.0/10
30. [《西雅图时报》和《新闻日报》起诉 OpenAI 与微软](#item-30) ⭐️ 6.0/10
31. [遗留系统重写为何经常失败](#item-31) ⭐️ 6.0/10
32. [资产价格变化重塑资本利得税与财富税分析](#item-32) ⭐️ 6.0/10
33. [人工智能风险上升之际，网络保险费率却持续下降](#item-33) ⭐️ 6.0/10
34. [澳大利亚拟允许用户关闭社交媒体算法](#item-34) ⭐️ 6.0/10
35. [开源 Fin-Ray 夹爪支持多机器人操作](#item-35) ⭐️ 6.0/10
36. [CrowdStrike 推出基于 NVIDIA Nemotron 的 SafeMind 网络安全人工智能系统](#item-36) ⭐️ 6.0/10
37. [仿鱼鳍软夹爪支持多机器人抓取](#item-37) ⭐️ 6.0/10
38. [Perplexity 首席执行官推出开源工具 Numbat 追踪失控 AI 代理](#item-38) ⭐️ 6.0/10
39. [人工智能应用周度观察](#item-39) ⭐️ 5.0/10
40. [德国选择党在萨克森-安哈尔特州的增长引发欧洲警报](#item-40) ⭐️ 5.0/10
41. [Hugging Face 推出开源 Microduck 机器人](#item-41) ⭐️ 5.0/10
42. [OpenTrailPaper 将 LILYGO 硬件变成自行车电脑](#item-42) ⭐️ 5.0/10
43. [CrowdStrike 推出面向防御者的 SafeMind 智能网络安全系统](#item-43) ⭐️ 5.0/10
44. [Microduck 机器人四天预订量突破一万](#item-44) ⭐️ 5.0/10

---

<a id="item-15" class="hz-item-anchor" data-hz-url="https://isaraerospace.com/press/history-for-european-spaceflight-isar-aerospace-reaches-orbit-and-deploys-payloads-on-second-flight" data-hz-title="伊萨尔航天第二次飞行成功入轨" data-hz-tags="spaceflight,aerospace,commercial-launch,European-space-industry,orbital-launch" data-hz-section="other"></a>
## [伊萨尔航天第二次飞行成功入轨](https://isaraerospace.com/press/history-for-european-spaceflight-isar-aerospace-reaches-orbit-and-deploys-payloads-on-second-flight) ⭐️ 9.0/10

伊萨尔航天的“光谱”火箭在第二次飞行中成功入轨并部署了有效载荷，这次任务同时是该运载火箭的鉴定飞行，也是它首次搭载有效载荷飞行。任务完成了最大动压段、主发动机关闭、级间分离、第二级点火和整流罩分离，随后达到轨道速度。 这一成果为欧洲新兴商业发射行业提供了重要的已验证能力，并可能为商业和机构客户扩大可用的发射选择。它也加强了欧洲争取更自主进入太空的努力，但社区讨论指出，欧洲在发射频率和发展策略上仍与美国存在差异。 “光谱”是一种两级液体燃料小型运载火箭，设计用于发射卫星，而第二次任务被定义为鉴定飞行，而不是常规商业运营任务。现有报道显示，这只是伊萨尔航天的第二次飞行，因此这一成就本身还不能证明其已经具备成熟或高频的发射能力。

hackernews · mpweiher · 9月6日 07:21 · [社区讨论](https://news.ycombinator.com/item?id=49584083)

**背景**: 伊萨尔航天是一家成立于 2018 年、总部位于慕尼黑附近的德国航天公司。它的“光谱”火箭用于发射小型卫星，而鉴定飞行是为了检验火箭系统是否按设计运行，然后再进入常规服务。成功入轨意味着火箭达到了足够的速度和轨道路径，使有效载荷能够留在太空中，而不是重新坠回地球。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://isaraerospace.com/press/history-for-european-spaceflight-isar-aerospace-reaches-orbit-and-deploys-payloads-on-second-flight">History for European spaceflight: Isar Aerospace reaches ...</a></li>
<li><a href="https://isaraerospace.com/mission-2">Isar Aerospace - Isar Aerospace</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isar_Aerospace">Isar Aerospace - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论总体上表示祝贺，并将此次飞行视为扩大太空进入能力、加强欧洲发射行业的重要一步。评论者还讨论了欧洲偏重少量发射和可靠性的路线与美国偏重高频发射和试错的路线之间的差异；另一些人则质疑“自主进入太空”的表述是否忽视了阿丽亚娜航天，并指出伊萨尔航天与拥有丰富经验的太空探索技术公司前员工及欧洲投资者之间的联系。

**标签**: `#spaceflight`, `#aerospace`, `#commercial-launch`, `#European-space-industry`, `#orbital-launch`

---

<a id="item-16" class="hz-item-anchor" data-hz-url="https://anubis.techaro.lol/blog/2026/anubis-wasm/" data-hz-title="Anubis 用一年时间交付兼容性 WebAssembly" data-hz-tags="WebAssembly,Browser Compatibility,Rust,Open Source,Security" data-hz-section="other"></a>
## [Anubis 用一年时间交付兼容性 WebAssembly](https://anubis.techaro.lol/blog/2026/anubis-wasm/) ⭐️ 8.0/10

Anubis 介绍了为交付向后兼容的 WebAssembly 实现而进行的一年努力。下一版本将允许管理员在阈值或机器人规则中启用基于工作量证明的检查。 这篇文章展示了在生产环境的安全工具中部署 WebAssembly 有多困难，因为项目必须同时保证浏览器兼容性和工具链行为的可预测性。它也凸显了所谓稳定的编译器目标发生变化时，开源项目维护者需要承担的额外负担。 Anubis 需要考虑包括 Chrome 66 在内的较旧浏览器目标，还要应对 Rust 的 wasm32-unknown-unknown 目标所生成特性发生意外变化的问题。讨论还强调，如果挑战需要 WebAssembly，网站应明确告知用户，尤其是当用户在浏览器中禁用了该功能时。

hackernews · xena · 9月6日 20:32 · [社区讨论](https://news.ycombinator.com/item?id=49590611)

**背景**: WebAssembly 是一种可移植的二进制格式，旨在让代码与 JavaScript 一起在浏览器中运行。Web 平台希望 WebAssembly 保持无版本化并向后兼容，但实际兼容性取决于浏览器支持哪些特性，以及工具链会生成哪些特性。Anubis 使用 WebAssembly 执行基于工作量证明的检查，帮助管理员区分自动化请求与其他流量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://anubis.techaro.lol/blog/2026/anubis-wasm/">It took a year to ship WebAssembly in Anubis | Anubis</a></li>
<li><a href="https://webassembly.org/">WebAssembly</a></li>

</ul>
</details>

**社区讨论**: 社区总体认可 Anubis 对兼容性的谨慎处理以及坦率的文章风格，评论者还分享了 Rust 和 WebAssembly 特性稳定性方面的类似经历。其他人则关注用户控制权和可访问性，希望网站在需要 WebAssembly 时给出明确提示，并提供便捷的浏览器兼容性测试方式；也有人建议使用变化较慢或与目标时期匹配的工具链。

**标签**: `#WebAssembly`, `#Browser Compatibility`, `#Rust`, `#Open Source`, `#Security`

---

<a id="item-17" class="hz-item-anchor" data-hz-url="https://openai.com/index/research-acceleration-view-inside-openai" data-hz-title="OpenAI探索用人工智能代理自动化研究" data-hz-tags="AI research,AI agents,recursive self-improvement,AI safety,research automation" data-hz-section="other"></a>
## [OpenAI 探索用人工智能代理自动化研究](https://openai.com/index/research-acceleration-view-inside-openai) ⭐️ 8.0/10

OpenAI 介绍了如何将能力不断增强的人工智能代理用作受监督的研究助手，并探索自动化深度学习和对齐研究的重要环节。其目标是构建能够在人类指导下完成明确研究任务的自动化人工智能研究员，包括原本可能需要熟练研究人员数天完成的工作。 如果这些系统变得可靠，它们可能提高研究效率，同时加快人工智能能力和人工智能安全领域的进展。这种方法还可能形成反馈循环，让更强的人工智能研究员推动更强系统的发展，但也会引发监督难度和加速人工智能进步风险等问题。 这些研究助手被描述为受监督的系统，而不是完全自主的研究员；社区讨论提到其推理成本很高，包括按应用程序接口价格计算的研究人员每日中位数超过 600 美元，以及另一条评论提到的每日约 8000 美元。讨论还指出，OpenAI 使用了“递归自我改进”这一概念的缩写“RSI”，却没有为不熟悉该术语的读者作出解释。

hackernews · iamsyr · 9月6日 15:08 · [社区讨论](https://news.ycombinator.com/item?id=49587217)

**背景**: 人工智能对齐是一个研究问题，重点是让人工智能系统可靠地追求人类设定的目标，并持续符合人类的价值观或要求。递归自我改进，即“RSI”，指系统提升自身智能，或提升继续进行改进的能力，从而可能形成不断增强的循环。在这一语境中，人工智能代理是能够通过工具或其他行动执行任务的系统，而人类研究人员负责提供方向和监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/research/automated-alignment-researchers">Automated Alignment Researchers : Using large language models to...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论总体上既感兴趣又保持谨慎：评论者认为，这可能是通向类似“AI 2027”式迭代改进的一条现实路径，但也质疑其高昂的运行成本、研究人员如何追踪代理生成的工作，以及“为了防御不断进步的人工智能而继续推进人工智能”这一安全论证是否存在悖论。其他评论还指出文章对“RSI”的使用不够清晰，并分享了长时间无人值守运行人工智能代理任务的个人经历。

**标签**: `#AI research`, `#AI agents`, `#recursive self-improvement`, `#AI safety`, `#research automation`

---

<a id="item-18" class="hz-item-anchor" data-hz-url="https://asahilinux.org/2026/09/m2-episode-1/" data-hz-title="Asahi Linux 正式支持 Apple M3 Mac" data-hz-tags="Asahi Linux,Apple Silicon,Linux,ARM64,Hardware Reverse Engineering" data-hz-section="other"></a>
## [Asahi Linux 正式支持 Apple M3 Mac](https://asahilinux.org/2026/09/m2-episode-1/) ⭐️ 8.0/10

Asahi Linux 已正式加入对搭载 Apple M3、M3 Pro 和 M3 Max 芯片的 Mac 支持，并通过安装程序提供相应支持。这一进展将 Linux 兼容范围扩展到新一代 Apple Silicon 硬件，但部分重要组件仍未完成。 由于 Apple 没有为这些系统提供完整的 Linux 支持，每一代新 Apple Silicon 芯片都需要大量硬件逆向工程工作。这项成果让新款 Mac 用户有了运行 Linux 的正式途径，也展示了开源开发者如何在缺乏厂商支持的情况下扩展 ARM64 兼容性。 M3 版本目前仍缺乏完善的 GPU 支持，并且由于缺少必要的 DCP 支持而暂不支持睡眠功能；社区讨论还指出 HDMI 支持缺失是阻碍用户采用的重要问题。因此，这是一项重大的兼容性里程碑，但还不是成熟完善的桌面 Linux 体验。

hackernews · mdp2021 · 9月6日 14:08 · [社区讨论](https://news.ycombinator.com/item?id=49586698)

**背景**: Asahi Linux 是一个开源项目，通过硬件逆向工程和开发新驱动，让 Linux 运行在 Apple Silicon Mac 上。Apple Silicon 指 Apple 设计的基于 ARM 的系统级芯片，而 M3 系列属于更新一代硬件，需要开发者研究尚未完整公开文档的硬件接口。安装程序正式支持意味着用户可以按照受支持的流程安装系统，但并不代表所有硬件功能都已可用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Asahi-Linux-Official-M3">Asahi Linux Now Officially Supports Apple M 3 Macs... - Phoronix</a></li>
<li><a href="https://www.igeeksblog.com/asahi-linux-m3-support/">Asahi Linux now supports M 3 Macs, but GPU support is still missing...</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上赞赏这项工程成就，但也对必须依靠逆向工程以及 Apple 没有更多直接参与感到遗憾。他们指出睡眠和 HDMI 支持缺失会实际阻碍用户采用，同时有评论提到社区正尝试利用 AI 加快更新一代 Apple Silicon 硬件的驱动开发。

**标签**: `#Asahi Linux`, `#Apple Silicon`, `#Linux`, `#ARM64`, `#Hardware Reverse Engineering`

---

<a id="item-19" class="hz-item-anchor" data-hz-url="https://openai.com/index/an-alien-mind/" data-hz-title="人工智能可能比我们想象的更难控制" data-hz-tags="AI alignment,AI safety,AI governance,frontier models,machine intelligence" data-hz-section="other"></a>
## [人工智能可能比我们想象的更难控制](https://openai.com/index/an-alien-mind/) ⭐️ 8.0/10

OpenAI 的文章《An Alien Mind》认为，能力不断增强的人工智能系统可能始终难以被人类充分理解、监测和对齐。文章警告，在任何实验室都尚未建立足够可靠的安全保障时，继续快速扩展前沿模型需要更加谨慎。 如果能力增长速度超过监测和对齐能力，开发者与政策制定者可能无法在系统广泛部署前发现并纠正危险行为。这一观点直接关系到前沿模型开发、自愿放缓、人工智能治理，以及竞争压力是否足以支持继续快速扩展的争论。 文章将人工智能描述为一种可能具有“异质性”的智能形态，而不只是更快的人类推理，因此其行为理解和可靠监督尤其困难。文章的核心判断是，目前没有任何实验室将对齐和监测问题解决到足以支持长期全速扩展的程度，但也承认有人主张继续建设能力更强的防御系统，以应对其他人工智能带来的风险。

hackernews · tosh · 9月6日 16:27 · [社区讨论](https://news.ycombinator.com/item?id=49588080)

**背景**: 人工智能对齐是指让人工智能系统追求人类真正意图所对应的目标、偏好或伦理原则。监测和评估是用于观察高能力系统、测试其行为，并在部署前或部署过程中识别风险的安全实践。前沿模型是能力最强的一类人工智能系统，因此随着能力提升，这些环节的失效可能带来更严重的后果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>
<li><a href="https://metr.org/common-elements">Common Elements of Frontier AI Safety Policies - METR</a></li>

</ul>
</details>

**社区讨论**: 社区讨论既有严肃担忧，也有讽刺和推测。评论者争论人工智能军备竞赛是否足以为快速扩展提供理由，质疑机构和企业决策背后的激励机制，并讨论开源模型和中国模型带来的影响；一些评论还强调文章呼吁自愿放缓，同时担心人类可能无法有效协调行动。

**标签**: `#AI alignment`, `#AI safety`, `#AI governance`, `#frontier models`, `#machine intelligence`

---

<a id="item-20" class="hz-item-anchor" data-hz-url="https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/" data-hz-title="使用大语言模型写作可能暴露你的思想缺口" data-hz-tags="LLMs,AI ethics,writing,authorship,human-computer interaction" data-hz-section="other"></a>
## [使用大语言模型写作可能暴露你的思想缺口](https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/) ⭐️ 8.0/10

2025 年 12 月 5 日，一篇文章指出，使用大语言模型代写文章可能削弱作者的思考过程、个人风格以及读者的信任。文章还引发了关于是否应披露大语言模型参与，以及应如何理解作者身份的讨论。 这个问题影响所有使用大语言模型撰写电子邮件、博客文章、设计文档或其他公开文字的人，因为写作不仅记录观点，也可能促使作者改变和澄清观点。这场讨论还涉及个人真实表达的价值，以及署名所代表的信任关系。 社区评论者强调，写作会将思绪逐步展开并迫使作者作出判断，而大语言模型生成的文字可能掩盖作者自身的推理过程和独特风格。另一些评论则质疑，要求披露究竟是因为当前大语言模型写作能力有限，还是因为读者有更根本的知情权，需要知道文字究竟由谁或什么生成。

hackernews · cyb0rg0 · 9月6日 11:56 · [社区讨论](https://news.ycombinator.com/item?id=49585644)

**背景**: 大语言模型是一种根据从大量数据中学习到的模式生成文字的语言模型。在这场讨论中，“撰写”文章指依靠大语言模型生成大部分文字，而不仅仅是进行少量编辑。署名通常意味着特定的人对作品负责，因此未披露大语言模型的参与会引发关于文风、责任和信任的问题。

**社区讨论**: 评论整体上认真讨论了文章提出的问题，但对原因有不同侧重。几位评论者强调写作本身就是思考过程，并认为保留个人特色很重要；另一些人指出，即使大语言模型未来显著提升写作能力，披露仍可能很重要。还有评论用餐厅用餐作比喻，说明机器生成的文字可能带来额外的期待和失望。

**标签**: `#LLMs`, `#AI ethics`, `#writing`, `#authorship`, `#human-computer interaction`

---

<a id="item-21" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/" data-hz-title="OpenAI研究人员的编码代理支出激增" data-hz-tags="OpenAI,AI research,coding agents,recursive self-improvement,research productivity" data-hz-section="other"></a>
## [OpenAI 研究人员的编码代理支出激增](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 8.0/10

Simon Willison 重点介绍了 OpenAI 的研究加速计划，并指出每位研究人员用于编码代理的支出已从 2026 年 6 月的大约 150 美元上升到 8 月底的约 600 美元。他推测，7 月底的急剧增长可能发生在内部员工获得后来发布为 GPT-6 Astra 的模型之后。 这一趋势表明，编码代理正成为研究人员日常工作的重要组成部分，OpenAI 也愿意在研究领域投入更多人工智能资源。如果这些工具能够提升研究人员构建和评估系统的能力，就可能加速 OpenAI 相关材料中所讨论的递归自我改进。 图表显示，每位研究人员的每日中位支出在 2 月接近于零，6 月达到约 150 美元，随后在 2026 年 8 月底陡增至约 600 美元。摘录并未确定 7 月底加速增长的原因，因此将其与 GPT-6 Astra 联系起来仍属于推测，而不是已证实的解释。

rss · Simon Willison · 9月6日 23:57

**背景**: 编码代理是能够自主编写、修改、调试和重构代码，并在整个代码库中处理多步骤任务的软件工具。代理式工程强调运用工程专业知识来指导和监督这些代理，而不是只把它们当作简单的代码补全工具。递归自我改进是指人工智能系统改进自身能力，而这些能力又帮助系统产生更多改进的反馈循环；不过，开放式递归自我改进仍受到评估和计算资源限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is Agentic Engineering? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2607.07663">[2607.07663] Recursive Self-Improvement in AI: From Bounded ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI research`, `#coding agents`, `#recursive self-improvement`, `#research productivity`

---

<a id="item-22" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/5/introducing-gpt-6-astra-for-developers/" data-hz-title="GPT-6 Astra提升提示理解与三维模型生成能力" data-hz-tags="AI,OpenAI,generative AI,LLMs,developer tools" data-hz-section="other"></a>
## [GPT-6 Astra 提升提示理解与三维模型生成能力](https://simonwillison.net/2026/Sep/5/introducing-gpt-6-astra-for-developers/) ⭐️ 8.0/10

OpenAI 推出了 GPT-6 Astra，Simon Willison 指出它在细节关注、提示理解和复杂输出方面都有提升。该模型尤其擅长生成详细的三维场景，包括花园、船厂、动物、城市景观和戴森球。 更可靠的提示理解能力和更强的三维生成能力，可能帮助开发者自动化视觉原型设计、互动内容创作以及使用 Blender 等工具的工作流程。OpenAI 将 Astra 定位为可用于复杂推理、编程、计算机操作、研究和文档创作的模型，因此它的潜在影响不局限于聊天应用。 OpenAI API 页面显示，GPT-6 Astra 支持低、中、高、超高和最大等推理强度，并拥有 105 万令牌的上下文窗口和 12.8 万令牌的最大输出长度。现有示例主要是观察性演示，因此尚不能证明其具体性能提升、生产环境可靠性或生成三维资产的专业质量。

rss · Simon Willison · 9月5日 23:27

**背景**: 大型语言模型能够理解用户提示，并生成文本、代码或其他结构化输出。这里的讨论重点是利用模型创建三维场景，并可能通过编码代理操作 Blender 等工具。上下文窗口决定模型一次可以处理多少输入内容，而推理强度则控制模型为任务分配的计算程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/models/gpt-6-astra">GPT-6 Astra Model | OpenAI API</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://til.simonwillison.net/llms/blender-coding-agents-macos">Using Blender with coding agents on macOS | Simon Willison’s TILs</a></li>

</ul>
</details>

**标签**: `#AI`, `#OpenAI`, `#generative AI`, `#LLMs`, `#developer tools`

---

<a id="item-23" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMihwFBVV95cUxQMERYUU5pVk9fdTV1b0FzQ1BUYk5uTXdvNEpaQXdGTG5xNmNEaUhiY1NTakh3Rk16dkZDOFFWOWhRSWdQVURXTTJsd1RRZ1ptSWo1TWxlcXJVWFBvamp1S0Zrb1duQlJPUUNKSmxUWjhfZTQ2OTJpbUt2Ni1yUGZ3TUpZcGRsdmM?oc=5" data-hz-title="Axis Robotics 开源大型 Franka 仿真数据集" data-hz-tags="Physical AI,Robotics,Simulation,Datasets,Sim-to-Real Learning" data-hz-section="other"></a>
## [Axis Robotics 开源大型 Franka 仿真数据集](https://news.google.com/rss/articles/CBMihwFBVV95cUxQMERYUU5pVk9fdTV1b0FzQ1BUYk5uTXdvNEpaQXdGTG5xNmNEaUhiY1NTakh3Rk16dkZDOFFWOWhRSWdQVURXTTJsd1RRZ1ptSWo1TWxlcXJVWFBvamp1S0Zrb1duQlJPUUNKSmxUWjhfZTQ2OTJpbUt2Ni1yUGZ3TUpZcGRsdmM?oc=5) ⭐️ 8.0/10

Axis Robotics 发布了面向 Franka 机械臂的公开仿真数据集之一，旨在支持具身智能研究与开发。公告没有说明数据集的确切规模或完整内容。 大规模开放数据集可以降低机器人研究门槛，尤其有助于模仿学习、策略训练和仿真到现实实验。它还可能提升基于广泛使用的 Franka 平台构建的操作系统的可复现性与基准测试能力。 现有搜索结果显示，类似的 Franka 仿真数据集可以包含 RGB 图像和逐回合 JSON 日志，但这些结果无法确认 Axis Robotics 数据集具体提供哪些数据模态或任务类型。该数据集的实际价值将取决于任务多样性、许可协议、仿真保真度，以及策略向真实硬件迁移的效果。

google_news · Yellow.com · 9月7日 05:09

**背景**: 仿真数据集记录机器人在虚拟环境中的操作经历，例如图像、动作和回合日志，使模型无需反复操作实体硬件即可进行训练。仿真到现实学习是指先在仿真环境中训练或改进机器人行为，再将其迁移到真实机器人上；两个环境之间的差异可能造成性能落差。Franka 机械臂常用于操作研究，因此针对该平台的数据集有助于比较不同方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/datasets/MEID0/franka-episodes-v1">MEID0/ franka -episodes-v1 · Datasets at Hugging Face</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2212827121009550">An architecture for sim-to-real and real-to-sim ...</a></li>

</ul>
</details>

**标签**: `#Physical AI`, `#Robotics`, `#Simulation`, `#Datasets`, `#Sim-to-Real Learning`

---

<a id="item-24" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMi_AFBVV95cUxPb2ptQW1OVU5xYzBvYzdTUDNVSGZXQm40cjBHWUlRaXdtYXpvX1k2R1l1ZWY3c2ZXMENEODkxY1A2OEhMWWVYdU5sZ1NHWGZxdG83WjdtXy14SmFLY1c3MXRqMmFFZnNwOXYtNUxUUm5Sa1hfeVNkSjBfbnNVaFg3NVJ6R0JpcW9IM0t2QVQ2OVktNE5Vd3ZaNjBaN3RJdUFRNDJodjRqd0FaYjVYUWtNTk1QeWdwQ0NuNGV2YXVpeXBNdGVGdi1mS3pOeTZlRmRvTjRDQnJJZ0pCaU5LTDViQkFEeEtrd2h2VW1RSUNRTHdJSEtULUM3RXE0bFHSAfwBQVVfeXFMT29qbUFtTlVOcWMwb2M3U1AzVUhmV0JuNHIwR1lJUWl3bWF6b19ZNkdZdWVmN3NmVzBDRDg5MWNQNjhITFllWHVObGdTR1hmcXRvN1o3bV8teEphS2NXNzF0ajJhRWZzcDl2LTVMVFJuUmtYX3lTZEowX25zVWhYNzVSekdCaXFvSDNLdkFUNjlZLTROVXd2WjYwWjd0SXVBUTQyaHY0andBWmI1WFFrTU5NUHlncENDbjRldmF1aXlwTXRlRnYtZkt6Tnk2ZUZkb040Q0JySWdKQmlOS0w1YkJBRHhLa3dodlVtUUlDUUx3SUhLVC1DN0VxNGxR?oc=5" data-hz-title="加州大学伯克利分校发布开放平台 CUA-Lite" data-hz-tags="Computer-Use Agents,Reinforcement Learning,AI Infrastructure,Evaluation,Open Source" data-hz-section="other"></a>
## [加州大学伯克利分校发布开放平台 CUA-Lite](https://news.google.com/rss/articles/CBMi_AFBVV95cUxPb2ptQW1OVU5xYzBvYzdTUDNVSGZXQm40cjBHWUlRaXdtYXpvX1k2R1l1ZWY3c2ZXMENEODkxY1A2OEhMWWVYdU5sZ1NHWGZxdG83WjdtXy14SmFLY1c3MXRqMmFFZnNwOXYtNUxUUm5Sa1hfeVNkSjBfbnNVaFg3NVJ6R0JpcW9IM0t2QVQ2OVktNE5Vd3ZaNjBaN3RJdUFRNDJodjRqd0FaYjVYUWtNTk1QeWdwQ0NuNGV2YXVpeXBNdGVGdi1mS3pOeTZlRmRvTjRDQnJJZ0pCaU5LTDViQkFEeEtrd2h2VW1RSUNRTHdJSEtULUM3RXE0bFHSAfwBQVVfeXFMT29qbUFtTlVOcWMwb2M3U1AzVUhmV0JuNHIwR1lJUWl3bWF6b19ZNkdZdWVmN3NmVzBDRDg5MWNQNjhITFllWHVObGdTR1hmcXRvN1o3bV8teEphS2NXNzF0ajJhRWZzcDl2LTVMVFJuUmtYX3lTZEowX25zVWhYNzVSekdCaXFvSDNLdkFUNjlZLTROVXd2WjYwWjd0SXVBUTQyaHY0andBWmI1WFFrTU5NUHlncENDbjRldmF1aXlwTXRlRnYtZkt6Tnk2ZUZkb040Q0JySWdKQmlOS0w1YkJBRHhLa3dodlVtUUlDUUx3SUhLVC1DN0VxNGxR?oc=5) ⭐️ 8.0/10

加州大学伯克利分校研究人员发布了 CUA-Lite，这是一个将沙箱、数据集、评测、监督微调和强化学习统一起来的计算机使用代理开放平台。该平台包含超过 3 万个可验证任务和 10 多个统一的监督微调数据集。 通过将关键研究组件整合到同一框架中，CUA-Lite 有望提高计算机使用代理训练和基准测试的效率与可复现性。它还可能降低研究人员在不同数据集、环境和学习方法之间比较代理时的基础设施负担。 CUA-Lite 使用统一的动作空间和数据格式，轻量级模型适配器可以将标准化样本转换为不同模型所需的训练格式。此次发布主要是基础设施方面的贡献，并不等同于新模型突破或广泛采用的证据。

google_news · MarkTechPost · 9月6日 06:11

**背景**: 计算机使用代理是通过感知图形用户界面并执行操作来完成用户目标的系统。相关研究通常需要代理、可执行环境或沙箱、交互轨迹或数据集，以及可靠的评测机制。在这种场景中，强化学习尤其困难，因为桌面任务通常缺少可扩展且能被机器读取的奖励信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cua-lite.github.io/">CUA - Lite — An Open Platform for Computer - Use Agents</a></li>
<li><a href="https://www.marktechpost.com/2026/09/05/uc-berkeley-researchers-release-cua-lite-an-open-platform-unifying-sandboxes-data-evaluation-and-rl-for-computer-use-agents/">UC Berkeley Researchers Release CUA - Lite , an Open Platform ...</a></li>
<li><a href="https://arxiv.org/pdf/2606.24515">Reinforcement Learning for Computer-Use Agents with ...</a></li>

</ul>
</details>

**标签**: `#Computer-Use Agents`, `#Reinforcement Learning`, `#AI Infrastructure`, `#Evaluation`, `#Open Source`

---

<a id="item-25" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMirAFBVV95cUxNUWgzTHpRSkhLM2FQYTJvZkpOaUU5QzRyWUV0VXVrOXZkWFdjTUdZajI5QlFZNEo2enEwbThwQ2c3OS1uQndDZGlETmdUT3RXRzV3RElPMGsxOUJBMlBxYmVyRDdPekoxUWN2RTY3LXNFb2F5VzZJTXJ2M192TEdZSG0zT1FwaUZZVmk0dmxfcVktaHFJUFVJYkxFdkJhRXlSVUhOMGtxcTlvUEFB0gGsAUFVX3lxTE1RaDNMelFKSEszYVBhMm9mSk5pRTlDNHJZRXRVdWs5dmRYV2NNR1lqMjlCUVk0SjZ6cTBtOHBDZzc5LW5Cd0NkaUROZ1RPdFdHNXdESU8wazE5QkEyUHFiZXJEN096SjFRY3ZFNjctc0VvYXlXNklNcnYzX3ZMR1lIbTNPUXBpRllWaTR2bF9xWS1ocUlQVUliTEV2QmFFeVJVSE4wa3FxOW9QQUE?oc=5" data-hz-title="IFM 发布 K2 Horizon 开放模型系列" data-hz-tags="Open-source AI,Large language models,Model releases,Apache 2.0,AI infrastructure" data-hz-section="other"></a>
## [IFM 发布 K2 Horizon 开放模型系列](https://news.google.com/rss/articles/CBMirAFBVV95cUxNUWgzTHpRSkhLM2FQYTJvZkpOaUU5QzRyWUV0VXVrOXZkWFdjTUdZajI5QlFZNEo2enEwbThwQ2c3OS1uQndDZGlETmdUT3RXRzV3RElPMGsxOUJBMlBxYmVyRDdPekoxUWN2RTY3LXNFb2F5VzZJTXJ2M192TEdZSG0zT1FwaUZZVmk0dmxfcVktaHFJUFVJYkxFdkJhRXlSVUhOMGtxcTlvUEFB0gGsAUFVX3lxTE1RaDNMelFKSEszYVBhMm9mSk5pRTlDNHJZRXRVdWs5dmRYV2NNR1lqMjlCUVk0SjZ6cTBtOHBDZzc5LW5Cd0NkaUROZ1RPdFdHNXdESU8wazE5QkEyUHFiZXJEN096SjFRY3ZFNjctc0VvYXlXNklNcnYzX3ZMR1lIbTNPUXBpRllWaTR2bF9xWS1ocUlQVUliTEV2QmFFeVJVSE4wa3FxOW9QQUE?oc=5) ⭐️ 8.0/10

基础模型研究院（IFM）于 2026 年 9 月 3 日发布了 K2 Horizon 系列，包含六个参数规模从 0.9B 到 375B 的模型。模型权重和代码均采用 Apache 2.0 许可证发布。 从小型模型到超大规模模型的完整覆盖，为边缘设备、本地部署、企业系统以及大规模推理和编码任务提供了更多选择。Apache 2.0 许可证也可能比限制更严格的授权条款更适合商业使用。 六个配置的参数规模分别为 0.9B、3.7B、7B、32B、36B-A4B 和 375B-A23B，IFM 还在发布中间检查点。IFM 表示，该系列面向推理、编码、智能体工作流、边缘设备和企业部署。

google_news · MarkTechPost · 9月7日 05:00

**背景**: 语言模型的参数数量通常可以粗略反映其能力上限和资源需求，因此 0.9B 模型一般比 375B 模型更容易在本地运行。Apache 2.0 是一种较为宽松的开源许可证，允许用户在遵守其规定条件的前提下使用、修改和再分发软件或模型相关材料。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ifm.ai/blog/k2/">Introducing K 2 Horizon : Frontier Performance, Radically Open</a></li>
<li><a href="https://www.apache.org/licenses/LICENSE-2.0">Apache License , Version 2 . 0 | Apache Software Foundation</a></li>

</ul>
</details>

**标签**: `#Open-source AI`, `#Large language models`, `#Model releases`, `#Apache 2.0`, `#AI infrastructure`

---

<a id="item-26" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/" data-hz-title="新通用顶级域名暴露大规模诈骗问题" data-hz-tags="DNS,cybersecurity,scams,domain abuse" data-hz-section="other"></a>
## [新通用顶级域名暴露大规模诈骗问题](https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/) ⭐️ 7.0/10

Terence Eden 援引 Interisle 报告指出，2025 年新增了 8500 万个通用顶级域名，其中 850 万个截至 2025 年 5 月被加入了封锁名单。报告估计，这些注册域名的滥用率至少为 10%，甚至可能接近 20%。 如果这些数据准确，说明域名注册基础设施正被广泛利用来支持诈骗、网络钓鱼和其他滥用行为。这会增加互联网用户、注册商、安全服务提供商以及包括 ICANN 在内的域名治理机构所面临的风险和成本。 这些数据部分基于出现在公开封锁名单中的域名，因此不能视为所有诈骗域名的精确统计。封锁名单可以识别与网络钓鱼、恶意软件、垃圾邮件或其他恶意活动相关的域名，但不同名单的覆盖范围和判定标准并不相同。

rss · Simon Willison · 9月6日 14:40

**背景**: 域名系统（DNS）会把人类易读的域名转换为计算机用于定位互联网服务的信息。通用顶级域名（gTLD）是域名末尾的部分，例如 .com 以及较新的通用扩展名，其运行受到与 ICANN 相关政策的管理。DNS 滥用封锁名单由安全组织、互联网服务提供商等机构维护，用于标记与恶意活动相关的域名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fasthosts.co.uk/blog/generic-top-level-domains-gtlds/">What are Generic TLDs? | gTLDs Explained | Fasthosts</a></li>
<li><a href="https://www.icann.org/resources/pages/what-2012-02-25-en">What Does ICANN Do? - ICANN</a></li>
<li><a href="https://dn.org/the-mechanisms-behind-public-blocklists-in-identifying-malicious-domains/">The Mechanisms Behind Public Blocklists in Identifying ...</a></li>

</ul>
</details>

**标签**: `#DNS`, `#cybersecurity`, `#scams`, `#domain abuse`

---

<a id="item-27" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMidkFVX3lxTFBIUk1BNXFibkhSbUJXV2FGTm9nYThCYzNvRzcwMnJhV2dXUHhwdVZ6Nzc4WUZUWHY0TVpLYlg5TWZwVHdXcHJQdGhsNkNudGZxU2Q2elBzX3dRbk5HQ2NiLTBBalE5Z1RUOU40YTBIalJBNFdRN0E?oc=5" data-hz-title="据报道Kimsuky利用人工智能编程代理批量生产恶意软件" data-hz-tags="Cybersecurity,Malware,North Korea,AI Coding Agents,Threat Intelligence" data-hz-section="other"></a>
## [据报道 Kimsuky 利用人工智能编程代理批量生产恶意软件](https://news.google.com/rss/articles/CBMidkFVX3lxTFBIUk1BNXFibkhSbUJXV2FGTm9nYThCYzNvRzcwMnJhV2dXUHhwdVZ6Nzc4WUZUWHY0TVpLYlg5TWZwVHdXcHJQdGhsNkNudGZxU2Q2elBzX3dRbk5HQ2NiLTBBalE5Z1RUOU40YTBIalJBNFdRN0E?oc=5) ⭐️ 7.0/10

一份报告称，与朝鲜有关联的间谍组织 Kimsuky 被发现使用人工智能编程代理批量生产恶意软件。现有消息背景没有提供足够的技术证据，因此无法独立核实其生产规模或具体使用的工具。 如果属实，人工智能辅助编程可能帮助国家支持的攻击者更快、更低成本地生产或修改恶意软件。这将促使防御者更加重视攻击行为和基础设施，而不能只依赖恶意软件特征码；不过目前人工智能工具通常是辅助攻击者，而不是完全自主运行的攻击系统。 Kimsuky 长期使用鱼叉式网络钓鱼、社会工程、凭据窃取和恶意软件部署等手段，包括利用 PowerShell 和 Windows 工具。应谨慎看待这份报告，因为使用人工智能编程代理本身并不能证明恶意软件具备新型能力、攻击者实现了行动自主化，或相关行动已经成功。

google_news · finance.biggo.com · 9月7日 06:35

**背景**: Kimsuky 是一个与朝鲜有关联的高级持续性威胁组织，据认为自大约 2012 年起一直活跃。该组织主要针对政府机构、智库、学者、记者，以及涉及朝鲜半岛、核政策和地缘政治议题的其他组织开展网络间谍活动。人工智能编程代理是一种能够根据自然语言指令生成或修改代码的软件工具，但人工智能生成的恶意软件通常仍依赖人工指挥以及传统的投递和执行方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-301a">North Korean Advanced Persistent Threat Focus: Kimsuky - CISA Kimsuky, Black Banshee, Velvet Chollima, Emerald Sleet ... Kimsuky APT Profile - North Korean Espionage Group TTPs ... North Korean Kimsuky Actors Leverage Malicious QR Codes in ... North Korean Kimsuky Actors Leverage Malicious QR Codes in ...</a></li>
<li><a href="https://threatactors.adversaryvillage.org/kimsuky/">Kimsuky | Threat Actor Profiles</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#Malware`, `#North Korea`, `#AI Coding Agents`, `#Threat Intelligence`

---

<a id="item-28" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiekFVX3lxTE1sZ09XbERfZHp5bkZYMVJFTUdRWlR6M0l2clN5VGhxX1B1RG5oN2MxRWhqNjJfTW43MkxMMWN1YXoyM2YwU3J6dEZJck9qbkJ3NFdWcVBiTWhlek9WOGdBRld1WXJiQzhWWTFNaTBBN3ZIWW9VR1E4RHBn0gGOAUFVX3lxTE8wX3h5Y2cyeHlLT0dGc05xUk5JOGNTa1ZvZXFFMGdnejA1LW1FTFJITnhzWnpYYUhDQ0RDaDE2SmVuYnFVZVRxXzFZdE0zRkdkZHVhcDNET0sySk4tUU82ekxYM0hLelJZNkJwS0lFcGQzTDZ1bXQ3eXA2ZUJqdl9Pai14b2JBRzBYdkc4X0E?oc=5" data-hz-title="Kimsuky被指利用人工智能代理发动韩国网络攻击" data-hz-tags="Cybersecurity,AI Coding Agents,Kimsuky,Cyberattacks,Threat Intelligence" data-hz-section="other"></a>
## [Kimsuky 被指利用人工智能代理发动韩国网络攻击](https://news.google.com/rss/articles/CBMiekFVX3lxTE1sZ09XbERfZHp5bkZYMVJFTUdRWlR6M0l2clN5VGhxX1B1RG5oN2MxRWhqNjJfTW43MkxMMWN1YXoyM2YwU3J6dEZJck9qbkJ3NFdWcVBiTWhlek9WOGdBRld1WXJiQzhWWTFNaTBBN3ZIWW9VR1E4RHBn0gGOAUFVX3lxTE8wX3h5Y2cyeHlLT0dGc05xUk5JOGNTa1ZvZXFFMGdnejA1LW1FTFJITnhzWnpYYUhDQ0RDaDE2SmVuYnFVZVRxXzFZdE0zRkdkZHVhcDNET0sySk4tUU82ekxYM0hLelJZNkJwS0lFcGQzTDZ1bXQ3eXA2ZUJqdl9Pai14b2JBRzBYdkc4X0E?oc=5) ⭐️ 7.0/10

据报道，与朝鲜有关联的黑客组织 Kimsuky 利用开源人工智能编程代理 opencode，为韩国境内以高端主题为诱饵的攻击制作诱饵文档。分析人员发现，四份文档的时间戳均为 2026 年 8 月 16 日，并在 PDF 的制作程序元数据中识别出 opencode。 这一案例表明，人工智能编程代理可能帮助威胁行为者更高效地制作具有迷惑性的攻击材料，从而加大依赖文档诱饵和自动化开发工具的组织所面临的压力。这也凸显了加强代理执行控制、仔细检查生成文件及其元数据的必要性。 目前报道的证据主要来自诱饵文档本身：这些文档具有相同的时间戳，且 PDF Producer 字段明确记录了 opencode。这些迹象表明该工具参与了文档制作，但现有报道并未证明整个行动是完全自主的，也没有提供完整的攻击链细节。

google_news · Chosunbiz · 9月7日 01:14

**背景**: Kimsuky 是一个与朝鲜有关联、以定向攻击活动闻名的网络间谍组织。人工智能编程代理是一类能够协助生成和执行代码的软件，可以自动完成部分开发任务。在这一案例中，该代理似乎被用于协助制作充当网络攻击诱饵的文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.yna.co.kr/view/AEN20260907003400320">N.K. hacking group Kimsuky used AI coding agents to create decoys...</a></li>
<li><a href="https://www.genians.co.kr/en/blog/threat_intelligence/ai-agent-opencode">Kimsuky Uses the AI Agent 'opencode' to Create Decoys as Its...</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#AI Coding Agents`, `#Kimsuky`, `#Cyberattacks`, `#Threat Intelligence`

---

<a id="item-29" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMilgFBVV95cUxPNTA0eXhUMm1CN0hkM0hFU05xY0JQdGkwd3k5Qk9RcDI1bENFU1RYVzR6clpEWElrUmpDSVJTdUExZGJOZU9MMEtZUmQxdlF1Z0YtdnRVT1lhbExzM3kzakZiTTFwUU1yR2g5VUFlZXBBNk1VVkt4Wmh3MWt6Z3R0NlZkTHNqdDJpRm5fMHJHNHhpUHV1Mmc?oc=5" data-hz-title="NVIDIA 为开源 Nova 驱动加入 vGPU 支持" data-hz-tags="NVIDIA,Nova driver,vGPU,GPU virtualization,Linux" data-hz-section="other"></a>
## [NVIDIA 为开源 Nova 驱动加入 vGPU 支持](https://news.google.com/rss/articles/CBMilgFBVV95cUxPNTA0eXhUMm1CN0hkM0hFU05xY0JQdGkwd3k5Qk9RcDI1bENFU1RYVzR6clpEWElrUmpDSVJTdUExZGJOZU9MMEtZUmQxdlF1Z0YtdnRVT1lhbExzM3kzakZiTTFwUU1yR2g5VUFlZXBBNk1VVkt4Wmh3MWt6Z3R0NlZkTHNqdDJpRm5fMHJHNHhpUHV1Mmc?oc=5) ⭐️ 7.0/10

NVIDIA 已提交一个包含 13 个补丁的系列，为开源 Nova Linux 驱动加入 vGPU 管理器和 VFIO 变体驱动。该工作旨在通过 Nova 支持创建和管理虚拟 GPU 实例。 这一变化可能扩大 Linux 上的开源 GPU 虚拟化能力，并提升 Nova 对虚拟化和云基础设施的价值。这也表明 NVIDIA 正在推动 Nova 成为其 Linux 图形生态中更完整的开源驱动方案，并逐步替代或接替 Nouveau。 该提案使用专门的 VFIO 路径实现虚拟化，并建立在 Nova 的 GPU System Processor 架构之上。Nova 仍处于开发阶段，目前还不适合普通终端用户在主线 Linux 内核中部署。

google_news · Open Source For You · 9月7日 08:08

**背景**: Nova 是一个开源、基于 Rust 的 NVIDIA 内核驱动项目，目标是替代或补充 Nouveau。vGPU 可以让一块物理 GPU 向虚拟机提供多个虚拟 GPU 设备，而 VFIO 则提供 Linux 中用于在虚拟化环境里分配和管理设备的机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://linuxsecurity.com/news/security-projects/nova-nvidia-gpu-drivers-linux">Nova : Strengthening NVIDIA Driver Protection for Linux Systems</a></li>
<li><a href="https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/assembly_managing-gpu-devices-in-virtual-machines_configuring-and-managing-virtualization">Chapter 16. Managing GPU devices in virtual machines | Configuring...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Nova driver`, `#vGPU`, `#GPU virtualization`, `#Linux`

---

<a id="item-30" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/09/05/seattle-times-and-newsday-are-the-latest-publications-to-sue-openai-and-microsoft/" data-hz-title="《西雅图时报》和《新闻日报》起诉OpenAI与微软" data-hz-tags="AI copyright,OpenAI,Microsoft,news publishing,AI regulation" data-hz-section="other"></a>
## [《西雅图时报》和《新闻日报》起诉 OpenAI 与微软](https://techcrunch.com/2026/09/05/seattle-times-and-newsday-are-the-latest-publications-to-sue-openai-and-microsoft/) ⭐️ 6.0/10

《西雅图时报》和《新闻日报》已起诉 OpenAI 与微软，指控两家公司未经授权使用其新闻报道训练人工智能系统。这些诉讼使更多新闻机构加入了围绕受版权保护的新闻内容是否可用于人工智能训练的持续法律争议。 这些案件可能影响法院和政策制定者如何评估受版权保护的新闻内容用于生成式人工智能训练的问题，并可能影响 OpenAI、微软、出版商以及未来的内容授权模式。它们还加剧了行业争论：人工智能公司是否应为使用新闻内容取得许可或支付补偿。 现有报道只说明两家出版机构提出了新闻内容被用于训练的指控，并未说明涉及的数据集、模型、索赔金额或具体法律主张。人工智能模型训练通常会处理大量示例，使系统学习统计模式，但这种复制行为在法律上的定性仍未确定。

rss · TechCrunch AI · 9月5日 22:49

**背景**: 大型语言模型会使用文本和其他数据集合进行训练，从中学习生成回答所需的模式。新闻机构担心，其报道内容，包括原本可能仅限付费用户阅读的材料，会被纳入开发流行人工智能系统的数据集。版权法通常赋予创作者控制作品特定使用方式的权利，但这些规则如何适用于人工智能训练仍在争论之中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nngroup.com/articles/ai-model-training/">How AI Models Are Trained - NN/G - Nielsen Norman Group</a></li>
<li><a href="https://niemanreports.org/the-battle-over-using-journalism-to-build-ai-models-is-just-starting/">The Battle Over Using Journalism to Build AI Models is Just ...</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6468318">Analysing the implications of training generative ai ...</a></li>

</ul>
</details>

**标签**: `#AI copyright`, `#OpenAI`, `#Microsoft`, `#news publishing`, `#AI regulation`

---

<a id="item-31" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/" data-hz-title="遗留系统重写为何经常失败" data-hz-tags="technical debt,software engineering,legacy systems,system rewrites,project management" data-hz-section="other"></a>
## [遗留系统重写为何经常失败](https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/) ⭐️ 6.0/10

Simon Willison 指出，从零开始替换技术债务严重的遗留系统很少成功，因为旧系统仍需持续演进，而新团队又难以复现其未被文档记录的行为和完整范围。最终可能会出现两个同时运行的生产系统，其中新系统只能处理旧系统部分功能。 这项分析揭示了系统迁移中的常见风险：交付压力可能迫使团队在替代系统尚未准备好时部分上线，从而增加运维复杂度，同时无法解决原有技术债务。它认为，加固现有系统并进行有针对性的重构，往往比一次性彻底重写更可靠。 由于旧系统仍支撑核心业务，它会持续变化；而开发者得知系统即将被替换后，可能只愿意以最低限度完成新功能。Willison 建议先为旧系统补充尽可能多的自动化测试，再通过有针对性的重构逐步将其改造成目标形态。

rss · Simon Willison · 9月6日 09:08

**背景**: 技术债务是软件系统因采用捷径、结构薄弱或缺少测试与文档而产生的未来维护成本。遗留系统是仍对业务十分重要、但设计已经难以修改的旧系统。绿地重写指从零构建新系统，但如果它要替代旧系统，就仍必须匹配旧系统未被记录的行为和业务范围。

**标签**: `#technical debt`, `#software engineering`, `#legacy systems`, `#system rewrites`, `#project management`

---

<a id="item-32" class="hz-item-anchor" data-hz-url="https://marginalrevolution.com/marginalrevolution/2026/09/capital-gains-vs-wealth-taxes.html?utm_source=rss&utm_medium=rss&utm_campaign=capital-gains-vs-wealth-taxes" data-hz-title="资产价格变化重塑资本利得税与财富税分析" data-hz-tags="Public Economics,Optimal Taxation,Asset Pricing,Wealth Tax,Capital Gains" data-hz-section="other"></a>
## [资产价格变化重塑资本利得税与财富税分析](https://marginalrevolution.com/marginalrevolution/2026/09/capital-gains-vs-wealth-taxes.html?utm_source=rss&utm_medium=rss&utm_campaign=capital-gains-vs-wealth-taxes) ⭐️ 6.0/10

这项研究建立了一个明确纳入资产价格波动的最优再分配税收模型。研究指出，资产价格变化不仅来自基础现金流的变化，因此传统资本税分析不足以准确比较资本利得税与财富税。 当金融市场估值波动时，这一框架可以帮助政策制定者更准确地评估不同税种的再分配效果。它把最优税收理论与现代资产定价行为联系起来，可能改变人们对资本利得税和财富税的评估方式。 传统方法的核心局限在于忽略资产价格，尽管资产价格可能在不依赖现金流变化的情况下波动。相关研究结果表明，合适的税基取决于价格变化的来源，并可能涉及已实现交易以及资本利得税和股息税。

rss · Marginal Revolution · 9月7日 07:47

**背景**: 资本利得税通常关注资产价值的增值，而财富税关注纳税人持有资产的价值。传统最优资本税理论往往强调现金流，没有充分刻画市场价格因其他估值条件变化而发生的波动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nber.org/system/files/working_papers/w32951/w32951.pdf">PUTTING THE "FINANCE" INTO "PUBLIC FINANCE": A THEORY OF ...</a></li>
<li><a href="https://www.ubscenter.uzh.ch/en/publications/policy_briefs/taxing-capital-but-right.html">Taxing capital, but right | UBS Center</a></li>

</ul>
</details>

**标签**: `#Public Economics`, `#Optimal Taxation`, `#Asset Pricing`, `#Wealth Tax`, `#Capital Gains`

---

<a id="item-33" class="hz-item-anchor" data-hz-url="https://marginalrevolution.com/marginalrevolution/2026/09/sentences-to-ponder-140.html?utm_source=rss&utm_medium=rss&utm_campaign=sentences-to-ponder-140" data-hz-title="人工智能风险上升之际，网络保险费率却持续下降" data-hz-tags="Cybersecurity,AI Risk,Cyber Insurance,Risk Markets" data-hz-section="other"></a>
## [人工智能风险上升之际，网络保险费率却持续下降](https://marginalrevolution.com/marginalrevolution/2026/09/sentences-to-ponder-140.html?utm_source=rss&utm_medium=rss&utm_campaign=sentences-to-ponder-140) ⭐️ 6.0/10

纽约大学斯特恩商学院研究人员 Nate Witkin 指出，全球网络保险费率在第二季度下降了约 4%，这已经是连续第 12 个季度下降。这一现象引发了疑问：既然人们对人工智能驱动的网络风险担忧正在加剧，保险定价为何尚未反映这种变化？ 这一趋势表明，网络保险价格可能更多反映当前损失经验、保险公司竞争、安全控制改进或承保方式变化，而不是新闻中对未来人工智能攻击的担忧。如果人工智能相关损失大幅增加，企业可能很快面临更高保费、更低保障限额、更多除外条款以及更严格的风险监测要求。 这里提到的下降是全球市场某一季度的总体数据，并不能单独证明网络风险正在降低，也不意味着所有客户的保费都在下降。近期行业报道显示，保险公司正因应人工智能驱动的威胁和老旧技术暴露，调整保障限额、保单措辞、承保模型和风险评分方式。

rss · Marginal Revolution · 9月6日 19:39

**背景**: 网络保险是企业向保险公司支付保费，以转移部分网络事件财务风险的一种安排，通常会受到保障条件和限额约束。保险公司会估算数据泄露或勒索软件事件发生的可能性及损失成本，同时评估企业的安全控制措施。人工智能驱动的网络风险可能使这一过程更加复杂，因为攻击者可能改变事件发生的速度、规模和性质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.insurancebusinessmag.com/us/news/cyber/cyber-insurance-enters-the-ai-risk-era-as-limits-wording-and-underwriting-models-shift-565329.aspx">Cyber insurance enters the AI risk era as limits, wording and ...</a></li>
<li><a href="https://insurancecurator.com/emerging-underwriting-models-ai-driven-risk-scoring-in-cybersecurity-insurance/">Emerging Underwriting Models: AI-Driven Risk Scoring in ...</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#AI Risk`, `#Cyber Insurance`, `#Risk Markets`

---

<a id="item-34" class="hz-item-anchor" data-hz-url="https://www.bbc.co.uk/news/articles/cn9wyvxn95vo?at_medium=RSS&at_campaign=rss" data-hz-title="澳大利亚拟允许用户关闭社交媒体算法" data-hz-tags="Platform Regulation,Algorithmic Transparency,Social Media,Technology Policy" data-hz-section="other"></a>
## [澳大利亚拟允许用户关闭社交媒体算法](https://www.bbc.co.uk/news/articles/cn9wyvxn95vo?at_medium=RSS&at_campaign=rss) ⭐️ 6.0/10

澳大利亚计划立法，要求包括 Meta、Google 和 TikTok 在内的大型平台允许用户关闭个性化社交媒体算法。一名部长表示，未提供这一选项的公司可能面临巨额处罚。 这项提案将让用户更好地控制信息流内容的筛选和排序方式，从而挑战以个性化推荐为默认设置的做法。它还可能加大监管机构对大型平台的压力，要求平台提供更高的透明度和更多用户选择。 现有信息描述的是一项计划中的要求，而不是已经生效的法律，并未说明具体罚款金额、实施时间表或关闭选项的技术设计。社交媒体算法通常会利用个人数据和其他信号筛选并排序内容，因此关闭个性化功能可能改变信息流的组织方式。

rss · BBC World News · 9月7日 03:40

**背景**: 社交媒体推荐算法是为每位用户筛选和排序帖子或其他内容的系统。与单纯按时间排列的信息流不同，算法排序的信息流可以利用人口统计资料、个人数据和推断出的兴趣来决定哪些内容优先出现。由于用户通常无法看见或影响这些筛选过程，算法透明度和用户控制权已经成为重要的政策议题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2451958822000872">A scoping review of personalized user experiences on social ...</a></li>
<li><a href="https://ojs.aaai.org/index.php/ICWSM/article/view/31376">Auditing Algorithmic Explanations of Social Media Feeds: A ...</a></li>
<li><a href="https://ide.mit.edu/insights/transparency-the-first-step-to-fixing-social-media/">Transparency: The First Step to Fixing Social Media</a></li>

</ul>
</details>

**标签**: `#Platform Regulation`, `#Algorithmic Transparency`, `#Social Media`, `#Technology Policy`

---

<a id="item-35" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiogFBVV95cUxPa0tpU3NJS0hJQkJYWkNDdTNlNWdjQXUwX3A0enptZEdiLVBfSHNmTEl1ckowbmZfT0pUbERPbE1ETTBZZ3JFamRqSGJJUk5xZ1B3NXZNZ2c0dkNrYmt0bjJCR0JpX1ktWk00Nm40bVVBOHoyOVJCcjg3aTRpS0VlQkVXRDZycFczbFlfM094VzZqLThOeHplU2g5bFhRak9QZWc?oc=5" data-hz-title="开源 Fin-Ray 夹爪支持多机器人操作" data-hz-tags="Robotics,Open Source Hardware,Grippers,Multi-Robot Systems" data-hz-section="other"></a>
## [开源 Fin-Ray 夹爪支持多机器人操作](https://news.google.com/rss/articles/CBMiogFBVV95cUxPa0tpU3NJS0hJQkJYWkNDdTNlNWdjQXUwX3A0enptZEdiLVBfSHNmTEl1ckowbmZfT0pUbERPbE1ETTBZZ3JFamRqSGJJUk5xZ1B3NXZNZ2c0dkNrYmt0bjJCR0JpX1ktWk00Nm40bVVBOHoyOVJCcjg3aTRpS0VlQkVXRDZycFczbFlfM094VzZqLThOeHplU2g5bFhRak9QZWc?oc=5) ⭐️ 6.0/10

该项目介绍了一种开源的仿生 Fin-Ray 软夹爪，用于涉及多个机器人的操作任务。现有资料显示，该设计面向多机器人协作搬运不同物体，并采用了三维打印硬件。 自适应夹爪可以让多个机器人更容易共同抓取和搬运物体，从而减少针对不同物体定制工具的需求。开源硬件方式也可能帮助研究人员和开发者复现、修改并评估这一设计。 搜索结果提到，该设计包含包络式抓取策略、力反馈、压阻式传感器、TPU 95A 材料和 STM32 控制器。不过，所提供的文章内容没有说明负载能力、抓取精度、支持的机器人平台或实际应用限制等定量信息。

google_news · Open Source For You · 9月7日 08:25

**背景**: Fin-Ray 效应是一种受鱼鳍启发的柔性结构原理：受到挤压时，结构会沿物体外形弯曲，从而适应不同形状。软体机器人夹爪利用柔顺材料或结构，相比刚性手指可以更温和地处理物体。多机器人操作还需要协调运动，以便机器人彼此配合并避免相互干扰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bioengineer.org/fin-ray-inspired-soft-gripper-enables-multi-robot-manipulation-of-diverse-objects/">Fin - Ray -inspired soft gripper enables multi- robot manipulation of...</a></li>
<li><a href="https://www.researchgate.net/publication/310515881_Fin_Ray_Effect_Inspired_Soft_Robotic_Gripper_From_the_RoboSoft_Grand_Challenge_Toward_Optimization/fulltext/58313bb708ae102f0731d46a/Fin-Ray-Effect-Inspired-Soft-Robotic-Gripper-From-the-RoboSoft-Grand-Challenge-Toward-Optimization.pdf">Fin Ray ® Effect Inspired Soft Robotic Gripper : From the RoboSoft...</a></li>
<li><a href="https://www.researchgate.net/publication/370114687_Online_and_Scalable_Motion_Coordination_for_Multiple_Robot_Manipulators_in_Shared_Workspaces">(PDF) Online and Scalable Motion Coordination for Multiple Robot ...</a></li>

</ul>
</details>

**标签**: `#Robotics`, `#Open Source Hardware`, `#Grippers`, `#Multi-Robot Systems`

---

<a id="item-36" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMicEFVX3lxTFBsZG02Q3JLNjVkelBYVnc2Wm8wdHJhcjVoS084emFsNmIxMFh3eUFBSnNVa0Z5TWdUNUVmUWhVWkFOQ0dKdkYySkNUZGdyZE4zQmhQMDZ6X3FIeHQyMnN3djRRbkpNb0xxOHdRYzBfUk3SAXZBVV95cUxPR09Qd1BPMS1EeHJqaEduWkJQTXhOUEk2OXdyN2t5eEFzMVc4OUxnX25fa2t4eWVMSmhabXNQejFvbGlxRUZONTljdEdrQXljVXQtdXJoTGd0Vk9iU0d2dVF2SHQ3cHVRMWVqOW5UQ1BhR1loR0tR?oc=5" data-hz-title="CrowdStrike推出基于NVIDIA Nemotron的SafeMind网络安全人工智能系统" data-hz-tags="AI cybersecurity,Agentic AI,CrowdStrike,NVIDIA Nemotron,Cybersecurity systems" data-hz-section="other"></a>
## [CrowdStrike 推出基于 NVIDIA Nemotron 的 SafeMind 网络安全人工智能系统](https://news.google.com/rss/articles/CBMicEFVX3lxTFBsZG02Q3JLNjVkelBYVnc2Wm8wdHJhcjVoS084emFsNmIxMFh3eUFBSnNVa0Z5TWdUNUVmUWhVWkFOQ0dKdkYySkNUZGdyZE4zQmhQMDZ6X3FIeHQyMnN3djRRbkpNb0xxOHdRYzBfUk3SAXZBVV95cUxPR09Qd1BPMS1EeHJqaEduWkJQTXhOUEk2OXdyN2t5eEFzMVc4OUxnX25fa2t4eWVMSmhabXNQejFvbGlxRUZONTljdEdrQXljVXQtdXJoTGd0Vk9iU0d2dVF2SHQ3cHVRMWVqOW5UQ1BhR1loR0tR?oc=5) ⭐️ 6.0/10

CrowdStrike 发布了 SafeMind，这是一套基于 NVIDIA Nemotron 模型构建的智能体网络安全系统。该系统设计为原生运行于 CrowdStrike Falcon 平台中。 这一发布体现了网络安全行业向专用人工智能智能体发展的趋势，这类智能体可支持持续性的防御和攻击性安全操作。如果与 Falcon 平台深度集成，现有用户可能无需更换安全环境即可使用这些能力。 NVIDIA 称 SafeMind 将攻击性人工智能与防御性人工智能结合在持续共同演化的循环中，而 CrowdStrike 表示该系统采用 Nemotron 构建。现有材料没有提供独立评测、性能结果、部署要求或其具体自主操作的详细信息。

google_news · gbhackers.com · 9月7日 05:26

**背景**: 智能体人工智能系统不仅根据提示生成文本，还被设计为围绕目标进行推理并执行任务。NVIDIA Nemotron 是一系列开放模型，提供开放权重、训练数据和训练配方，NVIDIA 将其定位为构建专用人工智能智能体的基础。CrowdStrike Falcon 是 SafeMind 计划原生运行的平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/topics/ai/nemotron">Nemotron AI Models | NVIDIA Developer</a></li>
<li><a href="https://blogs.nvidia.com/blog/nvidia-crowdstrike-fal-con-2026/">NVIDIA and CrowdStrike Strengthen Agentic Cybersecurity Frontier</a></li>
<li><a href="https://www.crowdstrike.com/en-us/press-releases/crowdstrike-launches-frontier-models-for-cybersecurity-with-nvidia/">CrowdStrike Launches Frontier Models for Cybersecurity , Created...</a></li>

</ul>
</details>

**标签**: `#AI cybersecurity`, `#Agentic AI`, `#CrowdStrike`, `#NVIDIA Nemotron`, `#Cybersecurity systems`

---

<a id="item-37" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiqgFBVV95cUxOT1ZZN1RlcGpsNldFVlZZLTJ6NXYxaVFIQTUtZXZpbVg3Z3VTR3dYanFsNEJGQVI5bE1FYTdWYnhuVl9VWTN2d2xYSENiclRCT01BbTdqbExPUVdydXY4ckl5VWgwTGRTVWVDZ1dVZnZzREpHbmtEaDgzQy14blM0dFo1ejdDaFd1MG9BSzFSVHdqdmhoUkZUUlpDRlpPUmxWSHJrYmpFVFZ4dw?oc=5" data-hz-title="仿鱼鳍软夹爪支持多机器人抓取" data-hz-tags="soft robotics,robotic manipulation,grippers,multi-robot systems,bio-inspired design" data-hz-section="other"></a>
## [仿鱼鳍软夹爪支持多机器人抓取](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOT1ZZN1RlcGpsNldFVlZZLTJ6NXYxaVFIQTUtZXZpbVg3Z3VTR3dYanFsNEJGQVI5bE1FYTdWYnhuVl9VWTN2d2xYSENiclRCT01BbTdqbExPUVdydXY4ckl5VWgwTGRTVWVDZ1dVZnZzREpHbmtEaDgzQy14blM0dFo1ejdDaFd1MG9BSzFSVHdqdmhoUkZUUlpDRlpPUmxWSHJrYmpFVFZ4dw?oc=5) ⭐️ 6.0/10

研究人员开发了一种仿 Fin-Ray 效应的软夹爪，旨在帮助多个机器人操作形状和性质各异的物体。现有报道指出了其多机器人操作应用，但未提供具体性能数据或系统细节。 能够适应不同物体的柔顺夹爪，或可减少协作机器人和多机器人工作流对专用工具的需求。这可能提升机器人操作的灵活性，但现有信息不足以判断其相较于现有夹爪的具体优势。 Fin-Ray 效应通常通过柔性指爪和内部横梁实现，接触物体时会发生变形，从而帮助夹爪贴合物体；相关设计也采用过直接 3D 打印的软结构。报道没有说明该新型夹爪的材料、负载能力、控制方式、感知能力或已验证的物体范围。

google_news · Bioengineer.org · 9月5日 22:34

**背景**: Fin-Ray 效应源于鱼鳍的变形方式，并被用于柔顺机器人机构。与刚性夹爪不同，软夹爪能够被动贴合物体表面，因此适合处理形状或性质各异的物体。不过，软夹爪在控制和反馈方面也可能面临挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2016.00070/full">Frontiers | Fin Ray® Effect Inspired Soft Robotic Gripper ...</a></li>

</ul>
</details>

**标签**: `#soft robotics`, `#robotic manipulation`, `#grippers`, `#multi-robot systems`, `#bio-inspired design`

---

<a id="item-38" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMi5AFBVV95cUxQQmIxamItZzBwX2VZNjdla2Fkdm14UnA4MFdwcUNlYWFCRmhnZC0xMWhiT2JiY293TFVldGJnc0pRRGVlSm5NZko3aXN6eXZfbTE1T3ZqWGV2VmtER2Y1bDBsYkdKVUtKZTQ0T0drc3hsWENCV09DY2dneWV4UHVfaEltaW04ZnRkbE1qZkZTbmlTMVV1cmhEUkRUekQ2Z1FsR1BtdUR5UEFiUUlhN1BZdEIyNjBxQ1NHSGRzMHdqYUlSNXYtVHpDQ082MG82TmlIbFZVNExQQnV4Z2k2T2UtRkdGcTXSAeoBQVVfeXFMUDVMN2RXUkVRVjhwTV9vZkU3VXlsUWxNTkttRkZFaGY0TVNHcmdqQ3F2ZXhya05tdTNfTHl4LVVXcGxoU1lOdTNMS3VZWEtPQUtYTngxdWwyZFM3QXB1aVVrOWt0ZzVXSEZRX05BVUJsZFRRa3NLMFR0YTdGM0NuNTd1c0dpNWJZcmFsU1dmdXd2THh6RkMybGp1RmQ1V2NSR1MzLW43WWU1Q2xGS0RUVHZETUFaZnd0Vllwd3UxVmJueGwyWWV1cXItTnI3VUd1WW1HNDBQZ2JtWVAyaWlDOE1sLVUzVGpXUE9R?oc=5" data-hz-title="Perplexity首席执行官推出开源工具Numbat追踪失控AI代理" data-hz-tags="AI agents,AI safety,Open source,Agent monitoring,AI security" data-hz-section="other"></a>
## [Perplexity 首席执行官推出开源工具 Numbat 追踪失控 AI 代理](https://news.google.com/rss/articles/CBMi5AFBVV95cUxQQmIxamItZzBwX2VZNjdla2Fkdm14UnA4MFdwcUNlYWFCRmhnZC0xMWhiT2JiY293TFVldGJnc0pRRGVlSm5NZko3aXN6eXZfbTE1T3ZqWGV2VmtER2Y1bDBsYkdKVUtKZTQ0T0drc3hsWENCV09DY2dneWV4UHVfaEltaW04ZnRkbE1qZkZTbmlTMVV1cmhEUkRUekQ2Z1FsR1BtdUR5UEFiUUlhN1BZdEIyNjBxQ1NHSGRzMHdqYUlSNXYtVHpDQ082MG82TmlIbFZVNExQQnV4Z2k2T2UtRkdGcTXSAeoBQVVfeXFMUDVMN2RXUkVRVjhwTV9vZkU3VXlsUWxNTkttRkZFaGY0TVNHcmdqQ3F2ZXhya05tdTNfTHl4LVVXcGxoU1lOdTNMS3VZWEtPQUtYTngxdWwyZFM3QXB1aVVrOWt0ZzVXSEZRX05BVUJsZFRRa3NLMFR0YTdGM0NuNTd1c0dpNWJZcmFsU1dmdXd2THh6RkMybGp1RmQ1V2NSR1MzLW43WWU1Q2xGS0RUVHZETUFaZnd0Vllwd3UxVmJueGwyWWV1cXItTnI3VUd1WW1HNDBQZ2JtWVAyaWlDOE1sLVUzVGpXUE9R?oc=5) ⭐️ 6.0/10

Perplexity 首席执行官 Aravind Srinivas 推出了开源工具 Numbat，用于监控 AI 代理、检测可疑行为，并帮助防御人员调查安全威胁。目前公开报道没有提供详细的评测结果或采用数据。 随着 AI 代理获得执行任务和使用工具的能力，监控其行为有助于组织识别潜在的失控活动并调查安全事件。开源方式可能让开发者和防御人员更容易检查、改造和部署 AI 代理安全与可观测性工具。 Numbat 被描述为监控和检测工具，但现有信息并未表明它可以替代沙箱、身份控制、端点检测与响应或网络安全控制。它的实际效果、支持的代理框架以及性能限制仍不明确。

google_news · timesnownews.com · 9月6日 12:47

**背景**: AI 代理是能够执行任务并与工具或外部信息交互的系统，而不只是生成单次回答。代理监控，也称为代理可观测性，会记录或检查代理活动，以帮助评估可靠性并识别可疑行为。失控 AI 代理指其行为可能超出预设边界或造成安全风险的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.timesnownews.com/technology-science/perplexity-ceo-aravind-srinivas-introduces-open-source-tool-to-track-rogue-ai-agents-article-156097489">Perplexity CEO Aravind Srinivas Introduces Open-Source Tool ...</a></li>
<li><a href="https://aimultiple.com/agentic-monitoring">15 AI Agent Observability Tools: AgentOps & Langfuse</a></li>
<li><a href="https://www.linkedin.com/posts/taaruff_rogue-ai-agents-are-raising-alarms-tech-activity-7493366872231395328-koXf">Rogue AI Agents Are Raising Alarms. Tech Giants Are Proposing...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#AI safety`, `#Open source`, `#Agent monitoring`, `#AI security`

---

<a id="item-39" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiWEFVX3lxTE9xTmlOTEhkdTFRblFCV0ptNmNFcmNPMXFETWtGaVFWVktRcHpUQm9qUGRiYVV6bllKMVRjMnplX0R3cXZld0hUdG9JTk54YkU3Q2M5U0xpM2s?oc=5" data-hz-title="人工智能应用周度观察" data-hz-tags="人工智能应用,行业观察,科技新闻,AI趋势" data-hz-section="other"></a>
## [人工智能应用周度观察](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9xTmlOTEhkdTFRblFCV0ptNmNFcmNPMXFETWtGaVFWVktRcHpUQm9qUGRiYVV6bllKMVRjMnplX0R3cXZld0hUdG9JTk54YkU3Q2M5U0xpM2s?oc=5) ⭐️ 5.0/10

界面新闻发布了一篇周度汇总，涵盖 2026 年 8 月 31 日至 9 月 6 日期间人工智能应用领域的主要动态。现有信息未列出汇总中涉及的具体事件、产品或技术突破。 这篇文章有助于读者跟踪人工智能应用领域的短期动态和趋势。不过，现有摘要缺乏足够细节，无法据此判断某项具体行业影响或重大变化。 该条目属于广泛的行业观察，而不是针对某项明确技术突破的报道，评分为 10 分制中的 5.0 分。由于未提供社区评论，无法评估讨论质量和读者情绪。

rss · Google News · 国家政策 · 9月6日 13:56

**背景**: 人工智能应用周度观察通常会汇总近期人工智能在产品、服务或行业中的应用动态。这类汇总有助于持续跟踪行业活动，但其信息价值取决于所收录事项的具体程度和分析深度。

**标签**: `#人工智能应用`, `#行业观察`, `#科技新闻`, `#AI趋势`

---

<a id="item-40" class="hz-item-anchor" data-hz-url="https://www.bbc.co.uk/news/articles/c986w38r4j5o?at_medium=RSS&at_campaign=rss" data-hz-title="德国选择党在萨克森-安哈尔特州的增长引发欧洲警报" data-hz-tags="European politics,AfD,Far-right,Germany,EU" data-hz-section="other"></a>
## [德国选择党在萨克森-安哈尔特州的增长引发欧洲警报](https://www.bbc.co.uk/news/articles/c986w38r4j5o?at_medium=RSS&at_campaign=rss) ⭐️ 5.0/10

英国广播公司报道，极右翼政党德国选择党在萨克森-安哈尔特州选举中取得了历史性增长。欧洲编辑卡娅·阿德勒表示，这一结果正在为欧盟和传统政党敲响警钟。 这一结果可能表明，政治风险正在超出德国单个州的范围，包括对极右翼更强的支持以及传统政党面临更大压力。它还可能影响有关欧盟未来方向和稳定性的讨论。 现有信息将这一发展描述为历史性增长，并强调其潜在影响，但没有提供具体得票数字、组阁安排或选民动机的详细解释。因此，这一分析指出了政治风险，但尚不能证明该结果将在多大程度上转化为更广泛的欧洲变化。

rss · BBC World News · 9月7日 04:07

**背景**: 德国选择党是一个在报道中被称为极右翼的德国政党。萨克森-安哈尔特州是德国的一个州，因此当地选举结果首先关系到地区政治，但也可能成为德国全国和欧洲政治讨论的信号。传统政党指的是已经确立的政治力量，它们可能需要回应德国选择党的选举增长。

**标签**: `#European politics`, `#AfD`, `#Far-right`, `#Germany`, `#EU`

---

<a id="item-41" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ScFQxRVZOQ1pRMjE3aU9JdE9VWjlQeWJYdEdyLUo2MWpoNm13QlFkRVIyUUNHem5rbnRQRklzOUN6ZDkxZkJRanl3RE8wYzEtMnQwcDJsSHM?oc=5" data-hz-title="Hugging Face 推出开源 Microduck 机器人" data-hz-tags="Open Source,Robotics,Hugging Face,Artificial Intelligence,Educational Technology" data-hz-section="other"></a>
## [Hugging Face 推出开源 Microduck 机器人](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9ScFQxRVZOQ1pRMjE3aU9JdE9VWjlQeWJYdEdyLUo2MWpoNm13QlFkRVIyUUNHem5rbnRQRklzOUN6ZDkxZkJRanl3RE8wYzEtMnQwcDJsSHM?oc=5) ⭐️ 5.0/10

Hugging Face 推出了名为 Microduck 的 25 厘米开源鸭形机器人，面向开发者和爱好者。该机器人售价 399 美元，旨在支持机器人和人工智能实验，包括强化学习应用。 Microduck 可能降低动手进行机器人实验的成本和复杂度，让教育工作者、爱好者及开发者更容易接触实体人工智能。它的开源定位还将 Hugging Face 的协作模式从软件和模型扩展到了现实世界的机器人硬件。 该机器人配备摄像头、激光雷达和双惯性测量单元，据称能够摇摆行走、轮滑、搬运物体并学习新的行为。不过，现有公告对其计算硬件、软件许可证、训练流程和实际性能提供的细节仍然有限。

google_news · Trend Hunter · 9月7日 00:01

**背景**: 开源机器人是指其设计或代码可以依据相应许可证进行查看、修改和共享的硬件或软件平台。强化学习是一种机器学习方法，智能体通过与环境互动，并根据行为获得反馈来学习动作策略。Hugging Face 的 LeRobot 项目提供预训练模型、示范数据集和仿真环境，旨在帮助人们开始进行机器人开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trendhunter.com/trends/duck-robot">Open-Source Toy Robots : Hugging Face Launches Its Duck Robot</a></li>
<li><a href="https://huggingface.co/lerobot">lerobot (LeRobot) - Hugging Face</a></li>

</ul>
</details>

**标签**: `#Open Source`, `#Robotics`, `#Hugging Face`, `#Artificial Intelligence`, `#Educational Technology`

---

<a id="item-42" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMingFBVV95cUxOU3FyTEEzYVh5OWp4cUFVNTNNaEgwcURIbTdMNzh3T1dhYnRaaHg5S016TnpwQVNFMHIwM0JGUHlRLWhGdkNER2VfeFQ3MmRUX1F5VTRmV0lpM01lRS10c0ZoN0lCbGFqMVpPRW5IbDc5SE5tM3liSVhHa0oxbEpDbWNLVUxpRnJzdVZiSTRUVm9xSXJMTTg3UU1MLWdpZw?oc=5" data-hz-title="OpenTrailPaper 将 LILYGO 硬件变成自行车电脑" data-hz-tags="Open Source,Embedded Systems,IoT,Hardware Projects,Cycling Technology" data-hz-section="other"></a>
## [OpenTrailPaper 将 LILYGO 硬件变成自行车电脑](https://news.google.com/rss/articles/CBMingFBVV95cUxOU3FyTEEzYVh5OWp4cUFVNTNNaEgwcURIbTdMNzh3T1dhYnRaaHg5S016TnpwQVNFMHIwM0JGUHlRLWhGdkNER2VfeFQ3MmRUX1F5VTRmV0lpM01lRS10c0ZoN0lCbGFqMVpPRW5IbDc5SE5tM3liSVhHa0oxbEpDbWNLVUxpRnJzdVZiSTRUVm9xSXJMTTg3UU1MLWdpZw?oc=5) ⭐️ 5.0/10

OpenTrailPaper 是一个开源自行车电脑项目，将 LILYGO T5 E-Paper S3 Pro 改造成 GPS 导航和骑行数据平台。其固件支持离线地图、GPX 路线、FIT 记录和蓝牙传感器，并配有用于地图、路线和设置的配套应用。 该项目展示了如何将一块基于 ESP32-S3 的开发板改造成支持导航和传感器的专业骑行设备。它为硬件爱好者提供了比封闭式商业自行车电脑更灵活、也更便于维护的替代方案，但主要吸引 DIY 用户。 该设备使用 4.7 英寸电子纸屏幕，适合户外低功耗使用，项目还包含 Android 和 iOS 配套应用。它是围绕特定 LILYGO 硬件开发的固件与应用项目，因此兼容性和最终使用体验可能取决于该开发板及可用的传感器集成。

google_news · Open Source For You · 9月7日 07:52

**背景**: 开发板是一种用于实验和原型开发的可编程硬件平台，而不是完整的消费电子产品。电子纸屏幕功耗较低，并且在强光下仍然易于阅读，因此适合电池供电的导航设备。在该项目中，基于 ESP32-S3 的 LILYGO 开发板提供计算平台，固件和配套应用则加入路线、地图和骑行记录等专用功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opentrailpaper.com/">OpenTrailPaper — DIY e-paper bike computer</a></li>
<li><a href="https://www.cnx-software.com/2026/09/05/opentrailpaper-transforms-lilygo-t5-e-paper-s3-pro-devkit-into-a-diy-e-paper-bike-computer/">OpenTrailPaper transforms LILYGO T5 E-Paper S3 Pro devkit ...</a></li>

</ul>
</details>

**标签**: `#Open Source`, `#Embedded Systems`, `#IoT`, `#Hardware Projects`, `#Cycling Technology`

---

<a id="item-43" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMibEFVX3lxTE9QSkl6OE56cDFxQzNoRDdtZXc0eFNsQncyNUpLd0duMTUzbGkzYlFOSVF4aVd5enJCb3hYZVU0eXRMeHJ3b0tjZmI0X0pyYVFuMFNwVENnX1ZHcTR6eW8xR3I5aGh1aE1SelMyZNIBckFVX3lxTE5WMzduRXlUY2QzeGl6cDY2b2FMSkhkdk9IVFdYMlBta1ZhSklKVEJVUW44eUtLV0JDVk5aUTBnNmVrYktubU8ySXo0NVpJeGZkcVBoZEg1U184aTExUkU3d2NsN0JfeVdYWkhBRmxHVWxJdw?oc=5" data-hz-title="CrowdStrike推出面向防御者的SafeMind智能网络安全系统" data-hz-tags="Agentic AI,Cybersecurity,Security Operations,AI Agents" data-hz-section="other"></a>
## [CrowdStrike 推出面向防御者的 SafeMind 智能网络安全系统](https://news.google.com/rss/articles/CBMibEFVX3lxTE9QSkl6OE56cDFxQzNoRDdtZXc0eFNsQncyNUpLd0duMTUzbGkzYlFOSVF4aVd5enJCb3hYZVU0eXRMeHJ3b0tjZmI0X0pyYVFuMFNwVENnX1ZHcTR6eW8xR3I5aGh1aE1SelMyZNIBckFVX3lxTE5WMzduRXlUY2QzeGl6cDY2b2FMSkhkdk9IVFdYMlBta1ZhSklKVEJVUW44eUtLV0JDVk5aUTBnNmVrYktubU8ySXo0NVpJeGZkcVBoZEg1U184aTExUkU3d2NsN0JfeVdYWkhBRmxHVWxJdw?oc=5) ⭐️ 5.0/10

CrowdStrike 宣布推出 SafeMind，这是一套专为网络防御者打造的智能网络安全系统，旨在帮助识别、验证和修复威胁。该系统将专业化安全模型与运行时工具结合起来，计划执行自主且持续时间较长的安全工作流。 SafeMind 体现了网络安全行业向智能 AI 发展的趋势，这类系统不仅提供建议，还能执行多步骤安全操作。如果实际效果符合预期，它可能帮助安全团队处理大量警报、加快响应并减轻分析师负担，但目前提供的信息尚未独立验证这些收益。 CrowdStrike 将 SafeMind 描述为一组专用模型和智能 AI 工具，其中包括进攻型 Red Tempest 与防御型 Blue Solano 安全模型，并计划将其接入 Falcon 平台。现有公告缺少详细技术证据、性能指标，以及关于自主权限、透明度、误报和人工监督的说明。

google_news · CyberSecurityNews · 9月6日 14:28

**背景**: 智能 AI 系统利用推理、规划和持续执行能力完成多步骤目标，而不是只对单条提示作出回应。在网络安全领域，这类系统正被用于调查警报、验证威胁和协调修复。运行时工具是帮助 AI 模型在规定工作流和环境中运行的控制与执行组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.crowdstrike.com/en-us/about-us/cyber-superintelligence-lab/">Cyber Superintelligence Lab: Agentic Cybersecurity | CrowdStrike</a></li>
<li><a href="https://www.microsoft.com/en-us/security/business/security-101/what-is-agentic-ai-cybersecurity">What Is Agentic AI in Cybersecurity? | Microsoft Security</a></li>

</ul>
</details>

**标签**: `#Agentic AI`, `#Cybersecurity`, `#Security Operations`, `#AI Agents`

---

<a id="item-44" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMidkFVX3lxTE1kTWlvdEg4MzRNNDM2LTRrcVZWU2w5Nmo5RWh4a2xfblV1V2pPdDJlZVNycEZUQVNzRzd1VlgtaEtqR0xYT3JiOGxXNXhYM0FCa1REdV96U0lpZVdkUTJNZ3l6TmVFMV9sNVlXdVVSMk5TR2NqVUE?oc=5" data-hz-title="Microduck机器人四天预订量突破一万" data-hz-tags="Open-source hardware,Robotics,Rockchip RK3566,Embedded systems,Hardware market" data-hz-section="other"></a>
## [Microduck 机器人四天预订量突破一万](https://news.google.com/rss/articles/CBMidkFVX3lxTE1kTWlvdEg4MzRNNDM2LTRrcVZWU2w5Nmo5RWh4a2xfblV1V2pPdDJlZVNycEZUQVNzRzd1VlgtaEtqR0xYT3JiOGxXNXhYM0FCa1REdV96U0lpZVdkUTJNZ3l6TmVFMV9sNVlXdVVSMk5TR2NqVUE?oc=5) ⭐️ 5.0/10

据报道，开源双足机器人 Microduck 在四天内获得超过一万份预订，意外带动了采用瑞芯微 RK3566 平台的产品需求，并推高了相关配件价格。 这一反响表明，价格相对亲民的开源桌面机器人能够吸引大量关注，并影响嵌入式硬件供应链的需求。它也可能为创客和开发者提供一个更容易上手的平台，用于试验机器人行为和硬件集成。 Pollen Robotics 介绍称，Microduck 高 25 厘米、重量不到 800 克，配备 15 个电机、摄像头、深度传感器、两个惯性测量单元，以及能够抓取物体的活动喙；其预订价格为 399 美元，不含税费和运费。不过，现有报道没有提供足够的独立证据来核实预订数量、配件涨价幅度或生产时间。

google_news · finance.biggo.com · 9月6日 11:05

**背景**: 双足机器人通过两条腿移动和保持平衡，而开源软硬件栈允许开发者查看、修改和扩展其系统。Microduck 是一款适合放在桌面上的小型机器人，可以行走、坐下、下蹲，并从一些常见跌倒中恢复，还能运行在仿真环境中训练的新行为。RK3566 是一款注重功耗效率的四核嵌入式应用处理器，常用于 Linux 或 Android 单板计算机及其他嵌入式设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pollen-robotics.com/microduck/blog/introducing-microduck/">Meet Microduck | Pollen Robotics</a></li>
<li><a href="https://www.notebookcheck.net/Rockchip-RK3566-Processor-Benchmarks-and-Specs.741611.0.html">Rockchip RK3566 Processor - Benchmarks and Specs Rockchip RK3566 - Rockchips.net Rockchip RK3566: Specs, Performance & Applications Rockchip RK3566 Overview | SoC Guides RK3566 Datasheet - processor | Rockchip Rockchip RK3566 - GadgetVersus</a></li>

</ul>
</details>

**标签**: `#Open-source hardware`, `#Robotics`, `#Rockchip RK3566`, `#Embedded systems`, `#Hardware market`

---