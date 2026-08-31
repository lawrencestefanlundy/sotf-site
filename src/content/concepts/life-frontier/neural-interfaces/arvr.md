---
type: concept
slug: arvr
canonical_name: AR/VR
aliases: []
kind: technology
parent_concepts:
- life-frontier
- neural-interfaces
related_concepts: []
sources:
- '[[2025-01-07-fund-frontier-expeditions-otherwise]]'
- '[[2023-05-25-interview-ben-mildenhall-co-inventor]]'
- '[[2026-08-03-spad-single-photon-market-scan]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
scorecard:
  viability: null
  drivers: null
  novelty: null
  diffusion: null
  impact: null
  timing_band: Unclear
  verdict: ''
scorecard_status: draft
mention_count: 33
sources_7d: 0
sources_30d: 4
recent_mentions:
- slug: 2026-08-03-spad-single-photon-market-scan
  title: SPAD / single-photon detector market scan — incumbent structure and company cohort
  date: '2026-08-03'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2025-01-07-fund-frontier-expeditions-otherwise
  title: Fund Frontier Expeditions otherwise just buy the "Magnificent Seven"
  date: '2025-01-07'
  kind: substack
- slug: 2023-05-25-interview-ben-mildenhall-co-inventor
  title: '☎️ Interview: Ben Mildenhall, Co-Inventor of Neural Radiance Fields (NeRFs) on the State of the Neural Rendering, Generative AI, and the Metaverse #007'
  date: '2023-05-25'
  kind: substack
neighbors: []
---
**AR/VR is the near-eye display and spatial-computing category that pulls together miniature optics, depth sensing, stretchable displays and on-device 3D reconstruction, and the 2026 literature shows its enabling components advancing in the lab while the flagship optical shortcut, the metalens eyepiece, fails at system level.**

## Summary

AR/VR head-worn systems need four things at once: an image source, an optic that puts that image on the retina from a few millimetres away, sensors that map the room and the wearer, and enough local compute to render and track at low latency inside a thermal budget. Each of those is a separate hardware discipline, and the sources here are almost entirely component papers that name AR/VR as their motivating application rather than assessments of headsets themselves.

On optics, the standard proposal has been to replace the bulky refractive eyepiece with a metalens, a flat nanostructured surface that focuses by diffraction. A 2026 study designed, fabricated and benchmarked a single-layer silicon nitride metalens tuned to the three emission peaks of an RGB OLED, and found that although it looks excellent by the usual metrics of point spread function and modulation transfer function under coherent light, it produces pronounced ghosting and background haze in a realistic testbed with incoherent OLED illumination, a dynamic-pupil eye model and near-eye focal lengths. The cause is intrinsic: polychromatic diffractive focusing is inherently multifocal. That is a rare and useful negative result, and it tells you the metric you evaluate a near-eye optic on decides whether you believe it works.

Around that sit the supporting layers. Visible-wavelength photonic integrated circuits are the route to compact RGB light engines, and a 200 mm CMOS pilot line now demonstrates a dual silicon nitride platform with active components added by micro-transfer printing as a back-end step; a visible spectral-domain OCT method has just been shown as the missing nondestructive diagnostic for those circuits, with 50 dB dynamic range and 8 um axial resolution in silicon nitride. For sensing, a 320x240 SPAD direct time-of-flight flash LiDAR reaches 108 m range with 2.93 mm depth resolution at 167.4 mW array power in 110 nm CMOS. For compute, a compute-in-memory architecture for Gaussian splatting reports 18 pJ per log-likelihood inference, aimed at edge robotics and AR/VR. And for form factor, a heterogeneous-modulus PDMS substrate achieves near-zero Poisson ratio so stretchable displays stop distorting laterally under strain.

The parameters that decide the category, as these sources frame it, are: system-level image quality under incoherent, dynamic-pupil conditions rather than bench PSF; milliwatt-class power for always-on depth sensing and reconstruction; and whether visible photonics can be manufactured at wafer scale with usable process control. Note that this concept sits under neural interfaces in the taxonomy, but none of the supplied sources connect AR/VR to neural interfacing in any way.

## Viability (unscored)

## Drivers (unscored)

## Novelty (unscored)

## Diffusion (unscored)

## Impact (unscored)

## Timing Unclear

---
*Assessment drafted 2026-08-31 from up to 11 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
