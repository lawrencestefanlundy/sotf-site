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
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: spectral-sensing
  name: Spectral Sensing
  path: /sensing/mems/spectral-sensing/
  macro: sensing
---
## Physics / mechanism

An on-chip spectral filter is a wavelength- or energy-selective element integrated directly into a sensor die or photonic circuit, so that spectral discrimination is performed in hardware at the point of detection rather than by a separate dispersive instrument. The supplied source set does not contain any direct characterisation of such devices: no source reports filter geometry, passband width, free spectral range, transmission efficiency, crosstalk between channels, or fabrication process. This page therefore records only the adjacent evidence available and should be treated as a stub until device-level sources are added.

The closest supported analogue in the corpus is detector-level energy discrimination in photon-counting computed tomography, where spectral separation is intrinsic to the detector rather than obtained by a second acquisition. Photon-counting CT was used to generate virtual monoenergetic images across 40 keV to 190 keV and to perform material decomposition for calcium hydroxyapatite inserts spanning 50 to 200 mg/cm3, with comparison against dual-energy CT at 120 and 140 kVp medrxiv photon counting computed tomography for phanto. This illustrates the general design argument for spectral discrimination in the sensor: one acquisition yields multiple spectral channels that can be recombined into quantitative material estimates.

The remaining sources tagged to this concept use "spectral" in the signal-processing sense, that is, decomposition of a time series or a mass spectrum into frequency or mass-to-charge components computed after acquisition. These include EEG power spectral classification medrxiv automated eeg classification to track levels o, spectrolaminar component modelling of local field potentials biorxiv spatial transcriptomic programs relate to spec and ion-pairing LC-MS metabolomics biorxiv reducing background ion burden in tributylamin. They are not evidence about integrated optical filters and are listed here only to make the tagging provenance explicit.

## Competitive landscape

No comparison between on-chip filter architectures is supported by these sources. The only hardware comparison present is between two spectral CT acquisition strategies: photon-counting CT, where spectral separation happens in the detector, versus dual-energy CT, where it comes from two tube voltages, evaluated at 120 and 140 kVp against phantom inserts of known composition medrxiv photon counting computed tomography for phanto. That axis, spectral separation in the sensor versus spectral separation in the source or in post-processing, is the same trade-off that motivates on-chip optical filters, but the corpus provides no optical-domain data point.

## Evidence base

- Photon-counting CT produced virtual monoenergetic images from 40 keV to 190 keV and was compared with dual-energy CT at 120 and 140 kVp for bone, muscle and adipose quantification, using inserts of 50 to 200 mg/cm3 calcium hydroxyapatite (2026-07-23) medrxiv photon counting computed tomography for phanto.
- Visual inspection of EEG power spectra remains the gold standard for ABCD consciousness classification; an automated convolutional network trained on 4,611 manually classified spectra matched it (2026-06-25) medrxiv automated eeg classification to track levels o.
- Spectral, temporal and complexity EEG features across 2,874 participants aged 5 to 18 showed unstable effect sizes at small sample sizes, with reproducibility emerging only in larger samples (2026-06-25) biorxiv sample size critically shapes the reliability .
- Local Spectral Expansion resolved frequency-by-depth LFP power maps into delta, theta, beta, low-gamma and high-gamma components across twelve matched macaque cortical regions (2026-07-09) biorxiv spatial transcriptomic programs relate to spec.
- Serial solid-phase extraction of tributylamine reduced background contaminant ions that increase spectral complexity and suppress analyte signal in LC-MS metabolomics (2026-06-25) biorxiv reducing background ion burden in tributylamin.
- Machine-learning seizure detection from amplitude-integrated EEG and compressed spectral array features reached AUCs of 0.80, 0.69 and 0.79 for random forest, SVM and neural network classifiers (2026-07-10) medrxiv neonatal seizure detection using combined aeeg.

## Frontier (open questions)

- What passband full width at half maximum, out-of-band rejection and insertion loss do current on-chip filter arrays achieve, and at which wavelengths?
- Does moving spectral selection into the sensor die reproduce the quantitative accuracy demonstrated for detector-level energy binning in photon-counting CT, or does channel crosstalk dominate the error budget?
- How many independent spectral channels can be integrated per pixel before signal-to-noise per channel falls below the level needed for material or analyte discrimination?
- Are on-chip filters manufacturable in a standard CMOS or silicon photonics flow with passband drift small enough over temperature and process corners to avoid per-device calibration?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
