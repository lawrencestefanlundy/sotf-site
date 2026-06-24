---
type: concept
slug: diamond
canonical_name: Diamond
aliases: []
kind: technology
parent_concepts:
- materials
- substrates
related_concepts:
- wide-bandgap-semiconductors
- gallium-nitride
- power-electronics
- quantum-sensing
- photonics
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-05-31-three-underrated-technologies-from]]'
frontier:
- ''
last_updated: '2026-06-17'
tags:
- concept
- technology
mention_count: 186
last_reorg_date: '2026-05-13'
sources_7d: 6
sources_30d: 37
recent_mentions:
- slug: 2026-06-23-evtol-certification-status-joby-stage4-archer-volocopter
  title: eVTOL type-certification status Q1-Q2 2026 — Joby Stage 4, Archer Stage 3, Volocopter pivot
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
- slug: 2026-05-02-nv-center-quantum-sensing-review-sciencedirect-2022
  title: NV center quantum sensing review (ScienceDirect 2022)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-high-sensitivity-nv-diamond-resonator-comm-materials-2025
  title: High-sensitivity NV diamond resonator (Comm. Materials 2025)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-quantumdiamonds-iq-capital
  title: QuantumDiamonds (IQ Capital)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-nv-center-wikipedia
  title: NV center (Wikipedia)
  date: '2026-05-02'
  kind: web
- slug: 2026-02-09-semianalysis-datacenter-cpu-2026
  title: 'CPUs are Back: The Datacenter CPU Landscape in 2026'
  date: '2026-02-09'
  kind: web
neighbors:
- slug: wide-bandgap-semiconductors
  name: Wide-Bandgap Semiconductors
  path: /sotf-site/materials/substrates/wide-bandgap-semiconductors/
  macro: materials
- slug: gallium-nitride
  name: Gallium Nitride
  path: /sotf-site/energy-power/power-electronics/gallium-nitride/
  macro: energy-power
- slug: power-electronics
  name: Power Electronics
  path: /sotf-site/energy-power/power-electronics/power-electronics/
  macro: energy-power
- slug: quantum-sensing
  name: Quantum Sensing
  path: /sotf-site/sensing/quantum-sensing/quantum-sensing/
  macro: sensing
- slug: photonics
  name: Photonics
  path: /sotf-site/photonic-systems/pic-platforms/photonics/
  macro: photonic-systems
---
## Physics / mechanism

Diamond is a metastable allotrope of carbon with sp³ tetrahedral bonding. Key properties: bandgap 5.47 eV (ultrawide), breakdown field ~10 MV/cm, thermal conductivity 2200 W/m·K (highest of any bulk material), carrier mobility electrons ~4500 cm²/V·s / holes ~3800 cm²/V·s. Boron-doped p-type diamond is achievable; n-type remains difficult. CVD synthesis (MPCVD) now produces single-crystal wafers up to 2" with defect densities approaching 10³ cm⁻², though 4" remains pre-commercial. NV-centre coherence times reach milliseconds at room temperature. Diamond Schottky diodes already demo >1 kV blocking with mΩ·cm² on-resistance. State-of-play: material quality is investor-grade but wafer economics are not yet.

## Competitive landscape

Competing ultrawide-bandgap (UWBG) materials: AlN (6.2 eV bandgap, mature epitaxy, weaker thermal conductivity ~320 W/m·K), Ga₂O₃ (4.8 eV, scalable melt-grown substrates, but poor thermal management), cBN (similar gap to diamond, near-zero commercial traction). SiC and GaN are incumbent power semiconductors but are wide- not ultrawide-bandgap and top out below diamond's theoretical Baliga figure of merit.

| Material | Bandgap (eV) | Thermal cond. (W/m·K) | Wafer maturity |
|---|---|---|---|
| Diamond | 5.47 | 2200 | 2", nascent |
| Ga₂O₃ | 4.8 | 20 | 4–6", advancing |
| AlN | 6.2 | 320 | 2–4", limited |

## Where the value is (opportunity-led, all routes)

## Diamond value-chain cluster

Diamond shows up at several points of the electronics stack, all sitting on a common substrate base. Same material, different role: worth holding as one cluster because a move at the base (single-crystal substrate cost/size, sovereign supply) or in demand (AI thermal, defence RF, quantum) ripples across the others.

**Base layer: substrate & material growth** (feeds every application above)

**Application layers** (the three value vectors, ranked by opportunity size)

Equipment and deposition tooling sits underneath all of these (CVD reactors: **sp3 Diamond**, Seki Diamond Systems), a picks-and-shovels layer that benefits if any device layer scales.

## Other diamond markets & applications

Beyond the electronic and quantum stack above, diamond serves several established markets. Most are lower VC-relevance for us directly, but they matter to the thesis because **they drive CVD diamond volume and cost, which is the base-layer gate** for the RF, thermal and quantum plays: cheaper, larger single-crystal wafers arrive on the back of these markets' scale.

| Market | Use of diamond | Companies (KB) | Relevance |
|---|---|---|---|
| **Optics & photonics** | Optical windows for high-power lasers and gyrotrons; IR / X-ray / synchrotron optics; Raman lasers; diamond photonics | **Element Six** (optical grade), **Coherent / II-VI**, **Edmund Optics**, **Tydex**, **Diatope** | Adjacent; defence / laser pull overlaps RF |
| **Electrochemistry & water** | Boron-doped diamond (BDD) electrodes: water / wastewater treatment, ozone generation, electrochemical sensors | Condias, Element Six (electrochemical grade) | Niche specialty industrial |
| **Industrial / superhard** | Cutting tools, abrasives, wear and optical coatings (diamond's original and largest market, commoditised) | **Sumitomo**, **Beijing Worldia**, **Zhongnan**, **Applied Diamond**, Sandvik | Low VC-relevance; scales material supply |
| **Lab-grown gemstone / consumer** | Jewellery-grade CVD / HPHT stones | Diamond Foundry (VRAI / Aether), **WD Lab Grown**, **IIa Technologies**, **New Diamond Era** | The cash engine that funds and scales CVD reactor capacity |
| **Biomedical / diagnostics** | Fluorescent and drug-delivery nanodiamonds; NV biosensing (overlaps quantum sensing) | **Orbis Diagnostics**, **QDTI** | Niche; quantum-sensing crossover |

The strategic point: the **gem and industrial markets are the volume base** that pulls down CVD single-crystal cost and pushes up wafer size. That base-layer trajectory is the decisive watch for whether the RF/power and quantum-device layers become economic this decade (see Frontier below).

> *Verification note (17 Jun 2026): pages marked unverified are auto-mapped (`data_source: sonnet-*`, `verified: false`); their descriptions and funding figures need a primary-source check before being cited in any memo or external artefact. Qnami in particular was auto-described as cat-qubit cavity tooling, which is wrong (it is NV scanning-probe magnetometry), corrected here.*

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)