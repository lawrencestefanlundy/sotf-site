---
type: concept
slug: deposition
canonical_name: Deposition
aliases: []
parent_concepts:
- equipment-processes
- manufacturing
related_concepts:
- chemical-vapor-deposition
- initiated-cvd-icvd
- powder-metallurgy
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
auto_stub: false
last_updated: '2026-08-31'
tags:
- concept
mention_count: 210
descendants:
- ald-atomic-layer-deposition
- chemical-vapor-deposition
- cvd-growth
- pvd-sputtering
scorecard:
  viability: 5
  drivers: 3
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
frontier:
- Does the PLD advantage in amorphous alumina ductility survive scaling from microcantilevers to wafer-scale coatings, and what structural difference between PLD, ALD and sputtered films of identical stoichiometry causes it?
- Does the 0.5 nm sputtered silicide template for GaN on Si(111) reproduce on production-diameter wafers and across the full set of 25 metallic species, and what vertical resistance is achieved in a finished device rather than a test structure?
- Is the 6% growth-axis elastic anisotropy in ion-beam-sputtered silica a general property of ion-beam-sputtered oxides, and does removing it at 900 C degrade other coating properties?
- Can kinetically driven dopant patterning during CVD, demonstrated in vanadium-doped WS2, be controlled deliberately rather than observed after the fact?
sources_7d: 8
sources_30d: 16
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-22-physics-ai-comp-landscape
  title: Physics-AI / ML-surrogate simulation competitive landscape (Zenithon comp set beyond PhysicsX)
  date: '2026-06-22'
  kind: web
- slug: 2026-05-18-deposition-materials-process-market-applied-materials
  title: Applied Materials Announces Record Q2 FY2026 Results and Guides for Greater Than 30% Equipment Growth in Calendar 2026
  date: '2026-05-18'
  kind: web
- slug: 2026-05-02-initiated-cvd-overview-wiley-analytical-science-2024
  title: Initiated CVD overview (Wiley Analytical Science 2024)
  date: '2026-05-02'
  kind: web
- slug: 2026-04-14-the-photonic-foundry-fallacy
  title: The Photonic Foundry Fallacy
  date: '2026-04-14'
  kind: substack
- slug: 2026-02-22-deposition-materials-process-market-companies-that-master
  title: Companies that master AS-ALD today specifically ASM and AMAT are positioned to dominate the $15B deposition market of the late 2020s
  date: '2026-02-22'
  kind: web
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2025-07-01-a-primer-carbon-nanotubes
  title: 'A Primer: Carbon Nanotubes'
  date: '2025-07-01'
  kind: substack
neighbors:
- slug: chemical-vapor-deposition
  name: CVD (Chemical Vapor Deposition)
  path: /manufacturing/equipment-processes/chemical-vapor-deposition/
  macro: manufacturing
- slug: initiated-cvd-icvd
  name: Initiated CVD (iCVD)
  path: /manufacturing/equipment-processes/initiated-cvd-icvd/
  macro: manufacturing
- slug: powder-metallurgy
  name: Powder Metallurgy
  path: /manufacturing/equipment-processes/powder-metallurgy/
  macro: manufacturing
---
**Deposition is the additive half of thin-film manufacturing, the family of processes (sputtering, CVD/MOCVD, atomic layer deposition, pulsed laser deposition, focused-beam direct write) that place atoms onto a substrate; the sources show it is mature and universal, and that the choice of deposition route now sets device performance as strongly as the choice of material.**

## Summary

Deposition covers every process that adds a solid film to a surface, as distinct from lithography (patterning) and etch (removal). Four families dominate the supplied evidence. Physical vapour deposition ejects atoms from a solid target: magnetron and dc sputtering, ion-beam sputtering for optical coatings, and pulsed laser deposition, which ablates a target with a focused laser and is used here for layered van der Waals magnets and for nuclear-grade alumina coatings. Chemical vapour deposition cracks gas-phase precursors on a hot surface, including metalorganic CVD for compound semiconductors, CVD growth of 2D crystals and carbides, and initiated CVD for polymer films <sup class="ref"><a href="https://analyticalscience.wiley.com/content/article-do/initiated-chemical-vapor-deposition" title="Initiated CVD overview (Wiley Analytical Science 2024)" rel="noopener">ref</a></sup>. Atomic layer deposition splits growth into self-limiting half-reactions, giving sub-nanometre thickness control and conformality. Direct-write methods such as focused electron beam induced deposition build freestanding 3D nanostructures by decomposing a precursor under the beam.

The parameters that decide outcomes are not exotic. Rate and temperature budget set what substrates survive. Conformality decides whether high-aspect-ratio features can be lined at all. Residual stress and microstructure, set by process pressure in sputtering, propagate into function: dense, smooth (111)-textured platinum films grown at low sputter pressure gave the highest hydrogen evolution activity despite less surface area than the porous, rougher films grown at high pressure. Phase selection is the other lever: reactive sputtering tends to favour metastable rocksalt-derived nitrides, so layered FeWN2 and FeMoN2 required post-deposition ammonia annealing, and FeMoN2 was only phase-pure at Fe-poor compositions.

The most useful single result in the set is a controlled comparison of routes at fixed chemistry. Amorphous Al2O3 films of similar stoichiometry were grown by PLD, ALD and sputter deposition; all PLD microcantilevers accommodated total strains above 10% without fracture, while half the ALD cantilevers fractured in an elastic-brittle manner and half showed bending plasticity. Composition did not determine mechanical behaviour; the growth route did. The same logic appears in the growth-axis elastic anisotropy of ion-beam-sputtered silica, a 6% compressive anisotropy along the film normal that the standard 500 C, 10 h detector anneal does not remove.

Deposition's economic ceiling is not set by deposition alone. Walker's 3D NAND cost model shows that stacking more deposited device layers does not reduce die cost monotonically: because any deep etch has a non-zero taper angle, the top-of-stack cell pitch grows linearly in layer count, so array footprint eventually grows faster than the layer count saves, producing a minimum in die cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. Films are cheap to add; the patterning of a thick stack is what bites.

## Viability (5/5)

Deposition is a mature manufacturing capability, and the supplied sources treat it as infrastructure rather than as a research risk. Independent groups report device-grade results across the full method space in a single month of 2026: ALD tuning of hBN photonic cavities with quality factors of ~4300 (1D photonic crystal cavity) and ~8300 (microdisk), PLD films of (Fe,Ni)5GeTe2 with a Curie temperature reaching ~498 K and a clear anomalous Hall effect, CVD-grown Mo2C nanoflakes with a superconducting diode efficiency exceeding 40% at 4 K. Ion-beam-sputtered SiO2 is described as a material still viable for future gravitational-wave mirror coatings and already subject to a standardised post-deposition heat treatment in ground-based detectors, which is a deployed-hardware datapoint, not a lab one.

The caveat is that viability of the category says nothing about viability of any given film. Per-material control remains uneven: FEBID produces non-uniform composition in intricate 3D geometries because growth dynamics change with beam translation and interaction volume; layered FeMoN2 only reaches good phase purity at Fe-poor compositions; and ALD alumina showed bimodal brittle-versus-plastic behaviour within a single sample set. The frontier is reproducibility and phase selection, not whether films can be grown.

**TLDR: Not in question: every source uses deposition as a working tool, and some routes are already in deployed hardware.**

## Drivers (3/5)

Demand is visible and specific in the sources. Vertical GaN-on-silicon is bottlenecked by the high electrical resistance of conventional epitaxial buffer layers, and the stated prize is cost-effective power electronics and high-resolution micro-LEDs, which is exactly a pull for a better nucleation and overgrowth process. Gravitational-wave detectors need lower coating thermal noise, which depends on the elastic properties of deposited layers. Nuclear plant lifetime pushes durable amorphous alumina coatings characterised to 650 C. Memory scaling is the largest pull: 3D NAND was sold on cost per bit falling monotonically with device layers, and the layer count race is the reason deposition and deep-etch capability matter commercially **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.

The supply side is absent. The sources contain no information on precursor availability, tool vendors, equipment capital cost, throughput, target material sourcing or capacity. Any judgement about deposition equipment as a market cannot be made from this evidence base, and the score reflects only the demand-side half of the picture. Walker's model also implies the demand driver is self-limiting in at least one flagship application: beyond the cost minimum, adding deposited layers makes the die more expensive, not less **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.

**TLDR: Clear demand pull from several device roadmaps; the sources say almost nothing about the supply side.**

## Novelty (3/5)

Nothing here is a new class of process. Sputtering, CVD, ALD and PLD all appear as established options, and the novelty sits in what they are better than. Two comparisons are quantified. Against conventional epitaxial buffer layers for GaN on Si(111), an in-situ sputtered sub-nanometre (0.5 nm) silicide template formed by rapid thermal annealing gave low vertical resistance and ohmic behaviour, and worked across 25 different metallic species before MOCVD overgrowth; the claimed advantage is versatility plus a resistance path that buffer layers block. Against ALD and sputter deposition at similar stoichiometry, PLD amorphous alumina was the only route where all tested microcantilevers exceeded 10% total strain without fracture. ALD's distinct advantage is post-fabrication precision: it shifted cavity resonances by ~9 nm in 1D photonic crystal cavities and ~16 nm in microdisks, a trimming capability sputtering cannot match.

A second novel thread is deterministic control of what was assumed to be random. Dopant distribution in 2D semiconductors is typically taken to be stochastic; CVD growth kinetics were shown to drive preferential vanadium incorporation along crystallographic bisectors in WS2 monolayers, creating localised tensile strain channels of about 0.70%, captured by an adsorption-growth-diffusion model with a single kinetic parameter. That reframes deposition kinetics as a defect-engineering tool. The score is held at 3 because these are single-group results, not yet replicated or transferred to manufacturing.

**TLDR: The methods are decades old; the genuinely new result is that route choice at fixed chemistry changes device physics.**

## Diffusion (4/5)

Adoption is not the question. The 18 sources span memory cost modelling, power electronics, quantum photonics, superconducting devices, electrocatalysis, correlated oxides, solid-state batteries, nuclear coatings, gravitational-wave optics and spintronic nanostructures, and every one of them uses a deposition step as the enabling process. One route is embedded in operating scientific hardware, with ion-beam-sputtered silica coatings and a standard 500 C, 10 h post-deposition anneal in ground-based detectors. MOCVD is treated as the scalable, low-cost overgrowth step that a new nucleation strategy must feed.

The barriers that remain are transfer barriers. Process windows are narrow and non-obvious: HER activity in sputtered Pt tracks sputter pressure through stress and microstructure rather than through surface area, and VO2 metal-insulator hysteresis differs between PLD and dc sputtered films of different grain size, so a recipe does not port between tools. Assumptions baked into downstream models can be wrong, as with the previously unverified isotropy of sputtered silica. Some routes are intrinsically slow or serial: FEBID needed 41 individually written nanowire structures to map growth angle from 0 to 90 degrees, which places it in prototyping rather than volume production. The sources give no throughput or yield figures, so the score rests on breadth of use rather than on measured manufacturing readiness.

**TLDR: Already diffused across essentially every materials field in the source set, with the barriers now being process transfer rather than acceptance.**

## Impact (4/5)

The breadth of consequence is high. If the sputtered silicide template generalises, it unlocks vertical GaN on silicon for power electronics and micro-LEDs by removing the buffer-layer resistance bottleneck. If coating elastic anisotropy is real and removable, it changes thermal-noise budgets for gravitational-wave detectors, since the anisotropy survives the current 500 C anneal but is nearly eliminated at 900 C. ALD trimming of resonators is the difference between statistical yield and deterministic emitter-cavity coupling in hBN quantum photonics. Air-stable CVD Mo2C is proposed as a platform for nonreciprocal supercurrent devices. Deposition-route selection for amorphous alumina determines whether a brittle ceramic film behaves plastically, which matters wherever thin ceramic layers must survive strain.

The honest discount is that deposition rarely captures the value it enables, and its leverage is bounded by neighbouring processes. Walker's analysis is the sharpest statement of that bound: adding deposited device layers to a 3D memory stack stops reducing cost once etch taper inflates the top-of-stack cell pitch, and a lithography-intensive layered approach using three critical masks per device layer can reach a smaller die and undercut the vertical-channel approach on total cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. Cheap film growth does not by itself produce cheap devices. A 5 is not earned because none of these device-level impacts is yet demonstrated in a shipped product within the sources.

**TLDR: Foundational: it gates several separate device roadmaps in the sources, though its own economic ceiling is set by patterning.**

## Timing Now (0-2yr)

Deposition itself is a present-tense manufacturing capability: the sources show it in deployed detector coatings, in MOCVD as the assumed scalable overgrowth route and as the basis of a memory cost model published in 2013 **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. Anyone assessing whether to bet on deposition existing has the wrong question.

The individual advances are earlier stage. The sputtered silicide template, the PLD ductility result, the kinetic dopant-patterning result in WS2 and the silica anisotropy measurement were all first published in 2026 and are single-group, coupon-scale demonstrations. Wafer-scale reproduction, then qualification, then insertion into a production flow is the normal multi-year path, and the sources give no evidence any of these has started it.

**TLDR: The toolset is in production today; the specific improvements in these sources are 2-5 years from mattering commercially.**

## Overrated or underrated? Underrated

Deposition is underrated relative to lithography as a determinant of device outcomes, and the evidence for that sits in the comparative studies rather than in any single hero result. Three films of the same nominal composition behaved from ductile to brittle depending only on whether they were grown by PLD, ALD or sputtering. An optical coating material assumed homogeneous and isotropic for the purposes of thermal-noise modelling turned out to carry a 6% growth-axis elastic anisotropy that had never been checked. Catalytic activity in platinum tracked sputter pressure rather than surface area. In each case the deposition parameter, not the material choice, is the design variable, and in each case it had been treated as a detail.

The counterweight, and the reason this is not a straightforward buy, is that deposition does not set its own ceiling. Walker's model shows that a strategy of adding ever more deposited layers has a cost minimum imposed by etch taper, beyond which cost rises with every layer, and that a lithography-heavy alternative can win outright **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. The correct position is that deposition process control is undervalued as a source of performance, while deposition-driven layer stacking is overvalued as a source of cost reduction. The sources support no view at all on the deposition equipment market.

## Prediction

By 31 December 2028, at least one published gravitational-wave coating study will report annealing ion-beam-sputtered silica above 500 C specifically to remove the growth-axis elastic anisotropy reported in May 2026, and will quantify the resulting change in coating thermal noise or mechanical loss.

## Evidence base

- November 2013: a rigorous 3D NAND cost model shows die cost per bit has a minimum in device layer count, because deep-etch taper makes top-of-stack cell pitch grow linearly with layers, and a layered approach using three critical masks per device layer can undercut vertical-channel NAND on total cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.
- 4 May 2026: an in-situ sputtered sub-nanometre (0.5 nm) silicide template formed by rapid thermal annealing, demonstrated across 25 metallic species, gives low-vertical-resistance ohmic GaN epitaxy on Si(111) and serves as a platform for MOCVD overgrowth.
- 4 May 2026: atomic layer deposition and gas condensation tuned hBN resonators with quality factors ~4300 (1D photonic crystal cavities) and ~8300 (microdisks), shifting resonances by ~9 nm and ~16 nm respectively.
- 5 May 2026: amorphous Al2O3 films of similar stoichiometry grown by PLD, ALD and sputtering behaved differently in microcantilever bending; all PLD cantilevers exceeded 10% total strain without fracture while half the ALD cantilevers fractured in elastic-brittle mode.
- 8 May 2026: Brillouin light scattering showed ion-beam-sputtered SiO2 has cylindrical elastic symmetry with 6% compressive anisotropy along the film normal, unchanged by the 500 C, 10 h anneal currently used in ground-based gravitational-wave detectors but nearly eliminated at 900 C.
- 8 May 2026: magnetron-sputtered Pt films deposited at low sputter pressure were dense, smooth and (111)-textured and gave the highest hydrogen evolution activity, while higher sputter pressures produced porous, rougher films with reduced activity despite greater surface area.

## Open questions

- Does the PLD advantage in amorphous alumina ductility survive scaling from microcantilevers to wafer-scale coatings, and what structural difference between PLD, ALD and sputtered films of identical stoichiometry causes it?
- Does the 0.5 nm sputtered silicide template for GaN on Si(111) reproduce on production-diameter wafers and across the full set of 25 metallic species, and what vertical resistance is achieved in a finished device rather than a test structure?
- Is the 6% growth-axis elastic anisotropy in ion-beam-sputtered silica a general property of ion-beam-sputtered oxides, and does removing it at 900 C degrade other coating properties?
- Can kinetically driven dopant patterning during CVD, demonstrated in vanadium-doped WS2, be controlled deliberately rather than observed after the fact?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
