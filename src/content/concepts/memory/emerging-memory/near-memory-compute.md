---
type: concept
slug: near-memory-compute
canonical_name: Near-Memory Compute
aliases:
- near-memory computing
- near memory compute
parent_concepts:
- memory
related_concepts:
- in-memory-computing
- processing-in-memory
- memory-wall
- von-neumann-bottleneck
- hbm
- 3d-monolithic-integration
- chiplets
sources: []
frontier:
- Does "digital plus 3D-stacked memory" close the energy gap before analog in-memory compute scales?
last_updated: '2026-06-16'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: in-memory-computing
  name: In-Memory Computing
  path: /sotf-site/memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /sotf-site/memory/emerging-memory/processing-in-memory/
  macro: memory
- slug: memory-wall
  name: The Memory Wall
  path: /sotf-site/compute/compute-architecture/memory-wall/
  macro: compute
- slug: von-neumann-bottleneck
  name: Von Neumann Bottleneck
  path: /sotf-site/compute/compute-architecture/von-neumann-bottleneck/
  macro: compute
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /sotf-site/memory/mainstream-memory/hbm/
  macro: memory
- slug: 3d-monolithic-integration
  name: 3D Monolithic Integration
  path: /sotf-site/compute/compute-architecture/3d-monolithic-integration/
  macro: compute
- slug: chiplets
  name: Chiplets
  path: /sotf-site/compute/compute-architecture/chiplets/
  macro: compute
---
The third option between a conventional von Neumann machine and true in-memory compute. Keep the compute general and digital, but move the memory physically closer to it, so the data has less far to travel. The compute and the memory stay separate functions; only the distance changes.

## How it differs from its neighbours

The shared goal is to attack the [Von Neumann Bottleneck](/sotf-site/compute/compute-architecture/von-neumann-bottleneck/) and the [The Memory Wall](/sotf-site/compute/compute-architecture/memory-wall/) by cutting data movement; near-memory does it with packaging rather than with a new device.

## Why it matters here

Near-memory is the lowest-risk, most-productised answer (it uses standard cells and standard memory), which is exactly why it commoditises: 3D-stacked SRAM-on-logic is becoming a foundry service. It is a key category in the **Hbm Free Inference Architectures** taxonomy and the foil against which in-memory and charge-domain approaches have to justify their device risk.

## Connected ideas

<!-- dataview block stripped for public site -->
