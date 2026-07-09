---
type: concept
slug: thermal-management
canonical_name: Thermal Management
aliases: []
kind: technology
parent_concepts:
- energy-power
- ai-thermal-management
related_concepts:
- thermal-stack-map
- thermal-interface-materials
- liquid-cooling-datacentre
- diamond-heat-spreader
- vapor-chambers
- phase-change-materials
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-03-08-diamonds-are-semiconductors-best-friend]]'
- '[[2026-04-28-thermal-stack-arms-race-global-diamond-heat-spreaders]]'
- '[[2026-04-24-thermal-stack-arms-race-global-thermal-management-market-to]]'
- '[[2026-04-10-thermal-stack-arms-race-liquid-cooling-for-ai-data-centers]]'
- '[[2024-yole-thermal-management-2024]]'
- '[[2026-04-01-ai-power-thermal-binding-market-projection-35-of-new-ai]]'
- '[[2025-08-19-thermal-stack-arms-race-thermal-interface-materials-market]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 81
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 4
sources_30d: 7
recent_mentions:
- slug: 2026-04-28-thermal-stack-arms-race-global-diamond-heat-spreaders
  title: Global Diamond Heat Spreaders Emerging for AI Chip Cooling
  date: '2026-04-28'
  kind: web
- slug: 2026-04-24-thermal-stack-arms-race-global-thermal-management-market-to
  title: Global Thermal Management Market to Reach £22bn by 2030, Driven by AI and Data Centres
  date: '2026-04-24'
  kind: web
- slug: 2026-04-10-thermal-stack-arms-race-liquid-cooling-for-ai-data-centers
  title: Liquid Cooling For AI Data Centers Market Growth Analysis - Size and Forecast 2026-2030
  date: '2026-04-10'
  kind: web
- slug: 2026-04-01-ai-power-thermal-binding-market-projection-35-of-new-ai
  title: 'Market projection: 35%+ of new AI datacenter capacity specifying liquid cooling by 2026'
  date: '2026-04-01'
  kind: web
- slug: 2026-03-08-diamonds-are-semiconductors-best-friend
  title: Diamonds are Semiconductors' Best Friend 2026
  date: '2026-03-08'
  kind: web
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-08-19-thermal-stack-arms-race-thermal-interface-materials-market
  title: 'Thermal Interface Materials Market Report 2026-2036: High-Performance TIMs for Data Centers, AI Servers, and 5G Infrastructure'
  date: '2025-08-19'
  kind: web
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
neighbors:
- slug: thermal-stack-map
  name: AI Thermal Stack Map (junction-to-ambient)
  path: /sotf-site/energy-power/thermal-management/thermal-stack-map/
  macro: energy-power
- slug: thermal-interface-materials
  name: Thermal Interface Materials (TIM)
  path: /sotf-site/energy-power/thermal-management/thermal-interface-materials/
  macro: energy-power
- slug: liquid-cooling-datacentre
  name: Liquid Cooling at Datacentre Scale
  path: /sotf-site/energy-power/thermal-management/liquid-cooling-datacentre/
  macro: energy-power
- slug: diamond-heat-spreader
  name: Diamond Heat Spreader
  path: /sotf-site/energy-power/thermal-management/diamond-heat-spreader/
  macro: energy-power
- slug: vapor-chambers
  name: Vapor Chambers
  path: /sotf-site/energy-power/thermal-management/vapor-chambers/
  macro: energy-power
- slug: phase-change-materials
  name: Phase-Change Materials (Thermal)
  path: /sotf-site/energy-power/thermal-management/phase-change-materials/
  macro: energy-power
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
