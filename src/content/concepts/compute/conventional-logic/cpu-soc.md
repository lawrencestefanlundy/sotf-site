---
type: concept
slug: cpu-soc
context_concept: true
canonical_name: CPU & SoC
aliases: []
kind: technology
parent_concepts:
- compute
- conventional-logic
related_concepts: []
sources: []
frontier:
- Does architectural temporal memory safety of the CHERI-D type reduce total overhead enough, relative to the software Cornucopia Reloaded baseline and to sanitizers at 46-57% on SPEC CPU 2017, to be enabled by default in a shipping core 2026 06 18 arxiv cheri d secure and efficient inline object id for cheri temp 2026 07 22 ptsan a practical memory safety sanitizer for cc with pointe?
- Do the Granite non-leakage proofs extend from a pipelined RISC design with speculation to a wide out-of-order commercial core, or does proof effort scale faster than design complexity 2026 07 31 granite a modular methodology for foundational verification ?
- How accurate are LLM-based source-level power surrogates outside the processor family they were fitted on, given that BigPower's evidence is confined to XiangShan configurations 2026 06 15 bigpower hierarchical source level module power estimation f?
- Will NPU software stacks close the up-to-10x framework-induced performance gap and take over the decode phase, or will heterogeneous CPU-plus-NPU scheduling remain the design point 2026 07 08 is your npu ready for llms dissecting the hidden efficiency ?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 16
last_reorg_date: '2026-05-14'
scorecard:
  viability: 5
  drivers: 4
  novelty: 2
  diffusion: 5
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2022-06-15-owner-of-uk-chip-designer-arm-may-float-some-of-firms-shares
  title: Owner of UK chip designer Arm may float some of firm’s shares in London - The Guardian
  date: '2022-06-15'
  kind: web
- slug: 2019-05-22-uk-chip-designer-arm-suspends-business-with-huawei-to-comply
  title: UK chip designer ARM suspends business with Huawei to comply with new U.S. rules - ET Telecom
  date: '2019-05-22'
  kind: web
neighbors: []
---
**The general-purpose CPU and the system-on-chip that surrounds it remain the default compute substrate, and the live research frontier has shifted from raw core performance to on-die specialisation, energy per instruction fetch, and architectural security guarantees.**

## Summary

A CPU is a general-purpose instruction processor: it fetches encoded instructions, decodes them, and executes them against registers and memory, with pipelining, branch prediction and caches used to hide latency. A system-on-chip (SoC) is the integrated die around it, combining one or more CPU cores with memory controllers, interconnect, accelerators (GPU, NPU, crypto, DSP) and I/O. In current practice the two are inseparable as a design object: the AIA chip pairs a RISC-V host processor for chip-to-chip communication with a 2D mesh of 16 custom RISC-V cores carrying bespoke sampling instructions, fabricated on Intel's 16 nm process, and Apple's M5 generation exposes per-GPU-core matrix units through a tensor API rather than scaling the CPU.

The parameters that decide a modern CPU/SoC design are no longer mainly clock rate and IPC. They are: energy per useful operation (instruction fetch from SRAM alone accounts for over 40% of energy in an embedded RISC-V baseline); which workloads should leave the core entirely (MCMC sampling executes inefficiently on conventional CPU/GPU platforms, and post-quantum signature schemes are effectively unusable in software on a Cortex-M4, with SPHINCS+ impractical and the reference Dilithium implementation failing to run at all); and what security properties the architecture can guarantee rather than bolt on in software.

The security thread is the most active in this source set. Conventional processors expose code and data as plaintext throughout execution; memory safety errors remain the dominant source of severe vulnerabilities in C and C++; and micro-architectural artefacts leak secrets through power and timing channels. The response is architectural: capability hardware with inline object IDs for temporal memory safety, instruction-level authenticated encryption in the fetch path, and ISA-level leakage contracts proved against RTL.

Underneath sits a design-and-verification economy that is itself changing. Symbolic execution over RTL Verilog found assertion violations in five open-source designs including an SoC and a CPU; lexical static analysis on RTL issues a correct security warning up to 60.8% of the time against 17.5% for prior work; and LLM-based surrogate models now estimate module-level CPU power directly from source-level design information without simulation at inference time, demonstrated on the open-source XiangShan processor family.

## Viability (5/5)

Viability for the category is settled by construction. The sources contain a 16 nm multi-core RISC-V SoC fabricated on an Intel process, loop-cache designs synthesised on GlobalFoundries 22 nm FDX+ at 0.5 V and 250 MHz, a shipping Apple M5 Pro benchmarked across fifteen model configurations, and a commodity x86-64 feature (Intel Linear Address Masking) used to remove software compatibility work in hardware.

The honest caveat is that viability of the *increments* varies. CHERI-D was evaluated in simulation and in hardware, SEAM-V is an architecture paper, and memristor-based reservoir computing for branch prediction is simulation only, with the authors themselves reporting that the framework needs further refinement to address shortfalls. Reversible spin-based logic is a proposal with simulations, not a device. So: the platform is a 5, individual roadmap items range from 2 to 4.

**TLDR: Not a question: these are fabricated, measured, shipping devices.**

## Drivers (4/5)

On the demand side the pull is specific and datable. Deploying LLMs on mobile improves privacy and reduces latency but is severely bottlenecked by hardware inefficiency; embedded RISC-V cores are increasingly deployed for on-device AI inference where energy is the primary constraint; the transition to post-quantum cryptography is forcing hardware acceleration onto resource-constrained parts because software-only PQC does not fit; memory safety is the dominant severe-vulnerability class; and rising data-centre and AI energy demand is reviving interest in fundamentally lower-dissipation logic. There is also a novel demand vector: cryo-CMOS as the interface layer for quantum computing, which requires accurate dynamic device models.

On the supply side, open-source cores lower the cost of experimentation: XiangShan for power modelling, NEORV32 for loop caches, RISC-V for custom sampling instructions, instruction-level encryption and logic locking. Verification and power estimation cost, historically the gate on how many design variants a team can explore, is being attacked directly: piecewise composition cut paths explored by an order of magnitude and runtime by 97%, and LLM surrogates remove simulation from the power-estimation inner loop.

**TLDR: Demand from on-device AI, PQC migration and memory-safety mandates; supply from open RISC-V cores plus cheaper verification and power modelling.**

## Novelty (2/5)

As a category, the conventional CPU/SoC is the incumbent, so the relevant question is what the increments beat and by how much. Measured gains in these sources are real but bounded: a dynamic loop cache cuts instruction fetches 48.3% and total energy 21.5%, a static software-managed variant reaches 83.3% fetch reduction and 35.5% energy reduction on a LeNet-5 workload; a hardware NTT accelerator on a Zynq-7000 moves Dilithium from not-running to millisecond-level key and signature generation, which is a categorical change but achieved by leaving the CPU; homomorphic-encryption-based logic locking costs 6.0% LUTs and 6.9% registers with a 2.6 us unlock. Software-side memory safety still carries 57.2% geomean overhead on SPEC CPU 2017 on x86-64, falling to 46.4% with Intel LAM, which is exactly the argument for architectural support.

Where the CPU is genuinely better than the alternative, the sources are precise: on mobile, NPUs excel at compute-bound prefilling while CPUs outperform all other backends in memory-bound decoding, because NPUs prefer large fixed-shape workloads and decoding is small-kernel and dynamic. Where it is worse, that is also precise: MCMC sampling is inefficient on conventional CPU/GPU platforms, motivating a dedicated 16-core accelerator SoC, and matrix-heavy LLM prefill on Apple silicon is up to 6.4x faster through dedicated on-GPU neural accelerators than through llama.cpp. The truly novel physics in this set, reversible spin logic claiming gate energy five to eight orders of magnitude below a room-temperature CMOS Toffoli, is a proposal that would displace CMOS rather than improve it.

**TLDR: The CPU/SoC is the baseline everything else is measured against; current increments are single-digit to roughly 2x, not step changes.**

## Diffusion (5/5)

Diffusion of the category needs no argument: the sources treat CPU and SoC as the assumed target across mobile inference, edge AI, embedded cryptography, and quantum control electronics.

The barriers apply to the extensions. Three recur. First, performance tax: pointer-based memory safety on stock hardware still costs tens of percent, and CHERI's current state-of-the-art temporal safety solution is software-based, providing only use-after-reallocation rather than use-after-free protection and paying for delayed reallocation and revocation. Second, toolchain and micro-architecture coupling: existing instruction-level encryption proposals depend on specific micro-architectures or non-standard ciphers, which is why SABLE explicitly aims to stay micro-architecture agnostic and compatible with the standard RISC-V toolchain with only post-processing of compiled ELF binaries. Third, software fragmentation on the accelerator side: framework-induced performance gaps reach up to 10x on NPUs due to divergent offloading and quantization strategies, and best-in-class throughput on M5 required hand-written Metal 4 tensor kernels. Silicon capability diffuses faster than the software that exploits it.

**TLDR: The platform is already universal; the open question is diffusion of specific extensions, which faces real overhead and toolchain barriers.**

## Impact (4/5)

Two impact channels are well evidenced. Energy: instruction fetch is over 40% of energy in an embedded baseline, so datapath-level changes deliver 21.5% to 35.5% total energy reduction on a real inference workload; multiplied across edge deployments this is a first-order sustainability and battery-life lever. Security: if temporal memory safety, non-leakage and instruction confidentiality can be guaranteed at the architecture level, an entire vulnerability class stops being a per-application software cost. Granite proves that the cycle-by-cycle timing of a pipelined RISC design with speculation, precise interrupts and I/O is determined solely by ISA-contract observables, ruling out leakage through known and unknown timing channels for constant-time programs. That is a strong statement about what hardware can promise software.

The reason this is a 4 and not a 5 is scope of demonstration. The verification and security results are on RISC designs, open-source SoCs and simulation or FPGA prototypes; none of the sources shows these guarantees at high-performance commercial core scale, and the highest-value AI compute is visibly migrating off the CPU to on-die matrix units. The SoC keeps the value; the general-purpose core's share of it is contested.

**TLDR: The substrate everything else runs on, and the place where memory-safety and side-channel classes can be closed rather than mitigated.**

## Timing Now (0-2yr)

Nothing here is speculative at the platform level. Commercial silicon with on-die neural accelerators is benchmarked on hardware, a custom 16 nm RISC-V SoC exists, and commodity address-masking features are already exploitable by sanitizers.

The increments split by band. Design-flow tooling (power surrogates, RTL symbolic execution, lexical CWE detection, pre-silicon side-channel root-cause analysis) is adoptable now because it slots into existing flows. Architectural security extensions require ISA and toolchain commitment and therefore run on a multi-year cycle. Post-CMOS reversible logic is a separate, much longer horizon: it is a proposal with simulated error landscapes and a cryogenic operating point.

**TLDR: The platform ships today; the security and energy increments in these sources are at prototype-to-early-silicon stage.**

## Overrated or underrated? Fairly rated

The consensus that the CPU has stopped being where AI performance comes from is correct and the sources support it: matrix work moves to dedicated on-die units for up to 6.4x prompt-processing gains, and workloads that resist parallelisation get their own SoC rather than a faster core. What is underweighted is that the CPU still wins the memory-bound half of LLM inference, beating GPU and NPU backends on decoding on mobile, so the practical answer is heterogeneous scheduling within one SoC, not replacement.

The part of this field that deserves more attention from investors than it gets is the security and verification layer. Software mitigations are still expensive (tens of percent on SPEC CPU 2017), the leading capability architecture lacks intrinsic temporal-safety support, and formal non-leakage against ISA contracts has only just been demonstrated on a pipelined RISC design. Whoever makes architectural memory safety and provable non-leakage cheap enough to enable by default captures a durable position in every SoC, and that is a CPU-and-SoC problem, not an accelerator problem.

## Prediction

By July 2028, published cross-backend measurements of on-device LLM inference will still show the CPU as the preferred backend for the memory-bound decode phase in the majority of configurations tested, with the NPU preferred for prefill, rather than a single backend winning both.

## Evidence base

- 2026-06-16: AIA, a 16-core custom RISC-V SoC with a RISC-V host processor, fabricated on Intel 16 nm because MCMC sampling executes inefficiently on conventional CPU/GPU platforms.
- 2026-07-08: cross-layer measurement across five frameworks and three backends finds NPUs best for compute-bound prefill and CPUs best of all backends for memory-bound decode, with framework-induced gaps up to 10x on NPUs.
- 2026-07-28: instruction fetch from SRAM is over 40% of energy in a baseline embedded RISC-V core; loop caches cut fetches 48.3% or 83.3% and total energy 21.5% or 35.5% on GlobalFoundries 22 nm FDX+ at 0.5 V, 250 MHz.
- 2026-07-22: PTSan reports 57.2% geomean overhead on SPEC CPU 2017 on x86-64, falling to 46.4% with Intel Linear Address Masking, illustrating the cost of software-only memory safety.
- 2026-06-16: SPHINCS+ is practically unusable and the reference Dilithium implementation fails to run on an STM32F407G Cortex-M4; an FPGA NTT accelerator on a Zynq-7000 ZedBoard brings key and signature generation to millisecond level.
- 2026-07-22: piecewise-composition symbolic execution over RTL Verilog reduces paths explored by an order of magnitude and runtime by 97%, finding assertion violations in five open-source designs including an SoC and a CPU.

## Open questions

- Does architectural temporal memory safety of the CHERI-D type reduce total overhead enough, relative to the software Cornucopia Reloaded baseline and to sanitizers at 46-57% on SPEC CPU 2017, to be enabled by default in a shipping core?
- Do the Granite non-leakage proofs extend from a pipelined RISC design with speculation to a wide out-of-order commercial core, or does proof effort scale faster than design complexity?
- How accurate are LLM-based source-level power surrogates outside the processor family they were fitted on, given that BigPower's evidence is confined to XiangShan configurations?
- Will NPU software stacks close the up-to-10x framework-induced performance gap and take over the decode phase, or will heterogeneous CPU-plus-NPU scheduling remain the design point?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
