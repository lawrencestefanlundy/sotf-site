---
type: concept
slug: metalens
canonical_name: Metalens
aliases:
- meta-lens
- metalenses
- meta-lenses
- planar-lens
kind: technology
parent_concepts:
- photonic-systems
- metasurfaces-flat-optics
related_concepts:
- metasurfaces-flat-optics
- metamaterials
- nanoimprint-lithography
- maskless-lithography
- e-beam-lithography
- silicon-photonics
sources: []
frontier:
- When does metalens-only consumer optics shipment exceed 1B units/year (current ~140M cumulative across ST/Metalenz partnership)?
- Does any major smartphone OEM replace its primary camera lens stack (vs ToF auxiliary) with a metalens by 2028?
- Does NIL or maskless-lithography become the dominant production process by 2028, displacing e-beam-prototyping bottleneck?
- How many of the ~15 companies on the metasurfaces-flat-optics page survive the metalens consolidation cycle (NILT-Radiant acquisition was the first; expect 3-5 more by 2028)?
- Does European metalens IP retention vs Asian-acquirer flow continue (NILT → Radiant 2025 was a sovereignty leak; will the next 3 EU metalens companies follow)?
last_updated: '2026-05-08'
tags:
- concept
- technology
- metalens
- meta-optics
- photonics
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 1
recent_mentions: []
neighbors:
- slug: metasurfaces-flat-optics
  name: Metasurfaces & Flat Optics
  path: /sotf-site/photonic-systems/metasurfaces/metasurfaces-flat-optics/
  macro: photonic-systems
- slug: metamaterials
  name: Metamaterials
  path: /sotf-site/photonic-systems/metasurfaces/metamaterials/
  macro: photonic-systems
- slug: nanoimprint-lithography
  name: Nanoimprint Lithography
  path: /sotf-site/manufacturing/lithography/nanoimprint-lithography/
  macro: manufacturing
- slug: maskless-lithography
  name: Maskless Lithography
  path: /sotf-site/manufacturing/lithography/maskless-lithography/
  macro: manufacturing
- slug: e-beam-lithography
  name: E-Beam Lithography
  path: /sotf-site/manufacturing/lithography/e-beam-lithography/
  macro: manufacturing
- slug: silicon-photonics
  name: Silicon Photonics
  path: /sotf-site/photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
---
*child of [Metasurfaces & Flat Optics](/sotf-site/photonic-systems/metasurfaces/metasurfaces-flat-optics/)*

## Physics / mechanism

A metalens is a planar metasurface engineered to perform the focusing function of a conventional curved lens. Sub-wavelength meta-atoms (typically TiO₂, GaN, or amorphous silicon pillars, 50–400 nm feature size) are patterned on a flat substrate; the local geometry of each atom imposes a phase delay on incident light, so the array as a whole imparts a hyperboloidal phase profile equivalent to a curved lens. Replaces stacked refractive elements with a single planar layer fabricated by semiconductor processes (e-beam in the lab, DUV / nanoimprint in production).

Operating regimes:
- **Visible / NIR consumer**: TiO₂ on glass at ~90% diffraction efficiency at 532 nm, NA up to 0.9 demonstrated in lab. Production-grade NA ~0.5.
- **MWIR / LWIR**: GaN-on-silicon or amorphous-Si on Si-substrate; lower efficiency tolerance, currently dominant in industrial sensing.
- **UV**: HfO₂ / SiO₂ candidates; mostly research-stage.

## Competitive landscape

| Approach | Form factor | Volume process | Diffraction efficiency | Status |
|---|---|---|---|---|
| Refractive (curved glass / molded) | 3D stack | Injection / grinding | ~99% | Mature, cheap |
| Diffractive optical element (DOE) | Planar | Embossing / etch | 60-80% (visible) | Mature in IR |
| Metalens (TiO₂ / GaN) | Planar (single layer) | NIL or DUV | 70-90% (visible, monochromatic) | Production at consumer scale (Metalenz/ST since 2023) |
| MEMS-tunable | Planar + actuated | MEMS process | Variable | Niche |

**Production trajectory.** Metalenz + STMicroelectronics shipped the first commercial metasurface in a consumer ToF sensor (VL53L8) in 2023. Cumulative shipments ~140M as of 2025. NIL Technology (NILT, Denmark) is the parallel production-process leader, vertically integrated through nanoimprint masters → meta-optic modules; acquired by Taiwan's **Radiant Opto Electronics** for €300M in Jan 2025 (signed Sept 2024).

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

See frontmatter `frontier:` block.
