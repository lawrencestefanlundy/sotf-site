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
- '[[2026-06-17-femtoai-company-profile]]'
- '[[2026-06-18-sensifai-hybrids-deck]]'
- '[[2024-02-26-micron-hbm3e-volume-production]]'
- '[[2024-yole-advanced-packaging-2024]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-06-17-femtoai-spu-ces2026]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- framework
mention_count: 54
descendants:
- hearing-aid-silicon-beachhead
- nvidia-jetson
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 15
recent_mentions:
- slug: 2026-07-01-hearing-aid-market-structure-edge-ai-beachhead
  title: Hearing-aid market structure as an edge-AI silicon beachhead (size, growth, concentration, commoditisation)
  date: '2026-07-01'
  kind: web
- slug: 2026-06-18-sensifai-hybrids-deck
  title: SensifAI — Funding Round deck (sensifai.vercel.app/hybrids)
  date: '2026-06-18'
  kind: web
- slug: 2026-06-17-femtoai-company-profile
  title: femtoAI (formerly Femtosense) — company profile, funding, leadership
  date: '2026-06-17'
  kind: web
- slug: 2026-06-17-femtoai-spu-ces2026
  title: femtoAI to Highlight its Sparse Processing Unit Edge AI Accelerator at CES 2026
  date: '2026-06-17'
  kind: web
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
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

## Where value accrues (vehicle-agnostic)
The largest, most durable value in edge AI sits with the platform owners who bundle the NPU into an SoC they already ship (Qualcomm, Apple, MediaTek, Arm via IP, NXP/ST/TI in industrial+auto) and the foundries that supply the low-power process + embedded NVM. Standalone edge-inference silicon is a graveyard (see **Low Power Edge Compute**): the honestly-capturable wedge is the sub-watt, no-HBM, memory-device niche merchant NPUs cannot serve, sold as a component.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
