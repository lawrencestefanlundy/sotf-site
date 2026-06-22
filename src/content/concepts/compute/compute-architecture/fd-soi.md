---
type: concept
slug: fd-soi
canonical_name: FD-SOI
aliases:
- fdsoi
kind: technology
parent_concepts:
- compute
- compute-architecture
related_concepts: []
sources:
- '[[2024-eu-chips-act-final-text]]'
- '[[2026-06-04-globalfoundries-emram-22fdx-availability]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-05-21-gf-quantum-technology-solutions]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 14
last_reorg_date: '2026-05-13'
sources_7d: 3
sources_30d: 7
recent_mentions:
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-06-04-globalfoundries-emram-22fdx-availability
  title: GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform
  date: '2026-06-04'
  kind: web
- slug: 2026-05-21-gf-quantum-technology-solutions
  title: GlobalFoundries launches Quantum Technology Solutions to scale U.S. quantum manufacturing
  date: '2026-05-21'
  kind: web
- slug: 2024-eu-chips-act-final-text
  title: European Chips Act — Regulation (EU) 2023/1781
  date: '2023-09-20'
  kind: web
neighbors: []
---
## Physics / mechanism

Fully Depleted Silicon-on-Insulator is a planar CMOS variant where a thin Si device layer (~5–7 nm) sits atop a buried oxide (BOX, ~25 nm), fully depleting the channel without doping. Electrostatic control comes from gate geometry and optional back-bias voltage applied through the substrate, not from impurity concentration. This eliminates random dopant fluctuation, the dominant variability source below 28 nm. Key metrics: 28FD-SOI from STMicroelectronics/GlobalFoundries delivers ~30% power reduction vs. bulk 28 nm at iso-performance, back-bias tunability of ±300 mV shifts Vt dynamically, and the process supports RF/mmWave up to ~300 GHz fT. 22FDX (GF) extends this to 22 nm with 12 nm BOX.

## Competitive landscape

| Approach | Node floor | Back-bias | RF suitability | Key risk |
|---|---|---|---|---|
| FD-SOI | 12 nm (R&D) | Yes, wide range | Excellent | Wafer cost premium ~15–20% |
| FinFET (bulk) | 3 nm production | Limited | Moderate | Parasitic capacitance, cost |
| Gate-all-around | 2 nm (Samsung/TSMC) | Possible | TBD at volume | Process maturity |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
