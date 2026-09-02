---
type: concept
slug: indium-gallium-arsenide
canonical_name: Indium Gallium Arsenide
aliases:
- InGaAs
- indium gallium arsenide
- In(x)Ga(1-x)As
parent_concepts:
- compound-semiconductors
related_concepts:
- indium-arsenide
- indium-phosphide
- gallium-arsenide
- ingaas-swir-sensors
sources:
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
scorecard:
  viability: 5
  drivers: 4
  novelty: 2
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 25
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors:
- slug: indium-arsenide
  name: Indium Arsenide
  path: /materials/substrates/indium-arsenide/
  macro: materials
- slug: indium-phosphide
  name: Indium Phosphide (InP)
  path: /materials/substrates/indium-phosphide/
  macro: materials
- slug: gallium-arsenide
  name: Gallium Arsenide (GaAs)
  path: /materials/substrates/gallium-arsenide/
  macro: materials
- slug: ingaas-swir-sensors
  name: InGaAs SWIR Sensors
  path: /sensing/imaging/ingaas-swir-sensors/
  macro: sensing
---
**InGaAs is the workhorse III-V alloy for anything that has to emit, detect or amplify light at telecom wavelengths, where silicon is blind, and the live question is not whether it works but whether it can be integrated onto silicon and silicon nitride photonic chips at scale.**

## Summary

Indium gallium arsenide (InGaAs) is a ternary compound semiconductor, an alloy of indium arsenide and gallium arsenide whose bandgap can be tuned by composition. Its practical significance is that the bandgap can be pushed well below silicon's, so InGaAs absorbs and emits at the 1550 nm telecom band and beyond, where silicon photodiodes are transparent. Source material notes this bandgap limitation directly: silicon single-photon avalanche diodes are mature and run at room temperature but cannot reach 1550 nm, while InGaAs-based SPADs can. It is normally grown epitaxially on indium phosphide substrates and used in heterostructures with InP, InAlAs or GaAs, which supply the barriers, passivation and lattice template.

The material appears in the literature in three distinct roles. First, as a detector absorber: gated InGaAs/InP SPADs are described as the mature non-cryogenic alternative to superconducting detectors for quantum key distribution, and GHz-gated arrays have been coupled to low-loss silica waveguides to build hybrid QKD receivers delivering secure key rates above 2 Mbps at short distance and 15 kbps over 100 km of fibre. Second, as an emitter: self-assembled InGaAs quantum dots are among the leading on-demand single-photon and entangled-photon sources, including energy-time entanglement from an InGaAs/GaAs dot grown monolithically on silicon. Third, as an active electronic layer bonded onto other platforms, for example epitaxial InGaAs transferred onto lithium niobate on insulator to build a surface-acoustic-wave acoustoelectric amplifier.

The parameters that decide InGaAs's future are not exotic. For detectors: quantum efficiency, dark count rate and afterpulsing, all of which the room-temperature van der Waals detector work cites as InGaAs weaknesses alongside environmental hazards in fabrication. For integration: whether InGaAs can be grown or bonded onto silicon and silicon nitride without losing performance, with a heterogeneously integrated InGaAs-on-InP uni-travelling-carrier balanced photodetector on thin-core silicon nitride reported at 0.92 GHz bandwidth. For reliability: defect and surface chemistry, where trap states in an InP/InGaAs stack on silicon become increasingly active below 140 K and suppress current down to 5 K, and where ambient oxidation of a bare InGaAs surface extinguishes acoustoelectric gain within weeks unless capped with InP or ALD alumina.

## Viability (5/5)

The sources show working devices with quantitative performance rather than proof-of-principle physics. GHz-gated InGaAs/InP SPAD arrays with negligible inter-pixel crosstalk have been combined with silica waveguide chips and run through BB84 protocol experiments, reaching over 2 Mbps at short distance and 15 kbps over 100 km of fibre. A simplified self-differencing gating scheme on an InGaAs photodiode recovers full quantum efficiency in less than one pulse-repetition period at 100 MHz, enabling continuous dead-time-free operation. A cryogenic InGaAs-InP photodiode operating at around 2.3 K supplies a stable bias current to an SNSPD, yielding 80.7% system detection efficiency, 32.6 cps background dark count rate and 57.5 ps jitter, comparable to electrical biasing.

On the emitter side, InGaAs quantum dots deliver antibunched emission with lifetimes as short as 0.51 ns from axial dots at nanowire tips, coherent control of the biexciton-exciton cascade with Franson visibilities up to 64.0% on silicon, and spectroscopically resolved g-factor shifts at tunnelling resonance in a quantum dot molecule. The unresolved items are integration yield and reliability, not basic function.

**TLDR: Not a question of whether it works: InGaAs devices are already delivering measured system-level results across detection, emission and amplification.**

## Drivers (4/5)

Demand: the strongest identified pull is quantum communication, where photonic integration of receivers is explicitly framed as the route to miniaturising QKD hardware and where cryogenic superconducting detectors are described as practically restrictive. Adjacent pull comes from heralded single-photon sources that use rapid-gating InGaAs/InP SPADs as both clock and spectral filter, from cryogenic optical interconnects needed between cold and room-temperature parts of quantum systems, and from the broad set of applications listed for silicon nitride photonics needing on-chip high-performance photodetection, including coherent fibre communications, optical clocks and low-noise microwave generation. One tier-7 commentary argues compound semiconductors and photonics will become important to the AI stack and that the UK holds a strategic position there, though it does not quantify InGaAs specifically <sup class="ref"><a href="https://stateofthefuture.substack.com/p/uk-opportunity-in-ai-compound-semiconductors" title="UK Opportunity in AI: Compound Semiconductors" rel="noopener">ref</a></sup>.

Supply: InGaAs remains tied to InP substrates and MBE/MOCVD-class epitaxy. The sources show three supply routes being worked: monolithic growth on silicon, which already yields entangled-photon emission but also brings active trap states at cryogenic temperature; heterogeneous integration of InGaAs-on-InP dies onto silicon nitride; and alumina-mediated wafer bonding onto lithium niobate, where unintentional silicon doping during epitaxy directly set the achievable gain and is called out as the process-control lever.

**TLDR: Demand is pulled by telecom-band quantum links and integrated photonics; supply is constrained by InP epitaxy and by the difficulty of putting III-V on silicon.**

## Novelty (2/5)

As a material, InGaAs is the baseline against which other things are measured. It is better than silicon in the one way that matters here: silicon SPADs are mature and room-temperature but bandgap-limited away from 1550 nm, while InGaAs SPADs are sensitive there. It is better than superconducting nanowire detectors in that it needs no cryogenics, which is the reason it is preferred for practical QKD receivers. It is worse than SNSPDs on raw detector metrics, as the same body of work implies by using an InGaAs photodiode as an auxiliary bias source for an SNSPD rather than as the detector.

The novelty in the sources sits one level up from the alloy: Sb-mediated facet engineering to suppress rotational twins and force abrupt few-nanometre axial InGaAs dots in nanowires, electrically switchable chiral light-matter coupling using an InAs/InGaAs dot in a glide-plane photonic crystal waveguide, Stark-tuned InGaAs/InAlAs intersubband-polaritonic metasurfaces characterised over 21 electric fields, and acoustoelectric amplification on lithium niobate at 32 dB/mm non-reciprocity for passivated devices. Meanwhile a black phosphorus van der Waals heterojunction is being proposed explicitly to displace InGaAs SPADs on efficiency, dark counts, afterpulsing and fabrication hazard at room temperature.

**TLDR: InGaAs is the incumbent, not the novelty; what is new is the integration and packaging around it, and challengers are now aimed squarely at its weaknesses.**

## Diffusion (4/5)

Diffusion of InGaAs as a discrete telecom-band detector and photodiode is a settled matter in these sources, which treat gated SPADs as mature and reach for InGaAs photodiodes as off-the-shelf components in unrelated experiments. The barrier is on-chip integration. The SPAD array work names the specific obstacles that had gone unaddressed: efficient GHz array gating, inter-pixel crosstalk and scalable waveguide coupling. On silicon nitride, high-performance integrated photodetection is described as having remained elusive, and the demonstrated balanced detector reaches only 0.92 GHz bandwidth.

Two reliability issues could slow adoption in specific niches. Cryogenic operation of InGaAs stacks on silicon suffers a trap-driven current-lowering mechanism that switches on below 140 K and persists to 5 K, which matters for cryo-to-room-temperature optical links. Bare InGaAs surfaces oxidise in ambient conditions and lose acoustoelectric response within weeks, requiring an InP or ALD alumina cap that itself perturbs device behaviour. Fabrication environmental hazard is also raised as a drawback.

**TLDR: Already diffused in discrete form; the barrier is co-packaging with silicon and silicon nitride photonics, plus surface and defect reliability.**

## Impact (4/5)

The upside is not one product but a position: InGaAs is the default absorber and a leading emitter host at wavelengths where fibre works. Concretely, it underpins non-cryogenic QKD receiver chips already delivering megabit-per-second class secure keys at short range and operating over 100 km of installed-length fibre, heralded spectrally pure photon sources for quantum networks, deterministic entangled-photon sources compatible with silicon manufacturing, and the detection layer for silicon nitride circuits addressing coherent communications, optical clocks, gyroscopes and low-noise microwave generation.

Two caveats hold the score below 5. First, much of the captured value accrues to the host platform and the system, not the alloy, which is a commodity input with established supply. Second, the sources contain a credible substitution threat at the highest-value detector niche, a room-temperature 1550 nm van der Waals single-photon detector explicitly targeting InGaAs's efficiency and dark-count deficits. Separate modelling work shows InGaAs thermal conductivity is dominated by alloy scattering, which is useful for thermoelectric design but also a constraint on power-dense devices.

**TLDR: If telecom-band quantum links and integrated coherent photonics scale, InGaAs is the material sitting under both; the value is broad but shared with the host platforms.**

## Timing Now (0-2yr)

The core material and its discrete devices are current technology, not a forecast. Gated InGaAs/InP SPADs are called a mature alternative to superconducting detectors, and hybrid waveguide-coupled arrays have already run protocol-level QKD experiments over 100 km of fibre. Off-the-shelf InGaAs photodiodes are being used as functional subsystems in other people's detectors.

The things that are not yet ready are dated by their current numbers. Heterogeneous InGaAs photodetection on silicon nitride is at 0.92 GHz bandwidth against applications that will want far more. Monolithic InGaAs quantum dots on silicon are approaching, not exceeding, the threshold for Bell inequality violation, with 64.0% visibility in an 80 ps window. Those two lines should be watched on a two to five year clock; the material itself needs no waiting.

**TLDR: Discrete InGaAs detectors and emitters are deployed today; the integration wave is mid-flight with system-level demonstrations already published.**

## Overrated or underrated? Fairly rated

InGaAs is correctly understood as the incumbent telecom-band III-V, and the sources bear that out without embellishment: it is the material people reach for when they need 1550 nm sensitivity without a cryostat, and it is the emitter host in most of the quantum dot work here. There is no hype gap to arbitrage, in either direction. The interesting judgement is that the near-term value has moved from the alloy to the joining technology. The publishable results in this set are about Sb-mediated facet control, alumina-mediated bonding to lithium niobate, waveguide coupling of SPAD arrays and monolithic growth on silicon, not about InGaAs itself.

The honest risk is that InGaAs's dominance is defensive rather than improving. Its detector weaknesses, efficiency, dark counts and afterpulsing, are stated plainly by a competing approach that has now demonstrated room-temperature single-photon detection at 1550 nm using a black phosphorus absorber. That threat is a single-group demonstration against a mature industrial base, so it does not change the call today, but a repeat with array-scale yield would.

## Prediction

By 31 December 2028, a heterogeneously integrated InGaAs photodetector on a thin-core silicon nitride platform will be reported with more than 10 GHz bandwidth, an order of magnitude above the 0.92 GHz balanced detector demonstrated in July 2026.

## Evidence base

- GHz-gated InGaAs/InP SPAD arrays coupled to low-loss silica waveguides produced compact hybrid QKD receivers with secure key rates over 2 Mbps at short distance and 15 kbps over 100 km of fibre.
- A self-differencing gating scheme on an InGaAs photodiode at 100 MHz recovered full quantum efficiency in under one pulse-repetition period, enabling dead-time-free continuous operation.
- A cryogenic InGaAs-InP photodiode biasing an SNSPD at about 2.3 K gave 80.7% system detection efficiency, 32.6 cps background dark counts and 57.5 ps minimum jitter.
- Energy-time entanglement was demonstrated from a single InGaAs/GaAs quantum dot grown monolithically on silicon, with Franson visibility of 64.0 plus or minus 7.0% for an 80 ps window.
- A heterogeneously integrated InGaAs-on-InP modified uni-travelling-carrier balanced photodetector on a 15 metre thin-core silicon nitride Mach-Zehnder interferometer achieved 0.92 GHz bandwidth.
- Epitaxial InGaAs bonded to X-cut lithium niobate on insulator gave 32 dB/mm stable non-reciprocity at 1.11 GHz for passivated devices, with bare-surface oxidation extinguishing the response within weeks.
- InGaAs SPADs are documented as sensitive at 1550 nm but suffering lower efficiency, high dark count rate, afterpulsing and fabrication environmental hazard, motivating a room-temperature black phosphorus alternative.

## Open questions

- Can InGaAs/InP SPAD arrays scale beyond the demonstrated hybrid silica-waveguide receivers to monolithic pixel counts while holding negligible crosstalk and GHz gating?
- Do the trap states that suppress current in InP/InGaAs-on-silicon stacks below 140 K yield to growth or annealing changes, or do they cap cryogenic optical interconnect performance?
- Does the room-temperature van der Waals 1550 nm single-photon detector reproduce at array scale with dark-count and efficiency figures that beat InGaAs SPADs in a real link?
- Can monolithic InGaAs quantum dots on silicon push Franson visibility past the Bell violation threshold at long integration windows, not only at 80 ps?

---
*Assessment drafted 2026-08-31 from up to 15 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
