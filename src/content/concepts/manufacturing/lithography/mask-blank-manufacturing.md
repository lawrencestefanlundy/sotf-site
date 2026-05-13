---
type: concept
slug: mask-blank-manufacturing
canonical_name: Mask Blank Manufacturing
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- lithography
related_concepts: []
companies_using:
- advanced-reproductions-corporation
- agc-inc-asahi-glass
- applied-materials-amat-semiconductor-products-group
- beijing-semiconductor-equipment-naura-technology-group
- carl-zeiss-smt
- coherent-corp-formerly-ii-vi-coherent
- compugraphics-international
- dai-nippon-printing-dnp
- entegris
- eutronis
- gudeng-precision-industrial
- hoya-corporation
- kla-corporation
- lasertec-corporation
- mitsui-chemicals
- nikon-corporation-precision-equipment-division
- omicronnano-omicron-nanotechnology
- photronics-inc
- shenzhen-newway-photomask-making
- shin-etsu-chemical
- ss-tech
- taiwan-mask-corporation-tmc
- toppan-inc
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


# Mask Blank Manufacturing

*Kind: technology*

## Physics / mechanism

Mask blanks are the upstream substrate from which photomasks are made. A blank consists of a low-thermal-expansion glass substrate (typically EUVL-grade Corning ULE or Schott Zerodur, with CTE ~0 ppb/K at 20°C) coated with absorber stack. For EUV, blanks carry a 40-bilayer Mo/Si multilayer reflective stack (~67% peak reflectance at 13.5 nm) deposited by ion-beam sputtering, plus a capping layer (Ru typically) and absorber (TaN or emerging low-n/high-k alternatives targeting phase-shift contrast). Flatness spec is <50 nm P-V across 152 mm; defect density targets <0.01 defects/cm² printable size. Only AGC, Hoya, and S&S Tech supply at volume; EUVL blank supply remains structurally constrained.

## Competitive landscape

---

## Cloudberry relevance

The direct competitive axis is blank supplier concentration—three vendors globally, zero Western alternatives at EUV spec. Adjacent tension: low-n absorber materials (TaN replacement candidates from imec/ASML roadmap) create re-qualification events that open supplier windows. Actinic blank inspection (only ASML's ABIx at scale) is a chokepoint separating blank quality from mask quality. Computational mask correction (inverse lithography, OPC) is a partial substitute insofar as it tolerates marginal blank defects—but cannot compensate for phase errors or multilayer non-uniformity.

| Approach | Maturity | Key constraint |
|---|---|---|
| Mo/Si multilayer EUV blank | HVM | Defect density, supplier duopoly |
| Low-n/high-k absorber stacks | Development | Material deposition control |
| Nanoimprint templates | Pilot (DRAM) | Resolution, overlay, throughput |

---

Mask blank supply is a single-point-of-failure in the EUV ecosystem—exactly the chokepoint-infrastructure thesis Cloudberry targets. Deal-flow angles: European or Japanese startups attacking defect inspection, alternative absorber deposition (ALD, PEALD), or substrate CTE engineering. GlobalFoundries-LP context: GF runs DUV-heavy nodes where DUV blank supply (Hoya dominance) and pellicle yield directly affect fab economics—supplier diversification or inspection tooling startups are natural portfolio candidates.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
