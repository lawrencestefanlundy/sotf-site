---
type: concept
slug: gallium-nitride
aliases:
- GaN
- gallium nitride
- GaN-on-Si
- GaN-on-SiC
canonical_name: Gallium Nitride
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
sources:
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-05-26-semianalysis-800vdc-revolution]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
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
mention_count: 26
sources_7d: 2
sources_30d: 5
recent_mentions:
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-22-sintered-metal-die-attach-landscape
  title: Sintered-silver / sintered-copper die-attach landscape — physics, incumbents, AI-migration question (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-05-26-semianalysis-800vdc-revolution
  title: Inside the 800VDC Revolution – Part 1
  date: '2026-05-26'
  kind: web
- slug: 2026-04-20-fixing-the-gan-problem
  title: Fixing the GaN Problem
  date: '2026-04-20'
  kind: web
- slug: 2026-03-08-diamonds-are-semiconductors-best-friend
  title: Diamonds are Semiconductors' Best Friend 2026
  date: '2026-03-08'
  kind: web
neighbors:
- slug: wide-bandgap-semiconductors
  name: Wide-Bandgap Semiconductors
  path: /materials/substrates/wide-bandgap-semiconductors/
  macro: materials
- slug: silicon-carbide
  name: Silicon Carbide
  path: /materials/substrates/silicon-carbide/
  macro: materials
- slug: aluminium-gallium-nitride
  name: Aluminium Gallium Nitride
  path: /materials/functional-layers/aluminium-gallium-nitride/
  macro: materials
- slug: indium-gallium-nitride
  name: Indium Gallium Nitride
  path: /materials/functional-layers/indium-gallium-nitride/
  macro: materials
- slug: power-electronics
  name: Power Electronics
  path: /energy-power/power-electronics/power-electronics/
  macro: energy-power
- slug: compound-semiconductors
  name: Compound Semiconductors
  path: /materials/substrates/compound-semiconductors/
  macro: materials
- slug: mocvd-mbe
  name: MOCVD / MBE
  path: /manufacturing/equipment-processes/mocvd-mbe/
  macro: manufacturing
---
Gallium nitride (GaN) is a III-nitride wide-bandgap semiconductor with a direct bandgap of 3.4 eV. It is the parent binary compound of a family of alloys spanning [Aluminium Gallium Nitride](/materials/functional-layers/aluminium-gallium-nitride/) (AlGaN, wider bandgap) and [Indium Gallium Nitride](/materials/functional-layers/indium-gallium-nitride/) (InGaN, narrower bandgap), enabling bandgap engineering across UV, visible, and near-IR wavelengths as well as tailored electronic properties.

In power electronics, GaN's key mechanism is the AlGaN/GaN heterojunction: the spontaneous and piezoelectric polarisation mismatch at the interface creates a two-dimensional electron gas (2DEG) without intentional doping, yielding electron sheet densities ~10¹³ cm⁻² and mobilities ~2000 cm²/V·s — far exceeding silicon. This makes lateral GaN HEMTs (high-electron-mobility transistors) the dominant device for sub-650V high-frequency switching. They are the enabling device for the PSU miniaturisation driving AI datacentre rack density and USB-C fast chargers. The thesis **Gan Power Datacentre** tracks GaN's expected capture of ≥30% of AI datacentre PSU stages by 2028.

In RF, GaN-on-SiC is the standard for 5G base station power amplifiers, defence radar (AESA arrays), and satellite communications, where power density and thermal handling at microwave frequencies exceed anything silicon LDMOS achieves.

GaN is grown by MOCVD (see [MOCVD / MBE](/manufacturing/equipment-processes/mocvd-mbe/)) on SiC substrates (highest performance), silicon (lowest cost), or native GaN boules. The SiC substrate path benefits from the thermal extraction advantage described in [Silicon Carbide](/materials/substrates/silicon-carbide/).

## Frontier

- Will GaN-on-Si reach 650V yield and reliability parity with GaN-on-SiC at 8-inch, or does substrate-induced defect density remain a ceiling?
- Can GaN power ICs (gate driver + FET monolithic) pull further system integration away from silicon ASIC + discrete topology?
- Does GaN capture any share above 650V (1200V class) once vertical GaN device architectures mature, challenging SiC's lock on EV traction?
