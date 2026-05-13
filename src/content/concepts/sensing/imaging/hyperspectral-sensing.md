---
type: concept
slug: hyperspectral-sensing
canonical_name: Hyperspectral Sensing
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- sensing
- imaging
related_concepts: []
companies_using:
- applied-spectral-imaging-asi
- bayspec
- brim-brothers
- cubert
- digimarc-perception-robic-formerly-photon-dynamics-now-via-d
- headwall-photonics
- hyspex-norsk-elektro-optikk
- imec
- inno-spec
- norsk-titanium-ntnu-spin-off-hyspec
- orbital-sidekick
- photon-etc
- photonfocus
- pixxel
- rebellion-photonics
- resonon
- senop
- sensia-solutions
- specim
- surface-optics-corporation
- teledyne-dalsa
- unispectral
- ximea
- xpec-vision
- zolix-instruments
ideas_referencing: []
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
---

# Hyperspectral Sensing

*Kind: technology · Attio deal count: 22*

## Physics / mechanism

Hyperspectral sensing captures spatially-resolved spectral data across tens to hundreds of contiguous narrow bands (typically 5–20 nm FWHM) spanning UV through LWIR, versus RGB's three broad channels. Detectors — InGaAs (SWIR, 900–1700 nm), HgCdTe (MWIR/LWIR), or Si CMOS (VIS-NIR) — are paired with dispersive elements (prism-grating, Fabry-Perot MEMS, or acousto-optic tunable filters) or computed tomography approaches (snapshot mosaic sensors). Key parameters: spectral resolution, spatial resolution, SNR, and frame rate trade off against each other hard. State of the art: snapshot mosaic sensors now hit >100 fps at sub-10 nm resolution; MEMS Fabry-Perot arrays are shrinking the form factor toward chip-scale.

## Competitive landscape


Multispectral (4–20 fixed bands) is cheaper, faster, and adequate for many classification tasks — the main competitive pressure. Raman spectroscopy offers higher chemical specificity but requires contact or near-contact geometry. Fluorescence LiDAR adds depth. Mid-IR laser absorption (TDLAS, QCL-based) beats hyperspectral on selectivity for gas-phase analytes. Thermal IR cameras cover temperature mapping without spectral resolution. The real competitive question is whether the application needs continuous spectral curves or just band ratios.

| Technique | Spectral resolution | Standoff / field-use | Cost vector |
|---|---|---|---|
| Hyperspectral | 5–20 nm, contiguous | Yes | Falling fast |
| Multispectral | Fixed bands, ~10–20 | Yes | Low |
| Raman | Sub-nm | Limited | High |

## Cloudberry relevance
Cloudberry's photonics and semiconductor angle is direct: chip-scale Fabry-Perot MEMS and integrated photonic spectrometers are foundry-manufacturable processes — squarely in GF's process portfolio. Deal-flow sits at the intersection of photonic IC design houses, MEMS fabs, and application-layer software (ag-tech, semiconductor wafer inspection, pharma inline QC). Wafer inspection is the highest-margin pull. Watch for fabless hyperspectral sensor designers needing GF-LP capital to tape out on 200/300 mm lines.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
