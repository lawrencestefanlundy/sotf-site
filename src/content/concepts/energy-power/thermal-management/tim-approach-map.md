---
type: concept
slug: tim-approach-map
canonical_name: TIM Approach Map (every thermal-interface-material class, in-market + R&D)
aliases:
- TIM coverage matrix
- TIM material-class map
- TIM approaches catalog
kind: framework
parent_concepts:
- thermal-interface-materials
- thermal-stack-map
related_concepts:
- thermal-interface-materials
- thermal-stack-map
- phase-change-materials
- graphene-thermal-films
- diamond-heat-spreader
- advanced-packaging
sources:
- '[[2026-06-22-tim-approaches-full-sweep]]'
- '[[2026-06-22-liquid-metal-tim-landscape]]'
- '[[2026-06-22-sintered-metal-die-attach-landscape]]'
- '[[2024-idtechex-thermal-interface-materials-2026-2036]]'
- '[[2024-yole-thermal-management-2024]]'
frontier:
- Does the >1kW AI die-level slot settle on liquid-metal-composite, PCMA, or nanocomposite (NovoLINC class) — or stay segmented?
- 'Aligned-hBN insulating TIM: a genuine white space with no startup, or does an incumbent filler house close it?'
- 'Boron-arsenide / θ-TaN ultrahigh-k: does anyone crack scalable crystal growth (the whole moat), or does it stay a university-IP sourcing target?'
last_updated: '2026-06-22'
tags:
- concept
- framework
- thermal
- tim
- map
mention_count: 0
sources_7d: 0
sources_30d: 3
recent_mentions: []
neighbors:
- slug: thermal-interface-materials
  name: Thermal Interface Materials (TIM)
  path: /sotf-site/energy-power/thermal-management/thermal-interface-materials/
  macro: energy-power
- slug: thermal-stack-map
  name: AI Thermal Stack Map (junction-to-ambient)
  path: /sotf-site/energy-power/thermal-management/thermal-stack-map/
  macro: energy-power
- slug: phase-change-materials
  name: Phase-Change Materials (Thermal)
  path: /sotf-site/energy-power/thermal-management/phase-change-materials/
  macro: energy-power
- slug: graphene-thermal-films
  name: Graphene Thermal Films
  path: /sotf-site/energy-power/thermal-management/graphene-thermal-films/
  macro: energy-power
- slug: diamond-heat-spreader
  name: Diamond Heat Spreader
  path: /sotf-site/energy-power/thermal-management/diamond-heat-spreader/
  macro: energy-power
- slug: advanced-packaging
  name: Advanced Packaging
  path: /sotf-site/manufacturing/packaging/advanced-packaging/
  macro: manufacturing
---
## How this relates to the stack map (two orthogonal axes)

[AI Thermal Stack Map (junction-to-ambient)](/sotf-site/energy-power/thermal-management/thermal-stack-map/) answers **where in the heat path** (L0 in-die → L8 heat reuse). This page answers **which material** fills the interface. They cross: a TIM class (say liquid metal) occupies a stack position (TIM1 die-attach). Use this page to be exhaustive about material options; use the stack map to place and compare them. The governing thesis over both is **Thermal Stack Arms Race** (the stack stays segmented).

**Stack-position shorthand:** TIM1 = die-attach (junction→lid); TIM1.5 = lid interface; TIM2 = spreader→cold plate. k in W/m·K (vendor-datasheet typicals, method-dependent).

## A. Commercial / in-market classes (24)

## B. R&D / emerging approaches (14) — maturity, players, wedge

| Approach | Maturity (TRL) | Key players (startup / lab) | Binding constraint | Wedge verdict |
|---|---|---|---|---|
| Next-gen VACNT + encapsulation | 8-9 prod / 3-5 frontier | **Carbice**, **Nawah**, **Trimtabs**; Cola (GA Tech) | off-chip growth + transfer, $/cm² | **incumbent-captured** (Carbice) |
| Vertically-aligned graphene (VG) | 7-8 | **Sht Smart High Tech**, Thermal Rex; Liu (Chalmers) | through-plane alignment + shorting | narrowing (SHT public + Henkel) |
| **Cu/metal-nanowire arrays** | 6-7 | **Novolinc**; Berkeley/UCSD/Stanford/CMU | dense uniform low-R arrays at scale | **YES — process moat** |
| Sintered nano-copper | 5-7 | **Kuprion**, **Nano Join**, **Elephantech** | pressureless void-free oxidation-free | incumbent-captured (Heraeus/MacDermid) |
| Self-healing / reworkable | 2-4 | none pure-play (**Arieca** gets it free) | k vs mobility trade-off | no standalone wedge |
| **LM containment composite** | 6-8 | ****Boston Materials**, **Arieca**, **Hymet****; UT Austin (Yu), CMU | pump-out, Ga corrosion, reliability | **YES — strongest wedge** |
| 2D beyond graphene (hBN/MXene) | 3-5 / 2-4 | MXene Inc (Drexel), BNNT Materials; Murata | k + alignment vs supply scale | **aligned-hBN = white space**; MXene = supply play |
| **Nanocomposite hybrid** | 5-7 | ****Novolinc**, **Boston Materials****; Shen (CMU) | continuous nano-architecture mfg | **YES** |
| Phononic / metamaterial | 1-3 | CMU, MIT (no TIM startup) | nanofab at scale; mostly insulating | no TIM wedge (science) |
| Direct-bond / TIM-less (Cu-Cu hybrid, TLP/SLID) | 8-9 / 5-7 | TSMC/Intel/Samsung, BESI, Adeia | sub-nm flatness, fab-level | **foundry-absorbed** |
| **Printed / jettable TIM** | 6-8 | ****Novolinc**, **Arieca**, fabric8labs**; **Indium** | HVM line-qual, BLT control | **YES — selective** (formulation + process) |
| Bio-inspired / structured | 2-4 | none (nanoGriptech adhesion pivot) | manufacture at yield; unproven vs LM | weak/none |
| Boron-arsenide / θ-TaN / BP | 2-4 | no startup; UCLA (Hu), Houston (Ren), UCSB | scalable defect-free crystal growth | **open but unbuilt** (sourcing target) |
| Diamond (GaN-on-diamond, nanocrystalline) | 6-8 | **Akash Systems**, **Diamond Foundry**, **Diamfab**; **Element Six De Beers**, **Coherent** | cost, CVD speed, CTE/TBR | yes-but-late/capital-heavy (EU seed: Diamfab) |

> **Metal-TIM note.** Solder TIM (sTIM), indium foil, and PCMA are the genuine **volume die-level path for >1kW AI accelerators today** (Indium-led) — promoted 22 Jun 2026 to its own slice, **Metal Solder Pcma Tim**. They are the incumbent that is already winning the volume, distinct from the speculative carbon classes and from consumer-led **Liquid Metal Tim**.

## C. Venture-stage startup roster (the live sourcing list)

## D. State of the art for >1kW AI accelerators (vs commodity)

Deployed/designed-in on bare-die GPUs/ASICs where commodity grease/pads pump out: **1. solder TIM (sTIM)** · **2. liquid metal + LM composites** · **3. PCMA** · **4. polymer PCM (PTM7950)** · **5. VACNT pads (Carbice)**. Next ring: indium foil (immersion), sintered-Ag (power stages, not the GPU die), carbon-fibre (Dexerials). Commodity = silicone grease / gap pads / gels (bulk of TIM2 by volume, just not the thermal-limited interface).

## E. Value capture & routing (vehicle-agnostic, ranked by where value is held)

## F. KB coverage status (the 100% check)

## Frontier
See frontmatter `frontier:` block.

## Reading list
- [AI Thermal Stack Map (junction-to-ambient)](/sotf-site/energy-power/thermal-management/thermal-stack-map/) — the orthogonal axis (where in the path)
- [Thermal Interface Materials (TIM)](/sotf-site/energy-power/thermal-management/thermal-interface-materials/) — the TIM physics/concept anchor
- **Thermal Stack Arms Race** — the governing thesis (segmented stack)
- **2026 06 22 Tim Approaches Full Sweep** — the exhaustive source sweep (vendors, R&D, startups)
- material slices: **Liquid Metal Tim** · **Sintered Silver Die Attach** · **Cnt Tim Billion Revenue** · **In Chip Microfluidic Cooling**
