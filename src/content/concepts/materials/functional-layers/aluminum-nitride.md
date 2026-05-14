---
type: concept
slug: aluminum-nitride
canonical_name: Aluminum Nitride (AlN)
aliases:
- AlN
- aluminium nitride
- AlN-on-sapphire
kind: technology
parent_concepts:
- materials
- functional-layers
related_concepts:
- scandium-aluminum-nitride
- gallium-nitride
- silicon-nitride
- piezoelectric
- electro-optic-modulators
sources: []
frontier:
- Does AlN reach 0.1 dB/cm waveguide loss at scale, or stay at ~1 dB/cm prototype demonstrations?
- Does ScAlN displace AlN for piezo-photonic devices because of its 5-10× stronger piezo+EO coefficients?
- Can AlN's UV transparency open a new application class (UV photonic ICs for chip-scale water/air monitoring) that silicon-photonics platforms can't address?
- Does any commercial photonic foundry add an AlN module to a multi-material PDK by 2028?
last_updated: 2026-05-07
tags:
- concept
- photonics
- aluminum-nitride
- piezo
- uv
mention_count: 0
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: scandium-aluminum-nitride
  name: Scandium Aluminum Nitride (ScAlN)
  path: /sotf-site/materials/functional-layers/scandium-aluminum-nitride/
  macro: materials
- slug: silicon-nitride
  name: Silicon Nitride
  path: /sotf-site/materials/substrates/silicon-nitride/
  macro: materials
- slug: piezoelectric
  name: Piezoelectric
  path: /sotf-site/materials/functional-layers/piezoelectric/
  macro: materials
---
*Wide-bandgap photonic + piezoelectric platform with UV transparency*

## Physics / mechanism

AlN has a wide bandgap (~6.2 eV — wider than SiC), making it transparent through UV. Refractive index ~2.1 at 1550 nm. AlN is non-centrosymmetric, so it exhibits second-order nonlinearity (χ²), enabling efficient electro-optic modulation and frequency conversion. It is also strongly piezoelectric, making it the dominant material for film bulk acoustic resonators (FBARs) in RF filters — the same property opens electro-acoustic modulators in photonics.

CMOS-fab compatibility is decent: AlN deposits via sputtering at moderate temperatures and is already used in MEMS lines. The challenge is high-quality crystalline AlN (vs polycrystalline) — single-crystal AlN-on-sapphire is the lab path; commercial AlN-on-Si is polycrystalline and lossy.

## Competitive landscape

AlN photonic waveguides have been demonstrated since 2012 (Yale group, IBM Zurich). Best loss ~0.5–1 dB/cm. Commercial photonic platforms: none yet. RF/MEMS commercial: Soitec (POI substrates), Skyworks, Qorvo, Broadcom for FBARs.

ScAlN (scandium-doped AlN) has emerged as the higher-performance variant — adding Sc increases piezoelectric and electro-optic coefficients 5–10× over pure AlN. ScAlN also exhibits ferroelectricity at certain compositions, opening additional functionality. See [Scandium Aluminum Nitride (ScAlN)](/sotf-site/materials/functional-layers/scandium-aluminum-nitride/).

## Frontier (open questions)

See frontmatter `frontier:` block.
