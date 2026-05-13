---
type: concept
slug: neuromorphic-computing
canonical_name: Neuromorphic Computing
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- logic-and-paradigms
related_concepts: []
companies_using:
- aibrains
- airhive-formerly-corticalio-related-neurosys
- applied-brain-research
- brainchip-holdings
- brainware-eth-spinout
- cerebo
- corticom
- grai-matter-labs
- ibm-research-northpole
- inivation
- innatera-nanosystems
- insightness-acquired-by-sony
- intel-loihi
- koniku
- memryx
- neuroblade
- neuromem-general-vision
- nuro-spinnaker2-tu-dresden-spinout
- prophesee
- rain-neuromorphics
- speck-synsense-product-eta-compute
- spiking-neural-networks-imec-spinout-axelera-ai
- synsense-aictx
- tianjic-tsinghua-university-spin-off
ideas_referencing: []
sources:
- '[[2025-09-23-the-compute-gradient]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2023-06-30-e06-the-model-t-moment-for-bits-llms]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 20
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 2
---

# Neuromorphic Computing

*Kind: technology · Attio deal count: 13*

## Physics / mechanism

Neuromorphic computing implements neural computation in hardware by co-locating memory and processing—eliminating the von Neumann bottleneck. Core primitive is the artificial neuron/synapse: spiking neural networks (SNNs) communicate via sparse binary events (spikes) rather than continuous activations, dramatically reducing switched capacitance. Key substrates: CMOS (Intel Loihi 2: 1M neurons, 120M synapses, 10× better energy/inference than GPU on sparse workloads), memristive crossbars (PCM, RRAM, OTS selectors), and emerging ferroelectric FETs. Synaptic density, spike encoding efficiency, and on-chip learning (STDP) are the differentiated parameters. Energy figures: 10–100 pJ/synaptic operation vs. ~1 nJ on GPU. Still pre-productisation: no dominant ISA, fragmented toolchains.

## Competitive landscape


Competing inference approaches: standard GPU/TPU inference (mature, high throughput, energy-hungry), analog in-memory computing (similar von Neumann escape, continuous weights, noise-limited precision), and photonic neural networks (ultralow latency, WDM parallelism, limited nonlinearity). SNNs compete directly with quantised transformers on edge inference benchmarks. The clearest competitive wedge is always-on sensory processing: radar, LiDAR, event cameras—domains where sparse, asynchronous data maps naturally to spike codes and where GPU idle power is prohibitive.

| Approach | Energy/op | Programmability | Maturity |
|---|---|---|---|
| Neuromorphic (SNN) | ~10–100 pJ | Low-medium | TRL 4–6 |
| Analog IMC | ~1–10 pJ | Low | TRL 4–5 |
| Digital GPU/TPU | ~1 nJ | High | Production |

## Cloudberry relevance
Cloudberry/GF-LP angle: GF's 22FDX and 12LP nodes are credible substrates for neuromorphic tapeouts—low leakage, embedded NVM options (eMRAM), and FD-SOI body-bias tuning align with the always-on, low-VDD requirements. Deal-flow targets: fabless startups needing a Tier-1 process partner without TSMC access (geopolitical + cost), and sensor-fusion edge-AI companies where the spike-domain advantage is measurable. Lunar Ventures' Berlin network surfaces European academic spinouts (Heidelberg, ETH) earlier than most. Watch for event-camera + neuromorphic chip combos as a bundled pitch.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
