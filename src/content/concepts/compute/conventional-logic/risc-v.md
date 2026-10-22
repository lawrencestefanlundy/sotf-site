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
- '[[2026-10-16-uneec-site]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2025-07-23-nvidia-cuda-on-risc-v]]'
- '[[2026-06-17-qualcomm-tenstorrent-talks]]'
- '[[2026-04-09-sifive-series-g]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2025-12-18-risc-v-25pct-penetration]]'
- '[[2026-02-09-semianalysis-datacenter-cpu-2026]]'
- '[[2025-10-09-risc-v-open-silicon-share-risc-v-summit-2025-keynote-risc-v]]'
- '[[2026-10-12-cnt-electronics-market-research]]'
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
mention_count: 130
sources_7d: 5
sources_30d: 15
recent_mentions:
- slug: 2026-10-16-uneec-site
  title: UNEEC Systems GmbH — company site (uneec.eu), incl. imprint
  date: '2026-10-16'
  kind: web
- slug: 2026-10-12-cnt-electronics-market-research
  title: 'Carbon nanotube electronics: market, cohort and M&A research (web sweep, 82 sources)'
  date: '2026-10-12'
  kind: web
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
neighbors: []
---
**RISC-V is an open, modular instruction set architecture that lets designers strip out, extend or specialise the CPU instruction set for a given workload, and the research literature now shows it fabricated in production nodes (Intel 16 nm, 12 nm FinFET chiplets) as the programmable substrate inside domain-specific accelerators rather than as a drop-in replacement for proprietary high-performance CPUs.**

## Summary

RISC-V is an instruction set architecture (ISA): the contract between compiled software and silicon. Unlike proprietary ISAs, it is published openly and structured as a small mandatory base plus optional standard extensions, and it permits vendors to add their own instructions. The sources here show all three of those properties being exercised. Standard extensions appear as named building blocks: `RV32IMC` for a constrained edge SoC, `RV64GC` for a general-purpose core, and `Zfh`/`Zvfh` for scalar and vector float16 arithmetic. The Vector Extension (RVV) provides a vector-length-agnostic programming model, so the same binary runs across implementations with different vector register widths.

## Viability (4/5)

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

**TLDR: Already in fabricated silicon and shared research infrastructure; the high-performance chiplet ambition sits further out.**

## Overrated or underrated? Fairly rated

Read the corpus by what RISC-V is used for and the pattern is consistent: in almost every paper here it is the programmable control and host layer around specialised hardware, not the performance engine itself. It is the host managing chip-to-chip communication for a sampling accelerator, the SoC around an approximate CNN unit, the substrate for security and verification research, and the standard test article for HLS pipeline work. That is a genuinely valuable position and the evidence for it is solid: it is now the default open substrate for architecture research and for custom silicon that needs a compiler.

The two directions of mispricing cancel out. Sceptics who treat RISC-V as a lab curiosity are contradicted by fabricated chips in commercial nodes and measured overheads in the single-digit percent. Enthusiasts who treat it as an imminent replacement for proprietary CPUs at the high end are contradicted by the leading open-chiplet group's own framing of an unclosed performance gap and by the admitted incompleteness of the stack outside logic RTL. The main unresolved risk visible here is fragmentation: this many one-off custom extensions is a strength for silicon efficiency and a liability for software portability, and the sources measure the former but not the latter.

## Prediction

By 31 December 2028, no open-source 7 nm quad-chiplet RISC-V system in the Ogopogo line described in will have been reported as silicon-proven in a peer-reviewed or arXiv publication.

## Evidence base

## Open questions

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
