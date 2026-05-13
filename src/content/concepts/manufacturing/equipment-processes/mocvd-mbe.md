---
type: concept
slug: mocvd-mbe
canonical_name: MOCVD / MBE
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
- aixtron
- azastra-opto
- bloo-semi
- compound-semiconductor-centre-csc
- enkris-semiconductor
- epigap-optronic
- epiworld-international
- ev-group-evg
- forge-nano
- fraunhofer-iaf
- iqe-plc
- landmark-optoelectronics
- laytec
- macom-technology-solutions
- mitsubishi-chemical-group-compound-semiconductor-division
- porotech
- quantum-epitaxial-designs
- sanan-optoelectronics
- silanna-semiconductor
- sumitomo-electric-industries
- transphorm
- veeco-instruments
- win-semiconductors
- wolfspeed
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

# MOCVD / MBE

*Kind: technology*

## Physics / mechanism

MOCVD (Metal-Organic Chemical Vapour Deposition) and MBE (Molecular Beam Epitaxy) are the two dominant epitaxial growth techniques for compound semiconductors. MOCVD flows metal-organic precursors (e.g. TMGa, TMIn) plus hydrides (AsH₃, PH₃) over a heated substrate; pyrolysis drives layer-by-layer deposition. MBE evaporates elemental sources in ultra-high vacuum (~10⁻¹⁰ Torr), enabling monolayer control via shuttered beams. Key parameters: growth rate (0.1–10 µm/hr), doping precision (≤10¹⁶ cm⁻³ background), interface abruptness (<1 monolayer), and wafer uniformity (±1–2% thickness across 6"). MOCVD dominates production (GaN LEDs, HEMTs, VCSELs, HBTs); MBE dominates R&D and quantum-layer structures where purity and abruptness are non-negotiable.

## Competitive landscape

MOCVD vs MBE is not really competitive—they occupy different niches—but both face pressure from alternative deposition approaches.

## Cloudberry relevance

| Technique | Throughput | Interface control | Typical use |
|---|---|---|---|
| MOCVD | High (multi-wafer reactors) | Good (±2 ML) | Production LEDs, RF, power |
| MBE | Low (single-wafer) | Excellent (<1 ML) | QW lasers, quantum dots, R&D |
| ALD / PEALD | High | Excellent (conformal) | Dielectrics, 2D materials, passivation |

Sputter and CVD are irrelevant for epitaxial III-V/III-N. ALD is encroaching on passivation and 2D-material growth. Hybrid approaches (MOMBE, GSMBE) exist but remain niche.


Cloudberry's photonics and compound-semi thesis makes MOCVD/MBE infrastructure the supply-chain chokepoint worth mapping. Foundry-adjacent startups (epitaxy-as-a-service, reactor tooling, in-situ metrology) are fundable; GlobalFoundries' LP relationship surfaces deal flow in GaN-on-Si and photonic integrated circuits where epi quality is the yield lever. Watch reactor vendors (Aixtron, Veeco) for spinouts, and university MBE labs commercialising quantum-dot laser or single-photon emitter IP.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
