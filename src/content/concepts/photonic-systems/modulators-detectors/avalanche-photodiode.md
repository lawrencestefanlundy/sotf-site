---
type: concept
slug: avalanche-photodiode
canonical_name: Avalanche Photodiode
aliases:
- APD
- SPAD
- single-photon avalanche diode
- avalanche photodiode
parent_concepts:
- photonic-integrated-circuits
- silicon-photonics
related_concepts:
- lidar
- time-of-flight
- hgcdte
- free-space-photonics
- photonic-imaging
- quantum-cascade-lasers
sources: []
frontier:
- Can SPAD arrays integrated on 300 mm CMOS silicon reach single-photon timing jitter below 50 ps at wafer-level yield?
- Will InGaAs/InP APDs be displaced by Si-SPAD arrays for 1550 nm LiDAR as process nodes shrink, or does the NIR absorption edge remain a hard limit?
- What gating/quench circuit co-integration approach best amortises the per-pixel readout overhead in megapixel SPAD imagers?
last_updated: 2026-06-02
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-02-singular-photonics-launch
  title: Singular Photonics — launch, SPAD portfolio + Meta collaboration (coverage)
  date: '2026-06-02'
  kind: web
neighbors:
- slug: lidar
  name: LiDAR
  path: /sotf-site/sensing/ranging-detection/lidar/
  macro: sensing
- slug: time-of-flight
  name: Time-of-Flight (iToF, dToF)
  path: /sotf-site/sensing/ranging-detection/time-of-flight/
  macro: sensing
- slug: hgcdte
  name: Mercury Cadmium Telluride
  path: /sotf-site/photonic-systems/modulators-detectors/hgcdte/
  macro: photonic-systems
- slug: free-space-photonics
  name: Free-Space Photonics
  path: /sotf-site/communications/fibre-and-free-space/free-space-photonics/
  macro: communications
- slug: photonic-imaging
  name: Photonic Imaging
  path: /sotf-site/sensing/imaging/photonic-imaging/
  macro: sensing
- slug: quantum-cascade-lasers
  name: Quantum Cascade Lasers
  path: /sotf-site/photonic-systems/light-sources/quantum-cascade-lasers/
  macro: photonic-systems
---
An **avalanche photodiode (APD)** is a reverse-biased p-n junction that exploits impact ionisation to amplify photocurrent internally: a single absorbed photon generates an electron–hole pair that is accelerated by a high electric field until it creates secondary carriers, yielding gains of 10–100× before readout electronics. Operating above the breakdown voltage converts the device into a **single-photon avalanche diode (SPAD)**, which produces a binary Geiger-mode pulse for each absorbed photon with timing jitter in the tens-to-hundreds of picoseconds range.

The defining material parameters are the **impact-ionisation coefficients** (α for electrons, β for holes) and the **excess noise factor** F(M). Silicon has a favourable α/β ratio (low excess noise) at visible wavelengths but cuts off near 1 µm; InGaAs/InP APDs extend sensitivity to 1.0–1.6 µm for telecom and eye-safe LiDAR, at the cost of higher dark-count rates and manufacturing complexity. Germanium-on-silicon APDs are an emerging monolithic route to 1550 nm sensitivity inside standard CMOS fabs.

SPADs are the key detector in **time-of-flight 3D imaging**, single-photon LiDAR, quantum-key-distribution receivers, and fluorescence lifetime microscopy. **Moon Photonics** works with mid-wave detector arrays that sit alongside APD technology in the photon-counting sensing stack.

## Frontier

- Can SPAD arrays integrated on 300 mm CMOS silicon reach single-photon timing jitter below 50 ps at wafer-level yield?
- Will InGaAs/InP APDs be displaced by Si-SPAD arrays for 1550 nm LiDAR as process nodes shrink, or does the NIR absorption edge remain a hard limit?
- What gating/quench circuit co-integration approach best amortises the per-pixel readout overhead in megapixel SPAD imagers?
