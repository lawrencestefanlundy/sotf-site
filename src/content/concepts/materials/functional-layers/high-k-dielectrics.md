---
type: concept
slug: high-k-dielectrics
canonical_name: High-K Dielectrics (HfO2, ZrO2)
aliases: []
kind: material
domain:
- cloudberry
- sotf
parent_concepts:
- materials
- functional-layers
related_concepts: []
companies_using:
- air-liquide-semiconductor-division
- applied-materials
- asm-international
- cerfe-labs
- entegris
- ferro-corporation-now-part-of-prince-international
- ferroelectric-memory-company-fmc
- forge-nano
- fraunhofer-ipms
- globalfoundries
- imec
- intel
- knowmade
- lam-research
- merck-kgaa-emd-electronics
- micron-technology
- namlab
- pulsedeon
- rapidus
- samsung-foundry
- sk-hynix
- smic
- synopsys-sentaurus-tcad
- tsmc
- weebit-nano
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- material
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# High-K Dielectrics (HfO2, ZrO2)

*Kind: material*

## Physics / mechanism

High-k dielectrics replace SiO2 as the gate insulator in MOSFETs. SiO2 hit a physical limit ~1.2 nm (direct tunneling leakage becomes unacceptable below ~3 nm equivalent oxide thickness). High-k materials—HfO2 (k≈25), ZrO2 (k≈25), and their silicates/aluminates—allow a physically thicker film to achieve the same capacitive coupling (EOT), suppressing leakage by orders of magnitude. Intel/TSMC adopted HfO2-based gate dielectrics at 45nm (2007). Current nodes use HfO2 + metal gate stacks (HKMG) achieving EOT <0.5 nm at 3nm-class nodes. Interface trap density (Dit) and fixed charge are the key reliability parameters. Doping HfO2 with Si, Al, or La tunes phase stability and EOT.

## Competitive landscape

HfO2 also underpins ferroelectric FETs (FeFET): doping with Si, Zr, Y, or La stabilises the orthorhombic phase, enabling non-volatile memory without perovskite complexity. Competing dielectrics include Al2O3 (k≈9, excellent interface, limited capacitance benefit), La2O3/LaAlO3 (higher k, moisture-sensitive, integration difficult), and TiO2 (k>80, severe leakage). For ferroelectric applications, HfO2-based films compete directly with PZT and SBT—legacy perovskites with better Pr but CMOS-incompatible processing. ZrO2 sits at the HfO2/ferroelectric boundary; HZO (Hf0.5Zr0.5O2) is the leading FeFET/FeCAP material.

## Cloudberry relevance

| Material | k value | CMOS compatible | Ferroelectric |
|---|---|---|---|
| HfO2 (doped) | 20–25 | Yes | Yes (orthorhombic) |
| Al2O3 | 9 | Yes | No |
| PZT | 300–1000 | No | Yes |


Directly relevant to GlobalFoundries, which licenses FeFET IP and positions 22FDX as an FeFET-capable platform. FeFET/FeRAM startups (embedded NVM, neuromorphic, CIM) building on HZO are plausible Cloudberry deal-flow—asset-light, fabless or fab-partnered, often spun from Fraunhofer/imec. HfO2 gate stack IP also surfaces in wide-bandgap (GaN, SiC) power devices where high-k passivation is unsolved—a photonics-adjacent angle where Lunar-stage companies are emerging.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
