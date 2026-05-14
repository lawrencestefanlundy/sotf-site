---
type: concept
slug: pzt-piezoelectric-photonic
canonical_name: Lead Zirconate Titanate (PZT) Photonics
aliases:
- PZT
- lead zirconate titanate
- Pb(Zr,Ti)O3
kind: technology
parent_concepts:
- materials
- functional-layers
related_concepts:
- barium-titanate
- piezoelectric
- ferroelectric-memory-share
- electro-optic-modulators
- silicon-photonics
sources: []
frontier:
- Lead-content regulatory risk — does RoHS / EU Critical Raw Materials Act limit PZT production for telecom by 2028?
- Does PZT-on-Si EO modulator performance match TFLN at >100 GHz — or stay below at lower-frequency niches?
- EpiPhotonics commercialisation — does the IBM Zurich PZT-on-Si platform reach foundry availability?
- Lead-free piezo replacements (KNN, NBT) — do they catch up to PZT performance for photonic applications?
last_updated: 2026-05-08
tags:
- concept
- photonics
- pzt
- piezoelectric
- ferroelectric
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: barium-titanate
  name: Barium Titanate
  path: /sotf-site/materials/functional-layers/barium-titanate/
  macro: materials
- slug: piezoelectric
  name: Piezoelectric
  path: /sotf-site/materials/functional-layers/piezoelectric/
  macro: materials
- slug: silicon-photonics
  name: Silicon Photonics
  path: /sotf-site/photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
---
*Strong piezoelectric + electro-optic ferroelectric for Si-integrated modulators*

## Physics / mechanism

PZT is a perovskite ferroelectric oxide with strong piezoelectricity (~600 pC/N) and Pockels electro-optic coefficient (~100-200 pm/V — comparable to BTO and ~5× LiNbO₃). Mature in piezo MEMS (sensors, actuators, ultrasound) and ferroelectric memory (FRAM, decades-mature for niche markets).

The photonic angle: PZT thin films on silicon (PZT-on-SOI, PZT-on-SiN) integrate strong EO modulation with the silicon photonic ecosystem. Sol-gel and PLD deposition routes are well-developed but require post-processing crystallisation that complicates CMOS-fab integration.

## Competitive landscape

EpiPhotonics (US, IBM Zurich derivative) is the lead commercialisation effort for PZT-on-SOI modulators. IBM Zurich, Princeton, and several European groups have published PZT-on-Si EO demonstrators. Lead-content regulatory pressure (RoHS) is a real constraint that limits some markets.

## Frontier (open questions)

See frontmatter `frontier:` block.
