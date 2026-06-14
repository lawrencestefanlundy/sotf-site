---
type: concept
slug: ai-machine-learning
canonical_name: AI & Machine Learning
aliases: []
kind: technology
parent_concepts:
- life-frontier
- ai-infrastructure
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 26
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-05-19-imec-ceo-calls-for-stronger-ai-design-push-in-eus-chips-act-
  title: Imec CEO calls for stronger AI design push in EU's Chips Act - TradingView
  date: '2026-05-19'
  kind: web
- slug: 2026-05-05-extreme-unveils-its-full-stack-ai-networking-vision-and-wi-f
  title: Extreme unveils its full-stack AI networking vision and Wi-Fi 7 lineup - Fierce Network
  date: '2026-05-05'
  kind: web
- slug: 2026-03-10-synaptics-redefines-edge-iot-with-first-ai-native-wi-fi-7-co
  title: Synaptics Redefines Edge IoT with ‘First AI-Native Wi-Fi 7 Connectivity Solution for IoT’ - All About Circuits
  date: '2026-03-10'
  kind: web
neighbors: []
---
## Physics / mechanism

Transformer-based large language models dominate current AI: attention mechanisms scale as O(n²) in sequence length, mitigated by sparse attention, flash attention, and MoE routing. Training runs now exceed 10²³–10²⁴ FLOPs; inference is the cost-dominant phase at scale. Key parameters: model size (1B–1T+ parameters), context window (128k–1M tokens), quantisation precision (FP8/INT4 for edge), and memory bandwidth (HBM3e at ~1.2 TB/s). SotA: GPT-4o, Gemini 1.5, Llama 3, Mistral. The bottleneck has shifted from algorithms to silicon—compute density, memory bandwidth, and interconnect (NVLink, UCIe, CXL) now determine competitive position.

## Competitive landscape

The primary axis of competition is silicon architecture: GPU (NVIDIA H100/B200) vs. purpose-built AI accelerators (Groq, Cerebras, Tenstorrent, SambaNova) vs. in-memory compute and neuromorphic (Intel Loihi, IBM NorthPole). Photonic inference accelerators (Lightmatter, Luminous) attack the bandwidth wall via optical interconnect. At the algorithm layer, SSMs (Mamba) challenge transformers on long-context efficiency. Edge AI competes on power envelope: sub-10W inference on NPUs (Apple ANE, Qualcomm Hexagon).

| Axis | GPU (NVIDIA) | AI ASIC | Photonic |
|---|---|---|---|
| Throughput | High | Very high (narrow workload) | Bandwidth-limited currently |
| Power efficiency | Moderate | High | Potentially transformative |
| Flexibility | High | Low | Low |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
