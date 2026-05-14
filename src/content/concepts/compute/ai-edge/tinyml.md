---
type: concept
slug: tinyml
canonical_name: TinyML
aliases: []
kind: technology
parent_concepts:
- compute
- ai-edge
related_concepts: []
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
recent_mentions: []
neighbors: []
---
## Physics / mechanism

TinyML refers to machine-learning inference executed on microcontrollers and ultra-low-power edge processors, typically operating under 1 mW and within SRAM budgets of 256 KB or less. Models are compressed via quantization (INT8/INT4, sometimes binary), pruning, and knowledge distillation before deployment. Key frameworks: TensorFlow Lite Micro, ONNX Runtime Mobile, Edge Impulse. State of the art achieves keyword spotting at ~100 µW (Arm Cortex-M4 class), image classification on MCUs at <1 ms latency. The binding constraint is memory bandwidth and SRAM, not compute FLOPS — distinguishing TinyML from standard edge AI. Hardware: Arm Cortex-M, RISC-V cores, dedicated NPU accelerators (Ambiq, Syntiant, GreenWaves).

## Competitive landscape

Competing approaches split along the power/capability curve. Larger edge AI chips (NXP i.MX RT, STM32 with NPU, Renesas RA) blur the boundary upward. Neuromorphic architectures (Intel Loihi, SpiNNaker) target similar power envelopes via event-driven sparsity rather than weight compression. Analog in-memory compute (Mythic, Atmosic) attacks the memory-bandwidth bottleneck directly at the array level. FPGA-based inference (Lattice sensAI) offers reconfigurability at higher cost. The core tension: quantization degrades accuracy; neuromorphic and analog approaches preserve sparsity but complicate training pipelines and process integration.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
