---
type: concept
slug: dennard-scaling
canonical_name: Dennard Scaling
aliases:
- dennard scaling
- mosfet scaling
parent_concepts:
- compute-architecture
related_concepts:
- moores-law
- memory-wall
- backside-power-delivery
sources: []
frontier:
- Do new device structures (GAA, CFET) recover any per-watt scaling, or only density?
last_updated: '2026-06-16'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: moores-law
  name: Moore's Law
  path: /sotf-site/compute/compute-architecture/moores-law/
  macro: compute
- slug: memory-wall
  name: The Memory Wall
  path: /sotf-site/compute/compute-architecture/memory-wall/
  macro: compute
- slug: backside-power-delivery
  name: Backside Power Delivery (BPD)
  path: /sotf-site/compute/compute-architecture/backside-power-delivery/
  macro: compute
---
Dennard and colleagues (IBM, 1974) observed that as a transistor shrinks, you can scale voltage and current down with its dimensions so that power density stays roughly constant. The practical consequence: each new process node gave you more transistors AND more performance at the same power and cost. This, not [Moore's Law](/sotf-site/compute/compute-architecture/moores-law/) alone, is what made five decades of "faster every year for free" possible.

## Why it ended

Dennard scaling broke down around 2005 to 2007. Below roughly 1 volt, threshold voltage and leakage current stopped cooperating: you could keep shrinking transistors (density continued), but you could no longer drop voltage proportionally, so power density started rising. The industry's response was to stop chasing single-thread frequency and go multicore, which led to "dark silicon" (more transistors than you can power on at once).

## Why it matters here

The end of Dennard scaling is the precise sense in which "Moore's Law stopped paying": transistors kept shrinking, but the free performance-per-watt gains stopped. With logic no longer getting cheaper to run, the binding constraint migrated to data movement and the [The Memory Wall](/sotf-site/compute/compute-architecture/memory-wall/). That migration is what the post-Moore architecture landscape is built to attack.

## Connected ideas

<!-- dataview block stripped for public site -->
