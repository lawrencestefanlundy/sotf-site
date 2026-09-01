---
type: concept
slug: perovskite
canonical_name: Perovskite
aliases:
- halide perovskite
- metal halide perovskite
- perovskite solar cell
- perovskite photovoltaic
- perovskite solar
- methylammonium lead
- MAPbI3
- FAPbI3
- perovskite film
- perovskite absorber
parent_concepts:
- generation
- energy-power
related_concepts:
- organic-photovoltaics
- silicon-photovoltaics
last_updated: '2026-08-31'
tags:
- concept
sources:
- '[[2026-08-31-qcells-tandem-iec-ul-certification-tuv-rheinland]]'
- '[[2025-2026-european-next-gen-pv-cohort]]'
- '[[2024-09-05-oxford-pv-first-commercial-tandem-shipment]]'
- '[[2025-04-18-longi-34-85-tandem-nrel-record]]'
scorecard:
  viability: 3
  drivers: 3
  novelty: 4
  diffusion: 2
  impact: 4
  timing_band: Later (5-10yr)
  verdict: Too early to say
scorecard_status: draft
mention_count: 102
sources_7d: 2
sources_30d: 22
recent_mentions:
- slug: 2026-08-31-qcells-tandem-iec-ul-certification-tuv-rheinland
  title: Qcells secures TUV Rheinland certification for perovskite-silicon tandem solar tech (pv magazine, 16 Jul 2026; pv-tech corroborating)
  date: '2026-08-31'
  kind: web
- slug: 2025-2026-european-next-gen-pv-cohort
  title: European next-gen PV cohort 2025-2026, Dracula, SunXT/Solertix, Perovion, HyET Solaris, Sofab Inks, Coatema
  date: '2026-06-01'
  kind: web
- slug: 2025-04-18-longi-34-85-tandem-nrel-record
  title: Longi achieves 34.85% efficiency for two-terminal tandem perovskite solar cell
  date: '2025-04-18'
  kind: web
- slug: 2024-09-05-oxford-pv-first-commercial-tandem-shipment
  title: Oxford PV starts commercial distribution of perovskite solar modules
  date: '2024-09-05'
  kind: web
neighbors:
- slug: organic-photovoltaics
  name: Organic Photovoltaics
  path: /energy-power/generation/organic-photovoltaics/
  macro: energy-power
- slug: silicon-photovoltaics
  name: Silicon photovoltaics
  path: /energy-power/generation/silicon-photovoltaics/
  macro: energy-power
---
**Perovskite is a crystal-structure family (ABX3 and its double-perovskite and layered variants) whose chemical substitutability lets one lattice motif be tuned into solar absorbers, photodetectors, quantum light emitters, catalysts and thermoelectrics; the current research frontier in these sources is not efficiency but escaping lead and taming defects.**

## Summary

Perovskite names a structure, not a compound. The parent ABX3 arrangement puts a large A cation in a cage of corner-sharing BX6 octahedra, and it tolerates an unusual amount of chemical substitution: the halide branch (CsPbBr3, methylammonium lead iodide, layered (PEA)2PbI4) underpins solar cells, LEDs and photodetectors, while the oxide branch (SrTiO3, EuTiO3, La0.6Sr0.4Fe1-xCoxO3, Ba2NiTeO6) delivers ferroelectrics, magnets and electrocatalysts. Ordered double perovskites (A2BB'X6) double the unit cell to accommodate two different B-site cations, opening up compositions with no lead at all.

The parameters that decide device behaviour are consistently the same across these sources. First, A/B/X chemistry sets the band gap: machine-learning models trained across A2BX6, A2BB'X6, A3B2X9 and A4BX6 halides identify B-site and X-site elemental properties as the dominant descriptors. Second, octahedral tilting and distortion matter as much as composition: in Cs2KInI6 the ideal cubic phase is dynamically unstable, and the distorted phases that are stable widen the gap, shift it from direct to indirect and flatten the band edges; under pressure, Ba2NiTeO6 crosses from rhombohedral to monoclinic with an accompanying direct-to-indirect gap change. Third, defect chemistry sets whether a good band structure translates into a good device. Bismuth-based oxide double perovskites Bi2FeCrO6 and Bi2MnCrO6 absorb strongly in the visible (10^4-10^5 cm^-1) with high carrier density but carry mixed cation valences and deep-level defects; iron doping introduces midgap 3d states that quench photoluminescence completely in CsPbCl3 while CsPbBr3 retains finite emission.

The framing in these sources is telling. Lead-halide perovskites are treated as the performance benchmark that non-toxic alternatives are trying to reach, and the stated reasons to leave them are lead toxicity and ambient instability rather than any shortfall in performance. Pnictogen chalcohalides such as BiSBr are described as promising non-toxic, stable substitutes but severely limited by carrier localisation, which is now traced to vacancy-derived defect-bound hot polarons. Beyond photovoltaics, the same lattice family is being pushed into quantum optics (room-temperature chiral superfluorescence, single-quantum-dot multiexciton spectroscopy), thermal management (ultralow thermal conductivity), oxygen-evolution catalysis and magnetocaloric cooling.

Note for the reader: the supplied sources are entirely fundamental physics and materials-science preprints. They contain no solar-cell efficiency figures, no module lifetimes, no manufacturing cost or capacity data. Several dimensions below therefore have to be scored on lab evidence only, and some cannot be scored at all.

## Viability (3/5)

Against that, every route away from lead in these sources is blocked by something specific and mechanistic. Cs2KInI6 has an attractive calculated 1.94 eV direct gap but its cubic phase is dynamically unstable, and the most stable structure found lies 13 meV/atom above the convex hull while lacking octahedral cation coordination. The bismuth oxide double perovskites carry deep-level defects. BiSBr does not intrinsically localise carriers but does so extrinsically once synthesis or post-treatment introduces vacancies. Score 3 rather than higher because the sources supply no efficiency, stability or lifetime numbers for any perovskite device, and rather than 2 because functioning devices in at least three distinct application classes are reported.

**TLDR: Working lab devices exist across several applications, but the sources themselves name the unsolved blockers: lead, instability and defects.**

## Drivers (3/5)

Supply: the discovery pipeline visible in these sources has changed character. A genetic algorithm plus machine-learned potentials plus first-principles validation identified 42 dynamically stable Cs2KInI6 structures, 11 of them verified ab initio. A physics-guided symbolic-regression framework picked GuaPbI3 out of compositional space before it was synthesised. Ensemble tree models (random forest, gradient boosting, XGBoost) now predict band gaps across four distinct halide perovskite structural families with strong reported accuracy. Machine-learned interatomic potentials with polarisable atomic multipoles reproduce Born effective charges and semi-quantitative Raman spectra for hybrid MAPbI3, extending simulation to the polar, ionic systems that previously defeated short-range potentials. Synthesis is also cheap: solution processing, antisolvent engineering, mechanochemistry, pore-wetting through polymeric membranes.

Demand: the sources give direction but no magnitude. Lead poisoning and notorious ambient instability are named as the motivation for the entire alternatives programme, and lead toxicity is called a critical barrier to practical development for imaging applications. There is no market sizing, policy instrument, price or procurement evidence in any source, so the demand half of this score rests on qualitative statements of regulatory and toxicity pressure only.

**TLDR: Supply side is accelerating through computational screening; demand is stated only qualitatively, as pressure to remove lead and improve stability.**

## Novelty (4/5)

Other entries are incremental but sharp: identification of a bound triexciton 7.4 plus or minus 1.9 meV blue-shifted from the exciton in single CsPbBr3 quantum dots, with the cascade order established; ferroelectric brightening of spin-forbidden dark excitons in WSe2 at zero magnetic field, replacing the strong external fields previously required, with twist angle controlling coupling strength; and oxygen-vacancy doping of EuTiO3 producing a phase diagram distinct from cation doping, including an antiferromagnetic-to-ferromagnetic change with Curie temperature about 11 K at carrier density about 10^21 cm^-3. Score 4 on the breadth and explicitness of the firsts; not 5 because none of them is yet shown to beat an incumbent technology on an application metric.

**TLDR: Several claimed firsts with quantified margins, including room-temperature chiral collective emission and millimetre-scale twisted oxide moire.**

## Diffusion (2/5)

The adoption barriers in these sources are chemical rather than commercial, and they are stubborn. Lead content blocks the halide branch in the applications where it works best. Ambient instability is cited alongside toxicity as characteristic of lead-based halide perovskites. Substitution introduces new failure modes: a single dopant species creates midgap states that render CsPbCl3 completely non-emissive, and electronic structure alone does not explain why CsPbBr3 survives the same treatment, so predictive control over doping is incomplete. Process sensitivity is severe: vacancies introduced during synthesis or post-treatment are what cause self-trapping in BiSBr, and oxygen vacancies segregate to the SrTiO3 surface across the whole band gap with segregation energies of -0.50 to -0.80 eV without improving catalytic activity.

There is one positive diffusion signal: fabrication routes are cheap and area-scalable in principle. Antisolvent engineering yields compact uniform films in one step, chiral superlattices already cover more than 100 by 100 micrometres, and freestanding oxide membranes have been assembled at millimetre scale. That is enough to justify 2 rather than 1, but the sources say nothing about yield, encapsulation, throughput, cost or operating lifetime, which are the terms on which diffusion is actually decided.

**TLDR: Barriers are named precisely and none is solved; the sources contain no manufacturing, scaling or field-deployment evidence at all.**

## Impact (4/5)

The case for high impact is the breadth demonstrated in a single month of literature. Photovoltaic absorbers with visible absorption coefficients of 10^4-10^5 cm^-1 and band-edge positions measured by ultraviolet photoelectron spectroscopy; a working computational imaging detector; room-temperature controllable chiral quantum light emission; quantum-communication-relevant nonlinear sources where sampling the coherence-time degree of freedom lowers the Holevo bound by 2.6-5.8 per cent across excitonic resonances in (PEA)2PbI4; oxygen-evolution catalysis with computed overpotentials of 0.45 V for pristine TiO2-terminated SrTiO3(001) and 0.43-0.48 V for neutral Fe substitution, degrading to 1.35 V in reduced dopant states; thermoelectric-relevant phonon suppression to 0.088 W m^-1 K^-1; and magnetocaloric entropy change up to 1.13 J kg^-1 K^-1 at 3 T in nanostructured La0.6Sr0.4FeCoO3.

The honest caveat is that several of these numbers are modest in absolute terms and the sources do not benchmark them against incumbents. The magnetocaloric figure, the OER overpotentials and the polarisation degree of the chiral emission are all early-stage values. Impact is scored 4 on the strength of the structural argument, that the same synthesis and modelling toolkit serves many end uses so progress compounds, rather than on any single demonstrated economic quantity, of which the sources give none.

**TLDR: One tunable lattice family spans photovoltaics, imaging, quantum light, catalysis, thermoelectrics and magnetocalorics, though the sources quantify none of the resulting value.**

## Timing Later (5-10yr)

Every source here is a fundamental physics or computational materials paper published between 5 May and 17 June 2026. The nearest-term items are laboratory demonstrators: a near-UV single-pixel imager and room-temperature chiral emission over a hundred-micrometre area. Those could plausibly reach specialist instrumentation sooner, but the sources do not say so.

For the energy-generation position this concept occupies, the timing is set by the blockers the sources name. Lead-free candidates are still at the stage of establishing whether a stable structure exists at all (Cs2KInI6 sits 13 meV/atom above the hull in its most stable form and loses octahedral coordination), or of diagnosing why carriers localise (BiSBr vacancy-bound hot polarons), or of measuring deep-level defects in a first-pass film. That is a 5-10 year path to competitive devices on any normal materials-development cadence, and the sources contain nothing that would justify a shorter band. Readers should treat this as a judgement about the alternatives programme; the commercial status of incumbent lead-halide photovoltaics is not addressed by any supplied source.

**TLDR: The lead-free and stability-hardened chemistries that these sources treat as the goal are pre-device; the sources give no deployment timeline for anything.**

## Overrated or underrated? Too early to say

For the specific question this taxonomy slot asks, whether perovskite is a generation technology that will matter, the supplied evidence cannot settle it. What the sources do establish is a clear and consistent picture of the field's internal logic: lead-halide perovskites are the reference against which everything else is measured, the reasons for wanting to replace them are toxicity and ambient instability rather than performance, and every replacement so far fails on structural stability or defect physics. That is a coherent research programme, not yet a technology verdict.

Where I will take a position: the computational half of the field is now genuinely ahead of the experimental half, and that is the most consequential development in these sources. Symbolic regression selecting a compound that was then synthesised and measured at 0.088 W m^-1 K^-1, genetic-algorithm structure search validated ab initio, band-gap models generalising across four structural families and multipole-based potentials reproducing hybrid perovskite vibrational spectra together mean the bottleneck has moved from candidate generation to defect control during synthesis. The Fe-doping result, where identical calculated midgap states produce opposite experimental outcomes in CsPbCl3 and CsPbBr3 and phonon calculations also fail to account for the difference, is the sharpest reminder that this bottleneck is real.

## Prediction

By 30 June 2029, lead-free halide and pnictogen-based alternatives to lead-halide perovskite absorbers will still be described in the peer-reviewed and preprint literature as trailing lead-halide perovskites on solar-cell performance, with defect-induced carrier localisation and dynamic lattice instability cited as the limiting causes.

## Evidence base

- First reported observation of chiral superfluorescence at room temperature from vertically aligned chiral perovskite superlattices over more than 100 by 100 micrometres, with circular polarisation up to about 14 per cent that reverses with handedness and responds to a weak magnetic field, 5 May 2026 
- Solution-deposited 350-450 nm Bi2FeCrO6 and Bi2MnCrO6 double-perovskite films show visible absorption of 10^4-10^5 cm^-1 and carrier densities of 10^17-10^20 cm^-3 but contain mixed cation valences and deep-level defects, with lead toxicity and ambient instability given as the motivation for leaving lead halides, 6 May 2026 
- Cs2KInI6 has a calculated 1.94 eV direct gap but a dynamically unstable cubic phase; machine-learning-accelerated search found 42 dynamically stable structures, the most stable lying 13 meV/atom above the convex hull and lacking octahedral cation coordination, with distortions widening the gap and turning it indirect, 4 June 2026 
- In BiSBr, carrier localisation is extrinsic: vacancies introduced during synthesis or post-treatment produce defect-bound hot polarons and self-trapping, the mechanism limiting non-toxic pnictogen absorbers from approaching lead-halide performance, 29 May 2026 
- A one-step-fabricated lead-free K2CuBr3 photoconductor with about 10^-10 A dark current and 38.82 / 61.94 microsecond response and recovery reconstructed near-UV single-pixel images with signal-to-noise improving from 16.4 to 31.7 dB, 2 June 2026 
- Symbolic-regression screening selected GuaPbI3, which was then synthesised mechanochemically and measured at room-temperature lattice thermal conductivity of about 0.088 W m^-1 K^-1 while retaining bulk electrical conduction, 15 June 2026 

## Open questions

- Can any lead-free perovskite or perovskite-derived absorber be shown to reach lead-halide-comparable device performance, given that the closest candidates currently fail on either dynamic stability (Cs2KInI6) or deep-level defects (Bi2FeCrO6, Bi2MnCrO6)?
- What controls the divergent doping response of CsPbCl3 versus CsPbBr3, since neither midgap electronic structure nor phonon calculations account for it, and can that mechanism be turned into a design rule?
- Can vacancy formation during synthesis and post-treatment be suppressed enough to eliminate defect-bound hot polarons in pnictogen chalcohalides, which the sources identify as extrinsic rather than intrinsic?
- Does the roughly 14 per cent circular polarisation of room-temperature chiral superfluorescence scale toward the values a quantum light source would need, and does it survive at wafer rather than hundred-micrometre scale?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
