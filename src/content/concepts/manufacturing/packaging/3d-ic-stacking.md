---
type: concept
slug: 3d-ic-stacking
canonical_name: 3D IC Stacking
aliases: []
kind: technology
parent_concepts:
- manufacturing
- packaging
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

3D IC stacking integrates multiple die vertically using through-silicon vias (TSVs), hybrid bonding, or micro-bumps, replacing lateral interconnects with vertical ones. Key parameters: TSV pitch (currently ~1–5 µm in leading HVM), hybrid bonding pitch down to ~1 µm (TSMC SoIC, Intel Foveros), inter-die bandwidth density exceeding 1 TB/s/mm², and z-height constraints (die thinned to 30–50 µm). Configurations include die-to-die (D2D), die-to-wafer (D2W), and wafer-to-wafer (W2W). W2W maximizes yield only when die sizes match. HBM stacks 8–16 DRAM die via TSVs; CoWoS and EMIB handle heterogeneous integration at package level. Primary bottleneck is thermal dissipation and yield stacking.

## Competitive landscape

| Approach | Pitch | Bandwidth density | Complexity |
|---|---|---|---|
| Micro-bump flip-chip | 40–100 µm | ~100 GB/s/mm² | Low |
| TSV + CoWoS/interposer | 5–10 µm | ~500 GB/s/mm² | Medium |
| Hybrid bonding (SoIC/Foveros) | 1–3 µm | >1 TB/s/mm² | High |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
