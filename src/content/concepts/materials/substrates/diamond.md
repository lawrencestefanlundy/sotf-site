---
type: concept
slug: diamond
canonical_name: Diamond
aliases: []
kind: technology
parent_concepts:
- materials
- substrates
related_concepts:
- wide-bandgap-semiconductors
- gallium-nitride
- power-electronics
- quantum-sensing
- photonics
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-05-31-three-underrated-technologies-from]]'
scorecard:
  viability: 4
  drivers: null
  novelty: 4
  diffusion: 3
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 326
sources_7d: 3
sources_30d: 9
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-10-quantumdiamonds-raises-91m-in-eu-chips-act-first-for-its-dia
  title: QuantumDiamonds raises €91M in EU Chips Act first for its diamond chip scanner - Dealroom
  date: '2026-07-10'
  kind: web
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-06-24-thermal-stack-arms-race-diamond-heat-spreaders-companies-in
  title: Diamond Heat Spreaders Companies in 2026
  date: '2026-06-24'
  kind: web
- slug: 2026-06-23-evtol-certification-status-joby-stage4-archer-volocopter
  title: eVTOL type-certification status Q1-Q2 2026 — Joby Stage 4, Archer Stage 3, Volocopter pivot
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-thermal-stack-arms-race-ai-computing-power-fuels-diamond
  title: AI Computing Power Fuels 'Diamond Cooling' Multi-Billion-Dollar Race
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
neighbors:
- slug: wide-bandgap-semiconductors
  name: Wide-Bandgap Semiconductors
  path: /materials/substrates/wide-bandgap-semiconductors/
  macro: materials
- slug: gallium-nitride
  name: Gallium Nitride
  path: /energy-power/power-electronics/gallium-nitride/
  macro: energy-power
- slug: power-electronics
  name: Power Electronics
  path: /energy-power/power-electronics/power-electronics/
  macro: energy-power
- slug: quantum-sensing
  name: Quantum Sensing
  path: /sensing/quantum-sensing/quantum-sensing/
  macro: sensing
- slug: photonics
  name: Photonics
  path: /photonic-systems/pic-platforms/photonics/
  macro: photonic-systems
---
**Diamond is being used in two distinct technical roles, as a host crystal for nitrogen-vacancy spin sensors that now deliver sub-picotesla magnetometry and measurements no other probe can make, and as a wide-bandgap semiconductor substrate whose devices still lack the circuit models needed to design with them.**

## Summary

Diamond appears in this knowledge base as a substrate material with two largely unconnected engineering stories. The first is diamond as a host lattice for point defects, above all the negatively charged nitrogen-vacancy (NV) centre, whose electron spin can be optically initialised and read out at room temperature. This makes a diamond chip into a magnetometer, an electric-field and temperature probe, and a radiofrequency detector, with spatial resolution set by the sensor-to-target distance rather than by optical wavelength. The second is diamond as a semiconductor: a hydrogen-terminated diamond surface supports a two-dimensional hole gas (2DHG) that can be gated into a field-effect transistor, which is the route most often proposed for diamond power and RF electronics.

The parameters that decide the sensing story are readout contrast, dynamic range, and how close the defect can sit to the target. Ensembles have historically been limited to a few percent optical contrast and a few microtesla of dynamic range; a laser-threshold approach that places NV centres inside a laser cavity reports 100 percent contrast, output up to 50 mW and photon-shot-noise-limited sensitivity below 400 fT/sqrt(Hz) on all vector components. A separate protocol that deliberately exploits NV charge-state ionisation, normally treated as a parasitic effect, raises readout contrast by 17 percent relative and cuts initialisation error by more than half. Supporting engineering is being worked in parallel: microwave field homogeneity across a large spin ensemble has been optimised by comparing five field-forming geometries and validating a barrel-shaped coil experimentally against a planar antenna, and the power sensitivity of NV radiofrequency detectors is shown to scale inversely with the physical size of the RF-spin interface, so smaller waveguides and loops win.

The electronics story is at a much earlier stage. Hole mobility in diamond 2DHG FETs has been assessed almost entirely by Hall measurement; a 2026 IEEE Access paper instead applies the standard silicon MOS characterisation toolkit, quasi-static C-V, effective normal field formulations and Arrhenius barrier extraction, to extract effective mobility and conduction barriers and to compare against silicon inversion and accumulation layers. It also reports an unexpected GIDL-like leakage mechanism despite the absence of intentional doping **Walker 2026 Diamond 2Dhg Conduction Mechanism**. The explicit purpose is to make extractable, robust device models possible, which is the prerequisite for any circuit design at all.

A caution on the evidence base: several sources retrieved under this concept do not concern the material. The diamond norm is a distance measure between quantum channels and appears in error-budget and verification work, and the diamond phase in block copolymer network morphology is a geometry, not carbon. These carry no weight here.

## Viability (4/5)

The semiconductor branch does not yet support the same score and pulls the composite down. The state of play described in the sources is that the community has been measuring mobility by Hall effect and is only now importing silicon's characterisation and modelling discipline, with an unexplained GIDL-like leakage path appearing in undoped structures **Walker 2026 Diamond 2Dhg Conduction Mechanism**. A device class without extractable compact models cannot be designed with, whatever the intrinsic material properties. Score 4 reflects strong demonstrated results on sensing and an explicit acknowledgement that the electronics case is unresolved in the available material.

**TLDR: Diamond NV sensing demonstrably works and is producing physics results; diamond as a transistor substrate is still pre-model.**

## Drivers (unscored)

None of the supplied sources addresses market pull, procurement, synthetic diamond wafer supply, pricing, or programme funding. Application areas are named as motivations only: inertial sensing and fundamental physics experiments for optically detected nuclear magnetic resonance, nanoscale metrology generally, and externally delivered RF signal detection. The only near-commercial statement is that extractable device models are the step between a materials result and anything fundable **Walker 2026 Diamond 2Dhg Conduction Mechanism**, which is an argument about sequencing rather than evidence of demand.

On the supply side there is characterisation work on natural stones and on nanodiamond powders, including nitrogen A and C centre distributions and vacancy-cluster Y-defects in a Yakutian diamond and infrared spectra of hydrogenated nanodiamonds from 2.6 to 30 nm, but neither speaks to production volume or material availability. No score is defensible.

**TLDR: The sources are entirely technical; they say nothing about demand, cost, wafer supply or funding.**

## Novelty (4/5)

The comparisons here are specific. Against the prior state of NV ensemble magnetometry, typically a few percent optical contrast and a few microtesla dynamic range, laser threshold magnetometry reaches 100 percent contrast, meaning the laser can be switched off entirely on magnetic resonance, with output up to 50 mW and sensitivity better than 400 fT/sqrt(Hz), improving super-linearly with contrast. The charge-state purification protocol is a smaller but cheap gain, 17 percent relative contrast and better than 50 percent lower initialisation error, and is described as directly implementable in existing experiments. Readout at the 1042 nm singlet transition, previously treated as dark, gives a second optical channel and is claimed to extend spin-state transcription towards the 1300 nm region, which matters for fibre-coupled operation. In the anvil cell, fabricating the NV ensemble on the anvil surface addresses a case where competing techniques are scarce.

Diamond is not unchallenged. The explicit motivation for spin defects in two-dimensional hexagonal boron nitride is that NV centres degrade near surfaces and in nanoscale volumes, precisely where sensor-target separation should be smallest; the hBN work maps hyperfine interactions and demonstrates switchable magnetic and electric noise sensing. That is a real threat to the thinnest-gap applications. For diamond as a transistor substrate no comparative performance number against silicon or other wide-bandgap materials appears in the sources, only a methodological transplant of the silicon toolkit **Walker 2026 Diamond 2Dhg Conduction Mechanism**.

**TLDR: Order-of-magnitude gains on the parameters that previously capped NV ensembles, plus measurements with no clear alternative probe.**

## Diffusion (3/5)

The signals of an emerging engineering discipline are present. Microwave field-forming geometries are being compared quantitatively and optimised for ensemble uniformity, with simulation validated by Rabi oscillation measurements. Detector design rules are being derived rather than tuned empirically, with RF power sensitivity shown to scale inversely with the interface dimension. Reconstruction of what the sensor actually saw is being treated as its own problem, including the finding that replacing a scalar or coherent forward approximation with a tensor power-summed dipolar operator changes the inverse landscape and exposes a centre-collapse failure mode. Telecom-compatible readout removes one integration barrier.

The barriers are equally clear. Surface and nanoscale degradation limits the closest-approach applications and is driving competitors. Diamond material quality remains heterogeneous, with defect populations that anticorrelate spatially and produce spatially heterogeneous photoluminescence in the 800 to 900 nm range, and even the mechanism behind conductivity in hydrogenated nanodiamond surfaces remains debated between monohydride termination and graphitic islets. For electronics the barrier is stated outright: no robust models, therefore no circuit design **Walker 2026 Diamond 2Dhg Conduction Mechanism**. Nothing in the sources evidences products, deployments or volumes, so the score reflects a credible but unproven path.

**TLDR: The engineering layer around diamond sensors is forming, but no source shows adoption outside laboratories.**

## Impact (3/5)

The demonstrated value is instrumental. Magnetometry inside a diamond anvil cell opens magnetic characterisation of matter at pressures where few probes work, evidenced by resolving the iron alpha-to-epsilon transition up to 30 GPa. High-fidelity optical readout of large coherent nuclear spin ensembles at millitesla or lower fields is put forward as a route to fundamental physics tests and inertial sensing, the latter being the only application in the set with obvious commercial scale, and it is a prospect rather than a result. Broadband RF detection with derived design scaling laws is a second candidate area.

The larger prize, diamond power and RF electronics, is where impact would be measured in markets rather than papers, and the sources give no performance or economic quantification of it, only the observation that the modelling groundwork is now being laid **Walker 2026 Diamond 2Dhg Conduction Mechanism**. A score above 3 would require evidence the sources do not contain. Two contextual sources support the case that diamond remains a reference material for fundamental theory and characterisation, with the electron-phonon contribution to total energy computed for carbon polymorphs including diamond for the first time in the standard Hamiltonian framework, but that is scientific rather than economic weight.

**TLDR: Clear new measurement capability in niches; the sources do not establish broad economic value.**

## Timing Soon (2-5yr)

On the sensing side the clock has already started. Results dated 2026 include high-pressure magnetometry to 30 GPa, optically detected nuclear magnetic resonance on roughly 10^16 spins and sub-400 fT/sqrt(Hz) laser threshold magnetometry. What is not yet in place is the packaging, uniformity and readout engineering needed for anything beyond bespoke instruments, and that work is visibly in progress rather than complete. A two to five year horizon for capable instrument-grade products is consistent with the evidence; anything faster would be extrapolation.

The electronics branch should be timed separately and later. The stated bottleneck is the absence of extractable, circuit-usable device models, plus an unexplained leakage mechanism in undoped 2DHG structures **Walker 2026 Diamond 2Dhg Conduction Mechanism**. Model development, validation and PDK-grade characterisation are multi-year activities even once the physics is understood, and the sources capture the field at the start of that process.

**TLDR: NV diamond sensing is already returning results in fixed laboratory instruments; usable diamond electronics is further out and gated on device models.**

## Overrated or underrated? Fairly rated

Diamond's reputation as the quantum sensing workhorse is earned rather than hyped. The 2026 literature in this set is not repeating first demonstrations; it is grinding out contrast, dynamic range, readout wavelength, microwave uniformity and inverse-problem reconstruction, and it is delivering measurements such as the iron magnetic transition at 30 GPa that justify the platform on its own terms. The honest qualifier is that the competitive frame is shifting: the case for two-dimensional hosts such as hBN rests explicitly on NV degradation near surfaces, which is exactly where the highest-value nanoscale measurements live. Diamond keeps the bulk-ensemble and extreme-environment ground; it may lose the atomically close-approach ground.

Diamond as a power semiconductor is a different bet and, on this evidence, is at an earlier stage than its rhetoric elsewhere usually suggests. The most useful signal in the set is not a record device but the argument that diamond 2DHG FETs need to be pulled into the silicon modelling framework before circuit design is possible, together with a leakage mechanism nobody expected **Walker 2026 Diamond 2Dhg Conduction Mechanism**. Investors treating those two branches as one story are mispricing both.

## Prediction

By 31 December 2028, NV-diamond magnetometry will have produced at least one further published measurement inside a diamond anvil cell above the 30 GPa reported in, while no publicly released circuit-design compact model for diamond 2DHG FETs will exist.

## Evidence base

- An NV ensemble fabricated on a diamond anvil surface imaged iron's stray field up to 30 GPa and resolved the alpha-to-epsilon magnetic transition, published 4 May 2026.
- A laser threshold magnetometer with NV centres inside a laser cavity reached 100 percent optical contrast, up to 50 mW output and photon-shot-noise-limited sensitivity below 400 fT/sqrt(Hz) on all vector components, against a prior norm of a few percent contrast and a few microtesla dynamic range, 5 May 2026.
- Optical polarisation and readout of roughly 10^16 carbon-13 nuclear spins was demonstrated in natural-abundance diamond with 0.5 to 10 ppm nitrogen using state-selective Landau-Zener transfer, 4 May 2026.
- Exploiting NV charge-state ionisation, normally treated as parasitic, improved readout contrast by 17 percent relative and reduced initialisation error by more than 50 percent, 14 May 2026.
- Diamond 2DHG FETs were characterised with the silicon MOS toolkit for the first time, yielding effective mobility and conduction barriers plus an unexpected GIDL-like leakage mechanism in the absence of intentional doping, with the stated aim of enabling circuit-design device models, IEEE Access 2026, DOI 10.1109/ACCESS.2026.3704335 **Walker 2026 Diamond 2Dhg Conduction Mechanism**.
- Competing platforms are being justified by NV weaknesses: performance degradation near surfaces and in nanoscale volumes is the explicit motivation for spin ensembles in two-dimensional hBN, 5 May 2026.

## Open questions

- Does the 100 percent contrast and sub-400 fT/sqrt(Hz) laser threshold magnetometer survive miniaturisation and thermal management outside an optical bench, and at what size and power budget?
- Can NV surface degradation be engineered away, or do two-dimensional hosts such as hBN take the nanoscale close-approach applications outright?
- What is the physical origin of the GIDL-like leakage seen in undoped diamond 2DHG FETs, and does it impose a hard off-state limit on the device class **Walker 2026 Diamond 2Dhg Conduction Mechanism**?
- How reproducible are diamond substrates at the defect level, given anticorrelated nitrogen centre distributions and spatially heterogeneous photoluminescence in real crystals?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
