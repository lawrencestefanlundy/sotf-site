---
type: concept
slug: cmos-image-sensors
canonical_name: CMOS Image Sensors
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
- brillnics
- cmosis-ams-osram
- epfl-spin-off-aqua-vit-caeleste
- espros-photonics
- forza-silicon
- fsens
- galaxycore
- gigajot-technology
- gpixel
- intrinsic-semiconductor-technologies
- newsight-imaging
- omnivision-technologies
- on-semiconductor-onsemi
- pixart-imaging
- prophesee
- pyxalis
- samsung-semiconductor
- sionyx
- smartsens-technology
- sony-semiconductor-solutions
- stmicroelectronics
- teledyne-dalsa
- tower-semiconductor
- varex-imaging
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# CMOS Image Sensors

*Kind: technology*

## Physics / mechanism

CMOS image sensors (CIS) convert photons to charge via the photoelectric effect in silicon photodiodes, then read out voltage using in-pixel source-follower transistors. The dominant architecture is backside-illuminated (BSI) stacked CIS, where the photodiode layer is flip-bonded to a logic wafer carrying ADCs and ISP logic—decoupling pixel pitch scaling from readout circuit area. Key parameters: quantum efficiency (peak ~80–90% at 550 nm in BSI), read noise (<1e⁻ in scientific CMOS), full-well capacity, dynamic range, and dark current density. Leading nodes: Sony Semiconductor, Samsung, OmniVision on 90–45 nm CIS-optimized processes. Pixel pitches now reach 0.56 µm (mobile) to 3.45 µm (machine vision). Stacked 3D integration (Cu-Cu hybrid bonding) enables >1 Gpixel/s readout.

## Competitive landscape

CIS competes with and complements several sensor modalities. CCD retains niche dominance in astronomy and medical imaging due to lower fixed-pattern noise. SPAD arrays challenge CIS in low-light and LiDAR time-of-flight applications. InGaAs focal plane arrays own SWIR (900–1700 nm) where silicon is blind. Emerging alternatives include perovskite and organic photodetector layers that could be monolithically integrated on CMOS logic wafers, threatening the silicon absorber layer specifically.

## Cloudberry relevance

| Modality | Wavelength range | Key advantage vs CIS |
|---|---|---|
| CCD | 350–1000 nm | Lower FPN, higher uniformity |
| SPAD array | 400–900 nm | Photon counting, ToF depth |
| InGaAs FPA | 900–1700 nm | SWIR sensitivity |


CIS sits at the intersection of foundry process specialization and heterogeneous integration—both core Cloudberry theses. GlobalFoundries has qualified CIS-adjacent specialty nodes (22FDX, 130BCDlite) that are relevant to custom readout IC and mixed-signal pixel architectures. Deal-flow angles: startups building SWIR-on-CMOS stacks using III-V or colloidal quantum dot absorbers; fabless CIS companies targeting industrial/medical niches underserved by Sony/Samsung; and IP plays around hybrid bonding process control or in-pixel neuromorphic readout for edge inference.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
