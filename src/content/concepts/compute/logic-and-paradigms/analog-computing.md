---
type: concept
slug: analog-computing
canonical_name: Analog Computing
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
- aizip
- anaflash
- analog-inference
- aspinity
- brainchip-holdings
- efficient-computer-fabric
- encharge-ai
- eta-compute
- grai-matter-labs
- imec
- intelic-formerly-innatera-nanosystems
- lightmatter
- luminous-computing
- movella-formerly-mcube
- mythic
- perceive-formerly-xnorai-spinout-lineage
- polyn-technology
- rain-neuromorphics
- rapid-silicon-formerly-rapid-analog
- silicon-storage-technology-microchip-technology-superflash
- spiking-neural-network-snn-startup-synsense
- syntiant
- wannaknow-axelera-ai
- weebit-nano
ideas_referencing: []
sources:
- '[[2023-09-18-e15-in-conversation-with-wisear-on]]'
- '[[2023-09-28-e16-in-conversation-with-shiv-malik]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2023-06-30-e06-the-model-t-moment-for-bits-llms]]'
- '[[2023-09-24-e16-in-conversation-with-john-waite]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 11
descendants:
- memcapacitor
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Analog Computing

*Kind: technology · Attio deal count: 2*

## Physics / mechanism

Analog computing encodes information as continuous physical quantities—voltage, current, charge, optical intensity—rather than discrete bits. Computation occurs via physical law: matrix-vector multiplication maps directly onto Kirchhoff's current law in resistive crossbar arrays, or onto interference in photonic meshes. Key parameters: energy-per-MAC (multiply-accumulate), precision (typically 4–8 effective bits vs. digital's 32), throughput density, and drift/noise floors. State of the art: memristor crossbars demonstrate sub-fJ/MAC at 8-bit equivalent precision; analog photonic accelerators (MIT, Lightmatter) hit >TOPS/W at inference workloads. Core limitation is weight-programming accuracy and device-to-device variability, both active research targets.

## Competitive landscape


Digital ASIC accelerators (Tenstorrent, Groq, Cerebras) dominate on programmability and precision; neuromorphic (Intel Loihi, IBM NorthPole) overlaps on event-driven, low-power inference. Photonic digital interconnect is adjacent but distinct. In-memory computing (SRAM/DRAM analog) competes at the edge.

| Approach | Energy/MAC | Precision | Programmability |
|---|---|---|---|
| Analog crossbar | <1 fJ | 4–8 bit | Low |
| Digital ASIC | ~1–10 pJ | 8–32 bit | High |
| Analog photonic | <0.1 pJ | ~6 bit | Medium |

## Cloudberry relevance
Cloudberry's GlobalFoundries-LP fund creates direct relevance: GF's 22FDX and 12LP nodes are natural candidates for mixed-signal/analog IP tape-outs, and several analog AI startups need a foundry outside TSMC. Deal-flow angles include analog inference IP licensors, edge-sensor compute integrators, and photonic-electronic co-design startups. Lunar Ventures' early-stage lens catches pre-silicon teams needing semiconductor-literate capital. Material-level adjacency to phase-change and ferroelectric memory (Radiant) makes analog NVM weight storage a direct pipeline interest.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
