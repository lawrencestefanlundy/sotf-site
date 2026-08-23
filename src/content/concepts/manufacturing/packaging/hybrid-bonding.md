---
type: concept
slug: hybrid-bonding
canonical_name: Hybrid Bonding (Cu-Cu)
aliases: []
kind: technology
parent_concepts:
- manufacturing
- packaging
related_concepts: []
sources:
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2026-06-22-sintered-metal-die-attach-landscape]]'
- '[[2026-06-01-hbm-state-of-play]]'
- '[[2026-07-02-semianalysis-ectc2026-advanced-packaging]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
- '[[2026-06-22-tim-approaches-full-sweep]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 14
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-sintered-metal-die-attach-landscape
  title: Sintered-silver / sintered-copper die-attach landscape — physics, incumbents, AI-migration question (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-01-hbm-state-of-play
  title: HBM state of play (mid-2026) — technology, supercycle, three-supplier standing
  date: '2026-06-01'
  kind: web
- slug: 2026-04-15-semianalysis-isscc-2026
  title: 'ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More'
  date: '2026-04-15'
  kind: web
neighbors: []
---
## Physics / mechanism

Direct copper-to-copper bonding achieved by planarising dielectric (SiO₂ or SiCN) and Cu pad surfaces to sub-nanometre roughness (Ra < 0.5 nm), then annealing at 200–400 °C. At temperature, Cu atoms interdiffuse across the interface, eliminating the bond line entirely. Electrical resistance across the joint is near-bulk Cu; pitch scalability reaches <1 µm today (TSMC SoIC at ~9 µm pitch in HVM, research demos at 1–3 µm). Bandwidth density scales inversely with pitch squared—orders of magnitude beyond flip-chip bumps. Dielectric fusion bonds simultaneously, providing mechanical integrity and hermetic sealing. Key process parameters: surface activation (plasma or CMP), particle control (sub-10 nm), and anneal ambient.

## Competitive landscape

| Approach | Min pitch | Electrical R | Thermal budget |
|---|---|---|---|
| Hybrid bonding (Cu-Cu) | <1 µm (lab), ~9 µm (HVM) | Near-bulk Cu | 200–400 °C |
| Micro-bump (SnAg) | ~20–40 µm | Higher (intermetallic) | ~260 °C reflow |
| TCB (Cu pillar) | ~10–20 µm | Moderate | ~250–300 °C |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
