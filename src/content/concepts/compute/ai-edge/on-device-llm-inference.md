---
type: concept
slug: on-device-llm-inference
canonical_name: On-Device LLM Inference
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
- apple
- arm
- axelera-ai
- blaize
- deepmind-google-gemini-nano-team
- enfabrica
- espressif-systems
- eta-compute
- google-deepmind-android
- hailo
- janai
- jina-ai
- kneron
- lepton-ai
- llamacpp-ggml-georgi-gerganov
- llmc-georgi-gerganov-ggml-llamacpp
- lorimer-analytics-lore-ai
- mediatek
- memryx
- microsoft-phi-team
- microsoft
- mistral-ai
- mlc-ai-machine-learning-compilation
- mx51-edgecortix
- neural-magic-acquired-by-red-hat
- neural-magic-now-part-of-red-hat
- octoml-now-octo-ai
- octoml-now-octo
- picovoice
- qualcomm-backed-nxp-semiconductors
- qualcomm
- rebellions
- rockchip
- samsung-electronics
- syntiant
- tenyx-acquired-by-salesforce
- useful-sensors
- volara
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

# On-Device LLM Inference

*Kind: technology*

## Physics / mechanism

On-device LLM inference runs transformer-based models locally on edge silicon—smartphones, PCs, embedded MCUs—without cloud round-trips. The bottleneck is memory bandwidth: attention and feed-forward layers are bandwidth-bound, not compute-bound, so DRAM bandwidth (measured in GB/s) and SRAM capacity set practical throughput ceilings. Quantization (INT4/INT8, sometimes FP8) shrinks weight footprint; structured pruning and speculative decoding reduce token latency. Current SoA: Apple M4 Neural Engine does ~38 TOPS, enabling 7–13B parameter models at 20–40 tok/s on-device. Qualcomm Snapdragon X Elite hits ~45 TOPS NPU. Sub-1B models (Phi-3-mini, Gemma 2B) run on embedded Cortex-M class targets with aggressive quantization.

## Competitive landscape

The primary axes of competition are NPU horsepower (Apple, Qualcomm, MediaTek), dedicated inference accelerator chips (Hailo, Kneron, Mythic, Etched), and in-memory computing architectures (Analog Devices' memristor work, SRAM-CIM from TSMC research). FPGA-based inference (Xilinx/Versal) occupies a niche for latency-sensitive industrial edge.

## Cloudberry relevance

| Approach | Latency | Flexibility | Power |
|---|---|---|---|
| SoC NPU | Low–Med | High | ~5–15 W |
| Discrete accelerator | Low | Low–Med | ~2–10 W |
| In-memory compute | Very low | Low | <1 W (target) |


GlobalFoundries' specialty nodes (22FDX, 12LP+) are directly in the stack: FD-SOI suits ultra-low-power inference at the extreme edge; GF's embedded NVM (eMRAM, eFlash) enables weight storage without off-chip DRAM. Deal-flow angle: fabless startups designing inference ASICs who need a non-TSMC, US-based foundry partner. Lunar Ventures' European deep-tech network surfaces compiler/runtime toolchain plays and neuromorphic architecture bets that need semi-process differentiation.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
