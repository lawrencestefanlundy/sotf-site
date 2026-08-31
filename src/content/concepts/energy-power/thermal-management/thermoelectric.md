---
type: concept
slug: thermoelectric
canonical_name: Thermoelectric
aliases: []
kind: technology
parent_concepts:
- energy-power
- ai-thermal-management
related_concepts: []
sources:
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-06-22-tim-approaches-full-sweep]]'
frontier:
- Can high-entropy Heusler chemistry push average zT materially above the reported 0.3 over 300 to 500 K without reintroducing cost or toxicity, and what module conversion efficiency does that translate into 2026 06 16 high entropy fe2val based thermoelectric modules with improv?
- Do the bulk Pt-coated YIG composites actually deliver volumetric power scaling in a multi-centimetre device, and how does that power density compare with a longitudinal Bi2Te3 module of the same volume 2026 07 22 trans scale spin seebeck effect in nanostructured bulk compo?
- How many of the DFT-predicted candidates in this literature, such as CrSi2N4, beta2SnGeX6 or XZnBi, are ever synthesised, and how far do measured power factors fall short of the calculated values 2026 05 15 strain enhanced hydrogen evolution electrical optical and th 2026 07 01 layered xznbi x rb cs with pudding mold bands complex fermi ?
- Can an anomalous Nernst material combine bipolar operation with a Curie temperature well above room temperature, given that the YCo3 demonstration sits below 225 K 2026 05 29 topological lifshitz transition induced bipolarity of anomal?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 60
last_reorg_date: '2026-05-13'
scorecard:
  viability: 4
  drivers: null
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 2
sources_30d: 12
recent_mentions:
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
neighbors: []
---
**Thermoelectrics convert a temperature difference directly into voltage with no moving parts; the physics is settled and modules are being built from cheap Heusler and Bi2Te3 alloys, but conversion figures of merit remain low enough that the technology stays confined to niches while a newer transverse, spin-based branch is still at the laboratory-demonstration stage.**

## Summary

A thermoelectric material generates a voltage when its two ends are held at different temperatures (the Seebeck effect) and pumps heat when a current is passed through it (the Peltier effect). Performance is captured by the dimensionless figure of merit zT, which rises with the Seebeck coefficient and electrical conductivity and falls with thermal conductivity. These three quantities are coupled in most solids, so materials work consists of decoupling them: engineering band structures with high degeneracy or unusual dispersion to raise the power factor, while scattering phonons to suppress the lattice thermal conductivity. Both levers appear repeatedly in the current literature. High-entropy engineering of Fe2VAl full Heuslers, combining heavy-element doping with controlled off-stoichiometry to create substitutional disorder on every lattice site, yields a lattice thermal conductivity of about 2.3 W m-1 K-1, among the lowest reported for that family, and an average zT of roughly 0.3 between 300 and 500 K. On the band-structure side, layered Zintl compounds XZnBi (X = Rb, Cs) are predicted to combine six degenerate hole pockets with a quasi-two-dimensional pudding-mould conduction band that mixes heavy and light electron masses.

The workhorse chemistry remains bismuth telluride. Recent work tunes n-type Bi2Te3 through selenium doping and annealing to control carrier concentration and suppress the bipolar effect over a wide temperature range, and formulates Bi2Te3/Sb2Te3 nanoparticles into PMMA-based hybrid inks with a dithiol binder, with 80 per cent nanoparticle loading giving the best performance and finite-element modelling used to set the p- and n-leg area ratio. Alongside these, a large volume of first-principles screening proposes new candidates: the lead-free double perovskites beta2SnGeX6 with bandgaps tunable from 1.44 down to 0.64 eV by halogen substitution, and the 2D monolayer CrSi2N4, for which Boltzmann transport calculations predict a room-temperature n-type power factor of 3.5 mW m-1 K-2. Cheaper computational routes are emerging in parallel, including deformation-potential and machine-learning interpolation schemes that reproduce electron-phonon transport from roughly 10 to 100 first-principles matrix elements per band and phonon mode, and a substitutional atomic distance model for alloy lattice thermal conductivity validated against SiGe and InGaAs.

A structurally different branch uses transverse geometries, where the electric field appears perpendicular to the heat flow. Spin caloritronics, reviewed as now transitioning from fundamental condensed-matter physics towards materials science and engineering, covers the spin Seebeck effect and the anomalous Nernst effect. Transverse devices avoid the series-connected pillar architecture of conventional modules, but have been limited by spin and magnon diffusion lengths to thin films; nanostructured bulk composites of Pt-coated yttrium iron garnet powders, made by dynamic powder sputtering and low-temperature sintering, have now shown isotropic bulk-scale spin Seebeck signals with power analysis pointing to volumetric rather than diffusion-limited scaling. Anomalous Nernst materials are being engineered by composition: Gd-Co-Pt ternary films reach a heat-flux sensitivity of about 0.24 micrometres per amp, with Pt driving a sign reversal of the Nernst coefficient, and the kagome magnet YCo3 shows a bipolar anomalous Nernst effect driven by a topological Lifshitz transition below its 225 K Curie temperature, relevant to thermopiles that need both signs from one material.

The deciding parameters are therefore: zT and the temperature window over which it is sustained; material cost, toxicity and scalability of synthesis; module-level losses at contacts and interfaces; and, for the transverse branch, whether large enough transverse coefficients can be found in materials that also survive bulk fabrication.

## Viability (4/5)

This is not a question of whether the physics works. The sources include a complete thermoelectric module fabricated from optimised high-entropy Fe2VAl alloys, with scaled-up batches produced by hot pressing whose properties agreed closely with laboratory-scale samples, and module characterisation showing improved conversion efficiency. Printed Bi2Te3/Sb2Te3 hybrid generators with geometry optimised by finite-element modelling have also been demonstrated. Reproducibility from laboratory to scaled batch is the specific risk that usually kills materials work, and one source addresses it directly.

The qualification is the magnitude. An average zT of about 0.3 across 300 to 500 K is a low-efficiency device by any energy-conversion standard, chosen because the material is cheap, robust and non-toxic rather than because it is good. Much of the rest of the corpus is first-principles prediction, not measurement: CrSi2N4, beta2SnGeX6 and XZnBi are computed candidates with no synthesis reported. The transverse branch is at a lower readiness level again: bulk spin Seebeck composites are a first demonstration of scalable geometry rather than a competitive generator, and the ZT of roughly 0.75 reported for Majorana-quantum-dot structures is a model calculation of the electronic figure of merit in a mesoscopic device, not a power source.

**TLDR: The effect is unambiguous and full modules have been built from scaled-up material batches, but the efficiency numbers on show are modest.**

## Drivers (unscored)

The demand-side rationale is asserted consistently across the corpus: direct conversion of waste heat into electricity for sustainable energy applications, with practical deployment said to require high efficiency combined with low cost, non-toxicity and scalability, and thermoelectrics described as a complementary renewable source needing energy-efficient, low-waste processing routes for broader adoption. Adjacent pull comes from sensing and photonics rather than power: heat-flux sensors based on the anomalous Nernst effect and waveguide-integrated graphene photodetectors that rely on the photo-thermoelectric effect for zero-bias, broadband operation.

**TLDR: Sources state the motivation but contain no market, policy or funding evidence, so no defensible score.**

## Novelty (3/5)

Judged against the existing thermoelectric baseline, the longitudinal materials work is refinement rather than a break. Bi2Te3 remains the reference system, tuned by selenium doping and annealing. The clearest quantified advance is high-entropy engineering of Fe2VAl, which produces one of the lowest lattice thermal conductivities reported for full-Heusler systems at about 2.3 W m-1 K-1; the resulting zT of about 0.3 is better than an unoptimised Heusler but not against the field. Computational methods are the quieter novelty: obtaining electron-phonon-limited transport from roughly 10 to 100 first-principles matrix elements instead of dense-grid interpolation is a genuine cost reduction in screening.

The transverse branch is what is new in kind. Conventional spin Seebeck devices are confined to nanoscale thin films because spin and magnon diffusion lengths cap the output; three-dimensional Pt-coated YIG composites are claimed to break that constraint and enable volumetric scaling. Anomalous Nernst design has moved from binary to ternary composition space, with sign reversal available as a design variable and, in YCo3, obtainable from a single material via a temperature-driven topological Lifshitz transition, which matters for thermopiles where switching the voltage sign raises output. Two results are new physics with no demonstrated device gain yet: intrinsic nonlinear Seebeck, Nernst and mixed-directional responses observed up to room temperature in Td-WTe2 and TaIrTe4 without magnetic fields or magnetic materials, and a predicted surface-dominated anomalous Nernst response in MnBi2Te4 multilayers that does not decay with slab thickness. The review of the field describes it as at a turning point from fundamental physics towards materials science, which is an accurate description of something not yet novel at the product level.

**TLDR: Incremental in the workhorse chemistries; genuinely new in transverse and nonlinear thermoelectric physics, with the device advantage still unproven.**

## Diffusion (2/5)

The adoption barriers are visible in the sources themselves. Efficiency is first: an average zT of about 0.3 restricts use to settings where the heat is free and reliability or absence of moving parts is worth more than conversion efficiency. Cost, toxicity and scalability are named explicitly as prerequisites for practical deployment in the same work, which is why the effort goes into Fe2VAl rather than telluride chemistry. Processing is being addressed: polymer-matrix inks with dithiol binders give a low-energy, low-waste route to films and devices, with percolation studies fixing the loading and finite-element modelling fixing the leg geometry.

For the transverse branch the barriers are more basic. Devices have been limited to thin-film architectures with restricted output power, and the bulk composite route is a first demonstration of mechanical integrity, continuous Pt percolation channels and isotropic signal, not of competitive power delivery. Operating temperature is another constraint where the physics depends on magnetic order: YCo3 has a Curie temperature of about 225 K, so its bipolar Nernst behaviour is below room temperature. The one place diffusion looks near-term is in components rather than generators, where the photo-thermoelectric effect underpins graphene photodetectors already being integrated into silicon photonics waveguides. No source reports a deployed system, a production volume or a cost per watt.

**TLDR: Manufacturing routes are being demonstrated, but efficiency is too low and the sources show no deployment.**

## Impact (3/5)

The honest ceiling on near-term impact is the figure of merit. At zT around 0.3, a module recovers a small fraction of the available exergy, and the value proposition rests on installed cost and robustness rather than yield. The transverse and nonlinear results extend what is physically possible, including a route to thermoelectric response in systems where the bulk contribution is symmetry-forbidden and nonreciprocal control of thermoelectric response for thermal management, but they do not yet change the energy arithmetic. A middling score reflects a wide but shallow value surface on the current evidence.

**TLDR: Broad application surface across waste heat, sensing and photonics, but nothing in the sources quantifies the value and current efficiency caps it.**

## Timing Soon (2-5yr)

The near-term clock runs on the conventional branch. Scaled-up Fe2VAl batches whose properties match laboratory samples, assembled into a characterised module, is a pre-commercial milestone rather than a physics result, and printable Bi2Te3/Sb2Te3 inks with FEM-optimised leg geometry point at low-cost fabrication within the same window. Faster computational screening also compresses the materials discovery loop, though the many DFT candidate papers in this corpus have not been synthesised and most will not be.

Spin caloritronics is on a different timeline. Its own review positions it as only now transitioning from fundamental condensed-matter physics towards materials science and engineering applications, and the flagship bulk result establishes a platform rather than a device. Room-temperature nonlinear thermoelectric effects were observed for the first time in 2026, which places any application at least a decade out. The exception is photonics, where the photo-thermoelectric effect is already the operating mechanism of waveguide-integrated detectors and improvements land immediately.

**TLDR: Cheap longitudinal modules and printed generators are at the pilot stage now; transverse and spin-based conversion is a research programme, not a product path.**

## Overrated or underrated? Fairly rated

Thermoelectrics are treated as a real but bounded technology, and that is what the evidence supports. The best module result here pairs cheap, non-toxic, scalable Heusler chemistry with an average zT of about 0.3 over 300 to 500 K: useful where heat is free and maintenance is expensive, not a route to grid-relevant waste-heat recovery. The very large volume of first-principles candidate papers in this corpus, spanning 2D nitrides, halide double perovskites and layered Zintls, should be discounted heavily; predicted power factors have a poor record of surviving synthesis, contact resistance and module assembly, and none of these compounds is reported as made.

Where the rating is arguably too low is the transverse branch, but as a research direction rather than an energy technology. Breaking the diffusion-length limit that has confined spin Seebeck devices to thin films, obtaining both Nernst polarities from a single material and finding a surface response that does not decay with thickness are all structural changes to what transverse devices can be built from. The near-term payoff is much more likely to be heat-flux sensors and photonic detectors than generators, and anyone pricing spin caloritronics as an energy play is ahead of the evidence.

## Prediction

By July 2029 no transverse thermoelectric device based on the spin Seebeck or anomalous Nernst effect will have been reported at module scale with a measured heat-to-electricity conversion efficiency, as opposed to a transverse coefficient, sensitivity or power-density figure.

## Evidence base

- 16 June 2026: high-entropy engineered Fe2VAl full Heuslers reach a lattice thermal conductivity of about 2.3 W m-1 K-1, among the lowest reported for the family, giving an average zT of roughly 0.3 from 300 to 500 K, with a full module built from hot-pressed scaled-up batches.
- 22 July 2026: nanostructured bulk composites of Pt-coated yttrium iron garnet powders show isotropic spin Seebeck signals at bulk scale, with power analysis indicating volumetric generation beyond the diffusion-limited thin-film geometries that have constrained the effect until now.
- 7 July 2026: Bi2Te3/Sb2Te3 hybrid inks in a PMMA matrix with a hexanedithiol binder give best performance at 80 per cent nanoparticle loading, with finite-element modelling used to optimise the p- and n-leg cross-sectional area ratio.
- 16 June 2026: Gd-Co-Pt ternary films reach an anomalous Nernst heat-flux sensitivity of about 0.24 micrometres per amp, with Pt inducing a sign reversal of the Nernst coefficient and Gd reducing thermal conductivity.
- 27 July 2026: intrinsic nonlinear Seebeck, Nernst and mixed-directional thermoelectric responses are observed up to room temperature in Td-WTe2 and TaIrTe4 without magnetic fields or magnetic materials.
- 5 May 2026: a field review places spin caloritronics at a turning point, transitioning from fundamental condensed matter physics to materials science and engineering application.

## Open questions

- Can high-entropy Heusler chemistry push average zT materially above the reported 0.3 over 300 to 500 K without reintroducing cost or toxicity, and what module conversion efficiency does that translate into?
- Do the bulk Pt-coated YIG composites actually deliver volumetric power scaling in a multi-centimetre device, and how does that power density compare with a longitudinal Bi2Te3 module of the same volume?
- How many of the DFT-predicted candidates in this literature, such as CrSi2N4, beta2SnGeX6 or XZnBi, are ever synthesised, and how far do measured power factors fall short of the calculated values?
- Can an anomalous Nernst material combine bipolar operation with a Curie temperature well above room temperature, given that the YCo3 demonstration sits below 225 K?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
