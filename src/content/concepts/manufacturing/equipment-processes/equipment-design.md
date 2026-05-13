---
type: concept
slug: equipment-design
canonical_name: Equipment & Design
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- equipment-processes
related_concepts: []
companies_using:
- ansys
- applied-materials
- asml
- axcelis-technologies
- bespoke-silicon-group
- cadence-design-systems
- coventor-lam-research
- fabric-cryptography
- fastprint-circuit-tech
- fraunhofer-iis-ims
- imec
- kla-corporation
- lam-research
- ligentec
- mentor-graphics-siemens-eda
- movella
- onto-innovation
- paragraf
- salience-labs
- seabird-technologies
- semilab
- semron
- siltectra-infineon
- synopsys
- tokyo-electron-tel
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 52
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---


# Equipment & Design

*Kind: technology · Attio deal count: 52*

## Physics / mechanism

Equipment & Design covers the tools and intellectual property layers that translate semiconductor physics into manufacturable products. Equipment spans lithography (ASML EUV at NA 0.33–0.55, sub-2nm patterning), CVD/ALD deposition (angstrom-level thickness control), etch (atomic-layer etch selectivity >100:1), CMP, and metrology (CD-SEM, scatterometry). EDA/design tools — Cadence, Synopsys, Siemens — convert architecture into GDSII, enforcing DRC, LVS, and increasingly AI-assisted place-and-route. Process design kits (PDKs) are the contractual interface between fab and designer. Cutting-edge nodes (2nm GAA) demand co-optimization of lithography, materials, and design rules simultaneously; the stack is tightly coupled.

## Competitive landscape


Equipment competes on throughput (wafers/hour), yield impact, and CoO. Litho alternatives: EUV multi-patterning vs. high-NA EUV vs. nanoimprint (Canon, EV Group) for cost-sensitive nodes. Deposition: ALD vs. MOCVD vs. MBE depending on material system. EDA competition narrows to Cadence/Synopsys duopoly; open-source (OpenROAD, Magic) relevant only at academic/prototype scale. Chiplet and 3D-IC architectures shift design complexity toward packaging EDA (Ansys, Siemens Xpedition), creating new toolchain adjacencies.

| Axis | Traditional EDA | AI-augmented EDA | Open-source EDA |
|---|---|---|---|
| Maturity | Production | Emerging | Research |
| PDK support | Full | Partial | Limited |
| Cost | High licence | High licence | Zero |

## Cloudberry relevance
For Cloudberry/GF-LP, PDK access is a structural moat — portfolio companies building photonic, compound-semi, or specialty-node designs depend on it directly. Deal-flow angles: EDA startups targeting photonic IC design (PIC PDKs are immature), novel metrology for advanced materials (SiC, GaN), and capital-efficient equipment plays targeting specialty fabs rather than leading-edge logic. Lunar Ventures' software lens adds relevance to AI-driven design automation and verification tooling at pre-seed.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
