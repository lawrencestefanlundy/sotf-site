---
type: concept
slug: fefet
canonical_name: FeFET (Ferroelectric FET)
aliases:
- ferroelectric fet
- ferroelectric field-effect transistor
- fe-fet
parent_concepts:
- feram
related_concepts:
- feram
- rram-reram
- charge-domain-compute
- in-memory-computing
- embedded-non-volatile-memory
sources:
- '[[2024-yole-emerging-memories-2024]]'
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2025-26-lapedus-next-gen-ferroelectric-memory]]'
frontier:
- Can HfO2 FeFET endurance and retention reach the bar for compute-in-memory (not just eNVM) at scale?
last_updated: '2026-06-16'
tags:
- concept
mention_count: 14
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-26-lapedus-next-gen-ferroelectric-memory
  title: Next-Gen Ferroelectric Memory Still A Work In Progress
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
neighbors:
- slug: feram
  name: FeRAM (Ferroelectric)
  path: /memory/mainstream-memory/feram/
  macro: memory
- slug: rram-reram
  name: RRAM / ReRAM
  path: /memory/emerging-memory/rram-reram/
  macro: memory
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /compute/non-conventional/charge-domain-compute/
  macro: compute
- slug: in-memory-computing
  name: In-Memory Computing
  path: /memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: embedded-non-volatile-memory
  name: Embedded Non-Volatile Memory
  path: /memory/emerging-memory/embedded-non-volatile-memory/
  macro: memory
---
A field-effect transistor whose gate stack includes a ferroelectric layer (modern devices use doped hafnium oxide). The polarisation state of the ferroelectric shifts the transistor threshold voltage, so the device itself stores a non-volatile bit (or multiple levels), switched by an electric field at very low energy. Distinct from [FeRAM (Ferroelectric)](/memory/mainstream-memory/feram/), which stores charge in a separate ferroelectric capacitor.

## Why it matters for compute

## Limitations

Endurance (polarisation fatigue over write cycles), retention, device-to-device variability, and scaling of the ferroelectric film thickness. These are why FeFET, like the rest of [Analog In-Memory Compute](/memory/emerging-memory/analog-in-memory-compute/), is not yet a settled volume technology.

## Cluster role

*Hand-authored synthesis, 16 June 2026.*

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
