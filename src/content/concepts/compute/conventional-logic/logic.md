---
type: concept
slug: logic
canonical_name: Compute & Logic
aliases:
- compute-logic
kind: technology
parent_concepts:
- compute
- conventional-logic
related_concepts: []
sources: []
frontier:
- Do the 13x to 20x remote-traffic reductions reported for chiplet-contiguous layout convert into comparable end-to-end throughput or energy-per-token improvements on real inference serving, or are they absorbed by other bottlenecks?
- Will GPU and SoC vendors expose the CPU-side energy telemetry that already exists in firmware, given that an audit found per-rail energy computed internally but unreachable through any supported software interface 2026 06 16 the energy blind spot nvidias flagship edge ai hardware cann?
- How far do inter-die connection density and latency limits constrain 3D stacked logic once real designs move beyond the simulated design-space exploration in the current FPGA modelling work 2026 06 15 modeling optimizing and exploring multi die fpga routing arc?
- Does dual-mode reuse of AI matrix engines for cryptographic workloads scale beyond the 1.2x latency advantage shown at prototype level, or will dedicated accelerators reclaim the ground?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 74
descendants: []
last_reorg_date: '2026-05-14'
scorecard:
  viability: 5
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-29-us-commerce-department-moves-to-block-china-ai-firms-from-re
  title: U.S. Commerce Department moves to block China AI firms from remote access to advanced chips - 디지털투데이
  date: '2026-08-29'
  kind: web
- slug: 2026-08-27-ainews-hot-chips-openais-jalapeno-cerebras-cs-5-groq-3-lpx-a
  title: '[AINews] Hot Chips: OpenAI’s Jalapeño, Cerebras CS-5, Groq 3 LPX, Apple M6'
  date: '2026-08-27'
  kind: web
- slug: 2026-08-06-the-year-ai-science-and-the-physical-ai-industry-came-alive
  title: The Year AI Science and the Physical AI Industry Came Alive
  date: '2026-08-06'
  kind: web
- slug: 2026-08-03-the-inference-engineering-masterclass-philip-kiely-ali-taha-
  title: The Inference Engineering Masterclass — Philip Kiely & Ali Taha, Baseten
  date: '2026-08-03'
  kind: web
- slug: 2026-07-31-memory-fakes-and-thermodynamic-compute-chips-act-bets-874m-o
  title: 'Memory, Fakes, and Thermodynamic Compute: CHIPS Act Bets $874M on Six AI Stack Gaps - Tech Times'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-29-department-of-commerce-announces-letters-of-intent-with-7-co
  title: Department of Commerce Announces Letters of Intent With 7 Companies for $874 Million to Accelerate Semiconductor R&D for the Compute Supply Chain - National Institute of Standards and Technology (.gov)
  date: '2026-07-29'
  kind: web
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-06-10-europe-pursues-new-ai-chip-dream---center-for-european-polic
  title: Europe Pursues New AI Chip Dream - Center for European Policy Analysis (CEPA)
  date: '2026-06-10'
  kind: web
neighbors: []
---
**Conventional digital logic (clocked CMOS processors, GPUs, FPGAs and fixed-function accelerators) remains the substrate on which essentially all computing is built, and the current research frontier has shifted away from faster arithmetic towards moving data less: chiplet-aware memory layouts, dual-mode reuse of existing arrays, and better simulation and measurement tooling.**

## Summary

**What it is.** "Conventional logic" is the mainstream computing substrate: Boolean gates implemented as clocked CMOS transistors, assembled into CPUs, GPUs, FPGAs and application-specific accelerators, and paired with a DRAM-based memory hierarchy. It is the baseline against which unconventional paradigms (quantum, spiking neuromorphic, analogue in-memory, physics-based annealers) are measured. The category is unglamorous precisely because it is universal, and the interesting question is not whether it works but where its remaining headroom lies.

**How the headroom is now being extracted.** A mid-2026 snapshot of computer-architecture research shows a consistent pattern: the wins no longer come from the logic itself but from three adjacent places. First, **data movement and packaging**. Multi-chiplet GPUs split memory into local and remote high-bandwidth memory across a silicon interposer, and remote traffic for a single matrix-multiply shape varies by up to 58x purely as a function of kernel and placement choices. Choosing a chiplet-contiguous global memory layout instead of fixed 4 KB page interleaving cuts remote traffic by 13.0x on Qwen 3 30B and 20.7x on Llama 3.1 70B matrix multiplications, with no operating-system or hardware changes. The same story appears in FPGAs, where die-stacking limits inter-die connection density and latency and therefore demands a bespoke inter-die routing architecture, and in DRAM, described as "the huge memory bottleneck that plagues modern computing systems".

**Second, reuse and specialisation of existing fabrics.** Rather than building new cryptographic silicon, a dual-mode systolic array supports both matrix and direct polynomial multiplication for 20% extra area and negligible power overhead in matrix mode, beating transform-based polynomial multiplication on the same class of engine by more than 1.2x in latency. At the other end, fully custom conventional-logic chips still deliver: a 16 nm RISC-V system-on-chip with sixteen cores customised for Monte Carlo sampling, and a 65 nm probabilistic decision-tree engine at 11.3 nJ per inference with a 30-minute hypoglycaemia forecasting F1 of 0.825.

**Third, tooling and observability.** The design-space arguments above are only as trustworthy as the simulators behind them, which is why memory simulators are being rebuilt with HBM3/4, LPDDR5/6 and GDDR7 support plus formal validation workflows, and why power estimation is being pushed to source level using large-language-model representations of design hierarchy. The parameters that decide outcomes in this field are therefore: how much of the workload's energy and latency is arithmetic versus movement, inter-die connectivity density and latency, arithmetic precision, and whether the software stack can express the optimal placement at all.

## Viability (5/5)

The sources contain fabricated silicon across multiple nodes and vendors: a 16 nm multicore RISC-V system-on-chip on an Intel process, a 65 nm medical inference engine measured at 11.3 nJ per inference, and a 22 nm GlobalFoundries evaluation of a photon-sensor readout architecture. Consumer and workstation hardware built on this substrate is shipping now, with GB10-based desktop AI systems from NVIDIA, Dell, HP, ASUS, MSI, Acer and Gigabyte in 2026.

The strongest viability signal is indirect: the alternatives lean on conventional logic rather than replacing it. An optoelectronic Ising machine for NP-complete 3-SAT problems integrates its coupling and nonlinear mechanisms in a 65 nm CMOS chip running at 1 GHz with 4-bit weights, over an active area of 3.1 mm2, specifically to eliminate benchtop equipment from the loop. Neuromorphic accelerators in the same batch are digital, time-multiplexed, fixed-point designs with design-time configurability. Conventional logic is the floor under the whole field.

**TLDR: Not in question: every result in the sources, including the unconventional ones, is realised in CMOS logic.**

## Drivers (4/5)

**Supply.** The constraints have moved. Die stacking enables 2.5D and 3D FPGAs for improved yield and capacity, but inter-die connection density and latency become first-order design limits. DRAM is framed as the binding bottleneck, with dedicated characterisation infrastructure being built to attack memory scaling problems. Notably, CPU-side processing accounts for up to 90.6% of total latency and 44% of total dynamic energy in agentic workloads, which means the conventional scalar core, not just the accelerator, is back on the critical path.

**TLDR: Demand is dominated by large-model inference and edge agentic AI; supply-side pressure comes from the memory wall and from packaging rather than from transistor scaling.**

## Novelty (3/5)

Measured against the naive conventional baseline, the deltas are large. Chiplet-contiguous layout beats 4 KB page interleaving by 13.0x and 20.7x on remote HBM traffic, and beats coarse locality-aware placement by 3.3x and 3.7x. A 2D block-swizzle traversal discovered by an agentic AI using a locality simulator cuts remote traffic by up to 5.1x versus the best 1D traversal. A hierarchical dataflow readout keeps packet loss ultra-low where conventional architectures exceed 80% data loss, and improves effective refresh rate by 2.14x. Dual-mode systolic hardware gains cryptographic capability for 20% area.

Two cautions keep this from scoring higher. First, most headline numbers are proxy metrics (remote traffic, packet loss, area) rather than end-to-end throughput or total cost of ownership. Second, the field's own comparative work finds the trade-offs unresolved: the first hardware-system-level comparison of transform-based and SumCheck-based proving primitives under a unified framework, at equal SRAM and off-chip bandwidth budgets, concludes there is no universal winner despite SumCheck's asymptotic advantage of O(N) versus O(N log N). That is the honest signature of a mature substrate: asymptotics lose to locality, and the answer is workload-dependent. Historical framing supports this reading, with in-network computation and hardware synchronisation primitives traced across four decades from the NYU Ultracomputer's Fetch-and-Add to NVIDIA SHARP and HPE Slingshot.

**TLDR: No single breakthrough; a set of large, workload-specific system-level multipliers on top of an incumbent baseline, with the sources explicitly warning that there is no universal winner.**

## Diffusion (3/5)

The strongest diffusion signal in the sources is a deliberate design constraint: the chiplet-contiguous layout achieves its traffic reductions "without changes to the operating system or hardware". Open infrastructure also lowers the barrier: an overhauled memory simulator with a Python configuration interface and two-way code generation over C++, enhancements to the open-source FPGA CAD flow VTR/VPR, and shared DRAM characterisation hardware explicitly intended for community use. Design-space exploration itself is being automated, including by agentic AI driving a simulator.

The barriers are equally visible. Custom accelerators require bespoke software: the sampling SoC needed a customised compiler chain for spatial mapping and scheduling, and the flexible neuromorphic accelerator fixes neuron models and precisions at design time. More damning is the observability gap: an audit of a flagship edge AI platform found no CPU energy counter, no power-rail monitor, no IPMI/BMC and no powercap protocol exposed, with only instantaneous GPU power available, even though the firmware already computes per-rail energy internally through an undocumented interface. Energy-efficiency optimisations diffuse poorly when practitioners cannot measure energy.

**TLDR: Software-layer wins can diffuse fast because they need no hardware change; custom silicon and measurement are gated by toolchains and vendor firmware.**

## Impact (4/5)

The workload being optimised is the one absorbing most of the world's new compute spending: matrix multiplication in large-model training and inference. A 13x to 20x reduction in remote HBM traffic on production model shapes, achieved in software, is the kind of change that shifts effective capacity per installed accelerator rather than merely improving a benchmark. At the edge, the combination of agentic energy overheads of 4.33x to 7.63x and CPU-side dominance of up to 90.6% of latency points to comparably large recoverable waste in a hardware category shipping across seven named vendors in 2026.

Beyond AI, the same substrate underpins domains where conventional logic is the enabling component rather than a cost line: readout for dark-matter detectors with hundreds of thousands of synchronised channels, where existing architectures can lose over 80% of data during photon bursts, and implantable-class medical inference at 11.3 nJ per inference with quantified uncertainty and noise robustness. What holds the score below 5 is that the sources measure proxies and single kernels, not deployed system-level savings.

**TLDR: Order-of-magnitude reductions in data movement on the single dominant workload class translate directly into capital and energy savings at fleet scale.**

## Timing Now (0-2yr)

Two clocks run at different speeds here. The locality, scheduling and layout work is available now because it requires no operating-system or hardware modification, and the simulators and CAD flows enabling it have been released or updated in mid-2026. The hardware it targets, multi-chiplet GPUs on silicon interposers, is the platform being optimised today, not a future one.

The specialised-silicon track is later. Test chips exist at 16 nm and 65 nm, but each needs a compiler chain and a market, and the 3D FPGA routing questions the sources describe as "unanswered" are still at the design-space-exploration stage. Expect the near-term returns from conventional logic to be software and packaging returns, with architectural specialisation arriving over a longer horizon that the sources do not date.

**TLDR: The software and layout half is deployable immediately; the custom-silicon half is already in fabricated test chips but needs toolchains.**

## Overrated or underrated? Underrated

Conventional CMOS logic gets treated as the boring incumbent while attention flows to post-CMOS paradigms, yet in this evidence base the incumbent is where all the measured gains actually land, and the alternatives are themselves implemented in it. The Ising machine that promises advantage on NP-complete problems is a 65 nm CMOS chip demonstrated with 64 spins; the neuromorphic accelerator is a digital fixed-point design. Meanwhile a memory-layout change on conventional hardware buys 13x to 20x less remote traffic on real large-model kernels. Free order-of-magnitude wins available in software indicate a system that is far from its efficiency frontier, which is a bullish, not bearish, signal for the incumbent substrate.

The qualification matters. What is underrated is the *systems and data-movement layer* of conventional logic, not conventional logic as a scaling story. Nothing in these sources claims transistor-level improvement; the evidence points the other way, towards packaging limits, DRAM as the binding constraint, and workload-dependent answers with no universal winner. Anyone investing on the assumption that conventional logic keeps improving by itself is reading this wrong. The returns accrue to whoever controls placement, scheduling, packaging and measurement.

## Prediction

By 30 June 2028, chiplet-local contiguous memory layout or an equivalent locality-aware placement policy will be a documented, default-enabled option in at least one major GPU vendor's production GEMM or LLM inference library, rather than a research prototype.

## Evidence base

- Remote HBM traffic for a single fixed GEMM shape on multi-chiplet GPUs varies by up to 58x across the kernel and placement design space, and an agentic AI using the simulator found a 2D block-swizzle traversal cutting remote traffic up to 5.1x versus the best 1D traversal (15 June 2026) 
- A chiplet-contiguous global memory layout reduces remote HBM traffic by 13.0x on Qwen 3 30B and 20.7x on Llama 3.1 70B GEMMs versus 4 KB interleaving, with no operating-system or hardware changes (15 June 2026) 
- An audit of the ASUS Ascent GX10 (GB10 SoC) found no CPU energy counter, no power-rail monitor, no IPMI/BMC and no powercap interface, with only instantaneous GPU power via NVML, while CPU-side processing accounts for up to 90.6% of latency and 44% of dynamic energy in agentic workloads (16 June 2026) 
- A dual-mode systolic array supporting both matrix and direct polynomial multiplication costs 20% additional area with negligible power overhead in matrix mode, and achieves more than 1.2x lower latency than NTT-based polynomial multiplication on systolic matrix engines (16 June 2026) 
- The first hardware-system-level comparison of NTT- and SumCheck-based zero-knowledge proving primitives at equal on-chip SRAM and off-chip bandwidth budgets concludes there is no universal winner, despite SumCheck's O(N) versus O(N log N) asymptotic advantage (16 June 2026) 
- A 64-spin all-to-all optoelectronic Ising machine benchmarked on 3-SAT integrates coupling and nonlinearity in a 65 nm CMOS chip of 3.1 mm2 active area running at 1 GHz with 4-bit coupling weights, showing unconventional computing still built on conventional logic (16 June 2026) 

## Open questions

- Do the 13x to 20x remote-traffic reductions reported for chiplet-contiguous layout convert into comparable end-to-end throughput or energy-per-token improvements on real inference serving, or are they absorbed by other bottlenecks?
- Will GPU and SoC vendors expose the CPU-side energy telemetry that already exists in firmware, given that an audit found per-rail energy computed internally but unreachable through any supported software interface?
- How far do inter-die connection density and latency limits constrain 3D stacked logic once real designs move beyond the simulated design-space exploration in the current FPGA modelling work?
- Does dual-mode reuse of AI matrix engines for cryptographic workloads scale beyond the 1.2x latency advantage shown at prototype level, or will dedicated accelerators reclaim the ground?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
