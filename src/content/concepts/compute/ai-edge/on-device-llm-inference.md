---
type: concept
slug: on-device-llm-inference
canonical_name: On-Device LLM Inference
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
---
## Physics / mechanism

On-device LLM inference runs transformer-based models locally on edge silicon—smartphones, PCs, embedded MCUs—without cloud round-trips. The bottleneck is memory bandwidth: attention and feed-forward layers are bandwidth-bound, not compute-bound, so DRAM bandwidth (measured in GB/s) and SRAM capacity set practical throughput ceilings. Quantization (INT4/INT8, sometimes FP8) shrinks weight footprint; structured pruning and speculative decoding reduce token latency. Current SoA: Apple M4 Neural Engine does ~38 TOPS, enabling 7–13B parameter models at 20–40 tok/s on-device. Qualcomm Snapdragon X Elite hits ~45 TOPS NPU. Sub-1B models (Phi-3-mini, Gemma 2B) run on embedded Cortex-M class targets with aggressive quantization.

## Competitive landscape

The primary axes of competition are NPU horsepower (Apple, Qualcomm, MediaTek), dedicated inference accelerator chips (Hailo, Kneron, Mythic, Etched), and in-memory computing architectures (Analog Devices' memristor work, SRAM-CIM from TSMC research). FPGA-based inference (Xilinx/Versal) occupies a niche for latency-sensitive industrial edge.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
