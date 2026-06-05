---
type: concept
slug: spatial-light-modulators
canonical_name: Spatial Light Modulators (SLMs)
aliases:
- SLM
- SLMs
- spatial light modulator
- LCOS-SLM
- DMD
- digital micromirror device
- liquid crystal on silicon
kind: technology
parent_concepts:
- photonic-systems
- modulators-detectors
related_concepts:
- holographic-volumetric-displays
- optical-neural-networks
- two-photon-polymerization
- xolography
- wafer-level-optics
- displays
- arvr
- metasurfaces-flat-optics
- barium-titanate
- lithium-niobate-tfln
- indium-phosphide
sources: []
frontier:
- III/V SLM miniaturisation — Microsoft has multiple papers; what is current pixel pitch and refresh rate ceiling?
- BTO-on-SiN heterogeneous integration as a path to fast SLM, or is BTO modulator-only? (Altro context)
- When does parallel-foci 2PP/xolography exceed 50 foci with SLM-driven beam shaping in production?
- Backplane integration architecture — III/V on Si, copper metamaterial (Neurophos), or LCOS legacy?
- Free-space active dielectric metasurface SLM at telecom (Flatlight-class) — does the AlN→Si transition preserve efficiency? Does any OCS integrator commit to a pilot?
- OCS market signal — Calient, Google OCS, Meta, Microsoft — are any of these actively scouting μs-class free-space SLM alternatives to MEMS?
last_updated: 2026-05-18
tags:
- concept
- technology
- photonics
- slm
- photonic-compute
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors:
- slug: holographic-volumetric-displays
  name: Holographic / Volumetric Displays
  path: /sotf-site/photonic-systems/displays/holographic-volumetric-displays/
  macro: photonic-systems
- slug: optical-neural-networks
  name: Optical Neural Networks
  path: /sotf-site/photonic-systems/photonic-compute/optical-neural-networks/
  macro: photonic-systems
- slug: two-photon-polymerization
  name: Two-Photon Polymerization
  path: /sotf-site/manufacturing/lithography/two-photon-polymerization/
  macro: manufacturing
- slug: xolography
  name: Xolography
  path: /sotf-site/manufacturing/lithography/xolography/
  macro: manufacturing
- slug: wafer-level-optics
  name: Wafer-Level Optics
  path: /sotf-site/photonic-systems/metasurfaces/wafer-level-optics/
  macro: photonic-systems
- slug: displays
  name: Displays
  path: /sotf-site/photonic-systems/displays/displays/
  macro: photonic-systems
- slug: arvr
  name: AR/VR
  path: /sotf-site/life-frontier/neural-interfaces/arvr/
  macro: life-frontier
- slug: metasurfaces-flat-optics
  name: Metasurfaces & Flat Optics
  path: /sotf-site/photonic-systems/metasurfaces/metasurfaces-flat-optics/
  macro: photonic-systems
- slug: barium-titanate
  name: Barium Titanate
  path: /sotf-site/materials/functional-layers/barium-titanate/
  macro: materials
- slug: lithium-niobate-tfln
  name: Lithium Niobate (TFLN)
  path: /sotf-site/materials/functional-layers/lithium-niobate-tfln/
  macro: materials
- slug: indium-phosphide
  name: Indium Phosphide (InP)
  path: /sotf-site/materials/substrates/indium-phosphide/
  macro: materials
---
*Cross-cutting photonic component appearing in 26+ concept pages.*

## Physics / mechanism

Devices that imprint a spatial pattern onto a coherent or incoherent light beam by modulating amplitude, phase, or polarization pixel-by-pixel. Three dominant technologies today:

Performance trade-offs: LCOS gives best phase resolution but is slow (≤120 Hz) and limited by liquid-crystal birefringence dynamics; DMD is fast but binary; MEMS is fast and continuous but small array. The frontier — bespoke metamaterial / III-V SLMs — promises GHz rates with continuous phase control on production-scale arrays, but manufacturing has historically been impossible at volume.

## Competitive landscape

Tom Walton-Pocock (Geometry, 2026-05-06) summarises the current frontier:

> *"Prior efforts to do III/V SLM all failed because manufacture was impossible … you have to make these tiny refractive units and III/V units have been notoriously tricky to make to wire in. The SLM standard now is everything is on a backplane. Building sufficiently many quantum wells that work all on the same wafer is combinatorially extremely hard. Microsoft tried this a lot — they have several papers."*

Implication: the dominant architectural pattern is **active optics layer + silicon-backplane electronics** (the LCOS pattern, but extending to non-LCOS materials). Lawrence's hypothesis: **III/V on silicon** is the eventual stack. BTO is on the wrong side of the SLM/modulator divide — it's a modulator material, not an SLM material.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- **Microsoft's III/V SLM papers** — Tom referenced multiple; pull via `/kb-research`. What pixel pitch, refresh rate, yield achieved?
- **Neurophos copper-metamaterial spec** — pixel pitch, switching speed, addressing scheme. Where Geometry's diligence landed.
- **OLIX architecture** — Tom + Geometry don't have material clarity. Watch for disclosures.
- **GF III/V-on-Si capability** — does any GF process node host III/V quantum wells with backplane integration?
- **Foundry path for active metasurfaces** — Neurophos-class metamaterials need bespoke fab; is there a path to standard foundry?
- **2PP parallel-foci ceiling** — current published SOTA 49 foci (Hahn/Wegener 2024); what unlocks 500+?
- **BTO-as-SLM** — Tom's view is "modulators only." Worth verifying with Altro: is there any device geometry where BTO functions as SLM?
