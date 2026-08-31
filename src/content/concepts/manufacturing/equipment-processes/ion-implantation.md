---
type: concept
slug: ion-implantation
canonical_name: Ion Implantation
aliases:
- ion implant
- implanter
- doping
parent_concepts:
- semiconductor-equipment
related_concepts:
- deposition
- etch
- materials-process
sources:
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
frontier:
- What fraction of implanted Er in Si3N4 is optically active after annealing, and does the four-fold emission gain from 20 nm to 80 nm ion range reflect activation, damage recovery, or purely the overlap with the Mie resonance field profile?
- What thermal budget does the required post-implant anneal impose, and is it compatible with a CMOS photonics back-end flow?
- At what feature scale does implantation lose to beam-induced chemical doping such as the electron-beam methane route, and does that boundary move with host material thickness?
- Can implanted doping profiles in realistic multilayer stacks be verified non-destructively, given that the accessible doping ranges for contact-free terahertz characterisation are still being mapped?
- What implanted Er3+ areal dose and anneal schedule maximise photoluminescence in Si3N4 before concentration quenching or residual implantation damage dominates, and how sharp is that optimum?
- Does implantation-induced damage in Si3N4 metasurfaces measurably degrade optical loss or resonance Q relative to undoped controls after annealing?
- Can contact-free terahertz time-domain spectroscopy resolve implanted, annealed dopant profiles in thin layers within the sensitivity bounds calculated for SiC, Si and GaN, or is it limited to bulk-like doping levels?
- For devices where implantation is not used, such as diamond 2D hole gas FETs, can the reported GIDL-like leakage be distinguished from implantation-style defect signatures by the same silicon MOS extraction toolkit?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 125
scorecard:
  viability: 3
  drivers: null
  novelty: 3
  diffusion: null
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 3
sources_30d: 17
recent_mentions:
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
neighbors:
- slug: deposition
  name: Deposition
  path: /manufacturing/equipment-processes/deposition/
  macro: manufacturing
- slug: etch
  name: Etch
  path: /manufacturing/equipment-processes/etch/
  macro: manufacturing
- slug: materials-process
  name: Materials & Process
  path: /materials/advanced-materials/materials-process/
  macro: materials
---
**Ion implantation drives ionised dopant atoms into a solid at controlled energy and dose, giving depth and lateral placement control that solution or growth-based doping cannot match, and in the supplied evidence it is the enabling step for putting erbium emitters into CMOS-compatible silicon nitride photonics.**

## Summary

Ion implantation introduces impurity atoms into a host material by ionising them, accelerating them in an electric field and firing them into the surface. Two knobs matter: the acceleration energy, which sets how deep the ions stop (the ion range, and hence the depth profile of the dopant), and the dose, which sets how many are delivered per unit area. Because the beam can be masked, dopants can also be placed laterally with lithographic precision. The penalty is lattice damage from the collision cascade, so implantation is almost always followed by a thermal anneal to repair the host lattice and move the implanted species into the sites where it is electrically or optically active.

In the supplied evidence, implantation appears as the doping route for erbium into silicon nitride metasurfaces. The metasurfaces are periodic nanocylinder arrays engineered for Mie-type resonances, and after thermal annealing the authors report a room-temperature photoluminescence enhancement factor of about 18 at a nanocylinder radius of 390 nm at telecom wavelength, with a near ten-fold reduction in luminescence lifetime indicating a Purcell-driven effect. Decisively for implantation as a process, the emission depends strongly on implantation depth: a four-fold increase in emission going from a 20 nm to an 80 nm ion range. That is the parameter that only a beam-based technique gives you cleanly.

The rest of the source set is best read as the competitive field. Dopants are being introduced by wet liquid infiltration of pre-sintered zirconia discs followed by sintering, by non-vacuum spin coating with a NaCl dopant, by oxygen-vacancy creation using CaH2 as an oxygen getter to reach carrier densities of order 10^21 cm^-3, by trace metal incorporation during film growth, and by electron-beam irradiation in a methane atmosphere that generates vacancies and cracks the gas simultaneously, confining 84 plus or minus 7 per cent of carbon-rich regions to the irradiated area. Implantation competes on placement precision and on getting species into hosts that will not accept them chemically; it loses on cost and simplicity wherever bulk uniform doping suffices.

## Viability (3/5)

The direct evidence is a single paper, but it is a good one: erbium implanted into Si3N4 nanocylinder metasurfaces, annealed, and measured to give roughly 18-fold photoluminescence enhancement at 390 nm radius in agreement with simulation, with time-resolved measurements attributing the gain to the Purcell effect rather than to more erbium being active. The implantation-specific result is that emission scales with ion range, four-fold from 20 nm to 80 nm, which means the depth profile is both controllable and consequential.

That supports viability of the process for this class of work, not a broader judgement. The supplied sources say nothing about implanted-dopant activation efficiency, damage recovery limits, thermal budget constraints in integrated flows, or throughput, all of which decide whether an implantation step survives into a production sequence. A score above 3 would be inventing evidence.

**TLDR: One clean device-level demonstration in the source set, with depth control behaving as intended and matching simulation.**

## Drivers (unscored)

Nothing in the supplied material addresses implanter supply, tool cost, installed base, capex cycles, or the size of any demand pool. The nearest thing to a demand signal is the stated motivation of the erbium work, which is to provide a pathway for integrating efficient active light sources into CMOS-compatible photonic devices, and the observation that contact-free doping metrology is being developed for SiC, Si and GaN layer stacks, implying commercial interest in doped-layer characterisation.

That is an inference about adjacent interest, not a driver assessment. Supply-side and demand-side quantification would both be fabricated if scored here, so the score is null.

**TLDR: The sources contain no market, capacity or cost information at all.**

## Novelty (3/5)

The competitive comparison the sources actually permit is on placement control. Implantation delivers a tunable stopping depth, and in the erbium work that translated into a four-fold emission difference between 20 nm and 80 nm ion range. Solution and growth routes in the same source set have no equivalent knob: wet infiltration relies on liquid trapped in pores and confirms doping only by mass increase and Rietveld phase analysis after sintering, and spin-coated sol-gel doping is described as a non-vacuum method with no depth targeting. Where uniform bulk doping is the goal, those routes are cheaper and implantation offers no advantage.

The interesting challenge comes from the electron-beam methane route for carbon doping of hBN, which is explicitly motivated by the claim that existing approaches lack nanoscale precision and control over the carbon supply, and which confines 84 plus or minus 7 per cent of carbon-rich regions to the irradiated area. For single-defect engineering in two-dimensional hosts, that is a genuine rival on precision. Implantation's edge is therefore scale-dependent: strong at the wafer and nanophotonic-layer scale, contested at the single-atom scale.

**TLDR: Better than the alternatives specifically on depth and lateral placement; the sources also show a rival technique claiming finer spatial control.**

## Diffusion (unscored)

The sources do not describe anyone adopting implantation in production, nor the barriers to doing so. The one adoption-relevant statement is that the erbium-implanted metasurface approach is presented as a route to CMOS-compatible photonic devices, which suggests the authors see no fundamental process-integration blocker. Against that, the same work requires a post-implant thermal anneal to realise the enhancement, and thermal budget is a classic integration constraint that the source does not quantify.

A secondary and indirect barrier visible in the set is measurement. Work on terahertz spectroscopy introduces a sensitivity metric precisely because the doping ranges accessible to contact-free characterisation are not obvious, and maps this for SiC, Si and GaN in realistic multilayer stacks. Doped-layer process control depends on metrology that is still being bounded. None of this adds up to a defensible diffusion score.

**TLDR: No adoption evidence in the sources; only a stated compatibility argument.**

## Impact (3/5)

If implantation reliably places rare-earth emitters at optimal depth inside resonant dielectric structures, the payoff is an on-chip light source in a material system already used for passive photonics. The measured numbers are meaningful: roughly 18-fold PL enhancement at telecom wavelength at room temperature, near ten-fold lifetime reduction, and four-fold emission gain from depth optimisation alone. Room-temperature operation matters here, because much of the neighbouring quantum-photonics work in the source set operates at cryogenic temperatures, for example transduction in Yb-doped Y2SiO5 at 30 mK.

The scoring limit is scope. Photoluminescence enhancement is not gain, and the sources do not report a working amplifier, laser or link. Value beyond this single application, in power devices, batteries, spintronics or oxide electronics, is not addressed by any supplied source; those all use non-implantation doping routes. Hence a mid score with narrow support rather than a high one.

**TLDR: Real value in the one demonstrated application, unquantified beyond it.**

## Timing Now (0-2yr)

The erbium metasurface work was published in May 2026 and reports finished, annealed, characterised structures with simulation agreement, so implantation as a research and prototyping step is available now. There is no waiting period on the technique itself.

What is not now is the product. Nothing in the sources shows an implanted-emitter device delivering optical gain, a data link or a manufactured part, and no timeline is given. Assessing when integrated Er:Si3N4 sources reach fabs would require information the sources do not contain, so the band applies to the process, not to the applications built on it.

**TLDR: The process is already being used to produce measured device-level results; the applications it enables are further out.**

## Overrated or underrated? Fairly rated

Ion implantation here behaves like the infrastructure technique it is: nobody is claiming it as the breakthrough, and the one paper that uses it treats it as the means to a photonic result rather than the result itself. That framing looks correct. Where placement matters, implantation is the only tool in the supplied source set that gives a tunable depth profile, and the four-fold emission change between 20 nm and 80 nm ion range shows the knob has real leverage. Where placement does not matter, the same source set is full of cheaper routes: liquid infiltration, spin coating, chemical getters and in-growth incorporation. That is a stable, well-understood division of labour, not a mispricing.

The caveat an investor should hold onto is that this assessment rests on one directly relevant source. Anyone treating implantation as a differentiated asset should ask what specifically requires beam placement in their flow, because the answer is often nothing, and the electron-beam methane result shows that even the precision argument is being contested at the atomic scale.

## Prediction

By 31 December 2028, published work will report an Er-implanted Si3N4 structure demonstrating net optical gain or lasing at telecom wavelength using implantation-depth optimisation; if instead the leading Er:Si3N4 active-photonics results by that date use non-implanted rare-earth incorporation, this prediction fails.

## Evidence base

- Er3+ implanted into Si3N4 nanocylinder metasurfaces gave roughly 18-fold room-temperature PL enhancement at 390 nm radius after thermal annealing, matching simulation, reported 5 May 2026.
- PL intensity in the same work depended strongly on implantation depth, with a four-fold emission increase going from 20 nm to 80 nm ion range, and a near ten-fold luminescence lifetime reduction attributed to the Purcell effect.
- A rival precision-doping route, electron-beam irradiation in low-pressure methane, confined 84 plus or minus 7 per cent of carbon-rich regions to the irradiated area of hBN, published 28 May 2026.
- Non-beam doping routes remain productive: wet nitric-acid infiltration co-doped pre-sintered 3YSZ discs with Sc, Mg and Y, confirmed by mass increase and Rietveld phase analysis, 8 May 2026.
- Chemical rather than beam doping reached carrier concentrations of about 10^21 cm^-3 in EuTiO3-delta using CaH2 as an oxygen getter, with a maximum Curie temperature near 11 K, 8 May 2026.
- Contact-free doping metrology is still being bounded: a sensitivity metric for reflection terahertz time-domain spectroscopy was introduced for SiC, Si and GaN in up to three-layer stacks, 5 May 2026.

## Open questions

- What fraction of implanted Er in Si3N4 is optically active after annealing, and does the four-fold emission gain from 20 nm to 80 nm ion range reflect activation, damage recovery, or purely the overlap with the Mie resonance field profile?
- What thermal budget does the required post-implant anneal impose, and is it compatible with a CMOS photonics back-end flow?
- At what feature scale does implantation lose to beam-induced chemical doping such as the electron-beam methane route, and does that boundary move with host material thickness?
- Can implanted doping profiles in realistic multilayer stacks be verified non-destructively, given that the accessible doping ranges for contact-free terahertz characterisation are still being mapped?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
