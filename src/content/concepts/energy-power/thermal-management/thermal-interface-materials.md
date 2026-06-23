---
type: concept
slug: thermal-interface-materials
canonical_name: Thermal Interface Materials (TIM)
aliases: []
kind: material
parent_concepts:
- energy-power
- ai-thermal-management
related_concepts:
- tim-approach-map
- thermal-stack-map
- ai-thermal-management
- phase-change-materials
- advanced-packaging
- diamond
- graphene-thermal-films
sources:
- '[[2024-idtechex-thermal-interface-materials-2026-2036]]'
- '[[2024-yole-thermal-management-2024]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
frontier:
- Which material wins which slot — does the stack stay segmented (liquid metal at die-level, sintered Ag at die-attach, CNT/graphene/diamond at lid/spreader) or does one class generalise?
- Containment, not conductivity, is the liquid-metal frontier — who solves Ga corrosion + pump-out at production reliability?
- Does the foundry/OSAT absorb TIM application as a qualified package option, collapsing the startup wedge?
last_updated: '2026-06-22'
tags:
- concept
- material
mention_count: 0
last_reorg_date: '2026-05-13'
descendants:
- tim-approach-map
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: tim-approach-map
  name: TIM Approach Map (every thermal-interface-material class, in-market + R&D)
  path: /sotf-site/energy-power/thermal-management/tim-approach-map/
  macro: energy-power
- slug: thermal-stack-map
  name: AI Thermal Stack Map (junction-to-ambient)
  path: /sotf-site/energy-power/thermal-management/thermal-stack-map/
  macro: energy-power
- slug: phase-change-materials
  name: Phase-Change Materials (Thermal)
  path: /sotf-site/energy-power/thermal-management/phase-change-materials/
  macro: energy-power
- slug: advanced-packaging
  name: Advanced Packaging
  path: /sotf-site/manufacturing/packaging/advanced-packaging/
  macro: manufacturing
- slug: diamond
  name: Diamond
  path: /sotf-site/materials/substrates/diamond/
  macro: materials
- slug: graphene-thermal-films
  name: Graphene Thermal Films
  path: /sotf-site/energy-power/thermal-management/graphene-thermal-films/
  macro: energy-power
---
## Physics / mechanism

Thermal interface materials fill the microscopic air gaps between a heat source (die, substrate, lid) and a heat sink or spreader. Without them, contact resistance dominates; even polished surfaces touch only at ~1–2% of nominal area. TIMs conduct heat across that interface, characterised by bulk thermal conductivity (W/m·K) and bond-line thickness (BLT, µm) — together yielding interface thermal resistance (mm²·K/W). Indium foil sits near 80 W/m·K; phase-change materials 3–10 W/m·K; filled polymer pads 3–8 W/m·K; liquid metal (Ga-In alloys) 20–40 W/m·K at <50 µm BLT. State of the art for high-performance compute is liquid metal or sintered silver (~200–250 W/m·K), deployed in HPC and AI accelerator lids where junction temps must stay below 95 °C at >300 W per die.

## Competitive landscape

Incumbent categories: filled silicones/epoxies (Shin-Etsu, Momentive, Henkel), phase-change pads (Bergquist/Henkel, Laird), indium foil (Indium Corp), liquid metals (Thermal Grizzly, Indium Corp). Competing approaches include vapour chambers and embedded microfluidic cooling, which bypass the TIM problem rather than solve it. Carbon-based options — vertically aligned CNT arrays, graphene laminates — offer >400 W/m·K in lab settings but conformability and cost limit deployment. Sintered silver scales in power electronics but requires pressure/temperature cure steps incompatible with some packaging flows.

> **For the exhaustive material-class catalog** — every TIM approach in-market and in R&D, with vendors, startups, maturity, and capture/route — see [TIM Approach Map (every thermal-interface-material class, in-market + R&D)](/sotf-site/energy-power/thermal-management/tim-approach-map/) (24 commercial classes + 14 R&D approaches, swept 22 Jun 2026). This page is the physics/concept anchor; the map is the comprehensive coverage matrix.

## Why it matters / where the value is

TIMs are a direct gating factor on chiplet / 2.5D / 3D packaging yield and reliability, and the binding thermal layer on >1kW AI accelerator packages — so the TIM market grows with accelerator shipments as a per-package consumable tax (the **Ai Compute Toll Booths** logic). The material classes do not converge: the stack stays segmented (see **Thermal Stack Arms Race**), which is itself the value-capture argument — a held material primitive defends one layer with a chemistry/process moat.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
