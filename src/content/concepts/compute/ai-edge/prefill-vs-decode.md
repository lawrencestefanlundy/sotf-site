---
type: concept
slug: prefill-vs-decode
canonical_name: Prefill vs Decode (LLM inference phases)
aliases:
- llm-decode
- decode-phase
- prefill-phase
- autoregressive-decode
kind: concept
parent_concepts:
- ai-infrastructure
related_concepts:
- in-memory-computing
- memcapacitor
- hbm
- weight-reuse-factor
- charge-domain-compute
sources: []
frontier:
- Does the prefill/decode split drive disaggregated inference hardware — separate silicon for each phase — and if so who supplies the decode-optimised part?
- As reasoning models (long chains of thought) grow, does decode's share of total inference cost rise far enough to justify dedicated decode accelerators?
- Does speculative decoding / parallel decode erode the "decode is serial and memory-bound" framing before HBM-free silicon reaches volume?
last_updated: '2026-06-14'
tags:
- concept
- ai-infrastructure
- llm-inference
- memory-bound
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors:
- slug: in-memory-computing
  name: In-Memory Computing
  path: /sotf-site/memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: memcapacitor
  name: Memcapacitor
  path: /sotf-site/memory/emerging-memory/memcapacitor/
  macro: memory
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /sotf-site/memory/mainstream-memory/hbm/
  macro: memory
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /sotf-site/compute/non-conventional/charge-domain-compute/
  macro: compute
---
## The two phases

**Prefill** processes the input prompt. All prompt tokens are available at once, so the matrix multiplications are large and parallel: high **arithmetic intensity** (many FLOPs per byte of weights fetched). Prefill is **compute-bound** — it saturates the FLOP units of a GPU and benefits from raw TFLOPS. This is the phase GPUs are good at.

**Decode** generates output tokens one at a time, autoregressively. Each new token requires a full pass over the model weights, but produces only a single token's worth of compute. The **weight reuse factor** is ~1: you fetch the entire weight set from memory to produce one token. Decode is therefore **memory-bandwidth-bound** — it is limited by how fast weights can be streamed from memory to the compute units, not by FLOPs. Adding more FLOPs does nothing; adding (or avoiding the need for) memory bandwidth is everything.

## Why this matters for the thesis

The memory wall binds at decode, not prefill. HBM exists to feed decode bandwidth in the datacentre; the **Hbm Bottleneck** is fundamentally a decode-phase problem. Three consequences:

1. **Edge AI and datacentre decode are the same problem.** Edge inference is bandwidth-bound because power and form factor rule out HBM; datacentre decode is bandwidth-bound because of the weight-reuse-factor-1 physics. The same architectural fix — compute-in-memory that bypasses the memory–compute boundary — addresses both. This is the core of the **Memcapacitor Compute Memory Bound Ai** device thesis and the **Hbm Free Inference Architectures** market thesis.

2. **Decode's cost share is rising.** Reasoning models (long chains of thought), agentic workloads, and long-context generation all lengthen the decode phase relative to prefill. The more decode dominates, the larger the addressable market for decode-optimised silicon.

## Where each player sits

## Caveat

Speculative decoding, parallel sampling, and batching partially recover arithmetic intensity in decode by processing multiple candidate tokens or requests together. None of these eliminate the underlying weight-streaming cost, but they soften how memory-bound decode is in practice — a watch item for whether the HBM-free thesis window stays open.
