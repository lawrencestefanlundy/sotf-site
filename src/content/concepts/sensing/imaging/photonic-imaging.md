---
type: concept
slug: photonic-imaging
canonical_name: Photonic Imaging
aliases: []
kind: category
parent_concepts:
- sensing
- imaging
related_concepts:
- lidar
- time-of-flight
- sensing-imaging
- avalanche-photodiode
- hgcdte
- free-space-photonics
- mid-ir-photonics
- spectral-sensing
- silicon-photonics
sources: []
frontier:
- Will chip-scale hyperspectral imagers reach cost parity with RGB cameras for consumer health wearables, or does pixel-count-versus-spectral-resolution tradeoff permanently stratify the market?
- Can computational imaging (coded aperture, event cameras, neural reconstruction) make low-cost sensors competitive with high-cost focal-plane arrays for industrial inspection?
- What integration level — monolithic vs flip-chip vs wafer-bond — best scales photon-counting SPAD imager arrays beyond 1 Mpixel at cost?
last_updated: 2026-06-02
tags:
- concept
- category
mention_count: 0
descendants: []
last_reorg_date: 2026-05-13
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: lidar
  name: LiDAR
  path: /sotf-site/sensing/ranging-detection/lidar/
  macro: sensing
- slug: time-of-flight
  name: Time-of-Flight (iToF, dToF)
  path: /sotf-site/sensing/ranging-detection/time-of-flight/
  macro: sensing
- slug: sensing-imaging
  name: Sensing & Imaging
  path: /sotf-site/sensing/imaging/sensing-imaging/
  macro: sensing
- slug: avalanche-photodiode
  name: Avalanche Photodiode
  path: /sotf-site/photonic-systems/modulators-detectors/avalanche-photodiode/
  macro: photonic-systems
- slug: hgcdte
  name: Mercury Cadmium Telluride
  path: /sotf-site/photonic-systems/modulators-detectors/hgcdte/
  macro: photonic-systems
- slug: free-space-photonics
  name: Free-Space Photonics
  path: /sotf-site/communications/fibre-and-free-space/free-space-photonics/
  macro: communications
- slug: mid-ir-photonics
  name: Mid-Infrared Photonics
  path: /sotf-site/photonic-systems/light-sources/mid-ir-photonics/
  macro: photonic-systems
- slug: spectral-sensing
  name: Spectral Sensing
  path: /sotf-site/sensing/mems/spectral-sensing/
  macro: sensing
- slug: silicon-photonics
  name: Silicon Photonics
  path: /sotf-site/photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
---
**Photonic imaging** is the category of sensing systems that form spatial or spectro-spatial images of a scene by detecting and processing photons — as distinct from electronic (radar, ultrasound) or chemical (film) imaging. The category spans:

- **3D / ranging:** LiDAR (direct ToF and FMCW), structured-light, and passive stereo — all relying on [Time-of-Flight (iToF, dToF)](/sotf-site/sensing/ranging-detection/time-of-flight/) measurement or geometric triangulation. [SPAD arrays](/sotf-site/photonic-systems/modulators-detectors/avalanche-photodiode/) are the detector of choice for single-photon 3D sensing.
- **Hyperspectral and multispectral:** snapshot or scanning imagers that resolve a spectral dimension (near-IR through LWIR) across each pixel, enabling material identification and gas-column imaging. [Mercury Cadmium Telluride](/sotf-site/photonic-systems/modulators-detectors/hgcdte/) FPAs dominate the thermal infrared bands; filter-wheel and Fabry–Pérot approaches serve near-IR.
- **Thermal imaging:** uncooled microbolometers and cooled HgCdTe arrays map scene temperature via MWIR/LWIR emission.
- **Computational imaging:** coded apertures, event cameras, and neural reconstruction pipelines that trade optics complexity for algorithm depth — relevant where SWaP constrains optic aperture.

The deep-tech investment angle is the **integration wedge**: moving from discrete optics + large focal-plane arrays to chip-scale photonic ICs with on-chip spectral filtering and pixel-level processing. [Mid-Infrared Photonics](/sotf-site/photonic-systems/light-sources/mid-ir-photonics/) integration drives cost reduction in spectroscopic imaging; [Silicon Photonics](/sotf-site/photonic-systems/pic-platforms/silicon-photonics/) underpins near-IR FMCW LiDAR.

## Frontier

- Will chip-scale hyperspectral imagers reach cost parity with RGB cameras for consumer health wearables, or does pixel-count-versus-spectral-resolution tradeoff permanently stratify the market?
- Can computational imaging (coded aperture, event cameras, neural reconstruction) make low-cost sensors competitive with high-cost focal-plane arrays for industrial inspection?
- What integration level — monolithic vs flip-chip vs wafer-bond — best scales photon-counting SPAD imager arrays beyond 1 Mpixel at cost?

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
