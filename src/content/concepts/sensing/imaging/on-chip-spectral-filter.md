---
type: concept
slug: on-chip-spectral-filter
canonical_name: On-chip spectral filter
aliases: []
related_concepts:
- spectral-sensing
- spectral-imaging-sensing
last_updated: '2026-08-31'
tags:
- concept
frontier:
- What passband full width at half maximum, out-of-band rejection and insertion loss do current on-chip filter arrays achieve, and at which wavelengths?
- Does moving spectral selection into the sensor die reproduce the quantitative accuracy demonstrated for detector-level energy binning in photon-counting CT, or does channel crosstalk dominate the error budget?
- How many independent spectral channels can be integrated per pixel before signal-to-noise per channel falls below the level needed for material or analyte discrimination?
- Are on-chip filters manufacturable in a standard CMOS or silicon photonics flow with passband drift small enough over temperature and process corners to avoid per-device calibration?
scorecard:
  viability: null
  drivers: null
  novelty: null
  diffusion: null
  impact: null
  timing_band: Unclear
  verdict: ''
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: spectral-sensing
  name: Spectral Sensing
  path: /sensing/mems/spectral-sensing/
  macro: sensing
---
**An on-chip spectral filter is a wavelength-selective optical structure fabricated directly onto an image sensor or photonic die so that spectral discrimination happens in the chip rather than in bulk optics; the sources supplied for this page do not address that technology at all, so no evidence-based assessment of it is possible here.**

## Summary

In the sensing and imaging taxonomy, an on-chip spectral filter refers to wavelength-selective optical structure built into the sensor stack itself: interference films, plasmonic or metasurface nanostructures, photonic resonators or lithographically patterned filter mosaics deposited over or alongside photodiodes. The intent is to replace bulk components (filter wheels, prisms, free-space gratings, discrete interferometers) so that a spectrometer or multispectral camera collapses into a single fabricated die. Where a conventional colour camera uses three or four broad filters, an on-chip spectral filter array aims for tens to hundreds of narrower channels, often with computational reconstruction recovering a spectrum from a set of deliberately overlapping, non-ideal filter responses.

The engineering parameters that decide whether such a device is useful are well defined in principle: peak transmission and therefore photon throughput, channel count and spectral resolution, inter-channel crosstalk, the sensor area consumed per spectral channel (which trades directly against spatial resolution), angular and thermal stability of the filter response, and compatibility with standard CMOS back-end processing, which determines whether the part can be made at image-sensor cost or only in a specialist fab. The competing approaches are bulk grating spectrometers, tunable filters, and detector-level spectral discrimination that needs no filter at all, such as energy-resolving photon counting.

The honest position on this page is that the supplied source set does not describe this technology. Every source tagged to the concept uses "spectral" in an unrelated sense: power-spectral analysis of EEG signals, mass-spectral features in metabolomics and plant volatile profiling, spectral graph theory in spatial transcriptomics, a spectral framework for epidemic inverse problems, and spectral computed tomography. The single source with any optical-hardware content, on photon-counting CT, concerns spectral separation achieved by energy-resolving detection rather than by an integrated filter. The concept tag appears to have been assigned by keyword rather than by subject matter, and no dimension below can be scored from this corpus.

## Viability (unscored)

## Drivers (unscored)

## Novelty (unscored)

## Diffusion (unscored)

## Impact (unscored)

## Timing Unclear

---
*Assessment drafted 2026-08-31 from up to 16 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
