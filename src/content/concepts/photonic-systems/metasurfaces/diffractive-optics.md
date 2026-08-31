---
type: concept
slug: diffractive-optics
canonical_name: Diffractive Optics
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 4
frontier:
- What insertion loss, crosstalk and port count does a trained multi-layer phase stack achieve in a deployed optical circuit switch, relative to the splitter-based multicast architectures it aims to replace?
- Can diffractive efficiency at photon energies above 20 keV be raised enough to compete with free-form refractive elements for TXM illumination, or is the refractive route structurally favoured?
- How does D²NN classification accuracy degrade with fabrication error, layer misalignment and illumination bandwidth, and what tolerance budget do lithographic processes need to hit?
- Do passive diffractive stacks retain their energy advantage once input encoding, detection and any electronic post-processing are included in end-to-end joules per inference?
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Diffractive optics shape light by imposing a spatially varying phase (or amplitude) profile on a wavefront and letting free-space propagation convert that modulation into a desired field distribution. Unlike a refractive lens, which accumulates phase through bulk material thickness, a diffractive element encodes the phase in surface relief or sub-wavelength structure, so the functional layer can be thin and lithographically or additively fabricated. Cascading several such layers, separated by propagation distances, gives a multi-layer transform whose input-output mapping is set entirely by the fixed phase patterns.

The diffractive deep neural network (D²NN) formulation treats each layer as a trainable set of phase pixels: the layers are optimised in simulation by deep learning, then fabricated as passive elements (3-D printed or lithographic), after which light diffracting through the stack performs the computation at the speed of light with no power consumed beyond the illumination lin ozcan d2nn science. The design parameters are therefore layer count, pixel pitch relative to wavelength, inter-layer spacing, and the achievable phase depth and fabrication fidelity of each pixel.

The same multi-layer phase-modulation architecture can be trained for routing rather than classification. A D²NN-style stack has been used to implement arbitrary simultaneous unicast and multicast connectivity in an optical switch, removing the lossy power splitters that limit multicast optical circuit switching scalability, and to add wavelength selectivity so that the same hardware routes in both space and wavelength dinc multicasting optical reconfigurable switch.

Efficiency is the principal physical constraint at short wavelengths. In full-field transmission X-ray microscopy, the reduced efficiency of diffractive optics at high photon energies limits performance, alongside the difficulty of matching the numerical aperture of the illumination to that of the objective; free-form diamond refractive optics were used to address the illumination-efficiency bottleneck, with full-field nano-imaging demonstrated at 20 keV free form diamond refractive optics enable efficient high en.

## Competitive landscape

| Approach | Where the sources place it |
|---|---|
| Multi-layer diffractive stacks (D²NN) | Passive, power-free optical computation and machine-learning inference at the speed of light lin ozcan d2nn science; also arbitrary unicast/multicast routing with wavelength selectivity dinc multicasting optical reconfigurable switch |
| Splitter-based multicast optical circuit switching | Scalability capped by splitter loss, which the diffractive stack eliminates dinc multicasting optical reconfigurable switch |
| Free-form refractive optics (diamond) | Chosen over diffractive optics for high-energy X-ray illumination, where diffractive efficiency falls off free form diamond refractive optics enable efficient high en |

The sources therefore show diffractive optics winning on passivity and on the ability to encode arbitrary trained transforms, and losing on raw efficiency in the hard X-ray regime, where refractive freeform elements were preferred.

## Evidence base

- The foundational D²NN paper (Lin, Rivenson, Yardimci, Veli, Luo, Jarrahi and Ozcan) appeared in *Science* **361**, 1004–1008 on 26 July 2018, establishing diffractive optics as a machine-learning substrate lin ozcan d2nn science.
- D²NN layers are passive and fabricated by 3-D printing or lithography; computation occurs at the speed of light with no power beyond the illumination lin ozcan d2nn science.
- Dinç, Yildirim, Oguz, Moser and Psaltis (arXiv:2401.14173, submitted 25 January 2024, revised 28 February 2024) used multi-layer phase modulation for a multicasting optical reconfigurable switch dinc multicasting optical reconfigurable switch.
- That switch supports arbitrary simultaneous unicast plus multicast connectivity and adds wavelength selectivity for space-wavelength routing dinc multicasting optical reconfigurable switch.
- At high photon energies, transmission X-ray microscopy performance is limited by the reduced efficiency of diffractive optics and by NA matching between illumination and objective free form diamond refractive optics enable efficient high en.
- Free-form diamond refractive optics enabled full-field nano-imaging at 20 keV, reported 22 July 2026 (arXiv:2607.19019v1) free form diamond refractive optics enable efficient high en.

## Frontier (open questions)

- What insertion loss, crosstalk and port count does a trained multi-layer phase stack achieve in a deployed optical circuit switch, relative to the splitter-based multicast architectures it aims to replace?
- Can diffractive efficiency at photon energies above 20 keV be raised enough to compete with free-form refractive elements for TXM illumination, or is the refractive route structurally favoured?
- How does D²NN classification accuracy degrade with fabrication error, layer misalignment and illumination bandwidth, and what tolerance budget do lithographic processes need to hit?
- Do passive diffractive stacks retain their energy advantage once input encoding, detection and any electronic post-processing are included in end-to-end joules per inference?

*Synthesised 2026-08-31 from 3 KB sources by the resynth pipeline; citations are KB source slugs.*
