---
type: concept
slug: edge-ai
canonical_name: Edge AI
aliases:
- edge ai compute
kind: framework
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- ai-edge
related_concepts: []
companies_using:
- arm
- au-zone-technologies
- axelera-ai
- brainchip-holdings
- canaan-inc
- cogneo-formerly-imagimob
- constella-intelligence-perceive-apple-acq-track
- deeplite
- edge-impulse
- edgeless-systems
- eta-compute
- expedera
- fastree3d
- greenwaves-technologies
- hailo-technologies
- imagimob
- intel
- iotatech
- kinara-formerly-deepvision
- kinara-formerly-flex-logix
- kneron
- latent-ai
- lorenz-technology
- mediatek
- neurala
- nvidia
- nxp-semiconductors
- prophesee
- qualcomm
- rockchip
- stmicroelectronics
- syntiant
- useful-sensors
- xailient
ideas_referencing: []
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
mention_count: 12
descendants:
- ai-accelerator-ip
- edge-ai
- edge-ai-infra
- iot-connected-devices
- iot-embedded
- on-device-llm-inference
- tinyml
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 2
---

# Edge AI

*Kind: framework · Attio deal count: 0*

## Physics / mechanism

Inference of ML models at or near data sources—sensors, endpoints, microcontrollers—rather than routing to cloud. Works by quantizing trained models (INT8, INT4, binary) and mapping them onto hardware optimized for MAC operations: NPUs, DSPs, or purpose-built inference ASICs. Key parameters: TOPS/W (efficiency), latency (ms), SRAM footprint (often <1 MB), and BOM cost. State of the art sits around 10–50 TOPS/W for edge NPUs (Arm Ethos-U85, Syntiant NDP120, Hailo-8). Sparse and in-memory computing architectures are pushing efficiency toward 100+ TOPS/W at 7–12nm nodes. Deployment constrained by model compression fidelity loss and memory bandwidth walls.

## Competitive landscape


Cloud inference (AWS Inferentia, NVIDIA H100 clusters) competes on model capability and developer tooling but loses on latency, privacy, and connectivity independence. On-device competition splits by tier: MCU-class (Ambiq, Nordic + TinyML), mobile-class (Apple Neural Engine, Qualcomm Hexagon), and embedded vision (Hailo, Axelera, Kneron). Adjacent techniques include neuromorphic (Intel Loihi, BrainChip) and analog in-memory compute (Mythic, Weebit). Photonic inference is an emerging adjacency with orders-of-magnitude efficiency potential but TRL 3–4.

| Approach | Latency | Power | Maturity |
|---|---|---|---|
| Cloud inference | 50–500ms | kW-scale | Production |
| Edge NPU (digital) | 1–20ms | 0.5–5W | Production |
| Photonic inference | <1ms (projected) | mW-scale (projected) | Pre-commercial |

## Cloudberry relevance
Direct relevance: GlobalFoundries' 22FDX and 12LP+ nodes are competitive process targets for edge inference ASICs—low leakage, embedded NVM, analog-friendly. Deal-flow angle: fabless startups designing inference chips on GF processes, or IP vendors (activation functions, sparsity engines) licensing to fabless players. Photonic inference startups are pipeline-relevant given Cloudberry's photonics thesis. Lunar Ventures' software-layer bets (TinyML toolchains, model compression) are complementary entry points upstream of the silicon.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
