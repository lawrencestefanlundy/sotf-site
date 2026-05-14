---
type: concept
slug: fowlp
canonical_name: FOWLP / Fan-Out WLP
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

Fan-out wafer-level packaging (FOWLP) embeds known-good dies into an epoxy mold compound, reconstructing an artificial wafer. RDL (redistribution layers) are then built on the molded surface, routing I/O beyond the die footprint—hence "fan-out." No substrate or underfill required. Key parameters: RDL line/space (currently 2µm/2µm in high-density variants; TSMC InFO pushes sub-2µm), die shift control (<5µm 3σ in mature flows), and package thickness (<0.5mm for mobile). TSMC InFO dominates via Apple A-series wins; ASE/Amkor offer cost-optimised variants. Bandwidth scales with RDL layer count; thermal performance limited by mold compound conductivity (~0.8 W/m·K vs. silicon ~150).

## Competitive landscape

FOWLP competes directly with flip-chip BGA on cost at mid-I/O counts, and with 2.5D interposer (CoWoS, EMIB) at high-bandwidth compute. For RF/mmWave, FOWLP trades against laminate SiP and QFN. Panel-level fan-out (PFLP) is the cost-reduction trajectory—larger panel formats cut per-unit cost but worsen die-shift yield.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
