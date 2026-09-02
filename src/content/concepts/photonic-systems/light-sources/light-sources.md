---
type: concept
slug: light-sources
canonical_name: Light Sources
aliases: []
parent_concepts:
- photonic-systems
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2026-05-02-energetiq-euv-light-sources]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
descendants:
- dfb-dbr-lasers
- external-laser-source
- frequency-combs
- laser-display-light-engines
- lasers
- photonic-clock-oscillator
- quantum-cascade-lasers
- semiconductor-optical-amplifier
- single-photon-sources
- vcsels
mention_count: 79
scorecard:
  viability: 4
  drivers: 3
  novelty: 4
  diffusion: 2
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Underrated
scorecard_status: draft
frontier:
- Do measured extraction and fibre-coupling efficiencies for free-standing circular Bragg gratings approach the simulated 68% and 40%, or does fabrication cost most of the predicted gain 2026 05 05 free standing circular bragg gratings enabling efficient gaa?
- What fraction of AFM-positioned quantum dots fall inside the 50 nm displacement tolerance across a wafer, given the reported 51(28) nm accuracy 2026 05 06 deterministic positioning of circular bragg gratings using a?
- Can the crystal-edge and coating phase contributions identified in linear optical parametric oscillators be controlled well enough to make squeezer thresholds predictable at manufacture 2026 06 02 phase sensitive crystal edge effects in linear optical param?
- Are microwatt-level chip-scale blue and nanowatt mid-IR outputs sufficient for atomic clock, sensing or spectroscopy applications, or is a power scaling route required 2026 05 05 nonlinear frequency translation in micromachined rb vapor ce?
- Do the theoretical advantages claimed for correlated and superradiant sources survive contact with real mode-matching and synchronisation constraints, given that these constraints already forced a switch to a narrowband laser in a covert-communication experiment 2026 05 29 toward practical two way covert communication?
sources_7d: 7
sources_30d: 18
recent_mentions:
- slug: 2026-05-02-energetiq-euv-light-sources
  title: Energetiq EUV light sources
  date: '2026-05-02'
  kind: web
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2023-08-31-e13-chiplets-how-chip-lego-is-driving
  title: '🔮 E13: Chiplets - How Chip Lego is Driving AI Progress'
  date: '2023-08-31'
  kind: substack
neighbors: []
---
**Light sources are the emitters that set the ceiling on every photonic system, and the 2026 literature shows the frontier has moved from making light at all to making it deterministically, on-chip, at the right wavelength and with controlled quantum statistics.**

## Summary

A light source is any device that converts energy into photons with a controlled set of properties: wavelength, linewidth, coherence, directionality, polarisation, and, increasingly, photon statistics. Within photonic systems it is the upstream component that fixes what everything downstream can do. A quantum network cannot exceed the purity and brightness of its single-photon source; an interferometric sensor cannot exceed the squeezing of its optical parametric oscillator; a time-resolved spectroscopy beamline cannot exceed the coherence and repetition rate of its free-electron laser.

The current research front splits into three mechanisms. First, gain-based emitters: semiconductor lasers scaled down to nanowires, where two ZnO nanowires separated by under 10 nm have been shown to frequency-lock, aligning all or a subset of their lasing modes and suppressing multi-mode behaviour; microcavity lasers whose emission is governed by chaotic ray dynamics rather than simple mode structure; and rare-earth emitters, where erbium implanted into silicon nitride metasurfaces gave a photoluminescence enhancement of about 18 and a tenfold lifetime reduction from the Purcell effect, offering a CMOS-compatible active source at telecom wavelength. Second, nonlinear conversion: chip-scale micromachined rubidium vapour cells generating roughly 20 microwatts of coherent blue light with a 1 MHz linewidth by four-wave mixing, outperforming a conventional glassblown cell in efficiency despite a much shorter interaction length; subwavelength resonators producing photon pairs by spontaneous parametric down-conversion at up to 0.45 Hz/mW; and twisted van der Waals crystals of NbOBr2 giving polarisation-entangled telecom photons with Bell-state fidelity above 95%. Third, single quantum emitters, principally epitaxial quantum dots embedded in circular Bragg grating cavities.

The parameters that decide whether any of this leaves the lab are unglamorous. Extraction and fibre-coupling efficiency: free-standing circular Bragg gratings made in a single aspect-ratio-dependent etch step are simulated to reach 68% free-space extraction and 40% coupling into a lensed single-mode fibre. Placement accuracy: atomic force microscopy nano-oxidation lithography has positioned quantum dots to a radial displacement of 51(28) nm, yielding a 245-fold photoluminescence enhancement with polarisation imbalance below 5%. Wavelength: local droplet etching produces symmetric telecom C-band dots with 0.2 meV linewidths and g2(0) = 0.07 ± 0.02. And reproducibility, which is where the field is weakest: nominally identical linear optical parametric oscillators show large threshold variations traceable to crystal-edge termination and coating phases.

## Viability (4/5)

On measured quantities the evidence is solid. Single-photon emission at telecom C-band with g2(0) = 0.07 ± 0.02 and 0.2 meV linewidths from droplet-etched dots, Bell-state fidelity above 95% with a coincidence-to-accidental ratio of about 335 from twisted NbOBr2, a 245-fold photoluminescence enhancement from a deterministically positioned dot in a free-standing cavity, a 30-beam array of polarisation-squeezed light at 2.03 dB from a single vapour cell, and roughly 20 microwatts of coherent blue light from a micromachined cell. These are working devices, not proposals.

Two things hold the score below 5. The headline efficiency numbers for the most application-relevant architecture, quantum dots in circular Bragg gratings, are finite-difference time-domain predictions of 68% extraction and 40% fibre coupling rather than measurements. And the parametric-oscillator work shows that nominally similar squeezers differ substantially in threshold because of microscopic phase contributions from crystal edges and coatings, which is a direct statement that yield and repeatability are not yet under control. Several results in the set are theory only, including the 65 dB correlation isolation from interference-amplified chirality and the factor-N Cramer-Rao improvement claimed for superradiant LIDAR.

**TLDR: The physics is demonstrated repeatedly and independently; the weak points are simulated efficiency figures and device-to-device reproducibility.**

## Drivers (3/5)

Supply is the stronger half. Independent groups are attacking the same problem, deterministic bright emission, through different process routes: aspect-ratio-dependent etching to avoid flip-chip bonding and its strain penalty, room-temperature AFM nano-oxidation to place dots relative to cavities, local droplet etching for symmetric telecom dots, ion implantation into silicon nitride for CMOS-compatible active layers, micromachining and anodic bonding for alkali vapour cells, and van der Waals stacking for nonlinear crystals. All of these reduce process complexity rather than add to it, which is the pattern that precedes manufacturability.

**TLDR: Supply-side fabrication routes are multiplying and converging on chip scale; demand is asserted by application need rather than demonstrated by market evidence in these sources.**

## Novelty (4/5)

There are also genuine mechanism firsts rather than incremental gains. Frequency locking between nanowire lasers at sub-10 nm gaps is described as previously unexplored, and is distinguished from earlier coupled-cavity nanowire lasers that relied on static filtering such as the Vernier effect. The directional and spectral distributions of down-converted photon pairs from a single nanoresonator are reported as a first measurement, enabled by pair rates of up to 0.45 Hz/mW, and used to validate an extended quasi-normal-mode theory. Photon thermalisation is demonstrated in a pumped dye solution with colloidal scatterers, extending a phenomenon previously confined to engineered resonant cavities. The deduction from 5 is that most of these are single-device demonstrations without a competing-technology benchmark on the same figure of merit.

**TLDR: Multiple credible first-of-kind and record claims, several with quantified margins over the previous best approach.**

## Diffusion (2/5)

The sources name the barriers themselves. Random spatial distribution of epitaxial quantum dots is the stated obstacle to deterministic cavity coupling, and the best answer here is 51(28) nm radial displacement with robust emission demonstrated only up to 50 nm displacement, meaning the process tolerance and the achieved accuracy are roughly the same size. Conventional cavity architectures are noted to require multi-layer processing or flip-chip bonding that introduces strain and limits scalability. Reproducibility is explicitly a problem for squeezed-light sources, where nominally similar oscillators show large threshold variations from crystal-edge and coating phases.

System integration is the second barrier. The covert-communication work is the clearest evidence: broadband classical and quantum sources offer high theoretical throughput but the mode-matching and phase-synchronisation requirements made them impractical, so the experiment used a narrowband laser and proposed a correlator-based receiver as a workaround. Absolute output is also modest where it matters: roughly 20 microwatts of blue and 50 nanowatts of collected mid-IR from the chip-scale vapour cell, 0.45 Hz/mW pair rates from a nanoresonator, and 2.03 dB across a 30-beam squeezed array. The silicon nitride erbium result is the exception with a plausible short diffusion path, because it is presented as a pathway to integrating active sources into CMOS-compatible photonic devices.

**TLDR: Positioning yield, cryogenic operation, absolute power levels and device-to-device variation all stand between these demonstrations and deployment.**

## Impact (4/5)

The leverage is structural. If a telecom C-band emitter combining low g2(0) with high fibre-coupled extraction becomes manufacturable, it removes the brightness bottleneck for quantum repeaters and entanglement distribution, which is the stated motivation across the quantum-dot papers. An efficient erbium source monolithically integrated in silicon nitride addresses the long-standing absence of active emitters in a CMOS-compatible platform. On the classical side, moving fully coherent EUV free-electron lasers from kilohertz to higher repetition rates by removing the hundred-megawatt seed requirement changes what time-resolved spectroscopy experiments are feasible at a whole class of facility.

Secondary impacts are real but less certain because they are theoretical. Superradiant LIDAR claims a Cramer-Rao bound reduced by a factor N in the number of thermal sources, improving further with correlation order, and interference-amplified chirality claims correlation and brightness isolations up to 65 dB and 17.3 dB as a route to directional nonclassical sources. Work quantifying the Holevo bound and effective secret-bit rates for four-wave-mixing fields in a two-dimensional perovskite, finding a 2.6 to 5.8% reduction when coherence time is included as a degree of freedom, shows the field beginning to attach communication-relevant metrics to source physics, which is a precondition for impact being realised rather than asserted.

**TLDR: Source quality gates quantum networking, integrated photonics and several sensing modalities, so improvements propagate widely.**

## Timing Soon (2-5yr)

The timeline is not uniform across the category. The seeded free-electron laser result is an experimental demonstration on a large facility and can plausibly be adopted as a beamline configuration change on a short horizon. Micromachined vapour cells are already a versatile chip-scale platform producing measured blue and mid-IR output, and erbium-doped silicon nitride metasurfaces sit close to an existing foundry process.

The quantum-dot line is the slower one, and it is the line that matters for quantum networking. Placement accuracy of 51(28) nm against a 50 nm tolerance and extraction efficiencies still quoted from simulation indicate a two-to-five year window before device-level performance is demonstrated at reproducible yield, with fielded deployment later. The nanoresonator and van der Waals photon-pair sources are earlier still: brightness at the 0.45 Hz/mW level is a physics result rather than a component specification.

**TLDR: Facility-scale and CMOS-adjacent results are usable now; deterministic quantum sources need another process-maturity cycle.**

## Overrated or underrated? Underrated

Attention in quantum photonics tends to concentrate on qubit counts, detectors and error correction. The evidence here says the binding constraint is upstream, in the source. The single most informative paper in the set is the least eye-catching one: nominally identical optical parametric oscillators show large threshold variations because of crystal-edge termination and coating phases. That is a manufacturing-yield problem dressed as a physics problem, and it is the same class of problem as random quantum-dot placement and strain from flip-chip bonding. Progress on it is worth more than another record fidelity figure.

The underrated call is specifically about the process engineering, not the claims. Single-step etching, room-temperature AFM oxidation lithography, droplet etching for symmetric telecom dots, ion implantation into silicon nitride and anodically bonded vapour cells are all moves towards fewer steps and standard toolsets, and that is what determines whether a source becomes a component. Against that, anyone reading the theoretical results as near-term capability should discount heavily: the 65 dB isolation figure and the factor-N LIDAR gain are calculations, and the covert-communication experiment shows what happens when a broadband quantum source meets a real system, which is that it gets replaced by a laser.

## Prediction

By 31 December 2028, at least one peer-reviewed deterministic quantum-dot-in-circular-Bragg-grating source will report a measured, not simulated, fibre-coupled photon extraction efficiency above 40% at a telecom wavelength; if the best measured figure published by then remains below 20%, the extraction-efficiency roadmap implied by the 68% FDTD predictions should be treated as stalled.

## Evidence base

- On 6 May 2026, AFM nano-oxidation lithography was reported to position GaAs quantum dots to 51(28) nm radial displacement inside free-standing asymmetric circular Bragg gratings, giving a 245-fold photoluminescence enhancement and polarisation imbalance below 5%.
- On 5 May 2026, a single-step aspect-ratio-dependent etch process for monolithic free-standing circular Bragg gratings was simulated to reach 68% free-space extraction and 40% coupling into a lensed single-mode fibre without bottom reflectors.
- On 8 May 2026, local droplet etching produced telecom C-band InGaAs quantum dots at 10^9/cm2 density with in-plane aspect ratio 1.14, 0.2 meV linewidths and g2(0) = 0.07 ± 0.02.
- On 15 May 2026, 90 degree twisted NbOBr2 was reported to give polarisation-entangled telecom photons with Bell-state fidelity above 95%, coincidence-to-accidental ratio of about 335 and brightness roughly an order of magnitude above recent TMD-based telecom sources.
- On 5 May 2026, erbium implanted into Si3N4 nanocylinder metasurfaces gave a photoluminescence enhancement of about 18 at 390 nm radius and a nearly tenfold lifetime reduction attributed to the Purcell effect, presented as a route to CMOS-compatible active sources.
- On 28 May 2026, a fully coherent EEHG free-electron laser was demonstrated using a single sub-microjoule seed, removing the hundred-megawatt peak-power seed lasers and dual-laser synchronisation that had restricted operation to kilohertz repetition rates.
- On 2 June 2026, phase-sensitive crystal-edge effects were shown to produce large threshold variations between nominally similar linear optical parametric oscillators, identifying reproducibility as an unresolved problem for squeezed-light sources.

## Open questions

- Do measured extraction and fibre-coupling efficiencies for free-standing circular Bragg gratings approach the simulated 68% and 40%, or does fabrication cost most of the predicted gain?
- What fraction of AFM-positioned quantum dots fall inside the 50 nm displacement tolerance across a wafer, given the reported 51(28) nm accuracy?
- Can the crystal-edge and coating phase contributions identified in linear optical parametric oscillators be controlled well enough to make squeezer thresholds predictable at manufacture?
- Are microwatt-level chip-scale blue and nanowatt mid-IR outputs sufficient for atomic clock, sensing or spectroscopy applications, or is a power scaling route required?
- Do the theoretical advantages claimed for correlated and superradiant sources survive contact with real mode-matching and synchronisation constraints, given that these constraints already forced a switch to a narrowband laser in a covert-communication experiment?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
