---
type: concept
slug: risc-v
canonical_name: RISC-V
aliases: []
kind: technology
parent_concepts:
- compute
- conventional-logic
related_concepts: []
sources:
- '[[2026-07-03-thats-a-learning-curve-mate-not-rsi]]'
- '[[2023-08-18-e11-in-conversation-with-lux-capital]]'
- '[[2026-07-17-the-once-and-future-kimi]]'
- '[[2026-02-13-four-things-friday]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2025-07-20-risc-v-open-silicon-share-shd-group-risc-v-market-analysis]]'
- '[[2024-eu-chips-act-final-text]]'
- '[[2026-01-23-risc-v-open-silicon-share-risc-v-hits-25-design-share-as]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2025-07-23-nvidia-cuda-on-risc-v]]'
- '[[2026-06-17-qualcomm-tenstorrent-talks]]'
- '[[2026-04-09-sifive-series-g]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2025-12-18-risc-v-25pct-penetration]]'
- '[[2026-02-09-semianalysis-datacenter-cpu-2026]]'
- '[[2025-10-09-risc-v-open-silicon-share-risc-v-summit-2025-keynote-risc-v]]'
- '[[2026-05-21-semianalysis-eda-market-primer]]'
scorecard:
  viability: 4
  drivers: 3
  novelty: 3
  diffusion: null
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 100
sources_7d: 2
sources_30d: 9
recent_mentions:
- slug: 2026-07-17-the-once-and-future-kimi
  title: The Once and Future Kimi
  date: '2026-07-17'
  kind: substack
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-03-thats-a-learning-curve-mate-not-rsi
  title: That’s a learning curve mate, not RSI
  date: '2026-07-03'
  kind: substack
- slug: 2026-06-17-qualcomm-tenstorrent-talks
  title: Qualcomm in advanced talks to acquire Tenstorrent at $8-10B (reported)
  date: '2026-06-17'
  kind: web
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-05-21-semianalysis-eda-market-primer
  title: EDA Market Primer - Market Dynamics, Cadence, Synopsys, Siemens, China EDA Rise
  date: '2026-05-21'
  kind: web
- slug: 2026-04-09-sifive-series-g
  title: SiFive raises $400M Series G at $3.65B valuation
  date: '2026-04-09'
  kind: web
- slug: 2026-02-13-four-things-friday
  title: Four Things Friday
  date: '2026-02-13'
  kind: substack
neighbors: []
---
**RISC-V is an open, modular instruction set architecture that lets designers strip out, extend or specialise the CPU instruction set for a given workload, and the research literature now shows it fabricated in production nodes (Intel 16 nm, 12 nm FinFET chiplets) as the programmable substrate inside domain-specific accelerators rather than as a drop-in replacement for proprietary high-performance CPUs.**

## Summary

RISC-V is an instruction set architecture (ISA): the contract between compiled software and silicon. Unlike proprietary ISAs, it is published openly and structured as a small mandatory base plus optional standard extensions, and it permits vendors to add their own instructions. The sources here show all three of those properties being exercised. Standard extensions appear as named building blocks: `RV32IMC` for a constrained edge SoC, `RV64GC` for a general-purpose core, and `Zfh`/`Zvfh` for scalar and vector float16 arithmetic. The Vector Extension (RVV) provides a vector-length-agnostic programming model, so the same binary runs across implementations with different vector register widths.

Modularity cuts both ways. One paper reduces a baseline `RV32IM` core to a minimal instruction subset for Tsetlin Machine inference, using instruction profiling to decide what to delete, and keeps programmability while simplifying the datapath and control path. Others go the other way and add custom instructions: an approximate logarithmic CNN unit behind a custom extension, and custom Knuth-Yao sampling and interpolation instructions inside 16 specialised cores on a 2D mesh. Because the RTL of several cores is open, a second layer of reuse appears: Sargantana cores dropped into the OpenPiton memory hierarchy, the NEORV32 core used as a testbed for loop caches, and open cores used as the standard vehicle for security and verification research.

The parameters that decide RISC-V's fate are not in the ISA document. They are: whether open implementations close the performance gap to proprietary designs at the high end, which the leading open-chiplet roadmap explicitly frames as an open goal rather than an achievement; whether the efficiency penalty of a general-purpose ISA against fixed-function accelerators can be closed by extension design rather than paid in energy; and whether the toolchain absorbs custom extensions without fragmenting, a constraint one design explicitly respects by remaining compatible with the standard RISC-V toolchain with only post-processing of compiled ELF binaries.

## Viability (4/5)

The reservation is at the top of the range. The open-chiplet roadmap positions its 7 nm quad-chiplet system as a concept architecture and states the aim of closing the performance gap to proprietary designs, so parity at the high end is an objective, not a demonstrated result. The same roadmap notes that openness does not yet extend through simulation, EDA, PDKs and off-die PHYs, which is where the practical friction sits. Hence 4 rather than 5: the ISA and the embedded-to-mid-range implementations plainly work; the flagship-performance claim does not yet stand on demonstrated silicon.

**TLDR: Silicon-proven in commercial nodes, boots Linux at 64 cores, with quantified area and energy numbers rather than projections.**

## Drivers (3/5)

On the demand side the sources are consistent about why designers reach for RISC-V. Edge AI inference is described as running under strict energy, performance, security and privacy constraints, with instruction fetch from SRAM accounting for over 40% of total core energy in one baseline, making microarchitectural surgery worthwhile. Workloads that map badly onto CPUs and GPUs, such as MCMC sampling for probabilistic models, create demand for custom instructions rather than faster general-purpose cores. Manufacturing economics push the same way: monolithic SoCs at 360 mm^2 on advanced nodes are cited at yields below 16%, motivating chiplet decomposition around a RISC-V CPU chiplet.

On the supply side the driver is resource scarcity in the research base. Academic projects face scalability challenges due to limited resources, which is given as the explicit reason for open-source, reusable multicore frameworks, and pre-silicon validation of large multicore designs already exceeds single-FPGA capacity, driving investment in shared open emulation platforms. What the sources do not contain is any commercial demand signal: no shipment volumes, design-win counts, licensing figures or customer names. The score reflects well-evidenced technical pull with an evidentiary hole where market demand should be.

**TLDR: Clear technical pull from edge-AI energy budgets and chiplet yield economics; the sources contain no market or commercial-demand data at all.**

## Novelty (3/5)

The comparison that matters is stated bluntly in one source: domain-specific accelerators give significantly higher performance and energy efficiency for DNN workloads than general-purpose processors but lack adaptability, whereas general-purpose ISA-based solutions such as RISC-V-based accelerators improve programmability at the cost of efficiency. RISC-V's distinctive contribution is that this tradeoff can be tuned per design rather than accepted. Subsetting a core to a workload retains programmability while reducing energy; standardised extensions deliver about 50% memory footprint reduction for on-device training versus float32 with minimal accuracy loss and negligible area cost; and microarchitectural additions inside the same ISA gave 48.3% fewer instruction fetches and 21.5% total energy reduction dynamically, or 83.3% and 35.5% with a software-managed static loop cache.

Against the alternatives, the openness itself is the second axis of novelty, and the sources show it being used for things a closed ISA makes awkward: microarchitecture-agnostic instruction-level authenticated encryption compatible with the standard toolchain, macro-cell-level information flow tracking for pre-silicon power side-channel root-cause analysis inside real processor RTL, and logic locking inserted into the privilege-switching path at 6.0% LUT and 6.9% register overhead. None of this is a step change in compute per watt on its own, which caps the score at 3.

**TLDR: The ISA is not new engineering; the measurable advantage is modularity plus open RTL, and it is paid for in efficiency against fixed-function accelerators.**

## Diffusion (unscored)

An honest reading of this evidence base cannot score diffusion. Every source is an arXiv architecture or security paper. There is real diffusion visible inside the research community: independent groups build on shared open cores and frameworks including OpenPiton and Sargantana, NEORV32 and the AIfES embedded training framework, and multiple projects commit to open-source release of their platforms. Access to commercial foundry capacity is also evidenced by fabrication in Intel 16 nm and GlobalFoundries 22 nm FDX+.

What is absent is everything needed to judge adoption: unit volumes, product design wins, software ecosystem coverage beyond compiler toolchain compatibility, and any comparison of RISC-V's installed base against incumbent ISAs. The stated barriers that can be read from the sources are the incompleteness of the open stack outside logic RTL, specifically simulation, EDA, PDKs and off-die PHYs, and the risk implicit in every custom-extension paper here that per-design instruction sets fragment the software story. Those are directional, not sufficient for a number.

**TLDR: The sources are entirely research artefacts and contain no commercial adoption, market share or deployment data.**

## Impact (3/5)

Where the sources quantify impact, it is meaningful but bounded to the design in hand. Energy reductions of 21.5% to 35.5% on a CNN inference workload from instruction-fetch caching, roughly halved memory footprint for on-device training, 3.1x average speedup at four cores with 9.3x on a vector addition benchmark from new core features, and a chiplet route around sub-16% monolithic yields at 360 mm^2. Aggregate across the edge-AI and accelerator-host category and that is a material efficiency lever, and enabling capability at the edge, such as reasoning and decision-making under MCMC that runs inefficiently on CPUs and GPUs, is a qualitative gain rather than a percentage.

The larger claim usually made for RISC-V, that an open ISA restructures the semiconductor industry's licensing and supply economics, is simply outside this evidence set. The one source that gestures at the frontier states the gap to proprietary designs as something still to be closed. A 3 records demonstrated, repeatable, moderate value with the upside unproven here.

**TLDR: Per-design gains are real and quantified in the tens of percent; the systemic value of an open ISA is not addressable from these sources.**

## Timing Now (0-2yr)

For its demonstrated role, the deeply embedded and accelerator-host niche, RISC-V is a present-tense technology in these sources rather than a forecast. Chips exist in Intel 16 nm and 12 nm FinFET chiplets, 64-core designs boot Linux under emulation, and the toolchain is treated as a stable dependency that new designs must not break.

The part that is not now is the top of the market. The open chiplet roadmap moves from silicon-proven Occamy through a mesh-NoC Ramora to Ogopogo, a 7 nm quad-chiplet concept architecture, and lists openness in simulation, EDA, PDKs and off-die PHYs as avenues to explore. Concept plus an incomplete supporting stack reads as a multi-year path, but the sources do not date those milestones, so any tighter timing on HPC-class parity would be invention.

**TLDR: Already in fabricated silicon and shared research infrastructure; the high-performance chiplet ambition sits further out.**

## Overrated or underrated? Fairly rated

Read the corpus by what RISC-V is used for and the pattern is consistent: in almost every paper here it is the programmable control and host layer around specialised hardware, not the performance engine itself. It is the host managing chip-to-chip communication for a sampling accelerator, the SoC around an approximate CNN unit, the substrate for security and verification research, and the standard test article for HLS pipeline work. That is a genuinely valuable position and the evidence for it is solid: it is now the default open substrate for architecture research and for custom silicon that needs a compiler.

The two directions of mispricing cancel out. Sceptics who treat RISC-V as a lab curiosity are contradicted by fabricated chips in commercial nodes and measured overheads in the single-digit percent. Enthusiasts who treat it as an imminent replacement for proprietary CPUs at the high end are contradicted by the leading open-chiplet group's own framing of an unclosed performance gap and by the admitted incompleteness of the stack outside logic RTL. The main unresolved risk visible here is fragmentation: this many one-off custom extensions is a strength for silicon efficiency and a liability for software portability, and the sources measure the former but not the latter.

## Prediction

By 31 December 2028, no open-source 7 nm quad-chiplet RISC-V system in the Ogopogo line described in will have been reported as silicon-proven in a peer-reviewed or arXiv publication.

## Evidence base

- Occamy, presented on 19 November 2025, is described as the first open, silicon-proven dual-chiplet RISC-V manycore in 12 nm FinFET, with a roadmap to a 7 nm quad-chiplet concept aimed at closing the gap to proprietary designs.
- AIA, published 16 June 2026, is a RISC-V host plus a 2D mesh of 16 custom RISC-V cores with bespoke Knuth-Yao sampling instructions, fabricated in Intel's 16 nm process.
- Loop cache work synthesised on GlobalFoundries 22 nm FDX+ at 0.5 V and 250 MHz reduced instruction fetches by 48.3% and total energy by 21.5% (dynamic), or 83.3% and 35.5% (static), against a baseline where instruction fetch was over 40% of core energy.
- Standard Zfh float16 support added +1.15% LUT6 and +0.05% FF to an RV64GC out-of-order FPGA softcore at 175 MHz while cutting on-device training memory footprint by about 50% versus float32.
- EMiX, published 29 April 2026, distributed a 64-core RISC-V architecture across eight Alveo U55c FPGAs and demonstrated full-system execution including Linux boot without fundamental RTL redesign.
- A chiplet RISC-V SoC proposal dated 22 September 2025 cites monolithic yields below 16% at 360 mm^2 advanced nodes as its motivation, integrating a 7 nm RISC-V CPU chiplet with dual 5 nm 15 TOPS INT8 accelerators and 16 GB HBM3 on a 30 mm x 30 mm interposer.
- A general-purpose-versus-specialised framing is stated directly on 7 July 2026: RISC-V-based accelerators improve programmability at the cost of efficiency relative to domain-specific hardware.

## Open questions

- Does the proliferation of per-design custom instruction extensions seen across these papers fragment the software toolchain, or do designs continue to converge on standard extensions such as Zfh, Zvfh and RVV plus minimally invasive post-processing?
- Can decoupled RVV implementations sustain throughput on short-vector, loop-tail and control-heavy phases well enough to compete with GPUs on data-parallel workloads, rather than only with scalar cores?
- Will openness actually extend beyond logic RTL into simulation, EDA, PDKs and off-die PHYs, which the chiplet roadmap identifies as the remaining closed layers?
- What are the commercial volumes and design wins? None of the available sources contain shipment, revenue or market-share data, so the adoption case is currently unassessable.

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
