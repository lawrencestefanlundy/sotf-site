---
type: concept
slug: single-photon-sources
canonical_name: Single-Photon Sources
aliases: []
kind: technology
parent_concepts:
- photonic-systems
- light-sources
related_concepts: []
sources: []
frontier:
- Can the three-body-interaction and ultrastrong-coupling blockade schemes be built in hardware, and do the predicted purities survive the cavity's back-action on the emitter dynamics identified in 2026 05 15 the influence of strong coupling between single photon sourc?
- Does the anomalous saturation caused by excited-state absorption into dark states 2026 08 04 breakdown of the optical saturation regime in molecular sing generalise beyond DBT in anthracene to quantum dots and colour centres, capping achievable brightness across platforms?
- 'Which host wins: telecom-band droplet-etched dots 2026 05 08 local droplet etching assisted quantum dot epitaxy for telec, silicon colour centres with their fabrication and spin-coherence advantages 2026 06 30 single photon emitters and spin photon interfaces in silicon, or room-temperature hBN 2026 06 16 deterministic single photon sources in hexagonal boron nitri?'
- Can electrical injection and electrostatic stabilisation in 2D-material emitters 2026 05 08 electronic and photonic integration of single quantum emitte remove the free-space excitation and post-selection that currently block turnkey operation, and what cryogenic control electronics will drive them given the SiC MOSFET variability at 650 mK 2026 05 05 reproducibility and variability in commercial sic mosfets at?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 25
last_reorg_date: '2026-05-13'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Later (5-10yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 2
sources_30d: 8
recent_mentions: []
neighbors: []
---
**A single-photon source emits exactly one photon per trigger event, and it is the missing component that photonic quantum computing and quantum networks are currently designed around rather than with: 2026 experiments deliver antibunching across many material platforms, but purity, brightness, indistinguishability and telecom-band integration have still not been achieved together in one device.**

## Summary

A single-photon source (SPS) is a device that, when triggered, emits one and only one photon into a defined optical mode. The standard figure of merit is the second-order correlation at zero delay, g²(0), which is 1 for a laser and 0 for a perfect single-photon emitter; values below roughly 0.5 confirm a single quantum emitter, and state-of-the-art work targets 0.1 and below. Three further parameters decide usefulness: brightness or emission efficiency (what fraction of triggers yield a collected photon), indistinguishability (whether successive photons interfere perfectly, required for fusion and Bell-state measurements), and wavelength (telecom bands for fibre, or matched to a spin qubit). A fifth, usually decisive in practice, is integration: whether the emitter can be excited electrically, stabilised against charge noise, and coupled into a waveguide or fibre without free-space alignment and post-selection.

The physics comes in two families. Saturable emitters are single quantum objects that can hold only one excitation at a time: epitaxial semiconductor quantum dots, colour centres in hexagonal boron nitride, silicon carbide and silicon, localised excitons in transition metal dichalcogenides, single organic molecules such as dibenzoterrylene, and acceptor-bound excitons in II-VI materials. Photon blockade is the alternative: a nonlinear cavity-emitter system whose energy ladder is anharmonic enough that absorbing a second photon is forbidden. Conventional and unconventional blockade schemes suffer a purity-brightness trade-off, which recent theory attacks using three-body interactions between one photonic mode and two qubits, or by numerical multi-objective optimisation of the open-system dynamics. A third route, heralded pair generation, is probabilistic by construction and carries multiphoton emission errors.

The parameter that actually decides the field is whether a true SPS is needed at all. In quantum key distribution it largely is not: decoy-state protocols were invented precisely to overcome the limitations of imperfect single-photon sources and are the most widely adopted approach in deployed systems. Verification protocols for delegated quantum computation have likewise been rewritten to replace single-photon sources with trusted local rotations or weak coherent pulses. Where the substitution fails is measurement-based photonic computing: schemes that build caterpillar and lattice graph states directly from single-photon sources, linear optics and heralded measurements need l-2 fewer photons and achieve a 2^(l-2) higher success rate than fusion-based assembly for a state of length l ≥ 3. That exponential is the real economic case for the technology.

## Viability (3/5)

The antibunching evidence is broad and reproducible. Local droplet etching produces symmetric InGaAs quantum dots in InAlAs at telecom C-band with 10⁹/cm² density, in-plane aspect ratio 1.14, 0.2 meV linewidths and g²(0) = 0.07 ± 0.02 under above-band continuous-wave excitation. Focused electron-beam irradiation creates site-controlled room-temperature emitters in hBN with g²(0) of 0.09, 0.12 and 0.16 across three independent flakes. Sb-mediated facet engineering yields axial InGaAs quantum dots at nanowire tips on a GaAs platform with 0.51 ± 0.02 ns lifetimes and pronounced antibunching. An acceptor-bound hole spin in ZnSe shows antibunching with 244 ps radiative recombination.

What is not demonstrated is the full parameter set in one device. The headline numbers of g²(0) ~ 10⁻⁶ to 10⁻⁸, 98.7-99.1% indistinguishability and 99.96% emission efficiency come from a theoretical scheme for a three-level atom in a strong or ultrastrong coupled cavity, not from hardware. Real emitters keep producing surprises that break the two-level-system model on which those designs rest: single DBT molecules under strong resonant drive show anomalous saturation, with fluorescence suppressed rather than saturating and linewidth broadening beyond the two-level prediction, attributed to intensity-dependent excited-state absorption into a short-lived dark state. Even the coupling to the readout circuit is not benign: a cavity used to funnel emission also acts as a spectral filter that distorts the source's own dynamics and photon statistics. Three, not higher: the demonstration base is real but the performance gap to application requirements is unclosed.

**TLDR: Single-photon emission is routine across many platforms; the simultaneous purity, brightness and indistinguishability that applications need exists only in theory papers.**

## Drivers (3/5)

On the demand side, single photons are described across these reviews as the carrier that distributes quantum information over distance and as indispensable core devices for linear optical quantum computing. The sharpest quantified pull is architectural: direct generation of caterpillar graph states from single-photon sources beats fusion-based assembly by a factor 2^(l-2) in success rate, and analyses of heralded Bell-state generation show seed-state quality under loss and multiphoton emission error sets the ceiling for everything built on top of it. Against that, demand is being actively substituted away in the two nearest-term markets: decoy-state QKD exists specifically to tolerate imperfect sources and is the dominant deployed approach, and hardware-efficient verification protocols have removed the single-photon-source requirement in favour of weak coherent pulses.

On the supply side the driver is materials and fabrication capability rather than a market signal. Silicon is attractive because it brings mature nanofabrication, integrated photonics and microelectronics, plus high isotopic purity giving long spin coherence; silicon carbide brings an emerging CMOS platform with defects usable as qubits or emitters. Multiple independent groups are pushing epitaxy, electron-beam patterning and 2D material stacks in parallel, which suggests healthy research supply but no consolidation on a winning platform.

**TLDR: Strong pull from photonic computing and quantum networks, but the QKD market has already engineered around the need for true single photons.**

## Novelty (3/5)

The comparison set is explicit in the literature supplied. Against weak coherent pulses, the alternative is decoy-state protocols, which are a security-proof workaround for source imperfection rather than a fix. Against heralded pair generation, the alternative carries multiphoton emission errors that propagate into Bell-state fidelity and heralding probability. Against probabilistic fusion assembly, deterministic sources plus linear optics and heralded measurement give the l-2 photon saving and 2^(l-2) success-rate gain already cited. That is a genuine categorical advantage, not an incremental one.

Within the SPS field itself, the novelty in this window is mostly mechanism and process, not performance records. Three-body-interaction photon blockade claims to cut the two-photon excitation path entirely and break the purity-brightness trade-off without requiring strong coupling or weak driving. A Liouville-space adjoint optimisation framework reaches roughly 60% design success for g²(0) < 0.1 with bounded brightness across a broad parameter space and no analytical guidance. A proposal for the terahertz regime addresses a band that currently has no deterministic single-photon source at all, projecting 65-92% efficiency and 88-100% purity from a hybrid resonator-nanoparticle cavity. These are design advances awaiting experimental confirmation, which is why this is a 3 rather than a 4.

**TLDR: Deterministic emission is categorically better than attenuated lasers and probabilistic pair sources, but the sources here do not quantify the delivered advantage in working hardware.**

## Diffusion (2/5)

The barriers are stated bluntly in the field's own reviews. Many solid-state platforms still rely on bulky optical excitation, careful alignment and post-selection to achieve useful linewidth, stability and brightness, whereas scalable quantum photonics needs turnkey engines that trigger on demand, resist environmental noise and couple efficiently into fibres or photonic circuits. The specific failure modes being fought are blinking, spectral wandering and charge-noise-induced broadening, addressed by electrical injection, electrostatic stabilisation and Stark tuning, none of which is yet standard. Organic molecules offer negligible dephasing, indefinite photostability and high photon rates, but only at cryogenic temperatures, and even then depart from ideal behaviour under strong drive in a way that depends on matrix quality.

The supporting stack is also immature. Cryogenic control electronics cannot be assumed: commercial SiC power MOSFETs measured from 300 K down to 650 mK show large gate hysteresis, threshold voltage shifts and subthreshold swing deterioration, attributed to carrier freeze-out and interface trap density, which the authors flag as a challenge for reliable cryo-CMOS or quantum device use. Room-temperature hBN emitters partly escape the cryogenic problem and survive heating to 300 °C with reversible thermal quenching, but their g²(0) of 0.09-0.16 and defect-chemistry uncertainty leave them short of computing-grade indistinguishability. Finally, adoption is discouraged by the existence of adequate substitutes in the deployed QKD and verification use cases.

**TLDR: Cryogenics, charge noise, blinking, alignment and post-selection keep almost every high-performance source in the laboratory.**

## Impact (4/5)

The value is leveraged rather than direct. Photonic architectures build cluster and repeater graph states by fusing small entangled seeds, so seed-state quality sets a baseline for every downstream application in communication, sensing and computing. Replacing probabilistic fusion with direct generation from deterministic sources changes resource counts exponentially in the state length. Combined with a spin, the same emitters become spin-photon interfaces that store quantum states for extended periods and form the basis of quantum networks and repeaters, which is the stated motivation for the silicon colour-centre and erbium programme.

Secondary impact spreads wider than quantum computing. Telecom C-band epitaxial dots would let entangled-photon distribution run over existing fibre infrastructure, monolithic nanowire emitters point at integration on silicon, and a deterministic terahertz source would open a band that currently has none. This is not a 5 because the sources also demonstrate that the largest deployed application, QKD, has already found a workable substitute.

**TLDR: A manufacturable deterministic source unlocks the resource-state economics of photonic quantum computing and the repeater layer of quantum networks.**

## Timing Later (5-10yr)

None of the supplied sources gives a roadmap or a date, so this band is inferred from maturity signals rather than stated schedules. The signals point the same way: reviews published in 2026 still frame electronic and photonic integration of quantum emitters as a survey of routes rather than an achieved capability, and the silicon review of June 2026 explicitly summarises open challenges towards coherent single-photon sources and scalable spin-photon interfaces. The best purity and efficiency figures in this window are simulation outputs.

A nearer-term subset exists. Room-temperature, site-controlled hBN emitters written by electron beam are usable for experiments now, and telecom-band droplet-etched dots are at the materials-characterisation stage. Component-level lab use is Now; the systems that would make the technology commercially decisive are Later.

**TLDR: Laboratory emitters are good now; turnkey, electrically driven, circuit-integrated sources with computing-grade indistinguishability are not close.**

## Overrated or underrated? Fairly rated

The field's self-description is accurate: single-photon sources are correctly identified as a long-standing bottleneck for linear optical quantum computing rather than a solved input, and nobody in these sources claims otherwise. The demonstrations are real, spread across at least six host materials, and reproducible enough that g²(0) below 0.2 is now table stakes rather than a result. What is not yet delivered is any single device combining sub-0.1 purity, high brightness, high indistinguishability, telecom wavelength and on-chip coupling, and the most spectacular numbers in this literature are theoretical.

The caution investors should take from these sources is the substitution risk. Two independent lines of work here remove the requirement for a true single-photon source: decoy-state security proofs for QKD and hardware-efficient verification protocols that swap single photons for weak coherent pulses. The value therefore concentrates almost entirely in measurement-based photonic computing and the repeater layer, where the 2^(l-2) resource-state advantage cannot be bought with protocol cleverness. Judge any SPS venture on whether it is targeting that market, and on whether its indistinguishability numbers come from hardware or from a simulation.

## Prediction

By 31 December 2028, no peer-reviewed experiment will report a single solid-state or cavity-QED single-photon source simultaneously achieving g²(0) below 10⁻⁴, indistinguishability above 98% and emission efficiency above 95%, the combination projected by the 2026 ultrastrong-coupling proposal.

## Evidence base

- 8 May 2026: local droplet etching produces symmetric InGaAs quantum dots in InAlAs at telecom C-band, density 10⁹/cm², aspect ratio 1.14, 0.2 meV linewidths, g²(0) = 0.07 ± 0.02 under above-band CW excitation.
- 16 June 2026: focused electron-beam irradiation creates deterministic room-temperature emitters in hBN with g²(0) of 0.09, 0.12 and 0.16 across three flakes, a phonon sideband near 575 nm and reversible thermal quenching up to 300 °C.
- 2 July 2026: a theoretical three-level-atom cavity scheme projects g²(0) ~ 10⁻⁶ with 98.73% indistinguishability in strong coupling, and pulsed ultrastrong-coupling performance of 99.96% efficiency, 98.98% indistinguishability and 99.99% purity.
- 6 August 2026: direct generation of caterpillar graph states from single-photon sources and linear optics needs l-2 fewer photons and achieves 2^(l-2) higher success rate than fusion-based assembly for l ≥ 3.
- 30 June 2026: decoy-state QKD is described as the most widely adopted approach for overcoming the limitations of imperfect single-photon sources, indicating the deployed market has engineered around the technology.
- 4 August 2026: single DBT molecules under strong resonant drive show fluorescence suppression and excess linewidth broadening rather than saturation, explained by intensity-dependent excited-state absorption into a dark state.
- 5 May 2026: commercial SiC MOSFETs measured from 300 K to 650 mK show large gate hysteresis, threshold shifts and subthreshold swing degradation, a challenge for the cryo-CMOS electronics that integrated quantum photonics would require.

## Open questions

- Can the three-body-interaction and ultrastrong-coupling blockade schemes be built in hardware, and do the predicted purities survive the cavity's back-action on the emitter dynamics identified in?
- Does the anomalous saturation caused by excited-state absorption into dark states generalise beyond DBT in anthracene to quantum dots and colour centres, capping achievable brightness across platforms?
- Which host wins: telecom-band droplet-etched dots, silicon colour centres with their fabrication and spin-coherence advantages, or room-temperature hBN?
- Can electrical injection and electrostatic stabilisation in 2D-material emitters remove the free-space excitation and post-selection that currently block turnkey operation, and what cryogenic control electronics will drive them given the SiC MOSFET variability at 650 mK?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
