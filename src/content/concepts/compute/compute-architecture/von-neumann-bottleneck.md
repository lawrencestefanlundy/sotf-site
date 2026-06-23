---
type: concept
slug: von-neumann-bottleneck
canonical_name: Von Neumann Bottleneck
aliases:
- von neumann bottleneck
- data-movement bottleneck
parent_concepts:
- compute-paradigms
related_concepts:
- memory-wall
- in-memory-computing
- processing-in-memory
- charge-domain-compute
sources: []
frontier:
- At what model size / batch regime does moving weights stop dominating energy, if ever?
last_updated: '2026-06-16'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: memory-wall
  name: The Memory Wall
  path: /sotf-site/compute/compute-architecture/memory-wall/
  macro: compute
- slug: in-memory-computing
  name: In-Memory Computing
  path: /sotf-site/memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /sotf-site/memory/emerging-memory/processing-in-memory/
  macro: memory
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /sotf-site/compute/non-conventional/charge-domain-compute/
  macro: compute
---
The classic computer keeps memory and processing in separate places, so instructions and data must shuttle back and forth across a bus. When the work is data-heavy and arithmetic-light, that shuttling, not the arithmetic, sets the cost.

## Why it dominates AI inference

Neural-network inference is mostly matrix-vector multiplication: stream a large weight set from memory, do one cheap multiply-accumulate per weight, repeat. The arithmetic is nearly free; fetching the operands is not. The canonical figures (Horowitz, "Computing's Energy Problem", ISSCC 2014): a floating-point operation costs on the order of a picojoule (~0.4-3.7 pJ depending on type/precision), while an off-chip DRAM access costs ~1.3-2.6 nJ, i.e. hundreds to ~1,000x more energy to *fetch* the value than to compute with it. So the energy and latency of inference are set by data movement, not FLOPS. The bandwidth-shaped sibling, quantified, is the [The Memory Wall](/sotf-site/compute/compute-architecture/memory-wall/) (compute +60,000x vs DRAM bandwidth +100x over 20 years, **2024 Gholami Ai And Memory Wall**).

## Why it matters here

This is the root justification for the whole in-memory and near-memory family: if moving the data is the cost, stop moving it. [In-Memory Computing](/sotf-site/memory/emerging-memory/in-memory-computing/) and [Charge-Domain Compute](/sotf-site/compute/non-conventional/charge-domain-compute/) fuse the multiply into the memory array; [Processing-in-Memory (PIM)](/sotf-site/memory/emerging-memory/processing-in-memory/) puts logic next to the memory banks; [Near-Memory Compute](/sotf-site/memory/emerging-memory/near-memory-compute/) stacks memory on the compute die. The bandwidth-shaped sibling of this problem is the [The Memory Wall](/sotf-site/compute/compute-architecture/memory-wall/).

## Connected ideas

<!-- dataview block stripped for public site -->
