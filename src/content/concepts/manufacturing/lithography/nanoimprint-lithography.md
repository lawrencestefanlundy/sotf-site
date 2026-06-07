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
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: maskless-lithography
  name: Maskless Lithography
  path: /sotf-site/manufacturing/lithography/maskless-lithography/
  macro: manufacturing
- slug: e-beam-lithography
  name: E-Beam Lithography
  path: /sotf-site/manufacturing/lithography/e-beam-lithography/
  macro: manufacturing
- slug: duv-immersion-lithography
  name: DUV / Immersion Lithography
  path: /sotf-site/manufacturing/lithography/duv-immersion-lithography/
  macro: manufacturing
- slug: metalens
  name: Metalens
  path: /sotf-site/photonic-systems/metasurfaces/metalens/
  macro: photonic-systems
- slug: metasurfaces-flat-optics
  name: Metasurfaces & Flat Optics
  path: /sotf-site/photonic-systems/metasurfaces/metasurfaces-flat-optics/
  macro: photonic-systems
- slug: metamaterials
  name: Metamaterials
  path: /sotf-site/photonic-systems/metasurfaces/metamaterials/
  macro: photonic-systems
---
## Physics / mechanism

Nanoimprint lithography (NIL) presses a patterned hard mold (quartz or silicon) into a resist layer under heat or UV, transferring sub-10 nm features via mechanical deformation rather than optical projection. Two dominant variants: thermal NIL (heat resin above Tg, press, cool, strip) and UV-NIL (UV-curable resist, room temperature, ~1–10 bar pressure). Resolution is determined by mold feature fidelity, not wavelength—demonstrated sub-5 nm half-pitch in research. Throughput remains the constraint; Canon's FPA-1200NZ2C targets HVM at ~100 wph. Key parameters: overlay accuracy (<1 nm demonstrated), residual layer thickness control, mold lifetime (>10k impressions typical).

## Competitive landscape

| Technique | Resolution limit | Throughput | Cost driver |
|---|---|---|---|
| EUV (ASML NXE) | ~8 nm HP production | 150–200 wph | Tool capex ($150–200M+) |
| Nanoimprint (Canon) | <5 nm HP capable | ~100 wph | Mold fabrication + lifetime |
| Electron-beam direct write | <5 nm, maskless | <1 wph | Write time, no parallelism |

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
