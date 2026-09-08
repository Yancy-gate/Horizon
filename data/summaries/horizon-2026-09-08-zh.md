# Horizon 每日速递 - 2026-09-08

> 从 111 条内容中筛选出 42 条重要资讯。

---

## 偏好雷达

> 基于你维护的偏好档案（data/preference-radar/profile.json）独立筛选的个性化内容。

今日暂无符合偏好的更新。

---
## 华科老师研究方向

> 依据学院教师公开研究方向与论文关键词筛选。

1. [注入时序提升 SPMSM 预测电流无传感器控制](#item-1) ⭐️ 7.0/10
2. [关键基础设施最坏情况扰动的模型与算法](#item-2) ⭐️ 7.0/10
3. [遗传算法优化共享 BRT 车道的公交网络](#item-3) ⭐️ 7.0/10
4. [STO-CAST 预测热带气旋停电](#item-4) ⭐️ 7.0/10
5. [考虑电网负荷的概率分层匹配电动汽车调度方法](#item-5) ⭐️ 7.0/10
6. [概率分层匹配降低电动公交车队规模与充电峰值](#item-6) ⭐️ 7.0/10
7. [固体氧化物燃料电池系统控制综述](#item-7) ⭐️ 6.0/10
8. [自适应电压协调提升虚拟同步发电机逆变器暂态稳定性](#item-8) ⭐️ 6.0/10
9. [永磁同步电机的级联双代价模型预测控制](#item-9) ⭐️ 5.0/10
10. [采用自适应谐波滤波的改进型 PMSM 无位置传感器控制](#item-10) ⭐️ 5.0/10
11. [层次匹配方法用于车辆调度](#item-11) ⭐️ 5.0/10

---
<a id="item-1" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/tpel.2026.3678851" data-hz-title="注入时序提升SPMSM预测电流无传感器控制" data-hz-tags="Sensorless motor control,Permanent-magnet synchronous motors,Model predictive control,Power electronics,Electric drives" data-hz-section="hust-research"></a>
## [注入时序提升 SPMSM 预测电流无传感器控制](https://doi.org/10.1109/tpel.2026.3678851) ⭐️ 7.0/10

该论文提出并通过实验验证了一种面向表面式永磁同步电机（SPMSM）的开关频率注入无传感器控制策略。该方法结合有限控制集死拍预测电流控制、扩展控制集、角域迭代优化和基于注入时刻的电压注入，以减少位置误差并缩短执行时间。 在有限控制集模型预测控制中，不准确的电压注入会扭曲位置误差信号并降低电流调节性能。该方法通过提高注入精度而不过度增加计算量，有望改善 SPMSM 驱动系统在低速或静止状态下的转子位置估计实用性。 该策略利用 d 轴电流偏置实现无传感器运行，同时包含一种简单的初始位置检测方法，并分析电流偏置引起的速度振荡。论文指出，传统误差补偿可能需要显著延长执行时间，而基于注入时刻的方法能够以更短的执行时间实现更精确的注入。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 3月31日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 无传感器电机控制不使用机械位置传感器，而是估算转子位置，因此在低速或静止状态下尤其具有挑战性。开关频率注入通过施加高频电压信号，并利用电机的电气响应推断转子位置。SPMSM 的转子磁各向异性相对较低，因此注入方法有助于提取位置信息；有限控制集模型预测控制则直接从离散集合中选择逆变器开关状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ieeexplore.ieee.org/document/10108031">Sensorless Control With Switching Frequency Square Wave ...</a></li>
<li><a href="https://www.mdpi.com/2079-9292/13/6/1131">Sensorless Control of Surfaced-Mounted Permanent Magnet ...</a></li>

</ul>
</details>

**标签**: `#Sensorless motor control`, `#Permanent-magnet synchronous motors`, `#Model predictive control`, `#Power electronics`, `#Electric drives`

---

<a id="item-2" class="hz-item-anchor" data-hz-url="https://doi.org/10.1016/j.ress.2026.113133" data-hz-title="关键基础设施最坏情况扰动的模型与算法" data-hz-tags="Critical Infrastructure,Reliability Engineering,Systems Resilience,Optimization,Risk Analysis" data-hz-section="hust-research"></a>
## [关键基础设施最坏情况扰动的模型与算法](https://doi.org/10.1016/j.ress.2026.113133) ⭐️ 7.0/10

该文章开发了用于识别和缓解关键基础设施系统最坏情况扰动的模型与算法。现有信息未说明涉及的基础设施类型、具体计算方法或数值结果。 最坏情况分析能够帮助可靠性工程师和基础设施运营者评估严重扰动对系统性能的影响，并确定缓解措施的优先级。这对于相互连接的系统尤其重要，因为故障可能在基础设施网络之间级联并增加恢复难度。 这项工作主要围绕模型和算法展开，现有材料未提供摘要、具体算法表述、验证数据集或性能对比，也未说明是否进行了实际部署。相关研究通常将最坏情况扰动识别建模为攻击者—运营者优化问题，即在评估扰动策略的同时考虑运营者的自适应运行响应。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 7月10日 00:00

**匹配依据**: 论文关键词命中 **critical infrastructure**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 关键基础设施系统包括对社会和其他基础设施至关重要的网络与服务，其发生中断可能造成广泛影响。最坏情况扰动分析并不只评估典型事件，而是寻找可能造成最大损害的故障或攻击场景。在相互依赖的系统中，一种基础设施可能依赖另一种基础设施，因此局部扰动可能传播并引发级联故障。缓解算法则用于表示扰动发生后运营者如何调整系统运行或恢复决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0951832026001596">A people-centric framework for worst-case disruption analysis of interdependent infrastructure systems - ScienceDirect</a></li>
<li><a href="https://cisac.fsi.stanford.edu/events/defending_critical_infrastructure_systems">Defending Critical Infrastructure Systems | FSI</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0950584925000448">Cascading failure prediction and recovery in large-scale ...</a></li>

</ul>
</details>

**标签**: `#Critical Infrastructure`, `#Reliability Engineering`, `#Systems Resilience`, `#Optimization`, `#Risk Analysis`

---

<a id="item-3" class="hz-item-anchor" data-hz-url="https://doi.org/10.23919/csms.2025.0021" data-hz-title="遗传算法优化共享BRT车道的公交网络" data-hz-tags="Transportation Optimization,Bus Rapid Transit,Genetic Algorithms,Network Design,Operations Research" data-hz-section="hust-research"></a>
## [遗传算法优化共享 BRT 车道的公交网络](https://doi.org/10.23919/csms.2025.0021) ⭐️ 7.0/10

该论文提出了一个明确纳入 BRT 车道共享的公交网络设计与频率设置双层模型，并设计了优先级遗传算法（PBGA）进行求解。在 Mandl 基准算例和临沂真实网络上的测试表明，该方法能够获得接近最优的解，降低乘客与运营商成本，并提高 BRT 车道利用率。 这项工作将公交网络规划从传统的线路与频率决策扩展到把共享 BRT 车道作为设计选项。如果其结果能够推广到其他城市，公交管理部门就可能在降低系统成本的同时，提高现有优先通行基础设施的利用率，并改善公交速度与换乘效率。 该方法通过增加 BRT 节点和 BRT 车道弧来描述共享车道网络，并使用基于优先级的染色体、交叉算子和变异算子编码网络决策。论文报告的优势来自基准算例和临沂网络实验，因此实际效果可能取决于当地出行需求、车道共享规则以及双层模型的假设。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 6月1日 00:00

**匹配依据**: 论文关键词命中 **bus transit**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 快速公交系统（BRT）是一种旨在提供更快、更高频服务的公交模式，通常使用专用车道等优先通行基础设施。BRT 车道共享允许普通公交在不干扰既有 BRT 运营的情况下使用这些车道，从而提高车道利用率并增强服务灵活性。双层模型将相关的规划决策与运营决策分开处理，而遗传算法则用于搜索难以直接求解的组合优化问题的优质解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciopen.com/article/10.23919/CSMS.2025.0021">Optimal Design of Bus Transit Networks Incorporating BRT-Lane ...</a></li>
<li><a href="https://www.transit.dot.gov/sites/fta.dot.gov/files/BRTBrochure.pdf">Bus Rapid Transit (BRT) Brochure</a></li>

</ul>
</details>

**标签**: `#Transportation Optimization`, `#Bus Rapid Transit`, `#Genetic Algorithms`, `#Network Design`, `#Operations Research`

---

<a id="item-4" class="hz-item-anchor" data-hz-url="https://doi.org/10.1111/risa.70275" data-hz-title="STO-CAST预测热带气旋停电" data-hz-tags="Deep Learning,Spatiotemporal Forecasting,Power Systems,Disaster Response,Climate Risk" data-hz-section="hust-research"></a>
## [STO-CAST 预测热带气旋停电](https://doi.org/10.1111/risa.70275) ⭐️ 7.0/10

研究人员推出了 STO-CAST，这是一种时空深度学习模型，能够在热带气旋期间根据不断变化的气象预测和已观测停电信息持续更新停电预报。该模型以 4 公里乘 4 公里的空间分辨率每小时生成预报，并同时支持提前 6 小时的临近预报和提前 60 小时的规划预报。 通过随着风暴和电力系统状态变化而更新预测，STO-CAST 有望帮助电力企业改善实时态势感知、应急响应、抢修队伍调度和资源预置。其高分辨率双时间尺度设计，将即时停电管理与热带气旋风险加剧背景下的主动韧性规划连接起来。 该模型将静态环境和基础设施属性与动态气象及停电序列结合起来，并通过留一风暴交叉验证框架对 2022 年台风梅花进行评估。其误差分解区分了模型局限、气象不确定性和观测缺口，但目前报告的证据仍主要来自单个案例研究。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月26日 00:00

**匹配依据**: 论文关键词命中 **tropical cyclone**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 时空模型学习同时随地点和时间变化的关系，这一点很重要，因为热带气旋的影响和停电情况会在事件期间不断移动和演变。状态依赖的观测更新滚动推理意味着，每次新的天气预测或停电观测都可以用于后续预报，而不是依赖一次性固定预测。临近预报关注短期情况，而提前 60 小时的时间范围则支持提前准备和资源预置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2512.06644">From Forecast to Action: A Deep Learning Model for</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/42186946/">From Forecast to Action: A Deep Learning Model for Predicting Power Outages During Tropical Cyclones - PubMed</a></li>

</ul>
</details>

**标签**: `#Deep Learning`, `#Spatiotemporal Forecasting`, `#Power Systems`, `#Disaster Response`, `#Climate Risk`

---

<a id="item-5" class="hz-item-anchor" data-hz-url="https://doi.org/10.6084/m9.figshare.31910706" data-hz-title="考虑电网负荷的概率分层匹配电动汽车调度方法" data-hz-tags="Electric vehicles,Stochastic optimization,Power grid scheduling,Operations research,Transportation systems" data-hz-section="hust-research"></a>
## [考虑电网负荷的概率分层匹配电动汽车调度方法](https://doi.org/10.6084/m9.figshare.31910706) ⭐️ 7.0/10

该文章提出一种概率分层匹配（P-HM）方法，用于同时考虑出行时间不确定性和电网负荷的随机电动汽车调度。模型在最大化准点率的同时，最小化车辆规模、运营成本和充电峰值负荷；数值结果显示，该方法优于基准方法，尤其在减少车辆规模方面表现突出。 这项工作将交通调度不确定性与充电需求峰值联系起来，而不是将交通状况和电网安全分开处理。随着电动汽车日益普及，该方法有望帮助公共交通运营商提高调度可靠性，并降低充电对电网造成的风险。 该方法将时刻表划分为多个层级，根据兼容概率匹配相邻层级，并结合贪婪局部搜索来处理峰值负荷违规问题。现有摘要指出其提升了鲁棒性和电网安全性，但没有给出基准测试的具体数值或验证范围。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 电动汽车调度问题是指在满足时刻表和运营要求的前提下，为公共交通班次分配车辆。当出行时间具有随机性时，延误和时刻变化会改变车辆的充电时间，从而可能形成更高的充电峰值。随机调度模型通过概率方式表示这种不确定性，而电网负荷约束则限制充电需求，以维护系统安全。此前研究也曾利用随机方法安排充电负荷，以缓解配电系统约束，这为将交通调度与电网因素结合起来提供了背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.osti.gov/pages/biblio/1362132">A two-stage stochastic optimization model for scheduling electric vehicle charging loads to relieve distribution-system constraints (Journal Article) | OSTI.GOV</a></li>
<li><a href="https://pubsonline.informs.org/doi/10.1287/trsc.1030.0069">A Robust Solution Approach to the Dynamic Vehicle Scheduling ...</a></li>

</ul>
</details>

**标签**: `#Electric vehicles`, `#Stochastic optimization`, `#Power grid scheduling`, `#Operations research`, `#Transportation systems`

---

<a id="item-6" class="hz-item-anchor" data-hz-url="https://doi.org/10.6084/m9.figshare.31910706.v1" data-hz-title="概率分层匹配降低电动公交车队规模与充电峰值" data-hz-tags="Electric Vehicle Scheduling,Optimization,Power Grids,Stochastic Modeling,Public Transportation" data-hz-section="hust-research"></a>
## [概率分层匹配降低电动公交车队规模与充电峰值](https://doi.org/10.6084/m9.figshare.31910706.v1) ⭐️ 7.0/10

该文章提出了一种考虑电网负荷约束的随机电动汽车调度概率分层匹配（P-HM）方法。该方法将时刻表划分为多个层级，依据兼容概率匹配相邻层级，并结合贪心局部搜索减少负荷峰值违规。 该方法同时考虑不确定行程时间、车队规模、运营成本、充电峰值和准点表现，处理了以往常被分开建模的相互影响。报告结果表明，它有望帮助公共交通运营商减少车辆需求，同时提高调度可靠性和电网安全性。 据报道，P-HM 优于基准方法，尤其在减少车队规模方面表现突出；其中的贪心局部搜索组件用于处理充电负荷峰值违规。现有内容没有给出具体改进数值，也未说明该方法在不同网络规模、充电设施或交通条件下的表现。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 电动汽车调度问题是指在满足时刻表和车辆运行要求的同时，为公共交通班次分配电动汽车。随机行程时间可能导致车辆晚到，并改变车辆的充电时间，从而增加充电负荷峰值。因此，在调度中同时考虑电网负荷，可以把交通运行可靠性与电力系统约束联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/0305215X.2026.2643627">Probability-based hierarchical matching approach for ...</a></li>
<li><a href="https://tandf.figshare.com/articles/dataset/Probability-based_hierarchical_matching_approach_for_stochastic_electric_vehicle_scheduling_considering_power_grid_load/31910706">Item - Probability-based hierarchical matching approach for ...</a></li>

</ul>
</details>

**标签**: `#Electric Vehicle Scheduling`, `#Optimization`, `#Power Grids`, `#Stochastic Modeling`, `#Public Transportation`

---

<a id="item-7" class="hz-item-anchor" data-hz-url="https://doi.org/10.23919/pcmp.2025.000294" data-hz-title="固体氧化物燃料电池系统控制综述" data-hz-tags="solid oxide fuel cells,power systems,control systems,energy systems,review" data-hz-section="hust-research"></a>
## [固体氧化物燃料电池系统控制综述](https://doi.org/10.23919/pcmp.2025.000294) ⭐️ 6.0/10

本文全面综述了固体氧化物燃料电池系统的控制目标、控制策略和未解决的挑战。文章还总结了相关控制研究在分布式发电、交通运输和住宅能源系统等应用中的进展。 这篇综述有助于电力系统和能源控制研究人员比较不同的固体氧化物燃料电池系统管理方法，因为这类系统虽然效率较高且燃料适应性强，但调节难度较大。文章的综合分析可能推动固体氧化物燃料电池技术更可靠地应用于分布式能源及其他能源场景。 固体氧化物燃料电池通常在约 600 至 1000 摄氏度下运行，并使用传导氧离子的固态氧化物电解质。其控制受到高温运行、多物理场耦合和长期退化的共同影响，因此控制器需要在性能、安全性和耐久性之间取得平衡。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 7月1日 00:00

**匹配依据**: 论文关键词命中 **fuel cell**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 固体氧化物燃料电池通过电化学反应发电，而不是直接燃烧发电。固态氧化物电解质在高温下传导氧离子，系统的运行条件和燃料处理过程需要通过控制进行协调。这些特性使固体氧化物燃料电池控制成为一个系统级问题，涉及热、电和化学动力学。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://core.ac.uk/download/pdf/77745.pdf">Oxygenated hydrocarbon fuels for solid oxide fuel cells</a></li>
<li><a href="https://ieeexplore.ieee.org/abstract/document/11595155">Solid Oxide Fuel Cell System Control: A Comprehensive Review ...</a></li>

</ul>
</details>

**标签**: `#solid oxide fuel cells`, `#power systems`, `#control systems`, `#energy systems`, `#review`

---

<a id="item-8" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560379" data-hz-title="自适应电压协调提升虚拟同步发电机逆变器暂态稳定性" data-hz-tags="grid-forming inverters,transient stability,virtual synchronous generators,power systems control" data-hz-section="hust-research"></a>
## [自适应电压协调提升虚拟同步发电机逆变器暂态稳定性](https://doi.org/10.1109/ccdc69976.2026.11560379) ⭐️ 6.0/10

该论文提出在虚拟同步发电机控制的构网型逆变器中，自适应协调快速和慢速内部电压源，以提升暂态稳定性。该控制器旨在根据系统需求，在扰动期间切换或协调不同的电压源动态特性。 构网型逆变器需要在电网发生大扰动时保持稳定，同时提供电网支撑功能，而自适应电压动态可能有助于平衡这些相互制约的要求。随着可再生能源接入增加、基于逆变器的资源在电力系统中的作用增强，这种方法可能具有实用价值。 该方法的核心设计权衡在于：快速内部电压动态有利于迅速响应电网变化，而较慢的动态有助于实现更自然的构网行为，并提升扰动下的稳定性。现有信息没有提供该论文的实验结果、定量稳定裕度或性能对比数据。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **grid-forming**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 构网型逆变器通过调节自身的电压和频率运行，而不是简单跟随已有的电网波形。虚拟同步发电机控制使逆变器在动态特性上模拟同步发电机的部分行为，包括与频率和相位相关的响应。内部电压源控制决定逆变器的电压参考值如何变化，因此其动态速度会同时影响扰动响应和稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ieeexplore.ieee.org/document/10105459/">Control of Grid - Forming VSCs: A Perspective of Adaptive Fast / Slow ...</a></li>
<li><a href="https://www.monash.edu/__data/assets/pdf_file/0020/3105740/Dayan_2020_JourPaper_HinfBasedControlDesignforGridformingInverters.pdf">Inverters with Enhanced Damping and Virtual</a></li>

</ul>
</details>

**标签**: `#grid-forming inverters`, `#transient stability`, `#virtual synchronous generators`, `#power systems control`

---

<a id="item-9" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560295" data-hz-title="永磁同步电机的级联双代价模型预测控制" data-hz-tags="Model Predictive Control,Permanent Magnet Synchronous Motors,Motor Drives,Dynamic Switching,Control Systems" data-hz-section="hust-research"></a>
## [永磁同步电机的级联双代价模型预测控制](https://doi.org/10.1109/ccdc69976.2026.11560295) ⭐️ 5.0/10

该论文提出了一种用于永磁同步电机的级联双代价函数模型预测控制策略，并引入动态切换以改善控制性能。现有信息未提供具体数值结果、硬件细节或基准对比。 永磁同步电机驱动系统广泛应用于工业自动化和电动汽车等高性能场景，快速响应与高效运行十分重要。结合多个代价函数和动态切换的控制策略，可能为平衡不同控制目标提供一种实用途径，但在缺乏验证数据的情况下，其广泛影响仍不确定。 该方法属于永磁同步电机模型预测控制研究范畴，相关研究已经探讨了双代价函数方法和基于切换的控制策略。由于所提供的记录不包含论文全文或实验结果，因此无法确认其对转矩脉动、计算时间、开关频率或跟踪误差的具体改善。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 模型预测控制利用数学模型预测电机对不同控制动作的响应，然后通过优化代价函数选择控制动作。永磁同步电机是一种利用永磁体产生转子磁场的电机，具有较高的效率和功率密度。在这一背景下，双代价函数设计使用两个控制目标或评价标准，而动态切换则根据运行状态改变当前采用的控制策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mdpi.com/2076-3417/13/10/6255">Overview of Predictive Control Technology for Permanent ...</a></li>
<li><a href="https://www.academia.edu/73456667/Dual_Cost_Function_Model_Predictive_Direct_Speed_Control_With_Duty_Ratio_Optimization_for_PMSM_Drives">(PDF) Dual Cost Function Model Predictive Direct Speed Control ...</a></li>
<li><a href="https://scholar.hit.edu.cn/en/publications/dynamic-threshold-adjustment-based-event-triggered-model-predicti/">Dynamic Threshold Adjustment-Based Event-Triggered Model ...</a></li>

</ul>
</details>

**标签**: `#Model Predictive Control`, `#Permanent Magnet Synchronous Motors`, `#Motor Drives`, `#Dynamic Switching`, `#Control Systems`

---

<a id="item-10" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560068" data-hz-title="采用自适应谐波滤波的改进型PMSM无位置传感器控制" data-hz-tags="PMSM control,Sensorless control,Active disturbance rejection control,Adaptive filters,Power electronics" data-hz-section="hust-research"></a>
## [采用自适应谐波滤波的改进型 PMSM 无位置传感器控制](https://doi.org/10.1109/ccdc69976.2026.11560068) ⭐️ 5.0/10

该论文提出了一种用于永磁同步电机的位置无传感器控制方法，将改进型主动扰动抑制控制与并行自适应谐波滤波器相结合。现有信息未提供定量结果、实验条件，也未明确说明除 2026 年 DOI 记录之外的具体发表日期。 无位置传感器控制可以减少对机械位置传感器的依赖，而扰动抑制和谐波滤波有望改善非理想运行条件下的控制性能。该工作主要与 PMSM 驱动、电机控制和电力电子领域的研究人员及工程师相关，但根据现有信息尚无法判断其更广泛的影响。 该方法的具体特点是将主动扰动抑制控制与并行自适应谐波滤波器结合起来，而不仅仅是采用无位置传感器控制。现有材料未提供摘要、基准测试数据、实现限制，或与现有方法的对比证据，因此其改进效果尚无法验证。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 永磁同步电机利用永磁体产生转子磁场，通常通过电子驱动系统进行控制。位置无传感器控制不使用机械传感器直接测量转子位置，而是对其进行估算。主动扰动抑制控制用于补偿扰动和模型不确定性，自适应谐波滤波器则会调整滤波特性，以处理谐波成分。

**标签**: `#PMSM control`, `#Sensorless control`, `#Active disturbance rejection control`, `#Adaptive filters`, `#Power electronics`

---

<a id="item-11" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560172" data-hz-title="层次匹配方法用于车辆调度" data-hz-tags="vehicle scheduling,matching algorithms,operations research,optimization" data-hz-section="hust-research"></a>
## [层次匹配方法用于车辆调度](https://doi.org/10.1109/ccdc69976.2026.11560172) ⭐️ 5.0/10

该论文提出了一种基于层次匹配的方法，用于解决车辆调度问题。现有信息没有说明其具体算法实现、基准测试结果或性能提升幅度。 车辆调度需要将车辆分配给预定行程，同时尽量降低运营成本和资本成本，因此更好的匹配方法可能有助于提高车队规划效率。不过，现有证据表明，这项工作更可能是面向特定领域的技术贡献，尚未显示出对整个行业的突破性影响。 车辆调度中的匹配模型可以包括容量约束匹配和多商品匹配，其中后者通常具有较高的计算复杂度；但所提供的材料没有说明该论文层次匹配方法的计算特性。现有信息也没有提供社区讨论、实际采用情况或对比评估数据。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 车辆调度是将车辆分配给一组起止时间固定的预定行程的过程。常见目标包括降低资本成本和运营成本。匹配算法用于建立车辆与行程之间的可行分配关系，而层次匹配则把这类决策组织成多个层级或阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubsonline.informs.org/doi/abs/10.1287/trsc.35.2.165.10135">Models and Algorithms for Single-Depot Vehicle Scheduling</a></li>
<li><a href="https://link.springer.com/rwe/10.1007/978-3-030-54621-2_704-1">Vehicle Scheduling | Springer Nature Link</a></li>
<li><a href="https://www.scribd.com/document/370190830/Bertossi-1987">Vehicle Scheduling: Matching Problems Analysis | PDF ... - Scribd</a></li>

</ul>
</details>

**标签**: `#vehicle scheduling`, `#matching algorithms`, `#operations research`, `#optimization`

---

## 其他资讯

12. [消费级硬件破解上世纪 90 年代 512 位 RSA 证书](#item-12) ⭐️ 8.0/10
13. [Mistral raises €3B](#item-13) ⭐️ 8.0/10
14. [Buckmaster 指控 OpenAI 涉人工智能辅助纳维–斯托克斯研究争议](#item-14) ⭐️ 8.0/10
15. [Broadcom 移除 VDDK 下载，VMware 迁移更难](#item-15) ⭐️ 8.0/10
16. [LG 智能电视引发新的隐私与监控担忧](#item-16) ⭐️ 8.0/10
17. [Open Jobs 以 CC0 发布三百万条职位信息](#item-17) ⭐️ 8.0/10
18. [IFM 发布 K2 Horizon：从 0.9B 到 375B 的六款 Apache 2.0 模型](#item-18) ⭐️ 8.0/10
19. [朝鲜黑客将木马化 HAProxy 变成网络流量窃听器](#item-19) ⭐️ 8.0/10
20. [LLM 0.35 新增对 GPT-6 Astra 的支持。](#item-20) ⭐️ 7.0/10
21. [恶意爬虫消耗内核基础设施资源](#item-21) ⭐️ 7.0/10
22. [Research acceleration: The view inside OpenAI](#item-22) ⭐️ 7.0/10
23. [Axis Robotics 开源大型 Franka 机械臂仿真数据集](#item-23) ⭐️ 7.0/10
24. [NVIDIA 为开源 Nova 驱动加入虚拟 GPU 支持](#item-24) ⭐️ 7.0/10
25. [据报道朝鲜黑客利用人工智能扩大钓鱼攻击](#item-25) ⭐️ 7.0/10
26. [Kimsuky 据报道在韩国使用人工智能编程代理](#item-26) ⭐️ 7.0/10
27. [Perplexity 推出开源工具 Numbat 追踪失控 AI 代理](#item-27) ⭐️ 7.0/10
28. [Pachocki：防御人工智能威胁可能需要更先进的人工智能](#item-28) ⭐️ 6.0/10
29. [新交通技术如何重塑城市密度](#item-29) ⭐️ 6.0/10
30. [新模型比较资本利得税与财富税](#item-30) ⭐️ 6.0/10
31. [人工智能传感器实现无塑料微塑料检测](#item-31) ⭐️ 6.0/10
32. [YuzukiNeko 将支持 Linux 的 RISC-V 装入 Pico 尺寸单板机](#item-32) ⭐️ 6.0/10
33. [优化方法识别软件生态系统中的重叠社区](#item-33) ⭐️ 6.0/10
34. [开源鳍射线夹爪支持多机器人协同操作](#item-34) ⭐️ 6.0/10
35. [金融行为监管局警告金融机构应对人工智能安全问题不堪重负](#item-35) ⭐️ 6.0/10
36. [Figma 称 AI 智能代理将安全警报处理提速 70%](#item-36) ⭐️ 6.0/10
37. [浏览器视频压缩工具可本地运行 FFmpeg](#item-37) ⭐️ 5.0/10
38. [韩国“多巴胺网站”模拟购物快感](#item-38) ⭐️ 5.0/10
39. [Emergent Ventures 公布第 59 届获资助者](#item-39) ⭐️ 5.0/10
40. [GitGuardian 探索人工智能分析公开泄露凭证](#item-40) ⭐️ 5.0/10
41. [InferenceX 加速 TPU 推理外部化](#item-41) ⭐️ ?/10
42. [坚持与沉没成本之间](#item-42) ⭐️ ?/10

---

<a id="item-12" class="hz-item-anchor" data-hz-url="https://mcpherrin.ca/2026/09/07/rsa.html" data-hz-title="消费级硬件破解上世纪90年代512位RSA证书" data-hz-tags="Cryptography,RSA,TLS,Legacy Systems,Security Research" data-hz-section="other"></a>
## [消费级硬件破解上世纪 90 年代 512 位 RSA 证书](https://mcpherrin.ca/2026/09/07/rsa.html) ⭐️ 8.0/10

这篇文章记录了研究者使用消费级硬件分解一张由上世纪 90 年代证书颁发机构签发的 512 位 RSA 证书。文章还分析了这一结果如何暴露旧式 TLS 部署以及未使用临时会话密钥的早期加密方案的弱点。 如果能够恢复证书私钥，那么在 TLS 连接使用不具备前向保密性的 RSA 密钥交换时，过去记录的流量可能面临解密风险。这项演示说明，即使使用这些系统的环境已经消失，过时的密码参数和旧式兼容模式仍可能构成安全隐患。 目标环境涉及 Netscape Communicator 4.51 等旧式客户端，包括出口版和美国版；由于现代 Go 的 crypto/tls 已经不再支持所需的 SSLv3 时代行为，项目因此需要自定义 TLS 实现。社区讨论认为，这次分解大约使用消费级 GPU 耗时两天，同时指出当时大量流量要么没有加密，要么使用了不具备临时密钥的保护方式。

hackernews · ahlCVA · 9月8日 01:16 · [社区讨论](https://news.ycombinator.com/item?id=49604637)

**背景**: RSA 的安全性依赖于分解两个大素数乘积的困难程度，而 512 位模数如今远低于现代安全要求。在较早的基于 RSA 的 TLS 握手中，服务器证书的长期私钥可能帮助恢复某次会话的加密密钥。临时 Diffie-Hellman 方法会生成独立且短期有效的会话密钥，并提供前向保密性，因此即使证书私钥后来泄露，也不会自动解密过去记录的会话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.startupdefense.io/cyberattacks/freak-attack">FREAK Attack: A Complete Security Vulnerability Guide</a></li>
<li><a href="https://www.encryptionconsulting.com/all-you-need-to-know-about-perfect-forward-secrecy/">All You Need to Know About Perfect Forward Secrecy</a></li>
<li><a href="https://www.cloudflare.com/learning/ssl/keyless-ssl/">How Does Keyless SSL Work? | Forward Secrecy - Cloudflare Key Exchange and Forward Secrecy | TLSleuth Perfect Forward Secrecy - GeeksforGeeks TLS Protocol and Cipher Suite Guide: Version, Forward Secrecy ... Key Exchange in SSL/TLS: Understanding RSA, Diffie-Hellman ...</a></li>

</ul>
</details>

**社区讨论**: 社区总体认可这项演示，评论者强调了使用消费级 GPU 大约两天完成分解、当时大量流量缺乏临时密钥甚至完全没有加密，以及“先记录、后解密”的风险。一位评论者批评文章过度依赖人工智能生成的解释，但补充了 Netscape 目标和使用自定义 TLS 实现的原因；其他人则认为其中的历史细节和幽默元素很有趣。

**标签**: `#Cryptography`, `#RSA`, `#TLS`, `#Legacy Systems`, `#Security Research`

---

<a id="item-13" class="hz-item-anchor" data-hz-url="https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/" data-hz-title="Mistral raises €3B" data-hz-tags="Mistral AI,Sovereign AI,Open-Weight Models,AI Industry,European Technology" data-hz-section="other"></a>
## [Mistral raises €3B](https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/) ⭐️ 8.0/10

Mistral’s €3 billion funding round strengthens Europe’s effort to build a sovereign AI ecosystem while prompting debate about the company’s model quality, business strategy, and ability to compete with larger US labs.

hackernews · kuberwastaken · 9月8日 05:06 · [社区讨论](https://news.ycombinator.com/item?id=49605767)

**标签**: `#Mistral AI`, `#Sovereign AI`, `#Open-Weight Models`, `#AI Industry`, `#European Technology`

---

<a id="item-14" class="hz-item-anchor" data-hz-url="https://cims.nyu.edu/~tristanb/statement.pdf" data-hz-title="Buckmaster指控OpenAI涉人工智能辅助纳维–斯托克斯研究争议" data-hz-tags="AI research ethics,academic integrity,mathematical research,Navier–Stokes,AI safety and governance" data-hz-section="other"></a>
## [Buckmaster 指控 OpenAI 涉人工智能辅助纳维–斯托克斯研究争议](https://cims.nyu.edu/~tristanb/statement.pdf) ⭐️ 8.0/10

Tristan Buckmaster 的声明指控，OpenAI 曾使用与纳维–斯托克斯问题有关的语言模型辅助研究成果，并对人工参与程度作出不实描述，同时就署名和公开披露向研究人员施压。现有材料将这些内容呈现为个人声明中的指控，尚未构成独立证实的事实。 这场争议凸显了资金雄厚的人工智能公司利用语言模型攻克高难度学术问题时，在数据来源、署名、同意以及权力不对等方面尚未解决的问题。它可能影响保护研究人员成果的规范，以及数学发现中人类和模型贡献程度的披露方式。 评论显示，OpenAI 的内部工作可能是在研究人员取得进展后展开的，也可能使用了公开可获得的信息；而声明则质疑“模型只得到问题陈述、几乎不需要人工输入”的说法。这里提供的证据仅包括一份声明和部分讨论摘录，因此事件经过以及是否使用私人会话数据仍不确定。

hackernews · procedurecall · 9月8日 05:42 · [社区讨论](https://news.ycombinator.com/item?id=49605915)

**背景**: 纳维–斯托克斯存在性与光滑性问题关注描述流体运动的方程在三维情况下是否始终具有良好的数学性质。它是克雷数学研究所千禧年大奖难题之一。大型语言模型能够生成和转换数学文本，但将其用于研究也会引发可靠性、验证、署名以及辅助与发现边界等问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier – Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://navier-stokes.org/navier-stokes-existence-and-smoothness/">Clay Navier - Stokes Problem : Official Statement Explained</a></li>

</ul>
</details>

**社区讨论**: 讨论整体上对涉嫌滥用研究人员成果、施压行为以及学术界与大型人工智能公司之间的不平等激励感到愤怒和担忧。其他评论者则聚焦于尚未解决的数据来源问题，追问私人模型会话是否被访问，以及研究人员的公开成果或提示词在多大程度上引导了 OpenAI 的内部工作。

**标签**: `#AI research ethics`, `#academic integrity`, `#mathematical research`, `#Navier–Stokes`, `#AI safety and governance`

---

<a id="item-15" class="hz-item-anchor" data-hz-url="https://www.virtualizationhowto.com/2026/09/leaving-vmware-just-got-harder-after-broadcom-pulled-vddk-downloads/" data-hz-title="Broadcom移除VDDK下载，VMware迁移更难" data-hz-tags="VMware,Broadcom,Virtualization,Migration,Vendor Lock-in" data-hz-section="other"></a>
## [Broadcom 移除 VDDK 下载，VMware 迁移更难](https://www.virtualizationhowto.com/2026/09/leaving-vmware-just-got-harder-after-broadcom-pulled-vddk-downloads/) ⭐️ 8.0/10

Broadcom 移除了公开的 VMware 虚拟磁盘开发工具包（VDDK）下载，使依赖该工具访问 VMware 虚拟磁盘的迁移、备份和互操作流程更加复杂。此举加剧了 VMware 客户和第三方工具厂商对平台退出难度的担忧。 VDDK 被用于让外部软件读取 VMware 虚拟磁盘，因此获取渠道受限可能阻碍备份产品以及迁移到其他平台的自动化流程。此次变化进一步加深了人们对 Broadcom 旗下 VMware 生态锁定效应的担忧，并可能提高更换厂商的运营成本。 搜索结果显示，没有 VDDK 时，一些迁移工具只能使用明显更慢的备用路径，而涉及 vSAN 的迁移可能无法进行；此外，工具厂商也不能随意再分发 VDDK。关机后传输磁盘或基于备份恢复等方法仍然可行，但速度可能更慢，且需要额外的运维步骤。

hackernews · josephcsible · 9月7日 20:32 · [社区讨论](https://news.ycombinator.com/item?id=49602699)

**背景**: VDDK 是基于虚拟磁盘应用程序接口的 VMware 开发工具包，可让应用程序访问和传输 VMware 虚拟磁盘。它还与 VMware 的 vSphere 数据保护流程有关，包括基于快照的虚拟机备份和恢复。由于许多备份和迁移产品都集成了这一接口，它的可用性会影响虚拟机在不同环境之间迁移的效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.shapeblue.com/broadcom-vddk-download-vmware-to-kvm/">Broadcom Removes VDDK Pages Without Explanation... - ShapeBlue</a></li>
<li><a href="https://aenix.io/migration/vmware/">VMware migration — exit VCF without breaking the application – Ænix</a></li>
<li><a href="https://platform9.com/blog/vddk-no-longer-available/">Broadcom Cut Public Access of Virtual Disk Development Kit ...</a></li>

</ul>
</details>

**社区讨论**: 讨论整体上对 Broadcom 管理 VMware 持负面态度，前员工和管理员将此次变化视为平台整体衰退的一部分，并对曾经强大的生态系统受到削弱表示遗憾。实践者比较了迁移到 Hyper-V 和 Proxmox 的体验：有人认为 Hyper-V 的工具更零散，也有人表示小规模迁移到 Proxmox 相对顺利；另有评论提出非法保存 VMware 源代码的想法，这显然涉及不可接受的违法行为。

**标签**: `#VMware`, `#Broadcom`, `#Virtualization`, `#Migration`, `#Vendor Lock-in`

---

<a id="item-16" class="hz-item-anchor" data-hz-url="https://www.youtube.com/watch?v=6IFVTcM28KA" data-hz-title="LG 智能电视引发新的隐私与监控担忧" data-hz-tags="Smart TVs,Privacy,Surveillance,IoT Security,Consumer Rights" data-hz-section="other"></a>
## [LG 智能电视引发新的隐私与监控担忧](https://www.youtube.com/watch?v=6IFVTcM28KA) ⭐️ 8.0/10

Gamers Nexus 的调查称，LG 智能电视可能会反复扫描本地网络中的附近设备，并在屏幕关闭时采集麦克风音频。测试显示，电视重新连接互联网后，所收集的数据可能会被上传。 如果这些行为在受影响的型号和配置中得到证实，电视可能在缺乏充分明确同意的情况下暴露家庭活动和设备信息。这也引发了有关消费者隐私、第三方同意、窃听法律以及联网家电可信度的更广泛问题。 相关报道将这一问题与自动内容识别（ACR）联系起来；该功能可以收集屏幕显示内容和观看情况，而独立测试则描述了电视通过联网设备协议发现本地网络设备的行为。现有材料主要来自调查和视频报道，因此确切涉及的型号、固件版本、设置、数据去向及法律性质仍需独立核实。

hackernews · treve · 9月7日 00:22 · [社区讨论](https://news.ycombinator.com/item?id=49592375)

**背景**: 自动内容识别是一种用于识别屏幕内容及观看时长的智能电视技术，通常用于分析或广告。扫描本地网络可以让设备发现附近连接的其他硬件，而采集麦克风音频则可能记录电视周围的声音。如果这些功能被清楚披露并受到适当控制，可能具有正当用途；但当用户或家庭访客不了解这些行为或没有同意时，它们就会带来隐私风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html">LG smart TVs caught logging audio with... - Notebookcheck News</a></li>
<li><a href="https://cyberinsider.com/lg-smart-tvs-found-scanning-home-networks-for-nearby-devices/">LG Smart TVs found scanning home networks for nearby devices</a></li>
<li><a href="https://digiday.com/future-of-tv/wtf-is-automatic-content-recognition/">WTF is automatic content recognition ?</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上十分担忧，重点讨论了 LG 的合同条款；他们认为条款把通知家庭成员和访客可能被采集语音的责任交给了设备所有者。部分人质疑这种做法是否会与要求所有相关方同意的窃听法律冲突，批评联网设备遥测已被正常化；也有人把关闭网络功能视为实际应对方式，同时指出在广告支持的网站上讨论广告监控可能存在矛盾。

**标签**: `#Smart TVs`, `#Privacy`, `#Surveillance`, `#IoT Security`, `#Consumer Rights`

---

<a id="item-17" class="hz-item-anchor" data-hz-url="https://www.reddit.com/r/opensource/comments/1wa4qh8/vendors_charge_1000mo_for_this_data_im_giving_it/" data-hz-title="Open Jobs以CC0发布三百万条职位信息" data-hz-tags="open data,machine learning,job search,data engineering,labor-market research" data-hz-section="other"></a>
## [Open Jobs 以 CC0 发布三百万条职位信息](https://www.reddit.com/r/opensource/comments/1wa4qh8/vendors_charge_1000mo_for_this_data_im_giving_it/) ⭐️ 8.0/10

Open Jobs 每天从约 6.5 万个公司招聘网站抓取超过 300 万条职位信息。该项目以 CC0 许可发布职位描述、公司和地点信息、职位网址及文本嵌入，并提供本地下载工具和可标记疑似过期或重置日期职位的搜索界面。 这项发布通过免账户、免订阅提供大规模招聘数据，可能降低构建求职产品和开展劳动力市场研究的成本。开放许可也便于进一步使用，而职位质量信号可能帮助用户区分有效职位与日期被重置或疑似过期的职位。 数据以静态 JSON 文件分发，仓库工具可以将所需部分下载为 Parquet 并在本地查询；Parquet 是面向列的数据格式，适合高效分析读取。数据还包含可用于相似度搜索或语义搜索的文本嵌入，但过期职位和日期重置标记是机器学习信号，并不能保证职位状态完全准确。

reddit · r/opensource · /u/OminousLatinWord · 9月7日 21:16

**背景**: 职位爬虫会自动访问公司招聘网站，并收集其中的职位信息。文本嵌入会把文字转换为软件可以按语义比较的数字表示，从而支持语义搜索。CC0 是一种将作品尽可能贡献给公共领域的许可方式，而 Parquet 按列存储数据，有助于提高只读取部分数据时的分析效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacamp.com/tutorial/apache-parquet">Apache Parquet Explained: A Guide for Data Professionals</a></li>
<li><a href="https://medium.com/@dilipmuthuraju/the-power-of-embeddings-unlocking-semantic-search-with-rag-9b4cdaf261db">The Power of Embeddings : Unlocking Semantic Search ... | Medium</a></li>
<li><a href="https://creativecommons.org/public-domain/">Public Domain - Creative Commons</a></li>

</ul>
</details>

**标签**: `#open data`, `#machine learning`, `#job search`, `#data engineering`, `#labor-market research`

---

<a id="item-18" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMirAFBVV95cUxNUWgzTHpRSkhLM2FQYTJvZkpOaUU5QzRyWUV0VXVrOXZkWFdjTUdZajI5QlFZNEo2enEwbThwQ2c3OS1uQndDZGlETmdUT3RXRzV3RElPMGsxOUJBMlBxYmVyRDdPekoxUWN2RTY3LXNFb2F5VzZJTXJ2M192TEdZSG0zT1FwaUZZVmk0dmxfcVktaHFJUFVJYkxFdkJhRXlSVUhOMGtxcTlvUEFB0gGsAUFVX3lxTE1RaDNMelFKSEszYVBhMm9mSk5pRTlDNHJZRXRVdWs5dmRYV2NNR1lqMjlCUVk0SjZ6cTBtOHBDZzc5LW5Cd0NkaUROZ1RPdFdHNXdESU8wazE5QkEyUHFiZXJEN096SjFRY3ZFNjctc0VvYXlXNklNcnYzX3ZMR1lIbTNPUXBpRllWaTR2bF9xWS1ocUlQVUliTEV2QmFFeVJVSE4wa3FxOW9QQUE?oc=5" data-hz-title="IFM 发布 K2 Horizon：从 0.9B 到 375B 的六款 Apache 2.0 模型" data-hz-tags="Open-source AI,Large language models,Model releases,Apache 2.0,AI infrastructure" data-hz-section="other"></a>
## [IFM 发布 K2 Horizon：从 0.9B 到 375B 的六款 Apache 2.0 模型](https://news.google.com/rss/articles/CBMirAFBVV95cUxNUWgzTHpRSkhLM2FQYTJvZkpOaUU5QzRyWUV0VXVrOXZkWFdjTUdZajI5QlFZNEo2enEwbThwQ2c3OS1uQndDZGlETmdUT3RXRzV3RElPMGsxOUJBMlBxYmVyRDdPekoxUWN2RTY3LXNFb2F5VzZJTXJ2M192TEdZSG0zT1FwaUZZVmk0dmxfcVktaHFJUFVJYkxFdkJhRXlSVUhOMGtxcTlvUEFB0gGsAUFVX3lxTE1RaDNMelFKSEszYVBhMm9mSk5pRTlDNHJZRXRVdWs5dmRYV2NNR1lqMjlCUVk0SjZ6cTBtOHBDZzc5LW5Cd0NkaUROZ1RPdFdHNXdESU8wazE5QkEyUHFiZXJEN096SjFRY3ZFNjctc0VvYXlXNklNcnYzX3ZMR1lIbTNPUXBpRllWaTR2bF9xWS1ocUlQVUliTEV2QmFFeVJVSE4wa3FxOW9QQUE?oc=5) ⭐️ 8.0/10

IFM 发布了 K2 Horizon 系列，该系列包含六款采用 Apache 2.0 许可证、参数规模从 0.9B 到 375B 不等的开放模型。

google_news · MarkTechPost · 9月7日 05:00

**标签**: `#Open-source AI`, `#Large language models`, `#Model releases`, `#Apache 2.0`, `#AI infrastructure`

---

<a id="item-19" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiyAFBVV95cUxNNmREaDNjWnlLVzlKeU5tcVRMWW40VFJXaWNFWkZSaVMxd1ZmODR2RWU1emZVLVVXVUVjN0YxOTlKREwtTWF5cW02cTY2Ql83SU5IVnJpZVZkTm93Z3hyOWhFaEpjSDBDODRRc2xaSlh2Y1RObjJvYVVrM0dta19ndnFiVEg5NFdka0p0eUUxQjJQazA5czlHS1RSUFJYTno2WURRRmRnZEFwUTNoemd6MGNDbUkyQWpWS21tUEZxemI5aFE5bm9KWg?oc=5" data-hz-title="朝鲜黑客将木马化HAProxy变成网络流量窃听器" data-hz-tags="Cybersecurity,Supply Chain Security,North Korea,HAProxy,SSL/TLS Interception" data-hz-section="other"></a>
## [朝鲜黑客将木马化 HAProxy 变成网络流量窃听器](https://news.google.com/rss/articles/CBMiyAFBVV95cUxNNmREaDNjWnlLVzlKeU5tcVRMWW40VFJXaWNFWkZSaVMxd1ZmODR2RWU1emZVLVVXVUVjN0YxOTlKREwtTWF5cW02cTY2Ql83SU5IVnJpZVZkTm93Z3hyOWhFaEpjSDBDODRRc2xaSlh2Y1RObjJvYVVrM0dta19ndnFiVEg5NFdka0p0eUUxQjJQazA5czlHS1RSUFJYTno2WURRRmRnZEFwUTNoemd6MGNDbUkyQWpWS21tUEZxemI5aFE5bm9KWg?oc=5) ⭐️ 8.0/10

据报道，朝鲜攻击者将名为 Ted 的后门植入韩国两家机构部署的 HAProxy，使其能够在传输层安全协议终止后截获流量。这起入侵据称把受信任的负载均衡组件变成了监控已解密网络通信的工具。 这起事件表明，攻击者一旦入侵位于受信任通信路径中的基础设施组件，就可能绕过用户对 HTTPS 机密性的依赖。对于使用 HAProxy 集中处理流量和传输层安全策略的机构而言，这也带来了严重的软件供应链和事件响应风险。 据报道，该攻击会替换主机上的合法 HAProxy 二进制文件，因此仅升级软件包可能无法清除恶意文件，除非以干净的方式完成升级并验证主机状态。由于 HAProxy 会在传输层安全协议终止过程中解密流量，位于这一环节的后门可能在内容转发到后端服务前访问明文数据。

google_news · Tech Times · 9月8日 02:56

**背景**: HAProxy 通常作为应用服务器前面的反向代理和负载均衡器使用。在传输层安全协议终止模式下，HAProxy 集中完成传输层安全握手并解密客户端流量，后端服务随后接收并处理解密后的连接。传输层安全拦截或“解密后检查”系统也利用通信路径中的这一位置检查已解密的 HTTPS 内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.haproxy.com/blog/haproxy-ssl-termination">HAProxy SSL Termination (Offloading) in 5 Simple Steps HAProxy SSL Termination Explained - SSL Dragon How to Configure HAProxy SSL Termination - oneuptime.com HAProxy SSL Termination: Offload TLS Without the Headache HAProxy SSL termination | Stack Harbor Knowledge Base HAProxy SSL Certificate Setup - Termination to A+ Grade SSL Termination and Certificate Selection | haproxy/docs ...</a></li>
<li><a href="https://www.techtimes.com/articles/326920/20260907/north-korea-trojanized-haproxy-south-korea-turning-ssl-termination-wiretap.htm">North Korea Trojanized HAProxy in South Korea, Turning SSL...</a></li>
<li><a href="https://www.ivonetworks.com/2021/07/ssl-tls-interception-https-content-inspection/">Emmett O'Brien: SSL / TLS Interception in Enterprise Security | IVO</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#Supply Chain Security`, `#North Korea`, `#HAProxy`, `#SSL/TLS Interception`

---

<a id="item-20" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/7/llm/" data-hz-title="LLM 0.35 新增对 GPT-6 Astra 的支持。" data-hz-tags="LLM,OpenAI,GPT-6 Astra,Developer Tools" data-hz-section="other"></a>
## [LLM 0.35 新增对 GPT-6 Astra 的支持。](https://simonwillison.net/2026/Sep/7/llm/) ⭐️ 7.0/10

Simon Willison 于 2026 年 9 月 7 日发布 LLM 0.35，新增了对 OpenAI 新模型 gpt-6-astra 的支持。 此次更新让开发者能够通过 LLM 的命令行工作流使用 GPT-6 Astra，并扩展了该工具可选的模型范围。该模型面向高级分析、软件工程、研究和长周期智能体任务等高难度工作。 发布公告仅列出了新增的 gpt-6-astra 模型，没有提供配置示例、兼容性说明、基准测试、价格信息或其他改动。外部资料将 GPT-6 Astra 描述为一种专有多模态推理模型，可接收文本和图像输入并生成文本。

rss · Simon Willison · 9月7日 23:54

**背景**: LLM 是 Simon Willison 开发的命令行工具，可用于向大语言模型发送提示词。它还可以把提示词和响应存储在 SQLite 中，为开发者提供可在本地编写脚本的模型交互工作流。GPT-6 Astra 是 OpenAI 的模型，定位于高级推理和持续时间较长的智能体任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/llm: Access large language models from the ...</a></li>
<li><a href="https://simonwillison.net/2026/Sep/7/llm/">Release: llm 0.35 - simonwillison.net</a></li>
<li><a href="https://openrouter.ai/openai/gpt-6-astra">GPT - 6 Astra - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**标签**: `#LLM`, `#OpenAI`, `#GPT-6 Astra`, `#Developer Tools`

---

<a id="item-21" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/7/creepy-crawlies/" data-hz-title="恶意爬虫消耗内核基础设施资源" data-hz-tags="web-crawling,Git,Linux infrastructure,resource management,scraping" data-hz-section="other"></a>
## [恶意爬虫消耗内核基础设施资源](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 7.0/10

Konstantin Ryabitsev 表示，git.kernel.org 用于为恶意爬虫渲染提交页面的 CPU 资源，已经超过了包括 Git 克隆在内的所有其他合法访问。分布在五个地理区域的节点上，始终有 14 个 CPU 核心专门用于将 Git 提交渲染为 HTML。 这份报告表明，自动化抓取带来的基础设施成本可能高于合法用户产生的成本，从而影响代码托管服务的容量和网页性能。它还凸显了一个更广泛的问题：拥有大量可抓取页面的网站，包括可能受到人工智能相关爬虫访问的服务，都可能面临类似压力。 受到影响的工作负载是渲染单个 Git 提交的 HTML 页面，而不是执行 Git 克隆，并且这些负载分布在五个地理区域的节点上。这份报告描述了恶意爬虫造成的运维负担，但没有提出具体的缓解方案，也没有估算由此产生的财务成本。

rss · Simon Willison · 9月7日 23:08

**背景**: Git 是一种版本控制系统，而 git.kernel.org 是 Linux 内核的官方 Git 代码仓库网站。Git 克隆会传输仓库数据供本地使用，而将提交渲染为 HTML 则会生成可供浏览器阅读的网页。爬虫是自动请求网页的程序，恶意爬虫可能在没有为网站带来相应价值的情况下产生大量请求。

**标签**: `#web-crawling`, `#Git`, `#Linux infrastructure`, `#resource management`, `#scraping`

---

<a id="item-22" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/" data-hz-title="Research acceleration: The view inside OpenAI" data-hz-tags="AI research,coding agents,recursive self-improvement,OpenAI,agentic engineering" data-hz-section="other"></a>
## [Research acceleration: The view inside OpenAI](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 7.0/10

Simon Willison examines OpenAI's research-acceleration initiative, focusing on the rapid growth of coding-agent usage and spending among its researchers.

rss · Simon Willison · 9月6日 23:57

**标签**: `#AI research`, `#coding agents`, `#recursive self-improvement`, `#OpenAI`, `#agentic engineering`

---

<a id="item-23" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMihgFBVV95cUxQbDFrSE13REZkLVN1OFU1ZkIwU1hKaHg5bmtmVUtHQWh3Y0NSQ2JMTW9wdXpCcG01bU1pWkRZUHF6azBDQ0dCRUZiT3Exek9XSFE5SHc3NmU2TGZvUHoyRGktOWo4d1BOS01qZHplMzI4WERiQjE2MEVoNFprNWlxNUlJcHBtdw?oc=5" data-hz-title="Axis Robotics 开源大型 Franka 机械臂仿真数据集" data-hz-tags="Robotics,Physical AI,Simulation,Open Source,Datasets" data-hz-section="other"></a>
## [Axis Robotics 开源大型 Franka 机械臂仿真数据集](https://news.google.com/rss/articles/CBMihgFBVV95cUxQbDFrSE13REZkLVN1OFU1ZkIwU1hKaHg5bmtmVUtHQWh3Y0NSQ2JMTW9wdXpCcG01bU1pWkRZUHF6azBDQ0dCRUZiT3Exek9XSFE5SHc3NmU2TGZvUHoyRGktOWo4d1BOS01qZHplMzI4WERiQjE2MEVoNFprNWlxNUlJcHBtdw?oc=5) ⭐️ 7.0/10

Axis Robotics 发布了一个面向物理人工智能和机器人研究的 Franka 机械臂开源仿真数据集。相关搜索结果标题称，AXIS 数据引擎包含 207 个机器人操作任务和 50,129 条轨迹。 开放的仿真数据可以提高物理人工智能研究的可复现性，并降低训练和评估机器人操作系统所需的成本。大型共享数据集还可能帮助研究人员在将方法部署到实体机器人之前，基于共同任务进行比较。 现有材料明确提到了 Franka 机械臂、仿真环境和开源发布，相关结果则报告了 207 个任务和 50,129 条轨迹。提供的报道没有说明数据集许可证、文件格式、仿真平台、任务分布，也没有说明仿真轨迹与真实机器人行为的接近程度。

google_news · BeInCrypto · 9月7日 09:01

**背景**: 这里的物理人工智能是指通过机器人感知并作用于现实世界的人工智能系统。仿真数据集包含在虚拟环境中生成的机器人经验，例如动作、状态和轨迹，使研究人员无需反复使用实体硬件就能开发和测试操作方法。Franka 机械臂常用于科研，因此面向该平台的数据可以支持不同团队开展可比较的实验。

**标签**: `#Robotics`, `#Physical AI`, `#Simulation`, `#Open Source`, `#Datasets`

---

<a id="item-24" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMilgFBVV95cUxPNTA0eXhUMm1CN0hkM0hFU05xY0JQdGkwd3k5Qk9RcDI1bENFU1RYVzR6clpEWElrUmpDSVJTdUExZGJOZU9MMEtZUmQxdlF1Z0YtdnRVT1lhbExzM3kzakZiTTFwUU1yR2g5VUFlZXBBNk1VVkt4Wmh3MWt6Z3R0NlZkTHNqdDJpRm5fMHJHNHhpUHV1Mmc?oc=5" data-hz-title="NVIDIA 为开源 Nova 驱动加入虚拟 GPU 支持" data-hz-tags="NVIDIA,Nova Driver,GPU Virtualization,Open Source,Linux" data-hz-section="other"></a>
## [NVIDIA 为开源 Nova 驱动加入虚拟 GPU 支持](https://news.google.com/rss/articles/CBMilgFBVV95cUxPNTA0eXhUMm1CN0hkM0hFU05xY0JQdGkwd3k5Qk9RcDI1bENFU1RYVzR6clpEWElrUmpDSVJTdUExZGJOZU9MMEtZUmQxdlF1Z0YtdnRVT1lhbExzM3kzakZiTTFwUU1yR2g5VUFlZXBBNk1VVkt4Wmh3MWt6Z3R0NlZkTHNqdDJpRm5fMHJHNHhpUHV1Mmc?oc=5) ⭐️ 7.0/10

NVIDIA 已为其开源 Nova 驱动加入虚拟 GPU 支持。这一变化扩展了 Nova 在虚拟化和共享 GPU 工作负载方面的能力。 这项更新可能让开源 Linux 驱动更适用于在多个虚拟机之间共享 GPU 资源的云计算和企业环境。它也可能推动 NVIDIA 开源驱动获得更广泛的采用，但现有报道尚未说明该功能的实际范围或成熟度。 现有信息只确认了虚拟 GPU 支持是此次变化的核心，但没有说明支持的 GPU 型号、软件版本、性能、许可方式或部署限制。所提供的材料也没有包含社区反馈或更多技术文档。

google_news · opensourceforu.com · 9月7日 08:08

**背景**: 虚拟 GPU 可以将 GPU 资源提供给虚拟机或相互独立的工作负载，而不是只分配给单个操作系统实例。Nova 是 NVIDIA 面向 Linux 图形硬件的开源驱动项目，因此加入虚拟 GPU 支持后，该项目便与虚拟化和资源共享场景建立了联系。

**标签**: `#NVIDIA`, `#Nova Driver`, `#GPU Virtualization`, `#Open Source`, `#Linux`

---

<a id="item-25" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiY0FVX3lxTE9obmt5VzZaaXpsMmdkWjBVSEVqTFFZTUhwQ3AtREhidS1pWkZjVDFpV1RBRFhDR3g3OUFEYVVidmRBc1JGbzh6TURjTW1aTkJwUGNkZndWSjc5UG1wdTdJNmZOc9IBY0FVX3lxTE9obmt5VzZaaXpsMmdkWjBVSEVqTFFZTUhwQ3AtREhidS1pWkZjVDFpV1RBRFhDR3g3OUFEYVVidmRBc1JGbzh6TURjTW1aTkJwUGNkZndWSjc5UG1wdTdJNmZOcw?oc=5" data-hz-title="据报道朝鲜黑客利用人工智能扩大钓鱼攻击" data-hz-tags="Cybersecurity,Artificial Intelligence,Phishing,North Korea,Cyber Threats" data-hz-section="other"></a>
## [据报道朝鲜黑客利用人工智能扩大钓鱼攻击](https://news.google.com/rss/articles/CBMiY0FVX3lxTE9obmt5VzZaaXpsMmdkWjBVSEVqTFFZTUhwQ3AtREhidS1pWkZjVDFpV1RBRFhDR3g3OUFEYVVidmRBc1JGbzh6TURjTW1aTkJwUGNkZndWSjc5UG1wdTdJNmZOc9IBY0FVX3lxTE9obmt5VzZaaXpsMmdkWjBVSEVqTFFZTUhwQ3AtREhidS1pWkZjVDFpV1RBRFhDR3g3OUFEYVVidmRBc1JGbzh6TURjTW1aTkJwUGNkZndWSjc5UG1wdTdJNmZOcw?oc=5) ⭐️ 7.0/10

据报道，朝鲜黑客正利用人工智能批量生成具有迷惑性的钓鱼文件，用于网络间谍活动和其他恶意行动。这一发展表明，人工智能正在提升其社会工程材料的产量和可信度。 人工智能辅助生成文件，可能让国家支持的攻击者以更低成本开展更加个性化的钓鱼活动，并减少语言或排版错误。这会增加组织的防御压力，因为它们不能再主要依靠明显的语法错误或通用措辞来识别钓鱼信息。 现有报道没有指出具体的朝鲜组织、人工智能模型、文件类型、受害者名单或经过确认的行动时间线，因此具体行动细节仍然有限。关于人工智能增强型钓鱼攻击的现有报道表明，大规模个性化和专业排版可能会消除传统的警示特征。

google_news · cyberpress.org · 9月7日 10:44

**背景**: 钓鱼攻击是一种社会工程技术，攻击者通过欺骗性消息或文件，诱使收件人泄露信息、打开恶意内容或执行其他不安全操作。人工智能可以帮助攻击者生成语法正确、与个人相关且排版专业的文本，使以往的识别建议变得不那么可靠。政府网络安全机构还指出，朝鲜国家支持的网络活动持续威胁多个国家和行业的组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hyve.com/insights/how-ai-is-changing-cyberattacks-and-security-defences/?trk=article-ssr-frontend-pulse_little-text-block">How AI is Changing Cyberattacks and... | Hyve Managed Hosting</a></li>
<li><a href="https://www.cisa.gov/topics/cyber-threats-and-advisories/advanced-persistent-threats/north-korea">North Korea Threat Overview and Advisories - CISA</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#Artificial Intelligence`, `#Phishing`, `#North Korea`, `#Cyber Threats`

---

<a id="item-26" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiekFVX3lxTE1sZ09XbERfZHp5bkZYMVJFTUdRWlR6M0l2clN5VGhxX1B1RG5oN2MxRWhqNjJfTW43MkxMMWN1YXoyM2YwU3J6dEZJck9qbkJ3NFdWcVBiTWhlek9WOGdBRld1WXJiQzhWWTFNaTBBN3ZIWW9VR1E4RHBn0gGOAUFVX3lxTE8wX3h5Y2cyeHlLT0dGc05xUk5JOGNTa1ZvZXFFMGdnejA1LW1FTFJITnhzWnpYYUhDQ0RDaDE2SmVuYnFVZVRxXzFZdE0zRkdkZHVhcDNET0sySk4tUU82ekxYM0hLelJZNkJwS0lFcGQzTDZ1bXQ3eXA2ZUJqdl9Pai14b2JBRzBYdkc4X0E?oc=5" data-hz-title="Kimsuky据报道在韩国使用人工智能编程代理" data-hz-tags="Cybersecurity,AI Agents,Nation-State Threats,North Korea,Threat Intelligence" data-hz-section="other"></a>
## [Kimsuky 据报道在韩国使用人工智能编程代理](https://news.google.com/rss/articles/CBMiekFVX3lxTE1sZ09XbERfZHp5bkZYMVJFTUdRWlR6M0l2clN5VGhxX1B1RG5oN2MxRWhqNjJfTW43MkxMMWN1YXoyM2YwU3J6dEZJck9qbkJ3NFdWcVBiTWhlek9WOGdBRld1WXJiQzhWWTFNaTBBN3ZIWW9VR1E4RHBn0gGOAUFVX3lxTE8wX3h5Y2cyeHlLT0dGc05xUk5JOGNTa1ZvZXFFMGdnejA1LW1FTFJITnhzWnpYYUhDQ0RDaDE2SmVuYnFVZVRxXzFZdE0zRkdkZHVhcDNET0sySk4tUU82ekxYM0hLelJZNkJwS0lFcGQzTDZ1bXQ3eXA2ZUJqdl9Pai14b2JBRzBYdkc4X0E?oc=5) ⭐️ 7.0/10

据报道，Kimsuky 利用人工智能编程代理支持针对韩国高端主题机构的网络攻击。现有报道没有提供具体的恶意软件名称、目标、工具或行动日期。 这则报道表明，生成式人工智能可能帮助与国家有关联的威胁组织加快网络攻击行动。这使依赖传统恶意软件检测的机构面临更快速、更灵活的攻击风险。 现有材料只有标题和简短摘要，因此无法仅凭所提供的证据确认人工智能的参与程度或据称使用的攻击技术。相关报道将人工智能辅助恶意软件生成描述为一种新兴趋势，但没有证明这些额外事实适用于此次具体事件。

google_news · Chosunbiz · 9月7日 01:14

**背景**: Kimsuky 是一个来自朝鲜的网络间谍组织，至少从 2012 年起就持续活动。MITRE ATT&CK 指出，该组织最初主要针对韩国政府机构、智库和各领域专家。人工智能编程代理是能够根据自然语言指令生成或修改代码的软件助手，因此可能减少创建恶意软件所需的时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://attack.mitre.org/groups/G0094/">Kimsuky , Black Banshee, Velvet Chollima, Emerald... | MITRE ATT&CK</a></li>
<li><a href="https://www.picussecurity.com/resource/blog/exposing-the-steps-of-the-kimsuky-apt-group">Exposing the Steps of the Kimsuky APT Group</a></li>
<li><a href="https://blog.barracuda.com/2024/04/16/5-ways-cybercriminals-are-using-ai--malware-generation">5 Ways cybercriminals are using AI : Malware generation</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#AI Agents`, `#Nation-State Threats`, `#North Korea`, `#Threat Intelligence`

---

<a id="item-27" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiggFBVV95cUxOR1ZwWEpZVW1Za2kzTDg2VUZnSlhnNVJLa1lWWDVxQktMYmpNN1hYS0NkS3ZGZ0dWekxiNlFyaDZFOGdsVWtXVDhCWmNlVVdFaTliTDJNUU54OTljMDJub01rZi1SSWlCcThmMTEyNGNFeWZFM3o2bzkxMDFKTndJaEZ3?oc=5" data-hz-title="Perplexity推出开源工具Numbat追踪失控AI代理" data-hz-tags="AI agents,AI safety,Open source,Observability,Perplexity" data-hz-section="other"></a>
## [Perplexity 推出开源工具 Numbat 追踪失控 AI 代理](https://news.google.com/rss/articles/CBMiggFBVV95cUxOR1ZwWEpZVW1Za2kzTDg2VUZnSlhnNVJLa1lWWDVxQktMYmpNN1hYS0NkS3ZGZ0dWekxiNlFyaDZFOGdsVWtXVDhCWmNlVVdFaTliTDJNUU54OTljMDJub01rZi1SSWlCcThmMTEyNGNFeWZFM3o2bzkxMDFKTndJaEZ3?oc=5) ⭐️ 7.0/10

Perplexity 推出了开源工具 Numbat，用于检测和追踪可能失控的 AI 代理。现有信息没有说明其发布日期、实现细节或评测结果。 随着 AI 代理变得更加自主，监控其行为对 AI 安全和系统可观测性越来越重要。开源追踪工具可能帮助开发者和运营人员调查代理的异常活动，但其实际影响取决于 Numbat 的能力和采用情况。 报道将 Numbat 描述为面向可能失控 AI 代理的开源工具，但没有提供其支持的代理类型、检测方法、部署要求或已知限制等技术信息。“失控”表示行为可能出乎预期或难以控制，并不等于确认代理具有恶意。

google_news · YourStory.com · 9月7日 11:55

**背景**: AI 代理是能够以一定程度自主性执行任务的软件系统。可观测性是指收集和检查系统行为信息，以帮助识别异常活动。在这一语境中，追踪失控代理意味着监控代理的行动，以发现可能不受控制或不符合预期的行为。

**标签**: `#AI agents`, `#AI safety`, `#Open source`, `#Observability`, `#Perplexity`

---

<a id="item-28" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/7/jakub-pachocki/" data-hz-title="Pachocki：防御人工智能威胁可能需要更先进的人工智能" data-hz-tags="AI safety,AI governance,OpenAI,AI ethics" data-hz-section="other"></a>
## [Pachocki：防御人工智能威胁可能需要更先进的人工智能](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 6.0/10

OpenAI 首席科学家 Jakub Pachocki 认为，快速训练更强大的模型可能是构建防御系统、应对其他人工智能系统威胁的必要条件。他同时警告，安全理由不能成为鲁莽开发或不计代价竞赛的借口。 这一观点将先进人工智能同时视为风险来源和保护基础设施、实时应对失控智能体的潜在工具。它凸显了人工智能治理中的核心矛盾：防御能力可能需要快速进步，但快速进步也可能放大治理试图控制的风险。 Pachocki 具体提到，保护基础设施、实时防御失控智能体以及发明全新的防护措施将是部署重点。这段话是一种战略立场，而不是技术方案，也没有证明能力更强的模型一定能可靠地提供这些防御能力。

rss · Simon Willison · 9月7日 22:26

**背景**: 人工智能对齐是指让人工智能系统的目标和行为符合人类的价值观、规则与意图。在这一语境中，对齐的系统可能帮助保护基础设施或应对有害的自主系统，而失控智能体则是可能探测、利用或绕过传统安全控制的自主系统。因此，这段话将模型能力与防御潜力及额外的安全风险联系在了一起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/ai-alignment">What is AI alignment? - IBM</a></li>
<li><a href="https://blog.barracuda.com/2026/08/31/rogue-ai-agents-cybersecurity-risk">What rogue AI agents teach us about cybersecurity risk</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI governance`, `#OpenAI`, `#AI ethics`

---

<a id="item-29" class="hz-item-anchor" data-hz-url="https://marginalrevolution.com/marginalrevolution/2026/09/will-new-transportation-technologies-increase-urban-density.html?utm_source=rss&utm_medium=rss&utm_campaign=will-new-transportation-technologies-increase-urban-density" data-hz-title="新交通技术如何重塑城市密度" data-hz-tags="Urban Economics,Transportation Technology,Urban Density,Economic Models" data-hz-section="other"></a>
## [新交通技术如何重塑城市密度](https://marginalrevolution.com/marginalrevolution/2026/09/will-new-transportation-technologies-increase-urban-density.html?utm_source=rss&utm_medium=rss&utm_campaign=will-new-transportation-technologies-increase-urban-density) ⭐️ 6.0/10

文章考察 21 世纪的交通创新会像 20 世纪的汽车一样推动城市分散，还是会像 19 世纪的铁路一样强化城市集中。文章指出，在出行次数具有内生性的情况下，经典模型中“通勤成本下降会降低城市集中度”的结论可能发生逆转。 这一分析质疑了“通勤更快或更便宜必然会推动城市发展外扩”的假设。它有助于理解新兴交通技术可能如何影响城市密度以及城市空间结构。 关键区别在于，模型可以假设出行次数固定，也可以允许出行需求随着通勤成本下降而变化。文章摘录没有指出某一种具体的新交通技术，也没有提供其对城市密度影响的量化预测。

rss · Marginal Revolution · 9月8日 04:56

**背景**: Alonso-Muth-Mills 模型是城市经济学中的经典框架，用于研究通勤成本、土地利用和城市集中度之间的关系。在标准设定中，通勤成本下降会让人们和经济活动更容易布局在远离城市中心的地方，从而降低集中度。但如果出行次数具有内生性，较低的交通成本也可能鼓励更多出行，进而改变这一预测。

**标签**: `#Urban Economics`, `#Transportation Technology`, `#Urban Density`, `#Economic Models`

---

<a id="item-30" class="hz-item-anchor" data-hz-url="https://marginalrevolution.com/marginalrevolution/2026/09/capital-gains-vs-wealth-taxes.html?utm_source=rss&utm_medium=rss&utm_campaign=capital-gains-vs-wealth-taxes" data-hz-title="新模型比较资本利得税与财富税" data-hz-tags="Optimal taxation,Capital gains tax,Wealth tax,Asset pricing,Public economics" data-hz-section="other"></a>
## [新模型比较资本利得税与财富税](https://marginalrevolution.com/marginalrevolution/2026/09/capital-gains-vs-wealth-taxes.html?utm_source=rss&utm_medium=rss&utm_campaign=capital-gains-vs-wealth-taxes) ⭐️ 6.0/10

这项研究通过将资产价格波动纳入模型，扩展了标准的最优资本税理论，以评估再分配税收政策。该研究采用现代金融学观点，认为资产价格变化既源于现金流变化，也源于其他市场因素。 通过纳入资产价格波动，该框架可以改进对资本利得税和财富税的比较。它可能帮助公共经济学研究者评估：当资产价值因与当前现金流无关的原因变化时，再分配政策应如何回应。 节选内容没有提供模型的具体假设、数学结果或政策建议。其主要局限是研究贡献仅被概括性地介绍，因此无法根据现有文本判断资本利得税与财富税哪一种更具优势。

rss · Marginal Revolution · 9月7日 07:47

**背景**: 最优资本税理论研究政府应如何对资本征税，同时平衡再分配目标与经济激励。资本利得税针对资产价值的增加征税，而财富税针对资产本身的价值征税。资产价格既可能反映预期或变化中的现金流，也可能受到其他市场因素影响，因此将价格变化视为收入可能会改变相关分析。

**标签**: `#Optimal taxation`, `#Capital gains tax`, `#Wealth tax`, `#Asset pricing`, `#Public economics`

---

<a id="item-31" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMikgFBVV95cUxOblN0NUtYX1AyV3hSWURVbU92RklTM3gxcm9WNUMyWHh2czIzYldDWTg2ZF9IckRMTmJZbklaSlpSaHlJRUNzOFV3cTRqNUMtQ1owTk1iU1QtWHg0aTdXdnVhSEhfZllLTnRXaUZLMHo4eHMtOG9GSGg4RVl0a0ZwRHJXZXVQZ1R0OTFtZWVzdDZyQQ?oc=5" data-hz-title="人工智能传感器实现无塑料微塑料检测" data-hz-tags="AI-assisted sensing,Microplastics,Environmental monitoring,Biosensors" data-hz-section="other"></a>
## [人工智能传感器实现无塑料微塑料检测](https://news.google.com/rss/articles/CBMikgFBVV95cUxOblN0NUtYX1AyV3hSWURVbU92RklTM3gxcm9WNUMyWHh2czIzYldDWTg2ZF9IckRMTmJZbklaSlpSaHlJRUNzOFV3cTRqNUMtQ1owTk1iU1QtWHg0aTdXdnVhSEhfZllLTnRXaUZLMHo4eHMtOG9GSGg4RVl0a0ZwRHJXZXVQZ1R0OTFtZWVzdDZyQQ?oc=5) ⭐️ 6.0/10

研究人员展示了一种无塑料、开源的人工智能辅助流式成像传感器原型，用于检测微塑料颗粒并估算其尺寸。该方法旨在无需依赖塑料制检测材料即可开展实验室评估。 微塑料广泛存在于水生环境中，但对其进行定量检测仍然困难。无塑料成像系统有望减少材料引入污染的担忧，并支持更易开展的环境监测，但其实际影响仍取决于进一步验证。 据报道，该系统将流式成像与人工智能辅助分析结合起来，并作为用于实验室检测和颗粒尺寸估算的开源原型提出。现有信息尚未说明它对不同塑料类型的准确性、检测限、现场表现，或相对于现有方法的优势。

google_news · Bioengineer.org · 9月8日 01:37

**背景**: 微塑料是存在于水等环境中的微小塑料颗粒，其定量检测通常需要判断颗粒是否存在，并估算其尺寸。流式成像会记录颗粒通过检测系统时的图像，而人工智能辅助分析则帮助解读这些图像。开源原型能够让实验室更容易获取和评估相关设计与软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bioengineer.org/ai-assisted-sensing-enables-plastic-free-microplastic-detection/">AI - Assisted Sensing Enables Plastic - Free Microplastic Detection</a></li>
<li><a href="https://link.springer.com/article/10.1186/s43591-026-00180-x">Zero- plastic : AI - assisted sensing for microplastic assessment</a></li>

</ul>
</details>

**标签**: `#AI-assisted sensing`, `#Microplastics`, `#Environmental monitoring`, `#Biosensors`

---

<a id="item-32" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMi0AFBVV95cUxPcUwxUlllOUJicXpPbVhPekVUb1JKREVtZmdVRUxPSThPZkNKamZONDdPMkhLMU95aWdxRERhZDVQdUt2VWUxd3g0eTVoekN1cnM2LVZHODd0dTRLT0lpclFWN0x3SFdKYklDdlBOUVRoajh5eGhwdlIyWWRFalJjdkRZc1dWaGZBekRZYUVGSmlOVnNzRERUTGN1Z2ZySWtLRzZBazlKRTFxbTZvNlNoc0x3MFBOSlJJSUNNcE93UzhSWWtuNl9Gc1BzT2hkUlZM0gHYAUFVX3lxTE5XSFAxQlp1b3ZLMU5McG1YQW9ueDVWOUo1S0NpUjlnTTg0U2ZURVd1eHBiM0dTOElhUDBoUzJDVVhZb1lJRmtGVFdHRGJoZTFDTm00YmlYM01kZjE4Vmo2YWhVa0RuUjhaSjlYbFp4N3o1bzJfenA4YmtBNjhBZjVtQkMwYmRWa3dpelloQ2hwellDa3IyNXJINFNCZEE5Q292aDBvNXZYanpCWnJQR1pLRjJwY1JTcVhlR2ExcHpsNWdPb3E4S01DRzFoMXNCYnZsaVJWUDYtbw?oc=5" data-hz-title="YuzukiNeko 将支持 Linux 的 RISC-V 装入 Pico 尺寸单板机" data-hz-tags="RISC-V,Linux,Single-board computers,Embedded systems,Allwinner" data-hz-section="other"></a>
## [YuzukiNeko 将支持 Linux 的 RISC-V 装入 Pico 尺寸单板机](https://news.google.com/rss/articles/CBMi0AFBVV95cUxPcUwxUlllOUJicXpPbVhPekVUb1JKREVtZmdVRUxPSThPZkNKamZONDdPMkhLMU95aWdxRERhZDVQdUt2VWUxd3g0eTVoekN1cnM2LVZHODd0dTRLT0lpclFWN0x3SFdKYklDdlBOUVRoajh5eGhwdlIyWWRFalJjdkRZc1dWaGZBekRZYUVGSmlOVnNzRERUTGN1Z2ZySWtLRzZBazlKRTFxbTZvNlNoc0x3MFBOSlJJSUNNcE93UzhSWWtuNl9Gc1BzT2hkUlZM0gHYAUFVX3lxTE5XSFAxQlp1b3ZLMU5McG1YQW9ueDVWOUo1S0NpUjlnTTg0U2ZURVd1eHBiM0dTOElhUDBoUzJDVVhZb1lJRmtGVFdHRGJoZTFDTm00YmlYM01kZjE4Vmo2YWhVa0RuUjhaSjlYbFp4N3o1bzJfenA4YmtBNjhBZjVtQkMwYmRWa3dpelloQ2hwellDa3IyNXJINFNCZEE5Q292aDBvNXZYanpCWnJQR1pLRjJwY1JTcVhlR2ExcHpsNWdPb3E4S01DRzFoMXNCYnZsaVJWUDYtbw?oc=5) ⭐️ 6.0/10

YuzukiNeko 是一款采用全志 F101 RISC-V 系统级芯片的紧凑型单板计算机，尺寸接近 Raspberry Pi Pico，并支持 Linux。该板配备 SPI NOR 闪存、microSD 卡槽、USB-C 接口和两个 20 针 GPIO 排针。 这款开发板将支持 Linux 的计算能力与熟悉的小型 Pico 外形结合起来，为嵌入式开发者提供了区别于微控制器级 Pico 开发板的另一种选择。它也丰富了面向实验和嵌入式 Linux 项目的紧凑型 RISC-V 硬件生态。 现有信息明确了该板的存储和扩展接口，但没有提供其广泛供货情况、性能测试结果或 F101 完整的软件支持状态。与尺寸更大的单板计算机相比，其紧凑外形也可能限制扩展能力和散热余量。

google_news · CNX Software · 9月7日 17:01

**背景**: 单板计算机将处理器、与内存相关的电路、存储接口和扩展连接器集成在一块电路板上。RISC-V 是一种开放的指令集架构，而 Linux 通常能提供比微控制器固件更丰富的软件环境。Raspberry Pi Pico 外形尺寸指的是与 Pico 开发板相近的紧凑物理尺寸和布局类别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cnx-software.ru/2026/09/08/yuzukineko-odnoplatnyj-kompyuter-na-allwinner-f101-risc-v-s-podderzhkoj-linux-v-form-faktore-raspberry-pi-pico/">YuzukiNeko — одноплатный компьютер на Allwinner F 101 ...</a></li>

</ul>
</details>

**标签**: `#RISC-V`, `#Linux`, `#Single-board computers`, `#Embedded systems`, `#Allwinner`

---

<a id="item-33" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMioAFBVV95cUxPMFdnd0pWclA2M3BZVkJoYjFhenVIUnp2RXZzcmhZcFRRUmFMcVBFUm1lNkVFQ2JqM1NtQ1owdWtIc2lMdTV6dE9MSU5lNm41R3p1a1pheWF3MUVoc3BKU1l1bWZydl9PVTZodzBxeWRDRzhRV2NSb0ZzUmJQZTFybnVnem5XYlBTUTJ5cHEtU3NyaU1zaFo3djZKamVBR3Y0?oc=5" data-hz-title="优化方法识别软件生态系统中的重叠社区" data-hz-tags="Software Engineering,Network Analysis,Community Detection,Optimization,Systems Research" data-hz-section="other"></a>
## [优化方法识别软件生态系统中的重叠社区](https://news.google.com/rss/articles/CBMioAFBVV95cUxPMFdnd0pWclA2M3BZVkJoYjFhenVIUnp2RXZzcmhZcFRRUmFMcVBFUm1lNkVFQ2JqM1NtQ1owdWtIc2lMdTV6dE9MSU5lNm41R3p1a1pheWF3MUVoc3BKU1l1bWZydl9PVTZodzBxeWRDRzhRV2NSb0ZzUmJQZTFybnVnem5XYlBTUTJ5cHEtU3NyaU1zaFo3djZKamVBR3Y0?oc=5) ⭐️ 6.0/10

研究人员开发了一种用于识别软件生态系统中重叠社区的优化方法。现有报道没有说明该方法的具体形式、评估数据或性能指标。 识别重叠社区有助于研究人员分析软件项目、库、平台及其他生态参与者之间的关系，因为同一个节点可能同时属于多个群体。不过，在验证准确性、可扩展性以及相较现有算法的优势之前，该方法的实际影响仍不确定。 重叠社区检测不同于将每个网络节点只分配给一个社区的方法，而软件生态系统可以表示为包含项目和利益相关者的复杂网络。报道没有提供优化目标、网络类型、计算成本或实验结果等信息。

google_news · Bioengineer.org · 9月7日 10:54

**背景**: 软件生态系统是由软件项目和参与者组成的网络，它们通过依赖关系或平台交互等方式相互连接。在重叠结构中，一个项目或参与者可能同时属于多个社区。社区检测研究包括团渗透和标签传播等方法，用于发现这种共享成员关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/1110.5813">Overlapping Community Detection in Networks : the State of the Art...</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3418209">Fine-Grained Network Analysis for Modern Software Ecosystems</a></li>

</ul>
</details>

**标签**: `#Software Engineering`, `#Network Analysis`, `#Community Detection`, `#Optimization`, `#Systems Research`

---

<a id="item-34" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiogFBVV95cUxPa0tpU3NJS0hJQkJYWkNDdTNlNWdjQXUwX3A0enptZEdiLVBfSHNmTEl1ckowbmZfT0pUbERPbE1ETTBZZ3JFamRqSGJJUk5xZ1B3NXZNZ2c0dkNrYmt0bjJCR0JpX1ktWk00Nm40bVVBOHoyOVJCcjg3aTRpS0VlQkVXRDZycFczbFlfM094VzZqLThOeHplU2g5bFhRak9QZWc?oc=5" data-hz-title="开源鳍射线夹爪支持多机器人协同操作" data-hz-tags="robotics,open source hardware,robotic manipulation,multi-robot systems" data-hz-section="other"></a>
## [开源鳍射线夹爪支持多机器人协同操作](https://news.google.com/rss/articles/CBMiogFBVV95cUxPa0tpU3NJS0hJQkJYWkNDdTNlNWdjQXUwX3A0enptZEdiLVBfSHNmTEl1ckowbmZfT0pUbERPbE1ETTBZZ3JFamRqSGJJUk5xZ1B3NXZNZ2c0dkNrYmt0bjJCR0JpX1ktWk00Nm40bVVBOHoyOVJCcjg3aTRpS0VlQkVXRDZycFczbFlfM094VzZqLThOeHplU2g5bFhRak9QZWc?oc=5) ⭐️ 6.0/10

一款开源、可三维打印的软体机器人夹爪将鳍射线效应、力传感和低成本电子设备结合起来，用于协同操作。该设计被定位为支持多台机器人协调工作的基础部件。 开放硬件和可三维打印部件可能降低协作机器人与多机器人操作研究的成本和开发门槛。柔顺夹爪还可能帮助机器人更安全、更灵活地处理形状各异的物体。 受鳍射线效应启发的手指由柔性侧壁和横向支撑条连接而成，系统还加入了力传感和低成本电子设备。现有信息尚未说明具体负载、精度、耐久性或多机器人演示效果。

google_news · opensourceforu.com · 9月7日 08:25

**背景**: 鳍射线效应源于鱼鳍的变形方式，可用于制造能够适应物体形状的夹爪手指。与刚性夹爪相比，软体机器人夹爪通常更柔韧、更轻，但控制和反馈可能更加困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.opensourceforu.com/2026/09/open-source-fin-ray-gripper-enables-multi-robot-manipulation/">Open - Source Fin - Ray Gripper Enables Multi-Robot Manipulation...</a></li>
<li><a href="https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2016.00070/full">Frontiers | Fin Ray® Effect Inspired Soft Robotic Gripper ...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#open source hardware`, `#robotic manipulation`, `#multi-robot systems`

---

<a id="item-35" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMibkFVX3lxTFBCRHpCOXVCVUwxV1FyUWJMblNRYk5OR1QtWkNXMnN1VmxWcTBKX2xkQVFtT0hfbTZ0dkpRckVaZjYwTE9Tc3dvSV9QSVRMN2xzLVE1M3daSk1pOGpvdjlSaUJfQWY1N1oxUzBvU0Jn0gFuQVVfeXFMUEJEekI5dUJVTDFXUXJRYkxuU1FiTk5HVC1aQ1cyc3VWbFZxMEpfbGRBUW1PSF9tNnR2SlFyRVpmNjBMT1Nzd29JX1BJVEw3bHMtUTUzd1pKTWk4am92OVJpQl9BZjU3WjFTMG9TQmc?oc=5" data-hz-title="金融行为监管局警告金融机构应对人工智能安全问题不堪重负" data-hz-tags="AI security,金融 regulation,cybersecurity,financial services,risk management" data-hz-section="other"></a>
## [金融行为监管局警告金融机构应对人工智能安全问题不堪重负](https://news.google.com/rss/articles/CBMibkFVX3lxTFBCRHpCOXVCVUwxV1FyUWJMblNRYk5OR1QtWkNXMnN1VmxWcTBKX2xkQVFtT0hfbTZ0dkpRckVaZjYwTE9Tc3dvSV9QSVRMN2xzLVE1M3daSk1pOGpvdjlSaUJfQWY1N1oxUzBvU0Jn0gFuQVVfeXFMUEJEekI5dUJVTDFXUXJRYkxuU1FiTk5HVC1aQ1cyc3VWbFZxMEpfbGRBUW1PSF9tNnR2SlFyRVpmNjBMT1Nzd29JX1BJVEw3bHMtUTUzd1pKTWk4am92OVJpQl9BZjU3WjFTMG9TQmc?oc=5) ⭐️ 6.0/10

金融行为监管局警告称，金融机构在采用人工智能的过程中，正受到大量相关安全问题发现的冲击。监管机构敦促这些机构加强风险识别、评估和管理。 这一警告表明，人工智能的应用正在增加金融服务机构的网络安全工作负担。风险管理流程薄弱，可能使机构更难有效应对人工智能相关的安全问题。 现有报道没有提供安全问题发现的具体数量、已公开事件或技术细节。报道的核心信息是，金融机构需要更完善的流程，以管理人工智能应用带来的大量风险及其重要性。

google_news · Silicon UK · 9月7日 07:43

**背景**: 人工智能应用是指金融机构将人工智能引入产品、服务或内部运营。安全问题发现是指需要调查和修复的已识别弱点或风险。风险管理则是评估这些问题并决定如何处理的过程。

**标签**: `#AI security`, `#金融 regulation`, `#cybersecurity`, `#financial services`, `#risk management`

---

<a id="item-36" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiowFBVV95cUxPZVU5WXZsVW9ibVl5ekpCNUJFdFo0LTZKUXFuX1Z5SDRGR01NR0VLVTEzb3NyX000QUlsNUFKb1F6QVB6R0paNWFoaXdvTkx4NW4tSEVmWTJ1SDFGbnhRdW4zeVJMSTRZalcwekZEZGFfYzdyZHoyWW5OT0dYbG85a0RqOWx5bzg0NF9fREo1Q2hlcl9PdFpFTE1CQ3drb0Nudmpr0gGoAUFVX3lxTE1rdmpPZkRJZHNoZHQ2OUt6TGhNMnllV0JuZnIwMEcxWXhOS0hYaUNlVXZfTGxlUnNpUFhGSVBQdFpRd0ZiWng3Vkg4WXdmcVlLOTJUQ003bGF5TzlaTTJGOXRmcHk3UzFtRkdRODh6eTFvaTdJakZiaDlaTll2X25HbjZxRW1EcDVwSEdHVkRVbURiVWNSd081cUFZWFNqT1pEM05IejNOYw?oc=5" data-hz-title="Figma称AI智能代理将安全警报处理提速70%" data-hz-tags="AI agents,cybersecurity,security operations,Figma,automation" data-hz-section="other"></a>
## [Figma 称 AI 智能代理将安全警报处理提速 70%](https://news.google.com/rss/articles/CBMiowFBVV95cUxPZVU5WXZsVW9ibVl5ekpCNUJFdFo0LTZKUXFuX1Z5SDRGR01NR0VLVTEzb3NyX000QUlsNUFKb1F6QVB6R0paNWFoaXdvTkx4NW4tSEVmWTJ1SDFGbnhRdW4zeVJMSTRZalcwekZEZGFfYzdyZHoyWW5OT0dYbG85a0RqOWx5bzg0NF9fREo1Q2hlcl9PdFpFTE1CQ3drb0Nudmpr0gGoAUFVX3lxTE1rdmpPZkRJZHNoZHQ2OUt6TGhNMnllV0JuZnIwMEcxWXhOS0hYaUNlVXZfTGxlUnNpUFhGSVBQdFpRd0ZiWng3Vkg4WXdmcVlLOTJUQ003bGF5TzlaTTJGOXRmcHk3UzFtRkdRODh6eTFvaTdJakZiaDlaTll2X25HbjZxRW1EcDVwSEdHVkRVbURiVWNSd081cUFZWFNqT1pEM05IejNOYw?oc=5) ⭐️ 6.0/10

据报道，Figma 部署了 AI 智能代理，使解决安全警报所需的时间缩短了 70%。 这一结果说明，AI 智能代理有望减少网络安全运营中的人工工作，并帮助安全团队更快响应。但现有报道缺乏足够的技术细节和独立验证，尚不能确定这一结果的普适性。 据报道，这一改进针对的是解决安全警报所需的时间，但现有信息没有说明部署架构、警报数量、测量周期或人工监督程度。因此，70%的数据更应被视为一项企业案例，而不是经过广泛验证的基准。

google_news · TechGig · 9月7日 00:16

**背景**: AI 智能代理是能够调查安全警报、分析现有信息并以机器速度作出决策的软件系统。在网络安全运营中，这种方法旨在自动化部分警报分类工作，减少安全分析师的人工调查负担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentmelt.com/blog/ai-cybersecurity-agent-incident-response/">AI Agents for Incident Response: From Alert to Resolution in Minutes</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#cybersecurity`, `#security operations`, `#Figma`, `#automation`

---

<a id="item-37" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Sep/7/video-compressor/" data-hz-title="浏览器视频压缩工具可本地运行 FFmpeg" data-hz-tags="FFmpeg,WebAssembly,Video Compression,Browser Tools,AI-Assisted Development" data-hz-section="other"></a>
## [浏览器视频压缩工具可本地运行 FFmpeg](https://simonwillison.net/2026/Sep/7/video-compressor/) ⭐️ 5.0/10

Simon Willison 发布了一个基于浏览器的视频压缩工具，该工具由 Claude Code 使用编译为 WebAssembly 的 FFmpeg 构建。它可以在本地生成多个可配置的 MP4 版本，提供从“最大”到“最小”的预设；示例中生成五个版本耗时 11.8 秒。 在浏览器中运行 FFmpeg，用户无需将视频上传到服务器即可完成压缩，这有助于保护隐私，也方便快速发布内容。该项目还展示了 AI 辅助开发如何将专业的命令行媒体处理流程转化为易用的网页工具。 界面提供五种预设，输出尺寸为 854×370 或 640×276，CRF 值范围为 22 至 28，音频比特率范围为 128 至 64 kbps，并支持调整编码速度、H.264 配置文件、帧率上限、移除元数据、移除音频以及仅编码前 10 秒。该工具默认通过 libx264 使用 H.264 Main 配置文件，采用 8 位 4:2:0 色彩，输出上限为 1080p 和 60 fps；示例中最小文件为 145 KB，即原文件的 48%。

rss · Simon Willison · 9月7日 18:29

**背景**: WebAssembly 是一种可在浏览器中执行的格式，因此 FFmpeg 等软件可以直接在网页内运行，而不必依赖服务器或桌面应用。FFmpeg 是用于转换和编码视频、音频的媒体处理工具；CRF 即恒定速率因子，通过在画质与文件大小之间进行权衡来调整编码质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ffmpegwasm.netlify.app/docs/overview/">Overview | ffmpeg .wasm</a></li>
<li><a href="https://tools.simonwillison.net/video-compressor">Video compressor</a></li>

</ul>
</details>

**标签**: `#FFmpeg`, `#WebAssembly`, `#Video Compression`, `#Browser Tools`, `#AI-Assisted Development`

---

<a id="item-38" class="hz-item-anchor" data-hz-url="https://marginalrevolution.com/marginalrevolution/2026/09/south-korean-aspirational-markets-in-everything.html?utm_source=rss&utm_medium=rss&utm_campaign=south-korean-aspirational-markets-in-everything" data-hz-title="韩国“多巴胺网站”模拟购物快感" data-hz-tags="South Korea,Consumer Technology,E-commerce,Digital Culture" data-hz-section="other"></a>
## [韩国“多巴胺网站”模拟购物快感](https://marginalrevolution.com/marginalrevolution/2026/09/south-korean-aspirational-markets-in-everything.html?utm_source=rss&utm_medium=rss&utm_campaign=south-korean-aspirational-markets-in-everything) ⭐️ 5.0/10

韩国出现了一种新趋势，Dopamine Shop 和 FoodNeverComes 等网站重现网络购物和点餐流程，但通常不会真正配送商品。用户可以搜索商品、比较评论、将物品加入购物车、填写地址，并下单或追踪虚拟订单。 这一趋势表明，一些用户追求的可能是数字消费带来的兴奋感和情绪满足，而不一定是真正完成购买。它也显示出，电子商务界面本身可以转变为娱乐体验，尤其是在韩国的数字文化中。 这些网站模仿普通电子商务的多个步骤，包括发现商品、比较评论、创建购物车、填写地址、下单和追踪配送。相关报道将其描述为无需真实消费的模拟体验，用户订购的食物或商品并不会送达。

rss · Marginal Revolution · 9月7日 18:41

**背景**: 网络购物通常把浏览商品、完成交易和实际配送结合在一起。这些“多巴胺网站”将浏览和下单仪式与真实购买分离，让用户在没有收到商品的情况下体验熟悉的电子商务互动。“多巴胺”在这里指这种模拟活动带来的愉悦刺激，而不是传统的零售市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mashable.com/life/south-korea-dopamine-sites-fake-shopping">South Korea’s dopamine sites simulate shopping without ...</a></li>
<li><a href="https://www.fastcompany.com/91560432/dopamine-sites-fake-online-shopping-apps-let-you-pretend-to-buy-things-foodnevercomes">'Dopamine sites': Fake online shopping apps let you pretend ...</a></li>

</ul>
</details>

**标签**: `#South Korea`, `#Consumer Technology`, `#E-commerce`, `#Digital Culture`

---

<a id="item-39" class="hz-item-anchor" data-hz-url="https://marginalrevolution.com/marginalrevolution/2026/09/emergent-ventures-winners-59th-cohort.html?utm_source=rss&utm_medium=rss&utm_campaign=emergent-ventures-winners-59th-cohort" data-hz-title="Emergent Ventures公布第59届获资助者" data-hz-tags="AI agents,autonomous vehicles,biomedical research,research funding,Emergent Ventures" data-hz-section="other"></a>
## [Emergent Ventures 公布第 59 届获资助者](https://marginalrevolution.com/marginalrevolution/2026/09/emergent-ventures-winners-59th-cohort.html?utm_source=rss&utm_medium=rss&utm_campaign=emergent-ventures-winners-59th-cohort) ⭐️ 5.0/10

Emergent Ventures 选出了第 59 届获资助者，其中包括研究英国自动驾驶的 Tym Syrytczyk、研究人工智能代理的 Shane Regan，以及研究代理和职业支持的 Maximilian Kornstein。其他获资助者包括利用肽类使用数据开展研究的加州大学伯克利分校研究人员、用人工智能更新荟萃分析的 Evan Warfel，以及筹建墨西哥生物医学智库的 Daniel Dominguez Gomez。 这一届获资助者显示，早期研究资金正流向人工智能代理、自动驾驶、生物医学数据和证据综合等多个方向。它也为了解 Emergent Ventures 认为具有潜力、但尚未受到广泛关注的项目提供了一个有限窗口。 公告列出了部分获资助者所在地区，并注明两名申请者的年龄：Shane Regan 为 16 岁，Maximilian Kornstein 为 15 岁。文章只提供了非常简短的项目描述，现有摘录在提到 Malhaar Agrawal 后被截断，因此没有说明资助金额、研究方法、时间表或预期成果。

rss · Marginal Revolution · 9月7日 04:32

**背景**: Emergent Ventures 是 Mercatus Center 于 2018 年启动的低管理成本奖学金和资助项目。该项目支持创业者及其他有潜力的人，开展旨在改善社会、具有高度可扩展性的“从零到一”项目。人工智能代理是能够追求目标、作出中间决策并执行多步骤行动的软件系统，而不仅仅是回应单次提示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mercatus.org/emergent-ventures">Emergent Ventures | Mercatus Center</a></li>
<li><a href="https://www.digital-chiefs.de/en/autonomous-ai-agents-enterprise-productivity-governance-2026/">Autonomous AI Agents in the Enterprise: Between Productivity Leap...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#autonomous vehicles`, `#biomedical research`, `#research funding`, `#Emergent Ventures`

---

<a id="item-40" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiXEFVX3lxTE9OODM5Q1FOUzRzaU9YUFJBMGJCRDY1OW4xUkRoRElNSUdTaTJvOVc5WUxWaUxINVR2eERqdVdBcHg0V0tqd1NmMXVrMTRyY1lCd3VHUW16Z244cTlQ?oc=5" data-hz-title="GitGuardian探索人工智能分析公开泄露凭证" data-hz-tags="Cybersecurity,Credential Leakage,AI,Secrets Management,Threat Detection" data-hz-section="other"></a>
## [GitGuardian 探索人工智能分析公开泄露凭证](https://news.google.com/rss/articles/CBMiXEFVX3lxTE9OODM5Q1FOUzRzaU9YUFJBMGJCRDY1OW4xUkRoRElNSUdTaTJvOVc5WUxWaUxINVR2eERqdVdBcHg0V0tqd1NmMXVrMTRyY1lCd3VHUW16Z244cTlQ?oc=5) ⭐️ 5.0/10

GitGuardian 讨论了使用人工智能分析和监控公开来源中暴露的凭证。所提供的材料没有说明新的产品发布、基准测试结果或具体技术突破。 公开暴露的凭证可能为攻击者进入企业系统提供途径，因此持续监控有助于安全团队更早发现并修复相关事件。人工智能分析可能补充传统的机密检测方法，但现有信息没有量化其额外效果。 GitGuardian 文档称，其 Public Monitoring 会持续扫描 GitHub 公开提交，将结果与组织的监控范围进行匹配，并分析 600 多种机密类型；大多数事件会在提交后约 10 分钟内创建并发出警报。所提供的文章摘要没有说明使用了哪些人工智能模型、如何处理误报，或如何验证凭证是否有效。

google_news · GitGuardian Blog · 9月7日 15:01

**背景**: 机密监控是指扫描公开来源，查找不应暴露的密码、API 密钥、令牌和其他凭证。GitGuardian 的公开监控文档介绍了持续扫描 GitHub 等来源，以发现与组织或其开发者相关的机密。发现暴露只是处理流程的第一步，组织仍需撤销或轮换凭证，并调查其是否可能已被滥用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.gitguardian.com/public-monitoring/detect-public-secret-incidents/overview">Detect public secret incidents | GitGuardian documentation</a></li>
<li><a href="https://docs.gitguardian.com/public-monitoring/home">home | GitGuardian documentation</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#Credential Leakage`, `#AI`, `#Secrets Management`, `#Threat Detection`

---

<a id="item-41" class="hz-item-anchor" data-hz-url="https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam" data-hz-title="InferenceX 加速 TPU 推理外部化" data-hz-tags="" data-hz-section="other"></a>
## [InferenceX 加速 TPU 推理外部化](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ ?/10

InferenceX 正在推进 Google TPU 推理软件栈的外部化，项目强调每美元性能最高提升 50%、客户群不断扩大，并涉及 Ironwood 和 TPUv8i。其首个原生 TorchTPU 服务模型的初始适配据称投入了数百个工程师工时，并提交了大量代码变更来优化推理性能。 更易使用且效率更高的 TPU 推理软件栈，可能为模型开发者提供 CUDA 部署之外的选择，并削弱 NVIDIA GPU 在生产推理中长期占据的软件优势。每美元性能的提升也可能增强 TPU 计算资源对推理客户的吸引力。 这项优化工作围绕原生 TorchTPU 服务软件栈展开，而 vLLM TPU 项目介绍了一种硬件插件，通过共享的降级路径统一支持 JAX 和 PyTorch。50% 这一数字是每美元性能方面的宣传性指标，但现有材料没有提供其对应的基准模型、延迟目标或部署条件。

rss · Semianalysis（半导体·AI 风向标） · 9月7日 20:00

**背景**: TPU 推理是指在 Google 的 TPU 加速器上运行已训练的机器学习模型，以生成预测结果或响应。TorchTPU 旨在让基于 PyTorch 的工作负载使用 TPU，而 CUDA 是 NVIDIA 广泛使用的 GPU 软件平台，因此扩大 TPU 软件支持与两个生态系统之间的竞争差距密切相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam">TPU Inference Externalization Full Steam Ahead - InferenceX</a></li>
<li><a href="https://github.com/vllm-project/tpu-inference">GitHub - vllm-project/ tpu - inference : TPU inference for vLLM, with...</a></li>

</ul>
</details>

---

<a id="item-42" class="hz-item-anchor" data-hz-url="https://seths.blog/2026/09/the-reality-of-sunk-costs/" data-hz-title="坚持与沉没成本之间" data-hz-tags="" data-hz-section="other"></a>
## [坚持与沉没成本之间](https://seths.blog/2026/09/the-reality-of-sunk-costs/) ⭐️ ?/10

Seth Godin 的文章探讨了重视坚持与识别沉没成本之间的张力。文章将社会对长期持续事物的偏好，与投资者需要独立评估每一轮新融资的做法进行了对比，而不是只依据过去的投入做决定。 这一差异很重要，因为坚持可能意味着可靠性，但仅仅因为已经投入资源而继续，也可能导致糟糕的决策。这个观点与公司、投资者以及所有需要判断某项持续努力是否值得继续获得支持的人都有关。 文章摘录用持续多年的告别巡演和可靠的本地印刷店说明坚持，随后将沉没成本的视角应用到公司再次融资的情境中。由于提供的内容在此处被截断，摘录没有说明评估新一轮融资的更多标准，也没有提供其他例子。

rss · Seth Godin · 9月7日 10:31

**背景**: 沉没成本是已经付出且无法收回的资源。理性决策通常应关注继续行动所带来的未来成本和收益，而不是把过去的投入当作继续行动的理由。在这篇文章的语境中，坚持体现了人们对稳定性和持久性的重视，而投资者的做法则要求单独判断下一轮融资是否具有充分理由。

---

