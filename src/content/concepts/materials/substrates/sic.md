---
type: concept
slug: sic
canonical_name: SiC
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- materials
- substrates
related_concepts: []
companies_using:
- alphatec-alpha-sic
- amantys
- blixt-tech
- bosch-semiconductor
- byd-semiconductor
- cissoid
- coherent-corp-ii-vi-sic
- danfoss-silicon-power
- enlightra
- genesic-semiconductor-acquired-by-wolfspeed
- infineon-technologies
- mitsubishi-electric
- norstel-acquired-by-stmicro
- odyssey-semiconductor
- onsemi
- rohm-semiconductor
- sanan-ic-sic-division
- sic-processing-gmbh
- sicc-sic-substrate
- sicrystal-rohm-group
- stmicroelectronics
- vitesco-technologies
- weeroc-maplesemi
- wolfspeed
ideas_referencing: []
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2024-yole-power-sic-2024]]'
- '[[2024-yole-power-gan-2024]]'
- '[[2024-omdia-power-electronics-forecast]]'
- '[[2024-trendforce-foundry-2024]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 21
last_reorg_date: '2026-05-13'
sources_7d: 2
sources_30d: 4
---

# SiC

*Kind: technology · Attio deal count: 7*

## Physics / mechanism

Silicon carbide (SiC) is a wide-bandgap (WBG) semiconductor: bandgap 3.26 eV (4H polytype), breakdown field ~3 MV/cm, thermal conductivity ~490 W/m·K — roughly 3× silicon on all three figures. These properties enable power devices that switch faster, run hotter, and waste less energy than Si equivalents. Key device types: MOSFETs and Schottky barrier diodes (SBDs) rated 650 V–3.3 kV. State of the art: 200 mm wafer production ramping (Wolfspeed, Coherent, SICC), on-resistance figures approaching theoretical limits, defect density (micropipes, basal plane dislocations) still the primary yield lever. Dominant application: EV inverters, where SiC cuts switching losses ~50% vs Si IGBT.

## Competitive landscape


GaN-on-Si competes directly below 900 V — lower substrate cost, higher switching frequency, but inferior at high-voltage/high-temperature. Si IGBTs remain entrenched in cost-sensitive, lower-frequency applications. GaAs and InP are irrelevant here. Diamond is a longer-horizon competitor with superior theoretical properties but no manufacturable substrate ecosystem. The real competitive axis is SiC vs GaN segmentation by voltage class and thermal budget.

| | SiC | GaN-on-Si | Si IGBT |
|---|---|---|---|
| Voltage sweet spot | 900 V–3.3 kV | 100–650 V | 600 V–6.5 kV |
| Switching freq | 10–100 kHz | 100 kHz–10 MHz | 1–20 kHz |
| Substrate maturity | 150/200 mm | 6–8" (on Si) | Commodity |

## Cloudberry relevance
SiC substrate and epitaxy supply chain is a chokepoint — investable. Deal-flow angles: European SiC epi suppliers, defect-metrology tooling, SiC MOSFET gate-driver IP, and packaging (die-attach materials rated >200°C). GlobalFoundries has no SiC fab presence, which creates white space for portfolio companies targeting captive or merchant SiC foundry services. Lunar Ventures' hardware thesis intersects here on power electronics enabling electrification infrastructure. Watch SiC-on-insulator and SiC photonics (emerging) as adjacencies.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
