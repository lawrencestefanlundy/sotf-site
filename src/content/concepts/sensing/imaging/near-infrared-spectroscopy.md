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
- Do temporal HRF shape features outperform GLM amplitude in leave-one-subject-out designs on independent cohorts, and by how much does accuracy drop relative to within-session cross-validation 2026 05 28 medrxiv personalized brain based analgesia detection w?
- What is the quantitative agreement (limits of agreement, per-lesion concordance) between depOFDI lipid metrics and NIRS-derived LCBI in cohorts larger than 29 pullbacks, and does either predict clinical events better 2026 06 01 medrxiv assessing lipid core burden index with depolar?
- Can fNIRS-derived connectivity and graph metrics discriminate anxiety-spectrum subgroups at individual-patient level with prospectively validated thresholds, rather than group-level contrasts 2026 06 12 medrxiv neurovascular instability impaired cortical re?
- How do fNIRS haemodynamic readouts co-register with MRS-derived metabolic measures in the same subjects, and does the optical signal add information beyond what high-field MRS already provides 2026 07 29 medrxiv assessment of glucose metabolism in vivo in th?
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

Near-infrared spectroscopy exploits the relative transparency of biological tissue to near-infrared light and the wavelength-dependent absorption of specific chromophores within it. In the functional neuroimaging variant (fNIRS), light is coupled into the scalp and detected a few centimetres away after diffuse propagation through cortex; changes in attenuation are converted into concentration changes for oxygenated haemoglobin (HbO), deoxygenated haemoglobin (HbR) and total haemoglobin (HbT), which together index cortical haemodynamics and neurovascular coupling medrxiv neurovascular instability impaired cortical re. Source-detector pairs are multiplexed into channel arrays: reported configurations include 36-channel bilateral montages over a target region medrxiv personalized brain based analgesia detection w and whole-head coverage medrxiv the effect of single pulse tms on working memo.

The measured quantity is a slow haemodynamic response, so analysis is dominated by modelling of the haemodynamic response function (HRF). Standard practice fits a general linear model (GLM) to obtain a response amplitude, but temporal shape descriptors carry additional information: late slope, mean first derivative and baseline-normalised amplitude showed larger effect sizes for detecting pharmacological analgesia (d = 0.63-0.79) than raw GLM amplitude (d = 0.56) medrxiv personalized brain based analgesia detection w. Other extracted features include peak response, temporal haemodynamic variability and beta activation, plus channel-to-channel functional connectivity and graph-theoretical network measures medrxiv neurovascular instability impaired cortical re. Because the technique is optical and non-ionising, it tolerates concurrent electromagnetic stimulation, enabling online recording during single-pulse transcranial magnetic stimulation medrxiv the effect of single pulse tms on working memo.

A separate application uses catheter-based NIRS to infer tissue composition rather than blood oxygenation. In coronary imaging, NIRS yields a lipid core burden index (LCBI) that is described as well validated and widely used for detecting lipid-rich, rupture-prone plaque, and is used as a readout for lipid-lowering therapy medrxiv assessing lipid core burden index with depolar. Here the spectroscopic signal provides chemical contrast without structural resolution, which is why it is deployed in combined NIRS-intravascular ultrasound catheters medrxiv assessing lipid core burden index with depolar.

Key practical parameters across both modalities are channel count and spatial coverage, portability, sensitivity to the haemodynamic (rather than neuronal or metabolic) variable, and generalisation of derived features across subjects. Between-subject variability is explicitly identified as a barrier to classifiers built on fNIRS features, and within-session cross-validation is identified as a design that inflates reported accuracy by conflating within- and between-person variance medrxiv personalized brain based analgesia detection w.

## Competitive landscape

For brain measurement, NIRS sits against magnetic resonance spectroscopy and diffusion MRI, which resolve metabolites and microstructure rather than haemoglobin: whole-brain 7T 3D-CRT-FID-MRSI maps regional NAA, glutamate and glutamine ratios medrxiv glutamine and naa dissociate in als across som, interleaved 1H/13C MRS at 7T quantifies glucose uptake and TCA cycle flux medrxiv assessment of glucose metabolism in vivo in th, and diffusion-weighted MRI combined with DW-MRS probes intracellular and extracellular tumour compartments medrxiv combined diffusion mri and mr spectroscopy pro. These require fixed high-field scanners; the fNIRS work reported here is described as portable and compatible with bedside or chairside protocols in dental patients medrxiv personalized brain based analgesia detection w.

For intravascular plaque composition, the direct competitor is depolarisation-sensitive optical frequency domain imaging (depOFDI), which provides intrinsic lipid contrast alongside high-resolution structural imaging in a single OFDI platform, and was benchmarked against NIRS-derived LCBI in 29 co-registered pullbacks from 33 patients medrxiv assessing lipid core burden index with depolar. The framing in that work is that NIRS is the validated reference standard for lipid burden, while OFDI-based metrics aim to consolidate structure and composition into one acquisition medrxiv assessing lipid core burden index with depolar.

## Evidence base

- Portable 36-channel bilateral fNIRS in 25 patients with clinically painful teeth, with 13 block-success patients analysed, identified temporal HRF features (late slope, mean first derivative, baseline-normalised amplitude) with analgesia interaction effect sizes d = 0.63-0.79 versus d = 0.56 for raw GLM amplitude (2026-05-28) medrxiv personalized brain based analgesia detection w.
- The same work states that between-subject variability prevents pain classifiers from generalising and that within-session cross-validation inflates reported accuracy (2026-05-28) medrxiv personalized brain based analgesia detection w.
- NIRS-derived LCBI is described as well validated and widely used for lipid-rich lesion detection; 33 patients underwent both polarisation-sensitive OFDI and NIRS-intravascular ultrasound during PCI, with 29 co-registered pullbacks analysed after four exclusions (2026-06-01) medrxiv assessing lipid core burden index with depolar.
- Multichannel fNIRS during a verbal fluency task was used to compare healthy controls, generalised anxiety disorder, anxious depression and anxiety-depression comorbidity, extracting peak response, temporal haemodynamic variability, beta activation and HbO/HbR/HbT signals, plus connectivity, graph metrics and machine-learning classification (2026-06-12) medrxiv neurovascular instability impaired cortical re.
- Concurrent whole-head fNIRS with single-pulse TMS to left DLPFC showed a reliable load-dependent increase in haemodynamic activity during a working memory task, while behavioural responses to TMS varied (2026-07-24) medrxiv the effect of single pulse tms on working memo.

## Frontier (open questions)

- Do temporal HRF shape features outperform GLM amplitude in leave-one-subject-out designs on independent cohorts, and by how much does accuracy drop relative to within-session cross-validation medrxiv personalized brain based analgesia detection w?
- What is the quantitative agreement (limits of agreement, per-lesion concordance) between depOFDI lipid metrics and NIRS-derived LCBI in cohorts larger than 29 pullbacks, and does either predict clinical events better medrxiv assessing lipid core burden index with depolar?
- Can fNIRS-derived connectivity and graph metrics discriminate anxiety-spectrum subgroups at individual-patient level with prospectively validated thresholds, rather than group-level contrasts medrxiv neurovascular instability impaired cortical re?
- How do fNIRS haemodynamic readouts co-register with MRS-derived metabolic measures in the same subjects, and does the optical signal add information beyond what high-field MRS already provides medrxiv assessment of glucose metabolism in vivo in th?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
