---
type: concept
slug: compressive-sensing
canonical_name: Compressive sensing
aliases: []
related_concepts:
- spectral-sensing
- spectral-imaging-sensing
last_updated: '2026-08-31'
tags:
- concept
sources: []
mention_count: 5
frontier:
- What compression ratio and reconstruction fidelity does the mid-infrared single-pixel spectrometer achieve, and how do these degrade as incident photon flux falls towards the single-photon regime?
- How does total acquisition time for a compressive single-pixel spectrometer compare with a noisy multi-pixel mid-infrared array at equal signal-to-noise ratio?
- What instantaneous bandwidth, channel count, and dynamic range does frequency-modulated local oscillator multiplexing deliver in a Rydberg receiver, and does sensitivity per channel fall relative to single-channel operation?
- Do compressive reconstructions remain reliable for dense or non-sparse spectra, and what sparsity threshold marks failure in each architecture?
parent_concepts:
- imaging
- sensing
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: spectral-sensing
  name: Spectral Sensing
  path: /sensing/mems/spectral-sensing/
  macro: sensing
---
## Physics / mechanism

Compressive sensing acquires a signal through a small number of structured, multiplexed measurements rather than sampling every channel independently, then recovers the full signal computationally by exploiting its sparsity. In practice this means designing a measurement matrix that mixes many signal components into each detected value, so that N spectral or spatial channels can be reconstructed from far fewer than N acquisitions. The approach is attractive wherever per-channel detectors are noisy, expensive, or physically unavailable.

In optical spectroscopy the measurement matrix can be imposed by a programmable spatial light modulator. A mid-infrared single-pixel spectrometer disperses light onto a digital micromirror device, which applies wavelength-encoding patterns before the encoded light is collected onto one detector. This substitutes a single low-noise detector for a multi-pixel infrared array, whose excessive noise otherwise limits sensitivity in photon-starved conditions. In that implementation the mid-infrared band is first translated: a nanophotonic supercontinuum spanning 3.1 to 3.9 micrometres is nonlinearly upconverted to the near-infrared via synchronous chirped-pulse pumping, providing both spectral mapping and sensitive detection before the compressive encoding stage.

The measurement matrix need not be optical. In a waveguide-coupled Rydberg atomic receiver, a frequency-modulated local oscillator creates multiple parallel sensing channels that collectively act as a physical compressive sensing matrix, producing several narrowband intermediate-frequency replicas of the incident RF signal. This addresses the narrow instantaneous bandwidth that fundamentally constrains Rydberg receivers, without the auxiliary electromagnetic fields or stringent parameter tuning required by approaches that physically broaden the atomic response.

Key design parameters across both cases are the number and structure of the encoding channels or patterns, the sparsity of the target spectrum, the noise of the single detection channel, and the acquisition time needed to collect the required number of multiplexed measurements.

## Competitive landscape

Compressive architectures compete against parallel-array acquisition and against physical bandwidth broadening. In mid-infrared spectroscopy, the alternative is a multi-pixel infrared array reading all spectral channels simultaneously; the compressive single-pixel design trades that parallelism for a single, quieter detector and sequential pattern acquisition. In Rydberg RF sensing, the alternative is broadening the atomic response itself using auxiliary fields, which the compressive spectral multiplexing framework is positioned against on grounds of system complexity.

The common pattern is that compressive sensing is a systems-level workaround for a detector or transducer limitation rather than a competing transducer technology, and it can be layered on top of other techniques such as nonlinear frequency upconversion.

## Evidence base

- A mid-infrared single-pixel spectrometer combining high-fidelity spectral upconversion with wavelength-encoding compressive measurement was reported on 28 May 2026.
- That system upconverts a mid-infrared nanophotonic supercontinuum spanning 3.1 to 3.9 micrometres to the near-infrared using synchronous chirped-pulse pumping.
- The upconverted signal is spatially dispersed onto a programmable digital micromirror device to implement the compressive encoding.
- The stated motivation is that conventional mid-infrared spectrometer sensitivity is limited by sensor noise, especially in multi-pixel arrays used for parallel spectral acquisition.
- A compressive spectral multiplexing framework for a waveguide-coupled Rydberg atomic receiver, using a frequency-modulated local oscillator to form a physical compressive sensing matrix, was reported on 3 July 2026.
- The Rydberg work targets the narrow instantaneous bandwidth constraint and avoids the auxiliary electromagnetic fields and parameter tuning of response-broadening methods.

## Frontier (open questions)

- What compression ratio and reconstruction fidelity does the mid-infrared single-pixel spectrometer achieve, and how do these degrade as incident photon flux falls towards the single-photon regime?
- How does total acquisition time for a compressive single-pixel spectrometer compare with a noisy multi-pixel mid-infrared array at equal signal-to-noise ratio?
- What instantaneous bandwidth, channel count, and dynamic range does frequency-modulated local oscillator multiplexing deliver in a Rydberg receiver, and does sensitivity per channel fall relative to single-channel operation?
- Do compressive reconstructions remain reliable for dense or non-sparse spectra, and what sparsity threshold marks failure in each architecture?

*Synthesised 2026-08-31 from 2 KB sources by the resynth pipeline; citations are KB source slugs.*
