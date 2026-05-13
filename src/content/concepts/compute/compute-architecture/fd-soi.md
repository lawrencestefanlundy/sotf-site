---
type: concept
slug: fd-soi
canonical_name: FD-SOI
aliases:
- fdsoi
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- compute-architecture
related_concepts: []
companies_using:
- antaios
- bosch-semiconductor
- cea-leti
- dolphin-design
- ethertronics-avx-antenna-products
- globalfoundries
- greenwaves-technologies
- innatera-nanosystems
- liqid-radiosense-novelda-heritage
- movella-mcube
- nordic-semiconductor
- nxp-semiconductors
- qualcomm
- renesas-electronics
- samsung-foundry
- semron
- silex-microsystems-kyocera
- sipearl
- soitec
- stmicroelectronics
- swave-semiconductors
- tiempo-secure
- uhnder
ideas_referencing: []
sources:
- '[[2024-eu-chips-act-final-text]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 3
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
---

# FD-SOI

*Kind: technology · Attio deal count: 0*

## Physics / mechanism

Fully Depleted Silicon-on-Insulator is a planar CMOS variant where a thin Si device layer (~5–7 nm) sits atop a buried oxide (BOX, ~25 nm), fully depleting the channel without doping. Electrostatic control comes from gate geometry and optional back-bias voltage applied through the substrate, not from impurity concentration. This eliminates random dopant fluctuation, the dominant variability source below 28 nm. Key metrics: 28FD-SOI from STMicroelectronics/GlobalFoundries delivers ~30% power reduction vs. bulk 28 nm at iso-performance, back-bias tunability of ±300 mV shifts Vt dynamically, and the process supports RF/mmWave up to ~300 GHz fT. 22FDX (GF) extends this to 22 nm with 12 nm BOX.

## Competitive landscape

| Approach | Node floor | Back-bias | RF suitability | Key risk |
|---|---|---|---|---|
| FD-SOI | 12 nm (R&D) | Yes, wide range | Excellent | Wafer cost premium ~15–20% |
| FinFET (bulk) | 3 nm production | Limited | Moderate | Parasitic capacitance, cost |
| Gate-all-around | 2 nm (Samsung/TSMC) | Possible | TBD at volume | Process maturity |

## Cloudberry relevance

FinFET dominates leading-edge compute. FD-SOI owns the efficiency/RF sweet spot at 22–28 nm where IoT, automotive radar, satellite comms, and edge-AI inference sit. GaAs/SiGe BiCMOS compete on RF but lack digital integration density.

GF is a direct LP-fund portfolio touchpoint — 22FDX is a GF process node. Deal-flow angles: fabless startups targeting LPWAN, V2X, or LEO satellite modems needing low-power RF integration; edge-AI inference chips where back-bias enables DVFS without leakage blowup; any team choosing 22FDX over TSMC 28 nm for cost or IP reasons. Lunar Ventures' B2B SaaS portfolio is orthogonal, but hardware spinouts from EU deep-tech (STMicro ecosystem, CEA-Leti licensees) are natural Cloudberry pipeline.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
