---
type: concept
slug: diagnostics
canonical_name: Diagnostics
aliases: []
kind: category
parent_concepts:
- life-frontier
- diagnostics-health
related_concepts: []
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2023-07-14-e08-optical-computing]]'
scorecard:
  viability: 3
  drivers: 3
  novelty: 4
  diffusion: 2
  impact: null
  timing_band: Soon (2-5yr)
  verdict: Too early to say
scorecard_status: draft
mention_count: 113
sources_7d: 3
sources_30d: 20
recent_mentions:
- slug: 2026-08-03-spad-single-photon-market-scan
  title: SPAD / single-photon detector market scan — incumbent structure and company cohort
  date: '2026-08-03'
  kind: web
- slug: 2026-06-04-asg-biosensor-host-cell-protein-bioprocess
  title: Startup's biosensor makes drug development and manufacturing cheaper (MIT News — Advanced Silicon Group)
  date: '2026-06-04'
  kind: web
- slug: 2026-03-18-bacteria-reveal-themselves-through-unique-sounds-a-breakthro
  title: 'Bacteria reveal themselves through unique sounds: a breakthrough for rapid diagnostics - TU Delft'
  date: '2026-03-18'
  kind: web
- slug: 2026-02-16-chip-scale-bio-instrumentation-lex-diagnostics-receives-fda
  title: LEX Diagnostics Receives FDA 510(k) Clearance and CLIA Waiver for LEX VELO System
  date: '2026-02-16'
  kind: web
- slug: 2026-01-13-chip-scale-bio-instrumentation-point-of-care-diagnostics
  title: Point-of-Care Diagnostics Market Analysis including CE-IVD POC cardiac biomarkers
  date: '2026-01-13'
  kind: web
- slug: 2024-11-05-confidential-ai-the-dog-that-didnt
  title: Confidential AI
  date: '2024-11-05'
  kind: substack
- slug: 2023-07-14-e08-optical-computing
  title: '🔮E08: Optical Computing'
  date: '2023-07-14'
  kind: substack
- slug: 2015-12-14-darpa-sbir-injectable-diagnostics-chemical-sensors-synthetic
  title: 'DARPA SBIR: Injectable Diagnostics, Chemical Sensors, Synthetic Biology - Global Biodefense'
  date: '2015-12-14'
  kind: web
neighbors: []
---
**"Diagnostics" here is not one technology but a measurement layer that has recently been rebuilt around nonlinear frequency conversion, single-photon silicon detection and machine-learning reconstruction, with strong benchtop results in physics instrumentation and only early, pre-clinical evidence on the health side.**

## Summary

A diagnostic is an instrument plus an inference chain: you couple to a system you cannot disturb much, record a signal that is noisy, incomplete or indirect, and reconstruct the quantity you actually wanted. The sources grouped under this concept span four very different systems being probed: living cells, gas mixtures and combustion, particle beams and thin-film growth, and quantum devices. What unites them is that the recent progress is in the reconstruction and detection layer rather than in new physical contrast mechanisms.

Three recurring building blocks show up. First, nonlinear upconversion: mid-infrared light, where molecular vibrational bonds give chemical specificity but detectors are poor, is optically mixed up to visible wavelengths so that cheap, room-temperature silicon single-photon avalanche diodes can be used. This underpins hyperspectral single-photon imaging demonstrated across 2.9 to 3.6 micrometres on egg yolk, yeast, polystyrene and polyethylene, a 3 micrometre edge-enhancement differentiator switching between first and fourth order at up to 60 Hz, and high-speed MIR videography where a nonlinear crystal is gated by time-multiplexed pump patterns and the frames are computationally unpicked from a single camera exposure. Second, learned signal separation: deep denoising autoencoders, an unsupervised interference-mitigation framework and blind source separation applied to laser absorption spectroscopy so that species can be resolved without complete reference spectra, and unsupervised embedding of RHEED patterns to separate high- from low-quality epitaxial films in situ. Third, estimator engineering, where the diagnostic quantity is redefined to be cheaper or less invasive to compute: subcubic online updates of partial-transpose moments from classical shadows, and a Bayesian-network reconstruction of a qubit Otto engine cycle that avoids the projective dephasing imposed by two-point energy measurement.

A caution about scope. The taxonomy places this under health, but the supplied evidence is overwhelmingly instrumentation physics with biomedical use cited as motivation rather than demonstrated. Nothing here is a clinical assay, and no source reports patient data, sensitivity or specificity against a clinical standard.

## Viability (3/5)

The physical demonstrations are real and quantified. A label-free microscope images intracellular viscoelasticity at biologically relevant frequencies, twenty times faster than previous label-free approaches and at diffraction-limited resolution, revealing features earlier methods could not reach. A silicon photonic integrated circuit speckle spectrometer reaches a stated record resolution of 100 MHz, or 0.8 pm at 1550 nm, as the front end of a 10 MHz-resolution RF spectrum analyser. A coherent transition radiation retrieval algorithm reconstructs modulated electron bunch trains and outperforms the Kramers-Kronig method on multi-Gaussian and coherent-harmonic-generation test cases.

What is missing is everything after the first instrument. Biological validation is on egg yolk, yeast and polymer films, reconstruction algorithms are tested on synthetic or model bunch trains, and the biosensor result is a model validated against finite-element simulation rather than against measured assays. The quantum-side diagnostics are honest about their own fragility: surface-code threshold estimates are shown to depend materially on the decoder and estimator chosen, with matching-style backends giving a crossing median of 0.0531 while Union-Find shows higher logical error rates and matching-fallback rates up to 0.747 at high noise. That is a warning that the diagnostic number can be an artefact of the inference pipeline. A 3, not higher, because reproducibility across labs, samples and operators is untested in these sources.

**TLDR: Benchtop demonstrations with hard numbers across several modalities, but nothing beyond model samples and single instruments.**

## Drivers (3/5)

On supply, the enabling shift is explicit. MIR single-photon imaging adoption is described as hindered by the absence of efficient room-temperature MIR detectors, and the fix is to upconvert into the visible so that cost-effective silicon SPADs do the detection at room temperature with low noise. The same logic recurs with a single-photon-sensitive silicon camera enabling high-contrast edge imaging under low light at 3 micrometres and with frame rates lifted past readout-electronics limits by optical multiplexing onto one silicon camera exposure. The second supply driver is cheap inference: machine learning removes the calibration burden that previously gated spectroscopy in messy environments, including recovering concentrations and spectral signatures when reference spectra are unavailable at all. A third is autonomous process control, where in situ RHEED plus unsupervised learning is proposed to cut manual tuning in molecular beam epitaxy.

On demand, the sources list application domains rather than evidence of pull: biomedical diagnostics, material inspection and remote sensing; combustion diagnostics, explosion reactions, photosynthetic tracking and thermal surveillance; chemical analysis, medical diagnostics and quantum sensing. There are no procurement figures, market sizes, customers or funding data anywhere in this set, so the demand half of the score is unsupported and I have kept it at a middling 3 on the strength of the supply argument alone.

**TLDR: Supply-side pull from commodity silicon detectors and learned reconstruction is well evidenced; demand is asserted, never measured.**

## Novelty (4/5)

Two items are novel in kind rather than degree. The coherence-preserving fluctuation diagnostic sidesteps the projective dephasing that two-point energy measurement forces on a quantum engine, reconstructing the unmeasured coherent cycle via a dynamic Bayesian network, and is careful to label its gains as gross working-medium advantages rather than net device efficiencies. The entangling-power diagnostic introduces concurrence- and negativity-based measures that, unlike a previously proposed linear-entropy quantity, vanish for all separable channels, which is a correctness fix in the metric itself.

**TLDR: Most entries state what they beat and by how much, and the margins are large rather than marginal.**

## Diffusion (2/5)

One genuine diffusion argument exists: pushing detection onto commodity silicon rather than exotic infrared arrays lowers cost and removes cryogenics, which is exactly the barrier named as blocking MIR single-photon imaging today, and putting a high-resolution spectrometer on a silicon photonic integrated circuit points at a manufacturable form factor. Against that, the same systems rely on nonlinear crystals, pulsed pump sources and phase-only spatial light modulators, and on computational deciphering steps whose robustness outside the demonstrated scenes is not established.

The learned-reconstruction layer carries its own adoption tax. Autoencoder-based blind source separation and unsupervised interference mitigation are attractive precisely because reference data are missing, which is also what makes them hard to certify for a regulated or safety-critical use. The surface-code work shows the general failure mode in a setting where ground truth is well defined: change the decoder and the reported threshold moves, and some estimates remain estimator-sensitive. Nothing in this source set addresses clinical validation, approval pathways, reimbursement, interoperability or field ruggedisation, so the score reflects demonstrated prototypes with no evidence of a route to volume.

**TLDR: Every result is a single instrument in a single lab; the sources contain no cost, manufacturing, standards or regulatory evidence.**

## Impact (unscored)

Every source states a capability and, at most, a list of fields that might use it. None quantifies what the capability is worth. The nearest approaches are indirect: reducing manual tuning in molecular beam epitaxy implies a throughput gain but none is measured; a hundredfold faster biosensor model implies cheaper design iteration but no design win is reported; access to previously inaccessible viscoelastic features implies biological insight but no biological or clinical finding is claimed.

There is a structural case that diagnostics are high leverage, because they gate what you can control: you cannot close a loop on epitaxial film quality, on a fusion-relevant or combustion process, on an accelerator bunch profile, or on quantum error correction without first measuring it. That case is plausible and is implicit in several abstracts, but it is not evidenced here, and assigning a number to it would be inventing one.

**TLDR: The sources do not support an assessment: no value, cost saving or outcome is quantified anywhere.**

## Timing Soon (2-5yr)

Split the concept. The quantum and process diagnostics are already operational inputs to other work: PT-moment estimation is framed as an online, fixed-memory routine consumed by entanglement certification and phase diagnostics, decoder-dependence analysis is being applied to threshold estimation pipelines today, and RHEED-plus-machine-learning is presented as an in situ diagnostic within a growth run. Those are now, in laboratories.

The optical instruments sit a step behind. Upconversion imaging, hyperspectral single-photon imaging and PIC spectrometers are complete working systems with quantified performance, so a two to five year window to reach specialist industrial and research instrument products is consistent with the evidence. Clinical or point-of-care diagnostics are a different clock entirely: the only health-specific contribution here is a design model for affinity biosensors, and no source describes an assay, a cohort or a validation study, so no timing claim for health diagnostics can be made from this base.

**TLDR: The instrumentation and estimator work is usable in research settings now; anything health-facing is not close in these sources.**

## Overrated or underrated? Too early to say

Judged as a health-diagnostics thesis, which is where the taxonomy puts it, this is too early to call. The source set is dominated by physics instrumentation that names biomedical application as motivation and then demonstrates on yeast, egg yolk and polymer films or on cultured cells. There is no clinical evidence, no comparison against an existing assay, and no regulatory signal at all. Anyone pricing this as a near-term diagnostics play is pricing an inference, not a result.

Judged as an instrumentation trend, the picture is more favourable and slightly underappreciated. The recurring move of converting a hard detection problem into a cheap silicon detection problem, then paying the difference in computation, is showing up independently across mid-infrared imaging, chip-scale spectrometry, spectroscopy and beam diagnostics, and it comes with quantified margins rather than qualitative claims. The counterweight, made by the sources themselves, is that once reconstruction carries the load, the reported number becomes a property of the inference pipeline as much as of the physical system. Cross-pipeline agreement, not another single-lab record, is the evidence that would settle this.

## Prediction

By 30 June 2028, mid-infrared upconversion hyperspectral imaging of the kind demonstrated on egg yolk and yeast across 2.9 to 3.6 micrometres will still have no published validation on human clinical samples against an established diagnostic standard.

## Evidence base

- 14 May 2026: a label-free microscope images intracellular viscoelasticity at biologically relevant frequencies, twenty times faster than previous label-free approaches and at diffraction-limited resolution, without a perturbing localised probe.
- 5 June 2026: cavity-enhanced SPDC plus frequency upconversion enables chemically specific single-photon hyperspectral imaging from 2.9 to 3.6 micrometres using room-temperature silicon SPADs, demonstrated on egg yolk, yeast, polystyrene and polyethylene.
- 5 May 2026: a two-compartment biosensor model reproduces finite-element binding kinetics with more than a 100-fold reduction in computation time and yields analytical equilibration time and required volume as functions of the Damkoehler number.
- 7 June 2026: a silicon PIC speckle spectrometer using a path-mismatched multimode interferometer reaches a stated record 100 MHz resolution, 0.8 pm at 1550 nm, within a 10 MHz-resolution RF spectrum analyser.
- 5 June 2026: surface-code threshold estimates shift with the decoder, with a matching-style backend giving crossing median p_c = 0.0531 (bootstrap [0.0415, 0.0572]) and Union-Find showing matching-fallback rates up to 0.747 at sigma = 0.50, showing diagnostic outputs can be pipeline artefacts.
- 28 May 2026: a non-chiral, non-resonant silicon grating produces broadband tunable chiral Smith-Purcell radiation with a stated record degree of polarisation of 0.87, proposed for integrated particle diagnostics platforms.

## Open questions

- Do the learned reconstruction methods for laser absorption spectroscopy hold up on species and interferents absent from their training and augmentation sets, given that their selling point is operating without complete reference data?
- Does the sample-volume framework predict measured performance of real affinity biosensors, rather than only matching finite-element simulation?
- How much of the reported advantage in each optical system survives removal of the spatial light modulator, pulsed pump and free-space alignment, that is, in a packaged instrument rather than a bench?
- For diagnostics whose output depends on the inference pipeline, do independent decoders, estimators or reconstruction algorithms agree on the same physical quantity, as the surface-code comparison suggests they may not?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
