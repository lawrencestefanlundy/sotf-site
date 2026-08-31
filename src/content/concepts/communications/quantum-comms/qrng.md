---
type: concept
slug: qrng
canonical_name: Qrng
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2026-08-03-spad-single-photon-market-scan]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 21
frontier:
- What certified bit rate per second, not per round, does the integrated contextuality QRNG achieve, and does the 0.077 bits-per-round min-entropy scale with mesh size or qutrit dimension 2026 06 07 on chip semi device independent quantum random number genera?
- 'Can the SPOQC CV-QRNG certified yield be raised above the ~2% of raw key achieved per pass, and what specifically limits it: ADC resolution, min-entropy bounding conservatism, or extractor overhead 2026 08 11 quantum random number generation from the continuous variabl?'
- Does the two-source seedless bootstrapping scheme survive an adversary with partial correlation between the two supposedly independent entropy sources, and what independence assumption is required quantitatively 2026 08 13 information theoretic solutions for seedless qrng bootstrapp?
- Does the predictability-coherence equality for multi-path interferometry yield an operationally tighter min-entropy bound than existing semi-DI certification for interference-based QRNGs 2026 07 22 trade off between predictability and quantum coherence for m?
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2026-08-03-spad-single-photon-market-scan
  title: SPAD / single-photon detector market scan — incumbent structure and company cohort
  date: '2026-08-03'
  kind: web
neighbors: []
---
## Physics / mechanism

A quantum random number generator (QRNG) extracts unpredictable bits from the intrinsic indeterminism of a quantum measurement rather than from a deterministic algorithm or a classical noise source. Two device families dominate the sources here. The discrete-variable route uses single photons in an interferometric network, where the which-path outcome is fundamentally random; the continuous-variable route performs homodyne measurement on the vacuum state and digitises the resulting quadrature fluctuations.

The output metric that matters is not raw bit rate but certified conditional min-entropy: the number of bits per round that remain unpredictable to an adversary who may partially control the device. Semi-device-independent QRNGs certify this from an observed violation of a non-classical inequality, so the security claim rests on measured statistics plus a small set of assumptions rather than on a full physical model of the hardware. An on-chip implementation integrating two silicon photonic chips, combining a heralded single-photon source with a reconfigurable interferometric mesh to prepare, transform and measure qutrit states, tested a KCBS contextuality inequality and reported a violation exceeding the classical bound by more than 10σ, from which a conditional min-entropy of H_min = 0.077 ± 0.002 per round was certified via a semidefinite-programming-based analysis. Contextuality-based certification requires no entanglement, which relaxes the hardware burden relative to loophole-free Bell-test approaches.

Raw quantum-derived bits are not uniform, so a randomness extractor is applied. Universal hash functions act as strong seeded extractors, with security bounded by the Quantum Leftover Hash Lemma. This creates the "randomness loop": a seeded extractor needs an initial random seed in order to produce randomness. One proposed resolution bootstraps from the raw data of two independent seedless QRNG entropy sources, and the same extractor machinery is proposed as an alternative to XOR-based combining of post-quantum cryptography and QKD keys.

Throughput after certification and extraction is severely reduced relative to raw acquisition. In a satellite-based CV-QRNG demonstration using the continuous-variable payload of the SPOQC mission, a raw key of roughly 1 Mb per satellite pass yielded approximately 19.5 kb of certified random numbers from a 12-bit ADC, with output validated against the NIST test suite and a formal upper bound placed on the min-entropy.

## Competitive landscape

| Approach | Entropy source | Certification | Reported figure |
|---|---|---|---|
| Semi-DI contextuality, integrated photonics | Heralded single photons in a reconfigurable mesh | KCBS inequality violation, SDP-derived bound | >10σ violation; H_min = 0.077 ± 0.002 per round |
| CV homodyne (vacuum fluctuations) | Vacuum-state quadrature noise, laser + homodyne detector | Min-entropy upper bound plus NIST suite | ~19.5 kb certified from ~1 Mb raw per satellite pass, 12-bit ADC |

The trade-off is between assumption strength and rate. The contextuality device buys a device-independence-flavoured security claim without entanglement, at the cost of a low certified entropy yield per round. The CV homodyne route reuses hardware already present for other functions, since the SPOQC payload laser also serves the QRNG and the homodyne detector could double as the receiver in an uplink scenario, favouring it where space, mass and power are constrained. Both then depend on the same downstream extractor and seeding question. Single-photon detector supply is a relevant upstream dependency for the discrete-variable route; market scanning identifies STMicroelectronics as the leading SPAD player on CMOS-integrated SPAD and vertically integrated manufacturing, with Sony Semiconductor Solutions and Hamamatsu Photonics in second tier.

## Evidence base

- On 7 June 2026, an on-chip semi-device-independent QRNG integrating two silicon photonic chips reported a KCBS contextuality violation exceeding the classical bound by more than 10σ and certified H_min = 0.077 ± 0.002 per experimental round.
- The same work states that contextuality-based certification permits quantitative security certification without requiring entanglement.
- On 11 August 2026, a CV-QRNG using the SPOQC mission continuous-variable payload extracted approximately 19.5 kb of certified random numbers from a raw key of approximately 1 Mb per satellite pass with a 12-bit ADC, tested against the NIST suite.
- The SPOQC homodyne setup uses the payload laser and could also serve as the detector in an uplink scenario, indicating hardware reuse across mission functions.
- On 13 August 2026, a proposal resolved the QRNG randomness loop by bootstrapping from raw data of two independent seedless entropy sources, using universal hash functions as strong seeded extractors with security from the Quantum Leftover Hash Lemma.
- The same work argues strong seeded extractors are an alternative to XOR-based combining of post-quantum cryptography and QKD keys.
- On 22 July 2026, a derived trade-off relation between basis-dependent predictability and a Kirkwood-Dirac-quasiprobability coherence measure for multi-path interferometry was reported as an exact equality for pure states.

## Frontier (open questions)

- What certified bit rate per second, not per round, does the integrated contextuality QRNG achieve, and does the 0.077 bits-per-round min-entropy scale with mesh size or qutrit dimension?
- Can the SPOQC CV-QRNG certified yield be raised above the ~2% of raw key achieved per pass, and what specifically limits it: ADC resolution, min-entropy bounding conservatism, or extractor overhead?
- Does the two-source seedless bootstrapping scheme survive an adversary with partial correlation between the two supposedly independent entropy sources, and what independence assumption is required quantitatively?
- Does the predictability-coherence equality for multi-path interferometry yield an operationally tighter min-entropy bound than existing semi-DI certification for interference-based QRNGs?

*Synthesised 2026-08-31 from 5 KB sources by the resynth pipeline; citations are KB source slugs.*
