---
type: concept
slug: 3d-monolithic-integration
canonical_name: 3D Monolithic Integration
aliases:
- monolithic-3d
- 3d-monolithic-growth
- m3d
kind: technology
parent_concepts:
- advanced-packaging
- compute-architecture
related_concepts:
- memcapacitor
- chiplets-architecture-share
- hbm
- 3d-stacking
sources:
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2024-yole-advanced-packaging-2024]]'
frontier:
- Does monolithic 3D growth actually yield at production scale — the binding risk for SEMRON's CapRAM density story?
- Where is the thermal ceiling — how many monolithic compute layers can stack before heat removal caps the design?
- Does monolithic 3D (grown layers) beat hybrid-bonded 3D (stacked dies, d-Matrix 3DIMC) on cost-per-effective-TOPS, or do they serve different sockets?
last_updated: '2026-06-14'
tags:
- concept
- advanced-packaging
- compute-architecture
- 3d
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: memcapacitor
  name: Memcapacitor
  path: /sotf-site/memory/emerging-memory/memcapacitor/
  macro: memory
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /sotf-site/memory/mainstream-memory/hbm/
  macro: memory
---
## Monolithic 3D vs stacked 3D

Two very different things both get called "3D":

- **Stacked / hybrid-bonded 3D (the mainstream).** Separate dies are fabricated, then bonded — through-silicon vias (TSVs) or copper hybrid bonding. HBM is stacked DRAM. d-Matrix's 3DIMC stacks DRAM on compute via packaging. TSMC CoWoS, SoIC. Each layer is a fully-built die; the dies are joined. Mature, but limited by bonding pitch and the cost of each die.
- **Monolithic 3D (M3D).** Layers are grown **sequentially on the same substrate** in the back-end-of-line (BEOL), at low enough temperature that the lower layers survive. There is no bonding step and no die-to-die interface — the vertical connections are normal interconnect vias, so they are tiny and dense (orders of magnitude finer pitch than hybrid bonding). The catch: the thermal budget of BEOL processing severely constrains what devices you can build in the upper layers, which is why M3D has historically been confined to memory and passive structures, not high-performance logic.

## Why memcapacitor fits monolithic 3D

## Why it is also the risk

The competitive counter is that hybrid-bonded digital 3D (**D Matrix** 3DIMC, ~10× HBM4 bandwidth) reaches the memory-bound socket first using mature bonding, before monolithic growth proves out. That device-class race is the central frontier question in **Memcapacitor Compute Memory Bound Ai**.
