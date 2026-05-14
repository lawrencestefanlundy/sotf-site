---
type: concept
slug: hafnium-oxide-photonic
canonical_name: Hafnium Oxide (HfO₂) Photonics
aliases:
- HfO2 photonic
- hafnia photonic
- ferroelectric HfO2
kind: technology
parent_concepts:
- materials
- functional-layers
related_concepts:
- ferroelectric-memory-share
- silicon-photonics
- electro-optic-modulators
- gallium-foundries
- 22fdx
sources: []
frontier:
- Does HfO₂ ferroelectric (Si-doped or Zr-doped) reach commercially-relevant Pockels coefficient at production scale?
- Can HfO₂-photonic share fab tooling with HfO₂-FeFET memory at GlobalFoundries 22FDX — same materials, two functions on one chip?
- What's the loss penalty for HfO₂ waveguides at 1550 nm — competitive with SiN, or fundamentally lossier?
- Does any commercial photonic foundry productise HfO₂ as an EO module by 2028?
last_updated: 2026-05-08
tags:
- concept
- photonics
- hafnium-oxide
- ferroelectric
- cmos-native
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
---
*CMOS-native dielectric emerging as photonic EO + ferroelectric memory platform*

## Physics / mechanism

HfO₂ has been the standard high-k gate dielectric in CMOS since the 45nm node — every advanced silicon process already uses it. Doped variants (Si:HfO₂, Zr:HfO₂) exhibit ferroelectricity, with Pockels coefficient ~10-30 pm/V. The combination of CMOS-fab-native materials + emerging EO + ferroelectric memory makes HfO₂ a uniquely well-positioned candidate for monolithic photonic-electronic integration.

The strategic pitch: any process that can deposit HfO₂ for FETs can also deposit HfO₂ for photonic modulators. The fab learning curve is already paid for.

## Competitive landscape

Research stage for photonics. Production for FeFET memory: GF 22FDX-FeFET (commercially available since 2024), Sony, NaMLab spin-offs. Photonic modulator demonstrators: IMEC, Fraunhofer IPMS. Integration with the same fab line that serves FeFET memory is the unique-selling-point.

## Frontier (open questions)

See frontmatter `frontier:` block.
