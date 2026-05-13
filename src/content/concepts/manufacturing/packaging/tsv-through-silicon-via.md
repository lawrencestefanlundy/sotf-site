---
type: concept
slug: tsv-through-silicon-via
canonical_name: TSV / Through-Silicon Via
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- packaging
related_concepts: []
companies_using:
- 3dis-technologies
- amkor-technology
- ase-technology-holding
- brewer-science
- disco-corporation
- ev-group-evg
- fraunhofer-izm
- imec
- intel
- leti-cea-leti
- liqid-now-part-of-ecosystem-eliyan
- marvell-technology
- micron-technology
- okmetic
- samsung-electronics
- silex-microsystems
- siltectra-now-infineon-subsidiary
- sk-hynix
- tezzaron-semiconductor
- tower-semiconductor
- tsmc
- unimicron-technology
- velodea-xperi-invensas
- x-fab-silicon-foundries
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

# TSV / Through-Silicon Via

*Kind: technology*

## Physics / mechanism

A Through-Silicon Via is a vertical electrical interconnect that passes completely through a silicon die or wafer. Etched by deep reactive-ion etching (Bosch process), lined with a dielectric (typically SiO₂, ~100–200 nm), barrier-seeded (Ta/TaN), and filled with electroplated copper or tungsten. Key parameters: via diameter (2–10 µm in leading-edge HBM stacks), aspect ratio (10:1–20:1), pitch (down to ~40 µm in HBM3), and RC parasitics. Bandwidth density exceeds 1 TB/s/mm² in HBM3 implementations. Thermal resistance and copper pumping (CTE mismatch-driven extrusion) remain the core reliability constraints. Via-last, via-middle, and via-first integration schemes each carry different cost and yield profiles.

## Competitive landscape

Wire bonding (cheap, mature, ~100 MHz bandwidth ceiling) and embedded multi-die interconnect bridge (EMIB, Intel) are the primary alternatives. Fan-out wafer-level packaging (FOWLP/InFO, TSMC) avoids TSVs entirely for some 2.5D configurations. Hybrid bonding (Cu-Cu direct bonding, <10 µm pitch) is the successor technology for highest-density stacking and threatens TSV for leading-edge AI accelerator packages.

## Cloudberry relevance

| Approach | Pitch | Bandwidth density | Cost |
|---|---|---|---|
| TSV / HBM | ~40 µm | ~1 TB/s/mm² | High |
| EMIB | N/A (bridge) | Moderate | Medium |
| Hybrid bonding | <10 µm | >10 TB/s/mm² | Very high |


TSVs are the enabling interconnect for HBM—the memory stack sitting on every AI accelerator. For Cloudberry, relevance sits at the process-equipment and materials layer: dielectric deposition, barrier films, CMP slurries, and inspection metrology are fundable niches adjacent to GlobalFoundries' advanced packaging roadmap. Lunar portfolio companies in photonic chiplets increasingly need TSV-based interposers for co-packaged optics. Deal-flow angle: fabless photonics or chiplet IP companies dependent on 2.5D integration whose unit economics hinge on TSV yield improvements.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
