---
type: concept
slug: sic
canonical_name: SiC
aliases: []
kind: technology
parent_concepts:
- materials
- substrates
related_concepts: []
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2026-06-22-sintered-metal-die-attach-landscape]]'
- '[[2026-06-22-thermal-stack-layer-landscape]]'
- '[[2024-yole-power-sic-2024]]'
- '[[2024-yole-power-gan-2024]]'
- '[[2026-05-26-semianalysis-800vdc-revolution]]'
- '[[2024-omdia-power-electronics-forecast]]'
- '[[2024-trendforce-foundry-2024]]'
- '[[2026-06-22-tim-approaches-full-sweep]]'
- '[[2026-06-01-nibras-ucl-chipstart]]'
- '[[2026-06-12-hku-sic-cryogenic-neuromorphic-chip-10mk]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 82
last_reorg_date: '2026-05-13'
sources_7d: 8
sources_30d: 30
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Silicon carbide (SiC) is a wide-bandgap (WBG) semiconductor: bandgap 3.26 eV (4H polytype), breakdown field ~3 MV/cm, thermal conductivity ~490 W/m·K — roughly 3× silicon on all three figures. These properties enable power devices that switch faster, run hotter, and waste less energy than Si equivalents. Key device types: MOSFETs and Schottky barrier diodes (SBDs) rated 650 V–3.3 kV. State of the art: 200 mm wafer production ramping (Wolfspeed, Coherent, SICC), on-resistance figures approaching theoretical limits, defect density (micropipes, basal plane dislocations) still the primary yield lever. Dominant application: EV inverters, where SiC cuts switching losses ~50% vs Si IGBT.

## Competitive landscape

GaN-on-Si competes directly below 900 V — lower substrate cost, higher switching frequency, but inferior at high-voltage/high-temperature. Si IGBTs remain entrenched in cost-sensitive, lower-frequency applications. GaAs and InP are irrelevant here. Diamond is a longer-horizon competitor with superior theoretical properties but no manufacturable substrate ecosystem. The real competitive axis is SiC vs GaN segmentation by voltage class and thermal budget.

| | SiC | GaN-on-Si | Si IGBT |
|---|---|---|---|
| Voltage sweet spot | 900 V–3.3 kV | 100–650 V | 600 V–6.5 kV |
| Switching freq | 10–100 kHz | 100 kHz–10 MHz | 1–20 kHz |
| Substrate maturity | 150/200 mm | 6–8" (on Si) | Commodity |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
