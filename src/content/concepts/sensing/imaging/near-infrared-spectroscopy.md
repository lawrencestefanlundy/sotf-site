---
type: concept
slug: near-infrared-spectroscopy
canonical_name: Near-infrared spectroscopy (NIR)
aliases: []
related_concepts:
- spectral-sensing
- spectral-imaging-sensing
last_updated: '2026-08-31'
tags:
- concept
sources: []
mention_count: 7
frontier:
- Does fNIRS cross-subject classification performance improve materially beyond AUC ~0.76 in larger, multi-site, prospectively validated cohorts, or is that near the ceiling imposed by between-subject haemodynamic variability?
- Why did only 13 of 25 patients achieve an analysable pharmacological block, and is the attrition a property of the anaesthesia protocol or of the fNIRS measurement?
- Does the high agreement between depolarisation-sensitive OFDI and NIRS LCBI hold in larger cohorts and at the lesion-level decision thresholds used clinically, which would make a separate NIRS catheter redundant?
- Do the group-level fNIRS differences reported across anxiety-spectrum and impulsivity cohorts survive out-of-sample subject-level testing, or do they follow the same inflation pattern the analgesia study warns about?
- Do temporal HRF shape features outperform GLM amplitude in leave-one-subject-out designs on independent cohorts, and by how much does accuracy drop relative to within-session cross-validation 2026 05 28 medrxiv personalized brain based analgesia detection w?
- What is the quantitative agreement (limits of agreement, per-lesion concordance) between depOFDI lipid metrics and NIRS-derived LCBI in cohorts larger than 29 pullbacks, and does either predict clinical events better 2026 06 01 medrxiv assessing lipid core burden index with depolar?
- Can fNIRS-derived connectivity and graph metrics discriminate anxiety-spectrum subgroups at individual-patient level with prospectively validated thresholds, rather than group-level contrasts 2026 06 12 medrxiv neurovascular instability impaired cortical re?
- How do fNIRS haemodynamic readouts co-register with MRS-derived metabolic measures in the same subjects, and does the optical signal add information beyond what high-field MRS already provides 2026 07 29 medrxiv assessment of glucose metabolism in vivo in th?
scorecard:
  viability: 4
  drivers: 3
  novelty: 2
  diffusion: 4
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
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
**Near-infrared spectroscopy uses light in the ~700-2500 nm window, where tissue and organic matter are relatively transparent, to read chemical composition and haemodynamics without contact or contrast, and it is already a working clinical and agricultural instrument rather than a laboratory prospect.**

## Summary

Near-infrared light penetrates several centimetres into biological material because water, haemoglobin and lipids absorb it comparatively weakly there. Two consequences follow, and they drive almost every application in the sources. First, molecular overtone and combination bands in the NIR give a chemical fingerprint, so reflected or transmitted spectra can be calibrated against protein, starch, fat, ash or lipid content. Second, oxygenated and deoxygenated haemoglobin have different NIR absorption spectra, so light shone through the scalp and returned to a nearby detector reports cortical blood oxygenation, which is the basis of functional NIRS (fNIRS).

The compositional branch appears here in two forms. In coronary intervention, NIRS-derived lipid core burden index (LCBI) is described as well validated and widely used for detecting lipid-rich, rupture-prone plaque, and is used as the reference against which a new depolarisation-sensitive optical frequency domain imaging metric is benchmarked in 29 co-registered pullbacks from 33 patients. In plant breeding, NIR is the routine assay for macronutrient traits: protein, starch, fat and ash were measured by NIR on mature grain across a USDA lima bean germplasm panel of 810 genotyped accessions with 141-308 accessions field-evaluated across three sites.

The functional branch is where the technology is least settled. Portable 36-channel fNIRS has been used to detect pharmacologically verified dental nerve block, with temporal haemodynamic response features outperforming raw GLM amplitude and leave-one-subject-out classification reaching AUC 0.68-0.76. Multichannel fNIRS separates anxiety-spectrum patient groups from controls on task-evoked HbO and HbT responses during verbal fluency, indexes prefrontal haemodynamics in impulsivity research, and can be run concurrently with single-pulse TMS across the whole head. A third, unrelated use is NIR as an energy delivery channel: remote, non-invasive NIR laser stimulation actuates an implanted antibacterial surface in a mouse model.

The parameters that decide any given NIR application are penetration depth versus the depth of the target, the strength and specificity of the chemical contrast at the wavelengths used, and whether a stable calibration transfers across samples or subjects. The last of these is the binding constraint for fNIRS: between-subject variability of the haemodynamic response is explicitly identified as the reason classifiers fail to generalise, and within-session cross-validation is identified as a source of inflated accuracy.

## Viability (4/5)

For compositional measurement the sources treat NIR as settled infrastructure rather than an experiment. NIRS-derived LCBI is characterised as well validated and widely used in coronary imaging and is used as the comparator for a challenger modality, and NIR is used without comment as the assay for protein, starch, fat and ash across a multi-environment germplasm evaluation. That is the profile of a technique whose viability is no longer in question in those niches.

Functional NIRS is viable as a measurement but not yet as a decision instrument. Portable 36-channel fNIRS detected an analgesia effect with interaction effect sizes d = 0.63-0.79 for engineered temporal features against d = 0.56 for raw GLM amplitude, and a difference-in-differences interaction at p = 0.011, but only 13 of 25 patients achieved a successful block and cross-subject classification reached AUC 0.68-0.76 (best random forest 0.760, permutation p = 0.002). Those are above chance and honestly evaluated, and they are far from clinical-grade discrimination. The same study names the two failure modes candidly: between-subject variability and optimistic within-session validation designs.

**TLDR: The physics and the instruments work; what varies by application is whether calibration transfers.**

## Drivers (3/5)

On supply, the distinguishing features are portability and benignity. The pain study used a portable 36-channel bilateral system at the chairside during a dental procedure, and whole-head fNIRS was run concurrently with TMS, which is difficult with competing modalities. In agriculture, NIR is fast and non-destructive enough to phenotype macronutrients across hundreds of accessions and multiple environments.

On demand, the clearest pull is compositional: lipid quantification is described as central to identifying rupture-prone plaque and as a therapeutic target for lipid-lowering therapy, which is an ongoing clinical need. The neuro applications are pulled by unmet measurement needs (objective analgesia verification, mechanistic accounts of anxiety-spectrum neurovascular coupling) rather than by demonstrated willingness to pay. The sources contain no market sizing, funding or procurement data, so this score reflects only the technical and clinical rationale visible in the literature.

**TLDR: Supply side is cheap, portable and non-ionising; demand is real but the sources show research pull more than procurement pull.**

## Novelty (2/5)

Nothing in the sources presents NIR itself as new. In coronary imaging it is the established reference: a depolarisation-sensitive OFDI lipid metric was developed and shown to correlate highly with NIRS maxLCBI4mm across 29 pullbacks, with the explicit motivation of folding compositional assessment into an OFDI platform already adopted for PCI guidance. That is displacement pressure on NIRS, not novelty for it. In plant phenotyping, NIR is a background tool.

Where novelty exists it is in the analysis layer and in the deployment context rather than the optics. The advance in the analgesia work is feature engineering plus honest leave-one-subject-out validation, which recovered a modest but genuine cross-subject signal where amplitude-only GLM features did worse. Using NIR as a remote actuation channel for an implanted antibacterial surface is a different kind of novelty, but there the light is an energy delivery mechanism, not a spectroscopic measurement.

**TLDR: NIR is the incumbent, not the challenger; in one flagship clinical use it is the thing being competed against.**

## Diffusion (4/5)

Two of the applications here are past the adoption question. NIRS-IVUS was acquired alongside polarisation-sensitive OFDI in a consecutive PCI cohort, and NIRS-LCBI is described as widely used; NIR macronutrient measurement is standard enough to appear as a method line in a large germplasm characterisation. fNIRS is clearly diffused within neuroscience research, appearing across pain, psychiatry, criminology and TMS-combination studies.

The barriers are specific to each branch. For clinical fNIRS the barrier is generalisation: per-patient calibration was required to get usable performance, and half the enrolled cohort did not yield an analysable block. For catheter NIRS the barrier is platform consolidation. If a single OFDI catheter can deliver both high-resolution structure and a validated lipid metric, the incremental case for carrying a separate NIRS-IVUS system weakens, and the 33-patient agreement study is a first step in that direction.

**TLDR: Already routine in interventional cardiology and grain phenotyping; fNIRS is diffused across research but not into clinical decisions.**

## Impact (3/5)

The ceiling is set by two things. Depth and specificity limit fNIRS to cortical haemodynamics, which is why the psychiatric findings are group-level mechanistic descriptions rather than individual diagnostics. And where a competing modality can supply the same contrast alongside richer information, NIR's marginal contribution shrinks. The sources do not contain economic or outcome data, so this is a judgement on clinical and scientific leverage, not on quantified value.

**TLDR: High value where it is already embedded, but in each case it is one input among several rather than the deciding technology.**

## Timing Now (0-2yr)

For lipid core assessment in the cath lab and macronutrient phenotyping in breeding programmes, the technology is deployed now and the live question is competitive substitution rather than maturation.

The frontier that has a timeline attached is single-subject fNIRS classification. The strongest result here is cross-subject AUC 0.68-0.76 with per-patient calibration in a 13-patient analysable subgroup. Moving from that to a prospectively validated clinical readout requires larger multi-site cohorts and demonstrated robustness to the between-subject variability the authors identify, which is a multi-year programme. NIR as an actuation channel for implants is at mouse-model stage.

**TLDR: Compositional NIR is in routine use today; individual-level fNIRS decoding is a 2-5 year question at best.**

## Overrated or underrated? Fairly rated

NIR is a mature, well-understood workhorse whose position the sources neither inflate nor undermine. It is priced correctly as infrastructure: cheap, portable, non-ionising, chemically specific enough for lipid and macronutrient quantification, and depth-limited enough that it will not replace tomographic or magnetic-resonance methods. The honest reading of the coronary evidence is that NIRS currently holds the validated-reference position and is being probed for substitution by a platform that already has structural imaging in the catheter.

The part that could be mispriced in either direction is portable fNIRS as an individual-level clinical readout. The analgesia study is the right kind of evidence because it discloses the failure modes rather than hiding them, and its AUC of 0.68-0.76 under leave-one-subject-out validation is a realistic baseline against which enthusiastic within-session numbers elsewhere should be discounted. Anyone underwriting an fNIRS diagnostic should assume per-subject calibration is mandatory and that a substantial fraction of sessions will be unusable.

## Prediction

By 31 December 2028, at least one OFDI-based intravascular platform will report a lipid metric validated against NIRS-derived maxLCBI4mm in a cohort of more than 100 patients, extending the 29-pullback agreement shown in 2026.

## Evidence base

- 2026-05-28: Portable 36-channel fNIRS during verified dental nerve block gave leave-one-subject-out AUC 0.68-0.76 (best random forest 0.760, permutation p = 0.002) with per-patient calibration, in 13 block-success patients of 25 enrolled.
- 2026-05-28: Engineered temporal HRF features (late slope, mean first derivative, baseline-normalised amplitude) showed analgesia interaction effects d = 0.63-0.79 versus d = 0.56 for raw GLM amplitude, with a difference-in-differences interaction at p = 0.011.
- 2026-06-01: NIRS-derived LCBI is described as well validated and widely used for detecting lipid-rich coronary lesions; a depolarisation-sensitive OFDI metric showed high correlation with NIRS maxLCBI4mm across 29 co-registered pullbacks from 33 patients.
- 2026-06-06: NIR spectroscopy was used to measure protein, starch, fat and ash on mature grain in a USDA lima bean germplasm study covering 810 genotyped accessions and 141-308 field-evaluated accessions across three sites.
- 2026-06-12: Multichannel fNIRS during verbal fluency showed reduced task-evoked HbO and HbT, preserved HbR, increased temporal haemodynamic variability and reduced beta activation in anxiety-spectrum patients versus controls, concentrated in frontopolar and medial prefrontal cortex.
- 2026-07-24: Whole-head fNIRS was run concurrently with single-pulse TMS to the left DLPFC during a working memory task, showing load-dependent haemodynamic increases and TMS-driven modulation across DLPFC, superior medial gyrus, precuneus and parietal lobule.
- 2026-07-01: Remote, non-invasive near-infrared laser stimulation actuated an implanted bactericidal wrinkled MXene surface, which suppressed bacterial burden in a mouse subcutaneous implant infection model.

## Open questions

- Does fNIRS cross-subject classification performance improve materially beyond AUC ~0.76 in larger, multi-site, prospectively validated cohorts, or is that near the ceiling imposed by between-subject haemodynamic variability?
- Why did only 13 of 25 patients achieve an analysable pharmacological block, and is the attrition a property of the anaesthesia protocol or of the fNIRS measurement?
- Does the high agreement between depolarisation-sensitive OFDI and NIRS LCBI hold in larger cohorts and at the lesion-level decision thresholds used clinically, which would make a separate NIRS catheter redundant?
- Do the group-level fNIRS differences reported across anxiety-spectrum and impulsivity cohorts survive out-of-sample subject-level testing, or do they follow the same inflation pattern the analgesia study warns about?

---
*Assessment drafted 2026-08-31 from up to 14 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
