---
type: concept
slug: memory-wall
canonical_name: The Memory Wall
aliases:
- memory bandwidth wall
parent_concepts:
- memory
related_concepts:
- von-neumann-bottleneck
- hbm
- hbm-cowos-bottleneck
- prefill-vs-decode
- processing-in-memory
- in-memory-computing
sources: []
frontier:
- Does the binding constraint shift from memory bandwidth to memory capacity (KV cache) as context windows and agentic multi-step grow?
- How far can HBM push the wall back before cost or supply caps it (HBM4/HBM5)?
last_updated: '2026-06-16'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-16-hbm-supercycle-2026
  title: 'HBM supercycle 2026: sold out, +20% pricing, HBM4 ramp, ASIC-HBM 35x'
  date: '2026-06-16'
  kind: web
neighbors:
- slug: von-neumann-bottleneck
  name: Von Neumann Bottleneck
  path: /sotf-site/compute/compute-architecture/von-neumann-bottleneck/
  macro: compute
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /sotf-site/memory/mainstream-memory/hbm/
  macro: memory
- slug: hbm-cowos-bottleneck
  name: HBM / CoWoS Bottleneck
  path: /sotf-site/compute/compute-architecture/hbm-cowos-bottleneck/
  macro: compute
- slug: prefill-vs-decode
  name: Prefill vs Decode (LLM inference phases)
  path: /sotf-site/compute/ai-edge/prefill-vs-decode/
  macro: compute
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /sotf-site/memory/emerging-memory/processing-in-memory/
  macro: memory
- slug: in-memory-computing
  name: In-Memory Computing
  path: /sotf-site/memory/emerging-memory/in-memory-computing/
  macro: memory
---
The growing gap between how fast processors can compute and how fast memory can feed them. Coined by Wulf and McKee (1995): if compute throughput grows faster than memory bandwidth and latency, then sooner or later every workload becomes memory-bound, and adding more compute stops helping.

## Why it binds now

AI inference made the wall the dominant constraint. A modern accelerator can do far more multiply-accumulates per second than its memory can supply operands for, so on memory-bandwidth-bound workloads the expensive silicon sits idle waiting on data. The economics compound it: [HBM (High-Bandwidth Memory)](/sotf-site/memory/mainstream-memory/hbm/) (stacked DRAM with through-silicon vias) is the industry's answer to push the wall back, but it is supply-constrained and expensive (see **Hbm Bottleneck** and [HBM / CoWoS Bottleneck](/sotf-site/compute/compute-architecture/hbm-cowos-bottleneck/)).

## Where it bites hardest

- **LLM decode:** each generated token streams the full weight set from memory, so decode is bandwidth-bound while prefill is compute-bound (see [Prefill vs Decode (LLM inference phases)](/sotf-site/compute/ai-edge/prefill-vs-decode/)).
- **The edge:** a hard power and thermal budget caps how much memory traffic is affordable.

## Architectural responses

Two families. Move memory closer to compute ([Near-Memory Compute](/sotf-site/memory/emerging-memory/near-memory-compute/), HBM), or do the compute inside the memory so the data never moves ([In-Memory Computing](/sotf-site/memory/emerging-memory/in-memory-computing/), [Processing-in-Memory (PIM)](/sotf-site/memory/emerging-memory/processing-in-memory/), [Charge-Domain Compute](/sotf-site/compute/non-conventional/charge-domain-compute/)). Most of the post-Moore accelerator landscape is a response to this one wall.

## Connected ideas

<!-- dataview block stripped for public site -->
