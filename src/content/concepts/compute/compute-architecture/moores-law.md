---
type: concept
slug: moores-law
canonical_name: Moore's Law
aliases:
- moores law
- moore's law
parent_concepts:
- compute-architecture
related_concepts:
- dennard-scaling
- memory-wall
- gaa-nanosheet
- cfet
- backside-power-delivery
sources: []
frontier:
- When does cost-per-transistor stop improving outright (not just slow), and at which node?
last_updated: '2026-06-16'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: dennard-scaling
  name: Dennard Scaling
  path: /sotf-site/compute/compute-architecture/dennard-scaling/
  macro: compute
- slug: memory-wall
  name: The Memory Wall
  path: /sotf-site/compute/compute-architecture/memory-wall/
  macro: compute
- slug: gaa-nanosheet
  name: GAA / Nanosheet Transistor
  path: /sotf-site/compute/compute-architecture/gaa-nanosheet/
  macro: compute
- slug: cfet
  name: CFET (Complementary FET)
  path: /sotf-site/compute/compute-architecture/cfet/
  macro: compute
- slug: backside-power-delivery
  name: Backside Power Delivery (BPD)
  path: /sotf-site/compute/compute-architecture/backside-power-delivery/
  macro: compute
---
Gordon Moore's 1965 observation (revised in 1975) that the number of transistors on a chip doubles roughly every two years. It is an economic and manufacturing trend, not a law of physics, and it held for decades on the back of lithography.

## What is actually slowing

Two things are often conflated and should be kept apart:

- **Density** is still improving. New device structures (GAA nanosheets, [CFET (Complementary FET)](/sotf-site/compute/compute-architecture/cfet/), [Backside Power Delivery (BPD)](/sotf-site/compute/compute-architecture/backside-power-delivery/)) keep packing more transistors in.
- **The economics and the energy stopped paying.** Cost-per-transistor has flattened below roughly 7nm, the number of foundries at the leading edge has collapsed to a handful (see **Sovereignty Semi Bifurcation**), and the per-watt gains ended when [Dennard Scaling](/sotf-site/compute/compute-architecture/dennard-scaling/) broke.

So "Moore's Law is dead" is the wrong headline. Transistors still shrink; what stopped paying is the cost and power curve. EUV and its successors keep density moving but do not restore the free lunch (see **Beyond Euv Not In 2020S**).

## Why it matters here

Once density gains no longer translate into cheaper, cooler compute, architecture has to do the work that process used to. That is the opening for "post-Moore" approaches, and the binding constraint that those approaches target is data movement and the [The Memory Wall](/sotf-site/compute/compute-architecture/memory-wall/), not transistor count.

## Connected ideas

<!-- dataview block stripped for public site -->
