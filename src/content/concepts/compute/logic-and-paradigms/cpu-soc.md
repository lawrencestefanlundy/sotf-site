---
type: concept
slug: cpu-soc
canonical_name: CPU & SoC
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- logic-and-paradigms
related_concepts: []
companies_using:
- amd
- ampere-computing
- andes-technology
- apple
- arm-holdings
- axelera-ai
- codasip
- esperanto-technologies
- hailo
- imagination-technologies
- intel
- kalray
- loongson-technology
- mediatek
- nuclei-system-technology
- qualcomm
- risc-v-international
- samsung-semiconductor
- semidynamics
- sifive
- syntiant
- tenstorrent
- tsmc
- valtrix-systems
- ventana-micro-systems
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 16
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# CPU & SoC

*Kind: technology · Attio deal count: 25*

## Physics / mechanism

A CPU executes sequential instruction streams via fetch-decode-execute pipelines; an SoC integrates CPU cores alongside GPU, NPU, memory controllers, I/O, and analog blocks on a single die. Key parameters: clock frequency (3–5 GHz high-performance), IPC (instructions per cycle), core count, cache hierarchy (L1/L2/L3 latency and capacity), TDP, and process node. Leading-edge logic is at TSMC N3/N2, Samsung SF3, Intel 18A. Apple M4 (~3 nm class, ~120 TOPS NPU) and Qualcomm Snapdragon X Elite define current SoC integration density. Power-performance-area (PPA) trade-offs dominate design decisions at every node shrink.

## Competitive landscape


The primary architectural competition is GPU (massively parallel, memory-bandwidth-bound workloads) and purpose-built accelerators (TPU, NPU, FPGA). At the chiplet/integration level, the contest is monolithic vs. disaggregated (UCIe, HBM stacking). RISC-V is eroding Arm's ISA lock-in in edge/embedded.

| Approach | Strength | Weakness |
|---|---|---|
| x86 CPU | Legacy software compatibility | Power efficiency ceiling |
| Arm SoC | PPA efficiency, mobile ecosystem | Licensing dependency |
| RISC-V | Open ISA, customisable | Toolchain/ecosystem immaturity |

## Cloudberry relevance
GlobalFoundries serves the trailing-edge and specialty node market—RF, embedded NVM, automotive-grade logic—not leading-edge CPU. Cloudberry relevance is upstream: EDA tools, advanced packaging (chiplets, 2.5D/3D), specialty analog IP blocks, and photonic interconnect for on-package bandwidth. Deal-flow targets include companies building chiplet infrastructure, silicon photonics die-to-die links reducing CPU–memory bottlenecks, and GF-compatible mixed-signal IP vendors enabling SoC differentiation outside the leading-edge arms race.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
