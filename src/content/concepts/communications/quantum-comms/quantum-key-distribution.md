---
type: concept
slug: quantum-key-distribution
canonical_name: Quantum Key Distribution
aliases: []
parent_concepts:
- quantum-comms
- communications
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 66
frontier:
- Can the numerical finite-key frameworks now being proposed be applied end to end to a shipped commercial transmitter and receiver, including higher-order intensity correlations and detector timing side channels, without collapsing the usable key rate 2026 05 14 numerical security analysis for practical quantum key distri?
- What is the cost, rate and assurance comparison against classical and post-quantum key exchange for the same link? No supplied source addresses it, and it decides adoption.
- Does the integrated-photonics metro prototype hold its stability and key rate when scaled from the demonstrated 4 km to the 50-100 km links that real operator topologies require 2026 05 29 quantum key distribution over a metropolitan network using a?
- Do geostationary downlinks yield enough annual secret key across realistic European cloud cover and daylight background to justify the space segment 2026 05 29 finite key feasibility of geostationary quantum key distribu?
- Can intensity-correlation and energy-time detector effects be bounded inside a single finite-key proof, and what residual key rate remains for a fully characterised industrial decoy-state BB84 system at its rated repetition rate?
- How many discrete phase settings does DPR-MP-QKD need to reach a specified fraction (say 99%) of the continuous-phase-randomisation key rate at metropolitan and long-haul distances 2026 05 15 discrete phase randomized mode pairing quantum key distribut?
- Does the measured secret key rate of free-space LLO self-referenced PSP CVQKD hold under realistic atmospheric turbulence and over what link budget 2026 05 08 high rate free space continuous variable qkd with self refer?
- Do QMF-QSDC protocols deliver higher throughput than QKD plus one-time pad at equal security parameter and channel loss, in an experimental implementation rather than an information-theoretic analysis 2026 05 04 a quantum memory free quantum secure direct communication pr?
- Does the Θ(N log N) authentication scaling for sparse E91 networks survive measurement in a deployed multi-user network, and what operational correlation length is observed 2026 05 28 emergent operational entanglement graphs and sub quadratic a?
scorecard:
  viability: 3
  drivers: null
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 1
sources_30d: 8
recent_mentions: []
neighbors: []
---
**Quantum key distribution uses the measurement properties of single photons or weak optical fields to let two parties grow a shared secret key whose secrecy rests on physics rather than computational hardness; the hardware now runs unattended in metropolitan fibre, but the gap between idealised security proofs and real devices remains the binding constraint.**

## Summary

Quantum key distribution (QKD) is a method for two parties to agree a symmetric encryption key over an untrusted channel. Instead of relying on a mathematical problem being hard, it encodes bits in quantum states of light. Any attempt to measure or copy those states disturbs them, so the legitimate parties can bound how much an eavesdropper could have learned by measuring the error rate, then compress the raw data down to a shorter key that is secret with high probability. The compression step (privacy amplification, typically universal hashing) and the accounting of how much secrecy survives finite data sets are where most of the theoretical work sits.

The field splits along several axes. Discrete-variable (DV) schemes such as decoy-state BB84 send weak laser pulses and count single-photon detections; the decoy-state trick uses deliberately varied pulse intensities to detect photon-number-splitting attacks. Continuous-variable (CV) schemes encode in the amplitude and phase quadratures and use homodyne detection with standard telecom components, trading distance for hardware familiarity and rate. Entanglement-based variants (E91, BBM92) distribute photon pairs and derive randomness from the correlations themselves rather than from a trusted transmitter. Measurement-device-independent and twin-field style protocols, including mode-pairing QKD, aim to remove trust in the detectors and to beat the repeaterless rate-versus-transmittance bound. High-dimensional encodings, for example in orbital angular momentum, raise bits per photon and noise tolerance at the cost of harder state generation and sorting.

The parameters that decide the technology are: channel loss in dB (which sets the key rate and, past a point, kills it entirely), detector noise and background light, clock rate, and the size of the data block available for finite-key statistics. Everything else is engineering around those four. A 1.25 GHz integrated-photonics prototype in 19-inch rack units has held continuous key exchange over more than 4 km of metropolitan fibre across more than 12 day-night cycles without intervention, and needs no chromatic dispersion compensation below 100 km. A free-space CV system with a local local oscillator and self-referenced passive state preparation reports an asymptotic secret key rate of 10.34 Mbps at up to 23.5 dB loss.

The unresolved problem is not whether keys can be produced but whether the security proof applied to a real box is actually valid. Recent work shows that high repetition rates create intensity correlations between successive pulses that leak encoding settings and violate a founding assumption of decoy-state QKD, with higher-order correlations mattering more than nearest-neighbour ones in two industrial prototypes, and that a gated avalanche detector's click timing shifts by more than 2 ns as pulse energy varies over 50 dB, which an attacker can use to push clicks into adjacent bit slots and render standard proofs inapplicable.

## Viability (3/5)

The engineering case is solid. A rack-mounted integrated-photonics transmitter and receiver ran 1.25 GHz QKD over deployed metropolitan fibre for more than 12 day-night cycles without manual intervention; GHz time-bin entanglement has been distributed over a roughly 30 km, 9.5 dB link in the Vienna fibre network using off-the-shelf components; free-space CV-QKD reports 10.34 Mbps at 23.5 dB loss with stable operation under turbulence. Squeezed-state CV-QKD has moved from theory to experimental confirmation of its predicted advantages over coherent states under finite-size security against collective attacks.

What holds the score at 3 is that the central selling point, information-theoretic security, is still not demonstrably true of shipped hardware. Two independent 2026 results attack the assumptions directly: pulse intensity correlations at high repetition rates leak setting information and significantly reduce the asymptotic key rate in industrial prototypes, with higher-order terms worse than expected, and detector energy-time behaviour lets an attacker toggle a click between adjacent key bit slots, breaking an implicit proof assumption. The theory side is responding with numerical finite-key frameworks valid against general coherent attacks that tolerate non-IID signals and only partial device characterisation, and with asymptotically tight phase-error-correction analyses. That is a live race between proof coverage and newly discovered side channels, and the sources do not show it settled.

**TLDR: Hardware demonstrably works in the field; the security claim on real devices does not yet close.**

## Drivers (unscored)

On supply, the literature shows the classic cost-down pattern: integrated photonics consolidated into standard 19-inch rack units explicitly framed as the requirement for industrial-scale adoption, entanglement sources built from off-the-shelf components, differential phase shift keying pursued specifically because it uses affordable commercial technology, passive state preparation pitched as low-cost and high-rate, and the existence of at least two industrial prototypes available for third-party characterisation.

On demand there is nothing usable. The supplied sources contain no market sizing, no procurement decisions, no regulatory or standards mandates, no operator commitments, no funding figures, and no comparison against the competing option of post-quantum cryptography. The only demand-side statements are generic assertions that secure communication and a future quantum internet will matter. Scoring this dimension from that material would be fabrication, so it is left null.

**TLDR: Supply-side momentum is visible in the sources; demand evidence is entirely absent, so no honest score.**

## Novelty (3/5)

Judged within its own field, the increments are real and quantified. Mode-pairing QKD exceeds the repeaterless rate-transmittance bound without global phase locking, and the discrete-phase-randomised version removes the physically unrealisable continuous phase randomisation assumption, converging on continuous-case rates at roughly 14 discrete phases while cutting the randomness demand to a few bits. Squeezed light beats coherent states on key rate, excess-noise tolerance and reconciliation-efficiency requirements, now experimentally rather than only theoretically. Variable-length security with Renyi leftover hashing and conic optimisation gives DPSK positive key at 10^5 signals beyond 12 dB, removing prior repetition-rate constraints in the proof. Network-layer claims are also non-trivial: entanglement-based QKD authentication is widely assumed to scale quadratically with users, but under realistic loss and decoherence the usable Bell-pair count scales linearly and authentication as Theta(N log N).

The missing comparison is the important one. Nothing in these sources measures QKD against classical or post-quantum key establishment on cost, rate, reach or assurance. The only alternative considered is quantum-memory-free quantum secure direct communication, offered as a substitute for QKD plus one-time pads. So the score reflects strong intra-field novelty and an unevidenced position relative to the incumbent it would displace.

**TLDR: Clear, measurable gains over previous QKD generations; the sources never benchmark it against classical alternatives.**

## Diffusion (2/5)

Barriers are stacked. Distance and loss dominate: the integrated-photonics field demonstration covered more than 4 km of metropolitan fibre, the Vienna entanglement link about 30 km at 9.5 dB, and going beyond metropolitan scale needs either satellites, where a GEO downlink faces extreme loss and daylight background and where achievable annual key yield depends on cloud cover, or repeater-like protocols. Certification is the second barrier: proofs valid for real, imperfect, high-speed hardware are only now being constructed, while independent testing keeps finding exploitable device behaviour.

The third barrier is that a QKD link is not a QKD service. Networks need routing that jointly optimises latency, key rate, congestion, finite key capacity and security constraints under changing traffic, an area still at the level of proposed quantum-inspired annealing and tensor-network heuristics, plus authentication scaling and operational monitoring, where a 2026 survey organises the practical exposure into nine problem classes across device, channel, protocol, machine-learning and network layers and notes that the machine-learning components introduced for adaptation and monitoring are themselves an attack surface. Niche channels such as underwater links remain at the simulation stage, with performance strongly dependent on water type.

**TLDR: Field-deployable boxes exist, but reach, certification and network-layer machinery are all immature.**

## Impact (3/5)

If the implementation-security gap closes, the payoff is qualitative rather than incremental: key agreement whose secrecy rests on physical law and information-theoretic bounds instead of assumed computational hardness. The named applications extend to continuous continental-scale secure communication via geostationary satellites and to entanglement distribution as the substrate for multiparty computation and for securely connecting quantum computers in a future quantum internet. Rates are already at the level where the key is not the bottleneck for many uses: 10.34 Mbps over a 23.5 dB free-space channel.

The ceiling is bounded in two ways the sources make visible. First, QKD addresses key distribution only, and its practical value is measured against whatever key exchange is already deployed, a comparison absent from this evidence base. Second, an alternative architecture, quantum-memory-free quantum secure direct communication, is explicitly proposed as a replacement for QKD plus one-time pads, so even within quantum communications the protocol layer is not settled. No source supplies economic or deployment-scale figures, so the score reflects a credible but narrow and unquantified upside.

**TLDR: A genuine change in the basis of key-exchange security, but it solves only key exchange and the sources quantify no value.**

## Timing Soon (2-5yr)

The point-to-point metropolitan case is already at the field-prototype stage: rack-format, integrated-photonics, 1.25 GHz, unattended operation over deployed fibre across more than 12 day-night cycles, with dispersion compensation unnecessary below 100 km. Entanglement distribution over a live city network with commodity parts is likewise demonstrated. Deployment therefore does not wait on physics.

What sets the 2-5 year band is the certification loop. Proof frameworks that cover real transmitters and receivers, non-IID signals and partial device characterisation appeared as new preprints in May 2026, and new device-level attacks are being published on the same timescale. Long-reach options are further out: geostationary QKD is at the feasibility-study stage, with positive-key regimes identified rather than demonstrated, and underwater QKD is still analytical and simulated.

**TLDR: Metro-scale hardware is deployable now; certifiable security and network-scale operation are the 2-5 year items.**

## Overrated or underrated? Fairly rated

The honest reading of this evidence base is that QKD is neither vapour nor imminent infrastructure. The hardware works, in deployed fibre, at GHz clocks, in rack units, unattended, with key rates in the Mbps range on lossy free-space channels. At the same time the marketing claim that distinguishes it from classical cryptography, unconditional security, is precisely the claim that current implementations cannot yet substantiate: independent characterisation of industrial prototypes found higher-order intensity correlations that invalidate a basic premise of decoy-state QKD and cut the key rate, and a gated detector's energy-dependent timing was shown to break an implicit assumption in the proofs outright.

The useful investor question is therefore not whether QKD works but whether the proof-versus-side-channel race converges, and whether anyone is obliged to buy the result. The first is tractable and progressing, with numerical finite-key frameworks moving towards rigorous certification of real setups. The second is unanswerable from this material: there is no demand-side evidence here at all, and no benchmark against classical or post-quantum alternatives. Anyone underwriting QKD on the strength of the physics literature alone is underwriting only half the thesis.

## Prediction

By 31 December 2028, no commercially sold QKD system will have a publicly documented security proof that simultaneously accounts for higher-order pulse intensity correlations at its rated repetition rate and for detector energy-time click-timing shifts of the kind measured at 312.5 MHz gating.

## Evidence base

- 29 May 2026: a 1.25 GHz integrated-photonics QKD prototype in standard 19-inch rack units maintained continuous, uninterrupted key exchange over more than 4 km of metropolitan fibre across more than 12 day-night cycles without manual intervention, and required no chromatic dispersion compensation below 100 km.
- 8 May 2026: a self-referenced, local-local-oscillator passive-state-preparation CV-QKD system reported a record asymptotic secret key rate of 10.34 Mbps over a free-space channel with up to 23.5 dB loss under turbulent conditions.
- 4 May 2026: intensity correlations were characterised in two industrial decoy-state BB84 prototypes; they leak encoding settings, invalidate a basic premise of the decoy-state method and significantly reduce the asymptotic key rate, with higher-order correlations mattering more than nearest-neighbour ones.
- 14 May 2026: an avalanche detector gated at 312.5 MHz showed click timing shifting by more than 2 ns as pulse energy varied over a 50 dB range, enabling proposed attacks that toggle clicks between adjacent key bit slots and render existing security proofs inapplicable.
- 14 May 2026: a numerical finite-key security framework valid against general coherent attacks was introduced, covering transmitter and receiver imperfections including non-IID signals from limited modulator bandwidth, and requiring only partial device characterisation.
- 14 May 2026: GHz sequential time-bin entangled states were distributed over an approximately 30 km, 9.5 dB link in the Vienna fibre network using off-the-shelf components.
- 29 May 2026: a decoy-state BB84 geostationary downlink was assessed with variable-length finite-key security across rural, urban and coastal environments and historical European cloud data, identifying positive-key regimes and bottlenecks rather than demonstrating operation.

## Open questions

- Can the numerical finite-key frameworks now being proposed be applied end to end to a shipped commercial transmitter and receiver, including higher-order intensity correlations and detector timing side channels, without collapsing the usable key rate?
- What is the cost, rate and assurance comparison against classical and post-quantum key exchange for the same link? No supplied source addresses it, and it decides adoption.
- Does the integrated-photonics metro prototype hold its stability and key rate when scaled from the demonstrated 4 km to the 50-100 km links that real operator topologies require?
- Do geostationary downlinks yield enough annual secret key across realistic European cloud cover and daylight background to justify the space segment?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
