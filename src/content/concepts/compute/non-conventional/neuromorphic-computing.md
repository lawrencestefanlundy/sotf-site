---
type: concept
slug: neuromorphic-computing
canonical_name: Neuromorphic Computing
aliases: []
kind: technology
parent_concepts:
- compute
- non-conventional
related_concepts: []
sources:
- '[[2025-09-23-the-compute-gradient]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2023-06-30-e06-the-model-t-moment-for-bits-llms]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2026-06-17-femtoai-spu-ces2026]]'
frontier:
- Does any spiking / neuromorphic chip find a volume socket beyond research and niche sensing?
- Do analog / memcapacitor devices become the substrate for neuromorphic, or stay separate?
last_updated: '2026-06-09'
tags:
- concept
- technology
mention_count: 39
last_reorg_date: '2026-05-14'
descendants:
- spiking-neural-networks
sources_7d: 2
sources_30d: 16
recent_mentions:
- slug: 2026-07-01-hearing-aid-market-structure-edge-ai-beachhead
  title: Hearing-aid market structure as an edge-AI silicon beachhead (size, growth, concentration, commoditisation)
  date: '2026-07-01'
  kind: web
- slug: 2026-06-17-femtoai-spu-ces2026
  title: femtoAI to Highlight its Sparse Processing Unit Edge AI Accelerator at CES 2026
  date: '2026-06-17'
  kind: web
- slug: 2026-01-22-ai-chips-computeram-and-the-future
  title: 'AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara'
  date: '2026-01-22'
  kind: substack
- slug: 2025-09-23-the-compute-gradient
  title: The Compute Gradient
  date: '2025-09-23'
  kind: substack
- slug: 2023-07-23-analog-computing-the-once-and-future
  title: '🔮 E09: Analog Computing: The Once and Future King'
  date: '2023-07-23'
  kind: substack
- slug: 2023-06-30-e06-the-model-t-moment-for-bits-llms
  title: '🔮 E06: Large Language Models and the Assembly Line'
  date: '2023-06-30'
  kind: substack
- slug: 2023-06-23-e05-the-future-of-edge-ai-brain-inspired
  title: '🔮 E05: Neuromorphic Computing & The Future of Edge AI'
  date: '2023-06-23'
  kind: substack
neighbors: []
---
## Physics / mechanism

Neuromorphic computing implements neural computation in hardware by co-locating memory and processing—eliminating the von Neumann bottleneck. Core primitive is the artificial neuron/synapse: spiking neural networks (SNNs) communicate via sparse binary events (spikes) rather than continuous activations, dramatically reducing switched capacitance. Key substrates: CMOS (Intel Loihi 2: 1M neurons, 120M synapses, 10× better energy/inference than GPU on sparse workloads), memristive crossbars (PCM, RRAM, OTS selectors), and emerging ferroelectric FETs. Synaptic density, spike encoding efficiency, and on-chip learning (STDP) are the differentiated parameters. Energy figures: 10–100 pJ/synaptic operation vs. ~1 nJ on GPU. Still pre-productisation: no dominant ISA, fragmented toolchains.

## Competitive landscape

Competing inference approaches: standard GPU/TPU inference (mature, high throughput, energy-hungry), analog in-memory computing (similar von Neumann escape, continuous weights, noise-limited precision), and photonic neural networks (ultralow latency, WDM parallelism, limited nonlinearity). SNNs compete directly with quantised transformers on edge inference benchmarks. The clearest competitive wedge is always-on sensory processing: radar, LiDAR, event cameras—domains where sparse, asynchronous data maps naturally to spike codes and where GPU idle power is prohibitive.

| Approach | Energy/op | Programmability | Maturity |
|---|---|---|---|
| Neuromorphic (SNN) | ~10–100 pJ | Low-medium | TRL 4–6 |
| Analog IMC | ~1–10 pJ | Low | TRL 4–5 |
| Digital GPU/TPU | ~1 nJ | High | Production |

## Where value accrues (vehicle-agnostic)
Neuromorphic's economic prize is the always-on sensing/inference tier inside devices that cannot afford a GPU's power budget — captured today mostly by the SoC platform owners and the foundries supplying low-leakage process + embedded NVM, not by standalone neuromorphic vendors (the category's base rate is poor; see **Low Power Edge Compute**). The credible substrate is a GF-shaped node: 22FDX / 12LP (low leakage, embedded NVM incl. eMRAM, FD-SOI body-bias) suits the always-on, low-VDD requirement.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- **Brain-inspired *algorithm* vs spiking-neuromorphic *hardware* — keep them distinct.** The 2026 mega-rounds in "brain-like AI" (Flourish, ~$500M at ~$2.5B, Bezos/Lux/GV; **2026 06 04 Bezos Flourish Brain Core Algorithm**) chase a *canonical cortical-column algorithm* re-run on conventional silicon, NOT spiking SNN hardware (Loihi/TrueNorth lineage). This page is the hardware substrate; the algorithm bet sits with **Extreme Low Power Compute** and **Biocomputing Substrate**. Watch whether the algorithm camp ever needs neuromorphic silicon to hit its 50 W target, or whether GPUs suffice once the algorithm is sparse enough.
