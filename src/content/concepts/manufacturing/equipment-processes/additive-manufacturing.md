---
type: concept
slug: additive-manufacturing
canonical_name: Additive Manufacturing
aliases: []
kind: technology
parent_concepts:
- manufacturing
- equipment-processes
related_concepts: []
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2024-09-13-bis-adopts-additional-controls-on-quantum-semiconductor-and-]]'
- '[[2022-05-09-elementum-funded-by-darpa-to-develop-am-process-for-rhenium-]]'
- '[[2024-09-16-bis-imposes-new-export-controls-on-quantum-semiconductor-and]]'
- '[[2021-02-04-meta-additive-awarded-innovate-uk-smart-grant-for-bjt-proces]]'
- '[[2020-12-17-university-additive-manufacturing-spin-out-secures-12m-innov]]'
- '[[2025-08-18-nist-awards-over-18-million-to-small-businesses-advancing-ai]]'
- '[[2024-09-11-bis-imposes-new-export-controls-on-quantum-semiconductor-and]]'
frontier:
- Does the unified TVAM plus 2PP platform hold its resolution and adhesion across many materials and repeated builds, or only in the demonstrated glass-rod, single-resin configuration 2026 06 19 a unified multiscale 3d printer combining single photon tomo?
- Do neural pre-correction models trained on one machine and resin transfer to other printers and chemistries, as the authors expect, or must they be retrained per installation 2026 06 05 first steps towards machine learning for prediction and pre ?
- Can composition non-uniformity in beam-induced deposition of overhanging 3D nanostructures be compensated in-process, rather than only measured after the fact 2026 05 15 compositional and magnetic characterisation of oblique co an?
- Will acoustic and magnetic side-channel leakage be treated as a qualification requirement for distributed AM, given a 98.89% G-code reconstruction rate from consumer smartphones 2026 07 02 a non line of sight multi modality based side channel ip the?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 62
descendants:
- metal-additive-manufacturing
last_reorg_date: '2026-05-13'
scorecard:
  viability: 4
  drivers: 3
  novelty: 3
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-08-18-nist-awards-over-18-million-to-small-businesses-advancing-ai
  title: NIST Awards Over $1.8 Million to Small Businesses Advancing AI, Semiconductors, Additive Manufacturing and More
  date: '2025-08-18'
  kind: web
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2024-09-16-bis-imposes-new-export-controls-on-quantum-semiconductor-and
  title: BIS Imposes New Export Controls on Quantum, Semiconductor and Additive Manufacturing Technologies - JD Supra
  date: '2024-09-16'
  kind: web
- slug: 2024-09-13-bis-adopts-additional-controls-on-quantum-semiconductor-and-
  title: BIS Adopts Additional Controls on Quantum, Semiconductor and Additive Manufacturing Technologies in Concert with International Partners - Mayer Brown
  date: '2024-09-13'
  kind: web
- slug: 2024-09-11-bis-imposes-new-export-controls-on-quantum-semiconductor-and
  title: BIS Imposes New Export Controls on Quantum, Semiconductor and Additive Manufacturing Technologies - globaltradeandsanctionslaw.com
  date: '2024-09-11'
  kind: web
- slug: 2022-05-09-elementum-funded-by-darpa-to-develop-am-process-for-rhenium-
  title: Elementum funded by DARPA to develop AM process for rhenium - Metal Additive Manufacturing magazine
  date: '2022-05-09'
  kind: web
- slug: 2021-05-06-weav3d-awarded-nsf-funding-to-further-develop-next-generatio
  title: WEAV3D awarded NSF funding to further develop next-generation composite forming machine - Design World
  date: '2021-05-06'
  kind: web
neighbors: []
---
**Additive manufacturing builds parts by adding material under digital control rather than cutting it away, and the current research frontier is less about the printers than about beating the resolution-versus-speed trade-off and making print fidelity predictable enough for real engineering parts.**

## Summary

Additive manufacturing (AM) is the family of processes that construct an object by depositing or solidifying material where a digital model says material should be, instead of removing it from a blank. The supplied evidence covers three distinct physical families rather than one technology. Light-based photopolymerisation cures liquid resin: two-photon polymerisation (2PP, also called direct laser writing) reaches sub-micrometre features but only over sub-millimetre volumes, while single-photon tomographic volumetric additive manufacturing (TVAM) forms centimetre-scale objects within seconds at feature sizes of tens of micrometres. Metal powder bed fusion (L-PBF) melts metal powder with a laser and is already used in production, but suffers from unstable melt-pool keyholes that generate porosity and spatter. At the smallest scale, focused electron beam induced deposition (FEBID) writes freestanding 3D nanowires directly.

The parameters that decide the field are resolution, build volume, throughput and fidelity, and they trade against each other. Photopolymerisation is explicitly described as constrained by a resolution/speed trade-off. Two lines of attack appear in the sources. The first is optical and computational: differentiable ray-optics and wave-optics models that compute projection patterns accounting for occlusions, refraction, scattering and even chemical blur, enabling overprinting onto pre-existing components and single-view holographic printing with roughly 10 micrometre lateral features. The second is hybridisation: running TVAM and 2PP on one platform in the same resin so a millimetre-scale body can carry sub-micrometre detail without stitching, platform changes or intermediate processing.

A parallel and equally large theme is process informatics. Prints deviate from the target because of physico-chemical effects, and neural networks are being trained to predict and pre-correct those deviations rather than relying on iterative trial prints. Related work covers automated defect classification that can absorb new defect classes and new part geometries from scarce data, machine health monitoring to replace experience-based maintenance, and physics-informed prediction of metal AM temperature fields that generalises to unseen materials without retraining. Read together, the sources describe a technology that already works and is now being industrialised through metrology, modelling and control.

## Viability (4/5)

Across the sources, AM is not being demonstrated in principle but used to make working parts. Two-photon polymerisation produced deformation sensors roughly 100 micrometres in height and width directly on commercial optical ferrules carrying 125 micrometre fibres, using off-the-shelf photopolymers OrmoComp and FemtoBond. The same technique, combined with in-situ iron oxide nanoparticle coprecipitation, yielded a magnetically actuated soft gripper and a bistable bit register with millimetre-scale elastic deformations. A 3D-printed nonlocal freeform Bessel-beam lens delivered an achromatic beam from 0.3 to 1 THz with a 0.65-wavelength FWHM and 4.7 mm depth of focus inside an integrated imaging system. L-PBF is described as already established in production sectors.

The honest limits are also documented. Direct laser writing prints deviate from the target because of physico-chemical processes, limiting accuracy and reliability. FEBID structures with overhangs show non-uniform atomic composition that varies with growth angle, measured across 41 cobalt and iron nanowires spanning 0 to 90 degrees. L-PBF keyhole instability still causes porosity and spatter, and TPL maintenance is often based on experience rather than measured machine state. This is a working technology with a quality-assurance deficit, not an unproven one.

**TLDR: The processes work and produce functional devices with commercial materials; repeatability and fidelity are the residual problems.**

## Drivers (3/5)

On supply, the enabling inputs are getting cheaper and more open. Volumetric projection optimisation is distributed as the open-source Dr.TVAM framework and produces usable projections within minutes, or lower-quality ones within seconds, for both laser and LED illumination. Consumer printers are cheap enough to be treated as generic motion platforms: an Elegoo Neptune 4 Max was converted into a digital-twin-supervised autonomous liquid handler by swapping the extruder for a pipette driven by the printer's own G-code gantry. Machine learning is arriving as a general-purpose fidelity tool, with the explicit claim that the approach transfers to other 3D printing technologies because they share the same fidelity problem.

On demand, the sources point at specific pull but give no market sizing. AM is stated to have transformed aerospace, automotive and healthcare by enabling adjustable production. Wireless is a named forward driver: permittivity of commercial 3D printing materials was characterised across 70 to 110 GHz specifically to support 6G antennas and metasurfaces. Microscale magnetoactive devices are described as scarce because of manufacturing limitations, which is demand waiting on process capability. No source here provides volumes, revenues or procurement commitments, so the demand side of this score rests on qualitative statements.

**TLDR: Strong supply-side pull from cheap hardware, open tooling and machine learning; demand is asserted in the sources rather than quantified.**

## Novelty (3/5)

The category is old, so novelty has to be judged at the technique level. The clearest step changes are in light-based printing. TVAM produces centimetre-scale objects in seconds, and the new contribution is overprinting onto or around pre-existing components made of different materials, including absorbing, refracting, reflecting and scattering elements, with the authors claiming their differentiable ray-optics approach exceeds existing open-source solutions in speed, flexibility and quality. The hybrid TVAM plus 2PP printer is better than prior hybrids specifically because it avoids stitched or layer-by-layer fabrication and separate platforms, which the authors identify as what made mesoscale manufacturing time-consuming. SHVAM is mechanically static, using time-multiplexed phase-only holograms from a single axis, and reports higher fidelity than optical-only optimisation because it pre-compensates for chemical blur, reaching about 10 micrometre features.

Elsewhere the improvements are real but narrower. MOSAIC segments L-PBF keyhole X-ray images at 19.9 ms per cropped frame on CPU with an average F1 of 0.894 and precision of 0.953 over 12 samples, matching or beating the SAM and YOLO baselines tested at 54 and 5284 ms respectively, and without manual labelling or model training. The parametric physics-informed neural network is novel mainly in generalising across unseen materials without labelled data, retraining or pre-training. A hybrid quantum-classical melt pool predictor is at simulator stage and does not yet constitute a demonstrated advantage.

**TLDR: AM itself is mature; what is genuinely new is volumetric and hybrid multiscale printing plus computational pre-correction, with measured but technique-level margins.**

## Diffusion (3/5)

Diffusion is uneven and the barriers named in the sources are mostly about trust rather than capability. Quality models in micro-AM are static, cannot detect unseen defect classes, cannot be updated efficiently from scarce data and do not transfer to new part geometries, which is why domain adaptation from hemisphere to cube geometries is treated as a research problem. Maintenance is reactive, causing either downtime and bad parts or unnecessary servicing. L-PBF is explicitly characterised as promising but afflicted by quality assurance concerns, with melt pool prediction from process parameters still difficult. Designers also hit manufacturability limits: inverse-designed MXene metamaterial absorbers with spatially variable substrates frequently come out non-manufacturable, requiring dedicated methodology to impose layer-to-layer connectivity constraints without destroying performance.

Two further frictions are visible. Basic materials data for new application domains is only now being generated, as with permittivity of common printing materials at 70 to 110 GHz. And security is a live obstacle to distributed manufacturing: acoustic and magnetic emissions collected by two ordinary smartphones placed 60 cm away in a non-line-of-sight setup reconstructed a printer's G-code at 98.89% command-level accuracy, with the attack shown to transfer to a second printer. Against that, adoption in adjacent fields is frictionless where precision demands are low, as shown by a consumer printer converted into a lab robot.

**TLDR: Already diffusing in production sectors and in labs, but qualification, materials data gaps and an unaddressed IP-leakage risk slow the rest.**

## Impact (3/5)

The strongest impact argument in these sources is that AM makes devices that are otherwise hard or impossible to build. FEBID is described as uniquely suited to nanoscale 3D prototypes including spintronic devices. Microscale soft-magnetic composites had previously suffered from limited control over particle loading, distribution and matrix stiffness, and locally modulating the two-photon dose restored that control well enough to build a functioning gripper and a bistable memory element. Printing directly onto a commercial fibre ferrule collapses an assembly problem into a fabrication step, and a printed freeform lens enabled a compact THz imaging system that conventional bulky transceiver architectures could not match on chromatic aberration, resolution and depth of focus.

The ceiling on this score is evidential, not conceptual. No source here provides cost, yield, throughput-per-hour or market figures, so the size of the prize cannot be sized from this material. The one cost-side data point is indirect: a converted consumer printer replacing high-cost proprietary liquid-handling hardware, which suggests where the value lands when AM commoditises precision motion. If the volumetric plus two-photon multiscale route holds up, its impact would be to make mesoscale parts with micro-scale detail economically routine, but that is a demonstration, not yet an industrial result.

**TLDR: Clearly an enabling capability across photonics, RF, spintronics and microrobotics, but the sources quantify device performance, not economic value.**

## Timing Now (0-2yr)

The technology is already deployed. L-PBF is in aerospace, automotive and healthcare production, two-photon polymerisation is being used with commercial resins on commercial fibre components, and printed materials are being characterised for near-term 6G work. The process-informatics layer, meaning ML pre-correction, few-shot defect classification and machine health monitoring, is at working-prototype stage on real experimental datasets and is the most likely thing to reach commercial machines first.

The genuinely new capabilities sit slightly further out. Overprinting with TVAM, single-view holographic volumetric printing at about 10 micrometres, and the unified TVAM/2PP platform are single-group demonstrations published in 2026. The quantum-assisted melt pool work is earlier still, validated on a simulator with shot-noise analysis.

**TLDR: Metal AM and two-photon micro-AM are in use now; volumetric and hybrid multiscale printing are at credible laboratory demonstration and are the next two to five years.**

## Overrated or underrated? Fairly rated

As a category, AM is neither hype nor a secret: it is in production, and the sources treat it as an established manufacturing route with a known weakness in quality assurance. The mistake would be to keep assessing it on printer specifications. Almost all the interesting 2026 work here is about closing the loop around the printer: differentiable physical models that compute what light to project given occlusions, refraction and chemical blur, neural pre-correction of print deviations, defect classifiers that survive geometry changes, and material-agnostic thermal prediction for metals. That software and metrology layer is the underrated part.

Two specifics deserve more weight than they currently get. First, the resolution/speed trade-off may be sidestepped rather than optimised: putting volumetric and two-photon printing on one platform in one resin removes the stitching and platform-swapping that made mesoscale parts slow. Second, side-channel IP theft is a structural threat to the distributed-manufacturing thesis, since two consumer smartphones at 60 cm and out of line of sight recovered G-code at 98.89% command-level accuracy and the attack transferred to another printer. Anyone underwriting a print-on-demand licensing model should price that.

## Prediction

By 31 December 2028, at least one commercially purchasable printer will offer combined volumetric single-photon and two-photon polymerisation on a single platform in a single resin, following the laboratory demonstration published in 2026.

## Evidence base

- 19 June 2026: a single-platform hybrid printer combined single-photon TVAM for millimetre-scale volumes with 2PP for sub-micrometre detail in the same photoresin, without intermediate post-processing or stitching.
- 16 June 2026: TVAM overprinting onto absorbing, refracting, reflecting and scattering pre-existing components was demonstrated in round and square vials, with the open-source Dr.TVAM differentiable ray-optics framework producing high-quality projections within minutes.
- 17 June 2026: single-view holographic volumetric printing using time-multiplexed phase-only holograms achieved roughly 10 micrometre lateral features and higher fidelity than optical-only optimisation by pre-compensating for chemical blur.
- 16 June 2026: the MOSAIC keyhole segmentation algorithm averaged an F1 of 0.894 and precision of 0.953 across 12 L-PBF samples at 19.9 ms per frame on CPU, versus 54 ms and 5284 ms for the SAM and YOLO baselines.
- 15 May 2026: 41 cobalt and iron nanowires grown by FEBID at angles from 0 to 90 degrees showed measurable composition and magnetic induction variation, quantifying a fidelity limit for 3D nanoscale printing.
- 2 July 2026: two smartphones 60 cm away in a non-line-of-sight setup reconstructed a 3D printer's G-code commands at 98.89% command-level accuracy, with transferability shown to a second printer.
- 21 July 2026: permittivity of commercial 3D printing materials was characterised from 70 to 110 GHz by open-waveguide extraction, targeted at 6G antennas and metasurfaces.

## Open questions

- Does the unified TVAM plus 2PP platform hold its resolution and adhesion across many materials and repeated builds, or only in the demonstrated glass-rod, single-resin configuration?
- Do neural pre-correction models trained on one machine and resin transfer to other printers and chemistries, as the authors expect, or must they be retrained per installation?
- Can composition non-uniformity in beam-induced deposition of overhanging 3D nanostructures be compensated in-process, rather than only measured after the fact?
- Will acoustic and magnetic side-channel leakage be treated as a qualification requirement for distributed AM, given a 98.89% G-code reconstruction rate from consumer smartphones?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
