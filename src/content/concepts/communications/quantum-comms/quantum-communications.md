---
type: concept
slug: quantum-communications
canonical_name: Quantum Communications
aliases: []
kind: technology
parent_concepts:
- communications
- quantum-comms
related_concepts: []
sources:
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
frontier:
- Can any photon memory reach a storage lifetime and efficiency sufficient for a two-link repeater chain, given that the Brillouin nanowire scheme is limited by acoustic-wave lifetime and remains theoretical 2026 07 03 memory device for photons by exploiting brillouin interactio?
- Does the O-band coexistence result at 24.4 km scale to full metro spans and multi-node topologies, or does spontaneous Raman noise from fully loaded C-band systems dominate beyond a certain length 2026 07 21 quantum entanglement distribution coexisting with high rate ?
- What is the cost per secure bit of a hybrid-integrated SPAD receiver relative to classical alternatives, given that none of these sources contains cost data 2026 06 05 hybrid integrated ingaasinp spad arrays for quantum communic?
- Does the proposed ZALM time-bin source, once built, actually deliver quasi-deterministic heralded entanglement at rates useful for repeaters, rather than only component-level compatibility 2026 05 05 zero added loss entanglement multiplexing using time bin spe?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 26
last_reorg_date: '2026-05-14'
scorecard:
  viability: 3
  drivers: 2
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2024-12-16-willow-and-the-race-to-quantum-advantage
  title: Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)
  date: '2024-12-16'
  kind: substack
neighbors: []
---
**Quantum communications uses single photons and entanglement to move keys and quantum states between distant parties with security guaranteed by physics rather than computational hardness; the point-to-point hardware is now working at telecom wavelengths on installed fibre, but the memories and repeaters needed for actual networks remain proposals.**

## Summary

Quantum communications covers two related things. The first is quantum key distribution (QKD), where a sender encodes bits on single photons or weak coherent states and any eavesdropper's measurement necessarily disturbs them, so the legitimate parties can bound the leaked information and distil a key whose security rests on quantum mechanics rather than on an unproven computational assumption. Protocol families differ in what they assume: prepare-and-measure schemes such as BB84 and SARG04, entanglement-based schemes such as BBM92, and continuous-variable schemes that encode on the quadratures of light and can be built from standard telecom transmitters and homodyne receivers. The second, more ambitious thing is a quantum network that distributes entanglement itself, as a resource for distributed quantum computing, distributed sensing and communication primitives that have no classical equivalent.

The parameters that decide the field are all physical-layer. Photon loss in fibre is exponential in distance and cannot be amplified away without destroying the quantum state, so key rate falls steeply with range: a recent hybrid-integrated receiver achieved over 2 Mbps at short distance and 15 kbps over 100 km of fibre using BB84. Detector quality sets the noise floor, and detector technology forces a hard trade: superconducting nanowire detectors have been integrated onto receiver chips but need cryogenics, while gated InGaAs/InP single-photon avalanche diodes work without cooling and can now be built into GHz-gated arrays with negligible inter-pixel crosstalk. For free-space and infrared operation the cryogenic problem is worse still, with existing mid- and long-wave infrared single-photon detectors needing 0.08 to 0.9 K.

Beyond a single link, distance requires quantum repeaters, and repeaters require both high-rate heralded entanglement sources and photon memories. Both are at the design and proof-of-principle stage in the sources here: a zero-added-loss multiplexing source design has been proposed for time-bin entanglement with experimental verification only of the compatibility of time-bin pulses and spectral shearing, and single-photon storage via Brillouin interactions in nanowires is a theoretical configuration, with the acoustic-wave lifetime identified as the limiting factor.

The most consequential deployment result is coexistence. Polarisation-encoded entanglement has been distributed in the O-band over an installed 24.4 km fibre while the same fibre carried a fully loaded state-of-the-art C-band classical line system with two 800 Gbps channels and the rest of the C-band filled with amplified spontaneous emission, plus a picosecond-precision L-band synchronisation signal, with Bell state fidelity preserved by careful wavelength allocation and narrow filtering against spontaneous Raman scattering. That determines whether quantum channels need dark fibre or can ride existing plant, which is the single largest cost question in the field.

## Viability (3/5)

The layer above the link is where viability is unproven. High-rate heralded entanglement sources for repeaters are still design proposals with only component-level experimental verification, and single-photon memory in the sources here is a theoretical scheme whose usable lifetime is explicitly limited by acoustic-wave decay. Underwater channels remain at the simulation stage, with quantum bit error rate and correlation modelled rather than measured. A 3 reflects that split: the link technology is demonstrated, the network technology is credible but contested.

**TLDR: Single links work on real fibre with real hardware; the repeater and memory layer that makes them a network does not exist yet.**

## Drivers (2/5)

On the supply side the sources show sustained, coordinated research funding. NSF has funded a multi-institution hybrid free-space and fibre quantum network programme under its Use-Inspired NextG line, with a satellite entanglement backbone feeding terrestrial regional networks, awarded to Yale at $368,000 and to UMass Amherst at $317,680 on 2 August 2026, plus $473,811 to Columbia on 4 August 2026 for the underlying quantum detection and estimation theory. These are single-lab research grants, not deployment programmes, and their size should be read accordingly. Alongside them, component-level work spans detectors, sources, memories and photonic couplers, indicating a broad supply pipeline.

The demand side is close to absent from these sources. No customer, procurement, tender, revenue figure, standard or regulatory mandate appears anywhere. The nearest thing to an articulated pull is technical: distributed quantum computing and sensing as consumers of high-quality entanglement, and privacy-constrained distributed machine learning as a possible application of pre-shared entanglement. Both are prospective. One commentary source also notes that quantum in general is arriving more expensively than expected <sup class="ref"><a href="https://stateofthefuture.substack.com/p/willow-and-the-race-to-quantum-advantage" title="Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)" rel="noopener">ref</a></sup>. A 2 is what the evidence supports; if demand signals exist, they are not in this corpus.

**TLDR: Visible push from government research programmes at modest scale; the sources contain essentially no demand-side evidence.**

## Novelty (3/5)

What quantum communications is better than is classical key exchange and classical secure aggregation, and the claimed advantage is categorical rather than incremental: security that follows from physics, and privacy properties that are information-theoretically unachievable by any classical protocol. The clearest quantified statement is in the distributed-learning primitive, where pre-shared entanglement and superdense coding cut per-link online communication by a provably optimal factor of two and enable composable epsilon-secure aggregation at a 2x overhead in GHZ copies, without changing the learning model. A factor of two in bandwidth, paid for with distributed entanglement, is a genuine but narrow margin. New primitives are also being proposed at the protocol level, including output-hiding function sharing claimed to improve security and efficiency relative to status-quo QKD protocols, though that source is a proposal without experimental support.

On raw performance the comparison is unflattering: 15 kbps over 100 km sits beside a classical system on the same class of fibre carrying two 800 Gbps channels. The novelty is therefore in the guarantee, not the capacity. Note also that these sources make no comparison against classical post-quantum cryptography, so the most important competitive question for QKD cannot be assessed from them. The engineering novelty within the field is real but modular: non-cryogenic SPAD arrays with GHz gating and negligible crosstalk address a stated open problem in receiver integration, and a proposed ferromagnet/superconductor detector would lift infrared single-photon operation from 0.08 to 0.9 K up to 3.75 K, removing dilution-refrigerator dependence.

**TLDR: Offers guarantees that are provably impossible classically, but the measured throughput and cost advantages over conventional channels are small or absent.**

## Diffusion (2/5)

The strongest diffusion argument in these sources is infrastructure compatibility. Entanglement has been distributed over an installed 24.4 km fibre simultaneously carrying a fully loaded C-band classical system with two 800 Gbps channels and a picosecond-precision synchronisation signal, with Bell state fidelity preserved through O-band operation, wavelength allocation informed by the measured spontaneous Raman spectrum, and narrow filtering. Combined with hybrid-integrated, non-cryogenic receivers and CV-QKD schemes explicitly targeted at affordability using standard telecom technology, this points to systems that could be dropped into existing plant rather than requiring dark fibre.

The barriers are still substantial. Reach is limited without repeaters, and repeater components are pre-demonstration. Photonic packaging loss remains material: a state-of-the-art vertical grating coupler in this corpus measured 8.35 dB single-coupler insertion loss around 1528 nm despite 12.80 dB unidirectionality, against 41% in-coupling efficiency in simulation, and in a single-photon system every decibel is throughput. Free-space and satellite architectures, which are the intended fix for range, exist here only as funded research plans covering routing, scheduling and mobility that have not been built. Security proofs also constrain operation: positive key rates in the finite-size regime require block sizes of order 10^8, which ties usable security to sustained high-rate links.

**TLDR: Coexistence with live classical traffic on installed fibre removes the biggest deployment blocker, but detector cooling, coupling losses and the missing repeater layer keep reach and cost unattractive.**

## Impact (3/5)

The sources support a qualitative impact case in two registers. As a security technology, QKD delivers information-theoretic key agreement over deployed fibre and, in principle, underwater and free-space channels, with proposed primitives extending to joint computation, financial transactions, signalling coordination and navigation. As an enabling layer, high-quality distributed entanglement is the prerequisite for distributed quantum computing and distributed quantum sensing, and it also underpins the quantum detection and estimation theory used for precision measurement. That second register is where the value concentrates: linking quantum processors and sensors is not something classical networks can do at all.

The counterweight is that where a like-for-like classical comparison exists, the gain is bounded. The distributed-training primitive buys a provably optimal factor of two on per-link online communication and a security property at 2x GHZ overhead. Key rates of 15 kbps at 100 km limit the technology to key material rather than data transport. None of these sources contains market sizing, cost data or adoption figures, so the score reflects the strength of the technical case only, and one commentary source cautions that quantum progress is arriving at higher cost than expected <sup class="ref"><a href="https://stateofthefuture.substack.com/p/willow-and-the-race-to-quantum-advantage" title="Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)" rel="noopener">ref</a></sup>.

**TLDR: Large if entanglement networking arrives, since it enables things with no classical analogue; modest as a drop-in replacement for classical secure links.**

## Timing Soon (2-5yr)

The near-term item is already at the engineering stage. Non-cryogenic SPAD arrays hybridised with waveguide chips have run BB84 at over 2 Mbps short-range and 15 kbps at 100 km, CV-QKD security proofs have reached realistic block sizes and standard telecom hardware, and coexistence with a fully loaded 800 Gbps-per-channel classical system on installed fibre has been shown. Those three together are what a metro-scale trusted-node deployment needs, so a 2 to 5 year window for such systems is consistent with the evidence.

The entanglement-network item is further out and the sources say so implicitly by their maturity level. Repeater sources are designs with component verification, photon memories are theory, satellite-plus-fibre architectures are newly funded research plans as of August 2026, and warm infrared single-photon detection for free-space links is a proposal reaching 3.75 K rather than room temperature. Treat entanglement-distribution networks as Later to Distant.

**TLDR: Integrated point-to-point QKD on installed fibre is demonstration-ready now; entanglement networks with repeaters are a decade-scale programme.**

## Overrated or underrated? Fairly rated

The honest reading of this corpus is that quantum communications has quietly become a real hardware discipline while remaining a speculative networking one. The receiver-integration result and the coexistence experiment are the kind of unglamorous engineering that decides whether a technology deploys: compact non-cryogenic detectors with negligible crosstalk, and quantum channels surviving next to live 800 Gbps traffic on installed fibre. Anyone dismissing QKD as a laboratory exercise is behind the evidence.

Equally, anyone pricing in quantum networks should look at what is missing. Memories and repeaters, the parts that turn links into networks and that justify the distributed-computing and distributed-sensing claims, appear here only as designs and theory. Funding is real but small at the individual-award level, and there is no demand-side evidence in these sources at all. The demonstrated advantage where a classical comparison is available is a factor of two. Fairly rated, then, with the caveat that the field is two technologies at very different stages and the market tends to score them as one.

## Prediction

By 31 December 2028, published quantum communications results will still report no memory-based quantum repeater node operating over installed metropolitan fibre carrying live classical traffic, while chip-integrated QKD receivers will exceed the 15 kbps at 100 km reported in September 2025.

## Evidence base

- Hybrid receivers combining GHz-gated InGaAs/InP SPAD arrays with low-loss silica waveguide chips ran BB84 at over 2 Mbps at short distance and 15 kbps over 100 km of fibre, without cryogenic cooling, reported 5 September 2025.
- O-band polarisation-encoded entanglement was distributed over an installed 24.4 km fibre while the same fibre carried a fully loaded C-band classical line system with two 800 Gbps channels plus ASE fill and an L-band picosecond synchronisation signal, with Bell state fidelity preserved (updated 21 July 2026).
- A finite-size security analysis for discrete-modulated continuous-variable QKD against general attacks removed bounded-dimension assumptions and reported positive key rates at block sizes of order 10^8 with a trusted detector model, 19 June 2026.
- A quantum ring all-reduce primitive using pre-shared entanglement and superdense coding reduces per-link online communication by a provably optimal factor of two and gives composable epsilon-secure aggregation at 2x overhead in GHZ copies, 19 June 2026.
- Repeater-grade entanglement sources remain at the design stage: a ZALM time-bin design was proposed with experimental verification only that time-bin pulses and spectral shearing are compatible (no appreciable phase shift), 5 May 2026.
- Existing mid- and long-wave infrared single-photon detectors for free-space quantum communications require 0.08 to 0.9 K; a ferromagnet/superconductor bilayer approach proposes raising this to 3.75 K, 17 June 2026.
- NSF funded a hybrid free-space and fibre quantum network programme with a satellite entanglement backbone at $368,000 (Yale) and $317,680 (UMass Amherst) on 2 August 2026, and $473,811 for quantum detection and estimation theory on 4 August 2026.

## Open questions

- Can any photon memory reach a storage lifetime and efficiency sufficient for a two-link repeater chain, given that the Brillouin nanowire scheme is limited by acoustic-wave lifetime and remains theoretical?
- Does the O-band coexistence result at 24.4 km scale to full metro spans and multi-node topologies, or does spontaneous Raman noise from fully loaded C-band systems dominate beyond a certain length?
- What is the cost per secure bit of a hybrid-integrated SPAD receiver relative to classical alternatives, given that none of these sources contains cost data?
- Does the proposed ZALM time-bin source, once built, actually deliver quasi-deterministic heralded entanglement at rates useful for repeaters, rather than only component-level compatibility?

---
*Assessment drafted 2026-08-31 from up to 15 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
