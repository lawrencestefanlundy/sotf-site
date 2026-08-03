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
sources:
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2025-08-12-scaling-the-memory-wall-the-rise-and-roadmap-of-hbm]]'
frontier:
- Does the binding constraint shift from memory bandwidth to memory capacity (KV cache) as context windows and agentic multi-step grow?
- How far can HBM push the wall back before cost or supply caps it (HBM4/HBM5)?
last_updated: '2026-06-22'
tags:
- concept
descendants:
- inference-economics
- token-cost-stack
mention_count: 12
sources_7d: 1
sources_30d: 2
recent_mentions:
- slug: 2026-07-31-positron-research-sprint
  title: 'Positron AI research sprint: architecture, funding, customers, manufacturing'
  date: '2026-07-31'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2026-01-22-ai-chips-computeram-and-the-future
  title: 'AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara'
  date: '2026-01-22'
  kind: substack
- slug: 2025-08-12-scaling-the-memory-wall-the-rise-and-roadmap-of-hbm
  title: 'Scaling the Memory Wall: The Rise and Roadmap of HBM'
  date: '2025-08-12'
  kind: web
neighbors:
- slug: von-neumann-bottleneck
  name: Von Neumann Bottleneck
  path: /compute/compute-architecture/von-neumann-bottleneck/
  macro: compute
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /memory/mainstream-memory/hbm/
  macro: memory
- slug: hbm-cowos-bottleneck
  name: HBM / CoWoS Bottleneck
  path: /compute/compute-architecture/hbm-cowos-bottleneck/
  macro: compute
- slug: prefill-vs-decode
  name: Prefill vs Decode (LLM inference phases)
  path: /compute/ai-edge/prefill-vs-decode/
  macro: compute
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /memory/emerging-memory/processing-in-memory/
  macro: memory
- slug: in-memory-computing
  name: In-Memory Computing
  path: /memory/emerging-memory/in-memory-computing/
  macro: memory
---
The growing gap between how fast processors can compute and how fast memory can feed them. Coined by Wulf and McKee (1995): if compute throughput grows faster than memory bandwidth and latency, then sooner or later every workload becomes memory-bound, and adding more compute stops helping.

## By the numbers (the divergence)

- **20-year divergence (Gholami et al., "AI and Memory Wall", IEEE Micro 2024 / Hot Chips 2023, **2024 Gholami Ai And Memory Wall**):** peak hardware compute grew **~60,000x**, DRAM bandwidth **~100x**, interconnect bandwidth **~30x**. Underlying rates: FLOPS **~3.0x / 2yr**, DRAM bandwidth **~1.6x**, interconnect **~1.4x**. Compute compounds ~2x faster than the memory feeding it, so the memory-bound share of work only grows.
- **Energy (Horowitz, ISSCC 2014):** a floating-point op costs on the order of a picojoule (FP range ~0.4-3.7 pJ); an off-chip DRAM fetch costs **~1.3-2.6 nJ**, i.e. hundreds to ~1,000x more energy to *fetch* a value than to compute with it. Data movement, not arithmetic, sets the energy bill.
- **Bandwidth today:** an HBM3E stack delivers ~1.2 TB/s on a 1,024-bit bus; HBM4 doubles the bus to 2,048-bit for >2 TB/s/stack (see [HBM (High-Bandwidth Memory)](/memory/mainstream-memory/hbm/)). At the accelerator level: H100 (HBM3) 3.35 TB/s, H200 (HBM3E) 4.8 TB/s, B200 (HBM3E) ~8 TB/s, versus a DDR5 channel in the tens of GB/s.
- **The decode consequence:** LLM decode reads the full weight set per token (reuse ≈ 1), so single-stream throughput ≈ aggregate memory bandwidth ÷ model size, landing in the tens of tokens/s for a frontier model while the compute sits mostly idle (see [Prefill vs Decode (LLM inference phases)](/compute/ai-edge/prefill-vs-decode/)).

## Why it binds now

AI inference made the wall the dominant constraint. A modern accelerator can do far more multiply-accumulates per second than its memory can supply operands for, so on memory-bandwidth-bound workloads the expensive silicon sits idle waiting on data. The economics compound it: [HBM (High-Bandwidth Memory)](/memory/mainstream-memory/hbm/) (stacked DRAM with through-silicon vias) is the industry's answer to push the wall back, but it is supply-constrained and expensive (see **Hbm Bottleneck** and [HBM / CoWoS Bottleneck](/compute/compute-architecture/hbm-cowos-bottleneck/)).

## Where it bites hardest

- **LLM decode:** each generated token streams the full weight set from memory, so decode is bandwidth-bound while prefill is compute-bound (see [Prefill vs Decode (LLM inference phases)](/compute/ai-edge/prefill-vs-decode/)).
- **The edge:** a hard power and thermal budget caps how much memory traffic is affordable.

## Architectural responses

Two families. Move memory closer to compute ([Near-Memory Compute](/memory/emerging-memory/near-memory-compute/), HBM), or do the compute inside the memory so the data never moves ([In-Memory Computing](/memory/emerging-memory/in-memory-computing/), [Processing-in-Memory (PIM)](/memory/emerging-memory/processing-in-memory/), [Charge-Domain Compute](/compute/non-conventional/charge-domain-compute/)). Most of the post-Moore accelerator landscape is a response to this one wall.

## Connected ideas

<!-- dataview block stripped for public site -->
