---
type: concept
slug: rad-hard-ics
canonical_name: Rad-Hard ICs
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
- 3d-plus
- antmicro
- apogee-semiconductor
- atmel-microchip-nantes-space-lab
- bae-systems-microelectronics
- caes-aeroflex-aeroflex-colorado-springs
- cobham-advanced-electronic-solutions-caes
- enpirion-intel-space-rad-hard
- frontgrade-technologies-formerly-sri-micro
- greenwaves-technologies
- ihp-microelectronics
- infineon-technologies-radiation-hardened
- issi-integrated-silicon-solution-inc
- lux-semiconductors
- microchip-technology-radiation-solutions
- nanoxplore
- renesas-electronics-space-rad-hard
- rha-solutions-radiation-hardness-assurance
- seakr-engineering
- sondrel
- stmicroelectronics-space-division
- syntiant-space-program
- tagore-technology
- texas-instruments-space-products
- vorago-technologies
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

# Rad-Hard ICs

*Kind: technology*

## Physics / mechanism

Rad-hard ICs are semiconductor devices engineered to tolerate ionising radiation environments — space, nuclear reactors, particle accelerators, medical imaging systems. Radiation damage manifests via two mechanisms: total ionising dose (TID), cumulative charge trapping in gate oxides that shifts threshold voltages and degrades leakage; and single-event effects (SEEs), transient ionisation from heavy ions or protons causing bit-flips (SEU), latch-up (SEL), or destructive burnout (SEB). Hardening approaches: radiation-hardened-by-process (RHBP) using specialised oxide growth and bipolar processes; radiation-hardened-by-design (RHBD) using enclosed-gate FETs, guard rings, TMR logic. State-of-the-art TID tolerance reaches 1 Mrad(Si); SEE LET thresholds above 80 MeV·cm²/mg are achievable. Key fabs: BAE Systems MicroElectronics, Microchip (Atmel), TSMC radiation-qualified flows, and GlobalFoundries' 22FDX with emerging RHBD libraries.

## Competitive landscape

Competing and adjacent approaches split along cost-vs-assurance axes. COTS-with-shielding is the low-cost fallback for LEO smallsats but adds mass and offers no SEE mitigation. FPGAs with scrubbing (Xilinx Kintex Rad, Microchip RTG4) compete for reconfigurable workloads. SiGe BiCMOS offers inherent TID resilience and dominates RF/mixed-signal rad-hard niches.

## Cloudberry relevance

| Approach | TID ceiling | SEE mitigation | Unit cost proxy |
|---|---|---|---|
| RHBP CMOS | >1 Mrad | Design-dependent | $$$$ |
| RHBD on COTS node | ~300 krad | TMR overhead | $$ |
| COTS + shielding | <100 krad effective | None | $ |


GlobalFoundries' 22FDX is a direct angle: FD-SOI's floating-body suppresses latch-up and GF is actively qualifying RHBD flows, making it a credible alternative to heritage SOS/SOI processes. New Space volume is collapsing NRE barriers — investable companies now build rad-hard IP blocks or EDA tooling for RHBD automation rather than owning a fab. Cloudberry deal-flow: fabless rad-hard IP vendors, RHBD-as-a-service on GF/TSMC qualified nodes, and radiation-test infrastructure plays serving the proliferating LEO constellation market.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
