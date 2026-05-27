---
type: concept
slug: edge-ai
canonical_name: Edge AI
aliases:
- edge ai compute
kind: framework
parent_concepts:
- compute
- ai-edge
related_concepts: []
sources:
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2024-yole-advanced-packaging-2024]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- framework
mention_count: 15
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 5
recent_mentions:
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-yole-advanced-packaging-2024
  title: Yole Group — Advanced Packaging 2024 Market Analysis
  date: '2024-12-01'
  kind: web
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2023-07-23-analog-computing-the-once-and-future
  title: '🔮 E09: Analog Computing: The Once and Future King'
  date: '2023-07-23'
  kind: substack
- slug: 2023-06-23-e05-the-future-of-edge-ai-brain-inspired
  title: '🔮 E05: Neuromorphic Computing & The Future of Edge AI'
  date: '2023-06-23'
  kind: substack
neighbors: []
---
## Physics / mechanism

Inference of ML models at or near data sources—sensors, endpoints, microcontrollers—rather than routing to cloud. Works by quantizing trained models (INT8, INT4, binary) and mapping them onto hardware optimized for MAC operations: NPUs, DSPs, or purpose-built inference ASICs. Key parameters: TOPS/W (efficiency), latency (ms), SRAM footprint (often <1 MB), and BOM cost. State of the art sits around 10–50 TOPS/W for edge NPUs (Arm Ethos-U85, Syntiant NDP120, Hailo-8). Sparse and in-memory computing architectures are pushing efficiency toward 100+ TOPS/W at 7–12nm nodes. Deployment constrained by model compression fidelity loss and memory bandwidth walls.

## Competitive landscape

Cloud inference (AWS Inferentia, NVIDIA H100 clusters) competes on model capability and developer tooling but loses on latency, privacy, and connectivity independence. On-device competition splits by tier: MCU-class (Ambiq, Nordic + TinyML), mobile-class (Apple Neural Engine, Qualcomm Hexagon), and embedded vision (Hailo, Axelera, Kneron). Adjacent techniques include neuromorphic (Intel Loihi, BrainChip) and analog in-memory compute (Mythic, Weebit). Photonic inference is an emerging adjacency with orders-of-magnitude efficiency potential but TRL 3–4.

| Approach | Latency | Power | Maturity |
|---|---|---|---|
| Cloud inference | 50–500ms | kW-scale | Production |
| Edge NPU (digital) | 1–20ms | 0.5–5W | Production |
| Photonic inference | <1ms (projected) | mW-scale (projected) | Pre-commercial |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
