---
type: concept
slug: epitaxy
canonical_name: Epitaxy
aliases: []
parent_concepts:
- equipment-processes
- manufacturing
related_concepts: []
sources:
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-05-02-self-buffered-bto-epitaxy-on-oxide-insulator-light-sci-app-2]]'
scorecard:
  viability: 4
  drivers: 3
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
mention_count: 71
sources_7d: 2
sources_30d: 6
recent_mentions:
- slug: 2026-05-02-self-buffered-bto-epitaxy-on-oxide-insulator-light-sci-app-2
  title: 'Self-buffered BTO epitaxy on oxide insulator (Light: Sci & App 2025)'
  date: '2026-05-02'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors: []
---
**Epitaxy is the family of processes that grow a single-crystal film in registry with a crystalline substrate, and it remains the step that sets the performance ceiling for power transistors, photonic and quantum emitters, and most exotic thin-film phases.**

## Summary

Epitaxy means growing a crystalline layer whose atomic lattice is aligned to that of the substrate underneath it. Rather than depositing an amorphous or polycrystalline film, the arriving atoms find lattice sites dictated by the surface below, so the film inherits its orientation and, if the lattice constants differ, a defined state of strain. This is how essentially every compound-semiconductor device stack is made: heterostructures, quantum wells, doped channels and buffer layers are all built by stacking epitaxial layers of controlled composition and thickness.

Several distinct techniques share the name. Molecular beam epitaxy (MBE) evaporates elemental sources in ultra-high vacuum onto a heated substrate, giving monolayer-level control and in-situ diagnostics via reflection high-energy electron diffraction (RHEED); the sources here use it for everything from single- to five-layer MoS2 on graphene/Ir(111) to PtTe2 films grown with single-monolayer precision from 1 to 20 ML. Metal-organic vapour phase epitaxy (MOVPE) uses gaseous precursors at high temperature and is the workhorse for nitrides. Halide vapour phase epitaxy (HVPE) trades some control for rate, reaching up to 30 µm/hr for β-Ga2O3 on sapphire. Liquid-phase epitaxy is used in ambient conditions for oriented metal-organic framework films by spin-assisted layer-by-layer deposition, and thermal laser epitaxy uses a focused high-power laser to evaporate refractory targets.

The parameters that decide outcomes recur across all of these papers. Substrate choice, crystallographic orientation and offcut: raising sapphire offcut from 0° to 8° shifted Ga2O3 growth from multidirectional to terrace-dominated, cutting roughness from 14.69 to 2.74 nm and rocking-curve FWHM from 994 to 414 arcsec, and GaSe morphology on GaAs depends on both orientation ((211)B versus (001)B) and pre-growth surface preparation. Growth temperature, which trades crystal quality against unwanted interdiffusion: high MOVPE temperatures needed for good AlGaN also drive barrier-channel intermixing that can destroy the two-dimensional electron gas entirely. Flux ratios, such as As2 flux around three times stoichiometry for InAs diodes or Se:Mn between 1.1 and 3.1 for Mn2In2Se5. And, increasingly, the ability to constrain where growth happens, via selective-area masks or pre-patterned nucleation sites.

## Viability (4/5)

Nothing here is speculative about whether epitaxy works. The sources report single-oriented monodomain growth of a metastable oxide, TaO2 on r-plane sapphire, by two independent methods; phase-pure (-201)-oriented Ga2O3 with 414 arcsec rocking curves; smooth single-crystalline Mn2In2Se5 at 1.5 nm RMS roughness; and single-photon emission with g2(0) = 0.07 ± 0.02 from droplet-etched telecom-band quantum dots. Sheet resistivities around 2,500 Ω/sq for AlN/Al0.75Ga0.25N are stated as consistent with the best reported values.

The caveats are equally explicit and keep this off a 5. The MBE-grown InAs thermoradiative diodes achieve breakdown above 0.3 V but reverse saturation current densities 200 times the radiative limit, which the authors themselves frame as initial development. Selective-area MBE on alternative dielectric masks is only partly solved: Al2O3 shows promising selectivity in the GaAs growth window, but HfO2 is dominated by Ga adsorption up to 650 °C and TiO2 proved reactive. Reported growth windows are often narrow or require careful compensation, and reproducibility remains a stated problem in the oriented-MOF case.

**TLDR: The core technique is proven and in daily use; the frontier variants deliver quantified results but with visible defect and yield gaps.**

## Drivers (3/5)

On the demand side the pull is visible and diverse. Quantum communication needs reproducible, symmetric emitters at specific telecom wavelengths, which is stated as the motivation for droplet-etched quantum dot epitaxy and for deterministic dot placement inside circular Bragg gratings. Wide-bandgap electronics drives the AlGaN HEMT interface work and Si-doped Ga2O3 on sapphire. Broadband spintronic THz emitters are limited by the spin Hall conductivity of the conversion layer, and epitaxial thickness control is offered as the way around that fixed material limit. 2D semiconductor device interest is cited directly as the reason to control MoS2 layer number.

On the supply side the sources support only one observation: capability is spreading through cheaper or more flexible source technologies. Thermal laser evaporation, using a 1 kW continuous-wave 1070 nm fibre laser focused to a sub-millimetre spot, can evaporate essentially any solid element including refractory metals, and a home-built system is described in enough detail to be replicated. Beyond that there is no data here on equipment vendors, tool prices, substrate availability or fab capacity, so this score reflects research-level demand evidence only.

**TLDR: Clear pull from quantum photonics, wide-bandgap power devices and THz sources; the sources say nothing about tool supply, cost or capacity.**

## Novelty (3/5)

As a class, epitaxy is decades-old infrastructure and is what alternatives are measured against, not the other way round. The comparison that matters is against non-epitaxial deposition, where crystalline registry, monolayer thickness control and abrupt heterointerfaces are simply unavailable. The sources illustrate the value of that registry sharply: MBE PtTe2 at 10 ML gives a THz emission amplitude six times an equivalent Pt reference, and the effect switches on only at the 2 ML semiconductor-to-semimetal transition. Epitaxial stabilisation also gives access to phases that are otherwise metastable, as with TaO2 on sapphire, and to unconventional routes such as Mn intercalation converting In2Se3 into Mn2In2Se5.

The specifically new increments in this evidence set are three. First, defeating the random spatial distribution of self-assembled quantum dots: AFM-assisted nano-oxidation lithography positions GaAs dots with 51(28) nm radial displacement, and the resulting free-standing asymmetric circular Bragg gratings show a 245-fold photoluminescence enhancement with polarisation imbalance and fine-structure splitting below 5 %. Second, mask engineering to widen selective-area regrowth beyond SiO2 and Si3N4, whose extinction coefficients block high-contrast infrared photonics. Third, machine learning applied to RHEED, where unsupervised clustering finds a clean boundary between high- and low-quality samples and identifies growth rate as the dominant influence on rocking-curve FWHM while Se/Ga flux ratio dominates roughness. Each is an improvement on a known method rather than a replacement of it.

**TLDR: Epitaxy is the incumbent, not the challenger; the genuine novelty is in placement determinism, metastable phase access and machine-learning process control.**

## Diffusion (3/5)

The diffusion picture is bimodal. MOVPE-grown nitrides and HVPE-grown oxides are described in terms that presume production relevance, with HVPE reaching 30 µm/hr and heteroepitaxy on sapphire rather than expensive native substrates, and one MOF route explicitly designed for rapid, ambient-condition, automated fabrication rather than vacuum equipment. Signs of process maturity also appear: XRD is proposed as a non-destructive in-line proxy for interface sharpness, and hBN films with silicon-doped single-photon emitters were transferred onto SiO2 to demonstrate device-integration compatibility.

The barriers are specific. MBE is a slow, ultra-high-vacuum, manually tuned process; the authors of the machine-learning study state directly that autonomous synthesis platforms remain underdeveloped for MBE. Serial AFM lithography for dot placement is called scalable by its authors but is nonetheless a per-site technique. Growth temperature windows are constrained on both sides, with high-temperature Si incorporation in hBN needing 900 to 1390 °C to be swept to find an optimum. Prior literature disagreement on GaSe/GaAs morphology, traced to unreported substrate preparation, is a candid illustration of how fragile cross-lab transfer still is.

**TLDR: Already industrially diffused in some forms, but the frontier processes carry throughput, reproducibility and substrate-cost barriers the sources make plain.**

## Impact (4/5)

The strongest argument for high impact is that in these papers the epitaxy step is what decides whether the device works at all. Alloy intermixing during AlGaN growth smooths the polarisation contrast and can completely destroy the 2DEG, meaning the transistor exists or does not depending on the growth scheme. Random dot positioning is named as the thing that hinders deterministic coupling of quantum emitters to microcavities, and fixing it buys a 245-fold photoluminescence enhancement. Thickness control alone moves spintronic THz output by a factor of six against a Pt reference. Band gap in MoS2, including whether the conduction band is pinned, changes with layer number in the range one to five.

That leverage is broad rather than deep in any single market: power electronics, quantum light sources at telecom wavelengths, THz instrumentation, thermoradiative energy harvesting and oriented MOF films for sensing, catalysis and separation all appear in this source set. What the sources do not provide is any quantification of economic value, addressable market or displacement of an incumbent product, so the score rests on technical criticality across many applications rather than on measured value capture.

**TLDR: Growth quality, not device design, is repeatedly the binding constraint on device performance across four unrelated application areas.**

## Timing Now (0-2yr)

For nitride HEMTs and oxide power semiconductors, the work in these sources is process refinement of an already-deployed manufacturing route, and the improvements, such as growth schemes that preserve the 2DEG or offcut selection that reduces roughness fivefold, can be absorbed on a timescale of months to a couple of years by anyone already running the tools.

The frontier items are slower. Deterministic quantum dot placement, telecom C-band droplet-etched emitters, Si-doped hBN emitters and thermoradiative InAs diodes are all at first-demonstration stage, with the InAs work two orders of magnitude off its radiative limit. Machine-learning-guided MBE is presented as offline correlation analysis on RHEED embeddings, not closed-loop autonomous control, which puts real autonomous epitaxy in a later band. The sources do not contain roadmaps or dates for any of these, so those horizons are inferred from technical readiness rather than stated.

**TLDR: Epitaxy is already the production process for the devices that depend on it; the specific advances here split between immediate process fixes and much longer-horizon quantum hardware.**

## Overrated or underrated? Underrated

Epitaxy is treated as background plumbing by most people looking at semiconductors, quantum hardware or THz systems, and this evidence set argues the opposite: the growth recipe is frequently the whole story. A transistor's 2DEG survives or does not depending on interdiffusion during growth. A THz emitter gains a factor of six from monolayer counting. A single-photon source becomes usable only once nucleation is placed to within tens of nanometres. Investment attention flows to the device and the system; the constraint sits upstream in the reactor.

The honest counterweight is that this is a mature field where progress is incremental and slow, and where much of the value accrues to a small number of established equipment and materials suppliers that these sources do not name. The most interesting under-priced thread is process automation: the admission that autonomous synthesis is underdeveloped for MBE, combined with a candid account of prior published disagreements caused by unrecorded substrate preparation, suggests reproducibility and recipe search are still done by hand in a field that has been industrialised for decades. That is where the next step change is most likely to come from.

## Prediction

By June 2028, at least one peer-reviewed report will demonstrate closed-loop, RHEED-driven machine-learning control of an MBE growth run, with a quantified reduction in the number of calibration growths needed to hit a target rocking-curve FWHM, going beyond the offline correlation analysis reported in.

## Evidence base

- 6 May 2026: AFM-assisted nano-oxidation lithography positions MBE-grown GaAs quantum dots with 51(28) nm radial displacement, and the resulting circular Bragg gratings show a 245-fold photoluminescence enhancement with fine-structure splitting and polarisation imbalance below 5 %.
- 5 June 2026: MBE PtTe2 grown with single-monolayer precision from 1 to 20 ML shows spintronic THz emission absent in the monolayer semiconducting phase, switching on near 2 ML and peaking at six times an equivalent Pt reference at 10 ML.
- 5 June 2026: HVPE Si-doped β-Ga2O3 on sapphire reached growth rates up to 30 µm/hr, and increasing offcut from 0° to 8° cut surface roughness from 14.69 to 2.74 nm and rocking-curve FWHM from 994 to 414 arcsec.
- 4 June 2026: high MOVPE temperatures needed for crystal quality in Al-rich AlGaN cause barrier-channel intermixing that can completely destroy the 2DEG; improved growth schemes gave sheet resistivities around 2,500 Ω/sq for AlN/Al0.75Ga0.25N.
- 8 May 2026: local droplet etching produced symmetric InGaAs quantum dots at 10^9/cm2 density with 1.14 in-plane aspect ratio, 0.2 meV linewidths and g2(0) = 0.07 ± 0.02 under continuous-wave above-band excitation.
- 2 June 2026: of three alternative selective-area MBE mask materials, Al2O3 showed promising selectivity in the GaAs growth window while HfO2 was highly non-selective due to Ga adsorption up to 650 °C and TiO2 proved reactive.

## Open questions

- Can MBE-grown InAs thermoradiative diodes close the gap from reverse saturation currents 200 times the radiative limit to something near it, or is the deficit intrinsic to the growth-related defect population?
- Does Al2O3 retain its selective-growth behaviour across full-wafer, repeated regrowth cycles at GaAs growth temperatures, and can HfO2's Ga adsorption problem be suppressed rather than avoided?
- Is serial AFM nano-oxidation placement of quantum dots at 51 nm accuracy compatible with any credible throughput, or does deterministic placement require a parallel patterning route?
- Does HVPE β-Ga2O3 on 8° offcut sapphire, at 414 arcsec rocking-curve FWHM, reach a defect density low enough for power-device breakdown and reliability targets, which the source does not report?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
