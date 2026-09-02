---
type: concept
slug: processing-in-memory
canonical_name: Processing-in-Memory (PIM)
aliases:
- pim
- processing in memory
- near-memory-compute
kind: technology
parent_concepts:
- memory
- in-memory-computing
related_concepts:
- in-memory-computing
- memcapacitor
- sram-cim
- charge-domain-compute
- hbm
- 3d-dram
sources:
- '[[2026-06-16-cim-landscape-2026]]'
frontier:
- Do the chiplet and CXL-attached designs survive fabrication, and how do measured end-to-end numbers compare with the simulated 1.20x-2.23x system speedups reported for NPU plus PIM platforms 2026 07 29 beyond prefill decode disaggregation dissecting llm inferenc?
- Can a PIM device designed today remain efficient across two generations of model-architecture change, given that bimodal MoE expert distributions already break existing static offload rules 2026 06 05 sieve dynamic expert aware pim acceleration for evolving mix?
- Does non-volatile PIM reach the device reliability and thermal-noise tolerance that the 2026 review identifies as the precondition for commercial viability 2026 06 05 a comparative study of digital memristor based processing in, or does DRAM and SRAM near-memory logic take the whole market?
- Does any of the competing scheduling and compiler frameworks consolidate into a portable programming model, or does every PIM part continue to require its own bespoke stack 2026 07 28 pimid a full system simulator with intricacy and diversity f?
- Do the memory IDMs (SK AiM, Samsung HBM-PIM) ever ship PIM in volume, or does it stay a decade-long demo? Every generation since 2021 has been "almost productised."
- Does a hyperscaler design PIM into a shipping system, the event that would make it real — and if so does that validate or kill the startup CIM cohort?
- Where is the line between PIM (logic near memory, IDM) and CIM (the cell computes, startup) actually drawn in products, and does it blur?
last_updated: '2026-08-31'
tags:
- concept
- in-memory-compute
- pim
- memory-idm
- map
mention_count: 36
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 2
sources_30d: 8
recent_mentions:
- slug: 2026-07-10-workload-phase-silicon-sweep
  title: 'Workload-phase silicon sweep: pre-training / RL / prefill / decode procurement split'
  date: '2026-07-10'
  kind: web
- slug: 2026-06-16-cim-landscape-2026
  title: 'Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM'
  date: '2026-06-16'
  kind: web
- slug: 2026-01-22-ai-chips-computeram-and-the-future
  title: 'AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara'
  date: '2026-01-22'
  kind: substack
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
neighbors:
- slug: in-memory-computing
  name: In-Memory Computing
  path: /memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: memcapacitor
  name: Memcapacitor
  path: /memory/emerging-memory/memcapacitor/
  macro: memory
- slug: sram-cim
  name: SRAM Compute-in-Memory
  path: /memory/emerging-memory/sram-cim/
  macro: memory
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /compute/non-conventional/charge-domain-compute/
  macro: compute
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /memory/mainstream-memory/hbm/
  macro: memory
- slug: 3d-dram
  name: 3D DRAM
  path: /memory/mainstream-memory/3d-dram/
  macro: memory
---
**Processing-in-Memory puts arithmetic and logic inside or immediately beside the memory arrays so that memory-bound workloads such as LLM decoding, graph traversal and vector search stop paying for data movement; the physics is sound and simulated speedups are large, but real PIM silicon remains scarce and almost every published number is a simulator number.**

## Summary

Conventional machines separate storage from compute, so every operand crosses a narrow, power-hungry bus. For kernels with low operational intensity (few arithmetic operations per byte fetched) this bus, not the arithmetic units, sets the ceiling. Processing-in-Memory (PIM) attacks that ceiling by co-locating computation with memory. Two families dominate. *Processing-using-memory* performs the operation in the array itself, either analog matrix-vector multiplication in a resistive crossbar or massively parallel bitwise logic for more general workloads. *Processing-near-memory* leaves the array alone and attaches logic at the bank periphery, on a logic die, or on a separate chiplet. Substrates in play across the literature include seven DRAM standards, SRAM, and non-volatile RRAM, PCM, MRAM and FeFET.

The parameters that decide whether a PIM design wins are consistent across the papers. First, kernel arithmetic intensity: LLM decoding is dominated by memory-bound GEMV or flat GEMM and is therefore the canonical target. Second, the area cost of putting processing elements inside DRAM, which reduces usable memory capacity, and the weakness of logic that can be built in a DRAM process at all. Third, communication inside the memory: prior transformer PIM designs suffered costly inter-bank traffic and could not scale past bank capacity, and PIM units have small local memory, expensive inter-unit communication and relatively weak compute. Fourth, for non-volatile PIM, device reliability and thermal noise, which perturb stored weights and degrade inference accuracy. Fifth, the host interface: how a CPU or GPU shares address space and bus with the PIM device without bank conflicts and bus congestion eating the gain.

The response to those constraints in 2025-2026 work is architectural rather than device-level: decouple logic and memory into chiplets built in different process nodes and connect them over an interposer, then attach the module over CXL; mix substrates so each kernel lands on the device that suits it, for example SRAM-PIM for latency-critical attention and HBM-PIM for weight-heavy GEMV, or a matrix tile plus a traversal tile in one 2.5D package; and add a scheduler that decides at runtime what goes to PIM and what stays on the host.

A separate strand treats content-addressable memory as the PIM primitive rather than arithmetic. Reformulating Insert, Search, Update and Delete as in-situ content-addressable operations turns indexing itself into a memory operation, and a hardware-first graph database model has been specified around a small content-addressable instruction set (CAR, CAR2, AAR) with a dually-addressable memory implemented in ordinary FPGA block RAM rather than exotic devices.

## Viability (3/5)

The mechanism is not in doubt and the design space is being explored seriously by multiple independent groups, including work co-authored by Onur Mutlu, Kunle Olukotun, Tajana Rosing and Shahar Kvatinsky. But the field states its own weakness plainly: real PIM hardware remains scarce and simulation is the primary way to explore the design space, which is the stated motivation for a new full-system simulator in July 2026. A 2026 review of memristor-based digital PIM concludes that device-level optimisation is still the gating factor for scalable and commercially viable PIM, and that reliability is a key open challenge.

There are also demonstrated physical limits that the architecture papers accept rather than dispute: putting processing elements inside DRAM chips costs capacity and yields weak compute because of DRAM fabrication constraints, and non-volatile PIM arrays lose inference accuracy to thermal noise unless the model is trained to tolerate it. The one piece of peer-reviewed hardware in these sources is small: an 8x512x36-bit dually-addressable memory on a Xilinx Virtex-7. That is a working primitive, not a system. Score 3 reflects a credible paradigm whose quantitative claims are almost entirely pre-silicon.

**TLDR: Physics and simulation are convincing; fabricated PIM silicon is explicitly described as scarce, so most headline numbers are unvalidated by hardware.**

## Drivers (4/5)

Demand is the strongest part of the case and it is named precisely. LLMs are becoming memory-bound as context length and KV cache size grow, and the decoding phase is dominated by low-intensity GEMV or flat GEMM, which is what PIM is good at. GPUs are described as suffering severe resource underutilisation and bandwidth bottlenecks on exactly these workloads. Beyond LLMs: billion-scale graph ANNS is capped at main-memory bandwidth on CPUs while GPUs lack the HBM capacity to hold the index; genomic sequence alignment and network analytics are addressed by heterogeneous PIM chiplets; data indexing is bottlenecked by the same memory wall; and on-device LLMs, driven by privacy and response time, make energy-intensive data transfer on mobile a first-order cost.

On supply, the enabling shift is packaging and interconnect rather than new memory cells: chiplet decoupling of logic and memory in heterogeneous process nodes over an interposer, packaged as a CXL-attached module, and 3D or 2.5D integration to mix substrates on one platform. One driver runs the other way: workloads are moving faster than PIM designs. Modern MoE models activate fewer experts out of increasingly many, producing bimodal token-to-expert distributions that break the static offload rules assumed by existing PIM systems and sharply reduce their efficiency. A hardware paradigm whose advantage depends on workload shape is exposed to model-architecture churn.

**TLDR: Demand pull from memory-bound LLM decoding, KV cache growth and on-device inference is strong and specific; supply is being unblocked by chiplets and CXL rather than by new devices.**

## Novelty (3/5)

The comparison baselines are explicit. Against an NVIDIA H100, a processing-using-memory matrix tile reports 42.8x speedup and 392x energy efficiency on all-pairs shortest path. Against prior PIM architectures, a 3D heterogeneous GNN training accelerator reports up to 3.8x in TOPS/W and 6.8x in TOPS/mm2 with no accuracy loss. In-situ content-addressable indexing reports 4.7-7.8x throughput, more than 14.5x lower tail latency and more than 61.4% fewer memory accesses than state-of-the-art hashing schemes on insertions. Algorithmic co-design contributes independently of the device: reducing attention inter-bank movement from O(N^2) to O(N) and intermediate matrices from N x N to d x d, and shrinking a PIM-resident ANNS index footprint by 14.5x.

Two things hold the score at 3. The gains are per-kernel and drop sharply outside the memory-bound regime, which is why a dedicated study exists to compare digital PIM against GPUs specifically to illuminate digital PIM's limitations. And at the system level, where PIM is one device among several, the honest numbers are far smaller: dynamic operator scheduling across NPU plus PIM platforms yields geometric-mean speedups of 1.20x to 2.23x over a prefill-decode disaggregation baseline, plus 1.28x from weight layout selection. The gap between 42.8x on a chosen kernel and roughly 1.2-2.2x end-to-end is the whole assessment.

**TLDR: Reported gains over GPUs and prior PIM are large (up to 42.8x speed and 392x energy on one kernel) but kernel-specific and simulated; the same community is publishing on where digital PIM loses to GPUs.**

## Diffusion (2/5)

Adoption barriers in these sources are structural, not marginal. Hardware scarcity is stated outright. The software stack is fragmented: separate frameworks are being proposed for MoE expert partitioning, thermally aware multi-objective scheduling across heterogeneous chiplets, operator placement and weight layout across NPU plus PIM, CNN fine-tuning configuration and CPU-PIM co-execution on mobile. Each of those is a signal that the default path does not work: on mobile, sharing a memory space with the CPU creates bank conflicts and bus congestion that can erase PIM's performance and energy benefit unless commands are slotted into CPU idle windows. Non-volatile PIM adds a model-level dependency: weights must be trained noise-aware and placed on the substrate least sensitive to thermal drift to hold accuracy across the operating temperature range.

The plausible diffusion routes are the ones that avoid changing the host. A CXL-attached PIM module presents as memory over a standard interface and does not require redesigning the accelerator. Implementing the PIM primitive in commodity logic is the other route: a dually-addressable memory built from FPGA block RAM shows that a content-addressable read primitive does not require ReRAM to exist, which lowers the barrier for whoever wants to ship the associated database instruction set. Score 2: early evidence, serious obstacles.

**TLDR: No hardware to buy in the sources, no settled programming model, and host coexistence, thermal management and scheduling are all still research problems.**

## Impact (4/5)

The targets are not niche. Decoding is the phase of LLM inference that dominates latency and is the phase PIM suits; graph-based ANNS is described as a core primitive of modern AI systems and is fundamentally memory-bound; graph-based dynamic programming underpins genomics and network analytics; and data indexing sits under most storage systems. Energy is the sharper end of the claim: 392x energy efficiency over an H100 on one kernel, and on mobile the motivation is that data transfer itself is the energy cost.

The realistic scale of impact is bounded by the end-to-end numbers rather than the kernel numbers. A 1.2x to 2.2x system speedup on heterogeneous NPU plus PIM platforms is commercially significant at datacentre scale but is not a paradigm replacement for GPUs. The sources support PIM as a complement that absorbs the memory-bound fraction of a pipeline, not as a substitute for compute-bound silicon; that is still a 4, because the memory-bound fraction of AI inference is growing with context length and KV cache size.

**TLDR: If PIM lands on LLM decoding and billion-scale retrieval, it changes the cost and energy basis of the workloads that dominate current AI spend.**

## Timing Soon (2-5yr)

As of July 2026 the field describes real PIM hardware as scarce and relies on simulation for design-space exploration, and the memristive branch still lists device reliability as the gate on commercial viability. That is not a zero-to-two-year picture. What is happening now is the pre-product work: packaging strategies that sidestep DRAM process limits, schedulers assuming GPU systems with attached HBM-PIM stacks, and full-system simulators to price host-device co-execution end to end.

The earliest credible commercial windows are the two where PIM does not have to displace anything: a CXL-attached memory module serving decode, and mobile SoCs where the alternative is paying transfer energy for on-device LLMs. Content-addressable primitives are a partial exception and could arrive sooner because they can be built in commodity block RAM today, but at demonstrated array sizes of 8x512x36 bits that is a component, not a market.

**TLDR: Architecture and software work is converging on CXL-attached modules and mobile co-execution, but hardware scarcity in mid-2026 rules out near-term mainstream deployment.**

## Overrated or underrated? Fairly rated

The diagnosis is right and the community is not fooling itself about the obstacles. Memory-bound decoding, KV cache growth, MoE routing and billion-scale retrieval genuinely leave GPUs underutilised, and PIM is the structurally correct answer to that specific problem. Equally, the same authors publishing the speedups are publishing the limits: a GPU-versus-digital-PIM study aimed at exposing digital PIM's constraints, a reliability review that makes device optimisation the precondition for commercial viability, and a simulator paper that concedes hardware scarcity. That is a healthy field, correctly priced as promising and unproven.

Where readers should discount is the headline multiples. Treat 42.8x and 392x as upper bounds on a chosen kernel in simulation, and treat 1.20x-2.23x end-to-end on a heterogeneous platform as the number that will decide procurement. The specific risk to watch is not the device physics but workload drift: Sieve shows that a single generation of model-architecture change (bimodal MoE expert distributions) already invalidates the offload assumptions of state-of-the-art PIM systems. A five-year silicon cycle chasing a one-year model cycle is the core commercial hazard here.

## Prediction

Through the end of 2028, PIM will remain an optional accelerator rather than a required component of mainstream LLM serving: the majority of published PIM-for-LLM performance claims will still be simulator-derived rather than measured on fabricated PIM silicon, and reported end-to-end system speedups on heterogeneous host-plus-PIM platforms will stay below 3x.

## Evidence base

- July 2026: a full-system PIM simulator paper states that real PIM hardware remains scarce and simulation is therefore the primary way to explore the design space, spanning eleven memory technologies (seven DRAM standards, SRAM, three non-volatile memories).
- November 2025 (published June 2026): Sangam decouples logic and memory into chiplets in heterogeneous process nodes on an interposer and attaches the module over CXL, explicitly to escape the capacity loss and weak PEs of processing elements built inside DRAM chips.
- April 2026: GEN-Graph's processing-using-memory matrix tile reports 42.8x speedup and 392x energy efficiency over an NVIDIA H100 on all-pairs shortest path, using a two-tile heterogeneous 2.5D chiplet.
- July 2026: dynamic operator scheduling across heterogeneous NPU plus PIM systems achieves geometric-mean speedups of only 1.20x to 2.23x over a prefill-decode disaggregation baseline, plus 1.28x from weight layout selection.
- May 2026: Sieve documents that modern MoE models' increasingly bimodal token-to-expert distributions dramatically reduce the efficiency of state-of-the-art PIM systems for LLMs, which relied on static offload rules.
- February 2026: a review of memristor-based digital PIM (RRAM, PCM, MRAM) identifies reliability and device-level optimisation as the key open challenges for scalable, commercially viable PIM.
- May 2025: a peer-reviewed ISCAS paper implements a dually-addressable (address and content) memory in FPGA block RAM at 8x512x36 bits on a Xilinx Virtex-7, showing the content-addressable PIM primitive does not require exotic devices.

## Open questions

- Do the chiplet and CXL-attached designs survive fabrication, and how do measured end-to-end numbers compare with the simulated 1.20x-2.23x system speedups reported for NPU plus PIM platforms?
- Can a PIM device designed today remain efficient across two generations of model-architecture change, given that bimodal MoE expert distributions already break existing static offload rules?
- Does non-volatile PIM reach the device reliability and thermal-noise tolerance that the 2026 review identifies as the precondition for commercial viability, or does DRAM and SRAM near-memory logic take the whole market?
- Does any of the competing scheduling and compiler frameworks consolidate into a portable programming model, or does every PIM part continue to require its own bespoke stack?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
