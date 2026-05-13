---
type: concept
slug: gan-on-si
canonical_name: GaN-on-Si
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- energy-power
- power-electronics
related_concepts: []
companies_using:
- ampleon
- belgan
- cambridge-gan-devices-cgd
- dynex-semiconductor
- enkris-semiconductor
- epc-efficient-power-conversion
- epigan-now-part-of-imec-spin-off-ecosystem
- gan-systems
- infineon-technologies
- innoscience
- integra-technologies
- metis-microsystems
- navitas-semiconductor
- nexgen-power-systems
- nexperia
- nxp-semiconductors
- odyssey-semiconductor
- power-integrations
- rfhic
- stmicroelectronics
- sumitomo-electric
- transphorm
- visic-technologies
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


# GaN-on-Si

*Kind: technology*

## Physics / mechanism

GaN grown epitaxially on large-diameter silicon substrates (200 mm dominant, 300 mm emerging). The lattice mismatch (~17%) and thermal expansion mismatch require buffer layer stacks—typically AlN nucleation + graded AlGaN—to manage threading dislocation density (~10⁸ cm⁻²) and wafer bow. The active device exploits the AlGaN/GaN heterointerface: spontaneous + piezoelectric polarisation induces a 2DEG with sheet carrier density ~10¹³ cm⁻² and electron mobility ~2000 cm²/V·s. Breakdown fields reach 3.3 MV/cm. Key figures of merit: R_on·A ~1–5 mΩ·cm² for 650 V devices; switching frequencies into MHz range. Dominant applications: power conversion (EV onboard chargers, data-centre PSUs, PFC), RF front-ends. Leading fabs: Infineon, STMicro, TSMC, GlobalFoundries, Wolfspeed (on SiC not Si), Transphorm, Navitas.

## Competitive landscape

GaN-on-SiC is the direct competitor for RF and high-power density applications—lower dislocation density, superior thermal conductivity (490 W/m·K vs 150 for Si), but 4× wafer cost and smaller diameter cap scalability. GaN-on-Si trades thermal headroom for CMOS-fab compatibility and cost. Silicon MOSFETs (SJ, superjunction) compete below 600 V on cost. SiC MOSFETs compete above 900 V on temperature tolerance.

## Cloudberry relevance

| Platform | Thermal conductivity | Max voltage | Wafer cost (relative) |
|---|---|---|---|
| GaN-on-Si | ~150 W/m·K | ~650 V practical | 1× |
| GaN-on-SiC | ~490 W/m·K | >1200 V | 4–6× |
| SiC MOSFET | ~490 W/m·K | 1700 V+ | 3–5× |


GlobalFoundries runs a qualified 200 mm GaN-on-Si power process (GF Fab 9, Malta NY)—direct deal-flow relevance for Cloudberry portfolio companies seeking a western, HVM-ready foundry alternative to Asian fabs. Investment angles: epiwafer suppliers, buffer-layer IP, gate dielectric startups solving E-mode reliability, and fabless design houses targeting EV/data-centre power. Lunar Ventures' early-stage focus maps onto IP-heavy fabless plays; Cloudberry's LP relationship with GF creates warm intro paths and co-investment signal from GF Ventures on GaN-adjacent deals.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
