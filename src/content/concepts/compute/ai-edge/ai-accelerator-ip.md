---
type: concept
slug: ai-accelerator-ip
canonical_name: AI Accelerator IP (Cadence Tensilica, Arm Ethos)
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
recent_mentions:
- slug: 2026-06-17-femtoai-company-profile
  title: femtoAI (formerly Femtosense) — company profile, funding, leadership
  date: '2026-06-17'
  kind: web
- slug: 2026-06-17-femtoai-spu-ces2026
  title: femtoAI to Highlight its Sparse Processing Unit Edge AI Accelerator at CES 2026
  date: '2026-06-17'
  kind: web
neighbors: []
---
## Physics / mechanism

Licensable processor IP cores optimised for inference workloads. Cadence Tensilica HiFi/Vision DSPs use a VLIW + SIMD architecture with configurable instruction-set extensions; customers add custom functional units at RTL generation time, meaning MAC-array width, SRAM banking, and dataflow (weight-stationary vs output-stationary) are design-time parameters rather than fixed silicon. Arm Ethos-U55/U65/U85 targets Cortex-M-class systems; Ethos-U85 delivers up to 4 TOPS at sub-500 mW in 5 nm. Key figures of merit: TOPS/W, TOPS/mm², and supported operator coverage for ONNX/TFLite graphs. Both ship as synthesisable RTL licensed per-design or royalty-per-unit, targeting edge MCU and embedded SoC integrations rather than datacenter.

## Competitive landscape

Competing IP blocks: Synopsys ARC NPX (tightly coupled NPU extensions on ARC scalar cores), CEVA NeuPro-S/M (streaming MAC arrays, strong in audio/vision fusion), Imagination IMG CXT (GPU-derived, broader operator coverage, higher area cost). Custom internal NPU teams at Apple, Samsung, and Qualcomm have made merchant IP less relevant at high volume. Chiplet and UCIe disaggregation is beginning to unbundle the compute tile from the IP licensing model entirely.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
