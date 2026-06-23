---
type: concept
slug: thermal-stack-map
canonical_name: AI Thermal Stack Map (junction-to-ambient)
aliases:
- thermal stack layers
- junction-to-ambient map
- cooling stack map
kind: framework
parent_concepts:
- ai-thermal-management
related_concepts:
- tim-approach-map
- thermal-interface-materials
- diamond-heat-spreader
- graphene-thermal-films
- vapor-chambers
- heat-pipes
- phase-change-materials
- liquid-cooling-datacentre
- advanced-packaging
sources:
- '[[2026-06-22-thermal-stack-layer-landscape]]'
- '[[2026-06-22-liquid-metal-tim-landscape]]'
- '[[2026-06-22-sintered-metal-die-attach-landscape]]'
- '[[2024-idtechex-thermal-interface-materials-2026-2036]]'
- '[[2024-yole-thermal-management-2024]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
frontier:
- When does the binding layer move from die-attach (TIM1) to in-die (L0)? TSMC IMC-Si commercialisation (~2027) is the tripwire.
- Does BSPDN force backside/microfluidic cooling (L0) into the mainstream, collapsing the TIM1 material race below it?
- Which layers does the foundry/OSAT absorb (value → public) vs leave to a specialist (seed wedge survives)?
last_updated: '2026-06-22'
tags:
- concept
- framework
- thermal
- ai-infrastructure
- map
mention_count: 0
descendants:
- tim-approach-map
sources_7d: 3
sources_30d: 3
recent_mentions: []
neighbors:
- slug: tim-approach-map
  name: TIM Approach Map (every thermal-interface-material class, in-market + R&D)
  path: /sotf-site/energy-power/thermal-management/tim-approach-map/
  macro: energy-power
- slug: thermal-interface-materials
  name: Thermal Interface Materials (TIM)
  path: /sotf-site/energy-power/thermal-management/thermal-interface-materials/
  macro: energy-power
- slug: diamond-heat-spreader
  name: Diamond Heat Spreader
  path: /sotf-site/energy-power/thermal-management/diamond-heat-spreader/
  macro: energy-power
- slug: graphene-thermal-films
  name: Graphene Thermal Films
  path: /sotf-site/energy-power/thermal-management/graphene-thermal-films/
  macro: energy-power
- slug: vapor-chambers
  name: Vapor Chambers
  path: /sotf-site/energy-power/thermal-management/vapor-chambers/
  macro: energy-power
- slug: heat-pipes
  name: Heat Pipes
  path: /sotf-site/energy-power/thermal-management/heat-pipes/
  macro: energy-power
- slug: phase-change-materials
  name: Phase-Change Materials (Thermal)
  path: /sotf-site/energy-power/thermal-management/phase-change-materials/
  macro: energy-power
- slug: liquid-cooling-datacentre
  name: Liquid Cooling at Datacentre Scale
  path: /sotf-site/energy-power/thermal-management/liquid-cooling-datacentre/
  macro: energy-power
- slug: advanced-packaging
  name: Advanced Packaging
  path: /sotf-site/manufacturing/packaging/advanced-packaging/
  macro: manufacturing
---
## Why this map exists — the comparison logic

Heat leaves an AI accelerator along a **path**, junction → ambient, through a stack of layers. Each layer is a distinct engineering problem with its own physics, its own competing approaches, and its own value-capture answer. The single most useful discipline:

The meta-thesis over the whole map is **Thermal Stack Arms Race**: **the stack stays segmented — no single material or layer wins all of it.** This page is the substrate that thesis reasons over; the demand-side spine is **Ai Power Thermal Binding** and the buy-side market is **Datacentre Thermal Power Market**.

## The stack, layer by layer

Heat flux at the hotspot now exceeds ~1 kW/cm²; package TDP is passing 1 kW and heading to 1.8–2.3 kW (Nvidia Rubin, CES Jan 2026). Each layer below is where some of that heat is conducted, acquired, transported, or rejected.

### L0 — In-die / embedded cooling  *(the frontier that bypasses the TIM problem)*
- **Role:** remove heat *inside* the silicon — microchannels etched into the die or interposer backside, on-die hotspot management. If heat never has to cross a die-attach interface, layers L1–L3 stop binding.
- **Binding question:** does the **foundry/OSAT absorb** the in-silicon primitive, or does a specialist hold a manufacturable one?
- **Approaches / who:** **Corintis** (EPFL; in-silicon microfluidics + Glacierware design software; Microsoft co-dev, ~3× heat removal / 65% lower peak temp, vendor-demoed); **TSMC IMC-Si** (microchannels fusion-bonded into CoWoS, >2.6 kW TDP, ~2027 commercialisation — *the* competitive fact); **Jetcool** SmartSilicon (on-die); Maxwell Labs (laser cooling, pre-product); imec/IBM-Zurich legacy; Adeia IP. See **In Chip Microfluidic Cooling**.
- **Capture → route:** value biases to **foundry/OSAT capture** (TSMC absorbing it ~2027); the narrow venture wedge is **design software + hyperscaler co-dev**, not the etch/bond primitive. **Cross-link: BSPDN** (backside power delivery, Intel 18A / TSMC A16) *forces* backside cooling and is the why-now. Listed: TSM, FLEX (JetCool), ADEA.

### L3 — TIM2 (lid/spreader → cold plate)
- **Role:** second interface, lid to cold plate. Lower flux than TIM1, larger area.
- **Approaches / who (incumbent-dense — the thickest, most commoditised material layer):** grease, gap pads, phase-change pads — Henkel, Dow, Shin-Etsu, Momentive, Wacker, Fujipoly, Laird, Parker/Chomerics, Honeywell/Solstice PTM, T-Global. See [Phase-Change Materials (Thermal)](/sotf-site/energy-power/thermal-management/phase-change-materials/).
- **Capture → route:** commodity incumbent material houses. **Public/incumbent.**

### L4 — Heat acquisition (cold plate / direct-to-chip)
- **Role:** carry heat into the coolant — direct-to-chip cold plate, microconvective, heat pipe, or (legacy) air heatsink.
- **Approaches / who:** single-phase DTC (**Jetcool**→Flex, CoolIT→Ecolab, Asetek-exited) — *the AI reference: NVIDIA GB200/GB300 spec single-phase DTC*; two-phase DTC (**Zutacore** $100M-C Jun 2026, accelsius $65M-B) — the >2 kW future bet.
- **Capture → route:** bare cold plate **commoditising to assembly margins**; value pools one layer up (integrated CDU + chemistry + services) and was rolled up in a 2025–26 M&A sweep (**Boyd→Eaton $9.5B**, **CoolIT→Ecolab $4.75B**). **Public read.** Listed: ETN, SU, VRT, NVT, ECL, FLEX.

### L5 — Coolant / dielectric working fluid
- **Role:** the fluid that carries heat away — single-phase water-glycol, two-phase dielectric, immersion fluid.
- **Approaches / who:** the **3M PFAS exit** (manufacturing ceased end-2025, ~80% of PFAS coolant supply) created a two-phase supply vacuum; fillers are chemical majors (Chemours Opteon, Solvay/Syensqo Galden, Daikin) and oil majors for single-phase PFAS-free (Shell, bp/Castrol). See **Dielectric Coolant Pfas Transition**.
- **Capture → route:** no ownable molecule; moat is **plant + qualification + regulatory capex**. **Public/incumbent-chemical read.** Listed: CC, SYENS, 6367, SHEL, BP.

### L6 — Distribution (CDU, manifolds, plumbing)
- **Role:** move coolant between cold plate and heat rejection — CDU, manifolds, pumps, quick-disconnects, rear-door HX.
- **Approaches / who:** **Vertiv**, alfa-laval, motivair→Schneider, chilldyne→Daikin, rittal, nvent, foxconn.
- **Capture → route:** **plumbing — competes to assembly margins; incumbents roll it up. Pass / public.**

### L7 — Heat rejection (system → ambient) / immersion
- **Role:** reject heat to the environment — immersion tanks, dry coolers, chillers, evaporative.
- **Approaches / who:** single-phase immersion (**Iceotope**, **Submer**, GRC), two-phase immersion (LiquidStack→Trane Mar 2026 — pivoted off two-phase after 3M exit).
- **Capture → route:** **HVAC-major margins — public read.** NVIDIA DTC reference keeps immersion a **<15% specialty** (the **Thermal Stack Arms Race** prediction). Listed: TT, VRT, NVT, SU.

### Adjacent thermal domains (not the AI datacentre stack — cross-link anchors)
- **Power-electronics modules** (sintered-Ag die-attach, double-sided cooling) → **Gan Power Datacentre**. **Photonics / CPO** (laser-junction thermal, CTE-matched layers) → **Photonic Packaging Cpo**. **EV / SiC traction** → **Sic Ev Traction Dominance**. **Cryogenic / quantum** (dilution fridges; *genuinely active VC* — Maybell Quantum ~$73M Mar 2026) → **Cryo Computing**. **Space / satellite** (radiative-only; orbital DCs — Starcloud put an H100 in orbit Nov 2025).

## Company placement table

The cohort, placed. `L#` = primary layer (secondary in parens). Status from the company page `decision:`. Garbled/duplicate auto-map slugs and demand-side (server OEMs, power devices) dropped — see the source note for the full raw classification.

**Coverage read:** thickest = **L3** (commodity TIM2 incumbents, ~16) and **L1** (the frontier, ~12). Thinnest = **L0** (Corintis ~the only true entry), **L5** (one real fluid line + dielectric secondaries), **L8** (2–3). The thin layers are where either a genuine wedge (L0) or a dislocation (L5 PFAS) sits — built out as **In Chip Microfluidic Cooling** and **Dielectric Coolant Pfas Transition**.

## Where the genuine early-stage venture wedge is (vehicle-agnostic, ranked by where value is held)

## Frontier

See frontmatter `frontier:` block.

## Reading list
- [TIM Approach Map (every thermal-interface-material class, in-market + R&D)](/sotf-site/energy-power/thermal-management/tim-approach-map/) — the orthogonal axis: every TIM material class (in-market + R&D), the comparison catalog
- **Thermal Stack Arms Race** — the thesis this map serves (no single substrate wins)
- **Ai Power Thermal Binding** / **Datacentre Thermal Power Market** — demand spine + buy-side market
- **Cnt Tim Billion Revenue** / **Liquid Metal Tim** / **Sintered Silver Die Attach** — the L1 material slices
- **In Chip Microfluidic Cooling** (L0) / **Dielectric Coolant Pfas Transition** (L5) — the thin-layer build-outs
- **2026 06 22 Thermal Stack Layer Landscape** — the per-layer ground-truth source note
