---
type: concept
slug: tinyml
canonical_name: TinyML
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- ai-edge
related_concepts: []
companies_using:
- alif-semiconductor
- ambiq-micro
- andes-technology
- arm-holdings
- arm
- brainchip-holdings
- cartesiam
- edge-impulse
- espressif-systems
- eta-compute
- greenwaves-technologies
- idun-technologies
- imagimob
- infineon-technologies
- latent-ai
- mymo-wireless
- neutonai
- nordic-semiconductor
- octoml
- perceive-formerly-xnorai-acquired-then-re-spun
- perceive
- prophesee
- qeexo
- renesas-electronics
- seoul-robotics
- silabs-silicon-laboratories
- simaai
- stmicroelectronics
- syntiant
- tinyml-foundation
- useful-sensors
- xmos
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# TinyML

*Kind: technology*

## Physics / mechanism

TinyML refers to machine-learning inference executed on microcontrollers and ultra-low-power edge processors, typically operating under 1 mW and within SRAM budgets of 256 KB or less. Models are compressed via quantization (INT8/INT4, sometimes binary), pruning, and knowledge distillation before deployment. Key frameworks: TensorFlow Lite Micro, ONNX Runtime Mobile, Edge Impulse. State of the art achieves keyword spotting at ~100 µW (Arm Cortex-M4 class), image classification on MCUs at <1 ms latency. The binding constraint is memory bandwidth and SRAM, not compute FLOPS — distinguishing TinyML from standard edge AI. Hardware: Arm Cortex-M, RISC-V cores, dedicated NPU accelerators (Ambiq, Syntiant, GreenWaves).

## Competitive landscape

Competing approaches split along the power/capability curve. Larger edge AI chips (NXP i.MX RT, STM32 with NPU, Renesas RA) blur the boundary upward. Neuromorphic architectures (Intel Loihi, SpiNNaker) target similar power envelopes via event-driven sparsity rather than weight compression. Analog in-memory compute (Mythic, Atmosic) attacks the memory-bandwidth bottleneck directly at the array level. FPGA-based inference (Lattice sensAI) offers reconfigurability at higher cost. The core tension: quantization degrades accuracy; neuromorphic and analog approaches preserve sparsity but complicate training pipelines and process integration.

## Cloudberry relevance

| Approach | Power envelope | Training compatibility |
|---|---|---|
| TinyML (MCU + quantization) | <1 mW | Standard (post-training quant) |
| Neuromorphic | <1 mW | Specialist (SNN conversion) |
| Analog in-memory compute | 1–10 mW | Moderate (aware training needed) |


Cloudberry relevance sits at the semiconductor and IP layer: proprietary NPU silicon, memory compilers optimized for sub-threshold SRAM, and process nodes (GlobalFoundries 22FDX is a direct fit — low-leakage FD-SOI for IoT). Deal-flow angles include fabless MCU+NPU startups targeting industrial sensing, photonic-sensor front-ends requiring on-chip inference (LIDAR, spectrometry), and EDA/IP tooling for model-to-silicon co-optimization. Lunar Ventures' enterprise software lens intersects where TinyML middleware and MLOps for constrained devices become recurring-revenue software businesses layered above the silicon stack.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
