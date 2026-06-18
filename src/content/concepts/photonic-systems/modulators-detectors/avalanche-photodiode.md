---
type: concept
slug: avalanche-photodiode
canonical_name: Avalanche Photodiode (APD / SPAD)
aliases:
- APD
- SPAD
- single-photon avalanche diode
- avalanche photodiode
- avalanche-photodiodes
- Avalanche Photodiodes
parent_concepts:
- photodetector
- photonic-integrated-circuits
- silicon-photonics
related_concepts:
- germanium-photodiodes
- ingaas-photodiodes
- hgcdte
- lidar
- time-of-flight
- free-space-photonics
- photonic-imaging
- quantum-cascade-lasers
sources:
- '[[2026-06-17-single-photon-detector-market-spad-snspd]]'
frontier:
- Can SPAD arrays integrated on 300 mm CMOS silicon reach single-photon timing jitter below 50 ps at wafer-level yield?
- Will InGaAs/InP APDs be displaced by Si-SPAD arrays for 1550 nm LiDAR as process nodes shrink, or does the NIR absorption edge remain a hard limit?
- What gating/quench circuit co-integration approach best amortises the per-pixel readout overhead in megapixel SPAD imagers?
- Does a single-photon detector (SPAD array / SNSPD) cross from niche into a system play big enough to escape the commodity-detector ceiling, outside incumbent capture? (see [[photonic-photodetection-layer]])
last_updated: 2026-06-17
tags:
- concept
- photonics
- photodetector
sources_7d: 1
sources_30d: 1
recent_mentions:
- slug: 2026-06-17-single-photon-detector-market-spad-snspd
  title: Single-photon detector market aggregation — SPAD, SiPM, SNSPD (2024–2035)
  date: '2026-06-17'
  kind: web
neighbors:
- slug: germanium-photodiodes
  name: Germanium Photodiodes
  path: /sotf-site/photonic-systems/modulators-detectors/germanium-photodiodes/
  macro: photonic-systems
- slug: ingaas-photodiodes
  name: InGaAs Photodiodes
  path: /sotf-site/photonic-systems/modulators-detectors/ingaas-photodiodes/
  macro: photonic-systems
- slug: hgcdte
  name: Mercury Cadmium Telluride
  path: /sotf-site/photonic-systems/modulators-detectors/hgcdte/
  macro: photonic-systems
- slug: lidar
  name: LiDAR
  path: /sotf-site/sensing/ranging-detection/lidar/
  macro: sensing
- slug: time-of-flight
  name: Time-of-Flight (iToF, dToF)
  path: /sotf-site/sensing/ranging-detection/time-of-flight/
  macro: sensing
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
> Merged canonical page (2026-06-17): absorbed the former duplicate `avalanche-photodiodes` (plural). One slug for the APD/SPAD concept.

An **avalanche photodiode (APD)** is a reverse-biased p-n junction that exploits impact ionisation to amplify photocurrent internally: a single absorbed photon generates an electron–hole pair that is accelerated by a high reverse-bias field (typically 20–200 V) until it creates secondary carriers, yielding gains of 10–100× before readout electronics. Operated above breakdown it becomes a **single-photon avalanche diode (SPAD)**, producing a binary Geiger-mode pulse per absorbed photon with timing jitter in the tens-to-hundreds of picoseconds.

## Physics / mechanism

The defining material parameters are the **impact-ionisation coefficients** (α for electrons, β for holes), the **excess noise factor** F(M), the **gain-bandwidth product** (GBP), and dark current. A favourable α/β ratio (low k) means low excess noise. **Separate absorption, charge and multiplication (SACM)** structures decouple the absorption and gain regions and are now standard. InGaAs/InP APDs dominate telecom (1310/1550 nm) with GBP ~160 GHz commercially; silicon APDs cover visible/NIR but cut off near 1 µm.

## Competitive landscape

| Detector | Wavelength | Noise (k) | CMOS-compatible |
|---|---|---|---|
| Si APD | 400–900 nm | Low (k~0.02) | Yes |
| InGaAs/InP APD | 900–1650 nm | Medium (k~0.4) | No |
| Ge-on-Si APD | 800–1600 nm | Medium-high (k~0.3) | Yes |

- **Si APD** — cheap, band-limited to ~1 µm.
- **InGaAs/InP APD** — telecom wavelengths, expensive, III-V fab-constrained, temperature-hostile for LiDAR.
- **Ge-on-Si APD** — the primary challenger: CMOS-compatible, wafer-scale, lower cost, but a less favourable k-ratio (higher noise).
- **HgCdTe APD** — MWIR/LWIR with near-unity k (near-noiseless gain), but cryogenic and defence-niche (see [Mercury Cadmium Telluride](/sotf-site/photonic-systems/modulators-detectors/hgcdte/)).
- **AlInAsSb, Al₀.₈Ga₀.₂As** — research-stage low-noise candidates.
- SPADs in SiPh platforms are displacing linear InGaAs APDs in quantum and ranging applications.

## Applications

SPADs are the key detector in **time-of-flight 3D imaging**, single-photon LiDAR, quantum-key-distribution receivers, and fluorescence-lifetime microscopy. Market sizing for the single-photon family (SPAD/SiPM ~$2.1B→$9.4B 2024–2031; SNSPD a smaller cryo-niche) is in **2026 06 17 Single Photon Detector Market Spad Snspd** — but SPAD/SiPM volume is incumbent-captured (Sony, STMicro, **Onsemi On Semiconductor**).

## Investment view (vehicle-agnostic)

The discrete high-speed / high-sensitivity detector is a single-component layer with a strategic-acquisition ceiling: value integrates into the silicon-photonics receiver or is bought by incumbents (the **Photonic Photodetection Layer** non-area). The larger, faster-growing pool is the single-photon / SiPM family for LiDAR, 3D sensing and quantum (**2026 06 17 Single Photon Detector Market Spad Snspd**: SPAD/SiPM ~$2.1B→$9.4B 2024–2031), but that volume is incumbent-captured (Sony, STMicro, **Onsemi On Semiconductor**) and SNSPD is a small cryogenic niche held by specialists.

Routes: **public** via the captured incumbents and SiPh primes; **track** a SiPh-native SPAD displacement play (monolithic Ge APD/SPAD on a CMOS SiPh platform, defensible IP in quench circuitry and pixel architecture) — a foundry-process-advantaged angle (GF 45CLO / 22FDX) that a European team could pursue. Worked single-component pass-case: **Moon Photonics** (HgCdTe e-APD).

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Can SPAD arrays on 300 mm CMOS reach single-photon timing jitter below 50 ps at wafer-level yield?
- Will InGaAs/InP APDs be displaced by Si-SPAD arrays for 1550 nm LiDAR as nodes shrink, or does the NIR absorption edge remain a hard limit?
- What gating/quench co-integration best amortises per-pixel readout overhead in megapixel SPAD imagers?
- Does a single-photon detector cross from niche into a system play big enough to escape the commodity-detector ceiling, outside incumbent capture? (**Photonic Photodetection Layer**)
