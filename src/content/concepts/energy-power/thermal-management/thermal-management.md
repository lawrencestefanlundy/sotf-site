---
type: concept
slug: thermal-management
canonical_name: Thermal Management
aliases: []
kind: technology
parent_concepts:
- energy-power
- ai-thermal-management
related_concepts: []
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2024-yole-thermal-management-2024]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 58
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 4
sources_30d: 12
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Heat dissipation in electronics governs reliability and performance scaling. Fourier's Law (q = -k∇T) defines conductive heat flux; thermal resistance (R_th = ΔT/P) is the core figure of merit. Key parameters: thermal conductivity (k, W/m·K), interface thermal resistance (ITR, mm²·K/W), heat flux density (W/cm²). State-of-the-art: copper heatspreaders (~400 W/m·K), vapor chambers (~10,000 W/m·K effective), diamond substrates (~2,200 W/m·K). Advanced packaging—chiplets, 3D stacking—drives heat flux above 1 kW/cm² in hotspots. Liquid cooling (direct-to-chip, two-phase immersion) handles 100–1,000 W/cm². Thermal interface materials (TIMs) typically 1–10 W/m·K; indium or carbon nanotube TIMs push toward 50–100 W/m·K.

## Competitive landscape

Competing and adjacent approaches segment by form factor and flux density. Air cooling dominates commodity; liquid cooling owns HPC/AI. Thermoelectrics (Peltier, ZT ~1–2) offer active spot cooling but low efficiency. Thermally conductive polymers compete in packaging weight/cost tradeoffs. Diamond, BN, AlN, and SiC ceramics compete as substrate materials. Embedded microfluidics and phononic metamaterials are emerging.

| Approach | Max Flux (W/cm²) | Complexity | Cost |
|---|---|---|---|
| Air / heatsink | ~50 | Low | Low |
| Liquid / two-phase | ~1,000 | High | Medium–High |
| Diamond substrate | ~500 (conduction) | Medium | Very High |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
