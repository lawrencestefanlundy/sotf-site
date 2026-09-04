---
type: concept
slug: gallium-arsenide
canonical_name: Gallium Arsenide (GaAs)
aliases: []
kind: material
parent_concepts:
- materials
- substrates
related_concepts: []
sources:
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-07-28-laser-on-a-chip-w-matt-crowley-scintil]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-06-22-thermal-stack-layer-landscape]]'
- '[[2026-07-11-neutral-pdk-heterogeneous-integration-landscape]]'
scorecard:
  viability: 4
  drivers: 3
  novelty: 2
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 86
sources_7d: 3
sources_30d: 14
recent_mentions:
- slug: 2026-07-28-laser-on-a-chip-w-matt-crowley-scintil
  title: Laser on a Chip w/ Matt Crowley @ Scintil Photonics
  date: '2026-07-28'
  kind: substack
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-04-14-the-photonic-foundry-fallacy
  title: The Photonic Foundry Fallacy
  date: '2026-04-14'
  kind: substack
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
neighbors: []
---
**Gallium arsenide is a direct-bandgap III-V semiconductor substrate that has become the default host material for solid-state quantum light sources, ultra-low-noise crystalline mirror coatings and ultra-clean two-dimensional electron gases, and the 2026 literature shows it functioning less as a novel material than as the reference platform on which precision quantum and photonic engineering is done.**

## Summary

Gallium arsenide (GaAs) is a compound semiconductor from the III-V family, grown as bulk crystals and, more relevantly here, as epitaxial layers by molecular beam epitaxy (MBE). Unlike silicon it has a direct bandgap, so it emits light efficiently; it also forms near-perfect lattice-matched heterostructures with aluminium gallium arsenide (AlGaAs) and can host indium gallium arsenide (InGaAs/InAs) inclusions. Those three properties generate almost all of its current research use: quantum dots that emit single or entangled photons, quantum wells and two-dimensional electron gases with very high carrier mobility, and epitaxial AlGaAs/GaAs multilayer stacks used as crystalline mirror coatings.

The way it works in each case comes down to bandgap engineering. Growing a thin, narrow-gap island (a GaAs or InGaAs quantum dot) inside a wider-gap matrix confines single electron-hole pairs, which then recombine to emit photons one at a time. Stacking alternating AlGaAs and GaAs layers with quarter-wave thickness builds a Bragg reflector whose crystalline order gives lower mechanical loss, and hence lower thermal noise, than sputtered amorphous coatings; this is why they appear in transportable optical clock cavities and are planned for gravitational-wave detector upgrades. Confining a high-mobility 2D electron gas in a GaAs/AlGaAs heterostructure and adding gate-defined superlattices makes the material a solid-state analogue simulator, for instance for the Haldane model of a Chern insulator.

The parameters that decide whether GaAs wins in any given application are: growth control (facet dynamics, twin defects, selectivity of regrowth masks), emitter placement accuracy relative to a photonic cavity, extraction and fibre-coupling efficiency of the emitted photons, optical absorption at the wavelengths a system needs to use, and the refractive index mismatch when bonding III-V material onto silicon. Several 2026 papers are effectively attacks on one of these parameters: aspect-ratio-dependent etching to make free-standing circular Bragg gratings in a single step, AFM nano-oxidation lithography to place dots to within tens of nanometres, antimony-mediated facet engineering to suppress rotational twins in nanowires, and alternative dielectric masks for selective-area MBE.

GaAs is also the material against which theory and simulation are calibrated. It is described explicitly as a prototypical bulk semiconductor for coherent phonon experiments and used as the benchmark case for digital quantum simulation of optical absorption and gain spectra. That role, as the known-good reference, is itself evidence of maturity.

## Viability (4/5)

The evidence for basic viability is strong and comes from measurement rather than promise. A transportable ultraviolet clock laser using an AlGaAs/GaAs-coated cavity reached a fractional frequency instability of about 2 x 10^-16 with acceleration sensitivity no greater than 4(2) x 10^-12 per ms^-2, among the lowest reported for transportable systems. A single photon deterministically generated from an InAs/GaAs quantum emitter was used to violate a Bell-like noncontextual hidden-variable inequality by 380 standard deviations. AFM-positioned GaAs quantum dots in free-standing circular Bragg gratings gave a 245-fold photoluminescence enhancement with fine-structure splitting comparable to bulk dots, and polarisation imbalance below 5 per cent. Nanowire-embedded InGaAs emitters showed lifetimes as short as 0.51 plus or minus 0.02 ns with clear photon antibunching.

What is not yet demonstrated is the efficiency figure that matters commercially. The 68 per cent free-space extraction and 40 per cent lensed-fibre coupling in the free-standing grating work are finite-difference time-domain predictions, not measurements. Growth remains delicate: MBE of GaSe on GaAs has produced contradictory morphologies and polytypes across studies until substrate surface preparation was systematically examined, and nanowire emitter formation is hindered by facet-dependent growth and rotational twins. The material works; the yield and reproducibility of the structures built in it are still being engineered.

**TLDR: Devices work now and produce measured, quantitative results across several independent platforms.**

## Drivers (3/5)

On the demand side the sources are explicit about the applications pulling GaAs forward. Deterministic, bright quantum light sources are named as a crucial building block for future quantum communication networks, and monolithic integration of single-photon sources onto silicon is stated as a key requirement for scalable quantum photonics. Precision metrology is a second driver: optical clocks need ultra-stable cavities, and future gravitational-wave detector upgrades such as A# are described as incorporating AlGaAs/GaAs coatings. Data communications and optical interconnects at 1.3 um are named as the driver for InAs/(Al)GaAs quantum dot lasers on silicon.

On the supply side the sources describe capability work rather than capacity: broadening the mask materials available for selective-area MBE beyond SiO2 and Si3N4, with Al2O3 found to grow selectively at typical GaAs growth temperatures while HfO2 was highly non-selective up to 650 degrees C and TiO2 reactive, and single-step top-down etching to replace flip-chip bonding and multi-layer processing. Nothing in the supplied material addresses wafer supply, gallium or arsenic feedstock, pricing or fab capacity, so this score reflects application pull only.

**TLDR: Clear pull from quantum networking, metrology and optical interconnects; the sources contain no market or capacity data.**

## Novelty (2/5)

GaAs is treated throughout as the known quantity. It is called a prototypical semiconductor system for coherent phonon studies and used as the benchmark against which a new digital quantum simulation framework was validated in the noiseless limit. Its advantages over silicon are structural and long known: a direct bandgap for efficient emission and lattice-matched AlGaAs heterostructures. The genuinely new content in these sources sits one level up, in process: AFM nano-oxidation lithography achieving 51(28) nm radial placement of quantum dots is the wrong link, the correct one being; aspect-ratio-dependent etching removing the need for bottom reflectors and strain-inducing flip-chip bonding; dilute Sb incorporation to suppress rotational twins.

Where direct comparison to competing materials is made, GaAs does not always win. A density functional theory survey of zincblende III-V and II-VI semiconductors found aluminium-containing compounds, particularly AlSb, gave the highest shift-current response under visible light, with GaAs among the comparison set rather than the leader. The high refractive index of (Al)GaAs is described as an active liability for coupling into standard 220 nm silicon waveguides, and AlGaAs/GaAs coatings absorb excessively at 532 nm, breaking existing gravitational-wave detector locking schemes. This is a mature material with well-characterised trade-offs, not a step change.

**TLDR: The material is a decades-old workhorse; the novelty in these sources is in fabrication and integration, and at least one competitor material beats it on a specific figure of merit.**

## Diffusion (3/5)

Diffusion within the research base is effectively complete: the supplied sources span quantum optics, materials growth, condensed matter, metrology and gravitational-wave instrumentation, from groups across Europe, the US and Australia, all using GaAs epitaxy as available infrastructure. The barriers are downstream of the material. For quantum light sources, random spatial distribution of MBE-grown dots hinders deterministic coupling to microcavities, and the workaround, room-temperature AFM-assisted nano-oxidation lithography, is a serial technique whose throughput is not addressed. Conventional bright-source architectures require multi-layer processing or flip-chip bonding that introduces strain and limits scalability.

For CMOS integration the barrier is optical: the high refractive index of (Al)GaAs pushes many designs to silicon waveguides thicker than 220 nm, which is incompatible with standard CMOS, forcing new epitaxial designs to confine the mode within the III-V waveguide instead. For gravitational-wave detectors the barrier is that adopting AlGaAs/GaAs coatings invalidates the existing frequency-doubled arm-length stabilisation system, requiring a multi-wavelength scheme using a 1596 nm auxiliary beam outside the coating's absorption bands. Note also that the neural-interface backplane source, though tagged with gallium arsenide, actually uses amorphous indium gallium zinc oxide transistors on polyimide, so it is not evidence of GaAs diffusion into bioelectronics.

**TLDR: Ubiquitous in research labs with MBE access, but each frontier application hits a specific integration barrier that is currently being worked around.**

## Impact (3/5)

If the GaAs quantum dot route to deterministic, fibre-coupled entangled photon pair sources matures, it underpins quantum communication networks, which is the explicit motivation given. The metrology impact is already partly realised: a transportable clock laser at 2 x 10^-16 instability moves optical clock performance out of the fixed laboratory, and AlGaAs/GaAs coatings are on the roadmap for gravitational-wave detector upgrades, where mirror thermal noise is a limiting term. In condensed matter, ultra-clean GaAs/AlGaAs heterostructures offer a route to emulating the Haldane model, a Chern insulator with quantised Hall conductance without Landau levels, in a solid-state system.

The ceiling on this score is that the sources give no evidence about the size of the served markets, the cost of GaAs systems relative to alternatives, or the volume of deployed devices. The 1.3 um quantum dot laser work, the closest thing to a mass-market application, is a numerical study of design trade-offs rather than a fabricated device. Impact is credible and broad in scientific terms; its economic magnitude is not assessable from what is here.

**TLDR: High leverage on quantum networking and precision measurement, but the sources demonstrate laboratory-scale value, not system-level value.**

## Timing Now (0-2yr)

For metrology the answer is now. The transportable UV clock laser with AlGaAs/GaAs crystalline coatings is a working system with measured instability and acceleration sensitivity, and the arm-length stabilisation scheme needed to accommodate these coatings in gravitational-wave detectors has already been demonstrated on a tabletop, ahead of the A# upgrade. Single-photon and entangled-pair sources are also operational in laboratory settings today, sufficient to run foundational experiments such as a 380-sigma Bell-like inequality violation.

The part that is not now is scalable manufacture. Deterministic emitter positioning has only just reached tens of nanometres accuracy by a serial AFM method, predicted fibre-coupling efficiencies remain unmeasured, and the epitaxial designs needed for CMOS-compatible III-V-on-silicon lasers are still at the simulation stage. Those threads look like a two to five year horizon on the evidence available.

**TLDR: GaAs is already the operating material in tier-one metrology and quantum optics experiments; scalable quantum-network deployment is further out.**

## Overrated or underrated? Fairly rated

GaAs is doing exactly what a mature substrate should do: it is invisible as a headline and load-bearing in practice. Across eighteen sources it appears as the enabling layer for optical clocks, gravitational-wave mirror coatings, quantum light sources, polariton physics in the very strong coupling regime, Rydberg exciton band mixing, and topological analogue simulation. Nobody is overselling it, and nobody needs to; the interesting bets are not on the material but on the process innovations layered onto it.

The position worth taking is that anyone treating GaAs as a differentiator is mispricing it, and anyone dismissing it because silicon photonics has more momentum is also mispricing it. The specific liabilities are documented and unglamorous: index mismatch with silicon waveguides, 532 nm absorption in AlGaAs/GaAs coatings, irreproducible epitaxy on inadequately prepared substrates, and random dot placement. Each has a credible workaround in the current literature. Value accrues to whoever industrialises those workarounds, not to the material itself.

## Prediction

By 31 December 2027, a measured (not simulated) fibre-coupled single-photon or entangled-pair collection efficiency of at least 40 per cent will be reported from a deterministically positioned GaAs or InGaAs quantum dot in a free-standing circular Bragg grating, matching the FDTD prediction in.

## Evidence base

- 5 May 2026: a transportable ultraviolet clock laser using an ultra-stable cavity with crystalline AlGaAs/GaAs mirror coatings reached fractional frequency instability of about 2 x 10^-16, with acceleration sensitivity no greater than 4(2) x 10^-12 per ms^-2.
- 6 May 2026: AFM nano-oxidation lithography positioned GaAs quantum dots to 51(28) nm radial displacement inside free-standing asymmetric circular Bragg gratings, giving 245-fold photoluminescence enhancement and polarisation imbalance below 5 per cent.
- 5 May 2026: a single-step aspect-ratio-dependent etching process produced monolithic free-standing circular Bragg gratings without bottom reflectors, with FDTD predicting up to 68 per cent free-space extraction and 40 per cent lensed single-mode fibre coupling.
- 14 May 2026: a photon deterministically generated from an InAs/GaAs quantum emitter, mapped into Gottesman-Kitaev-Preskill code space, violated a Bell-like noncontextual hidden-variable inequality by 380 standard deviations.
- 24 June 2026: because AlGaAs/GaAs coatings planned for the A# gravitational-wave detector upgrade absorb the frequency-doubled 532 nm beam, a multi-wavelength stabilisation scheme using a 1596 nm auxiliary beam was proposed and demonstrated on a tabletop.
- 2 June 2026: in a survey of alternative selective-area MBE mask materials, Al2O3 showed promising selectivity within typical GaAs growth temperatures while HfO2 was highly non-selective up to 650 degrees C due to Ga adsorption.
- 16 June 2026: a DFT survey of zincblende III-V and II-VI semiconductors found AlSb, not GaAs, gave the largest visible-light shift-current response.

## Open questions

- Do the free-standing circular Bragg grating designs actually deliver the simulated 68 per cent extraction and 40 per cent lensed-fibre coupling when measured, or does aspect-ratio-dependent etching introduce losses the FDTD model omits?
- Can AFM nano-oxidation positioning at 51(28) nm accuracy be parallelised to wafer-scale throughput, or does deterministic placement remain a one-device-at-a-time technique?
- Will AlGaAs/GaAs coatings survive into a deployed gravitational-wave detector upgrade, given that they force a redesign of arm-length stabilisation to avoid 532 nm absorption?
- Does the proposed epitaxial design for III-V-on-220 nm-silicon coupling work in fabricated devices, or does the (Al)GaAs refractive index keep quantum dot lasers off standard CMOS photonics lines?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
