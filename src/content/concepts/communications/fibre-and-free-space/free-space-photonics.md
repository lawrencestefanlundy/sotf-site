---
type: concept
slug: free-space-photonics
canonical_name: Free-Space Photonics
aliases:
- free-space optics
- free-space photonics
- FSO
parent_concepts:
- communications
- photonics
related_concepts:
- free-space-photonics
- lidar
- avalanche-photodiode
- photonic-imaging
- hgcdte
- co-packaged-optics
- optical-interconnect
- diffractive-deep-neural-network
- spatial-light-modulators
- mid-ir-photonics
sources:
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-06-16-trapped-ion-landscape-2026]]'
frontier:
- Can atmospheric-turbulence adaptive-optics correction (AO-FSO) reach the latency and power budget needed for untethered ground-to-ground links above 10 km?
- Will inter-satellite optical links (ISOL) become commodity infrastructure, and does that commoditise the terminal or the steering/pointing sub-system?
- What is the sustainable data-rate ceiling for a diffractive free-space compute link (light through air as a multiply-accumulate layer)?
last_updated: 2026-06-02
tags:
- concept
descendants:
- diffractive-deep-neural-network
mention_count: 18
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2026-06-16-trapped-ion-landscape-2026
  title: Trapped-ion quantum computing landscape 2026 (vendors, scale, integrated photonics)
  date: '2026-06-16'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
neighbors:
- slug: free-space-photonics
  name: Free-Space Photonics
  path: /communications/fibre-and-free-space/free-space-photonics/
  macro: communications
- slug: lidar
  name: LiDAR
  path: /sensing/ranging-detection/lidar/
  macro: sensing
- slug: avalanche-photodiode
  name: Avalanche Photodiode (APD / SPAD)
  path: /photonic-systems/modulators-detectors/avalanche-photodiode/
  macro: photonic-systems
- slug: photonic-imaging
  name: Photonic Imaging
  path: /sensing/imaging/photonic-imaging/
  macro: sensing
- slug: hgcdte
  name: Mercury Cadmium Telluride
  path: /photonic-systems/modulators-detectors/hgcdte/
  macro: photonic-systems
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: optical-interconnect
  name: Optical Interconnect
  path: /communications/optical-interconnect/optical-interconnect/
  macro: communications
- slug: spatial-light-modulators
  name: Spatial Light Modulators (SLMs)
  path: /photonic-systems/modulators-detectors/spatial-light-modulators/
  macro: photonic-systems
- slug: mid-ir-photonics
  name: Mid-Infrared Photonics
  path: /photonic-systems/light-sources/mid-ir-photonics/
  macro: photonic-systems
---
**Free-space photonics** is the transmission and manipulation of light beams through open space (air, vacuum) rather than through guided waveguides or fibre. It spans a wide application set united by the absence of a physical medium between source and receiver: **free-space optical communications (FSO)**, LiDAR, directed-energy sensing, inter-satellite laser links, and — at the intersection with computation — **diffractive free-space neural networks** where optical diffraction layers perform matrix–vector multiply in transit.

The engineering fundamentals differ sharply from guided photonics: beam divergence, pointing–acquisition–tracking (PAT), atmospheric turbulence (the primary impairment for terrestrial FSO), and background radiation dominate the link budget. Detectors must handle shot-noise-limited reception at high sensitivity — [APDs and SPADs](/photonic-systems/modulators-detectors/avalanche-photodiode/) are standard receivers for terrestrial FSO; [Mercury Cadmium Telluride](/photonic-systems/modulators-detectors/hgcdte/) FPAs serve MWIR atmospheric windows. Wavelengths are chosen for eye safety (1550 nm) and atmospheric transmission.

## Frontier

- Can atmospheric-turbulence adaptive-optics correction (AO-FSO) reach the latency and power budget needed for untethered ground-to-ground links above 10 km?
- Will inter-satellite optical links (ISOL) become commodity infrastructure, and does that commoditise the terminal or the steering/pointing sub-system?
- What is the sustainable data-rate ceiling for a diffractive free-space compute link (light through air as a multiply-accumulate layer)?
