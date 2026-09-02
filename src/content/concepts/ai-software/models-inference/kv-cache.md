---
type: concept
slug: kv-cache
canonical_name: KV cache
aliases:
- KV-cache
- key-value cache
- attention cache
parent_concepts:
- inference
related_concepts:
- inference
- inference-economics
- edge-inference
sources:
- '[[2026-07-17-the-once-and-future-kimi]]'
- '[[2025-10-23-data-value-migrates-to-retrieval-layer-agentic-databases]]'
- '[[2026-07-10-workload-phase-silicon-sweep]]'
- '[[2026-06-18-sensifai-hybrids-deck]]'
- '[[2026-06-09-semianalysis-deepseek-v4-inference]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-01-01-data-value-migrates-to-retrieval-layer-ai-agent-memory-2026]]'
- '[[2026-07-07-high-bandwidth-flash-the-full-report]]'
- '[[2026-03-24-data-value-migrates-to-retrieval-layer-gtc-2026-the]]'
- '[[2026-07-15-kimi-k3-launch-moonshot]]'
- '[[2025-10-09-data-value-migrates-to-retrieval-layer-lmcache-an-efficient]]'
- '[[2026-06-02-agentic-runtime-silicon-necessity]]'
frontier:
- Which HBM-light architectures have a published KV-bandwidth number at a stated context length, rather than only a weight-storage number?
- Does disaggregated prefill/decode serving open a decode-only socket where the KV cache, not the weights, is the thing being optimised?
- At what context length does KV traffic overtake weight traffic for a given model, and how does that crossover move as models adopt GQA/MLA and aggressive quantisation?
last_updated: 2026-07-29
tags:
- concept
mention_count: 52
sources_7d: 2
sources_30d: 16
recent_mentions:
- slug: 2026-07-17-the-once-and-future-kimi
  title: The Once and Future Kimi
  date: '2026-07-17'
  kind: substack
- slug: 2026-07-15-kimi-k3-launch-moonshot
  title: Kimi K3 — Moonshot launch post (architecture, quantisation, serving requirements)
  date: '2026-07-15'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-10-workload-phase-silicon-sweep
  title: 'Workload-phase silicon sweep: pre-training / RL / prefill / decode procurement split'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-07-high-bandwidth-flash-the-full-report
  title: 'High Bandwidth Flash: The Full Report'
  date: '2026-07-07'
  kind: web
- slug: 2026-06-18-sensifai-hybrids-deck
  title: SensifAI — Funding Round deck (sensifai.vercel.app/hybrids)
  date: '2026-06-18'
  kind: web
- slug: 2026-06-09-semianalysis-deepseek-v4-inference
  title: DeepSeekV4 1.6T Day 0 to Day 43 Performance Over Time - Huawei, GB300 NVL72, MI355X, B200
  date: '2026-06-09'
  kind: web
- slug: 2026-06-02-agentic-runtime-silicon-necessity
  title: Deep-research dossier — does the stateful agent runtime / control-plane layer need a novel silicon primitive?
  date: '2026-06-02'
  kind: web
neighbors:
- slug: inference
  name: Inference
  path: /ai-software/models-inference/inference/
  macro: ai-software
- slug: inference-economics
  name: 'Inference economics: the two customer KPIs'
  path: /ai-software/models-inference/inference-economics/
  macro: ai-software
- slug: edge-inference
  name: Edge Inference
  path: /compute/ai-edge/edge-inference/
  macro: compute
---
The per-request state a transformer accumulates during autoregressive decoding: for every token generated, every layer writes one key and one value vector, and every subsequent token reads all of them back. It is the reason decode is memory-bandwidth-bound rather than compute-bound, alongside the weights.

## Why it belongs in the KB as its own concept

The **Hbm Free Inference Architectures** theme is about routing around HBM. Almost every candidate architecture does that by making **weights** cheap to reach: analog in-memory compute, processing-in-memory, wafer-scale SRAM, varactor and memcapacitor storage. All of those attack the weight half of decode bandwidth.

**The KV cache is the half that cannot be attacked the same way.** It does not exist until inference starts, it grows by one entry per token per layer, and it is per-request. So it can never be pre-loaded into a fixed physical weight, however exotic the substrate. Any "no HBM" claim is really a claim about weights until the KV number is stated.

This distinction is the sizing screen the theme now applies: **ask for KV bandwidth at a target context length, not weight storage.**

## The arithmetic

For a GQA model, bytes of KV per token = `layers × kv_heads × head_dim × 2 (K and V) × bytes_per_element`.

Worked on Llama 3.1 8B (32 layers, 8 KV heads, head_dim 128, fp16):

- per token: 32 × 8 × 128 × 2 × 2 = **131 KB**
- at 8K context: ~**1.07 GB**, read in full for every token generated
- at a claimed 13 µs/token: ~**80 TB/s** of KV read bandwidth
- for comparison, an AMD Versal HBM part delivers ~**0.8 TB/s**

Two orders of magnitude, and it does not close at short context — 512 tokens still demands ~5 TB/s. The weight side of the same workload is 8-16 GB depending on precision, so at long context KV traffic is the comparable term, not a rounding error.

## Where this bit

## What it implies for where the HBM-light wedge actually is

If KV is irreducible, the defensible wedge for a weight-stationary substrate is **small-model, short-context, latency-bound** work — real-time control loops, qLDPC syndrome decoding, plasma control, robotics motion planning — where the model fits, the context is tiny, and settle time is the binding constraint.

It is **not** frontier LLM decode, which is where these companies repeatedly drift because that is where the fundraising narrative lives. The drift is predictable enough to be a screening signal in itself.

## The batching crossover, computed (31 Jul 2026)

The load-bearing arithmetic, done once here so it does not get re-derived. Batching amortises **weight** reads across users; it does **not** amortise KV reads, because each user's cache is read for their own attention. Weight traffic is therefore flat in the batch and KV traffic is linear, so there is a batch size past which adding a user costs more bandwidth than it saves.

From the published Llama 3.1 70B config (80 layers, 8 KV heads under GQA, head_dim 128, fp16 KV):

| Quantity | Value |
|---|---|
| KV cache per token, per user | **320 KB** (2 x 80 x 8 x 128 x 2 bytes) |
| 8,000-token context, one user | 2.6 GB |
| 128,000-token context, one user | 41 GB |
| 100 users at 8K context | 256 GB, against a B200's 192 GB — out of memory before the model loads |

Against fp8 weights (70 GB fetched once per token step, whatever the batch):

- **8K context: crossover at ~29 concurrent users**
- **128K context: crossover at ~1.8 users**

Caveat: fp8 weights with fp16 KV is the common deployment, not the only one, and MLA-style architectures (DeepSeek-V3) compress the per-token cache by roughly an order of magnitude, which moves the crossover right. That compression is itself the counterweight tracked on **Hbm Free Inference Architectures**.
