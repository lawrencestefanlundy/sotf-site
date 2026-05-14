---
type: concept
slug: ge-on-si-mid-ir
canonical_name: Germanium-on-Silicon Mid-IR Photonics
aliases:
- Ge-on-Si
- germanium photonics
- mid-IR Ge waveguides
kind: technology
parent_concepts:
- materials
- substrates
related_concepts:
- mid-ir-photonic-sensing
- silicon-photonics
- chalcogenide-glass
- quantum-cascade-lasers
sources: []
frontier:
- Can Ge-on-Si reach <1 dB/cm waveguide loss in the 3-8 μm band at production scale?
- Does Ge integration with QCL sources ([[quantum-cascade-lasers]]) enable a fully-integrated mid-IR sensing chip by 2028?
- Ge vs chalcogenide for mid-IR — does the CMOS-fab compatibility of Ge-on-Si win the battle, or does chalcogenide's wider transparency window matter more?
- Does Ge-Sn alloy waveguides extend the transparency window further into the long-wave IR (10+ μm), unlocking new sensing applications?
last_updated: 2026-05-08
tags:
- concept
- photonics
- germanium
- mid-ir
- sensing
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: silicon-photonics
  name: Silicon Photonics
  path: /sotf-site/photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
- slug: chalcogenide-glass
  name: Chalcogenide Glass
  path: /sotf-site/materials/advanced-materials/chalcogenide-glass/
  macro: materials
- slug: quantum-cascade-lasers
  name: Quantum Cascade Lasers
  path: /sotf-site/photonic-systems/light-sources/quantum-cascade-lasers/
  macro: photonic-systems
---
*CMOS-fab-compatible mid-IR waveguide platform for gas / breath / hyperspectral sensing*

## Physics / mechanism

Pure germanium is transparent from ~1.8 μm out to ~14 μm — covering most of the molecular-fingerprint mid-IR band where silicon absorbs (silicon's transparency cuts off around 4 μm at production-grade purity). Ge-on-Si waveguides leverage standard silicon photonic fab infrastructure with Ge epitaxy as an additional process step — already mature for Ge photodetectors integrated in silicon photonics.

The killer pitch: Ge-on-Si reuses the silicon-photonics ecosystem (CMOS fabs, design tools, foundries) for mid-IR applications, sidestepping the specialty-fab problem that limits chalcogenide. Combined with [Quantum Cascade Lasers](/sotf-site/photonic-systems/light-sources/quantum-cascade-lasers/) as the source side, a fully-integrated mid-IR PIC for chip-scale spectroscopy becomes feasible.

## Competitive landscape

## Frontier (open questions)

See frontmatter `frontier:` block.
