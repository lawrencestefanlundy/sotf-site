---
type: concept
slug: sram
canonical_name: SRAM
aliases: []
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts: []
sources:
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2026-06-16-cim-landscape-2026]]'
- '[[2026-07-25-thoughts-on-ai-and-power]]'
- '[[2026-07-10-workload-phase-silicon-sweep]]'
- '[[2026-07-31-etched-research-sprint]]'
- '[[2026-07-10-inference-silicon-deep-research]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-07-02-semianalysis-ectc2026-advanced-packaging]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-06-04-globalfoundries-emram-22fdx-availability]]'
- '[[2026-07-07-high-bandwidth-flash-the-full-report]]'
- '[[2026-01-13-semianalysis-interconnects-beyond-copper]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-06-17-femtoai-spu-ces2026]]'
- '[[2026-07-31-inference-silicon-roster-sprint]]'
- '[[2026-05-13-semianalysis-cerebras-faster-tokens]]'
- '[[2026-06-03-tendrils-compute]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
- '[[2026-08-14-chip-tail-verification-sweep]]'
- '[[2026-06-25-ibm-debuts-worlds-first-sub-1-nanometer-chip-technology]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 94
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 13
recent_mentions:
- slug: 2026-08-14-chip-tail-verification-sweep
  title: 'Chip-comparison tail verification sweep: 37 companies re-verified, consolidation wave confirmed'
  date: '2026-08-14'
  kind: web
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-31-etched-research-sprint
  title: Etched research sprint — tape-out speed, HBM supply, customer orders (4-lane web sweep)
  date: '2026-07-31'
  kind: web
- slug: 2026-07-31-inference-silicon-roster-sprint
  title: 'Inference-silicon roster verification sprint: 10 companies for the competitive-analysis capital map'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-10-workload-phase-silicon-sweep
  title: 'Workload-phase silicon sweep: pre-training / RL / prefill / decode procurement split'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-10-inference-silicon-deep-research
  title: 'Deep research: measured vs claimed inference-silicon economics (adversarially verified, 23/25 claims confirmed)'
  date: '2026-07-10'
  kind: web
neighbors: []
---
## Physics / mechanism

Six-transistor (6T) SRAM stores one bit in a cross-coupled inverter pair (two PMOS loads, two NMOS drivers) stabilised by two access transistors. No refresh required; data persists as long as power is supplied. Read/write speed is determined by bitline precharge time, wordline drive strength, and sense amplifier offset. At 5nm/3nm nodes, bitcells shrink to ~0.021 µm²; read current ~10–50 µA, access time sub-1ns, standby leakage ~1–10 nA/cell. Density tops out around 10–15 Mb/mm². SRAM dominates on-chip cache (L1/L2/L3) and register files across CPUs, GPUs, and AI accelerators.

## Competitive landscape

DRAM is the primary competitor for larger working memory: higher density, lower cost per bit, but requires refresh and has ~10× higher latency. Embedded DRAM (eDRAM) splits the difference but adds process complexity. Non-volatile alternatives—eMRAM, ePCM, eFlash—offer zero standby power but lose on write endurance or speed. For AI inference specifically, compute-in-memory (CIM) architectures repurpose SRAM arrays as analog MAC units, directly competing with digital SRAM + separate compute.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
