---
type: concept
slug: hyperspectral-satellites
canonical_name: Hyperspectral Satellites
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- space
related_concepts: []
companies_using:
- aeye-analytics-dba-orbital-insight-context-separate-this-is-
- benespace-formerly-known-as-biocarbon-engineering-context-th
- chang-guang-satellite-technology
- exactearth-exactview-rt-spire-acquired-context-standalone-wa
- ghgsat
- hispec-headwall-photonics
- hydrosat
- hypersat
- kompsat-satrec-initiative
- kuva-space
- leonardo-spa
- ohb-system
- orbital-sidekick
- pixxel
- planet-labs
- rezatec
- satellogic
- satvu
- simera-sense
- specim-spectral-imaging-ltd
- thales-alenia-space
- tyvak-terran-orbital
- wyvern
- xona-space-systems
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

# Hyperspectral Satellites

*Kind: technology*

## Physics / mechanism

Hyperspectral satellites capture reflected or emitted electromagnetic radiation across hundreds of contiguous narrow spectral bands (typically 5–10 nm bandwidth) spanning VNIR through SWIR or LWIR (400–2500 nm+). Each ground pixel carries a full spectral signature, enabling material identification rather than just colour differentiation. Pushbroom sensors dominate: a line of detector pixels dispersed through a prism or grating onto a 2D focal-plane array (FPA). Key parameters: spectral resolution, SNR (target >200:1), GSD (commercial leaders now at 3–10 m), and revisit rate. State of the art: Planet's Tanager (30 bands, SWIR, methane detection), HyperScout, and Pixxel's Firefly constellation (55 bands, 5 m GSD). Onboard processing increasingly necessary to manage downlink bandwidth.

## Competitive landscape

Multispectral imaging (Sentinel-2, Landsat: 10–13 broad bands) handles most commodity use cases at lower cost and higher cadence. Thermal IR imagers (LWIR) compete for emissions monitoring. SAR offers all-weather, day-night operation but no chemical specificity. Airborne hyperspectral (AVIRIS-NG, HySpex) gives higher SNR and flexibility but no persistent coverage. On the detector side, InGaAs FPAs (SWIR) and HgCdTe (LWIR) are the incumbent materials; emerging CMOS-integrated filter arrays threaten cost structure.

## Cloudberry relevance

| Modality | Spectral bands | GSD | Weather-tolerant |
|---|---|---|---|
| Hyperspectral satellite | 100–400 | 5–30 m | No |
| Multispectral satellite | 10–13 | 3–10 m | No |
| SAR | N/A | 1–5 m | Yes |


The FPA and optical subsystem are the semiconductor-intensive chokepoints. InGaAs and HgCdTe detector fabs, photonic integrated circuit-based spectrometers, and CMOS-compatible narrowband filter arrays all sit inside Cloudberry's photonics and advanced materials thesis. Miniaturisation of hyperspectral sensors onto smallsats requires wafer-level optical fabrication—directly adjacent to GlobalFoundries-LP portfolio interests. Deal-flow angle: sensor IP companies, PIC-based spectrometer startups, and onboard inference chip designers enabling edge processing of hypercube data.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
