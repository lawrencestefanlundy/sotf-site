---
type: concept
slug: image-sensor
canonical_name: Image sensor
aliases: []
related_concepts:
- spectral-sensing
- spectral-imaging-sensing
last_updated: '2026-08-31'
tags:
- concept
sources:
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-06-02-singular-photonics-launch]]'
mention_count: 24
frontier:
- Do SPADs in CMOS image sensor processes retain acceptable dark count rate after the full few × 10¹³ 1-MeV neutron equivalent/cm² dose required for LHC RICH upgrades, rather than the 10¹² so far tested 2026 06 05 characterization of cmos spads for future rich detectors?
- What yield and cost are achievable for wafer-scale stitched 65 nm sensors bent to beam-pipe radii, and does air cooling hold detection efficiency and resolution stable over an LHC run 2026 06 05 the new truly cylindrical tracker for the alice its3?
- Can 3D-stacked on-sensor DNN accelerators deliver measured TOPS/W and area figures competitive with off-sensor edge SoCs at equivalent task accuracy 2026 06 05 j3dai a tiny dnn based edge ai accelerator for 3d stacked cm?
- At what exposure time and source flux does qCMOS overtake EMCCD entirely, and does the crossover hold on apertures larger than 1 m 2026 06 05 the orca twin qcmos project i commissioning at calar alto ob?
- Does the 512× sketch compression preserve depth accuracy and photon-timing statistics well enough for LiDAR ranging at full sensor resolution, and how does the ratio scale with array size 2026 06 05 fpga implementation of sketched lidar for a 192 x 128 spad i?
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-02-singular-photonics-launch
  title: Singular Photonics — launch, SPAD portfolio + Meta collaboration (coverage)
  date: '2026-06-02'
  kind: web
- slug: 2026-02-12-how-to-invest-in-ai-sovereignty-sovereign
  title: How to Invest in AI Sovereignty — Sovereign Albion w/ Andrew Bennett
  date: '2026-02-12'
  kind: substack
neighbors:
- slug: spectral-sensing
  name: Spectral Sensing
  path: /sensing/mems/spectral-sensing/
  macro: sensing
---
## Physics / mechanism

An image sensor converts incident photons into an electrical signal on a spatially resolved grid of pixels. In CMOS implementations the photodiode, the in-pixel readout circuitry and, increasingly, the digital processing are fabricated in a standard logic-compatible process, which allows the sensor node size, depletion depth and doping profile to be tuned for a given application. Pixel pitch, sensitive-layer thickness, readout noise, frame rate and quantum efficiency are the primary parameters, and they trade against each other. A micro-pixel CMOS sensor developed for solar-flare X-ray polarimetry, for example, has a 2.5 µm pitch over a 12.8 × 12.8 mm² imaging area, with a measured sensitive layer of roughly 5 µm and insensitive layers of 0.8 µm Si, 2.1 µm SiO₂ and 0.24 µm Cu, giving a quantum efficiency of 3-4% at 10 keV development of solar flare x ray polarimeter with micro pixe.

CMOS image sensor process nodes are now used as a substrate for charged-particle tracking. The ALICE ITS3 upgrade uses wafer-scale Monolithic Active Pixel Sensors, up to 27 cm long, fabricated in a 65 nm CMOS image sensor process, thinned to 50 µm and bent around the beam pipe; an added low-dose n-type implant improves charge collection speed, with a spatial resolution of about 5 µm the new truly cylindrical tracker for the alice its3. The same design freedom applies to single-photon devices: SPADs have been produced in 55 nm BCD and 110 nm CMOS image sensor technologies and characterised for dark count rate after neutron irradiation up to 10¹² 1-MeV neutron equivalent/cm² characterization of cmos spads for future rich detectors.

Sensor cost and availability also shape optical system architecture. Multi-camera arrays use many commodity sensors in parallel: an epi-illumination multi-camera array microscope packs 24 synchronised units, each with a 13 megapixel CMOS image sensor, in a 4 × 6 array at 18 mm spacing, producing a stitched 72 × 108 mm² image at resolution down to 2.46 µm wide field reflective imaging with an epi illumination multi. Alternatively, temporal or spectral information can be encoded into spatial channels on a single sensor. A microlens array plus a stack of microscope cover glasses maps delayed replicas of a picosecond pulse onto a consumer-grade CMOS sensor, giving a 1.46 ps sampling interval, an effective 685 Gfps frame rate and ten frames of sequence depth for under US$500 in hardware low cost passive single shot ultrafast imaging at 685 gfps.

## Competitive landscape

For astronomical time-domain imaging, fast low-noise qCMOS sensors are displacing classical CCDs. Commissioning of an ORCA-Quest 2 camera on the 1.23 m telescope at Calar Alto found that qCMOS generally outperforms classical CCDs for high-cadence imaging on 1-metre-class telescopes, while EMCCDs remain competitive and in some cases slightly superior for very short exposures and faint sources the orca twin qcmos project i commissioning at calar alto ob. Within computational imaging, the sources support a three-way comparison of ways to increase information throughput: replicate sensors in an array wide field reflective imaging with an epi illumination multi, distribute image formation across several optical modules converging on one common sensor biorxiv bio cmsuperscript 2 distributed computational , or multiplex encoded channels onto one sensor and decode computationally low cost passive single shot ultrafast imaging at 685 gfps. The distributed-optics approach is presented as avoiding the hardware complexity of multi-camera systems and the contrast degradation associated with optical multiplexing biorxiv bio cmsuperscript 2 distributed computational .

Commercially, single-photon CMOS imaging sits alongside the broader edge-silicon segment; Semiconductor Engineering's Q2 2026 roundup recorded 80 semiconductor startups raising over $6.0B, with edge silicon re-emerging on physical-AI and on-device demand semiengineering startup funding q2 2026.

## Evidence base

## Frontier (open questions)

- Do SPADs in CMOS image sensor processes retain acceptable dark count rate after the full few × 10¹³ 1-MeV neutron equivalent/cm² dose required for LHC RICH upgrades, rather than the 10¹² so far tested characterization of cmos spads for future rich detectors?
- What yield and cost are achievable for wafer-scale stitched 65 nm sensors bent to beam-pipe radii, and does air cooling hold detection efficiency and resolution stable over an LHC run the new truly cylindrical tracker for the alice its3?
- Can 3D-stacked on-sensor DNN accelerators deliver measured TOPS/W and area figures competitive with off-sensor edge SoCs at equivalent task accuracy j3dai a tiny dnn based edge ai accelerator for 3d stacked cm?
- At what exposure time and source flux does qCMOS overtake EMCCD entirely, and does the crossover hold on apertures larger than 1 m the orca twin qcmos project i commissioning at calar alto ob?
- Does the 512× sketch compression preserve depth accuracy and photon-timing statistics well enough for LiDAR ranging at full sensor resolution, and how does the ratio scale with array size fpga implementation of sketched lidar for a 192 x 128 spad i?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
