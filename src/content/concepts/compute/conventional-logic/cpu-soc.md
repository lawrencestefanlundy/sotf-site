---
type: concept
slug: cpu-soc
context_concept: true
canonical_name: CPU & SoC
aliases: []
kind: technology
parent_concepts:
- compute
- conventional-logic
related_concepts: []
sources: []
frontier: []
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 16
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2022-06-15-owner-of-uk-chip-designer-arm-may-float-some-of-firms-shares
  title: Owner of UK chip designer Arm may float some of firm’s shares in London - The Guardian
  date: '2022-06-15'
  kind: web
- slug: 2019-05-22-uk-chip-designer-arm-suspends-business-with-huawei-to-comply
  title: UK chip designer ARM suspends business with Huawei to comply with new U.S. rules - ET Telecom
  date: '2019-05-22'
  kind: web
neighbors: []
---
## Physics / mechanism

A CPU executes sequential instruction streams via fetch-decode-execute pipelines; an SoC integrates CPU cores alongside GPU, NPU, memory controllers, I/O, and analog blocks on a single die. Key parameters: clock frequency (3–5 GHz high-performance), IPC (instructions per cycle), core count, cache hierarchy (L1/L2/L3 latency and capacity), TDP, and process node. Leading-edge logic is at TSMC N3/N2, Samsung SF3, Intel 18A. Apple M4 (~3 nm class, ~120 TOPS NPU) and Qualcomm Snapdragon X Elite define current SoC integration density. Power-performance-area (PPA) trade-offs dominate design decisions at every node shrink.

## Competitive landscape

The primary architectural competition is GPU (massively parallel, memory-bandwidth-bound workloads) and purpose-built accelerators (TPU, NPU, FPGA). At the chiplet/integration level, the contest is monolithic vs. disaggregated (UCIe, HBM stacking). RISC-V is eroding Arm's ISA lock-in in edge/embedded.

| Approach | Strength | Weakness |
|---|---|---|
| x86 CPU | Legacy software compatibility | Power efficiency ceiling |
| Arm SoC | PPA efficiency, mobile ecosystem | Licensing dependency |
| RISC-V | Open ISA, customisable | Toolchain/ecosystem immaturity |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
