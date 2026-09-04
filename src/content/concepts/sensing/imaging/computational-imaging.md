---
type: concept
slug: computational-imaging
canonical_name: Computational Imaging
aliases: []
parent_concepts:
- imaging
- sensing
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 16
frontier:
- Does embedding optical priors into the learning pipeline (as in PDI-Net) break the reported accuracy/latency trade-off on standard detection benchmarks, and what end-to-end latency figures are achievable on embedded infrared hardware 2026 06 02 dual integrated low latency single lens infrared computation?
- How far can the passive microlens-plus-glass-stack architecture extend sequence depth beyond ten frames without losing the 1.46 ps sampling interval or the sub-US$500 cost 2026 06 05 low cost passive single shot ultrafast imaging at 685 gfps?
- When generative diffusion priors are used for photon-limited reconstruction, what quantitative bounds separate photometrically faithful recovery from prior-induced hallucination at a given detected-photon count 2026 06 05 gqir generative quanta image reconstruction?
- Can physics-based self-supervised hologram reconstruction match iterative algorithms on quantitative phase-shift and absorption accuracy, not just twin-image suppression 2026 07 03 physics based self supervised learning of a deep network for?
- Does the single-wavelength restriction of the differentiable ray-wave model limit end-to-end optimisation of broadband hybrid refractive-diffractive imagers, and what error does polychromatic operation introduce 2026 08 14 a differentiable ray wave framework for hybrid refractive di?
sources_7d: 2
sources_30d: 3
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Computational imaging replaces the one-to-one mapping between scene points and detector pixels with an encoded measurement plus an inverse algorithm. The optical front end deliberately multiplexes the scene (through a coded aperture, diffractive element, scattering layer, microlens array or a single non-pixelated detector), and the image is recovered by solving an inverse problem constrained by a forward model of the optics. This decoupling lets the hardware be simplified or the measurement domain extended into regimes where a conventional lens-plus-array camera fails: photon-starved scenes, ultrafast transients, or targets behind scattering tissue.

Several distinct encoding strategies appear across the source set. Single-pixel imaging reconstructs spatial information from sequentially encoded optoelectrical signals without any pixelated detector array, so the detector material rather than the pixel pitch sets performance; a lead-free K₂CuBr₃ thin-film photoconductor has been used as the near-UV photoactive channel, showing photoswitching under 405 nm illumination and dark current on the order of 10⁻¹⁰ A. Synthetic wavelength holography interferes two optical fields to create a much longer synthetic wavelength, allowing lensless wide-field 3D fibre endoscopy through scattering layers between the target and the distal fibre end. Digital in-line holographic microscopy records only the intensity of a diffraction pattern, making the inversion to phase shift and absorption non-trivial and producing the twin-image artefact under naive backward propagation. Temporal encoding is also possible: a microlens array plus a stack of microscope cover glasses maps temporal information into spatial channels, recording delayed replicas within one CMOS exposure.

Key design parameters are therefore split between optics and compute: encoding diversity and conditioning of the forward operator, detector noise statistics and dark current, temporal sampling interval and sequence depth for transient capture, and the inference latency of the reconstruction network. Latency is a first-order constraint in machine-vision use: pipelines that chain reconstruction and detection add substantial inference cost, and compressing the reconstruction network alone leaves an accuracy/speed trade-off unless optical priors from the light path are embedded in the learning process. Co-design of the optics itself requires differentiable models; a differentiable ray-wave framework has been proposed for hybrid refractive-diffractive systems, applying to planar and curvilinear diffractive surfaces and arbitrary scalar holographic profiles, with each simulation evaluated at a single wavelength.

## Competitive landscape

Within ultrafast imaging, the sources contrast three routes: streak cameras, compressed-sensing computational imaging, and fully passive spatial-multiplexing optics. The first two are described as complex and costly; the passive off-the-shelf architecture reports hardware cost below US$500 with a 1.46 ps sampling interval, 685 Gfps effective frame rate and a sequence depth of ten frames, i.e. it trades sequence depth for cost and simplicity. For detector architectures, single-pixel imaging trades acquisition time (sequential encoding) for the elimination of a pixelated array, which matters most where array fabrication in a given spectral band is hard or where the photoactive material is novel. Perovskite candidates for such channels face a toxicity barrier from lead-based compositions, which motivates lead-free films.

On the reconstruction side, three families coexist: iterative model-based inversion, supervised deep networks, and physics-constrained self-supervised or generative-prior methods. The last group is attractive where labelled ground truth is unavailable (holography) or where measurement statistics are far from those assumed by pretrained restoration models (SPAD quanta bursts). Programmable metasurfaces sit adjacent as a reconfigurable encoding layer shared with holography and backscatter communications.

## Evidence base

- A lensless synthetic wavelength holography approach for wide-field 3D fibre endoscopy through scattering media was reported on 29 May 2026, targeting lesions obscured by scattering tissue.
- Lead-free K₂CuBr₃ thin-film photoconductors for near-UV single-pixel imaging were demonstrated with stable photoswitching at 405 nm and dark current around 10⁻¹⁰ A, reported 2 June 2026.
- PDI-Net integrates infrared reconstruction with object detection using a supervised U-Net at training time and a semi-U-Net encoder sharing features with a YOLO-based detector at inference, avoiding full image reconstruction; reported 2 June 2026.
- A passive single-shot ultrafast imager built from a commercial microlens array, microscope cover glasses and a consumer CMOS sensor achieved 1.46 ps sampling, 685 Gfps and ten frames for under US$500, reported 30 April 2026.
- gQIR adapts large text-to-image latent diffusion models to SPAD quanta burst imaging, handling Bernoulli photon statistics with burst-level spatio-temporal reasoning; reported 23 February 2026.
- A differentiable ray-wave framework for hybrid refractive-diffractive systems, operating as a plug-and-play module in standard ray tracing pipelines and covering curvilinear diffractive surfaces, was reported 14 August 2026.
- Prototype-aware bounds on wavefront synthesis with programmable metasurfaces, accounting for mutual coupling, binary programmability and lossy tunable loads, were derived using multiport network theory and semidefinite relaxation, reported 16 June 2026.

## Frontier (open questions)

*Synthesised 2026-08-31 from 9 KB sources by the resynth pipeline; citations are KB source slugs.*
