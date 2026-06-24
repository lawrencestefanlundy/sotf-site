---
type: concept
slug: external-laser-source
canonical_name: External Laser Source (ELS) for Co-Packaged Optics
aliases:
- ELS
- external light source
- external laser module
parent_concepts:
- lasers
related_concepts:
- co-packaged-optics
- silicon-photonics
- optical-interconnect
- dfb-dbr-lasers
- optical-frequency-comb
sources:
- '[[2026-06-17-sivers-onet-enablence-external-light-source-cpo]]'
frontier:
- Through 2028 do volume CPO/optical engines keep sourcing laser modules externally (merchant wedge survives), or does on-die laser integration win?
last_updated: 2026-06-17
tags:
- concept
- photonics
- light-source
- cpo
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors:
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /sotf-site/manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: silicon-photonics
  name: Silicon Photonics
  path: /sotf-site/photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
- slug: optical-interconnect
  name: Optical Interconnect
  path: /sotf-site/communications/optical-interconnect/optical-interconnect/
  macro: communications
- slug: dfb-dbr-lasers
  name: DFB / DBR Lasers
  path: /sotf-site/photonic-systems/light-sources/dfb-dbr-lasers/
  macro: photonic-systems
---
In co-packaged optics the laser is kept **off** the switch/compute ASIC and supplied as a separate external module (DFB/DBR laser arrays, sometimes plus a comb source and a star coupler) feeding light into the photonic engine over fibre. The reason is structural: laser junctions are temperature-sensitive and wavelength-critical, and the ASIC runs extremely hot, so isolating the laser preserves wavelength stability and reliability/serviceability (**2026 06 17 Sivers Onet Enablence External Light Source Cpo**).

This separation is what makes the light source a **merchant, separately-sourced supply layer** — the durable private wedge in **Photonic Light Source Supply** (ELS forecast ~10% of a >$20B CPO market by 2036). It is the deliberate contrast to the **Photodetector** / **Photonic Photodetection Layer** case: detectors are CMOS-native and grow monolithically on the silicon-photonics die, so they do **not** de-integrate into a sourced layer the way lasers do. Lasers leave the die; detectors stay on it — which is why one is a supply thesis and the other a non-area.
