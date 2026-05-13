---
type: concept
slug: thermal-interface-materials
canonical_name: Thermal Interface Materials (TIM)
aliases: []
kind: material
domain:
- cloudberry
- sotf
parent_concepts:
- energy-power
- thermal-management
related_concepts: []
companies_using:
- 3m
- applied-graphene-materials
- canatu
- carbice
- celanese-formerly-dupont-tim-assets
- dexerials
- dow-inc
- epotek-epoxy-technology
- fujipoly
- graphmatech
- henkel
- indium-corporation
- laird-thermal-systems-laird-performance-materials
- momentive-formerly-ge-advanced-materials
- nano-diamond-battery-ndb-nano-one-not-applicable-correct-nan
- panasonic-industry-division
- parker-hannifin-chomerics-division
- phase-change-energy-solutions
- schlumberger-slb-thermal-materials-group
- sheen-thermal
- shin-etsu-chemical
- skews-formerly-known-as-sts-thermal
- t-global-technology
- wacker-chemie
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- material
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---


# Thermal Interface Materials (TIM)

*Kind: material*

## Physics / mechanism

Thermal interface materials fill the microscopic air gaps between a heat source (die, substrate, lid) and a heat sink or spreader. Without them, contact resistance dominates; even polished surfaces touch only at ~1–2% of nominal area. TIMs conduct heat across that interface, characterised by bulk thermal conductivity (W/m·K) and bond-line thickness (BLT, µm) — together yielding interface thermal resistance (mm²·K/W). Indium foil sits near 80 W/m·K; phase-change materials 3–10 W/m·K; filled polymer pads 3–8 W/m·K; liquid metal (Ga-In alloys) 20–40 W/m·K at <50 µm BLT. State of the art for high-performance compute is liquid metal or sintered silver (~200–250 W/m·K), deployed in HPC and AI accelerator lids where junction temps must stay below 95 °C at >300 W per die.

## Competitive landscape

Incumbent categories: filled silicones/epoxies (Shin-Etsu, Momentive, Henkel), phase-change pads (Bergquist/Henkel, Laird), indium foil (Indium Corp), liquid metals (Thermal Grizzly, Indium Corp). Competing approaches include vapour chambers and embedded microfluidic cooling, which bypass the TIM problem rather than solve it. Carbon-based options — vertically aligned CNT arrays, graphene laminates — offer >400 W/m·K in lab settings but conformability and cost limit deployment. Sintered silver scales in power electronics but requires pressure/temperature cure steps incompatible with some packaging flows.

## Cloudberry relevance

| Material class | Thermal conductivity (W/m·K) | Key constraint |
|---|---|---|
| Filled polymer | 3–10 | High BLT, pump-out risk |
| Liquid metal | 20–40 | Ga corrosion, rework difficulty |
| Sintered silver | 150–250 | Cure pressure, cost |


For a deep-tech fund with semiconductor and photonics exposure, TIMs are a direct gating factor on chiplet/2.5D/3D packaging yield and reliability — the same substrate stack GlobalFoundries-LP portfolio companies work within. Deal-flow angles: novel inorganic filler chemistry (boron nitride, diamond nanoparticles), process-compatible deposition (sputtered or inkjet TIM for wafer-level packaging), and photonics-specific thermal management where coefficient-of-thermal-expansion mismatch between III-V and silicon demands tailored interface layers. Startups solving BLT-at-scale or eliminating pump-out in high-cycle environments are credible targets.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
