---
type: concept
slug: quantum-random-number-generation
canonical_name: Quantum Random Number Generation
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 6
frontier:
- Can the 5.92 Gbps instantaneous spatial-noise rate be sustained once parallel or on-sensor readout replaces serial electronic readout, and what min-entropy bound survives that change 2026 07 30 quantum random number generation using spatial quantum noise?
- Does the laser-phase-noise model predict measured generation rates across different laser linewidths and interferometer delays, and what rate does it identify as optimal for a photonic-integrated implementation 2026 07 07 performance analysis and optimization for laser phase noise ?
- How does certified CV-QRNG yield per satellite pass scale with ADC resolution above 12 bits and with longer raw key records 2026 08 11 quantum random number generation from the continuous variabl?
- What insertion loss and detection efficiency do poled-fibre phase modulators achieve in practice, and is that sufficient to close the detection-efficiency requirement for device-independent randomness certification 2026 08 06 poled fibre phase modulator for efficient high dimensional q?
sources_7d: 0
sources_30d: 2
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Quantum random number generation (QRNG) extracts bits from a physical process whose outcomes are fundamentally indeterminate under quantum mechanics, rather than from a deterministic algorithm. The practical task is to isolate a quantum entropy source from classical noise, digitise it, and then apply a randomness extractor that compresses the raw data down to a length bounded by a rigorously estimated min-entropy. Randomness is needed for simulation, cryptography and secure quantum communication quantum random number generation from the continuous variabl.

Several distinct entropy sources are in active use. Laser phase noise exploits spontaneous-emission-driven phase diffusion in a semiconductor laser, converted to intensity fluctuations by an interferometer; it is attractive for its high generation rate and its suitability for photonic integration performance analysis and optimization for laser phase noise . Continuous-variable (CV) QRNG performs homodyne measurement on the vacuum state, using an existing payload laser as local oscillator and a digitising ADC quantum random number generation from the continuous variabl. Spatial-mode schemes read out the spatial intensity fluctuations of coherent light across a camera sensor, treating shot noise resolved across many pixels as a parallel entropy source quantum random number generation using spatial quantum noise.

Key design parameters are the bandwidth of the entropy source, the probability distribution of the raw samples, the ADC resolution, and the extractable randomness per sample. For laser-phase-noise QRNG a full physical model predicting the entropy-source power spectrum and the raw-data probability distribution allows the source bandwidth and extractable randomness, and therefore the achievable generation rate, to be estimated and optimised quantitatively performance analysis and optimization for laser phase noise . In CV-QRNG the ADC resolution directly sets the yield: a 12-bit ADC applied to a raw record of about 1 Mb produced roughly 19.5 Kb of certified random numbers after formal min-entropy bounding quantum random number generation from the continuous variabl.

A separate branch is device-independent QRNG, in which randomness is certified from observed measurement statistics rather than from a trusted device model. This requires efficient detection of quantum states, and high-dimensional encoding is a route to improved noise resilience and information capacity; the experimental bottleneck is the loss and polarisation sensitivity of the active modulators normally needed for basis selection poled fibre phase modulator for efficient high dimensional q.

## Competitive landscape

| Approach | Entropy source | Reported figures | Noted constraint |
|---|---|---|---|
| Laser phase noise | Spontaneous-emission phase diffusion | Rate-optimisation model validated; high rate claimed performance analysis and optimization for laser phase noise  | Complete theoretical model for optimal rate was previously incomplete performance analysis and optimization for laser phase noise  |
| CV homodyne (vacuum) | Vacuum-state quadrature fluctuations | ~1 Mb raw per satellite pass, ~19.5 Kb certified, 12-bit ADC quantum random number generation from the continuous variabl | Yield limited by raw key length and ADC resolution |
| Spatial quantum noise (EMCCD) | Spatial intensity fluctuations of coherent states | 5.92 Gbps instantaneous without algorithmic extraction; 7.5 Mbps sustained quantum random number generation using spatial quantum noise | Sustained rate capped by serial electronic readout bandwidth quantum random number generation using spatial quantum noise |
| Device-independent / high-dimensional | Certified from measurement statistics | Poled-fibre phase modulator proposed to replace lossy active modulators poled fibre phase modulator for efficient high dimensional q | Modulator loss and polarisation sensitivity in high dimensions poled fibre phase modulator for efficient high dimensional q |

The trade-off across these approaches is between raw rate, integrability, and the strength of the security assumption. Trusted-device schemes (phase noise, CV homodyne, spatial noise) deliver higher throughput but depend on a validated device model for the min-entropy bound; device-independent QRNG weakens those assumptions at the cost of detection efficiency and modulator overhead poled fibre phase modulator for efficient high dimensional q.

## Evidence base

- A comprehensive physical model for laser-phase-noise QRNG was published on 7 July 2026, predicting the entropy-source power spectrum and raw-data probability distribution so that bandwidth and extractable randomness can be estimated and the system optimised performance analysis and optimization for laser phase noise .
- An EMCCD operated in high-speed kinetic mode, with detector calibration and shot-noise analysis, gave an instantaneous random bit rate of 5.92 Gbps without algorithmic randomness extraction, reported 30 July 2026 quantum random number generation using spatial quantum noise.
- In the same spatial-noise experiment, sustained output was limited to 7.5 Mbps by serial electronic readout bandwidth, identifying readout rather than the entropy source as the bottleneck quantum random number generation using spatial quantum noise.
- CV-QRNG using homodyne measurement of vacuum states on the SPOQC mission payload yielded about 19.5 Kb of certified random numbers from about 1 Mb of raw key per satellite pass with a 12-bit ADC, with min-entropy formally upper bounded and output tested against the NIST suite quantum random number generation from the continuous variabl.
- Poled optical fibre phase modulators were proposed on 6 August 2026 to address the loss and polarisation sensitivity of active modulators used for basis selection in high-dimensional device-independent QRNG and QKD poled fibre phase modulator for efficient high dimensional q.

## Frontier (open questions)

- Can the 5.92 Gbps instantaneous spatial-noise rate be sustained once parallel or on-sensor readout replaces serial electronic readout, and what min-entropy bound survives that change quantum random number generation using spatial quantum noise?
- Does the laser-phase-noise model predict measured generation rates across different laser linewidths and interferometer delays, and what rate does it identify as optimal for a photonic-integrated implementation performance analysis and optimization for laser phase noise ?
- How does certified CV-QRNG yield per satellite pass scale with ADC resolution above 12 bits and with longer raw key records quantum random number generation from the continuous variabl?
- What insertion loss and detection efficiency do poled-fibre phase modulators achieve in practice, and is that sufficient to close the detection-efficiency requirement for device-independent randomness certification poled fibre phase modulator for efficient high dimensional q?

*Synthesised 2026-08-31 from 4 KB sources by the resynth pipeline; citations are KB source slugs.*
