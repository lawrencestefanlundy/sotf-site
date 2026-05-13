---
type: concept
slug: duv-immersion-lithography
canonical_name: DUV / Immersion Lithography
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
- asml
- canon
- carl-zeiss-smt
- coventor-lam-research-subsidiary
- cymer-asml-subsidiary
- d2s
- entegris
- gigaphoton
- imec
- intel-foundry
- irresistible-materials
- jsr-corporation
- micron-technology
- naura-technology-group
- nikon
- onto-innovation
- samsung-semiconductor
- shanghai-micro-electronics-equipment-smee
- shin-etsu-chemical
- sk-hynix
- smic
- synopsys
- tokyo-ohka-kogyo-tok
- tsmc
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


# DUV / Immersion Lithography

*Kind: technology*

## Physics / mechanism

193 nm ArF excimer laser patterned through a refractive lens system onto a resist-coated wafer. Immersion variant interposes ultra-pure water (n ≈ 1.44) between final lens element and wafer, shrinking effective wavelength to ~134 nm and pushing numerical aperture to 1.35. Single-exposure resolution limit ~38 nm half-pitch; multi-patterning (SADP, SAQP, LELE) extends effective pitch to sub-10 nm at the cost of mask count and overlay budget. ASML NXT:2100i is current production workhorse; throughput ~275 wph. Installed base >3,000 tools globally. ArF-i remains the dominant patterning technology by wafer volume—EUV handles only a subset of critical layers.

## Competitive landscape

| Approach | Resolution (single expose) | Wavelength / NA | Cost/layer |
|---|---|---|---|
| ArF Immersion (193i) | ~38 nm hp | 193 nm / 1.35 | Low–medium |
| EUV (13.5 nm) | ~13 nm hp | 13.5 nm / 0.33 | High |
| High-NA EUV | ~8 nm hp | 13.5 nm / 0.55 | Very high |

## Cloudberry relevance

Multi-patterning with 193i competes directly with single-exposure EUV on logic nodes down to ~5 nm. Nanoimprint (CANON) and DSA (directed self-assembly) are adjacent but lack volume adoption. E-beam is used for mask writing and niche direct-write but throughput prohibits HVM.


GlobalFoundries runs 193i-only fabs (no EUV license post-IBM spin); every advanced GF process node depends on multi-patterning ArF-i. That makes mask infrastructure, overlay metrology, resist chemistry, and multi-patterning process IP directly relevant to Cloudberry's LP relationship. Deal-flow angles: novel resist materials (EUV-free shrink), computational lithography software, immersion fluid handling, and metrology tools that close overlay error budgets on SADP/SAQP flows—all accessible to sub-EUV fabs worldwide.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
