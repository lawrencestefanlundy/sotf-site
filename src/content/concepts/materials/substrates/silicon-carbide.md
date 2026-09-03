---
type: concept
slug: silicon-carbide
aliases:
- SiC
- 4H-SiC
- silicon carbide
canonical_name: Silicon Carbide
parent_concepts:
- wide-bandgap-semiconductors
related_concepts:
- wide-bandgap-semiconductors
- gallium-nitride
- silicon-carbide-photonics
- power-electronics
- compound-semiconductors
- mocvd-mbe
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-07-13-department-of-commerce-announces-direct-funding-agreement-wi]]'
- '[[2026-06-12-hku-sic-cryogenic-neuromorphic-chip-10mk]]'
- '[[2024-06-01-stmicroelectronics-to-build-5bn-silicon-carbide-campus-in-it]]'
scorecard:
  viability: 4
  drivers: 3
  novelty: 3
  diffusion: 3
  impact: null
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 54
sources_7d: 1
sources_30d: 6
recent_mentions:
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-14-boschs-sic-fab-deal-adds-to-a-resurgence-in-chips-act-fundin
  title: Bosch's SiC fab deal adds to a resurgence in CHIPS Act funding - Electronics360
  date: '2026-07-14'
  kind: web
- slug: 2026-07-13-department-of-commerce-announces-direct-funding-agreement-wi
  title: Department of Commerce Announces Direct Funding Agreement with Bosch for a $225 Million CHIPS Program Award to Support Domestic Production of Silicon Carbide Semiconductors - National Institute of Standards and Technology (.gov)
  date: '2026-07-13'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-22-sintered-metal-die-attach-landscape
  title: Sintered-silver / sintered-copper die-attach landscape — physics, incumbents, AI-migration question (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-12-hku-sic-cryogenic-neuromorphic-chip-10mk
  title: HKU world-first cryogenic neuromorphic chip at 10 mK (silicon carbide, impact-ionisation spiking)
  date: '2026-06-12'
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
- slug: silicon-carbide-photonics
  name: Silicon Carbide Photonics
  path: /materials/substrates/silicon-carbide-photonics/
  macro: materials
- slug: power-electronics
  name: Power Electronics
  path: /energy-power/power-electronics/power-electronics/
  macro: energy-power
- slug: compound-semiconductors
  name: Compound Semiconductors
  path: /materials/substrates/compound-semiconductors/
  macro: materials
- slug: mocvd-mbe
  name: MOCVD / MBE
  path: /manufacturing/equipment-processes/mocvd-mbe/
  macro: manufacturing
---
**Silicon carbide is a wide-bandgap semiconductor already deployed in high-power and harsh-environment electronics, and the current research front is not whether the material works but whether its crystal defects, interfaces and cryogenic behaviour can be controlled well enough to extend it into quantum devices, ultra-wide-bandgap heterostructures and fusion components.**

## Summary

Silicon carbide (SiC) is a compound semiconductor with a wide bandgap and unusually high thermal and chemical stability. It exists in many polytypes, which share the same local tetrahedral Si-C bonding but differ in long-range stacking: the cubic 3C form, the hexagonal 2H and 4H forms, the 6H form used in single-crystal substrates, and rhombohedral variants such as 9R. Polytype choice sets thermal stability, phonon transport and defect behaviour, and machine-learning molecular dynamics places the relative high-temperature stability ordering at 3C > 2H > 9R, with melting initiated by the formation of short C-C contacts and carbon-rich local regions before tetrahedral connectivity is lost.

The commercial base is power and harsh-environment electronics, where SiC is described as widely deployed, alongside an emerging CMOS technology platform. Three adjacent uses drive most of the current literature. First, quantum technology: crystal defects such as divacancies act as spin qubits or single-photon sources, and defect engineering depends on migration barriers that atomistic simulation now puts at 2.12 eV for carbon vacancies and 0.88 eV for carbon interstitials, a hierarchy that governs whether interstitial-vacancy recombination or vacancy aggregation into spin-active divacancies wins. Second, SiC as a thermal substrate for ultra-wide-bandgap devices, where Ga2O3/SiC heterointegration is attractive but interfacial thermal boundary conductance is the heat-removal bottleneck. Third, nuclear and fusion use, where SiC is a leading candidate for tritium permeation barriers and where measured permeation values vary widely between ideal single crystals and real defect-containing material.

The parameters that decide outcomes are almost all defect-related rather than intrinsic. Threading dislocation density in wafers drives reverse leakage and degradation, and commercial inspection based on surface profiling and photoluminescence dark contrast misses nanoscale threading dislocations that have no resolvable surface signature. Extended defects such as Shockley partial dislocations and dislocation complexes progressively reduce stiffness in 3C-SiC. Hydrogen solubility rises sharply in carbon-rich amorphous regions and at silicon vacancies relative to interstitial sites in pure beta-SiC, which is precisely the difference between an ideal permeation barrier and a leaky one. Metrology is being rebuilt around this: contact-free terahertz reflection spectroscopy is being mapped for accessible doping ranges in SiC, Si and GaN layer stacks, and machine-learned interatomic potentials now support multimillion-atom, microsecond simulations of SiC from ambient to extreme conditions.

## Viability (4/5)

SiC is stated to be widely deployed in high power and harsh environment electronics, with an emerging CMOS platform. That is the anchor: this is not a speculative material. The supplied evidence for the mainstream power application is thin in quantitative terms, but nothing in the sources contests it, and the entire research programme they describe is one of refining an already-fielded material rather than proving a concept.

The extensions are a different matter and each fails in a specific, characterised way. Commercial SiC power MOSFETs cooled from 300 K to 650 mK show large gate hysteresis, threshold voltage shifts and subthreshold swing deterioration, attributed to carrier freeze-out and high interface trap density, which the authors say may pose challenges for reliable use in quantum devices or cryo-CMOS. Ga2O3/SiC integration is blocked at the interface rather than in the bulk. Fusion permeation barrier performance is uncertain because real material is defective. Score 4 reflects a proven material with unproven frontiers, not a uniformly demonstrated technology.

**TLDR: The material itself is in production use; the frontier extensions each have a named, unsolved physical obstacle.**

## Drivers (3/5)

On demand, the sources name four distinct pulls: high power and harsh-environment electronics; ultra-wide-bandgap power devices needing SiC as a heat-spreading substrate for Ga2O3; quantum technologies using SiC spin defects, where first-principles work has identified a previously overlooked non-radiative channel in the divacancy triplet lifetime; and fusion reactor tritium permeation barriers. That breadth is a genuine driver. What the sources do not give is any market size, shipment volume, price trend or capacity figure, so the strength of these pulls cannot be graded.

On supply, the enabling tooling is moving quickly. Contact-free terahertz doping characterisation is being given a sensitivity metric that says in advance whether a given SiC layer stack is measurable at all. Confocal subsurface backscattering microscopy detects threading dislocations non-destructively and distinguishes their type by photoelastic scattering pattern, closing a gap left by commercial inspection systems. General-purpose machine-learned potentials now cover the pressure-temperature phase diagram and displacement threshold energies for 2H and 3C at multimillion-atom scale. Better cheap metrology and better predictive simulation are exactly what a defect-limited substrate industry consumes.

**TLDR: Several independent demand pulls are documented but none is quantified; supply-side tooling is visibly improving.**

## Novelty (3/5)

SiC's claim is being a wide-bandgap semiconductor that is also one of the most thermally and chemically stable materials known, which is what buys the high-power and harsh-environment position that silicon cannot hold. In the ultra-wide-bandgap stack it is not the active material but the heat sink under Ga2O3, and the orientation matters: thermal boundary conductance is consistently higher for Ga2O3(-201)/SiC(0001) than the alternative interface studied. In quantum, the comparator is diamond: the same computational framework that reaches quantitative agreement for the NV- centre in diamond identifies an extra non-radiative channel in the SiC divacancy, which is a correction to SiC's optical spin performance rather than an advantage over diamond.

Where the sources are quantitative they mostly describe SiC's own physics rather than a margin over a rival. Fracture energy of the single-crystal 6H-SiC {10-10} plane is 7.5 +/- 0.3 J/m2 by microscale double cantilever beam testing, with single cantilever beam geometry giving over twice that because of Ga implantation and residual stress. Topological surface phonons contribute over 30% of in-plane thermal conductivity in films below 10 nm across Si, 4H-SiC and c-BN, with a largest absolute contribution of 82 W/m-K, a shared effect rather than a SiC-specific edge. Score 3: real and differentiated, but the sources do not let anyone state by how much.

**TLDR: Clear qualitative advantages over silicon and as a substrate under Ga2O3, but the sources rarely quantify the margin.**

## Diffusion (3/5)

The binding barrier is defect control in real wafers. High densities of threading dislocations facilitate reverse leakage and degradation, and the installed base of commercial defect inspection, based on surface profiling and photoluminescence dark contrast, misses nanoscale threading dislocations because they lack resolvable surface signatures and band-edge photoluminescence is quenched by background dopants or compensating defects. A material whose failure modes cannot be screened at incoming inspection carries yield risk into every downstream product. Extended defects also soften the lattice, with stiffness falling as Shockley partial dislocation and dislocation complex densities rise.

Secondary barriers are application-specific. Cryogenic instability rules out naive reuse of commercial SiC MOSFETs in cryo-CMOS or quantum control without redesign. Heterointegration requires interfacial thermal transport that is currently hard to measure directly, with first-principles methods too expensive and empirical potentials lacking transferability across oxide and carbide bonding. Even measurement methodology is unsettled: micromechanical fracture values depend strongly on notch preparation, and vacuum annealing was needed to reconcile two test geometries. Standards and qualification data are therefore harder to establish than for a mature silicon process.

**TLDR: Adoption is gated by wafer defect density, inspection blind spots and interfacial engineering, all of which are being worked on but none of which is solved.**

## Impact (unscored)

The supplied material names high-value end uses across power electronics, ultra-wide-bandgap devices, quantum spin systems and fusion tritium permeation barriers. Breadth across four largely independent sectors is suggestive, and it is also why SiC is unusually well hedged against any single application disappointing.

But none of these sources contains a market figure, an efficiency gain against an incumbent at system level, a cost comparison, or a deployment volume. Assigning a score here would be inventing a judgement the evidence does not carry. The honest position is that the sources do not support an impact assessment, only the observation that the material sits under several separately important technology roadmaps.

**TLDR: The sources establish breadth of application but give no basis for sizing the value.**

## Timing Now (0-2yr)

SiC is described as already widely deployed in high power and harsh environment electronics, so for the mainstream use the relevant horizon is immediate: wafer defect density, inspection coverage and interfacial thermal engineering are current production problems, and the tooling being published against them, such as confocal subsurface backscattering microscopy for threading dislocations and contact-free terahertz doping metrology, is at the laboratory demonstration stage that typically precedes fab evaluation.

The extensions run later on different clocks. Quantum uses depend on controlling divacancy formation against competing recombination and aggregation pathways and on non-radiative channels only now being computed correctly. Cryogenic electronics would need devices that do not show the hysteresis and threshold shifts observed at 650 mK. Fusion permeation barriers are tied to reactor programme timelines the sources do not specify.

**TLDR: The base material is already deployed; the open questions are near-term manufacturing and metrology ones, with quantum and cryogenic uses further out.**

## Overrated or underrated? Fairly rated

SiC is a real, fielded material with a physically grounded advantage in wide bandgap and thermal and chemical stability, and the literature here reads exactly as one would expect for a technology in that position: no one is arguing about whether it works, and everyone is arguing about defects, interfaces and measurement. Treating it as an emerging technology would overstate the risk; treating it as solved would understate how much of its performance envelope is still limited by dislocations, interface traps and interfacial thermal resistance rather than by intrinsic material properties.

The position worth taking is on where the value sits. It is not in the material thesis, which is settled, but in defect metrology and interface engineering. A wafer inspection method that reliably finds nanoscale threading dislocations that current commercial tools miss addresses a yield and reliability problem in a shipping product line. The quantum and cryogenic angles are the most cited but the least supported by demonstrated device results in these sources: commercial SiC MOSFETs degrade badly at deep cryogenic temperatures, and anyone pricing SiC on a quantum-platform narrative is ahead of the evidence.

## Prediction

By June 2029, no commercially available SiC power MOSFET will be qualified by its manufacturer for operation below 1 K without the gate hysteresis and threshold-voltage instability reported down to 650 mK in.

## Evidence base

- Silicon carbide is described as widely deployed in high power and harsh environment electronics with an emerging CMOS platform, while commercial power MOSFETs cooled from 300 K to 650 mK show large gate hysteresis, threshold voltage shifts and subthreshold swing deterioration, attributed to carrier freeze-out and high interface trap density, 5 May 2026.
- Commercial SiC wafer inspection based on surface profiling and photoluminescence dark contrast misses nanoscale threading dislocations, which drive reverse leakage and degradation; confocal subsurface backscattering microscopy detects them non-destructively and distinguishes their type, 4 June 2026.
- Migration barriers of 2.12 eV for carbon vacancies and 0.88 eV for carbon interstitials in 3C-SiC set the mobility hierarchy that determines whether vacancies aggregate into spin-active divacancies or recombine, 28 May 2026.
- Interfacial thermal boundary conductance is the major heat-removal bottleneck for Ga2O3/SiC heterointegration, and is consistently higher for Ga2O3(-201)/SiC(0001) than the alternative orientation studied, 8 May 2026.
- Fracture energy of the 6H-SiC {10-10} plane measured 7.5 +/- 0.3 J/m2 by microscale double cantilever beam, while focused-ion-beam-notched single cantilever beams gave over twice that value due to Ga implantation and residual stress, 3 June 2026.
- Hydrogen solubility in beta-SiC is significantly enhanced in carbon-rich non-stoichiometric amorphous structures and at silicon vacancies compared with interstitial sites in pure material, bearing on SiC's use as a fusion tritium permeation barrier where experimental permeation values vary widely, 4 June 2026.

## Open questions

- Can confocal subsurface backscattering microscopy, or an equivalent optical method, be run at wafer-scale throughput and integrated into commercial SiC incoming inspection, rather than remaining a laboratory imaging technique?
- Is the cryogenic instability of SiC MOSFETs a property of commercial process choices, in particular interface trap density, or intrinsic to carrier freeze-out in the material, and can a redesigned device fix it?
- Do the predicted orientation-dependent thermal boundary conductances at Ga2O3/SiC interfaces survive experimental measurement on real, non-ideal interfaces, and is the resulting heat removal sufficient for ultra-wide-bandgap power devices?
- Can processing be tuned to favour divacancy stabilisation over interstitial-vacancy recombination at scale, given the 2.12 eV and 0.88 eV migration barriers for carbon vacancies and interstitials?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
