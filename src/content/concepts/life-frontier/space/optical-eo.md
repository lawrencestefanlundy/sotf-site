---
type: concept
slug: optical-eo
canonical_name: Optical EO (Planet, Maxar)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- space
related_concepts: []
companies_using:
- 21at-twenty-first-century-aerospace-technology
- airbus-defence-space
- albedo
- apollo-mapping
- blacksky-technology
- capella-space
- exolaunch-ororatech
- hera-systems-now-part-of-satellogic
- iceye
- iqps
- leaf-space-d-orbit
- maxar-technologies
- orbital-sidekick
- pixxel
- planet-labs
- satelites-mexicanos-kompsat-kariap-satellite
- satellogic
- skyfi-formerly-ursa-space
- skywatch
- soarearth
- spire-global
- spot-image-earthdaily-analytics-formerly-eads-astrium
- synthetaic
- umbra
- unseenlabs
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

# Optical EO (Planet, Maxar)

*Kind: technology*

## Physics / mechanism

Optical Earth Observation (EO) satellites capture reflected solar radiation across visible, near-infrared, and shortwave-infrared bands using push-broom or frame-camera architectures. Planet's SuperDove constellation (~200 satellites) delivers 3–5 m GSD multispectral imagery at daily revisit; Maxar's WorldView Legion targets 30 cm GSD panchromatic. Key parameters: ground sample distance (GSD), signal-to-noise ratio, swath width, revisit cadence, and radiometric calibration. Optical EO is daylight/cloud-limited. Focal-plane arrays use silicon CMOS or InGaAs for SWIR; detector pitch and telescope aperture set the resolution ceiling. State of the art pushes sub-30 cm commercial GSD with onboard radiometric correction and compressed downlink.

## Competitive landscape

SAR (Capella, ICEYE, Umbra) competes directly—cloud-penetrating, day/night, coherent phase data but lower intuitive interpretability and higher per-image cost. Hyperspectral (Pixxel, HyperScout) adds spectral resolution (200+ bands) at cost of GSD and data volume. Thermal IR (Satellogic, Orbital Sidekick) addresses different phenomenology. Multispectral vs. hyperspectral vs. SAR is a sensor-fusion problem, not winner-takes-all.

## Cloudberry relevance

| Modality | GSD (best commercial) | All-weather | Key use case |
|---|---|---|---|
| Optical MS | 30 cm | No | Change detection, agriculture |
| SAR | 25 cm | Yes | Maritime, deformation |
| Hyperspectral | 5 m | No | Mineralogy, crop stress |


Cloudberry relevance sits upstream: detector fabs, photonic readout ICs, and SWIR InGaAs arrays are semiconductor and photonics plays. GF's photonics and compound-semi capabilities (or adjacent fabs in the LP network) position the fund to back focal-plane array startups, on-board processing ASICs, or novel III-V detector materials that improve SWIR sensitivity or reduce cryogenic cooling requirements—bottlenecks limiting miniaturised high-resolution optical payloads.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
