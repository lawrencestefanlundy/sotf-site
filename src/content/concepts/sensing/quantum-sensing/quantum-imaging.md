---
type: concept
slug: quantum-imaging
canonical_name: Quantum Imaging (ghost, sub-shot-noise)
aliases: []
kind: technology
parent_concepts:
- sensing
- quantum-sensing
related_concepts: []
sources: []
frontier:
- At fixed total acquisition time and identical illumination at the sample, does coincidence-based contrast enhancement beat classical time gating or spatial filtering, or does the shot-noise penalty cancel the gain 2026 05 29 contrast enhanced imaging through weakly scattering media wi?
- How does scanning QIUL phase imaging compare with conventional mid-infrared spectroscopic imaging on time per field of view, sensitivity and instrument cost 2026 07 20 quantum scanning synthetic optical holography?
- Can integrated thin-film lithium niobate pair sources deliver enough brightness and spatial-mode quality to replace bulk SPDC crystals inside an imaging instrument 2026 05 04 generation of tunable entanglement from thin film lithium ni?
- Do sub-shot-noise imaging schemes retain a measurable advantage at the detection efficiencies and squeezing levels actually available, given the reported fragility to loss and the 2.03 dB figure from multiplexed sources 2026 08 04 below shot noise capacity in phase estimation using nonlinea 2026 05 28 large scale array of squeezed light and synchronization usin?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 14
last_reorg_date: '2026-05-13'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 3
recent_mentions: []
neighbors: []
---
**Quantum imaging uses correlated or squeezed light (entangled photon pairs, squeezed beams) to form images with contrast, wavelength coverage or noise properties that a classical beam of the same brightness cannot provide, and as of 2026 it remains a set of laboratory demonstrations whose most convincing advantage is wavelength conversion rather than raw sensitivity.**

## Summary

Quantum imaging is a family of optical techniques that exploit non-classical light. Three strands dominate. **Ghost and two-photon imaging** use spatially entangled photon pairs, typically from spontaneous parametric down-conversion (SPDC), where one photon probes the object and the other is detected on a camera or scanned detector; the image appears only in the coincidence statistics between the two arms. **Imaging with undetected light (QIUL)**, based on nonlinear interferometers and induced coherence, probes the sample with one photon of the pair but detects only its partner, so the sample can be illuminated at, for example, mid-infrared wavelengths while detection happens in the visible, where detectors are cheap and efficient. **Sub-shot-noise imaging and sensing** uses squeezed or twin-beam light to push intensity or phase measurements below the noise floor set by Poissonian photon statistics, in principle towards Heisenberg scaling.

The physics is settled; the engineering parameters decide whether any of it is useful. The first is photon budget. Correlation-based methods throw away most detections: a scattering-media contrast demonstration improved image contrast by post-selecting spatially correlated coincidences, but at the cost of higher shot noise because far fewer events survive. The second is acquisition time. Conventional camera-based covariance imaging needs tens of thousands of frames to pull correlations out of noise; recent work using a kurtosis-difference weighting reports usable results at 5,000 frames and removes the need to pre-calibrate a single correlation centre. The third is loss. Heisenberg scaling in SU(1,1) interferometers is known to be fragile under realistic detection efficiency and loss, which is why recent work concentrates on differential intensity measurements that degrade gracefully rather than on ideal Yurke-type schemes.

A formal comparison of the schemes as multiparameter estimation problems found that ghost imaging and two-photon imaging generally give higher precision for transmission estimation than imaging with undetected photons, though QIUL alone avoids coupling transmission estimates across spatial modes. That result matters for positioning: the case for QIUL is not sensitivity, it is access to wavelengths where good detectors do not exist. Supporting component work is moving in parallel: thin-film lithium niobate sources of polarization-entangled telecom pairs with pump-polarization-tunable Bell states and no extra optics, 30-beam arrays of polarization-squeezed light at 2.03 dB from a single atomic vapour cell, and metasurfaces performing parallel polarization projections across a 400-pixel biphoton field.

## Viability (3/5)

The demonstrations are real and increasingly go beyond test targets. Quantum scanning synthetic optical holography retrieved amplitude and phase images of binary, transparent and biological samples with mid-infrared probing and visible-wavelength detection, and decoupled spatial resolution from the photon-pair spatial correlations that previously limited QIUL. Contrast enhancement through weakly scattering media was predicted by simulation and confirmed experimentally in two illumination configurations. Spatially resolved CHSH tests over 400 pixels were achieved with an average of only 1.7 detected coincidence pairs per pixel per basis, which shows how far statistical and machine-learning post-processing can stretch a thin photon budget.

Against this, the failure modes are structural rather than incidental. Coincidence post-selection buys contrast by discarding events and therefore raises shot noise. Camera-based covariance imaging still needs thousands of frames even with improved estimators. Sub-shot-noise phase estimation loses its ideal scaling under loss and imperfect detection, so practical proposals retreat to more robust intensity-difference readouts. Several of the most striking ideas in this source set, including phase-subtractive interference with two undetected photons and optimal interaction-free localization in multipath interferometers, are theory only. A 3 reflects working hardware with an unresolved advantage argument, not a resolved one.

**TLDR: Working benchtop systems on real samples, but every advantage comes with a photon-budget or loss penalty.**

## Drivers (3/5)

On the supply side, the enabling parts are converging. Photon-pair sources are moving onto fabrication-compatible platforms: thin-film lithium niobate now delivers polarization-entangled telecom pairs with no additional entangling optics and with Bell state selected by pump polarization, using existing lithium niobate process capability. Squeezed-light generation is becoming multiplexed rather than one-beam-at-a-time, with a 30-beam polarization-squeezed array at 2.03 dB from a single vapour cell. Metasurfaces are absorbing measurement complexity that previously required serial projective tests. Statistical methods are cutting acquisition cost.

On the demand side, the sources describe the pull rather than measure it. The clearest articulated need is label-free mid-infrared imaging without mid-infrared detectors, applied to biological samples. Institutional demand is visible but small: an NSF award of $94,177 in August 2026 funds a workshop explicitly convening quantum physicists, biomedical engineers, clinicians and end users because most biomedical quantum sensing work has stayed in ideal lab environments and needs a translation roadmap. That is a candid statement of an unmet translation gap, not evidence of procurement. No customer, revenue or instrument-shipment figures appear anywhere in these sources.

**TLDR: Component supply is improving fast; demand is real in mid-infrared and photosensitive-sample imaging but not yet evidenced by buyers in these sources.**

## Novelty (3/5)

The honest comparison is against classical alternatives for the same task. For rejecting scattered light, the classical baselines are time gating and spatial filtering; the entangled-pair approach substitutes coincidence detection plus post-selection on spatial correlation, which also removes background light, and the paper is explicit that the gain in contrast is paid for in shot noise. For phase imaging, the distinctive claim is that a nonlinear-interferometer scheme can be made immune to uncontrollable interferometer phase fluctuations while still carrying phase information from photons that are never detected, which has no classical analogue. For mid-infrared microscopy, the advantage is architectural: probe in the MIR, detect in the visible, with a route towards diffraction-limited label-free phase imaging.

The sources do not support a claim that quantum imaging is broadly more precise. The multiparameter-estimation comparison places ghost imaging and two-photon imaging above imaging with undetected photons for transmission estimation, with QIUL's distinct benefit being that it does not couple transmission estimation across spatial modes. Meanwhile sub-shot-noise interferometry's headline scaling is described as fragile under realistic loss and detection. Squeezing levels quoted are modest, 2.03 dB in the multiplexed array. Genuinely new physics, quantified advantage still narrow.

**TLDR: Better than classical imaging on capability (probe wavelength, background rejection) more than on sensitivity, and the sources say so explicitly.**

## Diffusion (2/5)

Everything in this source set is a benchtop experiment, a simulation or a theory proposal. The strongest signal about adoption is negative and comes from inside the community: an NSF-funded workshop justified on the grounds that biomedical quantum sensing effort has largely been confined to ideal lab environments and that brainstorming is needed on how to accelerate translation of in-lab quantum sensors to practical deployed systems. That is an accurate description of the state of diffusion.

**TLDR: No deployed systems in the sources, and the field's own funders describe the lab-to-clinic gap as the open problem.**

## Impact (3/5)

If undetected-photon imaging matures, the payoff is specific and plausible: quantitative, label-free phase and amplitude imaging of biological tissue at mid-infrared probe wavelengths using visible-band detectors, which sidesteps the cost and noise of MIR focal-plane arrays. Related niches include imaging photosensitive or scattering samples where background rejection matters more than throughput and beyond-classical birefringence sensing for material structure, stress and composition. There is also a spillover route: the same source and correlation engineering feeds quantum communication and information processing.

The ceiling looks like specialist instrumentation rather than a replacement for mainstream microscopy or machine vision, and the sources give no market size, cost or throughput comparison against incumbent MIR spectroscopic imaging. The metrology analysis further suggests different quantum schemes will win different narrow tasks rather than one architecture dominating. A 3 marks a credible, bounded impact; the sources do not permit a higher claim.

**TLDR: A real new capability in mid-infrared and low-flux imaging, but the sources contain no quantification of the value at stake.**

## Timing Soon (2-5yr)

The 2026 literature marks a transition from proof-of-principle on test targets to imaging of transparent and biological samples with complex-field reconstruction, alongside estimator improvements that cut frame counts and source integration onto a manufacturable platform. Those are the ingredients of a first commercial research-grade instrument in the mid-infrared niche, not of a general imaging technology.

The rate-limiting step is translational rather than scientific, and the community has just started organising for it as of August 2026. Sub-shot-noise imaging specifically should be treated as later and less certain, given that its ideal scaling advantage is explicitly fragile under loss and that available multiplexed squeezing is at 2.03 dB.

**TLDR: Research instruments and first specialist mid-infrared microscopes are plausible within five years; broad imaging use is not in view.**

## Overrated or underrated? Fairly rated

The field is neither hype nor breakthrough: it is a set of narrow, physically sound capabilities being pushed towards instruments. The part usually oversold is the sensitivity story. The sources themselves say Heisenberg scaling in nonlinear interferometers is fragile under realistic loss and detection, that quantum contrast gains cost shot noise, and that undetected-photon imaging is generally less precise than ghost or two-photon imaging for transmission estimation. Anyone pitching quantum imaging as beating the classical limit in general should be asked which task, at what loss, in how many frames.

The part that deserves more attention is the wavelength-conversion architecture. Probing a biological sample in the mid-infrared while detecting visible photons, with amplitude and phase recovered and resolution no longer tied to photon-pair correlations, is a capability with no classical equivalent at comparable detector cost. That, plus manufacturable pair sources on thin-film lithium niobate, is where the commercial case will be won or lost. Judge the field on acquisition time per image against a classical MIR alternative, not on decibels of squeezing.

## Prediction

By 31 December 2029, quantum imaging with undetected light will have produced at least one commercially catalogued research-grade mid-infrared microscope, while no entangled-photon or sub-shot-noise imaging system will be in routine clinical use.

## Evidence base

- 20 July 2026: scanning synthetic optical holography implemented inside quantum imaging with undetected light retrieved amplitude and phase images of binary, transparent and biological samples, probing with mid-infrared photons while detecting only visible partners, and decoupled resolution from photon-pair spatial correlations.
- 27 July 2026: a quantum Fisher information analysis found ghost imaging and two-photon imaging generally more precise than imaging with undetected photons for transmission estimation, with QIUL uniquely avoiding coupling between spatial modes.
- 29 May 2026: spatially entangled photon pairs with correlation post-selection improved image contrast through weakly scattering media in simulation and experiment, at the cost of higher shot noise from fewer surviving events.
- 1 July 2026: conventional camera covariance quantum imaging is stated to need tens of thousands of frames; a kurtosis-difference weighted covariance method reports results at 5,000 frames without pre-calibrating a correlation centre.
- 4 August 2026: comparison of Yurke SU(1,1), Mandel induced-coherence and hybrid interferometers concludes that ideal Heisenberg scaling is fragile under realistic detection constraints and loss, favouring intensity-based differential measurements.
- 4 August 2026: NSF awarded $94,177 for a Quantum Imaging and Quantum Sensing workshop, noting that most biomedical quantum sensing work has been in ideal lab environments and that a translation roadmap is needed.

## Open questions

- At fixed total acquisition time and identical illumination at the sample, does coincidence-based contrast enhancement beat classical time gating or spatial filtering, or does the shot-noise penalty cancel the gain?
- How does scanning QIUL phase imaging compare with conventional mid-infrared spectroscopic imaging on time per field of view, sensitivity and instrument cost?
- Can integrated thin-film lithium niobate pair sources deliver enough brightness and spatial-mode quality to replace bulk SPDC crystals inside an imaging instrument?
- Do sub-shot-noise imaging schemes retain a measurable advantage at the detection efficiencies and squeezing levels actually available, given the reported fragility to loss and the 2.03 dB figure from multiplexed sources?

---
*Assessment drafted 2026-08-31 from up to 13 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
