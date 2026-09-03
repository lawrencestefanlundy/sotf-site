---
type: concept
slug: graphene
canonical_name: Graphene
aliases: []
kind: technology
parent_concepts:
- materials
- substrates
related_concepts: []
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2026-05-29-blairs-been-on-the-tokens-again]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
scorecard:
  viability: 3
  drivers: null
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Unclear
  verdict: Too early to say
scorecard_status: draft
mention_count: 309
sources_7d: 10
sources_30d: 16
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-24-thermal-stack-arms-race-diamond-heat-spreaders-companies-in
  title: Diamond Heat Spreaders Companies in 2026
  date: '2026-06-24'
  kind: web
- slug: 2026-06-23-inbrain-graphene-first-in-human
  title: 'InBrain Neuroelectronics: world-first-in-human graphene neural interface study, $50M Series B, FDA Breakthrough Device, Merck KGaA partnership'
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-thermal-stack-arms-race-ai-computing-power-fuels-diamond
  title: AI Computing Power Fuels 'Diamond Cooling' Multi-Billion-Dollar Race
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-04-fulfilling-the-promise-of-graphene---enterprisecamacuk
  title: Fulfilling the promise of graphene - enterprise.cam.ac.uk
  date: '2026-06-04'
  kind: web
- slug: 2026-05-29-blairs-been-on-the-tokens-again
  title: Blair's Been On The Tokens Again
  date: '2026-05-29'
  kind: substack
neighbors: []
---
**Graphene is a single atomic layer of carbon whose Dirac-like electrons and mechanical robustness make it the default substrate and tuning platform across 2D materials research, but the May 2026 literature shows it functioning mainly as a laboratory building block rather than a deployed material.**

## Summary

The current research literature uses graphene in four distinct roles. First, as an electronic substrate and support: graphene-supported dual-atom catalysts for water splitting, where the carbon/nitrogen coordination around the metal pair is the design variable, and graphene on Ir(111) as a growth template for molecular beam epitaxy of MoS2. Second, as an active optoelectronic layer, for example dual-layer graphene electro-optic phase modulators on silicon nitride waveguides for cryogenic photonic quantum processors. Third, as a correlated-electron platform: rhombohedral and twisted graphene stacks where flat bands and Berry curvature set the size of Cooper pairs and where moiré superlattices host Brown-Zak fermions detectable in nonlinear Hall oscillations from fields as low as 0.5 T. Fourth, as a passive surface or filler: a coating that reduces rarefied-air drag and an additive that refines magnesium grain structure for hydrogen storage.

The parameters that decide outcomes differ by role. For devices it is fabrication: sub-10 nm nanoribbon FETs have been written by AC-bias electrochemical AFM lithography, but the authors state plainly that integration into conventional transistor technology remains hindered by high fabrication costs and complex processing. For heterostructures it is the twist angle: 0 degree WS2-graphene stacks show efficient charge separation under 3.1 eV excitation, while at 30 degrees electron and hole transfer proceed at similar rates, cancelling the useful asymmetry. For photonics it is graphene quality alongside waveguide geometry and spacer permittivity. For coatings it is defect density and corrugation, which raise momentum accommodation, though graphene reportedly holds up at experimentally relevant defect densities.

## Viability (3/5)

There is no doubt the substance works as a laboratory material: it is grown epitaxially and used as a template for MBE growth of MoS2, patterned to sub-10 nm feature sizes into working FETs, measured by trARPES in epitaxially grown WS2-graphene heterostructures at controlled twist angles, and probed transport-wise in moiré devices down to 0.5 T onset fields. On the bulk side, high-pressure torsion of magnesium with graphene yields composites with measured desorption kinetics at 623 K and a desorption activation energy of 145 plus or minus 2 kJ/mol.

Against that, several of the most commercially suggestive claims in this source set are theory or simulation rather than fabricated hardware. The cryogenic phase modulator work is explicitly a systematic theoretical investigation combining electromagnetic simulation with a Kubo description of graphene conductivity; the dual-atom catalyst library of 228 structures with 24 active candidates is a DFT and machine-learning screen, not a tested electrode; the drag reduction result is molecular dynamics. A 3 reflects a material that unambiguously works with applications that are mostly still on paper.

**TLDR: The material itself is routine in labs; the device-level claims are split between real measurements and simulation only.**

## Drivers (unscored)

Every source here is an arXiv physics or materials paper. None reports production capacity, price per unit area, procurement volumes, company activity, or investment. Demand pull can only be inferred from stated motivations, which is weak evidence: photonic quantum computing needing low-loss cryogenic modulators, cost-effective overall water splitting, next-generation ultra-miniaturised transistors, drag on satellites in rarefied atmospheres, and magnesium hydrogen storage. That is a list of researcher intentions, not a demand signal.

One supply-side observation is supportable: the tooling ecosystem is maturing, with open software for generating commensurate supercells of twisted multilayer 2D materials and new real-space linear-scaling methods for driven, disordered graphene transport. That lowers the cost of design iteration, but it says nothing about whether anyone is buying. Score withheld.

**TLDR: The sources contain no market, funding, capacity or supply-chain information at all.**

## Novelty (3/5)

The clearest like-for-like comparisons in this set are: graphene coating on alpha-Al2O3(0001) lowers the tangential momentum accommodation coefficient for N2 relative to the bare surface, shifting scattering towards specular reflection, with the effect strengthening up to 900 K and benchmarked against graphite; AC electrochemical AFM lithography is presented as lower cost and electrode-free relative to photolithography and electron-beam lithography for sub-10 nm graphene patterning; and graphene composites cut magnesium grain size to 10-500 nm versus 850 nm for high-pressure-torsion magnesium alone, shifting the rate-controlling step from interfacial reaction to atomic diffusion. The direction of improvement is stated in each case; the magnitude relative to the deployed alternative usually is not.

Graphene is also increasingly a benchmark rather than a frontier. Rhombohedral beta-Cu2Se is proposed as a Dirac semimetal with Fermi velocities potentially exceeding graphene and with topologically protected Fermi arc surface states resilient to back- and side-scattering. Photonic honeycomb slabs and polariton lattices reproduce graphene-like Dirac dispersion in engineered platforms, and graphene-like motifs appear as one component of amorphous monolayer BCN. Where graphene remains genuinely distinctive in these sources is in stacked and twisted form, where Berry curvature can dominate the geometric lower bound on Cooper pair size and give pair sizes comparable to experimentally inferred coherence lengths in rhombohedral graphene.

**TLDR: Real comparative advantages are claimed in several niches, but almost none are quantified against the incumbent.**

## Diffusion (2/5)

The nanoribbon paper is explicit that despite extensive effort, integration of narrow GNR FETs into conventional transistor technology remains hindered by high fabrication costs and complex processing requirements. The remedy offered is direct-write electrochemical AFM lithography, which relies on the high-precision positioning capability of an AFM tip. That removes electrodes and mask cost but is a point-by-point writing method, so nothing in the source establishes throughput compatible with volume manufacturing.

Other roles face different barriers of the same kind. Heterostructure performance depends on twist angle control, with 0 and 30 degree stacks behaving qualitatively differently for charge separation, which means wafer-level angular alignment is a prerequisite for any optoelectronic product built this way. Modulator designs depend on graphene quality as an explicit optimisation variable alongside geometry and dielectric choice. On the more forgiving end, the coating application tolerates defects: graphene retains its drag-reducing performance at experimentally relevant defect densities, and the magnesium composite route uses bulk severe plastic deformation rather than lithography. Passive uses will diffuse before electronic ones.

**TLDR: Fabrication and integration are the named blockers, and the proposed fix is a serial scanning-probe process.**

## Impact (3/5)

The breadth is real. Within a single fortnight of literature, graphene appears as the support that makes atomically dispersed dual-atom catalysts tunable for both hydrogen and oxygen evolution, as the electro-optic layer that could shrink cryogenic phase modulators for photonic quantum computing while keeping insertion loss low, as the host for flat-band superconductivity whose coherence length is set by quantum geometry, as a channel material with a size-dependent band gap for ultra-miniaturised transistors, and as a drag-reducing surface for objects in rarefied atmosphere. A substrate that is simultaneously a catalyst support, an optical switch, a correlated-electron playground and a mechanical additive has unusually high option value.

What is missing is any figure that converts a physical effect into system-level value: no efficiency gain for an electrolyser, no drag coefficient reduction for a satellite orbit lifetime, no energy per bit for a modulator, no storage capacity in weight per cent for the magnesium composite. The hydrogen storage result actually shows a limit to the mechanism: the desorption activation energy stays at 145 plus or minus 2 kJ/mol regardless of grain or interphase boundaries, so the improvement comes from the frequency factor rather than from lowering the thermodynamic barrier. A 3 is the ceiling this evidence supports.

**TLDR: Broad optionality across catalysis, photonics, quantum devices and storage, but no source quantifies value against an incumbent system.**

## Timing Unclear

As a research substrate and characterisation benchmark, graphene is already in use now: it is the growth template in MBE studies, the test system for new diffraction imaging formalisms and for electron-irradiation simulations that identify quantum-only backscattering effects around 400 eV incident energy which diminish above 600 eV, and the reference against which new Dirac materials are pitched.

For everything else the sources provide no roadmap, no pilot line, no scale-up plan and no cost figures, so any band assigned to nanoribbon logic, cryogenic modulators or graphene-supported electrolysis would be invented rather than assessed. The internal ordering is visible even if absolute dates are not: passive bulk uses such as coatings and metal-matrix composites are experimentally demonstrated with defect tolerance and conventional processing, while the electronic and photonic uses still depend on unsolved patterning and alignment problems.

**TLDR: Already routine as a laboratory substrate; the sources give no basis for dating any of the application-level claims.**

## Overrated or underrated? Too early to say

Judged against this evidence base, graphene in 2026 is best understood as infrastructure for materials science rather than as a product. Its most defensible current value is that it makes other things measurable and tunable: a coordination scaffold for single- and dual-atom catalysts, a template for epitaxial growth of transition metal dichalcogenides, and a stack whose twist angle converts an abstract quantum geometry into a measurable transport signature. On that reading it is underrated, because scaffolding rarely gets credit.

As the wonder material that replaces silicon channels, the picture in these sources is unchanged from the long-standing one and is not encouraging: the gap problem forces you into sub-10 nm ribbons, and the fabrication route offered to get there is scanning-probe direct write. Because the source set contains no commercial, cost or capacity information whatsoever, a verdict of overrated or fairly rated cannot be earned here. The honest call is that these 18 papers can characterise the physics but cannot adjudicate the hype.

## Prediction

By 31 May 2028, an experimentally fabricated dual-layer graphene electro-optic phase modulator on a silicon nitride waveguide will have been reported with measured insertion loss and phase shift under cryogenic operation, rather than only simulated as in.

## Evidence base

## Open questions

- Can the sub-10 nm graphene nanoribbon FETs written by AC electrochemical AFM lithography be produced at more than one device at a time, and what is the device-to-device variation in band gap and on/off ratio?
- Do the 24 graphene-supported dual-atom catalysts identified by constant-potential DFT screening survive synthesis and show the predicted bifunctional activity and stability in an operating electrolyser?
- What drag coefficient or orbital lifetime change does the simulated reduction in tangential momentum accommodation translate into for a real coated surface, and does the coating survive atomic oxygen and thermal cycling?
- Is wafer-scale twist-angle control to within the tolerance that distinguishes 0 degree from 30 degree charge-separation behaviour in WS2-graphene achievable outside epitaxial growth on selected substrates?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
