---
type: concept
slug: nanoimprint-lithography
canonical_name: Nanoimprint Lithography
aliases:
- NIL
- nano-imprint-lithography
- UV-NIL
- thermal-NIL
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- lithography
related_concepts:
- maskless-lithography
- e-beam-lithography
- duv-immersion-lithography
- metalens
- metasurfaces-flat-optics
- metamaterials
companies_using:
- applied-materials
- cactus-materials
- canon
- eulitha
- ev-group-evg
- inkron
- kioxia
- lightpath-technologies
- liqxtal-technology
- micro-resist-technology
- molecular-imprints-acquired-by-canon
- morphotonics
- nano-x-nanofabrication-x
- nanonex
- nanova-biomatch
- nil-technology-nilt
- obducat
- prinano-technology
- radiant-opto-electronics
- scil-technology-a-suess-subsidiary
- simmonds-co-dek-nano
- sk-hynix
- suss-microtec
- toshiba
ideas_referencing:
- european-sovereignty-stack
- photonic-foundry-capacity
- beyond-euv-not-in-2020s
sources:
- '[[2025-01-06-radiant-acquires-nilt]]'
frontier:
- Does Canon FPA-1200NZ2C reach HVM in NAND at Kioxia by 2028, or stay research-stage?
- How fast does NIL scale for metalens consumer optics post NILT-Radiant acquisition (€300M, Jan 2025)?
- When does NIL displace e-beam for AR-waveguide master fabrication at production volume?
- Does multi-beam laser interference (maskless, e.g. Cnuic) take share from NIL for 3D / slanted-pyramid structures NIL contact-method limits cannot deliver?
- Mold lifetime + defect-rate curves at >100k impressions in production — public data still scarce.
last_updated: '2026-05-08'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 1
---


# Nanoimprint Lithography

*Kind: technology*

## Physics / mechanism

Nanoimprint lithography (NIL) presses a patterned hard mold (quartz or silicon) into a resist layer under heat or UV, transferring sub-10 nm features via mechanical deformation rather than optical projection. Two dominant variants: thermal NIL (heat resin above Tg, press, cool, strip) and UV-NIL (UV-curable resist, room temperature, ~1–10 bar pressure). Resolution is determined by mold feature fidelity, not wavelength—demonstrated sub-5 nm half-pitch in research. Throughput remains the constraint; Canon's FPA-1200NZ2C targets HVM at ~100 wph. Key parameters: overlay accuracy (<1 nm demonstrated), residual layer thickness control, mold lifetime (>10k impressions typical).

## Competitive landscape

| Technique | Resolution limit | Throughput | Cost driver |
|---|---|---|---|
| EUV (ASML NXE) | ~8 nm HP production | 150–200 wph | Tool capex ($150–200M+) |
| Nanoimprint (Canon) | <5 nm HP capable | ~100 wph | Mold fabrication + lifetime |
| Electron-beam direct write | <5 nm, maskless | <1 wph | Write time, no parallelism |

## Cloudberry relevance

NIL competes directly with EUV for leading-edge logic and NAND. Adjacent approaches include directed self-assembly (DSA), multi-patterning on DUV, and soft NIL for bio/photonics applications. Mold supply chain (Hoya, Toppan) and resist chemistry (JSR, Toray) are chokepoints. EUV has fab momentum; NIL's cost-per-wafer argument is strongest for memory and photonics.

Cloudberry relevance is highest in photonics and advanced packaging where NIL is enabling rather than competing with EUV. Grating couplers, [[metalens|metalens]] / [[metasurfaces-flat-optics|metasurface]] optics, and AR waveguide structures all use NIL at production scale. Deal-flow angles: mold materials startups, UV-curable resist chemistry, soft-NIL for integrated photonics substrates. GlobalFoundries doesn't run EUV, making NIL-patterned photonic components a credible differentiation play worth tracking for portfolio adjacency.

**The 2025 NILT → Radiant Opto-Electronics acquisition is a structural data point.** Taiwan-based **Radiant Opto Electronics** paid €300M for **NILT** (Denmark) in January 2025 to combine NILT's nanoimprint + meta-optics IP with Radiant's mass-production discipline (consumer-electronics scale). Two reads:
1. **NIL has graduated to consumer-electronics mass-production scale** — meta-optics is no longer research-stage; consumer ToF and AR products are the volume drivers
2. **European meta-optics IP exits to Asian acquirers** — see **European Sovereignty Stack**; NILT exit reflects structurally thinner European mass-production scale-up financing vs Asian strategic capital

**Where NIL fails — Cnuic angle.** Per Omar Durrani (**2026 05 08 Sotf Interview Omar Durrani Cnuic**): NIL "struggles with slanted/pyramid 3D structures" and is fundamentally a contact method. **Cnuic**'s multi-beam laser interference lithography is positioned as the 3D-structure-capable maskless alternative. NIL dominates flat / roll-to-roll / 2.5D structures; multi-beam interference targets 3D and curved.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

See frontmatter `frontier:` block for the canonical list. Headlines:
- Does Canon FPA-1200NZ2C reach HVM in NAND at Kioxia by 2028?
- How fast does NIL scale for metalens consumer optics post NILT-Radiant?
- When does NIL displace e-beam for AR-waveguide masters at production volume?
- Does multi-beam laser interference take share from NIL for 3D / slanted-pyramid structures NIL cannot deliver?
