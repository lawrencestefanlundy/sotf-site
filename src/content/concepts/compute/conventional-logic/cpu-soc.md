---
type: concept
slug: cpu-soc
canonical_name: CPU & SoC
aliases: []
kind: technology
parent_concepts:
- compute
- conventional-logic
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 16
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-05-12-hello-universe-nasas-next-gen-space-processor-undergoes-test
  title: 'Hello Universe: NASA’s Next-Gen Space Processor Undergoes Testing'
  date: '2026-05-12'
  kind: web
- slug: 2025-08-20-uncle-sam-eyes-slice-of-intel-in-return-for-chips-act-cash--
  title: Uncle Sam eyes slice of Intel in return for CHIPS Act cash - The Register
  date: '2025-08-20'
  kind: web
- slug: 2024-03-05-amd-reportedly-hits-us-regulatory-roadblock-for-china-tailor
  title: AMD reportedly hits U.S. regulatory roadblock for China-tailored chip - CNBC
  date: '2024-03-05'
  kind: web
- slug: 2019-02-03-season-4-episode-2-arm-softbank
  title: Season 4, Episode 2: ARM & SoftBank
  date: '2019-02-03'
  kind: web
- slug: 2017-11-20-episode-48-qualcomm---broadcom
  title: Episode 48: Qualcomm - Broadcom
  date: '2017-11-20'
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
