---
type: concept
slug: inspection
canonical_name: Inspection
aliases: []
parent_concepts:
- equipment-processes
- manufacturing
related_concepts: []
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-11-12-atomic-energy-can-nuclear-power-our]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2025-intelmarketresearch-compound-semi-inspection-rejected]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-05-29-nasas-roman-space-telescope-primary-mirror-gets-last-look]]'
- '[[2026-07-26-unitree-ipo-shipment-and-segment-data]]'
- '[[2026-07-09-munichs-quantumdiamonds-raises-91-million-to-scale-its-quant]]'
scorecard:
  viability: 3
  drivers: 3
  novelty: 4
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 88
sources_7d: 0
sources_30d: 16
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-26-unitree-ipo-shipment-and-segment-data
  title: 'Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-09-munichs-quantumdiamonds-raises-91-million-to-scale-its-quant
  title: Munich’s QuantumDiamonds raises €91 million to scale its quantum-based semiconductor inspection technology - EU-Startups
  date: '2026-07-09'
  kind: web
- slug: 2026-05-29-nasas-roman-space-telescope-primary-mirror-gets-last-look
  title: NASA’s Roman Space Telescope Primary Mirror Gets Last Look
  date: '2026-05-29'
  kind: web
- slug: 2025-intelmarketresearch-compound-semi-inspection-rejected
  title: Compound Semiconductor Inspection Equipment Market (IntelMarketResearch)
  date: '2025-12-31'
  kind: web
- slug: 2024-11-12-atomic-energy-can-nuclear-power-our
  title: 'Nuclear Fission: A Primer'
  date: '2024-11-12'
  kind: substack
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
neighbors: []
---
**Industrial inspection is being rebuilt around two independent fronts, cheap parallel optics plus machine learning on existing instrument data, and exotic photonics that pushes imaging into the mid-infrared at single-photon sensitivity; the first is close to production, the second is still benchtop.**

## Summary

Inspection is the measurement layer of manufacturing: the equipment and processing that decides whether a wafer, a weld, a board or a ceramic implant is good enough to ship, and if not, why it failed. It is a gating function rather than a product, so its economics are set by three parameters: throughput (area or parts per hour at the required resolution), sensitivity to the defect class that actually causes field failures, and whether the measurement is non-destructive. A tool that resolves a defect but takes an hour per sample, or that only sees it after sectioning the part, does not change a production line.

The sources cluster into three technical routes. The first is parallelised conventional optics: an epi-illumination multi-camera array microscope packs 24 synchronised microscope units in a 4x6 grid at 18 mm spacing, each with a 13 megapixel sensor, producing a stitched 72 x 108 mm image at 2.46 micrometre resolution on reflective samples including semiconductor wafers and printed circuit boards. The second is machine learning applied to instruments already installed on the line: a vision transformer trained on 8,493 SEM images (50x to 10,000x) drawn from five years of in-production burst and proof tests on alumina matrix composite implants classifies fracture cause into green body, hard machining and material defects at 0.907 accuracy and 0.888 macro-F1, with the finding that low magnification may suffice.

The third and largest group is new physics for defect classes the installed base cannot see. Confocal subsurface backscattering microscopy targets nanoscale threading dislocations in SiC, which drive reverse leakage and degradation and which commercial inspection based on surface profiling and photoluminescence dark contrast misses because they leave no resolvable surface signature. Structured-light metrology using Laguerre-Gaussian and Hermite-Gaussian beams with AI retrieval locates sub-wavelength nanostructures to lambda/110, or 7.2 nm, single-shot and alignment-free. A cluster of mid-infrared upconversion work converts 3 micrometre-band signals into the visible so silicon detectors can be used: noise equivalent power down to 0.3 fW/Hz^1/2 via a 36-fold cavity pump enhancement at 22 per cent peak conversion efficiency, a roughly 30 degree acceptance angle with frame rates to 216 kHz using aperiodic quasi-phase-matching, and tunable first- to fourth-order edge enhancement switchable at 60 Hz.

A caution on scope: several of the supplied sources use the word inspection in unrelated senses, such as packet inspection in quantum routers, ad hoc inspection of scientific datasets, and visual inspection of EEG power spectra. Those are excluded from the assessment below.

## Viability (3/5)

The individual measurements work. Upconversion detection reaches 0.3 fW/Hz^1/2 noise equivalent power, described as at least a ten-fold improvement over prior results; wide-field upconversion imaging achieves a roughly 30 degree acceptance angle in one shot without parameter scanning or post-processing; structured-light metrology reaches 7.2 nm precision single-shot. These are experimental results, not simulations.

What is missing is the manufacturing-relevant envelope. None of the optical sources report throughput per wafer or per part, cost, false-negative rate against a destructive ground truth, or stability outside a laboratory. The epi-MCAM covers 72 x 108 mm per capture cycle but must be mechanically translated for larger objects, and the cavity-enhanced upconversion detector runs at 55 W intra-cavity average power, which raises obvious questions about robustness in a fab. The strongest viability evidence is the vision transformer trained and cross-validated on five years of real in-production test images with a leakage audit confirming negligible specimen overlap, because that one was built against production data from the outset.

**TLDR: Physics demonstrated repeatedly and quantitatively, but almost entirely on benchtops; only the ML-on-SEM work touches production data.**

## Drivers (3/5)

On the supply side the enabling components are commodity: silicon CMOS sensors and EMCCDs used after frequency conversion, phase-only spatial light modulators and digital micromirror devices, and pretrained vision models reused as priors. The cost lever is explicit: upconversion and single-pixel schemes exist to avoid expensive, bulky, noisy infrared focal plane arrays. What the sources do not provide is any sizing of the market, capital budget or replacement cycle, so the driver score cannot go above the midpoint.

## Novelty (4/5)

The comparisons are explicit and quantified. Cavity pump enhancement gives at least a ten-fold improvement in noise equivalent power over previous upconversion results. Aperiodic quasi-phase-matching expands the acceptance angle to about 30 degrees, over ten times that of periodically poled crystals, which is the constraint that has kept upconversion imaging narrow-field. Time-stretch upconversion spectroscopy delivers 0.5 cm^-1 resolution over 2.4 to 4.2 micrometres at 0.14 photons per nanometre per pulse, an operating regime conventional mid-infrared spectrometers cannot reach because of sensor noise. Confocal subsurface backscattering microscopy is better than the alternative in the strongest sense available: it detects a defect class the incumbent commercial tools cannot see at all, and further distinguishes dislocation types by their photoelastic scattering patterns.

The less exotic entries also carry a novelty claim worth taking seriously. The finding that low-magnification SEM may suffice for fracture-cause classification attacks the cost driver of the incumbent workflow directly rather than adding capability, and single-frame radar reconstruction removes the synthetic aperture or multi-frame aggregation that makes radar impractical on small inspection platforms. The score stops at 4 because the baselines are, in most cases, prior laboratory work rather than deployed production tools.

**TLDR: Several results are stated as multiple-fold improvements over the named incumbent method, not incremental gains.**

## Diffusion (2/5)

Not one source reports a tool installed on a line, a qualification result, a cost of ownership figure or a cycle time per part. The epi-MCAM is described as having strong potential within industrial inspection applications, which is a statement of intent. Upconversion imaging results are framed as features that might stimulate subsequent applications. Inspection is a domain where the buyer's risk is asymmetric: a new tool must be demonstrated against the existing recipe on the same defect population before it displaces anything, and none of these have been.

The physical barriers differ by route. The upconversion systems depend on nonlinear crystals, high intra-cavity pump powers and spectro-temporal gating, which is a lot of alignment-sensitive apparatus to put next to a production tool. Structured-light metrology partly answers this by being alignment-free and single-shot, which is the single most diffusion-relevant property claimed in the whole set. The machine-learning route has the lowest barrier because it rides on instruments already present, but it inherits the classic obstacles: severe class imbalance, the need for interpretability in a safety-critical implant context, and unproven transfer across lines, materials or vendors.

**TLDR: No deployment evidence anywhere in the sources; the barriers are throughput, qualification and the conservatism of inspection recipes.**

## Impact (3/5)

The mechanism by which better inspection creates value is stated clearly in two cases. In SiC, threading dislocations cause reverse leakage and device degradation, so a non-destructive optical method that identifies and types them at the substrate stage acts on yield and on field reliability before value is added downstream. In ceramic hip and knee implants, reliable identification of fracture origins is described as critical for quality assurance and patient safety, and the current workflow is subjective. Both are cases where the inspection step, not the process step, is the bottleneck on quality.

Breadth also counts: the same sensing stack is invoked for remote sensing, environmental monitoring, biomedical diagnostics and infrared surveillance alongside industrial inspection, which means development costs are shared across markets. Against that, no source gives a defect escape rate, a yield delta, a scrap cost or a market size, so any claim that this is transformational rather than merely useful is not supported. A 3 reflects a credible and specific value mechanism with no measured magnitude.

**TLDR: Ties directly to yield in power semiconductors and to safety in medical implants, but no source quantifies the value at stake.**

## Timing Soon (2-5yr)

The ML route is closest. The vision transformer was trained on five years of in-production burst and proof test images and cross-validated on them, which is a step away from an in-line decision aid rather than a research demonstration. Camera-array microscopy is built from commodity CMOS sensors and standard objectives and needs integration work rather than invention.

The mid-infrared upconversion cluster is on a longer clock. It is progressing fast on the metrics that matter, with sensitivity, field of view and speed all improving within a few months of one another in 2026, but each demonstration is a free-space bench system, and none report throughput or environmental tolerance. Subsurface SiC inspection sits between the two: the method is described as simple and effective and addresses a defect class with a named commercial gap, which is the fastest path to a purchase order in this set.

**TLDR: Machine learning on existing inspection instruments is already production-adjacent; the photonic front needs several years of engineering before a fab or factory would qualify it.**

## Overrated or underrated? Fairly rated

Treated as a single field, inspection is fairly rated: real problems, real physics, no deployment evidence yet. But the internal weighting is wrong. The attention in these sources is concentrated on mid-infrared single-photon capability, where the achievements are genuine and quantified yet the path to a factory floor runs through pump lasers, nonlinear crystals and alignment budgets that nobody in these papers has costed. Meanwhile the two entries with the clearest commercial logic are unglamorous: a defect class that installed SiC inspection provably misses, and a demonstration that a cheaper, faster imaging mode plus a trained model can replace expensive expert-dependent analysis.

The practical test for anyone assessing an inspection technology is whether the pitch names the incumbent tool and the defects it misses. Two of these sources do; most do not, and instead list industrial inspection among four or five application domains. That is a sensing capability looking for a buyer, which is a slower and less certain business than a measurement gap with a known cost.

## Prediction

By 31 December 2028, at least one commercially marketed semiconductor substrate inspection tool will claim non-destructive detection of nanoscale threading dislocations in SiC, while no mid-infrared single-photon upconversion imager will be reported as qualified in a volume production inspection line.

## Evidence base

- 5 May to 30 June 2026: at least six independent optics groups name industrial inspection as a target application for mid-infrared upconversion sensing, spanning detection, spectroscopy, edge enhancement and wide-field imaging.
- 29 May 2026: a vision transformer trained on 8,493 in-production SEM images (50x-10,000x) classified implant fracture causes at 0.907 accuracy and 0.888 macro-F1 in stratified five-fold cross-validation, with low magnification found largely sufficient.
- 29 May 2026: cavity-enhanced mid-infrared upconversion reached 22 per cent peak conversion efficiency at 55 W intra-cavity average power and 0.3 fW/Hz^1/2 noise equivalent power, at least ten times better than previous results.
- 3 June 2026: aperiodic quasi-phase-matching widened the upconversion imaging acceptance angle to about 30 degrees, over ten times that of periodically poled crystals, enabling snapshot imaging at up to 216 kHz frame rate.
- 4 June 2026: commercial SiC defect inspection based on surface profiling and photoluminescence dark contrast is documented as missing nanoscale threading dislocations, which confocal subsurface backscattering microscopy detects non-destructively and can type by photoelastic scattering pattern.
- 5 June 2026: a 24-unit epi-illumination camera array microscope produced stitched 72 x 108 mm images at 2.46 micrometre resolution on semiconductor wafers and printed circuit boards, requiring mechanical translation for larger parts.
- 24 June 2026: single-shot, alignment-free structured-light metrology with AI retrieval located sub-wavelength nanostructures to lambda/110, or 7.2 nm, in 1D.

## Open questions

- What is the throughput, in wafer area or parts per hour, of confocal subsurface backscattering microscopy for SiC threading dislocations, and how does it compare with the surface-profiling and photoluminescence tools it would displace?
- Does the 0.907 accuracy of the SEM fracture-cause classifier hold on a different production line, a different ceramic grade or a different vendor's SEM, or is it specific to the five-year in-house dataset it was trained on?
- Can a 55 W intra-cavity pump upconversion detector be packaged to survive a factory environment, and at what cost relative to a cooled mid-infrared focal plane array?
- Does the lambda/110 structured-light metrology precision extend from 1D position of sub-wavelength nanostructures to the full 2D or 3D geometries that actually need measuring in production?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
