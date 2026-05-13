---
type: concept
slug: ai-machine-learning
canonical_name: AI & Machine Learning
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- ai-infrastructure
related_concepts: []
companies_using:
- ai21-labs
- aleph-alpha
- answerai
- anthropic
- baidu
- cerebras-systems
- cohere
- cradle
- google-deepmind
- helsing
- hugging-face
- igenius
- lightmatter
- lighton
- luminous-computing
- mistral-ai
- modular
- moonvalley
- normal-computing
- nvidia
- openai
- polyai
- poolside
- qdrant
- quantpi
- rebellions
- sakana-ai
- sambanova-systems
- scale-ai
- silo-ai
- synthesis-ai
- twelve-labs
- wayve
- weights-biases
- xai
ideas_referencing: []
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
---

# AI & Machine Learning

*Kind: technology · Attio deal count: 26*

## Physics / mechanism

Transformer-based large language models dominate current AI: attention mechanisms scale as O(n²) in sequence length, mitigated by sparse attention, flash attention, and MoE routing. Training runs now exceed 10²³–10²⁴ FLOPs; inference is the cost-dominant phase at scale. Key parameters: model size (1B–1T+ parameters), context window (128k–1M tokens), quantisation precision (FP8/INT4 for edge), and memory bandwidth (HBM3e at ~1.2 TB/s). SotA: GPT-4o, Gemini 1.5, Llama 3, Mistral. The bottleneck has shifted from algorithms to silicon—compute density, memory bandwidth, and interconnect (NVLink, UCIe, CXL) now determine competitive position.

## Competitive landscape


The primary axis of competition is silicon architecture: GPU (NVIDIA H100/B200) vs. purpose-built AI accelerators (Groq, Cerebras, Tenstorrent, SambaNova) vs. in-memory compute and neuromorphic (Intel Loihi, IBM NorthPole). Photonic inference accelerators (Lightmatter, Luminous) attack the bandwidth wall via optical interconnect. At the algorithm layer, SSMs (Mamba) challenge transformers on long-context efficiency. Edge AI competes on power envelope: sub-10W inference on NPUs (Apple ANE, Qualcomm Hexagon).

| Axis | GPU (NVIDIA) | AI ASIC | Photonic |
|---|---|---|---|
| Throughput | High | Very high (narrow workload) | Bandwidth-limited currently |
| Power efficiency | Moderate | High | Potentially transformative |
| Flexibility | High | Low | Low |

## Cloudberry relevance
Cloudberry's angle is the silicon and photonics stack beneath the model layer—not foundation models themselves. GlobalFoundries LP context: GF serves edge AI, automotive, and defence silicon; portfolio deal-flow targets inference hardware, photonic interconnect, and advanced packaging enabling chiplet-based AI accelerators. Lunar Ventures surfaces early-stage European AI-hardware plays. The investment thesis: software margins accrue to hyperscalers; durable value in AI sits in specialised compute, memory architectures, and the fab capacity enabling them.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
