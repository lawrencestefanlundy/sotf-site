---
type: concept
slug: atomic-clocks
canonical_name: Atomic Clocks
aliases: []
kind: technology
parent_concepts:
- sensing
- quantum-sensing
related_concepts: []
sources: []
frontier:
- Are the reported discrepancies of roughly 1 x 10^-16 in 87Sr ratios and 1.6 x 10^-17 in Al+/Yb resolved as systematics, and do independent laboratories reproduce the 3.2 x 10^-18 result 2026 07 20 atomic clock frequency ratios with fractional uncertainty le?
- Can a thorium-229 nuclear clock reach a systematic uncertainty budget competitive with 27Al+, 171Yb or 87Sr, rather than only demonstrating shot-noise-limited instability scaling against a Yb+ reference 2026 06 04 a thorium 229 optical nuclear clock with feedback loop?
- Do the integrated UV modulator, narrow-linewidth visible laser and microring comb combine into a working portable optical clock, and at what stability penalty relative to a cryogenic-cavity system 2026 05 05 thin film lithium tantalate for ultraviolet integrated elect 2026 07 28 ultranarrow linewidth self injection locked tunable blue gan?
- Do entanglement-enhanced and weak-measurement protocols deliver a net stability gain in a running clock with realistic loss, or does the loss-postselection required for the 0.85(1) qutrit fidelity erase the advantage 2026 08 07 qutrit entanglement and joint multi parameter estimation in  2026 07 21 extending the dynamic range in quantum frequency estimation ?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 15
last_reorg_date: '2026-05-13'
scorecard:
  viability: 5
  drivers: 4
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors: []
---
**Atomic clocks lock an oscillator to a fixed atomic or nuclear transition frequency; the best optical versions now agree to 3.2 parts in 10^18, meeting a stated milestone criterion for redefining the SI second, while a parallel effort tries to shrink the same physics onto photonic chips and into deployed networks.**

## Summary

An atomic clock disciplines a local oscillator to a transition in an atom, ion or nucleus, whose frequency is set by nature rather than by a manufactured artefact. Caesium microwave standards define the current SI second. Optical clocks interrogate transitions some five orders of magnitude higher in frequency, which divides the same fractional error over far more cycles and buys stability. The frontier platforms in the sources are trapped ions (27Al+), neutral atoms in optical lattices (171Yb, 87Sr) and atoms in optical tweezers (88Sr).

The performance-limiting parameters are not the atoms. They are the local oscillator, the environment and the readout. A clock laser must be quiet enough to interrogate a hertz-wide line, which today means a cryogenic reference cavity; Brownian noise in the thin-film mirror coatings of those cavities is the dominant fundamental limit. Laser frequency noise at high Fourier frequencies is not fixed by cavity locking alone, and one recent demonstration combined a cryogenic silicon cavity with an integrated Brillouin laser to suppress noise across more than seven decades, giving sub-hertz phase-integrated linewidth and sub-hertz Rabi spectroscopy on a three-dimensional 87Sr lattice clock. On the readout side, decoherence of the local oscillator produces phase slip errors that cap useful interrogation time, and both weak-measurement protocols and entangled multi-level probes are being proposed and tested to push past that.

Two distinct programmes sit under the same heading and should be judged separately. The first is metrological: comparing the best clocks well enough to redefine the second and to test fundamental physics. The second is engineering: making clocks small, cheap and robust enough to deploy. That second track runs through photonic integration, including an integrated ultraviolet electro-optic modulator on thin-film lithium tantalate aimed at portable clocks, narrow-linewidth visible diode lasers, and microring frequency combs for optical-to-microwave division.

A third path bypasses electron-shell transitions entirely. Thorium-229 has a nuclear transition at 148 nm that can be excited by laser light in a doped crystal, promising a solid-state clock that is more robust against external perturbations and more sensitive to variations in fundamental constants.

## Viability (5/5)

This is not a question of whether the physics works. Frequency ratios between 27Al+, 171Yb and 87Sr clocks have been measured with total fractional uncertainties at or below 3.2 x 10^-18, explicitly meeting a milestone criterion for redefinition of the SI second. Supporting subsystems are also demonstrated rather than proposed: a hybrid cryogenic-cavity plus Brillouin laser delivering sub-hertz linewidth and validated by sub-hertz Rabi spectroscopy on a real lattice clock, and genuine two-qutrit entanglement with loss-postselected fidelity 0.85(1) used for joint multi-parameter estimation on an optical clock platform.

The honest caveat sits inside the same paper that supplies the headline. Ratios disagreed with the group's own previous measurements by roughly 1 x 10^-16 for 87Sr and 1.6 x 10^-17 for Al+/Yb, which the authors use to argue for repeated high-precision comparisons across different laboratories. Systematic reproducibility, not statistical precision, is the live problem. Nuclear clocks are a full generation behind: a thorium-229 clock has been closed as a feedback loop against a Yb+ ion clock with shot-noise-limited instability scaling, which is a first-of-kind result rather than a competitive uncertainty budget.

**TLDR: Optical clocks are demonstrated hardware agreeing at parts in 10^18 across three independent atomic species.**

## Drivers (4/5)

Demand: the redefinition of the SI second is a formal, institutional driver with published criteria that the field is now measuring itself against. Beyond metrology, distributed quantum networking needs timing at every node for entanglement distribution, teleportation and swapping, and existing solutions such as White Rabbit constrain topology, scalability and free-space or satellite deployment. Clock-based tests of fundamental physics are a further pull, with thorium-229 offering enhanced sensitivity for such tests.

Supply: the component stack is moving quickly and independently of any single clock architecture. Integrated ultraviolet modulation on thin-film lithium tantalate has reached a VpiL of 85 mV.cm at 375 nm with 1.3 dB insertion loss, up to four orders of magnitude better in bandwidth per VpiL than bulk crystals, explicitly targeted at portable atomic clocks. A self-injection-locked blue GaN DFB laser reaches 170 Hz intrinsic linewidth at 452 nm with 11 mW fibre output and mode-hop-free tuning over 600 MHz. Microring frequency combs generated by four-wave mixing need low input power because of high resonator quality factor. Each of these removes a specific bulk-optics component from the bill of materials.

## Novelty (4/5)

The comparison that matters is against the caesium microwave standard that defines the second today. Reaching total fractional uncertainties at or below 3.2 x 10^-18 and satisfying a redefinition milestone criterion is the field's own statement that the incumbent has been surpassed. Within the optical class, thorium-229 is positioned as potentially rivalling or outperforming electron-shell clocks and being more robust against external perturbations, with the added advantage that the nuclei sit in a millimetre-sized room-temperature calcium fluoride crystal rather than a trap. Detecting the nuclear resonance in absorption rather than fluorescence, using under 1 nW of continuous-wave 148 nm light, removes the slow fluorescence decay from the signal chain and speeds acquisition.

Component-level margins are quantified where they matter. The TFLT UV modulator claims up to four orders of magnitude improvement in bandwidth per VpiL over bulk technologies. The coating-free total-internal-reflection resonator removes the dominant Brownian coating noise term of conventional reference cavities while reaching a 50 mm^3 mode volume comparable to state-of-the-art cavities, albeit at a finesse of only 1225. For network timing, the improvement is not precision but architecture: independently running miniature rubidium clocks plus post-processing approach White Rabbit performance without the dedicated link.

**TLDR: Optical clocks are good enough to displace the caesium definition, and several supporting components beat bulk incumbents by orders of magnitude.**

## Diffusion (3/5)

The barrier is visible in the best result itself: the 3.2 x 10^-18 ratio measurements depended on a common ultrastable reference delivered to all clocks over a 3.6 km phase-stabilised fibre, and state-of-the-art clock lasers still require a cryogenic silicon cavity even when supplemented by an integrated Brillouin laser. That is national-laboratory infrastructure, not a product. Reproducibility across institutions is unresolved, with discrepancies at the 1 x 10^-16 level against earlier measurements from the same group.

The lower tier diffuses now. Miniature rubidium clocks have been run at three geographically separated nodes on a deployed metropolitan telecom fibre network, stable over continuous eight-hour operation, delivering Hong-Ou-Mandel visibility above 70 per cent that is statistically equivalent to a dedicated White Rabbit link. Between these tiers, the integrated photonics needed for a portable optical clock exist as separate demonstrations rather than an assembled system. The sources do not show a full chip-scale optical clock, so the integration step remains unevidenced.

**TLDR: Miniature microwave clocks already deploy in the field; optical clocks remain laboratory instruments tethered to cryogenic cavities and kilometre-scale fibre links.**

## Impact (4/5)

Redefinition of the second propagates into every derived SI unit and into the timing layer of navigation, telecommunications and finance, and the sources establish that the technical criterion for it has now been met. Clock comparisons at this level also serve as instruments for testing fundamental principles of physics, an application where thorium-229 offers enhanced sensitivity. Frequency-stable lasers derived from the same work underpin high-fidelity quantum state manipulation for quantum sensing and computation more broadly, and coating noise reduction transfers directly to gravitational-wave detectors.

The near-term systems impact is clearest in quantum networking, where removing dedicated timing-distribution infrastructure lifts constraints on topology, scalability and free-space or satellite deployment. What the sources do not provide is any market sizing, cost figure or commercial deployment count, so the score reflects demonstrated scientific and infrastructural leverage rather than a measured economic case.

**TLDR: Redefining the base unit of time and enabling deployable quantum-network timing are large, but the sources quantify scientific rather than commercial value.**

## Timing Now (0-2yr)

The laboratory milestone is achieved, not forecast: ratio uncertainties at or below 3.2 x 10^-18 already meet a stated criterion for redefining the second. Deployed microwave-clock timing for quantum networks is also demonstrated on real metropolitan fibre today.

The other two threads run later and the sources do not date them. Portable optical clocks depend on integrating UV modulation, narrow-linewidth visible lasers and comb division into one package, and the cited work delivers only the individual components. Thorium-229 has just closed its first feedback loop and demonstrated continuous-wave absorption detection; no source gives an uncertainty budget competitive with optical clocks, so treat that branch as unresolved rather than imminent.

**TLDR: The redefinition-grade metrology has already arrived; portable optical clocks and nuclear clocks are on separate, later clocks.**

## Overrated or underrated? Fairly rated

The performance claims are real, independently structured around three atomic species, and self-critical about their own reproducibility. There is no credibility gap here of the kind common in quantum technology. Equally, nothing in the sources suggests a near-term commercial inflection: the best clocks need cryogenic cavities and kilometre-scale phase-stabilised fibre, and the deployed field results use miniature rubidium clocks that are an older, lower-performance class.

If there is an underrated slice, it is the component layer rather than the clocks. An integrated UV modulator with four orders of magnitude better bandwidth per VpiL than bulk crystals, a 170 Hz linewidth blue diode laser and a coating-free reference resonator each remove a specific bulk-optics obstacle, and their value is not confined to clocks. Investors chasing the clock itself are buying a national-laboratory instrument; the supply chain feeding it is the more tractable position.

## Prediction

By 31 December 2028, at least one laboratory other than the group reporting will publish an optical clock frequency ratio with total fractional uncertainty at or below 3.2 x 10^-18.

## Evidence base

- 2026-07-20: Frequency ratios between 27Al+, 171Yb and 87Sr clocks measured with total fractional uncertainty at or below 3.2 x 10^-18, meeting a milestone criterion for redefinition of the SI second, using a common ultrastable reference over 3.6 km of phase-stabilised fibre.
- 2026-07-20: The same work reports discrepancies against its own earlier measurements of about 1 x 10^-16 for 87Sr ratios and 1.6 x 10^-17 for Al+/Yb.
- 2026-06-04: A thorium-229 nuclear clock was closed as a feedback loop by stabilising a continuous-wave laser to the 148 nm nuclear transition in a millimetre-sized room-temperature CaF2 crystal, compared against a Yb+ single-ion clock.
- 2026-05-29: A cryogenic silicon cavity combined with an integrated Brillouin laser suppressed frequency noise over more than seven decades, giving under 1 Hz phase-integrated linewidth and 0.2 Hz^2/Hz above 10 MHz, verified by sub-hertz Rabi spectroscopy on a 3D 87Sr lattice clock.
- 2026-06-15: Independently running miniature rubidium clocks plus post-processing synchronised three nodes on deployed metropolitan telecom fibre for eight continuous hours, giving Hong-Ou-Mandel visibility above 70 per cent, statistically equivalent to a White Rabbit link.
- 2026-05-05: A thin-film lithium tantalate UV electro-optic modulator achieved VpiL of 85 mV.cm at 375 nm, 22.7 dB extinction ratio and 1.3 dB insertion loss, up to four orders of magnitude better in bandwidth per VpiL than bulk technologies, targeted at portable atomic clocks.
- 2026-08-03: A coating-free monolithic fused silica total-internal-reflection resonator reached finesse 1225 with a 50 mm^3 mode volume, removing the Brownian coating noise that limits conventional reference cavities.

## Open questions

- Are the reported discrepancies of roughly 1 x 10^-16 in 87Sr ratios and 1.6 x 10^-17 in Al+/Yb resolved as systematics, and do independent laboratories reproduce the 3.2 x 10^-18 result?
- Can a thorium-229 nuclear clock reach a systematic uncertainty budget competitive with 27Al+, 171Yb or 87Sr, rather than only demonstrating shot-noise-limited instability scaling against a Yb+ reference?
- Do the integrated UV modulator, narrow-linewidth visible laser and microring comb combine into a working portable optical clock, and at what stability penalty relative to a cryogenic-cavity system?
- Do entanglement-enhanced and weak-measurement protocols deliver a net stability gain in a running clock with realistic loss, or does the loss-postselection required for the 0.85(1) qutrit fidelity erase the advantage?

---
*Assessment drafted 2026-08-31 from up to 14 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
