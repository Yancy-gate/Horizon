# Horizon 每日速递 - 2026-08-31

> 从 112 条内容中筛选出 44 条重要资讯。

---

## 偏好雷达

> 基于你维护的偏好档案（data/preference-radar/profile.json）独立筛选的个性化内容。

今日暂无符合偏好的更新。

---
## 华科老师研究方向

> 依据学院教师公开研究方向与论文关键词筛选。

1. [自适应电压协调提升 VSG 逆变器暂态稳定性](#item-1) ⭐️ 7.0/10
2. [基于开关频率注入的更精准无传感器 SPMSM 控制](#item-2) ⭐️ 7.0/10
3. [采样延迟导致逆变器高频非被动性](#item-3) ⭐️ 7.0/10
4. [关键基础设施最坏扰动的建模与缓解算法](#item-4) ⭐️ 7.0/10
5. [STO-CAST 让热带气旋停电预测走向实时行动](#item-5) ⭐️ 7.0/10
6. [概率分层匹配协调电动汽车调度与电网负荷](#item-6) ⭐️ 7.0/10
7. [概率分层匹配优化电动汽车调度与电网负荷](#item-7) ⭐️ 7.0/10
8. [固体氧化物燃料电池系统控制综述](#item-8) ⭐️ 6.0/10
9. [优化共享快速公交专用道的公交网络](#item-9) ⭐️ 6.0/10
10. [概率层级匹配提升随机电动汽车调度](#item-10) ⭐️ 6.0/10
11. [级联双成本函数改进永磁同步电机预测控制](#item-11) ⭐️ 5.0/10
12. [结合改进型 ADRC 与自适应谐波滤波器的无传感器 PMSM 控制](#item-12) ⭐️ 5.0/10
13. [基于分层匹配的车辆调度方法](#item-13) ⭐️ 5.0/10
14. [多模式公交网络与时刻表一体化设计](#item-14) ⭐️ 5.0/10

---
<a id="item-1" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560379" data-hz-title="自适应电压协调提升VSG逆变器暂态稳定性" data-hz-tags="Grid-forming inverters,Virtual synchronous generators,Transient stability,Power systems control,Renewable energy integration" data-hz-section="hust-research"></a>
## [自适应电压协调提升 VSG 逆变器暂态稳定性](https://doi.org/10.1109/ccdc69976.2026.11560379) ⭐️ 7.0/10

该论文提出在虚拟同步发电机（VSG）控制的构网型逆变器中，自适应协调快速和慢速内部电压源。该控制器根据系统需求切换或协调两类动态特性，以提升逆变器在扰动期间的暂态稳定性。 随着可再生能源逐步替代传统同步机，构网型逆变器需要在电网扰动时维持电压、频率和同步运行。提升暂态稳定性有助于更可靠地接入光伏、风电和储能资源，但其实际影响仍取决于论文中的仿真或实验验证结果。 该方法的核心技术特点是自适应使用两种内部电压源动态特性，而不是依赖单一且固定的响应速度。现有信息未说明具体的切换判据、控制器参数，或实验与仿真中的性能提升幅度，因此这些内容仍需查阅论文全文确认。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **grid-forming**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 虚拟同步发电机是一种控制策略，可使逆变器模拟传统同步发电机的惯性、阻尼和下垂特性。构网型逆变器调节自身的内部电压和相角，以建立或支撑电网电压和频率，而不是仅跟踪外部设定的波形。在故障或其他扰动期间，逆变器的控制动态特性和限流行为会显著影响其能否保持同步与稳定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/topics/engineering/virtual-synchronous-generator">Virtual Synchronous Generator - an overview | ScienceDirect Topics</a></li>
<li><a href="https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2023.1331024/full">Frontiers | Improved VSG strategy of grid-forming inverters for supporting inertia and damping</a></li>
<li><a href="https://www.researchgate.net/publication/376378718_Exploring_Damping_Effect_of_Inner_Control_Loops_for_Grid-Forming_VSCs">(PDF) Exploring Damping Effect of Inner Control Loops for...</a></li>

</ul>
</details>

**标签**: `#Grid-forming inverters`, `#Virtual synchronous generators`, `#Transient stability`, `#Power systems control`, `#Renewable energy integration`

---

<a id="item-2" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/tpel.2026.3678851" data-hz-title="基于开关频率注入的更精准无传感器SPMSM控制" data-hz-tags="Sensorless Motor Control,PMSM,Model Predictive Control,Power Electronics,Electric Motor Drives" data-hz-section="hust-research"></a>
## [基于开关频率注入的更精准无传感器 SPMSM 控制](https://doi.org/10.1109/tpel.2026.3678851) ⭐️ 7.0/10

该论文提出了一种经过实验验证的表贴式永磁同步电机无传感器控制策略，将开关频率注入与有限控制集死区预测电流控制相结合。该方法采用带扩展控制集的角度域迭代优化、基于注入时间的补偿以及一种简便的初始位置检测方法，从而提高注入精度并减少执行时间。 在有限控制集预测控制中，不准确的电压注入会使位置误差信号恶化，并削弱无传感器运行效果。该方法在提高注入精度的同时减少计算执行时间，有望推动更实用的无传感器电机驱动，尤其适用于既需要省去位置传感器、又要求保持电流控制性能的场景。 该策略以直轴电流偏置为基础，并在一台 SPMSM 上完成了实现；论文还分析了电流偏置引起的速度振荡。作者指出，有限控制集固有的注入误差会降低电流控制性能，而传统补偿可能需要显著更长的执行时间，所提出的基于注入时间的方法则通过实验缓解了这一权衡。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 3月31日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 开关频率注入是一种无传感器技术，它施加高频电压或与开关相关的信号，并观测产生的电流响应来推断转子位置。SPMSM 是表贴式永磁同步电机，其转子位置通常由传感器测量，但也可以根据电气信号进行估算。有限控制集模型预测控制从逆变器可用的开关状态中进行选择，而死区预测电流控制旨在较短的预测区间内使电流达到参考值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ieeexplore.ieee.org/document/11458794">Novel Switching Frequency Injection Sensorless Control for ...</a></li>
<li><a href="https://ieeexplore.ieee.org/document/10108031">Sensorless Control With Switching Frequency Square Wave ...</a></li>

</ul>
</details>

**标签**: `#Sensorless Motor Control`, `#PMSM`, `#Model Predictive Control`, `#Power Electronics`, `#Electric Motor Drives`

---

<a id="item-3" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/apec51134.2026.11516799" data-hz-title="采样延迟导致逆变器高频非被动性" data-hz-tags="power electronics,grid-connected inverters,passivity-based control,control delays,power-system stability" data-hz-section="hust-research"></a>
## [采样延迟导致逆变器高频非被动性](https://doi.org/10.1109/apec51134.2026.11516799) ⭐️ 7.0/10

该论文量化分析了采样周期和采样时刻产生的控制延迟，如何影响并网跟随型逆变器导纳在奈奎斯特频率以上负阻尼区域的深度和带宽。论文还提出了一种考虑频率混叠的基于无源性的阻尼方法，并通过实验验证了其对高频稳定性的改善效果。 研究表明，提高采样频率可以减轻但无法消除高频非被动性，从而揭示了并网电力变换器中一个持续存在的稳定性风险。所提出的抑制方法有助于工程师评估并改善逆变器控制与电网谐振之间的相互作用，尤其适用于弱电网场景。 该分析区分了绝对延迟和相对延迟，并分别考察了它们对负阻尼区域的影响。由于该问题涉及采样系统奈奎斯特频率以上的导纳特性，仅依据奈奎斯特频率以下的常规直觉并不足够；所提出的阻尼设计明确考虑了频率混叠，并通过实验进行了验证。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 3月22日 00:00

**匹配依据**: 论文关键词命中 **grid-following**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 并网跟随型逆变器利用现有电网的电压和频率作为参考，通过控制系统调节注入电网的电流和功率。输出导纳描述逆变器的电流响应如何随外加电压扰动而变化，因此可用于基于阻抗或导纳的稳定性评估。奈奎斯特频率是采样频率的一半，采样控制系统中的更高频率分量可能通过频率混叠表现出来。基于无源性的评估关注逆变器是否表现为吸收净能量的元件，而不是产生可能放大电网振荡的负阻尼。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mdpi.com/1996-1073/16/16/5894">Small-Signal Modeling and Stability Analysis of a Grid-Following Inverter with Inertia Emulation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nyquist_frequency">Nyquist frequency - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/314202717_VSC_Input-Admittance_Modeling_and_Analysis_Above_the_Nyquist_Frequency_for_Passivity-Based_Stability_Assessment">VSC Input-Admittance Modeling and Analysis Above the Nyquist Frequency for Passivity-Based Stability Assessment | Request PDF</a></li>

</ul>
</details>

**标签**: `#power electronics`, `#grid-connected inverters`, `#passivity-based control`, `#control delays`, `#power-system stability`

---

<a id="item-4" class="hz-item-anchor" data-hz-url="https://doi.org/10.1016/j.ress.2026.113133" data-hz-title="关键基础设施最坏扰动的建模与缓解算法" data-hz-tags="Critical Infrastructure,Reliability Engineering,Resilience,Optimization,Systems Research" data-hz-section="hust-research"></a>
## [关键基础设施最坏扰动的建模与缓解算法](https://doi.org/10.1016/j.ress.2026.113133) ⭐️ 7.0/10

该论文研究用于识别和缓解关键基础设施系统最坏扰动的模型与算法。其重点是找出会导致系统性能最大幅度下降的故障或攻击，并为防御响应提供依据。 关键基础设施受到扰动时，可能影响重要服务的可靠性和连续性，因此识别破坏性最大的组件有助于运营者优先配置防护和缓解资源。该研究属于利用优化方法支持基础设施规划与恢复的可靠性和韧性研究领域。 相关方法通常将最坏扰动表述为阻断问题或双层优化问题，在这种问题中，需要评估对抗性扰动对加固等防御决策的影响。这类问题的计算难度可能较高，因此算法设计对于将模型应用于更大规模的基础设施网络十分重要。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 7月10日 00:00

**匹配依据**: 论文关键词命中 **critical infrastructure**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 关键基础设施系统提供重要服务，其中某些组件发生故障后，可能对整体性能产生不成比例的影响。最坏扰动分析旨在寻找对系统影响最严重的故障或攻击情景。随后，缓解模型可以帮助确定应优先保护哪些组件或采取哪些防御措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0951832026009427">Identifying and mitigating worst-case disruptions in critical ...</a></li>
<li><a href="https://roadef2026.sciencesconf.org/687427/document">Identifying Critical Infrastructure : A Bilevel Genetic Algorithm</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0951832024007889">Enhancing critical network infrastructure resilience through optimal post-disruption maintenance and routing decisions - ScienceDirect</a></li>

</ul>
</details>

**标签**: `#Critical Infrastructure`, `#Reliability Engineering`, `#Resilience`, `#Optimization`, `#Systems Research`

---

<a id="item-5" class="hz-item-anchor" data-hz-url="https://doi.org/10.1111/risa.70275" data-hz-title="STO-CAST让热带气旋停电预测走向实时行动" data-hz-tags="Deep Learning,Spatiotemporal Forecasting,Power Systems,Disaster Response,Climate Risk" data-hz-section="hust-research"></a>
## [STO-CAST 让热带气旋停电预测走向实时行动](https://doi.org/10.1111/risa.70275) ⭐️ 7.0/10

研究人员推出了 STO-CAST 这一时空深度学习模型，利用不断变化的气象预测和新观测到的停电信息，持续更新热带气旋期间的逐小时停电预测。该模型以 4 公里×4 公里的空间分辨率进行预测，提供 6 小时临近预报和 60 小时规划预报，并通过留一风暴交叉验证框架对 2022 年台风“梅花”进行了评估。 与开环或事件级模型不同，STO-CAST 能够在风暴条件和电力系统状态变化时调整预测，帮助公用事业单位改善应急态势感知和提前部署资源。更及时、更精细的预测有望支持风险知情型响应，并提升电力系统应对强热带气旋的韧性。 该模型将静态环境与基础设施属性同动态气象序列和停电序列结合起来，并通过误差分解区分模型局限、气象不确定性和观测缺口的影响。现有证据来自台风“梅花”的案例研究，因此其在不同风暴、地区和电网条件下的表现仍需进一步验证。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月26日 00:00

**匹配依据**: 论文关键词命中 **tropical cyclone**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 时空预测模型学习同时随地点和时间变化的规律，因此适合分析风暴移动过程中地理分散的电力系统如何出现停电。这里的临近预报是指结合当前观测信息进行短提前量预测，而较长期的预测模式则用于支持提前规划。留一风暴交叉验证会将一个风暴排除在训练样本之外，再用它测试模型，从而评估模型对未见事件的泛化能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.06644">[2512.06644] From Forecast to Action: A Deep Learning Model for Predicting Power Outages During Tropical Cyclones</a></li>
<li><a href="https://arxiv.org/pdf/2512.06644">From Forecast to Action: A Deep Learning Model for Predicting ...</a></li>

</ul>
</details>

**标签**: `#Deep Learning`, `#Spatiotemporal Forecasting`, `#Power Systems`, `#Disaster Response`, `#Climate Risk`

---

<a id="item-6" class="hz-item-anchor" data-hz-url="https://doi.org/10.6084/m9.figshare.31910706" data-hz-title="概率分层匹配协调电动汽车调度与电网负荷" data-hz-tags="Electric Vehicles,Optimization,Smart Grids,Stochastic Scheduling,Transportation Systems" data-hz-section="hust-research"></a>
## [概率分层匹配协调电动汽车调度与电网负荷](https://doi.org/10.6084/m9.figshare.31910706) ⭐️ 7.0/10

该研究提出了概率分层匹配（P-HM）方法，用于同时考虑行程时间不确定性和电网负荷约束的随机电动汽车调度。该方法将时刻表划分为多个层级，依据兼容概率匹配相邻层级，并结合贪心局部搜索减少峰值负荷违规。 该方法同时优化车队规模、运营成本、充电峰值负荷和准时 performance，能够处理交通可靠性与电网安全之间的相互影响。研究结果表明，它有望帮助公共交通运营商减少所需车辆数量，并使电动公交充电更适应电网容量约束。 该模型面向随机行程时间环境提升调度稳健性，并通过贪心局部搜索抑制充电峰值负荷；与基准方法相比，车队规模减少方面的效果尤其突出。不过，现有材料主要提供数值对比，尚未显示独立验证结果或真实交通网络中的部署证据。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 随机电动汽车调度问题是在行程时间和由此产生的充电需求存在不确定性的情况下，为时刻表中的班次分配电动汽车。这些不确定性可能使充电需求集中到高峰时段，从而加重电网负荷并降低调度可靠性。P-HM 通过根据相邻班次在运营上兼容的概率匹配时刻表层级，并利用局部搜索改进违反峰值负荷限制的方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/0305215X.2026.2643627">Probability-based hierarchical matching approach for ...</a></li>
<li><a href="https://tandf.figshare.com/articles/dataset/Probability-based_hierarchical_matching_approach_for_stochastic_electric_vehicle_scheduling_considering_power_grid_load/31910706">Item - Probability-based hierarchical matching approach for ...</a></li>

</ul>
</details>

**标签**: `#Electric Vehicles`, `#Optimization`, `#Smart Grids`, `#Stochastic Scheduling`, `#Transportation Systems`

---

<a id="item-7" class="hz-item-anchor" data-hz-url="https://doi.org/10.6084/m9.figshare.31910706.v1" data-hz-title="概率分层匹配优化电动汽车调度与电网负荷" data-hz-tags="Electric vehicle scheduling,Power grid optimization,Stochastic optimization,Operations research,Transportation systems" data-hz-section="hust-research"></a>
## [概率分层匹配优化电动汽车调度与电网负荷](https://doi.org/10.6084/m9.figshare.31910706.v1) ⭐️ 7.0/10

该文章提出了一种概率分层匹配（P-HM）方法，用于同时考虑行程时间不确定性和电网负荷约束的随机电动汽车调度。其模型在最大化准时性能的同时，联合最小化车队规模、运营成本和充电峰值负荷。 随机行程时间可能改变充电需求，使公共交通时刻表和电力负荷都更难预测，因此联合处理交通与电网约束有望提升运营稳定性。随着电动汽车普及，该方法可能帮助公共交通运营方减少所需车队规模，并改善电网负荷管理安全性。 P-HM 将时刻表划分为多个层级，并依据兼容概率匹配相邻层级，同时利用贪心局部搜索处理峰值负荷违规。报告的数值实验显示，该方法在减少车队规模方面尤其优于基准方法，但现有内容未提供更广泛真实场景下的详细验证。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 电动汽车调度问题是指在满足时刻表和车辆运行要求的前提下，为各项行程分配车辆。在这一场景中，随机调度用于表示行程时间的不确定性，而行程时间会影响车辆的充电时刻；同时，集中充电可能形成峰值负荷，因此也会影响电网。分层匹配通过在时刻表层级之间进行兼容性决策来处理调度问题，概率部分则用于表示这些匹配保持可行的可能性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/0305215X.2026.2643627">Probability-based hierarchical matching approach for ...</a></li>
<li><a href="https://www.researchgate.net/publication/377347437_Electric_Vehicle_Scheduling_State_of_the_Art_Critical_Challenges_and_Future_Research_Opportunities">(PDF) Electric Vehicle Scheduling : State of the Art, Critical...</a></li>

</ul>
</details>

**标签**: `#Electric vehicle scheduling`, `#Power grid optimization`, `#Stochastic optimization`, `#Operations research`, `#Transportation systems`

---

<a id="item-8" class="hz-item-anchor" data-hz-url="https://doi.org/10.23919/pcmp.2025.000294" data-hz-title="固体氧化物燃料电池系统控制综述" data-hz-tags="Solid Oxide Fuel Cells,Control Systems,Energy Systems,Power Systems,Review" data-hz-section="hust-research"></a>
## [固体氧化物燃料电池系统控制综述](https://doi.org/10.23919/pcmp.2025.000294) ⭐️ 6.0/10

该论文系统综述了固体氧化物燃料电池系统的控制目标、控制策略和未解决的挑战。它主要整合已有研究，而不是提出一种全新的控制方法。 这篇综述有助于能源系统和控制领域的研究人员比较不同的固体氧化物燃料电池运行管理方法，并识别仍需改进的方向。更完善的控制技术对于提升基于固体氧化物燃料电池的电力系统的实际部署能力和可靠性具有重要意义。 固体氧化物燃料电池系统需要协调电化学发电过程与燃料、空气供应等运行条件，相关控制研究还要考虑温度行为，包括温度梯度管理。该论文主要整合和分析控制目标、策略与挑战，因此其价值主要在于系统梳理，而不是展示已验证的性能突破。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 7月1日 00:00

**匹配依据**: 论文关键词命中 **fuel cell**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 固体氧化物燃料电池是一种通过氧化燃料来发电的电化学转换装置。它的基本结构是在阳极和阴极之间设置固体、通常为陶瓷材料的电解质；燃料供应给阳极，氧化剂通常为空气并供应给阴极。系统控制之所以重要，是因为这些运行输入和内部热状态会影响燃料电池的整体运行表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.netl.doe.gov/carbon-management/sofc/operating-principle">SOFC OPERATING PRINCIPLE | netl.doe.gov</a></li>
<li><a href="https://en.wikipedia.org/wiki/Solid_oxide_fuel_cell">Solid oxide fuel cell - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Solid Oxide Fuel Cells`, `#Control Systems`, `#Energy Systems`, `#Power Systems`, `#Review`

---

<a id="item-9" class="hz-item-anchor" data-hz-url="https://doi.org/10.23919/csms.2025.0021" data-hz-title="优化共享快速公交专用道的公交网络" data-hz-tags="transportation optimization,bus rapid transit,genetic algorithms,network design,operations research" data-hz-section="hust-research"></a>
## [优化共享快速公交专用道的公交网络](https://doi.org/10.23919/csms.2025.0021) ⭐️ 6.0/10

该论文提出了一个双层公交网络设计与频率设置模型，明确纳入普通公交共享快速公交专用道的情形。论文还提出了优先级遗传算法，该算法在 Mandl 基准算例中表现良好，并在临沂的真实网络中降低了乘客和运营方成本，同时提高了快速公交专用道的利用率。 这一框架可以帮助公交规划者更高效地利用未充分使用的快速公交基础设施，并改善公交速度、换乘和系统整体成本。它的主要价值在于方法和运营层面，尤其适用于已经拥有快速公交专用道、需要协调普通公交服务的城市。 该模型通过专门定义的快速公交节点和快速公交车道弧来表示共享车道基础设施，算法则使用基于优先级的染色体、交叉算子和变异算子。论文结果来自基准算例和临沂实验，因此其对其他道路布局、出行需求模式和运营政策的普适性仍需进一步验证。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 6月1日 00:00

**匹配依据**: 论文关键词命中 **bus transit**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 快速公交是一种相较于普通公交具有更高运力、可靠性和服务质量的公交系统，通常使用专用车道。在这项研究中，快速公交专用道共享是指普通公交可以使用这些车道，同时不干扰既定的快速公交运营。双层模型将网络和发车频率决策与由此产生的乘客或运营响应分开，而遗传算法则用于搜索这一优化问题的较优解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bus_rapid_transit">Bus rapid transit - Wikipedia</a></li>
<li><a href="https://www.transit.dot.gov/sites/fta.dot.gov/files/BRTBrochure.pdf">Bus Rapid Transit (BRT) Brochure</a></li>

</ul>
</details>

**标签**: `#transportation optimization`, `#bus rapid transit`, `#genetic algorithms`, `#network design`, `#operations research`

---

<a id="item-10" class="hz-item-anchor" data-hz-url="https://doi.org/10.1080/0305215x.2026.2643627" data-hz-title="概率层级匹配提升随机电动汽车调度" data-hz-tags="Electric Vehicle Scheduling,Stochastic Optimization,Smart Grids,Operations Research,Transportation Systems" data-hz-section="hust-research"></a>
## [概率层级匹配提升随机电动汽车调度](https://doi.org/10.1080/0305215x.2026.2643627) ⭐️ 6.0/10

该文章提出了一种考虑行程时间不确定性和电网负荷的随机电动汽车调度概率层级匹配（P-HM）方法。该方法结合时刻表分层、基于兼容概率的匹配和贪心局部搜索，以减少所需车辆数量和充电峰值违规，并提高准点性能。 公共交通运营商需要同时协调车辆可用性、不确定的行程时间、充电需求和电网约束，而不是分别优化这些因素。通过关联这些因素，该方法有望提高电动公交运营的可靠性，并减轻电网压力。 该模型同时最小化车辆数量、运营成本和充电峰值负荷，并最大化准点性能；数值实验显示其表现优于基准方法。现有证据主要来自数值实验，因此其在不同交通网络、需求模式和充电基础设施下的实际表现仍有待验证。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 4月1日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 电动汽车调度问题是指在满足车辆可用性和充电需求等运营约束的情况下，为计划行程分配电动汽车。在随机环境中，行程时间和充电需求并不是固定的，而是存在不确定性。之所以需要考虑电网负荷，是因为集中充电可能形成负荷峰值，影响电网安全，并与可靠的时刻表运营产生冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/0305215X.2026.2643627">Probability-based hierarchical matching approach for ...</a></li>
<li><a href="https://www.mdpi.com/2032-6653/17/5/255">Stochastic Optimal Scheduling Method for Vehicle–Grid ...</a></li>

</ul>
</details>

**标签**: `#Electric Vehicle Scheduling`, `#Stochastic Optimization`, `#Smart Grids`, `#Operations Research`, `#Transportation Systems`

---

<a id="item-11" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560295" data-hz-title="级联双成本函数改进永磁同步电机预测控制" data-hz-tags="Model Predictive Control,PMSM,Motor Drives,Power Electronics,Control Systems" data-hz-section="hust-research"></a>
## [级联双成本函数改进永磁同步电机预测控制](https://doi.org/10.1109/ccdc69976.2026.11560295) ⭐️ 5.0/10

该论文提出了一种用于永磁同步电机的模型预测控制方法，将级联双成本函数与动态切换相结合。该结构旨在提升动态响应能力，同时保持稳态控制性能。 永磁同步电机驱动系统广泛用于工业自动化和电动汽车等场景，既需要快速响应，也需要较小的稳态误差。若能缓解这两类目标之间的权衡，预测控制就可能更适合高性能电机驱动系统。 该方法针对传统预测控制可能存在的动态响应受限、权重因子调节困难、抗噪性和稳态性能等问题进行处理。现有资料没有给出该控制器的具体实验增益、计算需求或运行约束。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: 模型预测控制会反复利用电机模型评估可能的控制动作，并根据成本函数选择控制方案。永磁同步电机是一种需要在系统约束下调节转矩和电流的电机。在永磁同步电机驱动中，预测控制能够处理非线性行为和约束，但其性能取决于控制器设计和计算能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.semanticscholar.org/paper/Cascaded-Dual-Cost-Functions-Model-Predictive-for-Wang-Cheng/a1ea56b8309d0d116487a04a04bfbd28804a5a53">Cascaded Dual Cost Functions Model Predictive Control for ...</a></li>
<li><a href="https://grampc.github.io/grampc/tutorials/PMSM.html">Model predictive control of a PMSM — grampc 2.3 documentation</a></li>

</ul>
</details>

**标签**: `#Model Predictive Control`, `#PMSM`, `#Motor Drives`, `#Power Electronics`, `#Control Systems`

---

<a id="item-12" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560068" data-hz-title="结合改进型ADRC与自适应谐波滤波器的无传感器PMSM控制" data-hz-tags="PMSM control,Sensorless control,Active disturbance rejection,Adaptive harmonic filtering" data-hz-section="hust-research"></a>
## [结合改进型 ADRC 与自适应谐波滤波器的无传感器 PMSM 控制](https://doi.org/10.1109/ccdc69976.2026.11560068) ⭐️ 5.0/10

该论文提出了一种永磁同步电机无传感器控制方法，将改进型主动扰动抑制控制与并行自适应谐波滤波器结合起来。该方法旨在不依赖物理位置传感器的情况下，提高转子位置估计精度和扰动抑制能力。 准确的转子位置信息是矢量控制的基础，而取消位置传感器可以降低硬件复杂度，并提升某些电机驱动系统的适用性。这种组合有望同时缓解位置估计误差和周期性扰动问题，但现有信息显示其更像是面向专业研究的技术贡献，而不是具有广泛行业影响的突破。 ADRC 旨在无需高度精确的电机模型即可估计并补偿内部和外部扰动，而并行自适应滤波器则针对可能影响估计与控制的谐波分量。现有材料没有提供位置估计精度提升幅度、运行速度范围、计算开销或实验验证细节，因此目前还无法全面判断该方法的实际优势。

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **PMSM**（能源电子与智能制造）。

**关联教师**: 俞耀文、刘智伟、刘骁康、卢仁智、叶杰、唐其鹏、尹泉、彭刚 等共 21 人

**背景**: PMSM 无传感器控制通过电气测量量估计矢量控制所需的转子位置，而不是使用物理位置传感器。一种常见方法是利用定子电压和电流控制信息推算反电动势，但估计性能可能受到运行条件和扰动的影响。ADRC 是一种用于处理系统动态不确定性和外部扰动的控制框架，自适应谐波滤波器则能够估计变化的谐波分量，以减弱这些分量的不利影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2307187725009678">Sensorless rotor position estimation of PMSM for low and high ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s42835-023-01710-w">Overview of Active Disturbance Rejection Control for ...</a></li>
<li><a href="https://www.monolithicpower.com/en/learning/mpscholar/power-electronics/power-quality-and-harmonics/active-filters-for-harmonic-elimination?srsltid=AfmBOopAsjQATM-FVKgEVRKmlNzrjpDtXQ9JFhQmduQGv078rOLIWpOQ">Active Filters for Harmonic Elimination - Monolithic Power Systems</a></li>

</ul>
</details>

**标签**: `#PMSM control`, `#Sensorless control`, `#Active disturbance rejection`, `#Adaptive harmonic filtering`

---

<a id="item-13" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560172" data-hz-title="基于分层匹配的车辆调度方法" data-hz-tags="vehicle scheduling,optimization,matching algorithms,transportation systems,operations research" data-hz-section="hust-research"></a>
## [基于分层匹配的车辆调度方法](https://doi.org/10.1109/ccdc69976.2026.11560172) ⭐️ 5.0/10

该论文提出了一种基于分层匹配的车辆调度问题算法，重点是最小化车队规模。该方法被描述为一种用于将车辆分配给时刻表班次的多项式时间算法。 车辆调度会影响公共交通及其他基于时刻表的系统中的车队需求和运营成本。如果在保证班次分配可行的同时减少车队规模，该方法可能提高资源利用率，但其更广泛的影响仍取决于与现有优化方法的验证结果。 车辆调度问题被描述为 NP 难问题，而该方法主要关注车队规模优化，并未在现有材料中全面说明所有调度目标。提供的材料没有报告基准数据集、对比实验结果或该方法在不同目标之间的性能权衡。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **vehicle scheduling**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 车辆调度问题是将一组车辆分配给时刻表中的班次，以确保每个必需班次都得到覆盖。车队规模通常是核心目标，因为使用更少的车辆可以降低运营需求和成本。该问题在大规模情况下难以精确求解，因此研究者会采用基于匹配等算法方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.semanticscholar.org/paper/A-Hierarchical-Matching-Based-Approach-for-Vehicle-Shen-Li/820ef39a79a1c1ad6c402bbfc3b4844284e9576c">A Hierarchical Matching-Based Approach for Vehicle Scheduling</a></li>

</ul>
</details>

**标签**: `#vehicle scheduling`, `#optimization`, `#matching algorithms`, `#transportation systems`, `#operations research`

---

<a id="item-14" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11559800" data-hz-title="多模式公交网络与时刻表一体化设计" data-hz-tags="transportation optimization,public transit,timetable synchronization,operations research" data-hz-section="hust-research"></a>
## [多模式公交网络与时刻表一体化设计](https://doi.org/10.1109/ccdc69976.2026.11559800) ⭐️ 5.0/10

该研究考察多模式公共交通系统中的公交网络联合设计与时刻表同步。现有信息未说明具体算法、数据集或量化结果。 将网络结构与发车时间协调起来，可能改善不同交通方式之间的换乘并减少乘客等待时间，从而应对公共交通规划中的实际难题。目前其意义主要体现在方法层面，因为现有材料尚未证明具体的运营改进效果。 公共交通网络设计通常被视为非线性优化问题，而时刻表同步可以将乘客总换乘等待时间作为优化目标。由于未提供论文正文，现有信息无法判断其目标函数、运营约束、求解方法和局限性。

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · 5月15日 00:00

**匹配依据**: 论文关键词命中 **timetable**（系统工程与决策优化）。

**关联教师**: 余明晖、俞耀文、刘振元、刘智伟、刘磊、刘骁康、卢仁智、叶林涛 等共 25 人

**背景**: 公共交通网络设计问题关注如何安排公共交通系统中的线路和连接关系。时刻表同步则协调不同服务的出发和到达时间，使乘客在不同交通方式之间换乘时等待更短。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.academia.edu/80977335/Integrated_Multimodal_Transit_Route_Network_Design_with_Feeder_Systems">(PDF) Integrated Multimodal Transit Route Network Design with...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0191261519301201">Transit timetable synchronization for transfer time ...</a></li>

</ul>
</details>

**标签**: `#transportation optimization`, `#public transit`, `#timetable synchronization`, `#operations research`

---

## 其他资讯

15. [腾讯发布 7700 亿参数开放权重模型 Hy4 预览版](#item-15) ⭐️ 9.0/10
16. [为 2.4 亿个域名实现 P99 零毫秒自动补全](#item-16) ⭐️ 8.0/10
17. [理解 ChatGPT Work 的云端与本地智能代理工作流](#item-17) ⭐️ 8.0/10
18. [连续扩散语言模型重新探索整序列生成](#item-18) ⭐️ 8.0/10
19. [QubesOS 通过 Dom0 文件复制暴露代码执行漏洞](#item-19) ⭐️ 8.0/10
20. [新型云安全缺陷暴露多租户基础设施风险](#item-20) ⭐️ 8.0/10
21. [美国发射新太空望远镜绘制宇宙地图](#item-21) ⭐️ 8.0/10
22. [扩散语言模型构建指南](#item-22) ⭐️ 7.0/10
23. [探秘 1980 年太空实验室磁芯存储器模块](#item-23) ⭐️ 7.0/10
24. [OpenClaw 2.0 提升常驻人工智能代理的影响力](#item-24) ⭐️ 7.0/10
25. [8B 模型让手机实现本地视频剪辑规划](#item-25) ⭐️ 7.0/10
26. [人工智能视频冲击中国数字演员零工经济](#item-26) ⭐️ 7.0/10
27. [美国与伊朗在霍尔木兹海峡互相发动袭击](#item-27) ⭐️ 7.0/10
28. [Hugging Face 推出 399 美元端侧大模型设备](#item-28) ⭐️ 7.0/10
29. [伯克利轻量人形机器人降低成本](#item-29) ⭐️ 7.0/10
30. [AMD 以异构 SoC 进军机器人领域](#item-30) ⭐️ 7.0/10
31. [微软让 WinUI 完全开源](#item-31) ⭐️ 7.0/10
32. [Hugging Face 推出可学习的新型开源机器人 Microduck](#item-32) ⭐️ 7.0/10
33. [Code-as-World 将视频转换为可执行的 MuJoCo 模拟](#item-33) ⭐️ 7.0/10
34. [Opener 开源 DECT NR+ 物联网技术](#item-34) ⭐️ 7.0/10
35. [美国限制无人机和机器人，竞争或转向海外](#item-35) ⭐️ 6.0/10
36. [OpenMAIC 将多智能体人工智能课堂带到 GitHub](#item-36) ⭐️ 6.0/10
37. [科学智能体技能扩展人工智能科研工作流](#item-37) ⭐️ 6.0/10
38. [OpenShot 4.0 将视频编辑器界面迁移至 Qt6](#item-38) ⭐️ 6.0/10
39. [Roblox 向 ROOST 模型社区开放安全模型](#item-39) ⭐️ 6.0/10
40. [黑客遭恶意软件感染，攻击基础设施遭曝光](#item-40) ⭐️ 6.0/10
41. [Sanctuary AI 将单独出售机器人“大脑”](#item-41) ⭐️ 6.0/10
42. [《The Sequence》综述人工智能不断扩大的工业作用](#item-42) ⭐️ 6.0/10
43. [马斯克加速燃气轮机计划引发污染担忧](#item-43) ⭐️ 5.0/10
44. [卡特彼勒将采矿自动化经验用于人工智能部署](#item-44) ⭐️ 5.0/10

---

<a id="item-15" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Aug/29/hy4/" data-hz-title="腾讯发布7700亿参数开放权重模型Hy4预览版" data-hz-tags="Large Language Models,Open Weights,Mixture of Experts,Long Context,Tencent" data-hz-section="other"></a>
## [腾讯发布 7700 亿参数开放权重模型 Hy4 预览版](https://simonwillison.net/2026/Aug/29/hy4/) ⭐️ 9.0/10

腾讯发布了 Hy4 预览版，这是一款仅支持文本输入的开放权重大语言模型，拥有 7700 亿总参数、490 亿激活参数和 100 万词元上下文窗口。与 7 月发布的 Hy3 相比，其总参数从 2950 亿增至 7700 亿，激活参数从 210 亿增至 490 亿，上下文长度则从 25.6 万词元增至 100 万词元。 Hy4 预览版提高了开放权重模型在规模和长上下文能力方面的上限，可能为研究和部署提供更多闭源接口之外的选择。其混合专家架构可以在每次处理输入时只激活较小的一部分参数，同时保留庞大的模型容量，但完整模型仍然带来很高的存储和推理部署要求。 Hugging Face 上的模型文件约占 1.56 TB，而且该模型仅支持文本输入，不具备视觉能力。它的聊天模板支持两种推理设置，默认值为 high，另一种为 no_think；通过 OpenRouter 进行的示例显示，它能够生成 SVG 风格的图像描述，并出现了使用简略英语表达的推理轨迹。

rss · Simon Willison · 8月29日 23:53

**背景**: 在混合专家模型中，总参数量包括所有专家组件，而激活参数量指模型针对特定输入所选择的参数子集。这样，模型可以拥有很大的总容量，却不必为每个词元使用全部参数，不过完整权重的存储和部署成本仍可能很高。上下文窗口是模型一次能够处理的词元化文本数量，因此 100 万词元窗口可以容纳比 25.6 万词元窗口长得多的文档或对话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mindstudio.ai/blog/mixture-of-experts-architecture-glm-5-2-active-parameters">Mixture of Experts Architecture Explained: How GLM... | MindStudio</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/long-context">Long context | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Open Weights`, `#Mixture of Experts`, `#Long Context`, `#Tencent`

---

<a id="item-16" class="hz-item-anchor" data-hz-url="https://ruurtjan.com/articles/p99-0ms-autocomplete-for-240-million-domain-names" data-hz-title="为2.4亿个域名实现P99零毫秒自动补全" data-hz-tags="Autocomplete,Low-Latency Systems,Distributed Systems,Performance Engineering,Tries and Indexing" data-hz-section="other"></a>
## [为 2.4 亿个域名实现 P99 零毫秒自动补全](https://ruurtjan.com/articles/p99-0ms-autocomplete-for-240-million-domain-names) ⭐️ 8.0/10

文章介绍了一种为 2.4 亿个域名提供近似零毫秒 P99 自动补全的架构。文章重点分析了让最慢的百分之一请求看起来几乎即时所需的系统设计和性能取舍。 这种方法说明，自动补全系统可以将尾延迟而非平均响应时间作为优化目标，这对交互式应用十分重要。它还展示了全球一致的响应速度、网络距离、实现复杂度和域名建议质量之间的矛盾。 社区反馈指出了几个重要限制：部分推荐的域名可能并不存在，使用按键释放事件触发请求可能增加不必要的延迟，而距离服务位置较远的用户可能无法感受到所宣称的响应速度。评论还提出了按域名流行度加权的残差预测，以及将字典树节点存储为可通过内容分发网络访问的文件，以降低地理网络延迟。

hackernews · dbalatero · 8月31日 03:20 · [社区讨论](https://news.ycombinator.com/item?id=49505219)

**背景**: P99 是一种尾延迟指标，表示百分之九十九的请求都能在该延迟以内完成，因此它反映了最慢百分之一请求的体验。字典树也称为前缀树，它按照字符串中的连续字符存储内容，能够高效执行前缀查找，因此常用于自动补全。自动补全系统通常会预先计算或缓存各个前缀的结果，从而让每次按键只需执行极少的工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://duckkit.dev/glossary/latency-sre/tail-latency">Tail latency | duckkit.dev</a></li>
<li><a href="https://www.systemdesignsandbox.com/learn/design-autocomplete">Search Autocomplete (Typeahead) | System Design Sandbox</a></li>
<li><a href="https://www.geeksforgeeks.org/dsa/introduction-to-trie-data-structure-and-algorithm-tutorials/">Trie Data Structure - Commonly Asked Questions - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 评论者总体认可其中的性能工程思路，但质疑用户体验以及“零毫秒”这一说法的实际含义。主要争议包括推荐不存在的域名、使用按键释放事件触发请求、澳大利亚等地区的网络延迟，以及预测索引或由内容分发网络托管的字典树节点能否提供更简单且更适合全球用户的方案。

**标签**: `#Autocomplete`, `#Low-Latency Systems`, `#Distributed Systems`, `#Performance Engineering`, `#Tries and Indexing`

---

<a id="item-17" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/" data-hz-title="理解 ChatGPT Work 的云端与本地智能代理工作流" data-hz-tags="AI agents,ChatGPT,computer use,developer tools,AI security" data-hz-section="other"></a>
## [理解 ChatGPT Work 的云端与本地智能代理工作流](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

Simon Willison 分析了 OpenAI 于 7 月 9 日宣布的 ChatGPT Work，并区分了云端版本与基于桌面应用、此前与 Codex 相关的本地版本。他的测试显示，云端产品增加了模型选择、可联网的代码执行环境、无头 Chrome 浏览器、跨会话共享的持久化文件系统、可发布的 ChatGPT Sites、子代理以及可能的定时提示词自动化功能。 ChatGPT Work 让人工智能助手从回答问题进一步转向使用浏览器、代码、文件和委托子代理来完成多步骤任务。这可能推动面向开发者和其他付费用户的计算机操作自动化，但也会放大代理访问私人数据和外部内容所带来的安全后果。 目前，Work 仅向每月支付 20 美元或更高费用的订阅者开放，而且云端版与本地版提供的能力并不相同。云端界面提供 GPT-5.6 Sol、Luna 和 Terra 以及多种推理级别；文章同时指出，具体模型对应关系仍不明确，使用量可能计入 Code 配额，并警告将私人数据访问、不可信内容和向外传输信息的渠道结合起来会带来安全风险。

rss · Simon Willison · 8月30日 23:59 · [社区讨论](https://news.ycombinator.com/item?id=49504625)

**背景**: 人工智能代理是一种能够跨多个步骤进行推理并使用浏览器、终端或文件系统等工具的系统，而不只是生成文本。代码执行和浏览器访问让代理能够检查数据并采取行动，持久化存储则允许信息在不同会话之间保留。代理系统通常通过沙箱和权限控制限制文件系统及网络访问，因为外部文档、电子邮件或网站可能包含恶意指令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/alifunk/when-ai-agents-become-the-attack-surface-architecting-against-self-propagating-threats-4olp">When AI Agents Become the Attack Surface... - DEV Community</a></li>
<li><a href="https://code.visualstudio.com/docs/agents/concepts/trust-and-safety">Trust and safety</a></li>
<li><a href="https://www.room714.com/en/blog/ai-architecture-security-the-gap-nobody-audits">AI Architecture Security : The Gap Nobody Audits Until... | Room 714</a></li>

</ul>
</details>

**社区讨论**: 评论者认为计算机操作能力非常实用，例如通过远程和语音指令处理电子邮件、文档和表单。其他评论将 ChatGPT Work 视为 OpenAI 对 Claude Cowork 的竞争性回应，同时有评论强调，系统把私人数据访问、不可信内容暴露以及向攻击者传输信息的渠道结合在了一起，构成严重安全风险。

**标签**: `#AI agents`, `#ChatGPT`, `#computer use`, `#developer tools`, `#AI security`

---

<a id="item-18" class="hz-item-anchor" data-hz-url="https://sander.ai/2026/08/24/continuous-dlms.html" data-hz-title="连续扩散语言模型重新探索整序列生成" data-hz-tags="Diffusion Models,Large Language Models,Generative AI,Neural Network Architectures,AI Research" data-hz-section="other"></a>
## [连续扩散语言模型重新探索整序列生成](https://sander.ai/2026/08/24/continuous-dlms.html) ⭐️ 8.0/10

Sander Dieleman 考察了连续扩散语言模型重新受到关注的现象，这类模型通过反复优化整个序列来生成语言，而不是严格按照从左到右的顺序解码。在早期连续方法之后，离散扩散方法一度占据主流，如今连续方法正重新进入研究视野。 整序列优化可以让各个词元在多轮处理中相互影响，从而有机会提升连贯性，而不是让模型对每个下一个词元做出不可逆的决定。如果这种方法能够在大规模应用中实现高效率和有竞争力的性能，就可能影响语言模型架构、可控推理，以及语言系统中并行计算与顺序计算之间的取舍。 连续扩散通过在连续嵌入空间中执行扰动过程，来处理离散语言词元与高斯噪声之间的不匹配。该方法仍存在重要限制：扩散语言模型通常需要多轮优化，并且不像自回归模型那样能够直接使用标准键值缓存，不过一致性方法 CDLM 正尝试同时降低这两项成本。

hackernews · peter_d_sherman · 8月30日 20:46 · [社区讨论](https://news.ycombinator.com/item?id=49502611)

**背景**: 自回归语言模型按照顺序生成文本，每个新词元都根据已经生成的词元进行预测。扩散语言模型则从带噪声、被遮盖或不完整的序列开始，通过多轮重建逐步生成文本，因此可以同时处理多个位置。在连续扩散中，序列在加噪和去噪过程中使用连续嵌入空间表示，但最终输出仍然是离散的语言词元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sander.ai/2026/08/24/continuous-dlms.html">Continuous diffusion language models – Sander Dieleman</a></li>
<li><a href="https://arxiv.org/abs/2511.19269">[2511.19269] CDLM: Consistency Diffusion Language Models For ... CDLM: Consistency Diffusion Language Models For Faster Sampling Continuous Diffusion Language Models (CDLM's) — Botonomous.ai Continuous Diffusion Rivals Discrete in Language Modeling Continuous Diffusion Language Models (CDLMs) Are Back—Why Now</a></li>
<li><a href="https://james.trappett.org/blog/continuous-diffusion-language-models-a-technical-revival/">Continuous Diffusion Language Models: A Technical Revival</a></li>

</ul>
</details>

**社区讨论**: 讨论总体上对扩散语言模型持兴趣态度，一些评论者认为整序列优化可能比自回归采样更加连贯。另一些人质疑文章对自回归模型历史主导地位的描述，还有人设想让模型以不同速率思考，并将推理草稿与输出文本交错生成；评论也指出，实际效率仍是关键问题。

**标签**: `#Diffusion Models`, `#Large Language Models`, `#Generative AI`, `#Neural Network Architectures`, `#AI Research`

---

<a id="item-19" class="hz-item-anchor" data-hz-url="https://www.qubes-os.org/news/2026/08/29/qsb-118/" data-hz-title="QubesOS通过Dom0文件复制暴露代码执行漏洞" data-hz-tags="QubesOS,Security,Vulnerability,Arbitrary Code Execution,Operating Systems" data-hz-section="other"></a>
## [QubesOS 通过 Dom0 文件复制暴露代码执行漏洞](https://www.qubes-os.org/news/2026/08/29/qsb-118/) ⭐️ 8.0/10

QubesOS 中，`qvm-copy-to-vm`使用的 Dom0 错误报告后备通道存在漏洞，在特定条件下可能导致任意代码执行。VM 版本的`qvm-copy-to-vm`不受影响，因为其错误报告实现不使用`system()`。 该问题表明，即使是 QubesOS 中范围很小的特权工作流，也可能让与不受信任虚拟机相关的数据进入 Dom0 并触发代码执行。实际风险受到必须从 Dom0 执行文件复制这一条件的限制，但 Dom0 遭到攻破尤其严重，因为它负责 QubesOS 的核心管理与隔离功能。 受影响的路径明确与从 Dom0 向虚拟机复制文件，以及调用`system()`的错误报告功能有关，而对应的虚拟机端路径不受影响。社区讨论还强调，QubesOS 不建议使用 Dom0 进行日常工作或与可能已感染的虚拟机交互，这会缩小可能的攻击面，但无法消除该漏洞。

hackernews · vntok · 8月30日 08:51 · [社区讨论](https://news.ycombinator.com/item?id=49496918)

**背景**: QubesOS 将不同活动分隔到相互隔离的虚拟机中，而 Dom0 是负责系统重要部分的特权管理域。`qvm-copy-to-vm`等工具用于在不同域之间传输文件，Qubes 还使用 qrexec 等虚拟机间通信机制来支持受控交互。由于 Dom0 具有特权地位，在其中执行代码的后果通常比在普通虚拟机中执行代码更严重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49496918">Arbitrary code execution in QubesOS via copy - to - VM error reporting ...</a></li>
<li><a href="https://doc.qubes-os.org/en/latest/developer/services/qrexec.html">Qrexec: secure communication across domains - Qubes OS</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为该漏洞较为严重，但也指出其触发条件较窄，即必须从 Dom0 执行复制，因此遵循 QubesOS 操作建议的用户面临的利用可能性较低。其他评论围绕 QubesOS 规模较小但并非为零的攻击面展开讨论，另有一些评论谈到了项目的易用性和图形功能限制，但这些内容与漏洞本身没有直接关系。

**标签**: `#QubesOS`, `#Security`, `#Vulnerability`, `#Arbitrary Code Execution`, `#Operating Systems`

---

<a id="item-20" class="hz-item-anchor" data-hz-url="https://newsletter.semianalysis.com/p/most-neoclouds-suck-at-security" data-hz-title="新型云安全缺陷暴露多租户基础设施风险" data-hz-tags="Cloud Security,Container Security,Multi-Tenancy,Kubernetes,Infrastructure Security" data-hz-section="other"></a>
## [新型云安全缺陷暴露多租户基础设施风险](https://newsletter.semianalysis.com/p/most-neoclouds-suck-at-security) ⭐️ 8.0/10

文章分析了新型云服务商的安全弱点，涵盖容器逃逸、内核旁路网络、网络策略、安全密钥和多租户 Grafana。文章还讨论了 OpenAI 与 Hugging Face 的对比，并预览了 ClusterMAX 3.0。 新型云平台将专用基础设施与共享服务结合在一起，因此隔离、身份验证、网络或可观测性方面的缺陷可能影响多个客户。这项分析对评估敏感工作负载云服务商的组织，以及设计安全多租户系统的工程师都具有参考价值。 容器逃逸可能将容器内的低权限访问扩大为对主机或整个集群的访问，而内核旁路网络会将数据包处理移至用户空间，从而减少内核层面的检查。因此，多租户 Grafana 和网络策略需要严格的租户隔离、访问控制与监控。

rss · Semianalysis（半导体·AI 风向标） · 8月30日 15:46

**背景**: 容器会将应用及其依赖打包在一起，同时共享主机操作系统内核，因此配置错误或漏洞可能削弱容器与主机之间的边界。内核旁路网络通过用户空间机制处理网络操作，而不是使用传统的内核网络栈，通常可以降低延迟，但也带来不同的安全考量。多租户意味着多个客户共享底层服务，因此必须隔离数据、查询、凭据和管理访问权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unit42.paloaltonetworks.com/container-escape-techniques/">Container Breakouts: Escape Techniques in Cloud Environments</a></li>
<li><a href="https://blog.cloudflare.com/kernel-bypass/">Kernel bypass | Cloudflare Blog</a></li>
<li><a href="https://grafana.com/docs/loki/latest/operations/multi-tenancy/">Manage tenant isolation | Grafana Loki documentation</a></li>

</ul>
</details>

**标签**: `#Cloud Security`, `#Container Security`, `#Multi-Tenancy`, `#Kubernetes`, `#Infrastructure Security`

---

<a id="item-21" class="hz-item-anchor" data-hz-url="https://www.bbc.co.uk/news/articles/ce87e55vgpjo?at_medium=RSS&at_campaign=rss" data-hz-title="美国发射新太空望远镜绘制宇宙地图" data-hz-tags="Astronomy,Space Exploration,Dark Matter,Dark Energy,宇宙学" data-hz-section="other"></a>
## [美国发射新太空望远镜绘制宇宙地图](https://www.bbc.co.uk/news/articles/ce87e55vgpjo?at_medium=RSS&at_campaign=rss) ⭐️ 8.0/10

美国国家航空航天局发射了一台功能强大的新太空望远镜，开始执行一项持续多年的任务，为宇宙绘制新地图。该任务将研究暗物质和暗能量。 大规模宇宙地图可以帮助科学家更好地理解宇宙结构如何分布和演化。望远镜的观测结果还可能为暗物质以及与暗能量相关的宇宙加速膨胀提供重要证据。 这台望远镜预计将运行数年，重点是绘制宇宙地图，而不是进行一次短期观测。现有报道没有提供望远镜仪器、发射载具或观测时间表的具体信息。

rss · BBC World News · 8月30日 18:53

**背景**: 暗物质主要是通过引力效应被推断出来的，因为它似乎不会以可见的方式与普通物质和辐射发生相互作用。暗能量与宇宙加速膨胀有关，似乎主要产生大尺度影响，而不是局部影响。通过绘制宇宙结构，天文学家可以研究与这两种现象相关的线索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_matter">Dark matter - Wikipedia</a></li>
<li><a href="https://home.cern/science/physics/dark-matter/">Dark matter – Home | CERN</a></li>

</ul>
</details>

**标签**: `#Astronomy`, `#Space Exploration`, `#Dark Matter`, `#Dark Energy`, `#宇宙学`

---

<a id="item-22" class="hz-item-anchor" data-hz-url="https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/" data-hz-title="扩散语言模型构建指南" data-hz-tags="Diffusion Models,Language Models,Generative AI,Deep Learning,Model Architecture" data-hz-section="other"></a>
## [扩散语言模型构建指南](https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/) ⭐️ 7.0/10

这篇文章介绍了如何构建扩散语言模型，为传统自回归语言生成提供了另一种方案。文章还围绕其数学基础、解码效率、置信度估计和可能的扩展方向展开讨论。 扩散语言模型可以通过迭代去噪同时生成或修改多个词元，而不是严格按照从左到右的顺序生成文本，这可能提升解码的灵活性和速度。它们的发展可能拓展生成式语言模型的设计空间，尤其适用于离散词元建模和本地推理。 相关技术讨论涉及证据下界（ELBO）、重要性采样、离散扩散和置信度感知解码，这些因素决定了训练目标与生成过程的设计。社区反馈也指出了一个实际限制：尽管 DiffusionGemma 等模型在 GPU 上的每秒输出词元数可能很高，但置信度估计以及质量与计算资源之间的权衡仍然值得关注。

hackernews · volodia · 8月30日 23:41 · [社区讨论](https://news.ycombinator.com/item?id=49503956)

**背景**: 自回归语言模型通常一次生成一个词元，并根据前面的序列预测下一个词元。扩散语言模型则会对文本进行加噪或掩码处理，再通过多轮去噪学习还原文本。在离散文本场景中，模型处理的是词元而不是连续的图像像素，因此训练目标和去噪调度方式都是重要的设计问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ultralytics.com/glossary/diffusion-language-models">Diffusion Language Models: How They Work and Applications</a></li>
<li><a href="https://ar5iv.labs.arxiv.org/html/2303.06574">Diffusion Models for Non-autoregressive Text Generation : A Survey</a></li>
<li><a href="https://arxiv.org/html/2603.22248v1">Confidence-Based Decoding is Provably Efficient for Diffusion ...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论总体上积极且具有教育意义：一位评论者认为推导 ELBO 有助于理解相关数学结构，另一位则建议研究基于图像的文本生成，以避开离散词元生成的一些困难。其他评论者称赞 DiffusionGemma 在 GPU 上的速度和本地使用体验，但也指出置信度估计受到的关注不足，现有结果可能仍受时间和计算资源限制。

**标签**: `#Diffusion Models`, `#Language Models`, `#Generative AI`, `#Deep Learning`, `#Model Architecture`

---

<a id="item-23" class="hz-item-anchor" data-hz-url="https://www.righto.com/2026/08/spacelab-core-memory.html" data-hz-title="探秘1980年太空实验室磁芯存储器模块" data-hz-tags="computer architecture,core memory,space computing,reliability engineering,hardware history" data-hz-section="other"></a>
## [探秘 1980 年太空实验室磁芯存储器模块](https://www.righto.com/2026/08/spacelab-core-memory.html) ⭐️ 7.0/10

一篇逆向工程分析文章研究了 1980 年太空实验室计算机使用的磁芯存储器模块，包括其独特架构和工程权衡。该计算机的存储器由四块磁芯平面电路板组成，在磁芯存储器已经较晚使用的时期仍属于先进且高密度的设计。 该模块展示了在半导体存储器占据主流之前，航天计算机如何优先考虑可靠性并控制硬件复杂度。它也有助于理解抗辐射太空计算，以及关键系统所面临的可靠性约束如何影响设计。 据搜索结果，太空实验室计算机没有使用微处理器，而是由分布在多块电路板上的离散 TTL 逻辑芯片构成 16 位中央处理器。社区讨论还关注了不使用禁止线的架构，并提出这可能主要是为了减少读出放大器数量和简化电路板布局，而不一定是为了提高速度。

hackernews · pwg · 8月30日 20:00 · [社区讨论](https://news.ycombinator.com/item?id=49502214)

**背景**: 磁芯存储器通过穿有导线的小型铁氧体磁芯的磁状态来存储数据位。它曾因可靠性较高和访问时间相对较短而受到重视，但后来逐渐被半导体存储器取代。在航天器中，存储技术还必须结合辐射引发的故障模式和整个系统的可靠性要求进行评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.righto.com/2026/08/spacelab-core-memory.html">Cores in space: The core memory module from a 1980 Spacelab ...</a></li>
<li><a href="https://www.squaredtech.co/spacelabs-1980-computer-stunning-reverse-engineering-revealed">Spacelab Computer 1980 : Surprising Reverse-Engineering Find</a></li>
<li><a href="https://nepp.nasa.gov/files/25506/NEPPETW2010_LaBel_Memory.pdf">Memory Overview – Technologies and Needs - NASA</a></li>

</ul>
</details>

**社区讨论**: 评论总体赞赏磁芯存储器在关键系统和航天系统中的可靠性，同时讨论了无禁止线架构对速度、读出放大器数量和电路板布局的影响。一位评论者还将其联系到现代大语言模型系统中的冗余设计，但这一比较与文章主题只有部分关联。

**标签**: `#computer architecture`, `#core memory`, `#space computing`, `#reliability engineering`, `#hardware history`

---

<a id="item-24" class="hz-item-anchor" data-hz-url="https://openclaw.ai/blog/openclaw-2-accidentally" data-hz-title="OpenClaw 2.0提升常驻人工智能代理的影响力" data-hz-tags="AI agents,autonomous systems,AI security,LLM safety,developer tools" data-hz-section="other"></a>
## [OpenClaw 2.0 提升常驻人工智能代理的影响力](https://openclaw.ai/blog/openclaw-2-accidentally) ⭐️ 7.0/10

OpenClaw 2.0 被介绍为这一开源自主代理项目的一次重大更新，相关报道提到此次更新包含约 16,000 项变更。新版本加入了重构后的浏览器应用、更简便的安装方式、共享云端会话，以及对 ChatGPT、Claude、应用程序接口密钥和本地人工智能模型的支持。 这一发布体现了人工智能代理正从对话式助手发展为能够持续在线、调用工具并跨服务执行操作的系统。更强的能力可能帮助开发者和高级用户，但也会放大提示注入、权限过度和意外操作所带来的后果。 OpenClaw 采用自托管方式，并以消息平台作为主要交互界面；据报道，2.0 版本扩展了浏览器、会话、安装和模型集成功能。社区讨论强调，如果让常驻代理接触不可信的互联网文本或敏感账户，可能扩大权限提升和数据泄露的影响范围，因此沙箱隔离和人工监督仍是重要限制。

hackernews · doppp · 8月31日 03:38 · [社区讨论](https://news.ycombinator.com/item?id=49505310)

**背景**: 自主人工智能代理是一类利用大型语言模型规划任务、调用工具、访问数据并执行操作的软件，而不只是生成文字。OpenClaw 以消息平台作为主要交互界面，使用户能够与运行在自托管环境中的代理通信。安全问题在于，代理读取的文本可能包含试图操纵其行为的指令，尤其是在代理拥有高权限工具或个人账户访问权限时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems">Secure autonomous agentic AI systems | Microsoft Learn</a></li>
<li><a href="https://www.news9live.com/technology/artificial-intelligence/openclaw-2-0-update-ai-agents-multiplayer-16000-pull-requests-3003676">OpenClaw 2.0 is here with 16,000 changes, new AI agents and ...</a></li>

</ul>
</details>

**社区讨论**: 这 101 条评论的态度较为分化：一些用户分享了在容器中运行代理框架的实际收益，另一些人则质疑常驻代理究竟能完成哪些有价值的任务，或认为类似助手很容易自行构建。最强烈的批评集中在提示诱导的权限提升、电子邮件和金融账户暴露，以及在缺乏可靠隔离的情况下将自主软件连接到重要系统的风险上。

**标签**: `#AI agents`, `#autonomous systems`, `#AI security`, `#LLM safety`, `#developer tools`

---

<a id="item-25" class="hz-item-anchor" data-hz-url="https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247916663&idx=2&sn=174f44f53f5fb8296479fc52f461ad5f" data-hz-title="8B模型让手机实现本地视频剪辑规划" data-hz-tags="小语言模型,端侧AI,视频剪辑,多模态模型,模型自我进化" data-hz-section="other"></a>
## [8B 模型让手机实现本地视频剪辑规划](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247916663&idx=2&sn=174f44f53f5fb8296479fc52f461ad5f) ⭐️ 7.0/10

vivo AI Lab 与香港中文大学（深圳）的研究团队据报道提出了 RefineCut 框架，让一个 8B 开源模型反复修改剪辑方案，并由确定性验证器进行评分。据报道，该方法结合了多教师蒸馏与偏好优化训练，并已被 EMNLP 2026 主会接收。 这项方法表明，能力较强的视频剪辑规划有望从依赖云端前沿模型转向在手机上运行的小模型。它可能降低延迟和接口成本，同时改善隐私保护，并让设备厂商和用户更容易使用自动化且更稳定的剪辑功能。 RefineCut 将隐含在提示词中的决策转化为可以逐条检查的显式剪辑计划，并由验证器提供训练信号。报道中的比较是在相同闭环协议下进行的，因此 8B 模型超过两位教师模型并追平 DeepSeek-V4-Pro 的说法，不应被理解为其在所有视频剪辑任务上都具有普遍优势。

rss · 量子位 · 8月30日 02:19

**背景**: 8B 模型大约包含八十亿个参数，通常比许多前沿模型更小，因此更适合在本地设备上部署。在这一场景中，视频剪辑规划是决定选用哪些片段、时间点和其他操作，而不是直接渲染最终视频。验证器是一种按照指定标准检查剪辑方案是否合格的规则化或确定性组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.x-techcon.com/article/180860.html">手机本地一键成片，靠的是一个8B小模型的自我进化 | EMNLP'26</a></li>
<li><a href="https://news.sig.ai/cn/article/cmtfj4roy0001fkufbinbahhn">手机本地一键成片，全靠8B自我进化量子位 | 信鸽中文</a></li>

</ul>
</details>

**标签**: `#小语言模型`, `#端侧AI`, `#视频剪辑`, `#多模态模型`, `#模型自我进化`

---

<a id="item-26" class="hz-item-anchor" data-hz-url="https://marginalrevolution.com/marginalrevolution/2026/08/china-fact-of-the-day-81.html?utm_source=rss&utm_medium=rss&utm_campaign=china-fact-of-the-day-81" data-hz-title="人工智能视频冲击中国数字演员零工经济" data-hz-tags="Generative AI,AI video,Automation,Labor displacement,China tech" data-hz-section="other"></a>
## [人工智能视频冲击中国数字演员零工经济](https://marginalrevolution.com/marginalrevolution/2026/08/china-fact-of-the-day-81.html?utm_source=rss&utm_medium=rss&utm_campaign=china-fact-of-the-day-81) ⭐️ 7.0/10

包括字节跳动 Seedance 2.0 在内的先进人工智能视频生成工具，正越来越多地支持数字演员取代中国网络娱乐行业中的真人表演者。这一变化正在威胁中国零工经济中一个曾经活跃的就业领域。 这一发展表明，生成式人工智能正从实验阶段走向替代劳动力，并可能影响大量演员和网络 influencer。它可以降低内容制作成本，但也会加剧依赖数字娱乐获得收入的劳动者所面临的压力。 字节跳动称，Seedance 2.0 采用统一的多模态音视频生成架构，可接收文本、图像、音频和视频输入，并支持复杂的内容参考与编辑。现有报道没有提供受影响岗位数量、实际采用规模，或真人表演者是否会被完全取代的充分证据。

rss · Marginal Revolution · 8月30日 04:25

**背景**: 人工智能视频生成模型可以根据指令和其他参考媒体生成动态影像，而不必让真人表演者参与每个场景的拍摄。多模态模型能够结合文本、图像、音频和视频等输入，以引导生成结果。在网络娱乐领域，这些能力可以更低成本、更快速地制作数字角色和短视频内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/seedance2_0">Seedance 2.0 - seed.bytedance.com</a></li>
<li><a href="https://seed.bytedance.com/en/models">Seed Models - seed.bytedance.com</a></li>

</ul>
</details>

**标签**: `#Generative AI`, `#AI video`, `#Automation`, `#Labor displacement`, `#China tech`

---

<a id="item-27" class="hz-item-anchor" data-hz-url="https://www.bbc.co.uk/news/articles/cx2z72x5z1po?at_medium=RSS&at_campaign=rss" data-hz-title="美国与伊朗在霍尔木兹海峡互相发动袭击" data-hz-tags="US-Iran relations,military conflict,Strait of Hormuz,geopolitics,regional security" data-hz-section="other"></a>
## [美国与伊朗在霍尔木兹海峡互相发动袭击](https://www.bbc.co.uk/news/articles/cx2z72x5z1po?at_medium=RSS&at_campaign=rss) ⭐️ 7.0/10

美国与伊朗数周来首次互相发动袭击。美国对霍尔木兹海峡拉拉克岛的袭击据报道造成两人死亡、两人受伤，也是已知自 7 月底以来美国在当地的首次袭击。 此次互相袭击表明，华盛顿与德黑兰在这一具有重要战略意义的水道附近再次出现直接军事升级。冲突进一步扩大可能加剧地区安全风险，并影响全球能源市场。 据报道，拉拉克岛袭击造成两人死亡、两人受伤。现有信息称这是已知自 7 月底以来的首次美国袭击，但没有提供更多行动细节。

rss · BBC World News · 8月31日 08:34

**背景**: 霍尔木兹海峡是报道中袭击发生的具有重要战略意义的水道。美国与伊朗直接发动袭击，意味着两国关系中的军事升级更加公开和直接。

**标签**: `#US-Iran relations`, `#military conflict`, `#Strait of Hormuz`, `#geopolitics`, `#regional security`

---

<a id="item-28" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiU0FVX3lxTE10anNQWUJyb2dveFQyMkR5eFFBNzFBMjJaS2hJN1ppOVBnYURsaE9ka1FlVzFTdlRhN25aRnBDYlB6SDhJV0ZoS2wtbGt1X0FTNnZj?oc=5" data-hz-title="Hugging Face推出399美元端侧大模型设备" data-hz-tags="Hugging Face,On-device AI,Edge Computing,Large Language Models,AI Hardware" data-hz-section="other"></a>
## [Hugging Face 推出 399 美元端侧大模型设备](https://news.google.com/rss/articles/CBMiU0FVX3lxTE10anNQWUJyb2dveFQyMkR5eFFBNzFBMjJaS2hJN1ppOVBnYURsaE9ka1FlVzFTdlRhN25aRnBDYlB6SDhJV0ZoS2wtbGt1X0FTNnZj?oc=5) ⭐️ 7.0/10

Hugging Face 推出了一款售价 399 美元的设备，旨在降低端侧大语言模型实验和部署的成本。现有报道没有说明该设备的硬件配置、支持的模型或发布日期。 更低的设备价格可能扩大本地大语言模型开发的使用范围，并减少对云端推理的依赖。端侧运行还有望降低延迟、支持离线使用并改善隐私，但实际效果取决于设备性能和软件支持。 该消息带有较强的宣传性质，现有信息没有提供性能测试、内存容量、加速器规格、模型规模限制或部署软件等细节。据报道，Hugging Face 也在拓展机器人领域，其更广泛的硬件布局可追溯至 2024 年 3 月与 Rémi Cadene 及 Tesla Optimus 项目相关的工作。

google_news · 36 Kr · 8月31日 05:23

**背景**: 端侧大语言模型推理是指直接在本地设备上运行语言模型，而不是将请求发送到远程云服务。这种方式有助于应对隐私和网络连接问题，但本地硬件在算力和内存方面通常受到更严格的限制。关于神经网络处理器和适合移动设备的模型的研究，正致力于在这些限制下提升推理速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eu.36kr.com/en/p/3962888000181893">Hugging Face Launches Affordable $ 399 AI Device : Diving Deep Into...</a></li>
<li><a href="https://arxiv.org/abs/2407.05858">[2407.05858] Fast On - device LLM Inference with NPUs</a></li>

</ul>
</details>

**标签**: `#Hugging Face`, `#On-device AI`, `#Edge Computing`, `#Large Language Models`, `#AI Hardware`

---

<a id="item-29" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMinwFBVV95cUxOY3VoWlhBQzZPWFZFbnUtWUFqeXBMejFVcXNNVFQtT09yZkdXRlV4RFZYTmxmNXR4a3RtVFV0aHFhU3I4X3VjLXRENlVZb0JxbktYVkppM1BzS1c3RkdDVk5Sbkd0UG82RUtWTEwyTE52bUcyWHlvTnREaFdIM2VvTXNhU1p1a01rU0U0R2tNYzRyMGpCM0xCVEtOOTZiQ1U?oc=5" data-hz-title="伯克利轻量人形机器人降低成本" data-hz-tags="humanoid robotics,open source hardware,robot actuators,robotics research" data-hz-section="other"></a>
## [伯克利轻量人形机器人降低成本](https://news.google.com/rss/articles/CBMinwFBVV95cUxOY3VoWlhBQzZPWFZFbnUtWUFqeXBMejFVcXNNVFQtT09yZkdXRlV4RFZYTmxmNXR4a3RtVFV0aHFhU3I4X3VjLXRENlVZb0JxbktYVkppM1BzS1c3RkdDVk5Sbkd0UG82RUtWTEwyTE52bUcyWHlvTnREaFdIM2VvTXNhU1p1a01rU0U0R2tNYzRyMGpCM0xCVEtOOTZiQ1U?oc=5) ⭐️ 7.0/10

伯克利轻量人形机器人是一个开源人形机器人项目，通过在执行器中使用模块化三维打印齿轮箱和易于获得的组件，将目标成本控制在 5000 美元以下。该设计开放了机器人硬件和执行器技术，便于用户组装、定制和开展研究。 更低的硬件成本可以让无法负担商业平台的研究人员、学生和创客更容易接触人形机器人。开源方式还可能推动更广泛的实验，以及由社区共同改进人形机器人设计。 该平台重点采用模块化三维打印齿轮箱并支持定制，但现有信息无法证明它在性能、可靠性或安全性方面能够达到更昂贵商业人形机器人的水平。项目仍在持续发展，后续版本信息显示团队正在为未来的 V2 版本继续推进开发。

google_news · Open Source For You · 8月31日 07:58

**背景**: 执行器是让机器人产生运动的机构，齿轮箱则会调整电机的速度和扭矩，以适应特定动作需求。在该项目中，模块化三维打印齿轮箱被整合到执行器设计中，使部件相比专用工业硬件更容易制造和更换。开源硬件意味着项目公开设计资料，其他人可以据此组装、修改并参与改进平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/HybridRobotics/Berkeley-Humanoid-Lite">GitHub - HybridRobotics/berkeley-humanoid-lite: Codebase for ...</a></li>
<li><a href="https://lite.berkeley-humanoid.org/">Berkeley Humanoid Lite: An Open-source, Accessible, and ...</a></li>

</ul>
</details>

**标签**: `#humanoid robotics`, `#open source hardware`, `#robot actuators`, `#robotics research`

---

<a id="item-30" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMilAFBVV95cUxQX0FFT1NFTnNaeDNKbEtVLWlkVDBtVlFWN2toWjhLMVlMaFIzVC1CZW45aUg0NTE3cWc5UG1OZUdPSDdCdUEtWnB6MkNFMVhORHphRVhXSXBTQ3hQVDYyY0didUJrcW1EWFEtcDlDanJXY2lqYWk4MWZucVBEV1o1bVQ4Y0xHNWJfdWFsbFplLUNZcTlo?oc=5" data-hz-title="AMD以异构SoC进军机器人领域" data-hz-tags="AMD,Heterogeneous SoC,Robotics,Edge AI,Semiconductors" data-hz-section="other"></a>
## [AMD 以异构 SoC 进军机器人领域](https://news.google.com/rss/articles/CBMilAFBVV95cUxQX0FFT1NFTnNaeDNKbEtVLWlkVDBtVlFWN2toWjhLMVlMaFIzVC1CZW45aUg0NTE3cWc5UG1OZUdPSDdCdUEtWnB6MkNFMVhORHphRVhXSXBTQ3hQVDYyY0didUJrcW1EWFEtcDlDanJXY2lqYWk4MWZucVBEV1o1bVQ4Y0xHNWJfdWFsbFplLUNZcTlo?oc=5) ⭐️ 7.0/10

AMD 正在推进异构系统级芯片设计，以替代机器人和边缘人工智能领域以 GPU 为主导的方案。该策略旨在将不同类型的计算资源集成到单一芯片中，以服务这些应用。 如果取得成功，这种方案将为机器人开发者提供大型独立 GPU 之外的另一种选择，尤其适用于重视功耗、尺寸、延迟和集成度的场景。这也反映出半导体企业正在加剧竞争，推动更多人工智能处理能力部署到边缘设备中。 异构 SoC 会组合不同类型的处理单元，并可通过选择计算组件的组合来适配特定应用。现有报道没有提供具体的实现细节，因此尚不能证明某款产品已经推出、具备明确的性能优势，或能够确定取代基于 GPU 的系统。

google_news · EE Times Asia · 8月31日 02:30

**背景**: 系统级芯片会将主要计算功能集成到同一块芯片中，而不是分散在多个独立芯片上。异构设计会在芯片中加入不同类型的处理资源，分别处理不同工作负载，从而提升专用系统的灵活性和集成度。AMD 将其 Versal AI Edge 自适应 SoC 描述为支持机器人应用和异构传感器融合的单一设备方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/adaptive-socs-and-fpgas/versal/ai-edge-series.html">AMD Versal™ AI Edge Series</a></li>
<li><a href="https://arxiv.org/pdf/2009.01178">Agile SoC Development with Open ESP</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Heterogeneous SoC`, `#Robotics`, `#Edge AI`, `#Semiconductors`

---

<a id="item-31" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiigFBVV95cUxPNDcyT0pmaHBYNEd0M19JQm1YRk15eFJmMjJ2X1ZCV0tIdnF5VGNNcjAzN3RkVF9DSGFNZGVBWEF4TGw5VGhMLWRPQkZuSmlOLS1XWjltMUtUcWYzRjlGZDdma21OUUNBOERvZkxQc3J6TlJhakkzUGNTVDZ3S0hITmFBOFRVNkNjbkE?oc=5" data-hz-title="微软让 WinUI 完全开源" data-hz-tags="WinUI,Microsoft,Open Source,Windows Development,UI Frameworks" data-hz-section="other"></a>
## [微软让 WinUI 完全开源](https://news.google.com/rss/articles/CBMiigFBVV95cUxPNDcyT0pmaHBYNEd0M19JQm1YRk15eFJmMjJ2X1ZCV0tIdnF5VGNNcjAzN3RkVF9DSGFNZGVBWEF4TGw5VGhMLWRPQkZuSmlOLS1XWjltMUtUcWYzRjlGZDdma21OUUNBOERvZkxQc3J6TlJhakkzUGNTVDZ3S0hITmFBOFRVNkNjbkE?oc=5) ⭐️ 7.0/10

微软宣布，其现代 Windows 应用用户界面框架 WinUI 现已完全开源。主线开发已迁移到 GitHub，开发者可以创建分支、提交拉取请求并参与代码审查。 这一变化可以提高 WinUI 开发的透明度，并让 Windows 开发者生态在框架演进中发挥更大作用。它还可能促进社区贡献，为 Windows 应用提供更可预期的长期发展路径。 WinUI 3 作为 Windows App SDK 的一部分提供，面向 C# 和 C++ 开发者提供基于 XAML 的编程模型，并包含 Fluent Design 控件和高性能渲染功能。开源开发本身并不意味着每个 Windows 组件或所有产品决策都将由社区控制。

google_news · Open Source For You · 8月31日 07:38

**背景**: WinUI 3 是微软用于构建 Windows 桌面应用的现代原生用户界面框架。它采用 XAML 编程模型，旨在支持基于微软 Fluent Design System 的现代界面。Windows App SDK 将 WinUI 3 与其他面向 Windows 应用开发的功能结合在一起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/windows/apps/winui/winui3/">WinUI 3 - Windows apps | Microsoft Learn</a></li>
<li><a href="https://github.com/microsoft/microsoft-ui-xaml">GitHub - microsoft/microsoft-ui-xaml: WinUI: a modern UI ...</a></li>

</ul>
</details>

**标签**: `#WinUI`, `#Microsoft`, `#Open Source`, `#Windows Development`, `#UI Frameworks`

---

<a id="item-32" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMivwFBVV95cUxQemZqVUNlNnJZWUxIVFJocjdNMV9qcUkyYklXeFZUZzlmdV9WUkYyS054UGtBNk9lYWJWc3JncmQtNC1SS3BqSV9ZWUNHc1Z4OTdNcjYzRnZfaUZvaHZHLV9FOXFHcGhadndKcVFlbUwyWHdmZUpQNUN6V3dtdko5NVdON1kzR1dYZlhxNFdkcWlxWFhIdGdaTHZEcFFrVUJMeHVLenllYjN2bkJ1SWtvY1M4Q3A0YTlRTnh3YzRIY9IBxgFBVV95cUxPSmdMUkx5cXQ4UHA4ZVY5VE9QV1VwNFpTeVdhckNrc3NTdzk1MFp1T2FsWEVtd3htWkZaNXNEQ1htWm94Z3p2UmQtVXgyQS1CcFh6cjR6M0FSUWpPaW5CTW1IdjB1V2llMTVDYXFBM2N6MjBaLU9EOVluWDZvd0llRHl6aUhucDBqa2VQUHo5dzYycXNMRzBoRUdrN3R1dlN1cnJPSzFzTGp2djJBc1pqTnQ1MGZDZThDMGlqQ25pdG5SeWxFRkE?oc=5" data-hz-title="Hugging Face 推出可学习的新型开源机器人 Microduck" data-hz-tags="Robotics,Embodied AI,Open Source,Machine Learning,Hugging Face" data-hz-section="other"></a>
## [Hugging Face 推出可学习的新型开源机器人 Microduck](https://news.google.com/rss/articles/CBMivwFBVV95cUxQemZqVUNlNnJZWUxIVFJocjdNMV9qcUkyYklXeFZUZzlmdV9WUkYyS054UGtBNk9lYWJWc3JncmQtNC1SS3BqSV9ZWUNHc1Z4OTdNcjYzRnZfaUZvaHZHLV9FOXFHcGhadndKcVFlbUwyWHdmZUpQNUN6V3dtdko5NVdON1kzR1dYZlhxNFdkcWlxWFhIdGdaTHZEcFFrVUJMeHVLenllYjN2bkJ1SWtvY1M4Q3A0YTlRTnh3YzRIY9IBxgFBVV95cUxPSmdMUkx5cXQ4UHA4ZVY5VE9QV1VwNFpTeVdhckNrc3NTdzk1MFp1T2FsWEVtd3htWkZaNXNEQ1htWm94Z3p2UmQtVXgyQS1CcFh6cjR6M0FSUWpPaW5CTW1IdjB1V2llMTVDYXFBM2N6MjBaLU9EOVluWDZvd0llRHl6aUhucDBqa2VQUHo5dzYycXNMRzBoRUdrN3R1dlN1cnJPSzFzTGp2djJBc1pqTnQ1MGZDZThDMGlqQ25pdG5SeWxFRkE?oc=5) ⭐️ 7.0/10

Hugging Face 旗下的 Pollen Robotics 推出了 Microduck，这是一款售价 399 美元、旨在通过强化学习学习新行为的开源双足机器人。该机器人高 25 厘米，现已开放预订，预计在圣诞节前发货。 Microduck 将价格较低的实体平台与开源软件栈结合起来，可能让开发者、研究人员和爱好者更容易开展具身人工智能与机器人实验。它支持先在仿真环境中训练行为、再在真实机器人上运行，也体现了人工智能从数字环境走向物理世界的发展趋势。 该机器人配备 15 个电机、摄像头、激光雷达和可抓取物体的喙，并可开箱使用。现有信息尚未证明它在真实环境中的学习效果、采用情况，以及能够稳定完成的任务范围。

google_news · The Indian Express · 8月30日 03:50

**背景**: 具身人工智能是指通过机器人等实体感知并作用于物理世界的人工智能系统。强化学习让系统尝试不同动作，并根据反馈不断改进；仿真环境则可以在部署到硬件之前，以更安全、更低成本的方式进行训练。开源软件栈能够让更多人修改机器人软件并尝试不同的训练流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pollen-robotics.com/microduck/">Microduck - A tiny biped robot you can teach new tricks ...</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI ? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#Robotics`, `#Embodied AI`, `#Open Source`, `#Machine Learning`, `#Hugging Face`

---

<a id="item-33" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMinwFBVV95cUxQVUxqbS1MN3VodV9pWjdoMVBNTUJQVkg1TXBqMXl0M1dzVlNSUHlRX2kxaDBLQlhKV0FnUW9UTWZuMzFxd1hvRGpkN2V5UU5hWEcxdWs3QlBvQ2NMNGpKQWxhSk5jRlIteTFYUVlhV3NMa3RiWXVLT0VKRm9KLWRsNy1SN0pfZGFfcDlVaFRNQ0FVUnZVc3ZMdkVTTWpOLWvSAZ8BQVVfeXFMUFVMam0tTDd1aHVfaVo3aDFQTU1CUFZINU1wajF5dDNXc1ZTUlB5UV9pMWgwS0JYSldBZ1FvVE1mbjMxcXdYb0RqZDdleVFOYVhHMXVrN0JQb0NjTDRqSkFsYUpOY0ZSLXkxWFFZYVdzTGt0Yll1S09FSkZvSi1kbDctUjdKX2RhX3A5VWhUTUNBVVJ2VXN2THZFU01qTi1r?oc=5" data-hz-title="Code-as-World将视频转换为可执行的MuJoCo模拟" data-hz-tags="Embodied AI,World Models,Robotics Simulation,MuJoCo,Code Generation" data-hz-section="other"></a>
## [Code-as-World 将视频转换为可执行的 MuJoCo 模拟](https://news.google.com/rss/articles/CBMinwFBVV95cUxQVUxqbS1MN3VodV9pWjdoMVBNTUJQVkg1TXBqMXl0M1dzVlNSUHlRX2kxaDBLQlhKV0FnUW9UTWZuMzFxd1hvRGpkN2V5UU5hWEcxdWs3QlBvQ2NMNGpKQWxhSk5jRlIteTFYUVlhV3NMa3RiWXVLT0VKRm9KLWRsNy1SN0pfZGFfcDlVaFRNQ0FVUnZVc3ZMdkVTTWpOLWvSAZ8BQVVfeXFMUFVMam0tTDd1aHVfaVo3aDFQTU1CUFZINU1wajF5dDNXc1ZTUlB5UV9pMWgwS0JYSldBZ1FvVE1mbjMxcXdYb0RqZDdleVFOYVhHMXVrN0JQb0NjTDRqSkFsYUpOY0ZSLXkxWFFZYVdzTGt0Yll1S09FSkZvSi1kbDctUjdKX2RhX3A5VWhUTUNBVVJ2VXN2THZFU01qTi1r?oc=5) ⭐️ 7.0/10

MirroS 的 Code-as-World 利用智能体循环，将现实世界视频重写为可执行的 MuJoCo 物理程序。该系统会提出、执行、渲染、验证并反复改进世界假设，而不是仅依赖视觉语言模型的一次性预测。 这种方法可能为具身人工智能和机器人系统提供更加明确、受物理约束的世界表示，用于推理和模拟。通过生成可执行程序，它有望连接视觉观察与可控的机器人环境，但现有材料尚未证明其实际性能。 MuJoCo 是一个开源物理引擎，用于机器人学、生物力学、图形学等领域的快速、精确模拟。现有摘录介绍了智能体工作流程，但没有提供视频到程序转换的基准结果、定量精度指标或详细局限性。

google_news · MarkTechPost · 8月30日 01:35

**背景**: 世界模型是对实体及其交互如何随时间变化的表示，使人工智能系统能够推理可能的结果。MuJoCo 将物理场景表示为可执行的模拟，并由物体、接触、运动和其他物理参数共同控制。在 Code-as-World 中，这种表示是可以运行和检查的程序代码，而不只是视觉预测或潜在表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mirros.ai/report/code-as-world.pdf">Code as Worlds: Agentic Discovery of Executable World ...</a></li>
<li><a href="https://mujoco.org/">MuJoCo — Advanced Physics Simulation</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#World Models`, `#Robotics Simulation`, `#MuJoCo`, `#Code Generation`

---

<a id="item-34" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMigAFBVV95cUxNUjUxNnRhNWhZenNCU1BFOHRKOWVvZ3hrbnk4ajgzZlJLT3l2VjhBQklKQVRaZTZGU2xGajBDMGZsS0hmN3RsY1NMQ19qTkVDNmFQdm9PTjlnMHF3bU5UZDZTdDQzRFlWUWRkZkF5ak1GWjM3MEJMMHNBUVNpSGFvYw?oc=5" data-hz-title="Opener 开源 DECT NR+ 物联网技术" data-hz-tags="IoT,DECT NR+,Open Source,Wireless Communications,Embedded Systems" data-hz-section="other"></a>
## [Opener 开源 DECT NR+ 物联网技术](https://news.google.com/rss/articles/CBMigAFBVV95cUxNUjUxNnRhNWhZenNCU1BFOHRKOWVvZ3hrbnk4ajgzZlJLT3l2VjhBQklKQVRaZTZGU2xGajBDMGZsS0hmN3RsY1NMQ19qTkVDNmFQdm9PTjlnMHF3bU5UZDZTdDQzRFlWUWRkZkF5ak1GWjM3MEJMMHNBUVNpSGFvYw?oc=5) ⭐️ 7.0/10

Opener 已为物联网开源 DECT NR+ 技术，使开发和实验更加容易。现有报道没有说明开源内容具体包括哪些组件、采用何种许可证或是否提供参考硬件。 开放获取可能降低开发工业物联网、计量和智能电网无线系统的门槛。此举也可能促进人们试验一种面向大规模设备连接和工业低时延通信的非蜂窝第五代移动通信技术。 DECT NR+ 面向去中心化和自主组网，也支持网状网络部署，据报道单个网络可扩展到数百万台设备。不过，新闻内容过于简略，无法评估 Opener 实现的性能、互操作性、许可证条款或量产准备程度。

google_news · Open Source For You · 8月31日 08:28

**背景**: DECT NR+ 也称为 DECT-2020 NR，是欧洲电信标准协会为 DECT 频段制定的一种无线电标准。它面向物联网和工业应用，并被称为非蜂窝第五代移动通信技术，这意味着设备无需依赖传统移动网络运营商即可通信。其去中心化设计旨在支持计量、智能电网和工业自动化等应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DECT-2020">DECT-2020 - Wikipedia</a></li>
<li><a href="https://www.rfwireless-world.com/tutorials/dect-nr-tutorial">DECT NR+ Tutorial: Network Architecture, Protocol Stack ...</a></li>

</ul>
</details>

**标签**: `#IoT`, `#DECT NR+`, `#Open Source`, `#Wireless Communications`, `#Embedded Systems`

---

<a id="item-35" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/08/30/the-u-s-is-building-barriers-around-drones-and-robots-china-still-has-scale/" data-hz-title="美国限制无人机和机器人，竞争或转向海外" data-hz-tags="Robotics,Drones,U.S.-China Competition,Supply Chains,Technology Policy" data-hz-section="other"></a>
## [美国限制无人机和机器人，竞争或转向海外](https://techcrunch.com/2026/08/30/the-u-s-is-building-barriers-around-drones-and-robots-china-still-has-scale/) ⭐️ 6.0/10

美国正在收紧对外国制造无人机和机器人的限制。该分析认为，中国的制造规模可能会把全球竞争转移到其他市场，而不是让竞争消失。 这一发展表明，贸易和市场准入壁垒可能限制相关产品在美国的销售，却无法消除中国制造能力带来的竞争优势。因此，企业和政策制定者可能会在美国以外的市场面临更激烈的竞争。 现有材料没有说明具体法规、企业、产品型号或产量数据。其核心限制是，在一个市场限制外国制造设备，可能只会改变竞争发生的地点，而不会终结竞争。

rss · TechCrunch AI · 8月31日 02:34

**背景**: 无人机和机器人是依赖制造业与供应链的实体产品。制造规模可以帮助生产商大量制造设备，并在国际市场上展开竞争；而限制措施则可能影响哪些外国制造产品能够在美国销售或使用。

**标签**: `#Robotics`, `#Drones`, `#U.S.-China Competition`, `#Supply Chains`, `#Technology Policy`

---

<a id="item-36" class="hz-item-anchor" data-hz-url="https://github.com/THU-MAIC/OpenMAIC" data-hz-title="OpenMAIC 将多智能体人工智能课堂带到 GitHub" data-hz-tags="Multi-Agent Systems,AI Education,TypeScript,Interactive Learning,Open Source" data-hz-section="other"></a>
## [OpenMAIC 将多智能体人工智能课堂带到 GitHub](https://github.com/THU-MAIC/OpenMAIC) ⭐️ 6.0/10

清华大学的 THU-MAIC/OpenMAIC 在 GitHub 上获得关注，过去 24 小时新增 31 个星标和 1 个复刻。这个基于 TypeScript 的开源项目提供了一键生成的沉浸式课堂，由多个相互协作的人工智能智能体驱动。 OpenMAIC 展示了多智能体系统如何通过在共享课堂环境中协调不同的人工智能角色，让教育软件变得更加互动。它以开源形式提供，可能为开发者和教育工作者试验人工智能辅助学习体验提供一个实用起点。 该项目使用 TypeScript 编写，相关 OpenMAIC 介绍提到它支持互动幻灯片、测验、模拟，以及能够与学习者进行语音交流、绘图和讨论的人工智能教师。不过，现有证据仅显示其处于早期阶段，最近新增 31 个星标和 1 个复刻，且没有报告拉取请求或社区讨论。

ossinsight · THU-MAIC · 8月30日 10:24

**背景**: 多智能体系统是一种软件架构，其中多个能够自主运行的人工智能智能体彼此互动，而不是只依赖单一助手。在 OpenMAIC 中，这种方式被用于围绕某个主题或文档组织沉浸式课堂。项目介绍的课堂功能包括教学互动、测验、幻灯片和模拟活动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openmaic.io/">OpenMAIC — Open Multi-Agent Interactive Classroom</a></li>
<li><a href="https://open.maic.chat/home">OpenMAIC — Open Multi-Agent Interactive Classroom</a></li>

</ul>
</details>

**标签**: `#Multi-Agent Systems`, `#AI Education`, `#TypeScript`, `#Interactive Learning`, `#Open Source`

---

<a id="item-37" class="hz-item-anchor" data-hz-url="https://github.com/K-Dense-AI/scientific-agent-skills" data-hz-title="科学智能体技能扩展人工智能科研工作流" data-hz-tags="AI agents,scientific computing,machine learning,drug discovery,Python" data-hz-section="other"></a>
## [科学智能体技能扩展人工智能科研工作流](https://github.com/K-Dense-AI/scientific-agent-skills) ⭐️ 6.0/10

K-Dense-AI 的 Python 库 scientific-agent-skills 提供 161 个经过验证的技能，并可访问 100 多个科学数据库，用于构建人工智能辅助的科研工作流。该仓库在过去 24 小时内新增 11 个星标和 1 个复刻，并支持 Cursor、Claude Code、Codex、Pi、Antigravity 以及开放的 Agent Skills 标准。 该项目可能降低为人工智能智能体配置生物学、化学、医学和药物发现领域专业流程及数据访问能力的成本。它兼容跨平台的技能标准，也可能让科研能力更容易在不同智能体工具之间复用。 该库以可复用技能的形式分发，并可通过项目文档中的命令安装；底层的 Agent Skills 格式则将能力表示为可移植且可进行版本控制的文件。现有信息主要来自宣传性描述，而最近新增 11 个星标和 1 个复刻本身并不能证明其科学或技术影响力。

ossinsight · K-Dense-AI · 8月30日 10:24

**背景**: 人工智能智能体是能够结合模型、工具、指令和外部数据执行多步骤任务的软件系统。Agent Skill 是一种轻量且可复用的专业知识或工作流组件，用于扩展智能体的能力。开放标准旨在让兼容的智能体在不同开发环境中发现并使用这些技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://cursor.com/docs/skills">Agent Skills | Cursor Docs</a></li>
<li><a href="https://github.com/K-Dense-AI/scientific-agent-skills">GitHub - K - Dense - AI / scientific - agent - skills : Turn any AI agent into...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#scientific computing`, `#machine learning`, `#drug discovery`, `#Python`

---

<a id="item-38" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiVEFVX3lxTE5YaGZiM0tkN2YtME15YTFiZndRRmF1elI4bzlmcEREZy1vVDE4NmpEbi1SUS1rWGdqaUt5Yk9tSFVRNkg0cWd3OW1kZ0pJT0cwQVRrSg?oc=5" data-hz-title="OpenShot 4.0 将视频编辑器界面迁移至 Qt6" data-hz-tags="OpenShot,Qt6,Open Source,Video Editing,Desktop Applications" data-hz-section="other"></a>
## [OpenShot 4.0 将视频编辑器界面迁移至 Qt6](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5YaGZiM0tkN2YtME15YTFiZndRRmF1elI4bzlmcEREZy1vVDE4NmpEbi1SUS1rWGdqaUt5Yk9tSFVRNkg0cWd3OW1kZ0pJT0cwQVRrSg?oc=5) ⭐️ 6.0/10

OpenShot 4.0 已作为这款开源非线性视频编辑器的重大更新发布。此次版本的核心变化是将用户界面适配到 Qt6。 此次迁移使 OpenShot 的桌面应用基础得到现代化，并与 Qt 框架当前的发展方向保持一致。这可能有助于项目在受支持的桌面平台上维护和持续改进其界面。 Qt6 迁移不仅是外观 redesign，而是一次重要的框架转换，因此兼容性和迁移工作是项目需要关注的事项。目前公开的公告没有提供太多实现细节，也没有说明可量化的性能变化。

google_news · Phoronix · 8月30日 19:55

**背景**: OpenShot 是一款开源非线性视频编辑应用，这意味着用户可以在时间线上安排和编辑视频、音频片段，而不必只能按顺序处理素材。Qt6 是用于构建桌面软件的跨平台应用和用户界面框架。将应用界面从较早的 Qt 版本迁移到 Qt6，通常需要进行大量代码和兼容性更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/OpenShot-4.0">OpenShot 4.0 Released In Adapting Video Editor UI To Qt6</a></li>
<li><a href="https://en.ubunlog.com/qt-6-2-has-already-been-released-and-these-are-its-news/">Qt 6 .2 has already been released and these are its news</a></li>

</ul>
</details>

**标签**: `#OpenShot`, `#Qt6`, `#Open Source`, `#Video Editing`, `#Desktop Applications`

---

<a id="item-39" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiiwFBVV95cUxQWVRnZjQ1bkhqS2t2MlBWT3ctdHNWMWZoMnhVb1VPTklHU3p0aG1TQ0E1WWNGTnpVV2Q4U0N4XzNzc1k3b21Hd0FxYktWRlBPbmwxY0lvVWlKYjRQNFB6dVl2MkRJYUwyVWtteWN0RGN1aklUa1p3NWZKODhCbGJlazItWVNaS3Q3V3dn?oc=5" data-hz-title="Roblox向ROOST模型社区开放安全模型" data-hz-tags="AI safety,Open source,Content moderation,Machine learning,Online platforms" data-hz-section="other"></a>
## [Roblox 向 ROOST 模型社区开放安全模型](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQWVRnZjQ1bkhqS2t2MlBWT3ctdHNWMWZoMnhVb1VPTklHU3p0aG1TQ0E1WWNGTnpVV2Q4U0N4XzNzc1k3b21Hd0FxYktWRlBPbmwxY0lvVWlKYjRQNFB6dVl2MkRJYUwyVWtteWN0RGN1aklUa1p3NWZKODhCbGJlazItWVNaS3Q3V3dn?oc=5) ⭐️ 6.0/10

2026 年 8 月 19 日，Roblox 宣布向稳健开放在线安全工具（ROOST）模型社区贡献三个开源安全模型。此次贡献包括其个人身份信息分类器和 Roblox Sentinel 的更新版、最新的语音安全分类器，以及一个可供其他公司评测自身分类器的新数据集。 公开生产级安全模型和评测资源，可能减少信任与安全团队在构建内容审核及在线风险缓解系统时的重复工作。这也可能让规模较小的平台和开发者获得可检查的起点，同时由各个平台自行决定治理方式和政策。 这些模型将通过 ROOST 模型社区分发，该社区旨在让不同组织能够部署开放且可检查的安全模型。公告没有详细说明模型架构、训练数据、许可证、实测性能或部署限制，因此不应将这些贡献视为经过普遍验证的内容审核解决方案。

google_news · Roblox · 8月30日 15:54

**背景**: ROOST 即稳健开放在线安全工具，是一个专注于在线安全的开源工具计划。其模型社区汇集开发者、实践者和模型创建者，旨在提高安全模型的可获得性。开放且可检查的模型可以帮助组织开发审核系统，但每个平台仍需建立自己的治理机制、政策和运营保障措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://about.roblox.com/newsroom/2026/08/roblox-open-source-safety-models-roost">Roblox Brings Open-Source Safety Models to ROOST Model Community</a></li>
<li><a href="https://roost.tools/">Robust Open Online Safety Tools</a></li>
<li><a href="https://github.com/roostorg/model-community">GitHub - roostorg/model-community: Making open safety AI ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#Open source`, `#Content moderation`, `#Machine learning`, `#Online platforms`

---

<a id="item-40" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMibEFVX3lxTE1ZLXgxWHFEand4NkJHM2QyTy0wbGs5X1Ezc0cwSThEZi1RVUQ4b2xvb2VmcmlQOThESmo5UTVyLWk5SFA0b3UwZXgtejdmSzV2R0VtNVVzNFRtUmlsaWtyTFRJS3pOUlVndVdkcdIBckFVX3lxTE80WUFlRWc2em9aWl9WNzQtc3V5cmExNGx0TnhZM2NYNW5jN2lJclh5RzVlZ2pWdHdWMU96OG1wZHE2ZWtWcHFhZGFhLVg4SHplamhSZkRvdHMxZVBJVGUyVGtQWFdfWC00QjdJbC1ERU9qQQ?oc=5" data-hz-title="黑客遭恶意软件感染，攻击基础设施遭曝光" data-hz-tags="Cybersecurity,Malware Analysis,Threat Intelligence,RATs,Phishing" data-hz-section="other"></a>
## [黑客遭恶意软件感染，攻击基础设施遭曝光](https://news.google.com/rss/articles/CBMibEFVX3lxTE1ZLXgxWHFEand4NkJHM2QyTy0wbGs5X1Ezc0cwSThEZi1RVUQ4b2xvb2VmcmlQOThESmo5UTVyLWk5SFA0b3UwZXgtejdmSzV2R0VtNVVzNFRtUmlsaWtyTFRJS3pOUlVndVdkcdIBckFVX3lxTE80WUFlRWc2em9aWl9WNzQtc3V5cmExNGx0TnhZM2NYNW5jN2lJclh5RzVlZ2pWdHdWMU96OG1wZHE2ZWtWcHFhZGFhLVg4SHplamhSZkRvdHMxZVBJVGUyVGtQWFdfWC00QjdJbC1ERU9qQQ?oc=5) ⭐️ 6.0/10

据报道，一次影响黑客的恶意软件感染事件暴露了他们使用的远程访问木马、钓鱼工具包和攻击基础设施。现有报道没有提供具体的恶意软件名称、受影响团伙或技术细节。 这一事件可能通过暴露攻击者通常使用的工具和基础设施，为威胁情报分析提供有价值的线索。它也说明恶意软件运营者的系统遭到入侵后，攻击活动本身可能反过来暴露攻击者。 远程访问木马是一类能够让攻击者远程控制受感染设备的恶意软件，而钓鱼工具包通常用于开展窃取凭据的攻击活动。由于提供的内容只有标题，目前无法独立评估此次暴露的范围及其安全影响。

google_news · CyberSecurityNews · 8月31日 05:23

**背景**: 远程访问木马，也称为 RAT，是一种能够让攻击者未经授权远程访问受害者计算机的恶意软件。钓鱼工具包是一组帮助攻击者创建和运行钓鱼活动的工具，通常用于窃取凭据或其他敏感信息。攻击基础设施是指用于投递恶意软件、收集数据或管理受感染设备的服务器、域名及相关系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fortinet.com/resources/cyberglossary/remote-access-trojan">fortinet.com/resources/cyberglossary/ remote - access - trojan</a></li>
<li><a href="https://socradar.io/blog/top-phishing-kits-cybercriminals/">Top 10 Phishing Kits Used by Cybercriminals</a></li>

</ul>
</details>

**标签**: `#Cybersecurity`, `#Malware Analysis`, `#Threat Intelligence`, `#RATs`, `#Phishing`

---

<a id="item-41" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMinAFBVV95cUxPcmUwUTlmeXYzOU51VlJKbWFFMWdRRllBWFM5QXk3RFZUV0RCVm4wNHk3c3ZZVFp6UlJtd2FxS3VLMHpMMl82bm12NW9rR0xkLTVKWlA5NHFLT3U3R2NfZjBiVm5YVGFCc0V0bFVZeVlkb2wtMmphYnQ0MVkwUFh4dzZIM1RVY00tWFVPMEliQmhjclJmTVdVTVlBYjY?oc=5" data-hz-title="Sanctuary AI将单独出售机器人“大脑”" data-hz-tags="Embodied AI,Humanoid Robots,Robotics Software,AI Commercialization" data-hz-section="other"></a>
## [Sanctuary AI 将单独出售机器人“大脑”](https://news.google.com/rss/articles/CBMinAFBVV95cUxPcmUwUTlmeXYzOU51VlJKbWFFMWdRRllBWFM5QXk3RFZUV0RCVm4wNHk3c3ZZVFp6UlJtd2FxS3VLMHpMMl82bm12NW9rR0xkLTVKWlA5NHFLT3U3R2NfZjBiVm5YVGFCc0V0bFVZeVlkb2wtMmphYnQ0MVkwUFh4dzZIM1RVY00tWFVPMEliQmhjclJmTVdVTVlBYjY?oc=5) ⭐️ 6.0/10

Sanctuary AI 计划将其人形机器人软件和控制系统作为独立产品商业化，而不再只销售完整的 Phoenix 机器人。该策略可能让其他硬件平台也使用这家公司的机器人控制技术。 出售控制系统可能推动 Sanctuary AI 转向软件与平台业务模式，并扩大其具身智能技术的市场。此举也可能加快人形机器人硬件与负责感知、学习和执行物理任务的软件之间的分离。 现有信息没有说明定价、许可条款、兼容机器人、客户承诺或外部采用证据。Sanctuary AI 的 Phoenix 平台使用 Carbon 人工智能控制系统，近期版本同时改进了硬件和软件，但这项公告没有提供独立产品发布的具体技术细节。

google_news · Startup Fortune · 8月29日 23:31

**背景**: Phoenix 是 Sanctuary AI 的通用型人形机器人平台，Carbon 则是用于控制该平台运行的人工智能系统。具身智能是指通过机器人等系统在现实物理世界中采取行动的人工智能，而不仅是在软件中生成输出。将控制系统与 Phoenix 分离，理论上可能让软件部署到不同的机器人机体上，但现有资料没有确认这种互操作性已经实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.therobotreport.com/sanctuary-ai-latest-phoenix-humanoid-can-learn-tasks-in-24-hours/">Sanctuary AI 's latest Phoenix humanoid can... - The Robot Report</a></li>
<li><a href="https://chozan.co/embodied-ai/">Embodied AI : Why Humanoid Robots Are Moving AI Into... - ChoZan</a></li>

</ul>
</details>

**标签**: `#Embodied AI`, `#Humanoid Robots`, `#Robotics Software`, `#AI Commercialization`

---

<a id="item-42" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMid0FVX3lxTE04U1JMSV9BTlJLd3BuaGd5STNaYlhsMWp4M0syOVNINWc1ak5lRC14bllXV1VLNG1UUXdFbW5QRDYwS0pKcEpNcG9ERElZdnFJQktEWHlITEYzSHNqMGxFSFUxYXJTeC1xTlJDTk1TUUxWNWNvRG5v?oc=5" data-hz-title="《The Sequence》综述人工智能不断扩大的工业作用" data-hz-tags="Artificial Intelligence,Industrial AI,AI Industry Trends,Technology News" data-hz-section="other"></a>
## [《The Sequence》综述人工智能不断扩大的工业作用](https://news.google.com/rss/articles/CBMid0FVX3lxTE04U1JMSV9BTlJLd3BuaGd5STNaYlhsMWp4M0syOVNINWc1ak5lRC14bllXV1VLNG1UUXdFbW5QRDYwS0pKcEpNcG9ERElZdnFJQktEWHlITEYzSHNqMGxFSFUxYXJTeC1xTlJDTk1TUUxWNWNvRG5v?oc=5) ⭐️ 6.0/10

《The Sequence》第 923 期《Radar》回顾了过去一周的重要人工智能进展，重点关注人工智能在工业应用中的不断扩展。现有信息没有列出其中涉及的具体进展。 这篇综述凸显了一个更广泛的转变：人们讨论人工智能时，正从通用技术本身逐渐转向其在工业场景中的实际应用。它的具体意义取决于完整期刊中所收录的应用和进展。 该条目由《The Sequence》和 Jesus Rodriguez 以周度综述形式发布，但现有内容没有提供技术规格、公司名称、部署数据或讨论数据。因此，读者需要查看完整期刊，才能评估其中各项进展及其依据。

google_news · TheSequence | Jesus Rodriguez · 8月30日 11:03

**背景**: 这里的人工智能指的是被应用于研究或面向消费者的使用场景之外的技术和系统。工业应用是指人工智能在工业环境中的使用，因此“工业化转向”表示人们日益重视这些实际应用。

**标签**: `#Artificial Intelligence`, `#Industrial AI`, `#AI Industry Trends`, `#Technology News`

---

<a id="item-43" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/08/30/musks-faster-path-to-more-gas-turbines-comes-with-pollution-problem/" data-hz-title="马斯克加速燃气轮机计划引发污染担忧" data-hz-tags="Energy Infrastructure,Gas Turbines,Environmental Impact,SpaceX,Public Health" data-hz-section="other"></a>
## [马斯克加速燃气轮机计划引发污染担忧](https://techcrunch.com/2026/08/30/musks-faster-path-to-more-gas-turbines-comes-with-pollution-problem/) ⭐️ 5.0/10

埃隆·马斯克表示，SpaceX 一座保密铸造厂可以自行铸造燃气轮机叶片，并将燃气发电上线时间比其他项目提前 18 个月。该策略可能加快轮机部署，但也会加剧对正面临诉讼和公共卫生审查的燃料来源的依赖。 更快部署燃气发电可能帮助高能耗设施获得电力，但新增轮机也可能加剧本已面临空气质量问题社区的污染和健康风险。该计划凸显了快速扩大电力供应与减少化石燃料基础设施污染之间的更广泛矛盾。 该方案的核心是在内部制造轮机叶片，可能采用先进铸造方法；单晶叶片旨在承受高温，同时减少蠕变变形和氧化。可是，现有信息尚未说明该铸造厂的产能、排放控制措施，也未独立验证其所谓的 18 个月优势。

rss · TechCrunch AI · 8月30日 16:54

**背景**: 燃气轮机通过燃烧天然气产生高温膨胀气体，再推动轮机叶片发电。轮机叶片承受极高的热和机械应力，因此制造商可能采用单晶铸造来提高抗蠕变和抗氧化能力。燃气轮机设施会排放空气污染物，从而引发公共卫生担忧；所引研究称，影响范围还可能延伸到数英里之外的居民。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.newayaerotech.com/study-cases/cmsx-alloy-single-crystal-casting-industrial-gas-turbines-blades">CMSX Alloy Single Crystal Casting Industrial Gas Turbines Blades</a></li>
<li><a href="https://www.pecva.org/work/energy-work/data-centers/new-study-highlights-public-health-impacts-of-gas-turbine-powered-data-centers/">New Study Highlights Public Health Impacts of Gas Turbine ...</a></li>

</ul>
</details>

**标签**: `#Energy Infrastructure`, `#Gas Turbines`, `#Environmental Impact`, `#SpaceX`, `#Public Health`

---

<a id="item-44" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/08/30/caterpillar-is-bringing-to-ai-deployment-what-it-learned-from-automating-mining/" data-hz-title="卡特彼勒将采矿自动化经验用于人工智能部署" data-hz-tags="industrial AI,autonomous systems,mining automation,AI deployment" data-hz-section="other"></a>
## [卡特彼勒将采矿自动化经验用于人工智能部署](https://techcrunch.com/2026/08/30/caterpillar-is-bringing-to-ai-deployment-what-it-learned-from-automating-mining/) ⭐️ 5.0/10

卡特彼勒正将数十年来在偏远采矿地点部署自主机器的经验应用于人工智能部署。其采矿自动化工作包括远程控制设备、自动化流程以及自主运输车队。 在偏远且高风险的环境中运行自主设备，可以为如何在受控条件之外可靠部署人工智能提供实际经验。这可能影响工业企业将人工智能与现有机械、通信网络及运营流程整合的方式。 卡特彼勒的矿山之星解决方案可以自动化单个采矿流程、远程控制一台机器、协调不同类型的设备，或让自主运输卡车在没有人工干预的情况下运行。目前提供的信息没有说明该公司正在采矿业之外应用哪些人工智能系统、部署方法或性能成果。

rss · TechCrunch AI · 8月30日 15:00

**背景**: 采矿自动化利用软件、传感器、通信设备和机器控制系统，执行原本需要人员持续操作的任务。自主运输系统可以让卡车在司机有限控制或完全没有直接控制的情况下导航并运输物料。卡特彼勒表示，其技术支持从单个流程自动化到整支自主车队运行的不同层级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cat.com/en_US/by-industry/mining/autonomy-leadership.html">Autonomy & Automation | Cat | Caterpillar</a></li>
<li><a href="https://www.cat.com/en_US/by-industry/mining/minestar-solutions/automation.html">Automation Solutions | Cat | Caterpillar</a></li>

</ul>
</details>

**标签**: `#industrial AI`, `#autonomous systems`, `#mining automation`, `#AI deployment`

---

