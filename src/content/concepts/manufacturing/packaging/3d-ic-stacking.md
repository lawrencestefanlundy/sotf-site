---
type: concept
slug: 3d-ic-stacking
canonical_name: 3D IC Stacking
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- packaging
related_concepts: []
companies_using:
- 3d-plus
- adeia-spun-off-from-xperi
- amkor-technology
- ase-group-advanced-semiconductor-engineering
- besi-be-semiconductor-industries
- cadence-design-systems
- cea-leti
- cirtran-evatec
- ev-group-evg
- fraunhofer-izm
- imec
- integra-technologies
- intel
- kuprion
- lumileds-coherent-ii-vi-heritage
- micron-technology
- monolithic-power-systems-mps
- onto-innovation
- samsung-semiconductor
- sifive-now-part-of-risc-v-ecosystem-private
- sk-hynix
- synopsys
- tsmc
- unimicron-technology
- xperi-formerly-tessera-technologies
ideas_referencing: []
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
---

# 3D IC Stacking

*Kind: technology*

## Physics / mechanism

3D IC stacking integrates multiple die vertically using through-silicon vias (TSVs), hybrid bonding, or micro-bumps, replacing lateral interconnects with vertical ones. Key parameters: TSV pitch (currently ~1–5 µm in leading HVM), hybrid bonding pitch down to ~1 µm (TSMC SoIC, Intel Foveros), inter-die bandwidth density exceeding 1 TB/s/mm², and z-height constraints (die thinned to 30–50 µm). Configurations include die-to-die (D2D), die-to-wafer (D2W), and wafer-to-wafer (W2W). W2W maximizes yield only when die sizes match. HBM stacks 8–16 DRAM die via TSVs; CoWoS and EMIB handle heterogeneous integration at package level. Primary bottleneck is thermal dissipation and yield stacking.

## Competitive landscape

| Approach | Pitch | Bandwidth density | Complexity |
|---|---|---|---|
| Micro-bump flip-chip | 40–100 µm | ~100 GB/s/mm² | Low |
| TSV + CoWoS/interposer | 5–10 µm | ~500 GB/s/mm² | Medium |
| Hybrid bonding (SoIC/Foveros) | 1–3 µm | >1 TB/s/mm² | High |

## Cloudberry relevance

Adjacent approaches: chiplets on organic substrates (lower cost, lower density), silicon photonics co-packaging (replaces electrical I/O with optical), and near-memory compute architectures that reduce bandwidth pressure altogether. TSMC, Intel, Samsung, and ASE dominate packaging. Equipment layer: Besi, ASMPT, EV Group for bonding tools. Materials pressure on dielectrics, barrier layers, and thermal interface materials is significant.


GF's 3D bonding roadmap (Fotonix, silicon photonics) and its foundry position in heterogeneous integration make 3D stacking directly deal-relevant. Cloudberry angles: bonding equipment startups, novel TIM or low-k dielectric materials, EDA/co-design tooling for 3D floorplanning, and photonic-electronic co-stacking plays where GF's fab relationships create differentiated access. Thermal management materials companies are underloved here and fit advanced materials thesis.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
