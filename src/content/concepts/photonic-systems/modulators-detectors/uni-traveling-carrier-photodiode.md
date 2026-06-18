---
type: concept
slug: uni-traveling-carrier-photodiode
canonical_name: Uni-Traveling-Carrier Photodiode (UTC-PD)
aliases:
- UTC-PD
- UTC photodiode
parent_concepts:
- photodetector
related_concepts:
- germanium-photodiodes
- ingaas-photodiodes
- optical-interconnect
- co-packaged-optics
sources: []
frontier:
- Does a UTC/MUTC structure reach volume datacom (800G/1.6T) as a discrete sourced component, or stay a III-V niche for mmWave/THz and instrumentation?
last_updated: 2026-06-17
tags:
- concept
- photonics
- photodetector
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: germanium-photodiodes
  name: Germanium Photodiodes
  path: /sotf-site/photonic-systems/modulators-detectors/germanium-photodiodes/
  macro: photonic-systems
- slug: ingaas-photodiodes
  name: InGaAs Photodiodes
  path: /sotf-site/photonic-systems/modulators-detectors/ingaas-photodiodes/
  macro: photonic-systems
- slug: optical-interconnect
  name: Optical Interconnect
  path: /sotf-site/communications/optical-interconnect/optical-interconnect/
  macro: communications
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /sotf-site/manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
---
A high-speed photodiode in which **only electrons** are the active (fast) carriers — the absorption layer is p-doped so photogenerated holes relax quickly via majority-carrier response, while electrons traverse a separate depleted collection layer. This sidesteps the slow-hole space-charge bottleneck that limits conventional PIN photodiodes at high optical power, giving simultaneously **high bandwidth (200+ GHz demonstrated)** and high output power/linearity.

UTC-PDs are usually built in III-V (InGaAs/InP), with modified-UTC (MUTC) variants and silicon-integrated demonstrations. They dominate mmWave/THz photonics, optical-to-electrical conversion for wireless, and high-linearity instrumentation; they are a candidate structure for the next datacom bandwidth generation but, like the rest of the receiver layer, the value tends to integrate into the silicon-photonics platform or stay a III-V specialist part rather than a standalone business — see **Photonic Photodetection Layer**.
