---
type: concept
slug: quantum-key-distribution
canonical_name: Quantum Key Distribution
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 65
frontier:
- Can intensity-correlation and energy-time detector effects be bounded inside a single finite-key proof, and what residual key rate remains for a fully characterised industrial decoy-state BB84 system at its rated repetition rate?
- How many discrete phase settings does DPR-MP-QKD need to reach a specified fraction (say 99%) of the continuous-phase-randomisation key rate at metropolitan and long-haul distances 2026 05 15 discrete phase randomized mode pairing quantum key distribut?
- Does the measured secret key rate of free-space LLO self-referenced PSP CVQKD hold under realistic atmospheric turbulence and over what link budget 2026 05 08 high rate free space continuous variable qkd with self refer?
- Do QMF-QSDC protocols deliver higher throughput than QKD plus one-time pad at equal security parameter and channel loss, in an experimental implementation rather than an information-theoretic analysis 2026 05 04 a quantum memory free quantum secure direct communication pr?
- Does the Θ(N log N) authentication scaling for sparse E91 networks survive measurement in a deployed multi-user network, and what operational correlation length is observed 2026 05 28 emergent operational entanglement graphs and sub quadratic a?
sources_7d: 0
sources_30d: 7
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Quantum key distribution (QKD) generates a shared secret key between two parties whose secrecy rests on quantum mechanics and on idealised device models rather than on computational hardness numerical security analysis for practical quantum key distri. Implementations divide broadly into prepare-and-measure schemes, in which one party encodes randomly chosen states and the other measures them, and entanglement-based schemes, which draw randomness inherently from the measurement of shared entangled states and are argued to offer generally higher security than prepare-and-measure implementations distribution of ghz sequential time bin entanglement in a me. The canonical prepare-and-measure protocol is BB84; two-way variants (LM05, two-way BB84) and entanglement-based secure dense coding are also studied, with secret key rates derivable from entropic uncertainty relations under collective attacks noise adaptive two way secure deterministic quantum key dist.

Because practical transmitters use weak coherent laser pulses rather than single photons, the decoy-state method is the dominant approach for bounding an eavesdropper's information: the sender randomises pulse intensity so that photon-number-splitting leakage can be estimated intensity correlations in decoy state bb84 quantum key distr. Key rate is limited by channel transmissivity, so systems raise the transmitter repetition rate to compensate. This introduces correlations between successive optical pulses that leak information about encoding settings including intensity, violating a basic premise of decoy-state QKD; measurements on two industrial prototype decoy-state BB84 systems show these correlations significantly reduce the asymptotic key rate intensity correlations in decoy state bb84 quantum key distr. High-speed operation also produces non-independent-and-identically-distributed signals arising from the limited bandwidth of optical modulators numerical security analysis for practical quantum key distri.

Security proofs must be finite-size to be operationally meaningful. Phase error correction (PEC) is a general strategy that has yielded finite-size proofs for many protocols, but the conventional PEC approach cannot in general reach the asymptotically optimal key rate as long as the PEC failure probability is estimated via the phase error rate; a PEC-type strategy built on universal source compression with quantum side information has been proposed to close that gap asymptotically tight security analysis of quantum key distri. Variable-length approaches using entropy accumulation with Rényi leftover hashing plus conic optimisation have been applied to differential phase shift keying (DPSK), removing earlier repetition-rate constraints and costly statistical estimators, and yielding key rates at 10^5 signals beyond 12 dB channel loss finite size general security for differential phase shift ke.

Source-side assumptions are a recurring weak point. Mode-pairing QKD (MP-QKD) exceeds the repeaterless rate-transmittance bound while avoiding global phase locking, but its source analysis assumes continuous phase randomisation, which is not experimentally realisable; a discrete-phase-randomised variant with a discrete decoy-state method approaches the continuous-randomisation key rate as the number of discrete phases increases discrete phase randomized mode pairing quantum key distribut. On the receiver side, detector imperfections remain exploitable: an avalanche single-photon detector sinusoidally gated at 312.5 MHz was found moderately superlinear in click probability, and its click timing advanced by more than 2 ns as incoming pulse energy varied over a 50 dB range, an energy-time effect an attacker could use to toggle clicks conditionally energy time attack on detectors in quantum key distribution.

## Competitive landscape

| Approach | Distinguishing feature | Reported status |
|---|---|---|
| Decoy-state BB84 (discrete variable) | Weak coherent pulses, intensity randomisation | Industrial prototypes measured; inter-pulse intensity correlations cut asymptotic key rate intensity correlations in decoy state bb84 quantum key distr |
| DPSK | Uses affordable commercial technologies | General-adversary finite-size security at 10^5 signals beyond 12 dB finite size general security for differential phase shift ke |
| Continuous-variable QKD with passive state preparation | Low cost, high rate; local local oscillator with self-referenced pilot | Free-space LLO SR-PSP system implemented high rate free space continuous variable qkd with self refer |
| Mode-pairing QKD | Beats repeaterless rate-transmittance bound without global phase locking | Discrete-phase-randomised variant proposed and simulated discrete phase randomized mode pairing quantum key distribut |
| Entanglement-based (E91, time-bin) | Inherent randomness; basis for future quantum internet | Sequential time-bin entanglement distributed over metropolitan fibre with off-the-shelf components distribution of ghz sequential time bin entanglement in a me |

An adjacent alternative avoids key distribution entirely: quantum-memory-free quantum secure direct communication (QMF-QSDC) is analysed as a substitute for conventional QKD combined with one-time pads, using universal hashing of coded sequences without wiretap coding, supported by privacy amplification theorems against quantum side information under collective attacks a quantum memory free quantum secure direct communication pr.

## Evidence base

- Intensity correlations between successive pulses were characterised in two industrial decoy-state BB84 prototypes and shown to significantly reduce the asymptotic secret key rate, invalidating a basic decoy-state premise intensity correlations in decoy state bb84 quantum key distr.
- A sinusoidally gated avalanche single-photon detector at 312.5 MHz showed moderate superlinearity and a click-time shift of more than 2 ns across a 50 dB range of incoming pulse energy, enabling a proposed energy-time attack energy time attack on detectors in quantum key distribution.
- A numerical finite-key security framework valid against general coherent attacks was introduced that accommodates transmitter and receiver imperfections, including non-IID signals from limited modulator bandwidth, requiring only partial device characterisation numerical security analysis for practical quantum key distri.
- Variable-length security analysis for DPSK using Rényi leftover hashing and conic optimisation achieved secret key rates with 10^5 signals beyond 12 dB finite size general security for differential phase shift ke.
- A new phase-error-correction strategy based on universal source compression with quantum side information was shown to provably achieve the asymptotically optimal key rate, which conventional PEC cannot in general reach asymptotically tight security analysis of quantum key distri.
- Sequential time-bin entangled states were distributed in a metropolitan fibre network using off-the-shelf components, demonstrating feasibility for entanglement-based QKD distribution of ghz sequential time bin entanglement in a me.
- In sparse metropolitan entanglement networks under loss, decoherence and LOCC constraints, Bell correlations decay exponentially along entanglement-swapping paths, so CHSH-usable Bell pairs scale linearly with network size and authentication complexity scales as Θ(N log N) rather than quadratically emergent operational entanglement graphs and sub quadratic a.

## Frontier (open questions)

- Can intensity-correlation and energy-time detector effects be bounded inside a single finite-key proof, and what residual key rate remains for a fully characterised industrial decoy-state BB84 system at its rated repetition rate?
- How many discrete phase settings does DPR-MP-QKD need to reach a specified fraction (say 99%) of the continuous-phase-randomisation key rate at metropolitan and long-haul distances discrete phase randomized mode pairing quantum key distribut?
- Does the measured secret key rate of free-space LLO self-referenced PSP CVQKD hold under realistic atmospheric turbulence and over what link budget high rate free space continuous variable qkd with self refer?
- Do QMF-QSDC protocols deliver higher throughput than QKD plus one-time pad at equal security parameter and channel loss, in an experimental implementation rather than an information-theoretic analysis a quantum memory free quantum secure direct communication pr?
- Does the Θ(N log N) authentication scaling for sparse E91 networks survive measurement in a deployed multi-user network, and what operational correlation length is observed emergent operational entanglement graphs and sub quadratic a?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
