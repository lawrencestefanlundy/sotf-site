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
- '[[2023-08-18-e11-in-conversation-with-lux-capital]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2024-eu-chips-act-final-text]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-02-09-semianalysis-datacenter-cpu-2026]]'
- '[[2026-05-21-semianalysis-eda-market-primer]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 47
last_reorg_date: '2026-05-14'
sources_7d: 4
sources_30d: 11
recent_mentions:
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-05-21-semianalysis-eda-market-primer
  title: EDA Market Primer - Market Dynamics, Cadence, Synopsys, Siemens, China EDA Rise
  date: '2026-05-21'
  kind: web
- slug: 2026-02-09-semianalysis-datacenter-cpu-2026
  title: 'CPUs are Back: The Datacenter CPU Landscape in 2026'
  date: '2026-02-09'
  kind: web
- slug: 2026-01-22-ai-chips-computeram-and-the-future
  title: 'AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara'
  date: '2026-01-22'
  kind: substack
- slug: 2024-eu-chips-act-final-text
  title: European Chips Act — Regulation (EU) 2023/1781
  date: '2023-09-20'
  kind: web
- slug: 2023-08-18-e11-in-conversation-with-lux-capital
  title: '☎️ E11: In Conversation with Lux Capital on the State of the Future'
  date: '2023-08-18'
  kind: substack
neighbors: []
---
## Physics / mechanism

RISC-V is an open-standard instruction set architecture (ISA) released under royalty-free licenses, originally from UC Berkeley (2010). Unlike proprietary ISAs, any entity can implement RISC-V cores without licensing fees. The base integer ISA is fixed; optional extensions (M, A, F, D, C, V for vector, etc.) are modular. Implementations span 32-bit microcontrollers to 64-bit server-class cores. Current SOTA: SiFive P870 at ~4 GHz on TSMC N3, competitive with Arm Cortex-A series on SPECint. Vector extension (RVV 1.0) enables AI/ML inference acceleration. Embedded cores (e.g., CV32E40P) run at sub-milliwatt budgets, dominant in IoT and secure enclaves.

## Competitive landscape

Arm is the primary incumbent — same application domains, vastly larger software ecosystem, stronger per-core performance at advanced nodes today. x86 competes at server/desktop but is irrelevant in embedded. MIPS and PowerPC are legacy residuals. The real competitive axis is not ISA performance but ecosystem maturity and vendor lock-in tolerance.

| ISA | Licensing | Ecosystem maturity | Edge/IoT traction |
|---|---|---|---|
| Arm | Royalty-bearing | Very high | Dominant |
| RISC-V | Free/open | Growing fast | Strong, accelerating |
| x86 | Proprietary | High (server/PC) | Negligible |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
