---
type: concept
slug: gallium-nitride
canonical_name: Gallium Nitride
aliases:
- GaN
- gallium nitride
- GaN-on-Si
- GaN-on-SiC
parent_concepts:
- wide-bandgap-semiconductors
- power-electronics
related_concepts:
- wide-bandgap-semiconductors
- silicon-carbide
- aluminium-gallium-nitride
- indium-gallium-nitride
- power-electronics
- compound-semiconductors
- mocvd-mbe
sources: []
frontier:
- Will GaN-on-Si reach 650V yield and reliability parity with GaN-on-SiC at 8-inch, or does substrate-induced defect density remain a ceiling?
- Can GaN power ICs (gate driver + FET monolithic) pull further system integration away from silicon ASIC + discrete topology?
- Does GaN capture any share above 650V (1200V class) once vertical GaN device architectures mature, challenging SiC's lock on EV traction?
last_updated: 2026-06-02
tags:
- concept
descendants:
- aluminium-gallium-nitride
- indium-gallium-nitride
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-04-20-fixing-the-gan-problem
  title: Fixing the GaN Problem
  date: '2026-04-20'
  kind: web
- slug: 2025-12-19-lfg-for-semiconductors
  title: LFG (for semiconductors)
  date: '2025-12-19'
  kind: substack
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2025-10-09-a-specific-theory-of-sovereign-ai
  title: A Specific Theory of Sovereign AI
  date: '2025-10-09'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2024-omdia-power-electronics-forecast
  title: Omdia — Power Semiconductors Long-Term Forecast 2024
  date: '2024-11-01'
  kind: web
- slug: 2024-yole-power-sic-2024
  title: Yole Group — Power SiC 2024 Market Analysis
  date: '2024-09-15'
  kind: web
neighbors:
- slug: wide-bandgap-semiconductors
  name: Wide-Bandgap Semiconductors
  path: /sotf-site/materials/substrates/wide-bandgap-semiconductors/
  macro: materials
- slug: silicon-carbide
  name: Silicon Carbide
  path: /sotf-site/materials/substrates/silicon-carbide/
  macro: materials
- slug: aluminium-gallium-nitride
  name: Aluminium Gallium Nitride
  path: /sotf-site/materials/functional-layers/aluminium-gallium-nitride/
  macro: materials
- slug: indium-gallium-nitride
  name: Indium Gallium Nitride
  path: /sotf-site/materials/functional-layers/indium-gallium-nitride/
  macro: materials
- slug: power-electronics
  name: Power Electronics
  path: /sotf-site/energy-power/power-electronics/power-electronics/
  macro: energy-power
- slug: compound-semiconductors
  name: Compound Semiconductors
  path: /sotf-site/materials/substrates/compound-semiconductors/
  macro: materials
- slug: mocvd-mbe
  name: MOCVD / MBE
  path: /sotf-site/manufacturing/equipment-processes/mocvd-mbe/
  macro: manufacturing
---
Gallium nitride (GaN) is a III-nitride wide-bandgap semiconductor with a direct bandgap of 3.4 eV. It is the parent binary compound of a family of alloys spanning [Aluminium Gallium Nitride](/sotf-site/materials/functional-layers/aluminium-gallium-nitride/) (AlGaN, wider bandgap) and [Indium Gallium Nitride](/sotf-site/materials/functional-layers/indium-gallium-nitride/) (InGaN, narrower bandgap), enabling bandgap engineering across UV, visible, and near-IR wavelengths as well as tailored electronic properties.

In power electronics, GaN's key mechanism is the AlGaN/GaN heterojunction: the spontaneous and piezoelectric polarisation mismatch at the interface creates a two-dimensional electron gas (2DEG) without intentional doping, yielding electron sheet densities ~10¹³ cm⁻² and mobilities ~2000 cm²/V·s — far exceeding silicon. This makes lateral GaN HEMTs (high-electron-mobility transistors) the dominant device for sub-650V high-frequency switching. They are the enabling device for the PSU miniaturisation driving AI datacentre rack density and USB-C fast chargers. The thesis **Gan Power Datacentre** tracks GaN's expected capture of ≥30% of AI datacentre PSU stages by 2028.

In RF, GaN-on-SiC is the standard for 5G base station power amplifiers, defence radar (AESA arrays), and satellite communications, where power density and thermal handling at microwave frequencies exceed anything silicon LDMOS achieves.

GaN is grown by MOCVD (see [MOCVD / MBE](/sotf-site/manufacturing/equipment-processes/mocvd-mbe/)) on SiC substrates (highest performance), silicon (lowest cost), or native GaN boules. The SiC substrate path benefits from the thermal extraction advantage described in [Silicon Carbide](/sotf-site/materials/substrates/silicon-carbide/).

## Frontier

- Will GaN-on-Si reach 650V yield and reliability parity with GaN-on-SiC at 8-inch, or does substrate-induced defect density remain a ceiling?
- Can GaN power ICs (gate driver + FET monolithic) pull further system integration away from silicon ASIC + discrete topology?
- Does GaN capture any share above 650V (1200V class) once vertical GaN device architectures mature, challenging SiC's lock on EV traction?
