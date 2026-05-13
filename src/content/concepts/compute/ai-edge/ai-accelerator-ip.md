---
type: concept
slug: ai-accelerator-ip
canonical_name: AI Accelerator IP (Cadence Tensilica, Arm Ethos)
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
- andes-technology
- arm-holdings
- axelera-ai
- blaize
- bluespec
- cadence-design-systems
- ceva
- deepx
- efinix
- esperanto-technologies
- eta-compute
- expedera
- flex-logix-technologies
- greenwaves-technologies
- hailo-technologies
- imagination-technologies
- innatera-nanosystems
- kneron
- liqid-kinara-formerly
- neuroblade
- nuclei-system-technology
- perceive-formerly-xnorai-spin-out-amazon
- perceive
- quadric
- recogni
- simaai
- synopsys
- syntiant
- tenstorrent
- untether-ai
- verisilicon
- vorago-technologies
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

# AI Accelerator IP (Cadence Tensilica, Arm Ethos)

*Kind: technology*

## Physics / mechanism

Licensable processor IP cores optimised for inference workloads. Cadence Tensilica HiFi/Vision DSPs use a VLIW + SIMD architecture with configurable instruction-set extensions; customers add custom functional units at RTL generation time, meaning MAC-array width, SRAM banking, and dataflow (weight-stationary vs output-stationary) are design-time parameters rather than fixed silicon. Arm Ethos-U55/U65/U85 targets Cortex-M-class systems; Ethos-U85 delivers up to 4 TOPS at sub-500 mW in 5 nm. Key figures of merit: TOPS/W, TOPS/mm², and supported operator coverage for ONNX/TFLite graphs. Both ship as synthesisable RTL licensed per-design or royalty-per-unit, targeting edge MCU and embedded SoC integrations rather than datacenter.

## Competitive landscape

Competing IP blocks: Synopsys ARC NPX (tightly coupled NPU extensions on ARC scalar cores), CEVA NeuPro-S/M (streaming MAC arrays, strong in audio/vision fusion), Imagination IMG CXT (GPU-derived, broader operator coverage, higher area cost). Custom internal NPU teams at Apple, Samsung, and Qualcomm have made merchant IP less relevant at high volume. Chiplet and UCIe disaggregation is beginning to unbundle the compute tile from the IP licensing model entirely.

## Cloudberry relevance

| IP | Arch style | Peak TOPS (edge) | Licensing model |
|---|---|---|---|
| Arm Ethos-U85 | Fixed-function NPU | 4 TOPS | Royalty |
| Cadence Tensilica | Configurable VLIW | ~2 TOPS (config-dep) | Per-design + royalty |
| CEVA NeuPro-M | Streaming MAC | ~8 TOPS | Per-design + royalty |


Cloudberry portfolio companies building edge-inference silicon—sensors, photonic compute, advanced-materials-based memory—must choose or licence an NPU core early; it anchors PPA targets and tapeout risk. GlobalFoundries' 22FDX and 12LP+ nodes are primary targets for Ethos/Tensilica integrations, making IP-node co-optimisation a genuine differentiator. Deal-flow angle: fabless startups licensing these cores are natural introductions; IP stack choice signals how defensible the architecture actually is versus wrapping a commodity block.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
