# Horizon Daily - 2026-08-31

> From 112 items, 44 important content pieces were selected

---

## Preference Radar

> Personalized picks from your maintained preference profile (data/preference-radar/profile.json).

No preference-matched updates today.

---
## HUST Research Directions

> Research highlights matched to public faculty directions at HUST's School of Artificial Intelligence and Automation.

1. [Adaptive Voltage Coordination Improves VSG Inverter Transient Stability](#item-1) ⭐️ 7.0/10
2. [More Accurate Sensorless SPMSM Control with Switching-Frequency Injection](#item-2) ⭐️ 7.0/10
3. [Sampling Delays Drive High-Frequency Inverter Non-Passivity](#item-3) ⭐️ 7.0/10
4. [Models and Algorithms for Mitigating Worst-Case Infrastructure Disruptions](#item-4) ⭐️ 7.0/10
5. [STO-CAST Brings Real-Time Power-Outage Forecasting to Tropical Cyclones](#item-5) ⭐️ 7.0/10
6. [Probabilistic Scheduling Coordinates Electric Vehicles and Grid Loads](#item-6) ⭐️ 7.0/10
7. [Probabilistic EV Scheduling Balances Fleet Efficiency and Grid Load](#item-7) ⭐️ 7.0/10
8. [Review of SOFC System Control Objectives and Challenges](#item-8) ⭐️ 6.0/10
9. [Optimizing Bus Networks with Shared BRT Lanes](#item-9) ⭐️ 6.0/10
10. [Probability-Based Matching Improves Stochastic EV Scheduling](#item-10) ⭐️ 6.0/10
11. [Cascaded Cost Functions Improve PMSM Predictive Control](#item-11) ⭐️ 5.0/10
12. [Improved Sensorless PMSM Control with ADRC and Adaptive Harmonic Filters](#item-12) ⭐️ 5.0/10
13. [Hierarchical Matching for Vehicle Scheduling](#item-13) ⭐️ 5.0/10
14. [Integrated Bus Network and Timetable Design for Multimodal Transit](#item-14) ⭐️ 5.0/10

---
<a id="item-1" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560379" data-hz-title="Adaptive Voltage Coordination Improves VSG Inverter Transient Stability" data-hz-tags="Grid-forming inverters,Virtual synchronous generators,Transient stability,Power systems control,Renewable energy integration" data-hz-section="hust-research"></a>
## [Adaptive Voltage Coordination Improves VSG Inverter Transient Stability](https://doi.org/10.1109/ccdc69976.2026.11560379) ⭐️ 7.0/10

The paper proposes adaptively coordinating fast and slow internal voltage sources in virtual synchronous generator (VSG)-controlled grid-forming inverters. The controller switches or coordinates their dynamics according to system needs to improve transient stability during disturbances. Grid-forming inverters must maintain voltage, frequency, and synchronism as renewable generation replaces conventional synchronous machines. Improving their transient stability could support more reliable integration of photovoltaic, wind, and energy-storage resources, although the practical impact depends on the paper's validation results. The central technical feature is the adaptive use of two internal-voltage-source dynamics rather than relying on a single fixed response speed. The available information does not specify the switching criteria, controller parameters, or experimental and simulation performance improvements, so those aspects should be verified in the full paper.

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · May 15, 00:00

**Match**: Paper keyword **grid-forming** matched under **能源电子与智能制造**.

**Related faculty**: 俞耀文, 刘智伟, 刘骁康, 卢仁智, 叶杰, 唐其鹏, 尹泉, 彭刚 and 13 more

**Background**: A virtual synchronous generator is a control strategy that makes an inverter emulate characteristics of a conventional synchronous generator, including inertia, damping, and droop behavior. A grid-forming inverter regulates its internal voltage and angle to establish or support grid voltage and frequency, rather than merely tracking an externally imposed waveform. During faults or other disturbances, the inverter's control dynamics and current limits can strongly affect whether it remains synchronized and stable.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/topics/engineering/virtual-synchronous-generator">Virtual Synchronous Generator - an overview | ScienceDirect Topics</a></li>
<li><a href="https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2023.1331024/full">Frontiers | Improved VSG strategy of grid-forming inverters for supporting inertia and damping</a></li>
<li><a href="https://www.researchgate.net/publication/376378718_Exploring_Damping_Effect_of_Inner_Control_Loops_for_Grid-Forming_VSCs">(PDF) Exploring Damping Effect of Inner Control Loops for...</a></li>

</ul>
</details>

**Tags**: `#Grid-forming inverters`, `#Virtual synchronous generators`, `#Transient stability`, `#Power systems control`, `#Renewable energy integration`

---

<a id="item-2" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/tpel.2026.3678851" data-hz-title="More Accurate Sensorless SPMSM Control with Switching-Frequency Injection" data-hz-tags="Sensorless Motor Control,PMSM,Model Predictive Control,Power Electronics,Electric Motor Drives" data-hz-section="hust-research"></a>
## [More Accurate Sensorless SPMSM Control with Switching-Frequency Injection](https://doi.org/10.1109/tpel.2026.3678851) ⭐️ 7.0/10

The paper introduces an experimentally validated sensorless control strategy for surface-mounted permanent-magnet synchronous motors that combines switching-frequency injection with finite-control-set deadbeat predictive current control. It uses an angular-domain iterative optimization method with an extended control set, injection-time compensation, and a simple initial-position detection method to improve injection accuracy and reduce execution time. In finite-control-set predictive control, inaccurate voltage injection can distort the position-error signal and weaken sensorless operation. By improving injection precision while reducing computational execution time, the method could support more practical sensorless motor drives, particularly where eliminating a position sensor and maintaining current-control performance are important. The strategy is based on a d-axis current offset and is implemented on an SPMSM; the paper also analyzes speed oscillation caused by the current offset. The authors report that inherent finite-control-set injection errors can degrade current control and that conventional compensation may require substantially more execution time, while the proposed injection-time method addresses this trade-off experimentally.

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · Mar 31, 00:00

**Match**: Paper keyword **PMSM** matched under **能源电子与智能制造**.

**Related faculty**: 俞耀文, 刘智伟, 刘骁康, 卢仁智, 叶杰, 唐其鹏, 尹泉, 彭刚 and 13 more

**Background**: Switching-frequency injection is a sensorless technique that applies a high-frequency voltage or switching-related signal and observes the resulting current response to infer rotor position. An SPMSM is a surface-mounted permanent-magnet synchronous motor, whose rotor position is normally measured with a sensor but can instead be estimated from electrical signals. Finite-control-set model predictive control selects among available inverter switching states, while deadbeat predictive current control aims to drive the current toward its reference within a short prediction interval.

<details><summary>References</summary>
<ul>
<li><a href="https://ieeexplore.ieee.org/document/11458794">Novel Switching Frequency Injection Sensorless Control for ...</a></li>
<li><a href="https://ieeexplore.ieee.org/document/10108031">Sensorless Control With Switching Frequency Square Wave ...</a></li>

</ul>
</details>

**Tags**: `#Sensorless Motor Control`, `#PMSM`, `#Model Predictive Control`, `#Power Electronics`, `#Electric Motor Drives`

---

<a id="item-3" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/apec51134.2026.11516799" data-hz-title="Sampling Delays Drive High-Frequency Inverter Non-Passivity" data-hz-tags="power electronics,grid-connected inverters,passivity-based control,control delays,power-system stability" data-hz-section="hust-research"></a>
## [Sampling Delays Drive High-Frequency Inverter Non-Passivity](https://doi.org/10.1109/apec51134.2026.11516799) ⭐️ 7.0/10

The paper quantifies how sampling-period and sampling-instant delays shape the depth and bandwidth of negative damping in grid-following inverter admittance above the Nyquist frequency. It also proposes a frequency-aliasing-aware passivity-based damping method, with experiments confirming improved high-frequency stability. The results show that increasing the sampling frequency can reduce, but does not eliminate, high-frequency non-passivity, identifying a persistent source of instability in grid-connected power converters. The proposed mitigation could help engineers assess and improve stability when inverter controls interact with grid resonances, especially in weak-grid applications. The analysis distinguishes absolute delay from relative delay and examines their separate effects on the negative-damping region. Because the issue involves admittance behavior above the sampling system’s Nyquist limit, conventional below-Nyquist intuition is insufficient; the proposed damping design explicitly accounts for frequency aliasing and was experimentally validated.

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · Mar 22, 00:00

**Match**: Paper keyword **grid-following** matched under **能源电子与智能制造**.

**Related faculty**: 俞耀文, 刘智伟, 刘骁康, 卢仁智, 叶杰, 唐其鹏, 尹泉, 彭刚 and 13 more

**Background**: A grid-following inverter uses the existing grid voltage and frequency as references while its control system regulates injected current and power. Its output admittance describes how the inverter’s current response changes with applied voltage disturbances, making it useful for impedance- or admittance-based stability assessment. The Nyquist frequency is half the sampling rate; frequency components above it can be represented through aliasing in a sampled control system. Passivity-based assessment examines whether the inverter behaves as a net energy-absorbing element rather than contributing negative damping that can amplify grid oscillations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mdpi.com/1996-1073/16/16/5894">Small-Signal Modeling and Stability Analysis of a Grid-Following Inverter with Inertia Emulation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nyquist_frequency">Nyquist frequency - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/314202717_VSC_Input-Admittance_Modeling_and_Analysis_Above_the_Nyquist_Frequency_for_Passivity-Based_Stability_Assessment">VSC Input-Admittance Modeling and Analysis Above the Nyquist Frequency for Passivity-Based Stability Assessment | Request PDF</a></li>

</ul>
</details>

**Tags**: `#power electronics`, `#grid-connected inverters`, `#passivity-based control`, `#control delays`, `#power-system stability`

---

<a id="item-4" class="hz-item-anchor" data-hz-url="https://doi.org/10.1016/j.ress.2026.113133" data-hz-title="Models and Algorithms for Mitigating Worst-Case Infrastructure Disruptions" data-hz-tags="Critical Infrastructure,Reliability Engineering,Resilience,Optimization,Systems Research" data-hz-section="hust-research"></a>
## [Models and Algorithms for Mitigating Worst-Case Infrastructure Disruptions](https://doi.org/10.1016/j.ress.2026.113133) ⭐️ 7.0/10

The paper examines models and algorithms for identifying and mitigating worst-case disruptions in critical infrastructure systems. Its focus is on finding failures or attacks that cause the greatest decline in system performance and informing defensive responses. Critical infrastructure disruptions can affect the reliability and continuity of essential services, so identifying the most damaging components can help operators prioritize protection and mitigation resources. The work contributes to a broader reliability and resilience research area that uses optimization to support infrastructure planning and recovery. Related approaches formulate worst-case disruption as an interdiction or bilevel optimization problem, in which an adversarial disruption is evaluated against defensive decisions such as fortification. These problems can be computationally difficult, making algorithm design important for applying the models to larger infrastructure networks.

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · Jul 10, 00:00

**Match**: Paper keyword **critical infrastructure** matched under **系统工程与决策优化**.

**Related faculty**: 余明晖, 俞耀文, 刘振元, 刘智伟, 刘磊, 刘骁康, 卢仁智, 叶林涛 and 17 more

**Background**: Critical infrastructure systems provide essential services and may contain components whose failure has a disproportionate effect on overall performance. Worst-case disruption analysis searches for the failure or attack scenario with the most severe system impact. Mitigation models then help determine which components or defensive measures should receive priority.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0951832026009427">Identifying and mitigating worst-case disruptions in critical ...</a></li>
<li><a href="https://roadef2026.sciencesconf.org/687427/document">Identifying Critical Infrastructure : A Bilevel Genetic Algorithm</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0951832024007889">Enhancing critical network infrastructure resilience through optimal post-disruption maintenance and routing decisions - ScienceDirect</a></li>

</ul>
</details>

**Tags**: `#Critical Infrastructure`, `#Reliability Engineering`, `#Resilience`, `#Optimization`, `#Systems Research`

---

<a id="item-5" class="hz-item-anchor" data-hz-url="https://doi.org/10.1111/risa.70275" data-hz-title="STO-CAST Brings Real-Time Power-Outage Forecasting to Tropical Cyclones" data-hz-tags="Deep Learning,Spatiotemporal Forecasting,Power Systems,Disaster Response,Climate Risk" data-hz-section="hust-research"></a>
## [STO-CAST Brings Real-Time Power-Outage Forecasting to Tropical Cyclones](https://doi.org/10.1111/risa.70275) ⭐️ 7.0/10

Researchers introduced STO-CAST, a spatiotemporal deep learning model that continuously updates hourly power-outage forecasts during tropical cyclones using changing meteorological projections and newly observed outages. It forecasts at 4 km by 4 km resolution with a 6-hour nowcasting horizon and a 60-hour planning horizon, and was evaluated on Typhoon Muifa in 2022 using a Leave-One-Storm-Out framework. Unlike open-loop or event-level models, STO-CAST can adapt forecasts as storm conditions and grid states evolve, helping utilities improve both emergency situational awareness and advance resource staging. More timely, localized predictions could support risk-informed response and strengthen power-system resilience during severe tropical cyclones. The model combines static environmental and infrastructure attributes with dynamic meteorological and outage sequences, and its error decomposition separates the effects of model limitations, meteorological uncertainty, and observation gaps. The evidence comes from a case study of Typhoon Muifa, so broader performance across storms, regions, and grid conditions remains to be established.

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · May 26, 00:00

**Match**: Paper keyword **tropical cyclone** matched under **系统工程与决策优化**.

**Related faculty**: 余明晖, 俞耀文, 刘振元, 刘智伟, 刘磊, 刘骁康, 卢仁智, 叶林涛 and 17 more

**Background**: Spatiotemporal forecasting models learn patterns that vary across both location and time, which is useful when outages develop across a geographically distributed power system as a storm moves. Nowcasting refers here to short-lead forecasting that incorporates current observations, while the longer-horizon mode uses forecasts to support advance planning. Leave-One-Storm-Out evaluation tests a model on a storm that was excluded from the training examples, providing an assessment of generalization to an unseen event.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.06644">[2512.06644] From Forecast to Action: A Deep Learning Model for Predicting Power Outages During Tropical Cyclones</a></li>
<li><a href="https://arxiv.org/pdf/2512.06644">From Forecast to Action: A Deep Learning Model for Predicting ...</a></li>

</ul>
</details>

**Tags**: `#Deep Learning`, `#Spatiotemporal Forecasting`, `#Power Systems`, `#Disaster Response`, `#Climate Risk`

---

<a id="item-6" class="hz-item-anchor" data-hz-url="https://doi.org/10.6084/m9.figshare.31910706" data-hz-title="Probabilistic Scheduling Coordinates Electric Vehicles and Grid Loads" data-hz-tags="Electric Vehicles,Optimization,Smart Grids,Stochastic Scheduling,Transportation Systems" data-hz-section="hust-research"></a>
## [Probabilistic Scheduling Coordinates Electric Vehicles and Grid Loads](https://doi.org/10.6084/m9.figshare.31910706) ⭐️ 7.0/10

The study proposes a probability-based hierarchical matching (P-HM) method for stochastic electric-vehicle scheduling that jointly considers uncertain trip times and power-grid load constraints. It partitions timetables into tiers, matches adjacent tiers using compatibility probabilities, and applies greedy local search to reduce peak-load violations. By optimizing fleet size, operating cost, charging peak load, and on-time performance together, the approach addresses the interdependence between transport reliability and grid security. The reported gains could help public-transport operators reduce fleet requirements while making electric-bus charging more compatible with constrained power networks. The model is designed to improve robustness under stochastic travel times and to mitigate charging peaks through a greedy local-search step, with particularly strong results in fleet-size reduction against benchmark methods. However, the available report provides numerical comparisons without independent validation or evidence of deployment in a real transport network.

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · Apr 1, 00:00

**Match**: Paper keyword **vehicle scheduling** matched under **系统工程与决策优化**.

**Related faculty**: 余明晖, 俞耀文, 刘振元, 刘智伟, 刘磊, 刘骁康, 卢仁智, 叶林涛 and 17 more

**Background**: The stochastic electric-vehicle scheduling problem involves assigning electric vehicles to timetable trips when travel times and resulting charging needs are uncertain. These uncertainties can shift charging demand into peak periods, potentially worsening grid loading and reducing schedule reliability. P-HM addresses this by matching timetable tiers according to the probability that adjacent trips are operationally compatible, while its local-search component repairs or improves solutions that violate peak-load limits.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/0305215X.2026.2643627">Probability-based hierarchical matching approach for ...</a></li>
<li><a href="https://tandf.figshare.com/articles/dataset/Probability-based_hierarchical_matching_approach_for_stochastic_electric_vehicle_scheduling_considering_power_grid_load/31910706">Item - Probability-based hierarchical matching approach for ...</a></li>

</ul>
</details>

**Tags**: `#Electric Vehicles`, `#Optimization`, `#Smart Grids`, `#Stochastic Scheduling`, `#Transportation Systems`

---

<a id="item-7" class="hz-item-anchor" data-hz-url="https://doi.org/10.6084/m9.figshare.31910706.v1" data-hz-title="Probabilistic EV Scheduling Balances Fleet Efficiency and Grid Load" data-hz-tags="Electric vehicle scheduling,Power grid optimization,Stochastic optimization,Operations research,Transportation systems" data-hz-section="hust-research"></a>
## [Probabilistic EV Scheduling Balances Fleet Efficiency and Grid Load](https://doi.org/10.6084/m9.figshare.31910706.v1) ⭐️ 7.0/10

The article proposes a probability-based hierarchical matching (P-HM) method for stochastic electric-vehicle scheduling that accounts for uncertain trip times and power-grid load constraints. Its model jointly minimizes fleet size, operating cost, and charging peak load while maximizing on-time performance. Stochastic trip times can shift charging demand and make both transit schedules and electricity loads less predictable, so treating transportation and grid constraints together could improve operational robustness. The approach may help public-transport operators reduce fleet requirements while supporting safer grid-load management as electric-vehicle adoption grows. P-HM partitions the timetable into tiers and matches adjacent tiers according to compatibility probabilities, while a greedy local search addresses peak-load violations. The reported numerical experiments show particularly strong fleet-size improvements over benchmark methods, but the available description does not provide detailed validation across broader real-world settings.

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · Apr 1, 00:00

**Match**: Paper keyword **vehicle scheduling** matched under **系统工程与决策优化**.

**Related faculty**: 余明晖, 俞耀文, 刘振元, 刘智伟, 刘磊, 刘骁康, 卢仁智, 叶林涛 and 17 more

**Background**: The electric-vehicle scheduling problem concerns assigning vehicles to trips while satisfying timetable and vehicle-operation requirements. In this setting, stochastic scheduling represents uncertain trip times, which can affect when vehicles need to charge; charging is also a grid concern because simultaneous demand can create peak loads. Hierarchical matching reduces the scheduling problem to compatibility decisions between timetable tiers, and the probability component represents how likely those matches are to remain feasible.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/0305215X.2026.2643627">Probability-based hierarchical matching approach for ...</a></li>
<li><a href="https://www.researchgate.net/publication/377347437_Electric_Vehicle_Scheduling_State_of_the_Art_Critical_Challenges_and_Future_Research_Opportunities">(PDF) Electric Vehicle Scheduling : State of the Art, Critical...</a></li>

</ul>
</details>

**Tags**: `#Electric vehicle scheduling`, `#Power grid optimization`, `#Stochastic optimization`, `#Operations research`, `#Transportation systems`

---

<a id="item-8" class="hz-item-anchor" data-hz-url="https://doi.org/10.23919/pcmp.2025.000294" data-hz-title="Review of SOFC System Control Objectives and Challenges" data-hz-tags="Solid Oxide Fuel Cells,Control Systems,Energy Systems,Power Systems,Review" data-hz-section="hust-research"></a>
## [Review of SOFC System Control Objectives and Challenges](https://doi.org/10.23919/pcmp.2025.000294) ⭐️ 6.0/10

This paper presents a comprehensive review of control objectives, strategies, and open challenges for solid oxide fuel cell systems. It synthesizes existing work rather than introducing a new control method. The review can help energy-system and control researchers compare approaches for managing SOFC operation and identify areas requiring further development. Better control is important for improving the practical deployment and reliability of SOFC-based power systems. An SOFC system must coordinate electrochemical power generation with operating conditions such as fuel and air supply, while control research also considers thermal behavior, including temperature-gradient management. The article is a synthesis of objectives, strategies, and challenges, so its value lies primarily in organization and analysis rather than a demonstrated performance breakthrough.

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · Jul 1, 00:00

**Match**: Paper keyword **fuel cell** matched under **能源电子与智能制造**.

**Related faculty**: 俞耀文, 刘智伟, 刘骁康, 卢仁智, 叶杰, 唐其鹏, 尹泉, 彭刚 and 13 more

**Background**: A solid oxide fuel cell is an electrochemical conversion device that produces electricity by oxidizing a fuel. Its basic structure includes a solid, usually ceramic, electrolyte between an anode and a cathode; fuel is supplied to the anode and an oxidant, typically air, to the cathode. System control is needed because these operating inputs and internal thermal conditions affect overall fuel-cell behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://www.netl.doe.gov/carbon-management/sofc/operating-principle">SOFC OPERATING PRINCIPLE | netl.doe.gov</a></li>
<li><a href="https://en.wikipedia.org/wiki/Solid_oxide_fuel_cell">Solid oxide fuel cell - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Solid Oxide Fuel Cells`, `#Control Systems`, `#Energy Systems`, `#Power Systems`, `#Review`

---

<a id="item-9" class="hz-item-anchor" data-hz-url="https://doi.org/10.23919/csms.2025.0021" data-hz-title="Optimizing Bus Networks with Shared BRT Lanes" data-hz-tags="transportation optimization,bus rapid transit,genetic algorithms,network design,operations research" data-hz-section="hust-research"></a>
## [Optimizing Bus Networks with Shared BRT Lanes](https://doi.org/10.23919/csms.2025.0021) ⭐️ 6.0/10

The paper introduces a bi-level Bus Transit Network Design and Frequency Setting model that explicitly incorporates regular buses sharing Bus Rapid Transit lanes. It also proposes a Priority-Based Genetic Algorithm, which performed strongly on Mandl’s benchmark instances and reduced passenger and operator costs while increasing BRT-lane utilization in a real-world Linyi network. The framework could help transit planners use underutilized BRT infrastructure more efficiently while improving bus speeds, transfers, and system-wide costs. Its main significance is methodological and operational, particularly for cities that already have BRT lanes and need to coordinate regular bus services with them. The model represents shared-lane infrastructure through specially defined BRT nodes and BRT-lane arcs, while the algorithm uses priority-based chromosomes, crossover, and mutation operators. The reported results are based on benchmark and Linyi experiments, so their generalizability to other road layouts, demand patterns, and operating policies remains to be tested.

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · Jun 1, 00:00

**Match**: Paper keyword **bus transit** matched under **系统工程与决策优化**.

**Related faculty**: 余明晖, 俞耀文, 刘振元, 刘智伟, 刘磊, 刘骁康, 卢仁智, 叶林涛 and 17 more

**Background**: Bus Rapid Transit is a bus system designed to provide higher capacity, reliability, and service quality than conventional buses, often using dedicated lanes. In this study, BRT-lane-sharing means that regular buses can use those lanes without disrupting scheduled BRT operations. A bi-level model separates network and frequency decisions from the resulting passenger or operational responses, while a genetic algorithm searches for good solutions to the resulting optimization problem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bus_rapid_transit">Bus rapid transit - Wikipedia</a></li>
<li><a href="https://www.transit.dot.gov/sites/fta.dot.gov/files/BRTBrochure.pdf">Bus Rapid Transit (BRT) Brochure</a></li>

</ul>
</details>

**Tags**: `#transportation optimization`, `#bus rapid transit`, `#genetic algorithms`, `#network design`, `#operations research`

---

<a id="item-10" class="hz-item-anchor" data-hz-url="https://doi.org/10.1080/0305215x.2026.2643627" data-hz-title="Probability-Based Matching Improves Stochastic EV Scheduling" data-hz-tags="Electric Vehicle Scheduling,Stochastic Optimization,Smart Grids,Operations Research,Transportation Systems" data-hz-section="hust-research"></a>
## [Probability-Based Matching Improves Stochastic EV Scheduling](https://doi.org/10.1080/0305215x.2026.2643627) ⭐️ 6.0/10

The article proposes a probability-based hierarchical matching (P-HM) method for stochastic electric vehicle scheduling that considers both uncertain trip times and power-grid load. It combines timetable tiering, compatibility-probability matching, and greedy local search to reduce fleet requirements and charging-peak violations while improving on-time performance. Public transport operators must coordinate vehicle availability, uncertain travel times, charging demand, and grid constraints rather than optimize them separately. By linking these factors, the method could support more reliable electric-bus operations while reducing pressure on the electricity grid. The model jointly minimizes fleet size, operating cost, and charging peak load while maximizing on-time performance, and numerical experiments report better results than benchmark methods. The evidence is based primarily on numerical experiments, so its practical performance under different networks, demand patterns, and charging infrastructures remains to be established.

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · Apr 1, 00:00

**Match**: Paper keyword **vehicle scheduling** matched under **系统工程与决策优化**.

**Related faculty**: 余明晖, 俞耀文, 刘振元, 刘智伟, 刘磊, 刘骁康, 卢仁智, 叶林涛 and 17 more

**Background**: The electric vehicle scheduling problem concerns assigning electric vehicles to scheduled trips while satisfying operational constraints such as vehicle availability and charging needs. In a stochastic setting, trip times and charging demand are uncertain rather than fixed. Power-grid load considerations are important because synchronized charging can create peaks that threaten grid security and conflict with reliable timetable operation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/0305215X.2026.2643627">Probability-based hierarchical matching approach for ...</a></li>
<li><a href="https://www.mdpi.com/2032-6653/17/5/255">Stochastic Optimal Scheduling Method for Vehicle–Grid ...</a></li>

</ul>
</details>

**Tags**: `#Electric Vehicle Scheduling`, `#Stochastic Optimization`, `#Smart Grids`, `#Operations Research`, `#Transportation Systems`

---

<a id="item-11" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560295" data-hz-title="Cascaded Cost Functions Improve PMSM Predictive Control" data-hz-tags="Model Predictive Control,PMSM,Motor Drives,Power Electronics,Control Systems" data-hz-section="hust-research"></a>
## [Cascaded Cost Functions Improve PMSM Predictive Control](https://doi.org/10.1109/ccdc69976.2026.11560295) ⭐️ 5.0/10

The paper presents a model predictive control approach for permanent-magnet synchronous motors (PMSMs) that combines cascaded dual cost functions with dynamic switching. The proposed structure aims to improve dynamic response while preserving steady-state control performance. PMSM drives are used in applications such as industrial automation and electric vehicles, where fast response and low steady-state error are both important. Reducing the tradeoff between these objectives could make predictive control more practical for high-performance motor drives. The approach addresses limitations associated with conventional predictive control, including reduced dynamic response, weighting-factor tuning, noise immunity, and steady-state behavior. The available information does not report specific experimental gains, computational requirements, or operating constraints for the proposed controller.

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · May 15, 00:00

**Match**: Paper keyword **PMSM** matched under **能源电子与智能制造**.

**Related faculty**: 俞耀文, 刘智伟, 刘骁康, 卢仁智, 叶杰, 唐其鹏, 尹泉, 彭刚 and 13 more

**Background**: Model predictive control repeatedly uses a motor model to evaluate possible control actions and select one according to a cost function. A permanent-magnet synchronous motor is an electric machine whose torque and current must be regulated under system constraints. In PMSM drives, predictive control is attractive because it can address nonlinear behavior and constraints, but its performance depends on controller design and computation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.semanticscholar.org/paper/Cascaded-Dual-Cost-Functions-Model-Predictive-for-Wang-Cheng/a1ea56b8309d0d116487a04a04bfbd28804a5a53">Cascaded Dual Cost Functions Model Predictive Control for ...</a></li>
<li><a href="https://grampc.github.io/grampc/tutorials/PMSM.html">Model predictive control of a PMSM — grampc 2.3 documentation</a></li>

</ul>
</details>

**Tags**: `#Model Predictive Control`, `#PMSM`, `#Motor Drives`, `#Power Electronics`, `#Control Systems`

---

<a id="item-12" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560068" data-hz-title="Improved Sensorless PMSM Control with ADRC and Adaptive Harmonic Filters" data-hz-tags="PMSM control,Sensorless control,Active disturbance rejection,Adaptive harmonic filtering" data-hz-section="hust-research"></a>
## [Improved Sensorless PMSM Control with ADRC and Adaptive Harmonic Filters](https://doi.org/10.1109/ccdc69976.2026.11560068) ⭐️ 5.0/10

The paper proposes a sensorless control method for permanent-magnet synchronous motors that combines improved active disturbance rejection control with parallel adaptive harmonic filters. The approach is intended to improve rotor-position estimation and rejection of disturbances without relying on a physical position sensor. Accurate rotor-position information is essential for vector control, while removing position sensors can reduce hardware complexity and improve applicability in some motor-drive systems. The combination could help address estimation errors and periodic disturbances, although the available information indicates a specialized research contribution rather than a broad industry breakthrough. ADRC is designed to estimate and compensate for internal and external disturbances without requiring a highly precise motor model, while the parallel adaptive filters target harmonic components that can affect estimation and control. The supplied material does not report quantitative accuracy improvements, operating-speed ranges, computational requirements, or experimental validation details, so the method's practical advantages cannot yet be assessed fully.

openalex · 华科 AIA 期刊 · 能源电子与智能制造 · May 15, 00:00

**Match**: Paper keyword **PMSM** matched under **能源电子与智能制造**.

**Related faculty**: 俞耀文, 刘智伟, 刘骁康, 卢仁智, 叶杰, 唐其鹏, 尹泉, 彭刚 and 13 more

**Background**: Sensorless PMSM control estimates the rotor position needed for vector control from electrical measurements rather than using a physical position sensor. One common approach derives back electromotive force from stator-voltage and current-control information, but estimation performance can be affected by operating conditions and disturbances. ADRC is a control framework intended to handle uncertain system dynamics and external disturbances, while adaptive harmonic filters estimate changing harmonic components so that their effects can be reduced.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2307187725009678">Sensorless rotor position estimation of PMSM for low and high ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s42835-023-01710-w">Overview of Active Disturbance Rejection Control for ...</a></li>
<li><a href="https://www.monolithicpower.com/en/learning/mpscholar/power-electronics/power-quality-and-harmonics/active-filters-for-harmonic-elimination?srsltid=AfmBOopAsjQATM-FVKgEVRKmlNzrjpDtXQ9JFhQmduQGv078rOLIWpOQ">Active Filters for Harmonic Elimination - Monolithic Power Systems</a></li>

</ul>
</details>

**Tags**: `#PMSM control`, `#Sensorless control`, `#Active disturbance rejection`, `#Adaptive harmonic filtering`

---

<a id="item-13" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11560172" data-hz-title="Hierarchical Matching for Vehicle Scheduling" data-hz-tags="vehicle scheduling,optimization,matching algorithms,transportation systems,operations research" data-hz-section="hust-research"></a>
## [Hierarchical Matching for Vehicle Scheduling](https://doi.org/10.1109/ccdc69976.2026.11560172) ⭐️ 5.0/10

The paper proposes a Hierarchical Matching-based algorithm for the Vehicle Scheduling Problem, with particular emphasis on minimizing fleet size. The approach is presented as a polynomial-time method for assigning vehicles to timetabled trips. Vehicle scheduling affects fleet requirements and operating costs in public transportation and other timetable-based systems. A method that reduces fleet size while preserving feasible trip assignments could improve resource utilization, although the broader impact depends on validation against established optimization methods. The Vehicle Scheduling Problem is described as NP-hard, while the proposed method focuses on fleet-size optimization rather than presenting a general account of all scheduling objectives. The provided materials do not report benchmark datasets, comparative results, or the method's performance trade-offs.

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · May 15, 00:00

**Match**: Paper keyword **vehicle scheduling** matched under **系统工程与决策优化**.

**Related faculty**: 余明晖, 俞耀文, 刘振元, 刘智伟, 刘磊, 刘骁康, 卢仁智, 叶林涛 and 17 more

**Background**: The Vehicle Scheduling Problem assigns a fleet of vehicles to timetabled trips so that every required trip is covered. Fleet size is often a central objective because using fewer vehicles can reduce operating requirements and costs. The problem is difficult to solve exactly at scale, which motivates algorithmic approaches such as matching-based methods.

<details><summary>References</summary>
<ul>
<li><a href="https://www.semanticscholar.org/paper/A-Hierarchical-Matching-Based-Approach-for-Vehicle-Shen-Li/820ef39a79a1c1ad6c402bbfc3b4844284e9576c">A Hierarchical Matching-Based Approach for Vehicle Scheduling</a></li>

</ul>
</details>

**Tags**: `#vehicle scheduling`, `#optimization`, `#matching algorithms`, `#transportation systems`, `#operations research`

---

<a id="item-14" class="hz-item-anchor" data-hz-url="https://doi.org/10.1109/ccdc69976.2026.11559800" data-hz-title="Integrated Bus Network and Timetable Design for Multimodal Transit" data-hz-tags="transportation optimization,public transit,timetable synchronization,operations research" data-hz-section="hust-research"></a>
## [Integrated Bus Network and Timetable Design for Multimodal Transit](https://doi.org/10.1109/ccdc69976.2026.11559800) ⭐️ 5.0/10

The study examines the joint design of bus networks and timetable synchronization across multimodal public transit systems. The available description does not report specific algorithms, datasets, or measured results. Coordinating network structure with departure times could improve transfers between modes and reduce passenger waiting, addressing a practical challenge in public transit planning. Its significance is currently best understood as methodological, because the available material does not establish a demonstrated operational improvement. Transit network design is generally treated as a nonlinear optimization problem, while timetable synchronization can target total passenger transfer waiting time. Because the paper content is not provided, its objective formulation, operational constraints, solution method, and limitations cannot be assessed from the available information.

openalex · 华科 AIA 期刊 · 系统工程与决策优化 · May 15, 00:00

**Match**: Paper keyword **timetable** matched under **系统工程与决策优化**.

**Related faculty**: 余明晖, 俞耀文, 刘振元, 刘智伟, 刘磊, 刘骁康, 卢仁智, 叶林涛 and 17 more

**Background**: A transit network design problem concerns how routes and connections should be arranged in a public transportation system. Timetable synchronization coordinates departure and arrival times so that passengers can transfer between services with less waiting, especially when multiple modes are involved.

<details><summary>References</summary>
<ul>
<li><a href="https://www.academia.edu/80977335/Integrated_Multimodal_Transit_Route_Network_Design_with_Feeder_Systems">(PDF) Integrated Multimodal Transit Route Network Design with...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0191261519301201">Transit timetable synchronization for transfer time ...</a></li>

</ul>
</details>

**Tags**: `#transportation optimization`, `#public transit`, `#timetable synchronization`, `#operations research`

---

## Other highlights

15. [Tencent Unveils Hy4 Preview, a 770B-Parameter Open-Weight Model](#item-15) ⭐️ 9.0/10
16. [Achieving Effectively Zero-P99 Autocomplete for 240 Million Domains](#item-16) ⭐️ 8.0/10
17. [Understanding ChatGPT Work’s Cloud and Local Agentic Workflows](#item-17) ⭐️ 8.0/10
18. [Continuous Diffusion Language Models Revisit Whole-Sequence Generation](#item-18) ⭐️ 8.0/10
19. [QubesOS Vulnerability Enables Code Execution Through Dom0 File Copying](#item-19) ⭐️ 8.0/10
20. [Neocloud Security Gaps Expose Risks in Multi-Tenant Infrastructure](#item-20) ⭐️ 8.0/10
21. [NASA Launches Telescope to Map the Universe](#item-21) ⭐️ 8.0/10
22. [A Practical Guide to Building Diffusion Language Models](#item-22) ⭐️ 7.0/10
23. [Inside a 1980 Spacelab Core-Memory Module](#item-23) ⭐️ 7.0/10
24. [OpenClaw 2.0 Raises the Stakes for Always-On AI Agents](#item-24) ⭐️ 7.0/10
25. [An 8B Model Brings Local Video Editing Planning to Phones](#item-25) ⭐️ 7.0/10
26. [AI Video Challenges China’s Digital-Actor Gig Economy](#item-26) ⭐️ 7.0/10
27. [US and Iran Exchange Strikes in Strait of Hormuz](#item-27) ⭐️ 7.0/10
28. [Hugging Face Introduces a $399 Device for On-Device LLM Experimentation](#item-28) ⭐️ 7.0/10
29. [Berkeley Humanoid Lite Makes Humanoid Robotics More Affordable](#item-29) ⭐️ 7.0/10
30. [AMD Targets Robotics with Heterogeneous SoCs](#item-30) ⭐️ 7.0/10
31. [Microsoft Makes WinUI Fully Open Source](#item-31) ⭐️ 7.0/10
32. [Hugging Face Introduces Microduck, an Open-Source Learning Robot](#item-32) ⭐️ 7.0/10
33. [Code-as-World Turns Videos Into Executable MuJoCo Simulations](#item-33) ⭐️ 7.0/10
34. [Opener Open-Sources DECT NR+ for IoT](#item-34) ⭐️ 7.0/10
35. [U.S. Drone and Robot Barriers May Shift Competition Abroad](#item-35) ⭐️ 6.0/10
36. [OpenMAIC Brings Multi-Agent AI Classrooms to GitHub](#item-36) ⭐️ 6.0/10
37. [Scientific Agent Skills Expands AI Research Workflows](#item-37) ⭐️ 6.0/10
38. [OpenShot 4.0 Migrates Its Video Editor UI to Qt6](#item-38) ⭐️ 6.0/10
39. [Roblox Contributes Open-Source Safety Models to ROOST](#item-39) ⭐️ 6.0/10
40. [Hackers’ Malware Infection Exposes Their Attack Infrastructure](#item-40) ⭐️ 6.0/10
41. [Sanctuary AI to Sell Its Robot Brain Separately](#item-41) ⭐️ 6.0/10
42. [The Sequence Reviews AI’s Expanding Industrial Role](#item-42) ⭐️ 6.0/10
43. [Musk’s Faster Gas-Turbine Plan Raises Pollution Concerns](#item-43) ⭐️ 5.0/10
44. [Caterpillar Applies Mining Automation Lessons to AI Deployment](#item-44) ⭐️ 5.0/10

---

<a id="item-15" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Aug/29/hy4/" data-hz-title="Tencent Unveils Hy4 Preview, a 770B-Parameter Open-Weight Model" data-hz-tags="Large Language Models,Open Weights,Mixture of Experts,Long Context,Tencent" data-hz-section="other"></a>
## [Tencent Unveils Hy4 Preview, a 770B-Parameter Open-Weight Model](https://simonwillison.net/2026/Aug/29/hy4/) ⭐️ 9.0/10

Tencent has released Hy4 Preview, an open-weight text-only LLM with 770 billion total parameters, 49 billion active parameters, and a 1-million-token context window. Compared with July’s Hy3, it increases the totals from 295 billion to 770 billion parameters, active parameters from 21 billion to 49 billion, and context length from 256,000 to 1 million tokens. Hy4 Preview raises the scale and long-context capability available in an open-weight model, potentially expanding research and deployment options beyond closed APIs. Its mixture-of-experts design can provide a very large parameter capacity while activating only a smaller subset for each input, although the full model still presents substantial storage and serving demands. The Hugging Face files occupy about 1.56 TB, and the model is text-only rather than multimodal. Its chat template supports two reasoning settings, with high as the default and no_think as the alternative; an example through OpenRouter showed the model generating an SVG-style image description and exposed a reasoning trace with abbreviated English phrasing.

rss · Simon Willison · Aug 29, 23:53

**Background**: In a mixture-of-experts model, the total parameter count includes all expert components, while the active parameter count refers to the subset selected for a particular input. This allows a model to have very high total capacity without using every parameter for every token, though serving and storing the complete set of weights can remain expensive. A context window is the amount of tokenized text a model can process as one input, so a 1-million-token window can accommodate much longer documents or conversations than a 256,000-token window.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mindstudio.ai/blog/mixture-of-experts-architecture-glm-5-2-active-parameters">Mixture of Experts Architecture Explained: How GLM... | MindStudio</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/long-context">Long context | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Tags**: `#Large Language Models`, `#Open Weights`, `#Mixture of Experts`, `#Long Context`, `#Tencent`

---

<a id="item-16" class="hz-item-anchor" data-hz-url="https://ruurtjan.com/articles/p99-0ms-autocomplete-for-240-million-domain-names" data-hz-title="Achieving Effectively Zero-P99 Autocomplete for 240 Million Domains" data-hz-tags="Autocomplete,Low-Latency Systems,Distributed Systems,Performance Engineering,Tries and Indexing" data-hz-section="other"></a>
## [Achieving Effectively Zero-P99 Autocomplete for 240 Million Domains](https://ruurtjan.com/articles/p99-0ms-autocomplete-for-240-million-domain-names) ⭐️ 8.0/10

The article presents an architecture for delivering effectively zero-millisecond P99 autocomplete across 240 million domain names. It focuses on the systems and performance trade-offs required to make the slowest one percent of requests appear instantaneous. The approach illustrates how autocomplete systems can optimize for tail latency rather than average response time, an important goal for interactive applications. It also highlights the tension between globally consistent responsiveness, network distance, implementation complexity, and the quality of suggested domains. Community feedback identified important caveats: some suggested domains may not exist, triggering on keyup may add unnecessary delay, and users far from the serving location may not experience the claimed responsiveness. Suggestions included popularity-weighted residual prediction and storing trie nodes as CDN-accessible files to reduce geographic network latency.

hackernews · dbalatero · Aug 31, 03:20 · [Discussion](https://news.ycombinator.com/item?id=49505219)

**Background**: P99 is a tail-latency measure: it is the latency below which 99 percent of requests complete, so it describes the experience of the slowest one percent. A trie, or prefix tree, stores strings by their successive characters and supports efficient prefix lookups, making it a common structure for autocomplete. Autocomplete systems typically precompute or cache prefix results so that each keystroke requires minimal work.

<details><summary>References</summary>
<ul>
<li><a href="https://duckkit.dev/glossary/latency-sre/tail-latency">Tail latency | duckkit.dev</a></li>
<li><a href="https://www.systemdesignsandbox.com/learn/design-autocomplete">Search Autocomplete (Typeahead) | System Design Sandbox</a></li>
<li><a href="https://www.geeksforgeeks.org/dsa/introduction-to-trie-data-structure-and-algorithm-tutorials/">Trie Data Structure - Commonly Asked Questions - GeeksforGeeks</a></li>

</ul>
</details>

**Discussion**: Commenters broadly appreciated the performance engineering but questioned the user experience and the meaning of the zero-millisecond claim. Concerns centered on nonexistent-domain suggestions, keyup-based triggering, regional latency in places such as Australia, and whether predictive indexing or CDN-hosted trie nodes could provide a simpler or more globally effective design.

**Tags**: `#Autocomplete`, `#Low-Latency Systems`, `#Distributed Systems`, `#Performance Engineering`, `#Tries and Indexing`

---

<a id="item-17" class="hz-item-anchor" data-hz-url="https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/" data-hz-title="Understanding ChatGPT Work’s Cloud and Local Agentic Workflows" data-hz-tags="AI agents,ChatGPT,computer use,developer tools,AI security" data-hz-section="other"></a>
## [Understanding ChatGPT Work’s Cloud and Local Agentic Workflows](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

Simon Willison analyzes ChatGPT Work, announced by OpenAI on July 9, and distinguishes its cloud version from the desktop-based local version formerly associated with Codex. His testing finds that the cloud product adds model selection, internet-enabled code execution, a headless Chrome browser, persistent shared storage, publishable ChatGPT Sites, sub-agents, and possibly scheduled prompt automations. ChatGPT Work moves an AI assistant beyond answering questions toward completing multi-step tasks with browsers, code, files, and delegated sub-agents. That could make computer-use automation more practical for developers and other paid users, while increasing the consequences of giving an agent access to private data and external content. Work is currently restricted to subscribers paying $20 per month or more, and its cloud and local variants expose different capabilities. The cloud interface offers GPT-5.6 Sol, Luna, and Terra with several reasoning levels, while the article notes uncertainty about exact model mappings, possible billing against Code usage, and the security risk of combining private-data access, untrusted content, and channels for communicating information outward.

rss · Simon Willison · Aug 30, 23:59 · [Discussion](https://news.ycombinator.com/item?id=49504625)

**Background**: An AI agent is a system that can reason across multiple steps and use tools such as browsers, terminals, or file systems rather than only generating text. Code execution and browser access let an agent inspect data and perform actions, while persistent storage allows information to remain available across sessions. Security guidance for agent systems commonly uses sandboxing and permission controls to restrict file-system and network access, because external documents, emails, or websites can contain malicious instructions.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/alifunk/when-ai-agents-become-the-attack-surface-architecting-against-self-propagating-threats-4olp">When AI Agents Become the Attack Surface... - DEV Community</a></li>
<li><a href="https://code.visualstudio.com/docs/agents/concepts/trust-and-safety">Trust and safety</a></li>
<li><a href="https://www.room714.com/en/blog/ai-architecture-security-the-gap-nobody-audits">AI Architecture Security : The Gap Nobody Audits Until... | Room 714</a></li>

</ul>
</details>

**Discussion**: Commenters described the computer-use capabilities as highly useful, including remote, voice-driven work involving email, documents, and forms. Others framed ChatGPT Work as OpenAI’s competitive response to Claude Cowork, while a prominent security concern was that the system combines private-data access, exposure to untrusted content, and ways to transmit information to an attacker.

**Tags**: `#AI agents`, `#ChatGPT`, `#computer use`, `#developer tools`, `#AI security`

---

<a id="item-18" class="hz-item-anchor" data-hz-url="https://sander.ai/2026/08/24/continuous-dlms.html" data-hz-title="Continuous Diffusion Language Models Revisit Whole-Sequence Generation" data-hz-tags="Diffusion Models,Large Language Models,Generative AI,Neural Network Architectures,AI Research" data-hz-section="other"></a>
## [Continuous Diffusion Language Models Revisit Whole-Sequence Generation](https://sander.ai/2026/08/24/continuous-dlms.html) ⭐️ 8.0/10

Sander Dieleman examines the renewed interest in continuous diffusion language models, which generate language through iterative refinement of an entire sequence rather than strictly left-to-right decoding. The approach is returning after discrete diffusion methods became more prominent following earlier work on continuous formulations. Whole-sequence refinement could make generation more coherent by allowing tokens to influence one another during multiple passes, instead of committing permanently to each next token. If the approach becomes efficient and competitive at scale, it could affect model architectures, controllable reasoning, and the balance between parallelism and sequential computation in language systems. Continuous diffusion addresses the mismatch between categorical language tokens and Gaussian noise by applying the corruption process in a continuous embedding space. Important caveats remain: diffusion language models typically require multiple refinement steps and cannot use standard key-value caching as straightforwardly as autoregressive models, although consistency-based methods such as CDLM aim to reduce both costs.

hackernews · peter_d_sherman · Aug 30, 20:46 · [Discussion](https://news.ycombinator.com/item?id=49502611)

**Background**: Autoregressive language models generate text sequentially: each new token is predicted from the tokens that have already been produced. Diffusion language models instead begin with a noisy, masked, or otherwise incomplete sequence and repeatedly reconstruct it, enabling the model to process many positions together. In continuous diffusion, the sequence is represented in a continuous embedding space during the noise and denoising process, even though the final output consists of discrete language tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://sander.ai/2026/08/24/continuous-dlms.html">Continuous diffusion language models – Sander Dieleman</a></li>
<li><a href="https://arxiv.org/abs/2511.19269">[2511.19269] CDLM: Consistency Diffusion Language Models For ... CDLM: Consistency Diffusion Language Models For Faster Sampling Continuous Diffusion Language Models (CDLM's) — Botonomous.ai Continuous Diffusion Rivals Discrete in Language Modeling Continuous Diffusion Language Models (CDLMs) Are Back—Why Now</a></li>
<li><a href="https://james.trappett.org/blog/continuous-diffusion-language-models-a-technical-revival/">Continuous Diffusion Language Models: A Technical Revival</a></li>

</ul>
</details>

**Discussion**: The discussion is broadly interested in diffusion language models, with some commenters viewing whole-sequence refinement as potentially more coherent than autoregressive sampling. Others challenge the historical account of autoregressive dominance, while additional speculation focuses on variable-rate thinking and interleaving a reasoning scratchpad with output; commenters also note that practical efficiency remains an important question.

**Tags**: `#Diffusion Models`, `#Large Language Models`, `#Generative AI`, `#Neural Network Architectures`, `#AI Research`

---

<a id="item-19" class="hz-item-anchor" data-hz-url="https://www.qubes-os.org/news/2026/08/29/qsb-118/" data-hz-title="QubesOS Vulnerability Enables Code Execution Through Dom0 File Copying" data-hz-tags="QubesOS,Security,Vulnerability,Arbitrary Code Execution,Operating Systems" data-hz-section="other"></a>
## [QubesOS Vulnerability Enables Code Execution Through Dom0 File Copying](https://www.qubes-os.org/news/2026/08/29/qsb-118/) ⭐️ 8.0/10

A QubesOS vulnerability in the Dom0 error-reporting backchannel used by `qvm-copy-to-vm` can enable arbitrary code execution under specific conditions. The VM variant of `qvm-copy-to-vm` is not affected because its error-reporting implementation does not use `system()`. The issue shows that even a narrowly scoped privileged workflow in QubesOS can create a path from untrusted VM-related data to code execution in Dom0. Its practical risk is limited by the requirement to perform file copying from Dom0, but compromise of Dom0 is especially serious because it is central to QubesOS management and isolation. The affected path is specifically associated with copying from Dom0 to a VM and with error reporting that invokes `system()`, while the corresponding VM-side path is unaffected. Community discussion also emphasizes that QubesOS guidance discourages using Dom0 for routine work or for interacting with potentially infected VMs, which reduces the likely attack surface but does not eliminate the vulnerability.

hackernews · vntok · Aug 30, 08:51 · [Discussion](https://news.ycombinator.com/item?id=49496918)

**Background**: QubesOS separates activities into isolated virtual machines, while Dom0 is the privileged management domain that controls important parts of the system. Tools such as `qvm-copy-to-vm` move files between domains, and Qubes uses inter-VM communication mechanisms such as qrexec to support controlled interactions. Because Dom0 has a privileged role, code execution there carries greater consequences than execution inside an ordinary VM.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49496918">Arbitrary code execution in QubesOS via copy - to - VM error reporting ...</a></li>
<li><a href="https://doc.qubes-os.org/en/latest/developer/services/qrexec.html">Qrexec: secure communication across domains - Qubes OS</a></li>

</ul>
</details>

**Discussion**: Commenters generally viewed the vulnerability as serious but noted that its narrow trigger—copying from Dom0—makes exploitation less likely for users who follow QubesOS operational guidance. Others used the disclosure to discuss QubesOS’s small but nonzero attack surface, while separate comments raised broader opinions about the project’s usability and graphics limitations that were not directly related to the vulnerability.

**Tags**: `#QubesOS`, `#Security`, `#Vulnerability`, `#Arbitrary Code Execution`, `#Operating Systems`

---

<a id="item-20" class="hz-item-anchor" data-hz-url="https://newsletter.semianalysis.com/p/most-neoclouds-suck-at-security" data-hz-title="Neocloud Security Gaps Expose Risks in Multi-Tenant Infrastructure" data-hz-tags="Cloud Security,Container Security,Multi-Tenancy,Kubernetes,Infrastructure Security" data-hz-section="other"></a>
## [Neocloud Security Gaps Expose Risks in Multi-Tenant Infrastructure](https://newsletter.semianalysis.com/p/most-neoclouds-suck-at-security) ⭐️ 8.0/10

The article analyzes security weaknesses among neocloud providers, covering container escapes, kernel-bypass networking, network policies, security keys, and multi-tenant Grafana. It also discusses OpenAI versus Hugging Face and previews ClusterMAX 3.0. Neocloud platforms combine specialized infrastructure with shared services, so weaknesses in isolation, authentication, networking, or observability can affect multiple customers. The analysis is relevant to organizations evaluating cloud providers for sensitive workloads and to engineers designing secure multi-tenant systems. A container escape can turn low-privilege access inside a container into access to the host or broader cluster, while kernel-bypass networking can reduce kernel-level checks because packet processing moves into user space. Multi-tenant Grafana and network policies therefore require careful tenant isolation, access control, and monitoring.

rss · Semianalysis（半导体·AI 风向标） · Aug 30, 15:46

**Background**: A container packages an application and its dependencies while sharing the host operating system kernel, so a misconfiguration or vulnerability can weaken the boundary between the container and the host. Kernel bypass networking sends network operations through user-space mechanisms instead of the conventional kernel network stack, often to reduce latency but with different security considerations. Multi-tenancy means multiple customers share an underlying service, making isolation of data, queries, credentials, and administrative access essential.

<details><summary>References</summary>
<ul>
<li><a href="https://unit42.paloaltonetworks.com/container-escape-techniques/">Container Breakouts: Escape Techniques in Cloud Environments</a></li>
<li><a href="https://blog.cloudflare.com/kernel-bypass/">Kernel bypass | Cloudflare Blog</a></li>
<li><a href="https://grafana.com/docs/loki/latest/operations/multi-tenancy/">Manage tenant isolation | Grafana Loki documentation</a></li>

</ul>
</details>

**Tags**: `#Cloud Security`, `#Container Security`, `#Multi-Tenancy`, `#Kubernetes`, `#Infrastructure Security`

---

<a id="item-21" class="hz-item-anchor" data-hz-url="https://www.bbc.co.uk/news/articles/ce87e55vgpjo?at_medium=RSS&at_campaign=rss" data-hz-title="NASA Launches Telescope to Map the Universe" data-hz-tags="Astronomy,Space Exploration,Dark Matter,Dark Energy,宇宙学" data-hz-section="other"></a>
## [NASA Launches Telescope to Map the Universe](https://www.bbc.co.uk/news/articles/ce87e55vgpjo?at_medium=RSS&at_campaign=rss) ⭐️ 8.0/10

NASA has launched a powerful new space telescope that is beginning a multi-year mission to create a new map of the universe. The mission will investigate dark matter and dark energy. A large-scale map of the universe could improve scientists’ understanding of how cosmic structure is distributed and evolves. Its observations may also provide important evidence about dark matter and the accelerated expansion associated with dark energy. The telescope is expected to operate over several years and focus on mapping the universe rather than making a single short observation. The available report does not provide specific details about the telescope’s instruments, launch vehicle, or observing schedule.

rss · BBC World News · Aug 30, 18:53

**Background**: Dark matter is inferred mainly from its gravitational effects because it does not appear to interact with ordinary matter and radiation in ways that make it visible. Dark energy is associated with the accelerated expansion of the universe and appears to have a large-scale effect rather than a local one. By mapping cosmic structure, astronomers can study clues related to both phenomena.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_matter">Dark matter - Wikipedia</a></li>
<li><a href="https://home.cern/science/physics/dark-matter/">Dark matter – Home | CERN</a></li>

</ul>
</details>

**Tags**: `#Astronomy`, `#Space Exploration`, `#Dark Matter`, `#Dark Energy`, `#宇宙学`

---

<a id="item-22" class="hz-item-anchor" data-hz-url="https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/" data-hz-title="A Practical Guide to Building Diffusion Language Models" data-hz-tags="Diffusion Models,Language Models,Generative AI,Deep Learning,Model Architecture" data-hz-section="other"></a>
## [A Practical Guide to Building Diffusion Language Models](https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/) ⭐️ 7.0/10

The article presents a technical guide to building diffusion language models, an alternative to conventional autoregressive language generation. It also frames related questions around their mathematical foundations, decoding efficiency, confidence estimation, and possible extensions. Diffusion language models can generate or revise multiple tokens through iterative denoising rather than producing text strictly from left to right, which could improve decoding flexibility and speed. Their progress may broaden the design space for generative language models, especially for discrete-token modeling and local inference. The technical discussion involves the evidence lower bound (ELBO), importance sampling, discrete diffusion, and confidence-aware decoding; these areas determine how the training objective and generation procedure are designed. Community feedback also highlights a practical caveat: although models such as DiffusionGemma can be fast in output tokens per second on GPUs, confidence estimation and the quality-versus-compute trade-off remain important considerations.

hackernews · volodia · Aug 30, 23:41 · [Discussion](https://news.ycombinator.com/item?id=49503956)

**Background**: Autoregressive language models typically generate text one token at a time, conditioning each new token on the preceding sequence. Diffusion language models instead corrupt or mask text and learn to reverse that process through repeated denoising steps. In discrete text settings, the model operates on tokens rather than continuous image pixels, making the training objective and denoising schedule important design issues.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ultralytics.com/glossary/diffusion-language-models">Diffusion Language Models: How They Work and Applications</a></li>
<li><a href="https://ar5iv.labs.arxiv.org/html/2303.06574">Diffusion Models for Non-autoregressive Text Generation : A Survey</a></li>
<li><a href="https://arxiv.org/html/2603.22248v1">Confidence-Based Decoding is Provably Efficient for Diffusion ...</a></li>

</ul>
</details>

**Discussion**: The discussion was broadly positive and educational: one commenter found the ELBO derivation clarifying, while another suggested exploring image-based text generation to avoid some difficulties of discrete token generation. Others praised DiffusionGemma’s GPU speed and local usability, but noted that confidence estimation received too little attention and that published results may still be limited by available time and compute.

**Tags**: `#Diffusion Models`, `#Language Models`, `#Generative AI`, `#Deep Learning`, `#Model Architecture`

---

<a id="item-23" class="hz-item-anchor" data-hz-url="https://www.righto.com/2026/08/spacelab-core-memory.html" data-hz-title="Inside a 1980 Spacelab Core-Memory Module" data-hz-tags="computer architecture,core memory,space computing,reliability engineering,hardware history" data-hz-section="other"></a>
## [Inside a 1980 Spacelab Core-Memory Module](https://www.righto.com/2026/08/spacelab-core-memory.html) ⭐️ 7.0/10

A reverse-engineering analysis examines the core-memory module used in a 1980 Spacelab computer, including its unusual architecture and engineering tradeoffs. The computer’s memory was built from four core-plane boards and was considered advanced and high-density for its late use of core memory. The module shows how spacecraft computers prioritized reliability and carefully managed hardware complexity before semiconductor memory became dominant. Its design provides historical insight into radiation-tolerant space computing and the reliability constraints that shaped critical systems. The Spacelab computer reportedly used no microprocessor; its 16-bit CPU was constructed from discrete TTL logic chips across multiple boards. Community discussion also highlighted an architecture without inhibit lines, raising questions about whether it primarily reduced the number of sense amplifiers and simplified board layout rather than increasing speed.

hackernews · pwg · Aug 30, 20:00 · [Discussion](https://news.ycombinator.com/item?id=49502214)

**Background**: Magnetic-core memory stores bits by using the magnetic state of small ferrite cores threaded by wires. It was valued for reliability and relatively short access times, but it was eventually displaced by semiconductor memory. In spacecraft, memory technology must also be evaluated against radiation-related failure modes and broader system-reliability requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://www.righto.com/2026/08/spacelab-core-memory.html">Cores in space: The core memory module from a 1980 Spacelab ...</a></li>
<li><a href="https://www.squaredtech.co/spacelabs-1980-computer-stunning-reverse-engineering-revealed">Spacelab Computer 1980 : Surprising Reverse-Engineering Find</a></li>
<li><a href="https://nepp.nasa.gov/files/25506/NEPPETW2010_LaBel_Memory.pdf">Memory Overview – Technologies and Needs - NASA</a></li>

</ul>
</details>

**Discussion**: The comments were broadly appreciative of core memory’s reliability in critical and space systems, while also asking technical questions about the inhibit-line-free architecture and its effect on speed, amplifier count, and board layout. One commenter connected the discussion to redundancy in modern LLM-based systems, although that comparison was only partially related to the article.

**Tags**: `#computer architecture`, `#core memory`, `#space computing`, `#reliability engineering`, `#hardware history`

---

<a id="item-24" class="hz-item-anchor" data-hz-url="https://openclaw.ai/blog/openclaw-2-accidentally" data-hz-title="OpenClaw 2.0 Raises the Stakes for Always-On AI Agents" data-hz-tags="AI agents,autonomous systems,AI security,LLM safety,developer tools" data-hz-section="other"></a>
## [OpenClaw 2.0 Raises the Stakes for Always-On AI Agents](https://openclaw.ai/blog/openclaw-2-accidentally) ⭐️ 7.0/10

OpenClaw 2.0 is presented as a major update to the open-source autonomous-agent project, with reports citing 16,000 changes. The update includes a rebuilt browser app, easier installation, shared cloud sessions, and support for ChatGPT, Claude, API keys, and local AI models. The release illustrates how AI agents are moving from conversational assistants toward systems that can remain available, use tools, and act across services with less human intervention. That broader capability could benefit developers and power users, but it also increases the consequences of prompt injection, excessive permissions, and unintended actions. OpenClaw is self-hosted and uses messaging platforms as a primary interface, while the reported 2.0 update broadens its browser, session, installation, and model integrations. Community discussion emphasizes that exposing an always-on agent to untrusted internet text or sensitive accounts could create a large privilege-escalation and data-loss blast radius, making sandboxing and human oversight important limitations.

hackernews · doppp · Aug 31, 03:38 · [Discussion](https://news.ycombinator.com/item?id=49505310)

**Background**: An autonomous AI agent is software that uses a large language model to plan tasks, invoke tools, access data, and perform actions rather than only generating text. OpenClaw uses messaging platforms as its main user interface, allowing users to communicate with an agent while it operates in a self-hosted environment. The security concern is that text an agent reads can contain instructions designed to manipulate its behavior, especially when the agent has access to privileged tools or personal accounts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems">Secure autonomous agentic AI systems | Microsoft Learn</a></li>
<li><a href="https://www.news9live.com/technology/artificial-intelligence/openclaw-2-0-update-ai-agents-multiplayer-16000-pull-requests-3003676">OpenClaw 2.0 is here with 16,000 changes, new AI agents and ...</a></li>

</ul>
</details>

**Discussion**: The 101 comments show mixed reactions: some users describe practical benefits from agent harnesses running in containers, while others question what useful tasks always-on agents actually perform or believe comparable assistants are easy to build. The strongest criticism focuses on prompt-induced privilege escalation, exposure of email and financial accounts, and the risks of connecting autonomous software to valuable systems without robust isolation.

**Tags**: `#AI agents`, `#autonomous systems`, `#AI security`, `#LLM safety`, `#developer tools`

---

<a id="item-25" class="hz-item-anchor" data-hz-url="https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247916663&idx=2&sn=174f44f53f5fb8296479fc52f461ad5f" data-hz-title="An 8B Model Brings Local Video Editing Planning to Phones" data-hz-tags="小语言模型,端侧AI,视频剪辑,多模态模型,模型自我进化" data-hz-section="other"></a>
## [An 8B Model Brings Local Video Editing Planning to Phones](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247916663&idx=2&sn=174f44f53f5fb8296479fc52f461ad5f) ⭐️ 7.0/10

vivo AI Lab and The Chinese University of Hong Kong, Shenzhen reportedly proposed RefineCut, a closed-loop framework in which an 8B open-source model iteratively revises editing plans and receives scores from a deterministic verifier. The reported training process combines multi-teacher distillation with preference optimization, and the work is said to have been accepted to the EMNLP 2026 main conference. The approach suggests that capable video-editing planning may be moved from cloud-based frontier models to smaller models running locally on phones. This could reduce latency and API costs while improving privacy and making automated, consistent editing more accessible to device manufacturers and users. RefineCut turns implicit prompt-driven decisions into explicit editing plans that can be checked item by item, with the verifier supplying the training signal. The reported comparisons use the same closed-loop protocol, so the claim that the 8B model surpasses two teachers and matches DeepSeek-V4-Pro should not be interpreted as universal superiority across all video-editing tasks.

rss · 量子位 · Aug 30, 02:19

**Background**: An 8B model has roughly eight billion parameters, making it substantially smaller than many frontier models and generally more suitable for local deployment. In this setting, video editing planning means deciding which clips, timings, transitions, or other operations should be used, rather than directly rendering the final video. A verifier is a rule-based or otherwise deterministic component that evaluates whether a proposed plan satisfies specified criteria.

<details><summary>References</summary>
<ul>
<li><a href="https://www.x-techcon.com/article/180860.html">手机本地一键成片，靠的是一个8B小模型的自我进化 | EMNLP'26</a></li>
<li><a href="https://news.sig.ai/cn/article/cmtfj4roy0001fkufbinbahhn">手机本地一键成片，全靠8B自我进化量子位 | 信鸽中文</a></li>

</ul>
</details>

**Tags**: `#小语言模型`, `#端侧AI`, `#视频剪辑`, `#多模态模型`, `#模型自我进化`

---

<a id="item-26" class="hz-item-anchor" data-hz-url="https://marginalrevolution.com/marginalrevolution/2026/08/china-fact-of-the-day-81.html?utm_source=rss&utm_medium=rss&utm_campaign=china-fact-of-the-day-81" data-hz-title="AI Video Challenges China’s Digital-Actor Gig Economy" data-hz-tags="Generative AI,AI video,Automation,Labor displacement,China tech" data-hz-section="other"></a>
## [AI Video Challenges China’s Digital-Actor Gig Economy](https://marginalrevolution.com/marginalrevolution/2026/08/china-fact-of-the-day-81.html?utm_source=rss&utm_medium=rss&utm_campaign=china-fact-of-the-day-81) ⭐️ 7.0/10

Advanced AI video-generation tools, including ByteDance’s Seedance 2.0, are increasingly enabling digital actors to replace human performers in China’s online entertainment sector. The shift is threatening jobs in a once-vibrant part of the country’s gig economy. The development shows how generative AI is moving beyond experimentation into labor substitution, potentially affecting large numbers of performers and online influencers. It could also lower production costs while intensifying pressure on workers whose income depends on digitally produced entertainment. ByteDance describes Seedance 2.0 as a unified multimodal audio-video generation model that accepts text, image, audio, and video inputs, supporting sophisticated content referencing and editing. The available report provides limited evidence about the number of jobs affected, the scale of adoption, or whether human performers will be fully replaced.

rss · Marginal Revolution · Aug 30, 04:25

**Background**: AI video-generation models create moving images from instructions and other reference media, rather than requiring every scene to be filmed with human performers. A multimodal model can combine inputs such as text, images, audio, and video to guide the generated result. In online entertainment, these capabilities can make it cheaper and faster to produce digital characters and short-form video content.

<details><summary>References</summary>
<ul>
<li><a href="https://seed.bytedance.com/en/seedance2_0">Seedance 2.0 - seed.bytedance.com</a></li>
<li><a href="https://seed.bytedance.com/en/models">Seed Models - seed.bytedance.com</a></li>

</ul>
</details>

**Tags**: `#Generative AI`, `#AI video`, `#Automation`, `#Labor displacement`, `#China tech`

---

<a id="item-27" class="hz-item-anchor" data-hz-url="https://www.bbc.co.uk/news/articles/cx2z72x5z1po?at_medium=RSS&at_campaign=rss" data-hz-title="US and Iran Exchange Strikes in Strait of Hormuz" data-hz-tags="US-Iran relations,military conflict,Strait of Hormuz,geopolitics,regional security" data-hz-section="other"></a>
## [US and Iran Exchange Strikes in Strait of Hormuz](https://www.bbc.co.uk/news/articles/cx2z72x5z1po?at_medium=RSS&at_campaign=rss) ⭐️ 7.0/10

The United States and Iran exchanged strikes for the first time in weeks. A US attack on Larak Island in the Strait of Hormuz reportedly killed two people and injured two others, marking the first known US strike there since late July. The exchanges signal renewed direct military escalation between Washington and Tehran in a strategically important waterway. Further fighting could increase regional security risks and affect global energy markets. The reported casualties on Larak Island were two dead and two injured. The available information identifies the attack as the first known US strike since late July but provides no further operational details.

rss · BBC World News · Aug 31, 08:34

**Background**: The Strait of Hormuz is the strategically important waterway identified in the report as the site of the attack. Direct strikes by the United States and Iran represent a more overt form of military escalation in the broader context of US-Iran relations.

**Tags**: `#US-Iran relations`, `#military conflict`, `#Strait of Hormuz`, `#geopolitics`, `#regional security`

---

<a id="item-28" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiU0FVX3lxTE10anNQWUJyb2dveFQyMkR5eFFBNzFBMjJaS2hJN1ppOVBnYURsaE9ka1FlVzFTdlRhN25aRnBDYlB6SDhJV0ZoS2wtbGt1X0FTNnZj?oc=5" data-hz-title="Hugging Face Introduces a $399 Device for On-Device LLM Experimentation" data-hz-tags="Hugging Face,On-device AI,Edge Computing,Large Language Models,AI Hardware" data-hz-section="other"></a>
## [Hugging Face Introduces a $399 Device for On-Device LLM Experimentation](https://news.google.com/rss/articles/CBMiU0FVX3lxTE10anNQWUJyb2dveFQyMkR5eFFBNzFBMjJaS2hJN1ppOVBnYURsaE9ka1FlVzFTdlRhN25aRnBDYlB6SDhJV0ZoS2wtbGt1X0FTNnZj?oc=5) ⭐️ 7.0/10

Hugging Face has introduced a $399 device aimed at making on-device large language model experimentation and deployment more affordable. The available report does not specify the device’s hardware configuration, supported models, or release timeline. A lower-cost device could broaden access to local LLM development and reduce reliance on cloud inference. On-device execution may also support lower latency, offline use, and improved privacy, although the practical benefits depend on the device’s performance and software support. The announcement is presented in a promotional context, and the available information does not provide benchmarks, memory capacity, accelerator details, model-size limits, or deployment software. Hugging Face has also been expanding into robotics, with its broader hardware efforts reportedly tracing back to work involving Rémi Cadene and the Tesla Optimus project in March 2024.

google_news · 36 Kr · Aug 31, 05:23

**Background**: On-device LLM inference means running a language model directly on a local device instead of sending requests to a remote cloud service. This approach can help address privacy and connectivity concerns, but local hardware has tighter limits on computing power and memory. Research on NPUs and mobile-sized models focuses on improving inference speed within those constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://eu.36kr.com/en/p/3962888000181893">Hugging Face Launches Affordable $ 399 AI Device : Diving Deep Into...</a></li>
<li><a href="https://arxiv.org/abs/2407.05858">[2407.05858] Fast On - device LLM Inference with NPUs</a></li>

</ul>
</details>

**Tags**: `#Hugging Face`, `#On-device AI`, `#Edge Computing`, `#Large Language Models`, `#AI Hardware`

---

<a id="item-29" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMinwFBVV95cUxOY3VoWlhBQzZPWFZFbnUtWUFqeXBMejFVcXNNVFQtT09yZkdXRlV4RFZYTmxmNXR4a3RtVFV0aHFhU3I4X3VjLXRENlVZb0JxbktYVkppM1BzS1c3RkdDVk5Sbkd0UG82RUtWTEwyTE52bUcyWHlvTnREaFdIM2VvTXNhU1p1a01rU0U0R2tNYzRyMGpCM0xCVEtOOTZiQ1U?oc=5" data-hz-title="Berkeley Humanoid Lite Makes Humanoid Robotics More Affordable" data-hz-tags="humanoid robotics,open source hardware,robot actuators,robotics research" data-hz-section="other"></a>
## [Berkeley Humanoid Lite Makes Humanoid Robotics More Affordable](https://news.google.com/rss/articles/CBMinwFBVV95cUxOY3VoWlhBQzZPWFZFbnUtWUFqeXBMejFVcXNNVFQtT09yZkdXRlV4RFZYTmxmNXR4a3RtVFV0aHFhU3I4X3VjLXRENlVZb0JxbktYVkppM1BzS1c3RkdDVk5Sbkd0UG82RUtWTEwyTE52bUcyWHlvTnREaFdIM2VvTXNhU1p1a01rU0U0R2tNYzRyMGpCM0xCVEtOOTZiQ1U?oc=5) ⭐️ 7.0/10

Berkeley Humanoid Lite is an open-source humanoid robot project designed to cost under $5,000 by using modular, 3D-printed gearboxes in its actuators and widely available components. The design makes the robot’s hardware and actuator technology available for building, customization, and research. Lower hardware costs could make humanoid robotics more accessible to researchers, students, and makers who cannot afford commercial platforms. Its open-source approach may also encourage broader experimentation and community-driven improvements in humanoid robot design. The platform emphasizes modular 3D-printed gearboxes and customization, but the available information does not establish that it matches the performance, reliability, or safety of more expensive commercial humanoid robots. The project is still evolving, with later releases describing continued development toward a future V2 version.

google_news · Open Source For You · Aug 31, 07:58

**Background**: An actuator is the mechanism that produces movement in a robot, while a gearbox modifies motor speed and torque to suit the required motion. In this project, modular 3D-printed gearboxes are integrated into the actuator design, allowing parts to be produced and replaced more easily than specialized industrial hardware. Open-source hardware means that the design materials are shared so others can build, modify, and contribute to the platform.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/HybridRobotics/Berkeley-Humanoid-Lite">GitHub - HybridRobotics/berkeley-humanoid-lite: Codebase for ...</a></li>
<li><a href="https://lite.berkeley-humanoid.org/">Berkeley Humanoid Lite: An Open-source, Accessible, and ...</a></li>

</ul>
</details>

**Tags**: `#humanoid robotics`, `#open source hardware`, `#robot actuators`, `#robotics research`

---

<a id="item-30" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMilAFBVV95cUxQX0FFT1NFTnNaeDNKbEtVLWlkVDBtVlFWN2toWjhLMVlMaFIzVC1CZW45aUg0NTE3cWc5UG1OZUdPSDdCdUEtWnB6MkNFMVhORHphRVhXSXBTQ3hQVDYyY0didUJrcW1EWFEtcDlDanJXY2lqYWk4MWZucVBEV1o1bVQ4Y0xHNWJfdWFsbFplLUNZcTlo?oc=5" data-hz-title="AMD Targets Robotics with Heterogeneous SoCs" data-hz-tags="AMD,Heterogeneous SoC,Robotics,Edge AI,Semiconductors" data-hz-section="other"></a>
## [AMD Targets Robotics with Heterogeneous SoCs](https://news.google.com/rss/articles/CBMilAFBVV95cUxQX0FFT1NFTnNaeDNKbEtVLWlkVDBtVlFWN2toWjhLMVlMaFIzVC1CZW45aUg0NTE3cWc5UG1OZUdPSDdCdUEtWnB6MkNFMVhORHphRVhXSXBTQ3hQVDYyY0didUJrcW1EWFEtcDlDanJXY2lqYWk4MWZucVBEV1o1bVQ4Y0xHNWJfdWFsbFplLUNZcTlo?oc=5) ⭐️ 7.0/10

AMD is pursuing heterogeneous system-on-chip designs as an alternative to GPU-dominant approaches in robotics and edge AI. The reported strategy aims to integrate different types of computing resources into a single device for these applications. If successful, this approach could give robotics developers another option beyond large standalone GPUs, particularly where power, size, latency, and integration are important. It also reflects broader competition among semiconductor companies to bring more AI processing closer to edge devices. A heterogeneous SoC combines different processing elements and can be tailored to an application by selecting the mix of computing components. The available report provides limited implementation details, so it does not establish a specific product, performance advantage, or confirmed displacement of GPU-based systems.

google_news · EE Times Asia · Aug 31, 02:30

**Background**: A system-on-chip integrates major computing functions into one piece of silicon rather than spreading them across separate chips. In a heterogeneous design, the chip contains different kinds of processing resources that can handle distinct workloads, which can improve flexibility and integration for specialized systems. AMD describes its Versal AI Edge adaptive SoCs as a way to support robotics and heterogeneous sensor fusion on a single device.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/products/adaptive-socs-and-fpgas/versal/ai-edge-series.html">AMD Versal™ AI Edge Series</a></li>
<li><a href="https://arxiv.org/pdf/2009.01178">Agile SoC Development with Open ESP</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#Heterogeneous SoC`, `#Robotics`, `#Edge AI`, `#Semiconductors`

---

<a id="item-31" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiigFBVV95cUxPNDcyT0pmaHBYNEd0M19JQm1YRk15eFJmMjJ2X1ZCV0tIdnF5VGNNcjAzN3RkVF9DSGFNZGVBWEF4TGw5VGhMLWRPQkZuSmlOLS1XWjltMUtUcWYzRjlGZDdma21OUUNBOERvZkxQc3J6TlJhakkzUGNTVDZ3S0hITmFBOFRVNkNjbkE?oc=5" data-hz-title="Microsoft Makes WinUI Fully Open Source" data-hz-tags="WinUI,Microsoft,Open Source,Windows Development,UI Frameworks" data-hz-section="other"></a>
## [Microsoft Makes WinUI Fully Open Source](https://news.google.com/rss/articles/CBMiigFBVV95cUxPNDcyT0pmaHBYNEd0M19JQm1YRk15eFJmMjJ2X1ZCV0tIdnF5VGNNcjAzN3RkVF9DSGFNZGVBWEF4TGw5VGhMLWRPQkZuSmlOLS1XWjltMUtUcWYzRjlGZDdma21OUUNBOERvZkxQc3J6TlJhakkzUGNTVDZ3S0hITmFBOFRVNkNjbkE?oc=5) ⭐️ 7.0/10

Microsoft has announced that WinUI, its modern Windows application UI framework, is now fully open source. Mainline development has moved to GitHub, where developers can create branches, submit pull requests, and participate in code reviews. The change could make WinUI development more transparent and give the Windows developer ecosystem a greater role in shaping the framework. It may also support broader community contributions and more predictable long-term evolution for Windows applications. WinUI 3 is delivered as part of the Windows App SDK and provides a XAML-based programming model for C# and C++ developers, along with Fluent Design controls and high-performance rendering. Open-source development does not by itself guarantee that every Windows component or all product decisions will be community-controlled.

google_news · Open Source For You · Aug 31, 07:38

**Background**: WinUI 3 is Microsoft's modern native user interface framework for building Windows desktop applications. It uses the XAML programming model and is designed to support modern interfaces based on Microsoft's Fluent Design System. The Windows App SDK packages WinUI 3 with other capabilities intended for Windows application development.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/windows/apps/winui/winui3/">WinUI 3 - Windows apps | Microsoft Learn</a></li>
<li><a href="https://github.com/microsoft/microsoft-ui-xaml">GitHub - microsoft/microsoft-ui-xaml: WinUI: a modern UI ...</a></li>

</ul>
</details>

**Tags**: `#WinUI`, `#Microsoft`, `#Open Source`, `#Windows Development`, `#UI Frameworks`

---

<a id="item-32" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMivwFBVV95cUxQemZqVUNlNnJZWUxIVFJocjdNMV9qcUkyYklXeFZUZzlmdV9WUkYyS054UGtBNk9lYWJWc3JncmQtNC1SS3BqSV9ZWUNHc1Z4OTdNcjYzRnZfaUZvaHZHLV9FOXFHcGhadndKcVFlbUwyWHdmZUpQNUN6V3dtdko5NVdON1kzR1dYZlhxNFdkcWlxWFhIdGdaTHZEcFFrVUJMeHVLenllYjN2bkJ1SWtvY1M4Q3A0YTlRTnh3YzRIY9IBxgFBVV95cUxPSmdMUkx5cXQ4UHA4ZVY5VE9QV1VwNFpTeVdhckNrc3NTdzk1MFp1T2FsWEVtd3htWkZaNXNEQ1htWm94Z3p2UmQtVXgyQS1CcFh6cjR6M0FSUWpPaW5CTW1IdjB1V2llMTVDYXFBM2N6MjBaLU9EOVluWDZvd0llRHl6aUhucDBqa2VQUHo5dzYycXNMRzBoRUdrN3R1dlN1cnJPSzFzTGp2djJBc1pqTnQ1MGZDZThDMGlqQ25pdG5SeWxFRkE?oc=5" data-hz-title="Hugging Face Introduces Microduck, an Open-Source Learning Robot" data-hz-tags="Robotics,Embodied AI,Open Source,Machine Learning,Hugging Face" data-hz-section="other"></a>
## [Hugging Face Introduces Microduck, an Open-Source Learning Robot](https://news.google.com/rss/articles/CBMivwFBVV95cUxQemZqVUNlNnJZWUxIVFJocjdNMV9qcUkyYklXeFZUZzlmdV9WUkYyS054UGtBNk9lYWJWc3JncmQtNC1SS3BqSV9ZWUNHc1Z4OTdNcjYzRnZfaUZvaHZHLV9FOXFHcGhadndKcVFlbUwyWHdmZUpQNUN6V3dtdko5NVdON1kzR1dYZlhxNFdkcWlxWFhIdGdaTHZEcFFrVUJMeHVLenllYjN2bkJ1SWtvY1M4Q3A0YTlRTnh3YzRIY9IBxgFBVV95cUxPSmdMUkx5cXQ4UHA4ZVY5VE9QV1VwNFpTeVdhckNrc3NTdzk1MFp1T2FsWEVtd3htWkZaNXNEQ1htWm94Z3p2UmQtVXgyQS1CcFh6cjR6M0FSUWpPaW5CTW1IdjB1V2llMTVDYXFBM2N6MjBaLU9EOVluWDZvd0llRHl6aUhucDBqa2VQUHo5dzYycXNMRzBoRUdrN3R1dlN1cnJPSzFzTGp2djJBc1pqTnQ1MGZDZThDMGlqQ25pdG5SeWxFRkE?oc=5) ⭐️ 7.0/10

Hugging Face, through its Pollen Robotics arm, has introduced Microduck, a $399 open-source biped robot designed to learn new behaviors through reinforcement learning. The 25-centimeter robot is available for preorder, with shipments expected before Christmas. Microduck could make embodied AI and robotics experimentation more accessible to developers, researchers, and hobbyists by combining an affordable physical platform with an open-source software stack. Its ability to train behaviors in simulation and run them on a real robot also reflects the broader shift toward AI systems that learn through interaction with the physical world. The robot has 15 motors, a camera, LiDAR, and a grasping beak, and it is intended to be usable out of the box. Its main caveat is that the available information does not yet establish real-world learning performance, adoption, or the range of tasks it can reliably perform.

google_news · The Indian Express · Aug 30, 03:50

**Background**: Embodied AI refers to artificial intelligence systems that perceive and act in the physical world through a body such as a robot. Reinforcement learning trains a system by allowing it to try actions and improve based on feedback, while simulation can provide a safer and less expensive environment for training before deployment on hardware. An open-source stack makes the robot's software and training workflow more accessible for modification and experimentation.

<details><summary>References</summary>
<ul>
<li><a href="https://pollen-robotics.com/microduck/">Microduck - A tiny biped robot you can teach new tricks ...</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI ? | NVIDIA Glossary</a></li>

</ul>
</details>

**Tags**: `#Robotics`, `#Embodied AI`, `#Open Source`, `#Machine Learning`, `#Hugging Face`

---

<a id="item-33" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMinwFBVV95cUxQVUxqbS1MN3VodV9pWjdoMVBNTUJQVkg1TXBqMXl0M1dzVlNSUHlRX2kxaDBLQlhKV0FnUW9UTWZuMzFxd1hvRGpkN2V5UU5hWEcxdWs3QlBvQ2NMNGpKQWxhSk5jRlIteTFYUVlhV3NMa3RiWXVLT0VKRm9KLWRsNy1SN0pfZGFfcDlVaFRNQ0FVUnZVc3ZMdkVTTWpOLWvSAZ8BQVVfeXFMUFVMam0tTDd1aHVfaVo3aDFQTU1CUFZINU1wajF5dDNXc1ZTUlB5UV9pMWgwS0JYSldBZ1FvVE1mbjMxcXdYb0RqZDdleVFOYVhHMXVrN0JQb0NjTDRqSkFsYUpOY0ZSLXkxWFFZYVdzTGt0Yll1S09FSkZvSi1kbDctUjdKX2RhX3A5VWhUTUNBVVJ2VXN2THZFU01qTi1r?oc=5" data-hz-title="Code-as-World Turns Videos Into Executable MuJoCo Simulations" data-hz-tags="Embodied AI,World Models,Robotics Simulation,MuJoCo,Code Generation" data-hz-section="other"></a>
## [Code-as-World Turns Videos Into Executable MuJoCo Simulations](https://news.google.com/rss/articles/CBMinwFBVV95cUxQVUxqbS1MN3VodV9pWjdoMVBNTUJQVkg1TXBqMXl0M1dzVlNSUHlRX2kxaDBLQlhKV0FnUW9UTWZuMzFxd1hvRGpkN2V5UU5hWEcxdWs3QlBvQ2NMNGpKQWxhSk5jRlIteTFYUVlhV3NMa3RiWXVLT0VKRm9KLWRsNy1SN0pfZGFfcDlVaFRNQ0FVUnZVc3ZMdkVTTWpOLWvSAZ8BQVVfeXFMUFVMam0tTDd1aHVfaVo3aDFQTU1CUFZINU1wajF5dDNXc1ZTUlB5UV9pMWgwS0JYSldBZ1FvVE1mbjMxcXdYb0RqZDdleVFOYVhHMXVrN0JQb0NjTDRqSkFsYUpOY0ZSLXkxWFFZYVdzTGt0Yll1S09FSkZvSi1kbDctUjdKX2RhX3A5VWhUTUNBVVJ2VXN2THZFU01qTi1r?oc=5) ⭐️ 7.0/10

MirroS’s Code-as-World uses an agentic loop to rewrite real-world videos into executable MuJoCo physics programs. The system proposes, executes, renders, verifies, and iteratively refines world hypotheses rather than relying on a single vision-language model prediction. This approach could give embodied AI and robotics systems more explicit, physically constrained world representations for reasoning and simulation. By producing executable programs, it may help connect visual observation with controllable robot environments, although the available material does not establish its practical performance. MuJoCo is an open-source physics engine used for fast and accurate simulation in robotics, biomechanics, graphics, and related fields. The provided excerpt describes the agentic workflow but gives no benchmark results, quantitative accuracy measures, or detailed limitations for the video-to-program conversion.

google_news · MarkTechPost · Aug 30, 01:35

**Background**: A world model is a representation of how entities and their interactions change over time, allowing an AI system to reason about possible outcomes. MuJoCo represents physical scenes as executable simulations governed by objects, contacts, motion, and other physical parameters. In Code-as-World, the proposed representation is program code that can be run and checked instead of only a visual or latent prediction.

<details><summary>References</summary>
<ul>
<li><a href="https://mirros.ai/report/code-as-world.pdf">Code as Worlds: Agentic Discovery of Executable World ...</a></li>
<li><a href="https://mujoco.org/">MuJoCo — Advanced Physics Simulation</a></li>

</ul>
</details>

**Tags**: `#Embodied AI`, `#World Models`, `#Robotics Simulation`, `#MuJoCo`, `#Code Generation`

---

<a id="item-34" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMigAFBVV95cUxNUjUxNnRhNWhZenNCU1BFOHRKOWVvZ3hrbnk4ajgzZlJLT3l2VjhBQklKQVRaZTZGU2xGajBDMGZsS0hmN3RsY1NMQ19qTkVDNmFQdm9PTjlnMHF3bU5UZDZTdDQzRFlWUWRkZkF5ak1GWjM3MEJMMHNBUVNpSGFvYw?oc=5" data-hz-title="Opener Open-Sources DECT NR+ for IoT" data-hz-tags="IoT,DECT NR+,Open Source,Wireless Communications,Embedded Systems" data-hz-section="other"></a>
## [Opener Open-Sources DECT NR+ for IoT](https://news.google.com/rss/articles/CBMigAFBVV95cUxNUjUxNnRhNWhZenNCU1BFOHRKOWVvZ3hrbnk4ajgzZlJLT3l2VjhBQklKQVRaZTZGU2xGajBDMGZsS0hmN3RsY1NMQ19qTkVDNmFQdm9PTjlnMHF3bU5UZDZTdDQzRFlWUWRkZkF5ak1GWjM3MEJMMHNBUVNpSGFvYw?oc=5) ⭐️ 7.0/10

Opener has open-sourced DECT NR+ technology for IoT, making the implementation more accessible for development and experimentation. The available report does not specify which components, licenses, or reference hardware are included. Open access could lower barriers for developers building scalable wireless systems for industrial IoT, metering, and smart-grid applications. It may also encourage experimentation with a non-cellular 5G technology designed to support large device populations and low-latency industrial communications. DECT NR+ is designed for decentralized and autonomous networking, including mesh deployments, and is reported to scale to millions of devices within a single network. However, the news item provides too little information to assess Opener’s implementation performance, interoperability, licensing terms, or production readiness.

google_news · Open Source For You · Aug 31, 08:28

**Background**: DECT NR+, also called DECT-2020 NR, is a radio standard developed by the European Telecommunications Standards Institute for DECT bands. It targets IoT and industrial applications and is described as a non-cellular 5G technology, meaning devices can communicate without relying on a traditional mobile-network operator. Its decentralized design is intended to support applications such as metering, smart grids, and industrial automation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DECT-2020">DECT-2020 - Wikipedia</a></li>
<li><a href="https://www.rfwireless-world.com/tutorials/dect-nr-tutorial">DECT NR+ Tutorial: Network Architecture, Protocol Stack ...</a></li>

</ul>
</details>

**Tags**: `#IoT`, `#DECT NR+`, `#Open Source`, `#Wireless Communications`, `#Embedded Systems`

---

<a id="item-35" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/08/30/the-u-s-is-building-barriers-around-drones-and-robots-china-still-has-scale/" data-hz-title="U.S. Drone and Robot Barriers May Shift Competition Abroad" data-hz-tags="Robotics,Drones,U.S.-China Competition,Supply Chains,Technology Policy" data-hz-section="other"></a>
## [U.S. Drone and Robot Barriers May Shift Competition Abroad](https://techcrunch.com/2026/08/30/the-u-s-is-building-barriers-around-drones-and-robots-china-still-has-scale/) ⭐️ 6.0/10

The United States is tightening restrictions on foreign-made drones and robots. The analysis argues that China’s manufacturing scale may redirect global competition to other markets rather than eliminate it. The development shows that trade and market-access barriers may limit sales in the United States without removing the competitive advantage created by China’s manufacturing capacity. Companies and policymakers may therefore face stronger competition in markets outside the United States. The available material does not identify specific regulations, companies, product models, or production figures. Its central caveat is that restricting foreign-made equipment in one market may change where competition occurs rather than end the competition.

rss · TechCrunch AI · Aug 31, 02:34

**Background**: Drones and robots are physical products that depend on manufacturing and supply chains. Manufacturing scale can help producers make equipment in larger volumes and compete across international markets, while restrictions can limit which foreign-made products are sold or used in the United States.

**Tags**: `#Robotics`, `#Drones`, `#U.S.-China Competition`, `#Supply Chains`, `#Technology Policy`

---

<a id="item-36" class="hz-item-anchor" data-hz-url="https://github.com/THU-MAIC/OpenMAIC" data-hz-title="OpenMAIC Brings Multi-Agent AI Classrooms to GitHub" data-hz-tags="Multi-Agent Systems,AI Education,TypeScript,Interactive Learning,Open Source" data-hz-section="other"></a>
## [OpenMAIC Brings Multi-Agent AI Classrooms to GitHub](https://github.com/THU-MAIC/OpenMAIC) ⭐️ 6.0/10

Tsinghua University’s THU-MAIC/OpenMAIC is gaining attention on GitHub, adding 31 stars in the past 24 hours and one fork. The TypeScript-based open-source project presents a one-click, immersive classroom powered by multiple interacting AI agents. OpenMAIC illustrates how multi-agent systems could make educational software more interactive by coordinating AI roles in a shared classroom environment. Its open-source availability may give developers and educators a practical starting point for experimenting with AI-assisted learning experiences. The project is written in TypeScript, and the related OpenMAIC descriptions mention interactive slides, quizzes, simulations, and AI teachers that can speak, draw, and discuss with learners. However, the available evidence shows only modest early traction, with 31 recent stars, one fork, and no reported pull requests or community debate.

ossinsight · THU-MAIC · Aug 30, 10:24

**Background**: A multi-agent system is a software setup in which multiple autonomous AI agents interact rather than relying on a single assistant. In OpenMAIC, this approach is used to organize an immersive classroom around a topic or document. The project’s stated classroom features include teaching interactions, quizzes, slides, and simulations.

<details><summary>References</summary>
<ul>
<li><a href="https://openmaic.io/">OpenMAIC — Open Multi-Agent Interactive Classroom</a></li>
<li><a href="https://open.maic.chat/home">OpenMAIC — Open Multi-Agent Interactive Classroom</a></li>

</ul>
</details>

**Tags**: `#Multi-Agent Systems`, `#AI Education`, `#TypeScript`, `#Interactive Learning`, `#Open Source`

---

<a id="item-37" class="hz-item-anchor" data-hz-url="https://github.com/K-Dense-AI/scientific-agent-skills" data-hz-title="Scientific Agent Skills Expands AI Research Workflows" data-hz-tags="AI agents,scientific computing,machine learning,drug discovery,Python" data-hz-section="other"></a>
## [Scientific Agent Skills Expands AI Research Workflows](https://github.com/K-Dense-AI/scientific-agent-skills) ⭐️ 6.0/10

K-Dense-AI's Python library, scientific-agent-skills, offers 161 validated skills and access to more than 100 scientific databases for AI-assisted research workflows. The repository gained 11 stars and one fork in the past 24 hours and supports Cursor, Claude Code, Codex, Pi, Antigravity, and the open Agent Skills standard. The project could reduce the effort required to equip AI agents with specialized procedures and data access for biology, chemistry, medicine, and drug discovery. Its compatibility with a cross-platform skills standard may also make scientific capabilities easier to reuse across different agent tools. The library is distributed as reusable skills and can be installed through the project's documented command, while the underlying Agent Skills format represents capabilities as portable, version-controlled files. The available information is largely promotional, and the recent activity of 11 stars and one fork does not by itself establish scientific or technical impact.

ossinsight · K-Dense-AI · Aug 30, 10:24

**Background**: AI agents are software systems that can perform multi-step tasks by combining a model with tools, instructions, and external data. An Agent Skill is a lightweight, reusable package of specialized knowledge or workflows that extends what an agent can do. The open standard is intended to let compatible agents discover and use these skills across different development environments.

<details><summary>References</summary>
<ul>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://cursor.com/docs/skills">Agent Skills | Cursor Docs</a></li>
<li><a href="https://github.com/K-Dense-AI/scientific-agent-skills">GitHub - K - Dense - AI / scientific - agent - skills : Turn any AI agent into...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#scientific computing`, `#machine learning`, `#drug discovery`, `#Python`

---

<a id="item-38" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiVEFVX3lxTE5YaGZiM0tkN2YtME15YTFiZndRRmF1elI4bzlmcEREZy1vVDE4NmpEbi1SUS1rWGdqaUt5Yk9tSFVRNkg0cWd3OW1kZ0pJT0cwQVRrSg?oc=5" data-hz-title="OpenShot 4.0 Migrates Its Video Editor UI to Qt6" data-hz-tags="OpenShot,Qt6,Open Source,Video Editing,Desktop Applications" data-hz-section="other"></a>
## [OpenShot 4.0 Migrates Its Video Editor UI to Qt6](https://news.google.com/rss/articles/CBMiVEFVX3lxTE5YaGZiM0tkN2YtME15YTFiZndRRmF1elI4bzlmcEREZy1vVDE4NmpEbi1SUS1rWGdqaUt5Yk9tSFVRNkg0cWd3OW1kZ0pJT0cwQVRrSg?oc=5) ⭐️ 6.0/10

OpenShot 4.0 has been released as a major update to the open-source, non-linear video editor. Its central change is adapting the user interface to Qt6. The migration modernizes OpenShot’s desktop application foundation and keeps it aligned with the current development direction of the Qt framework. It may improve the project’s ability to maintain and evolve its interface across supported desktop platforms. Qt6 is a major framework transition rather than merely a cosmetic redesign, so compatibility and migration work are important considerations for the project. The available announcement provides limited technical detail about the implementation or any measurable performance changes.

google_news · Phoronix · Aug 30, 19:55

**Background**: OpenShot is an open-source, non-linear video editing application, meaning users can arrange and edit video and audio clips in a timeline without processing the material only in sequential order. Qt6 is a cross-platform application and user-interface framework used to build desktop software. Moving an application’s interface from an earlier Qt generation to Qt6 can require substantial code and compatibility updates.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/OpenShot-4.0">OpenShot 4.0 Released In Adapting Video Editor UI To Qt6</a></li>
<li><a href="https://en.ubunlog.com/qt-6-2-has-already-been-released-and-these-are-its-news/">Qt 6 .2 has already been released and these are its news</a></li>

</ul>
</details>

**Tags**: `#OpenShot`, `#Qt6`, `#Open Source`, `#Video Editing`, `#Desktop Applications`

---

<a id="item-39" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMiiwFBVV95cUxQWVRnZjQ1bkhqS2t2MlBWT3ctdHNWMWZoMnhVb1VPTklHU3p0aG1TQ0E1WWNGTnpVV2Q4U0N4XzNzc1k3b21Hd0FxYktWRlBPbmwxY0lvVWlKYjRQNFB6dVl2MkRJYUwyVWtteWN0RGN1aklUa1p3NWZKODhCbGJlazItWVNaS3Q3V3dn?oc=5" data-hz-title="Roblox Contributes Open-Source Safety Models to ROOST" data-hz-tags="AI safety,Open source,Content moderation,Machine learning,Online platforms" data-hz-section="other"></a>
## [Roblox Contributes Open-Source Safety Models to ROOST](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQWVRnZjQ1bkhqS2t2MlBWT3ctdHNWMWZoMnhVb1VPTklHU3p0aG1TQ0E1WWNGTnpVV2Q4U0N4XzNzc1k3b21Hd0FxYktWRlBPbmwxY0lvVWlKYjRQNFB6dVl2MkRJYUwyVWtteWN0RGN1aklUa1p3NWZKODhCbGJlazItWVNaS3Q3V3dn?oc=5) ⭐️ 6.0/10

On August 19, 2026, Roblox announced that it is contributing three open-source safety models to the Robust Open Online Safety Tools (ROOST) Model Community. The contribution includes updates to its PII Classifier and Roblox Sentinel, its latest voice safety classifier, and a new evaluation dataset for benchmarking other classifiers. Making production safety models and evaluation resources openly available could reduce duplicated work for trust-and-safety teams building content moderation and online-risk mitigation systems. It may also give smaller platforms and developers access to inspectable starting points, while leaving governance and policy decisions to each platform. The models are being distributed through the ROOST Model Community, which aims to make open, inspectable safety models deployable by different organizations. The announcement provides limited information about model architectures, training data, licenses, measured performance, or deployment limitations, so the contributions should not be treated as universally validated moderation solutions.

google_news · Roblox · Aug 30, 15:54

**Background**: ROOST, or Robust Open Online Safety Tools, is an open-source tooling initiative focused on online safety. Its Model Community brings together developers, practitioners, and model creators to make safety models more accessible. Open and inspectable models can help organizations develop moderation systems, but each platform still needs to establish its own governance, policies, and operational safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://about.roblox.com/newsroom/2026/08/roblox-open-source-safety-models-roost">Roblox Brings Open-Source Safety Models to ROOST Model Community</a></li>
<li><a href="https://roost.tools/">Robust Open Online Safety Tools</a></li>
<li><a href="https://github.com/roostorg/model-community">GitHub - roostorg/model-community: Making open safety AI ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#Open source`, `#Content moderation`, `#Machine learning`, `#Online platforms`

---

<a id="item-40" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMibEFVX3lxTE1ZLXgxWHFEand4NkJHM2QyTy0wbGs5X1Ezc0cwSThEZi1RVUQ4b2xvb2VmcmlQOThESmo5UTVyLWk5SFA0b3UwZXgtejdmSzV2R0VtNVVzNFRtUmlsaWtyTFRJS3pOUlVndVdkcdIBckFVX3lxTE80WUFlRWc2em9aWl9WNzQtc3V5cmExNGx0TnhZM2NYNW5jN2lJclh5RzVlZ2pWdHdWMU96OG1wZHE2ZWtWcHFhZGFhLVg4SHplamhSZkRvdHMxZVBJVGUyVGtQWFdfWC00QjdJbC1ERU9qQQ?oc=5" data-hz-title="Hackers’ Malware Infection Exposes Their Attack Infrastructure" data-hz-tags="Cybersecurity,Malware Analysis,Threat Intelligence,RATs,Phishing" data-hz-section="other"></a>
## [Hackers’ Malware Infection Exposes Their Attack Infrastructure](https://news.google.com/rss/articles/CBMibEFVX3lxTE1ZLXgxWHFEand4NkJHM2QyTy0wbGs5X1Ezc0cwSThEZi1RVUQ4b2xvb2VmcmlQOThESmo5UTVyLWk5SFA0b3UwZXgtejdmSzV2R0VtNVVzNFRtUmlsaWtyTFRJS3pOUlVndVdkcdIBckFVX3lxTE80WUFlRWc2em9aWl9WNzQtc3V5cmExNGx0TnhZM2NYNW5jN2lJclh5RzVlZ2pWdHdWMU96OG1wZHE2ZWtWcHFhZGFhLVg4SHplamhSZkRvdHMxZVBJVGUyVGtQWFdfWC00QjdJbC1ERU9qQQ?oc=5) ⭐️ 6.0/10

A malware infection affecting hackers reportedly exposed their remote-access trojans, phishing kits, and attack infrastructure. The available report does not provide specific malware names, affected groups, or technical details. The incident could provide valuable threat-intelligence leads by revealing tools and infrastructure normally used by attackers. It also illustrates how malware operations can expose the attackers themselves when their systems are compromised. A remote-access trojan is malware that can give an attacker remote control of an infected device, while phishing kits are toolsets commonly used to conduct credential-theft campaigns. Because the provided content contains only a headline, the scope of the exposure and the security impact cannot be independently assessed here.

google_news · CyberSecurityNews · Aug 31, 05:23

**Background**: A remote-access trojan, or RAT, is a type of malware that enables unauthorized remote access to a victim’s computer. Phishing kits are packaged tools that help attackers create and operate phishing campaigns, often to steal credentials or other sensitive information. Attack infrastructure refers to the servers, domains, and related systems used to deliver malware, collect data, or manage compromised devices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fortinet.com/resources/cyberglossary/remote-access-trojan">fortinet.com/resources/cyberglossary/ remote - access - trojan</a></li>
<li><a href="https://socradar.io/blog/top-phishing-kits-cybercriminals/">Top 10 Phishing Kits Used by Cybercriminals</a></li>

</ul>
</details>

**Tags**: `#Cybersecurity`, `#Malware Analysis`, `#Threat Intelligence`, `#RATs`, `#Phishing`

---

<a id="item-41" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMinAFBVV95cUxPcmUwUTlmeXYzOU51VlJKbWFFMWdRRllBWFM5QXk3RFZUV0RCVm4wNHk3c3ZZVFp6UlJtd2FxS3VLMHpMMl82bm12NW9rR0xkLTVKWlA5NHFLT3U3R2NfZjBiVm5YVGFCc0V0bFVZeVlkb2wtMmphYnQ0MVkwUFh4dzZIM1RVY00tWFVPMEliQmhjclJmTVdVTVlBYjY?oc=5" data-hz-title="Sanctuary AI to Sell Its Robot Brain Separately" data-hz-tags="Embodied AI,Humanoid Robots,Robotics Software,AI Commercialization" data-hz-section="other"></a>
## [Sanctuary AI to Sell Its Robot Brain Separately](https://news.google.com/rss/articles/CBMinAFBVV95cUxPcmUwUTlmeXYzOU51VlJKbWFFMWdRRllBWFM5QXk3RFZUV0RCVm4wNHk3c3ZZVFp6UlJtd2FxS3VLMHpMMl82bm12NW9rR0xkLTVKWlA5NHFLT3U3R2NfZjBiVm5YVGFCc0V0bFVZeVlkb2wtMmphYnQ0MVkwUFh4dzZIM1RVY00tWFVPMEliQmhjclJmTVdVTVlBYjY?oc=5) ⭐️ 6.0/10

Sanctuary AI plans to commercialize its humanoid-robot software and control system as a standalone product, rather than selling only complete Phoenix robots. The strategy would let other hardware platforms potentially use the company’s robot-control technology. Selling the control system could shift Sanctuary AI toward a software-and-platform business model and broaden the market for its embodied-AI technology. It may also accelerate the separation of humanoid-robot hardware from the software that enables perception, learning, and physical task execution. The available information does not specify pricing, licensing terms, compatible robots, customer commitments, or evidence of external adoption. Sanctuary AI’s Phoenix platform uses the Carbon AI control system, and recent versions have combined hardware and software improvements, but the announcement provides few technical details about a standalone release.

google_news · Startup Fortune · Aug 29, 23:31

**Background**: Phoenix is Sanctuary AI’s general-purpose humanoid robot platform, while Carbon is the company’s AI control system for operating it. Embodied AI refers to artificial intelligence that acts in the physical world through systems such as robots, rather than producing outputs only in software. Separating the control system from Phoenix could allow the software to be deployed across different robotic bodies, although the available sources do not confirm that this interoperability is already supported.

<details><summary>References</summary>
<ul>
<li><a href="https://www.therobotreport.com/sanctuary-ai-latest-phoenix-humanoid-can-learn-tasks-in-24-hours/">Sanctuary AI 's latest Phoenix humanoid can... - The Robot Report</a></li>
<li><a href="https://chozan.co/embodied-ai/">Embodied AI : Why Humanoid Robots Are Moving AI Into... - ChoZan</a></li>

</ul>
</details>

**Tags**: `#Embodied AI`, `#Humanoid Robots`, `#Robotics Software`, `#AI Commercialization`

---

<a id="item-42" class="hz-item-anchor" data-hz-url="https://news.google.com/rss/articles/CBMid0FVX3lxTE04U1JMSV9BTlJLd3BuaGd5STNaYlhsMWp4M0syOVNINWc1ak5lRC14bllXV1VLNG1UUXdFbW5QRDYwS0pKcEpNcG9ERElZdnFJQktEWHlITEYzSHNqMGxFSFUxYXJTeC1xTlJDTk1TUUxWNWNvRG5v?oc=5" data-hz-title="The Sequence Reviews AI’s Expanding Industrial Role" data-hz-tags="Artificial Intelligence,Industrial AI,AI Industry Trends,Technology News" data-hz-section="other"></a>
## [The Sequence Reviews AI’s Expanding Industrial Role](https://news.google.com/rss/articles/CBMid0FVX3lxTE04U1JMSV9BTlJLd3BuaGd5STNaYlhsMWp4M0syOVNINWc1ak5lRC14bllXV1VLNG1UUXdFbW5QRDYwS0pKcEpNcG9ERElZdnFJQktEWHlITEYzSHNqMGxFSFUxYXJTeC1xTlJDTk1TUUxWNWNvRG5v?oc=5) ⭐️ 6.0/10

The Sequence’s Radar Issue #923 reviews notable AI developments from the past week, with a focus on AI’s expanding role in industrial applications. The available item does not identify the specific developments covered. The roundup highlights a broader shift from discussing AI primarily as a general-purpose technology to examining how it is being used in industrial settings. Its practical significance depends on the specific applications and developments included in the full issue. The item is presented as a weekly review by The Sequence and Jesus Rodriguez, but the provided content contains no technical specifications, company names, deployment figures, or discussion data. Readers therefore need the full issue to assess the individual developments and their evidence.

google_news · TheSequence | Jesus Rodriguez · Aug 30, 11:03

**Background**: Artificial intelligence refers here to technologies and systems being applied beyond research or consumer-facing use. Industrial applications are uses of AI in industrial settings, so the phrase “industrial turn” describes a growing emphasis on those practical applications.

**Tags**: `#Artificial Intelligence`, `#Industrial AI`, `#AI Industry Trends`, `#Technology News`

---

<a id="item-43" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/08/30/musks-faster-path-to-more-gas-turbines-comes-with-pollution-problem/" data-hz-title="Musk’s Faster Gas-Turbine Plan Raises Pollution Concerns" data-hz-tags="Energy Infrastructure,Gas Turbines,Environmental Impact,SpaceX,Public Health" data-hz-section="other"></a>
## [Musk’s Faster Gas-Turbine Plan Raises Pollution Concerns](https://techcrunch.com/2026/08/30/musks-faster-path-to-more-gas-turbines-comes-with-pollution-problem/) ⭐️ 5.0/10

Elon Musk says a secretive SpaceX foundry could cast its own gas-turbine blades and bring gas power online 18 months faster than competing efforts. The strategy could accelerate turbine deployment, but it also expands reliance on a fuel source facing lawsuits and public-health scrutiny. Faster gas-power deployment could help supply electricity for energy-intensive facilities, but additional turbines may increase air pollution and health risks in communities that already face poor air quality. The plan highlights a broader tension between rapidly expanding power capacity and reducing pollution from fossil-fuel infrastructure. The proposal centers on manufacturing turbine blades in-house, potentially using advanced casting methods; single-crystal blades are designed to withstand high temperatures while limiting creep deformation and oxidation. However, the supplied information does not establish the foundry’s production scale, emissions controls, or whether the claimed 18-month advantage has been independently verified.

rss · TechCrunch AI · Aug 30, 16:54

**Background**: A gas turbine generates electricity by burning gas to produce hot, expanding gases that drive turbine blades. Turbine blades operate under severe heat and mechanical stress, so manufacturers may use single-crystal casting to improve resistance to creep and oxidation. Public-health concerns arise because gas-turbine facilities can emit air pollutants that affect nearby communities and, according to the cited study, people living miles away.

<details><summary>References</summary>
<ul>
<li><a href="https://www.newayaerotech.com/study-cases/cmsx-alloy-single-crystal-casting-industrial-gas-turbines-blades">CMSX Alloy Single Crystal Casting Industrial Gas Turbines Blades</a></li>
<li><a href="https://www.pecva.org/work/energy-work/data-centers/new-study-highlights-public-health-impacts-of-gas-turbine-powered-data-centers/">New Study Highlights Public Health Impacts of Gas Turbine ...</a></li>

</ul>
</details>

**Tags**: `#Energy Infrastructure`, `#Gas Turbines`, `#Environmental Impact`, `#SpaceX`, `#Public Health`

---

<a id="item-44" class="hz-item-anchor" data-hz-url="https://techcrunch.com/2026/08/30/caterpillar-is-bringing-to-ai-deployment-what-it-learned-from-automating-mining/" data-hz-title="Caterpillar Applies Mining Automation Lessons to AI Deployment" data-hz-tags="industrial AI,autonomous systems,mining automation,AI deployment" data-hz-section="other"></a>
## [Caterpillar Applies Mining Automation Lessons to AI Deployment](https://techcrunch.com/2026/08/30/caterpillar-is-bringing-to-ai-deployment-what-it-learned-from-automating-mining/) ⭐️ 5.0/10

Caterpillar is applying decades of experience deploying autonomous machines at remote mining sites to its approach to AI deployment. The company’s mining automation work includes remotely controlled equipment, automated processes, and autonomous haulage fleets. Operating autonomous equipment in remote, high-risk environments can provide practical lessons for deploying AI reliably outside controlled settings. This could influence how industrial companies integrate AI with existing machinery, communications networks, and operational processes. Caterpillar’s MineStar solutions can automate a single mining process, remotely control one machine, coordinate different equipment types, or operate autonomous haul trucks without human intervention. The available information does not specify which AI systems, deployment methods, or performance results the company is now applying beyond mining.

rss · TechCrunch AI · Aug 30, 15:00

**Background**: Mining automation uses software, sensors, communications, and machine-control systems to perform tasks that would otherwise require continuous human operation. Autonomous haulage systems allow trucks to navigate and transport materials with limited or no direct control from a driver. Caterpillar describes its technology as supporting automation ranging from individual processes to entire autonomous fleets.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cat.com/en_US/by-industry/mining/autonomy-leadership.html">Autonomy & Automation | Cat | Caterpillar</a></li>
<li><a href="https://www.cat.com/en_US/by-industry/mining/minestar-solutions/automation.html">Automation Solutions | Cat | Caterpillar</a></li>

</ul>
</details>

**Tags**: `#industrial AI`, `#autonomous systems`, `#mining automation`, `#AI deployment`

---

