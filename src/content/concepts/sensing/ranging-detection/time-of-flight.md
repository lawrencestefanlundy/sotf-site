---
type: concept
slug: time-of-flight
canonical_name: Time-of-Flight (iToF, dToF)
aliases: []
kind: technology
parent_concepts:
- sensing
- ranging-detection
related_concepts: []
sources:
- '[[2026-08-03-spad-single-photon-market-scan]]'
- '[[2026-06-02-singular-photonics-launch]]'
frontier:
- Does asynchronous per-pixel peak detection hold up against strong solar background, where pile-up couples range and flux estimates 2026 06 05 performance bounds of ranging precision in spad based dtof l, or does its SNR-threshold trigger degrade exactly when it is most needed?
- Can DMD-based spatial modulation that turned a 64x64 SPAD array into an effective 256x256 at 670 m 2026 06 05 high resolution long range 3d single photon imaging with a c be reduced to a fieldable module, or does it stay a bench technique?
- Does in-pixel digital compute justify its silicon area and power against simply shipping more conventional SPAD pixels from a vertically integrated incumbent 2026 08 03 spad single photon market scan?
- Can a fabless SPAD challenger second-source away from its largest competitor's fab, and on what timeline 2026 08 03 spad single photon market scan?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 18
last_reorg_date: '2026-05-13'
scorecard:
  viability: 5
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 1
sources_30d: 3
recent_mentions:
- slug: 2026-08-03-spad-single-photon-market-scan
  title: SPAD / single-photon detector market scan — incumbent structure and company cohort
  date: '2026-08-03'
  kind: web
- slug: 2026-06-02-singular-photonics-launch
  title: Singular Photonics — launch, SPAD portfolio + Meta collaboration (coverage)
  date: '2026-06-02'
  kind: web
neighbors: []
---
**Time-of-flight sensing measures distance by timing how long light takes to return from a target, and it has moved from lab technique to a commodity depth-sensing layer in phones, cars and robots, with the current research frontier in how single-photon detector arrays are read out rather than in the ranging principle itself.**

## Summary

Time-of-flight (ToF) ranging recovers distance from the round-trip delay of an emitted optical signal. Two implementation families dominate. Direct ToF (dToF) timestamps individual photon arrivals against the laser fire, which in practice means single-photon avalanche diodes (SPADs) feeding time-to-digital converters and building a per-pixel histogram whose peak is the range. Indirect ToF (iToF) modulates a continuous-wave source and infers delay from the phase of the returned light, using pixels closer to conventional CMOS imagers. dToF buys ambient-light robustness and long range at the cost of timing electronics per pixel; iToF buys pixel simplicity at the cost of ambiguity and multipath sensitivity. The same acronym is used for an unrelated analytical technique, time-of-flight secondary ion mass spectrometry (ToF-SIMS) and ToF mass spectrometry generally, which appears widely in materials and chemistry work such as MOF thin-film characterisation and autonomous SIMS campaigns; this page is about optical ranging.

The parameters that decide a dToF system are photon budget against solar or scene background, detector dead time, laser pulse width and the quantisation resolution of the timing electronics. A Cramer-Rao lower bound analysis for SPAD dToF shows that pile-up caused by dead time does more than lose counts: it statistically couples the distance estimate to the photon flux rate, degrading precision, and it sets an optimal rather than maximal illumination level. The same analysis finds that adding photon-number-resolving capability to the detector yields rapidly diminishing returns. In other words, the physics ceiling is now reasonably well mapped, and design effort has shifted to architecture.

On the supply side, the market scan places STMicroelectronics as the leading SPAD player on the strength of CMOS-integrated SPAD and vertically integrated manufacturing at consumer and automotive volume, with Sony Semiconductor Solutions and Hamamatsu Photonics in a second tier and the patent landscape showing ST ahead of Sony and PixArt. At the application end, ToF modules are now treated as commodity parts: an Arducam ToF depth camera supplies point clouds for a fruit sugar prescreening classifier, and ToF sits alongside camera and ultrasound in a fused depth-estimation stack for sub-100 mW microcontroller platforms.

## Viability (5/5)

There is no open question about whether optical ToF ranging works. CMOS-integrated SPAD sensors are in consumer and automotive volume production from the incumbent supplier, and a 2026 agricultural sensing paper simply buys an Arducam ToF depth camera and an AS7265x NIR spectrometer as building blocks, reaching over 90% accuracy on a high/low sugar classification from the ToF point cloud alone. Technologies at low viability do not get used casually as inputs to other people's experiments.

**TLDR: Shipping in volume and used as an off-the-shelf commodity part in unrelated research; the physics limits are now derived rather than guessed at.**

## Drivers (4/5)

**TLDR: Demand is broad and already commercial; supply is concentrated in one vertically integrated incumbent, which is both a driver and a risk.**

## Novelty (3/5)

ToF as a concept is not novel, and the honest comparison is against other depth modalities and against previous ToF readout schemes. Against alternatives, the sources are suggestive rather than decisive: the ULP fusion work adds ultrasound and camera to ToF rather than relying on ToF alone, implying ToF is insufficient by itself under those constraints, while passive UWB radar work explicitly notes it lacks the known ToF first-path reference that tag-based systems enjoy, and has to reconstruct distance from multi-channel phase fusion instead. That is an argument that optical ToF's direct, unambiguous first-return timing is a real advantage where it is available.

Within ToF, the increments are specific and measurable but under-benchmarked. Asynchronous per-pixel depth reporting is claimed to reduce latency, mitigate motion blur and raise effective frame rate relative to frame-based systems, demonstrated at 2.4 microsecond latency, though the comparison baseline is not quantified. Spatial modulation with a DMD extends a 64x64 array to an effective 256x256 at 670 m, a sixteenfold pixel-count gain over the native format. Mid-infrared upconversion adds a ToF 3D imaging mode via picosecond optical gating while widening the acceptance angle to about 30 degrees, over tenfold better than periodically poled crystals, at frame rates to 216 kHz. Notably, the CRLB analysis argues one obvious upgrade path, photon-number resolution, delivers rapidly diminishing returns, which caps how much novelty is left on the detector side.

**TLDR: The ranging principle is old; the genuinely new content is readout architecture and computational aperture tricks, and the sources rarely give head-to-head baselines.**

## Diffusion (4/5)

Diffusion is largely accomplished for short-range consumer and automotive use, where CMOS-integrated SPAD ships at volume, and ToF modules are commodity enough to be dropped into an embedded agricultural rig without custom optics work. The adoption argument is therefore about extending into harder envelopes rather than about first adoption.

Three barriers show up in the sources. Power: on sub-100 mW platforms, adding sensors forces an explicit energy-versus-accuracy trade, which the fusion work handles with confidence-gated incremental sensor activation rather than always-on ToF. Photon-flux management: pile-up from dead time both loses information and couples the range estimate to flux, so there is an optimal, not maximal, illumination, which constrains outdoor and long-range operation. Bandwidth and data volume: frame-based synchronous readout carries redundant background data and computational load, the problem asynchronous event-driven readout is designed to remove. Long-range demonstrations still rely on bench apparatus such as a DMD alongside the SPAD array, which is a real barrier to fielding that class of performance. On the supply side, sole-sourcing challengers at the incumbent's fab is a diffusion constraint on competitive alternatives, not on the category itself.

**TLDR: Already diffused into consumer and automotive volume; remaining barriers are power, ambient-light pile-up and supply concentration rather than acceptance.**

## Impact (4/5)

The ceiling on the score is that value accrues as a sensor bill-of-materials line inside other systems, and the sources give no revenue, unit or cost figures to size it. The market structure described, with one vertically integrated incumbent holding consumer and automotive volume, suggests margins compress towards commodity for the sensor itself, with differentiation moving to in-pixel compute and readout architecture. High systemic importance, contested economic capture.

**TLDR: A foundational sensing layer for robotics, driving, wearables and inspection, but captured as a component margin rather than a platform.**

## Timing Now (0-2yr)

ToF ranging is already in consumer and automotive volume and is used as an off-the-shelf part in unrelated research,. Nothing about the category is prospective.

**TLDR: The technology is deployed; the 0-2 year question is whether event-driven and in-pixel-compute readout reaches product.**

## Overrated or underrated? Fairly rated

## Prediction

By 31 December 2028, at least one commercially announced SPAD depth sensor will implement asynchronous, per-pixel event-driven depth readout on-chip (as distinct from the FPGA proof-of-concept at 2.4 microsecond latency reported in), rather than global frame-synchronous histogramming.

## Evidence base

## Open questions

- Does asynchronous per-pixel peak detection hold up against strong solar background, where pile-up couples range and flux estimates, or does its SNR-threshold trigger degrade exactly when it is most needed?
- Can DMD-based spatial modulation that turned a 64x64 SPAD array into an effective 256x256 at 670 m be reduced to a fieldable module, or does it stay a bench technique?
- Does in-pixel digital compute justify its silicon area and power against simply shipping more conventional SPAD pixels from a vertically integrated incumbent?
- Can a fabless SPAD challenger second-source away from its largest competitor's fab, and on what timeline?

---
*Assessment drafted 2026-08-31 from up to 16 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
