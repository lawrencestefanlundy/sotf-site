---
type: concept
slug: spiking-neural-networks
canonical_name: Spiking Neural Networks
aliases:
- SNN
- spiking-neural-network
- spiking neural net
kind: technology
parent_concepts:
- neuromorphic-computing
related_concepts:
- neuromorphic-computing
- edge-ai
sources: []
last_updated: 2026-06-17
tags:
- concept
- technology
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: neuromorphic-computing
  name: Neuromorphic Computing
  path: /sotf-site/compute/non-conventional/neuromorphic-computing/
  macro: compute
- slug: edge-ai
  name: Edge AI
  path: /sotf-site/compute/ai-edge/edge-ai/
  macro: compute
---
*Child of [Neuromorphic Computing](/sotf-site/compute/non-conventional/neuromorphic-computing/).*

## Physics / mechanism

Spiking neural networks (SNNs) encode and transmit information as discrete, asynchronous events (spikes) over time, rather than the continuous-valued activations of conventional ANNs. A neuron integrates incoming weighted spikes and fires only when its membrane potential crosses a threshold, so computation is **event-driven and sparse**: no spike, no switched capacitance, no energy spent. This is the algorithmic layer that most [Neuromorphic Computing](/sotf-site/compute/non-conventional/neuromorphic-computing/) hardware is built to run. Differentiated parameters: spike-encoding scheme (rate vs temporal), on-chip learning rule (STDP / surrogate-gradient backprop), synaptic density, and energy per synaptic operation (~10–100 pJ vs ~1 nJ on GPU).

The decade-long blocker was **programmability**, not physics: training SNNs was hard until surrogate-gradient methods + maturing toolchains made them trainable like standard DNNs (see **Low Power Edge Compute** belief ledger). That reframed SNNs from a standalone-chip thesis toward an offload/feature-block inside someone else's SoC.

## Where it fits

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Does surrogate-gradient training close the accuracy gap with quantised ANNs at iso-power?
- Does any SNN chip reach a volume socket beyond research and niche sensing? (see **Low Power Edge Compute** prediction #3)

*Created 2026-06-17 — filled a concept-page gap surfaced by the fabrication audit (companies tagged `spiking-neural-networks` had no page to resolve to).*
