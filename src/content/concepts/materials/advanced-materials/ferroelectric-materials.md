---
type: concept
slug: ferroelectric-materials
canonical_name: Ferroelectric Materials
aliases:
- ferroelectric
- ferroelectrics
- FE materials
parent_concepts:
- advanced-materials
- materials
related_concepts:
- hafnium-oxide
- barium-titanate
- piezoelectric
- aluminium-scandium-nitride
- high-k-dielectrics
sources:
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- Does any ferroelectric material class beyond HfO2 reach CMOS-compatible integration — specifically, can sub-20 nm BaTiO3 films be ALD-deposited with device-grade phase control?
- 'Neuromorphic / analogue computing: can multi-state FeFET polarisation (partial switching) be used for reliable weight storage in edge-AI inference — what is the practical bit precision ceiling?'
- What is the commercialisation path for AlScN ferroelectric (CMOS-compatible, high coercive field) as a piezo-MEMS alternative to PZT — does it reach MEMS foundry production by 2028?
last_updated: '2026-06-02'
tags:
- concept
mention_count: 143
sources_7d: 8
sources_30d: 32
recent_mentions:
- slug: 2025-26-lapedus-next-gen-ferroelectric-memory
  title: Next-Gen Ferroelectric Memory Still A Work In Progress
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
neighbors:
- slug: hafnium-oxide
  name: Hafnium Oxide
  path: /materials/functional-layers/hafnium-oxide/
  macro: materials
- slug: barium-titanate
  name: Barium Titanate
  path: /materials/functional-layers/barium-titanate/
  macro: materials
- slug: piezoelectric
  name: Piezoelectric
  path: /materials/functional-layers/piezoelectric/
  macro: materials
- slug: aluminium-scandium-nitride
  name: Aluminium Scandium Nitride
  path: /materials/functional-layers/aluminium-scandium-nitride/
  macro: materials
- slug: high-k-dielectrics
  name: High-K Dielectrics (HfO2, ZrO2)
  path: /materials/functional-layers/high-k-dielectrics/
  macro: materials
---
A ferroelectric material possesses a spontaneous electric polarisation that can be reversed by an applied electric field below the material's dielectric breakdown — the defining property that distinguishes ferroelectrics from ordinary dielectrics. This switchable polarisation creates a polarisation-vs-field hysteresis loop (the P-E loop) analogous to the B-H hysteresis loop in ferromagnetics. At the microscopic level, ferroelectricity arises from off-centering of ions in the unit cell (displacive mechanism in perovskites such as BaTiO₃ and PZT) or from order-disorder transitions, producing two or more stable polarisation states that persist in zero field. Above the Curie temperature, the material transitions to a paraelectric phase.

The technologically important parameters are: spontaneous polarisation Ps (µC/cm²), coercive field Ec (MV/cm), endurance (switching cycles before fatigue), retention (polarisation stability at operating temperature), and process compatibility. Classic ferroelectrics — PZT (lead zirconate titanate, Ps ~100 µC/cm²) and SBT (SrBi₂Ta₂O₉) — offer high Ps but require film thicknesses >50 nm and anneal temperatures >600°C that are incompatible with CMOS back-end processes. This locked ferroelectric memory to standalone or front-end-of-line applications for three decades.

The field's current axis of investment relevance is [Hafnium Oxide](/materials/functional-layers/hafnium-oxide/) ferroelectrics (HZO, Si:HfO₂): the first ferroelectric class to be CMOS-native, scalable below 10 nm, and ALD-deposited at BEOL-compatible temperatures. This enables embedded FeFET and FeRAM in standard logic fabs — the enabler behind **Ferroelectric Memory Share**.

Beyond memory, ferroelectric materials are the physics substrate for piezoelectric MEMS actuators and sensors (AlScN, [Aluminium Scandium Nitride](/materials/functional-layers/aluminium-scandium-nitride/) is the CMOS-compatible piezo challenger to PZT), electro-optic modulators ([Barium Titanate](/materials/functional-layers/barium-titanate/), lithium niobate), and neuromorphic weight-storage (partial FeFET polarisation switching for analogue inference).

## Frontier

See frontmatter `frontier:` block.
