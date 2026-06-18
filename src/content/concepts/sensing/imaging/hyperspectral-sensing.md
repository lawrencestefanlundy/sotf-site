---
type: concept
slug: hyperspectral-sensing
canonical_name: Hyperspectral Sensing
aliases: []
kind: technology
parent_concepts:
- sensing
- imaging
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 22
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-01-13-diffraqtion-secures-42-million-to-deploy-quantum-camera-cons
  title: Diffraqtion Secures $4.2 Million to Deploy Quantum Camera Constellations for SDA - satnews.com
  date: '2026-01-13'
  kind: web
neighbors: []
---
## Physics / mechanism

Hyperspectral sensing captures spatially-resolved spectral data across tens to hundreds of contiguous narrow bands (typically 5–20 nm FWHM) spanning UV through LWIR, versus RGB's three broad channels. Detectors — InGaAs (SWIR, 900–1700 nm), HgCdTe (MWIR/LWIR), or Si CMOS (VIS-NIR) — are paired with dispersive elements (prism-grating, Fabry-Perot MEMS, or acousto-optic tunable filters) or computed tomography approaches (snapshot mosaic sensors). Key parameters: spectral resolution, spatial resolution, SNR, and frame rate trade off against each other hard. State of the art: snapshot mosaic sensors now hit >100 fps at sub-10 nm resolution; MEMS Fabry-Perot arrays are shrinking the form factor toward chip-scale.

## Competitive landscape

Multispectral (4–20 fixed bands) is cheaper, faster, and adequate for many classification tasks — the main competitive pressure. Raman spectroscopy offers higher chemical specificity but requires contact or near-contact geometry. Fluorescence LiDAR adds depth. Mid-IR laser absorption (TDLAS, QCL-based) beats hyperspectral on selectivity for gas-phase analytes. Thermal IR cameras cover temperature mapping without spectral resolution. The real competitive question is whether the application needs continuous spectral curves or just band ratios.

| Technique | Spectral resolution | Standoff / field-use | Cost vector |
|---|---|---|---|
| Hyperspectral | 5–20 nm, contiguous | Yes | Falling fast |
| Multispectral | Fixed bands, ~10–20 | Yes | Low |
| Raman | Sub-nm | Limited | High |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
