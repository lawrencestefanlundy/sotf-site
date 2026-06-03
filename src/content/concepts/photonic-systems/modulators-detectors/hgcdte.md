---
type: concept
slug: hgcdte
canonical_name: Mercury Cadmium Telluride
aliases:
- HgCdTe
- MCT
- mercury cadmium telluride
parent_concepts:
- compound-semiconductors
related_concepts:
- avalanche-photodiode
- mid-ir-photonics
- photonic-imaging
- quantum-cascade-lasers
- sensing-imaging
- free-space-photonics
sources: []
frontier:
- Can MOVPE-grown HgCdTe on silicon substrates reach military-grade uniformity at commercial cost, or does lattice mismatch remain a disqualifier?
- Will avalanche-mode HgCdTe (eAPD) displace InGaAs APDs for 1–5 µm single-photon sensing, given HgCdTe's near-unity impact-ionisation ratio?
- At what CdTe composition does the Type-III (semimetal) crossover set a practical bandgap floor for room-temperature MWIR operation?
last_updated: 2026-06-02
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: avalanche-photodiode
  name: Avalanche Photodiode
  path: /sotf-site/photonic-systems/modulators-detectors/avalanche-photodiode/
  macro: photonic-systems
- slug: mid-ir-photonics
  name: Mid-Infrared Photonics
  path: /sotf-site/photonic-systems/light-sources/mid-ir-photonics/
  macro: photonic-systems
- slug: photonic-imaging
  name: Photonic Imaging
  path: /sotf-site/sensing/imaging/photonic-imaging/
  macro: sensing
- slug: quantum-cascade-lasers
  name: Quantum Cascade Lasers
  path: /sotf-site/photonic-systems/light-sources/quantum-cascade-lasers/
  macro: photonic-systems
- slug: sensing-imaging
  name: Sensing & Imaging
  path: /sotf-site/sensing/imaging/sensing-imaging/
  macro: sensing
- slug: free-space-photonics
  name: Free-Space Photonics
  path: /sotf-site/communications/fibre-and-free-space/free-space-photonics/
  macro: communications
---
**Mercury cadmium telluride (Hg₁₋ₓCdₓTe, HgCdTe or MCT)** is a II-VI ternary alloy whose bandgap is continuously tunable from ~0 eV (x = 0, pure HgTe semimetal) to ~1.5 eV (x = 1, CdTe) by varying the cadmium mole fraction x. This tunability makes HgCdTe the dominant photodetector material for **short-wave (SWIR, 1–3 µm), mid-wave (MWIR, 3–5 µm), and long-wave infrared (LWIR, 8–12 µm)** focal-plane arrays.

The key figures of merit are the **specific detectivity D***, cutoff wavelength λ_c (determined by composition), and operating temperature. MWIR HgCdTe can achieve background-limited performance (BLIP) at 77–200 K; LWIR arrays typically require 77 K cryocooling. High electron mobility (~10⁵ cm²/V·s at 77 K) and low effective mass also support **electron-APD (eAPD)** operation: in a thin multiplication region, the electron impact-ionisation coefficient dominates strongly over the hole coefficient, giving near-noiseless single-photon gain — an advantage InGaAs cannot match.

Substrate choices (CdZnTe bulk, CdTe/Si) and MOVPE vs LPE growth govern uniformity and scalability. **Moon Photonics** builds mid-wave HgCdTe detector arrays sitting within this material class. HgCdTe eAPDs increasingly compete with [SPAD](/sotf-site/photonic-systems/modulators-detectors/avalanche-photodiode/) arrays for lidar and FLIM applications in the 1–5 µm band.

## Frontier

- Can MOVPE-grown HgCdTe on silicon substrates reach military-grade uniformity at commercial cost, or does lattice mismatch remain a disqualifier?
- Will avalanche-mode HgCdTe (eAPD) displace InGaAs APDs for 1–5 µm single-photon sensing, given HgCdTe's near-unity impact-ionisation ratio?
- At what CdTe composition does the Type-III (semimetal) crossover set a practical bandgap floor for room-temperature MWIR operation?
