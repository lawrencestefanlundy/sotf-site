---
type: concept
slug: functional-layers
canonical_name: Functional Layers
aliases: []
parent_concepts:
- materials
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 1
descendants:
- aluminium-oxide
- aluminium-scandium-nitride
- aluminum-nitride
- barium-titanate
- cadmium-telluride
- conducting-polymers
- ferroelectric-hfo2
- hafnium-oxide
- hafnium-oxide-photonic
- high-k-dielectrics
- lithium-niobate-tfln
- lithium-tantalate-tflt
- low-k-dielectrics
- piezoelectric
- polymer-waveguides
- pzt-piezoelectric-photonic
- scandium-aluminum-nitride
- thin-film-arrays
- thin-film-magnetics
- thin-film-stability
- two-dimensional-electron-gas-2deg
frontier:
- What insertion loss per layer does the silicon-on-lithium-niobate GMR metasurface incur, and how many layers can be cascaded before throughput or wavefront fidelity collapses?
- What drive voltage and modulation bandwidth accompany the reported resonance shift, and how do they trade against the Q >2000 operating point?
- Can 100 pm perturbation control be held across a full-aperture array in a repeatable fabrication process, and what is the yield?
- What is the measured phase and amplitude range per element, and is it sufficient for the claimed holography and photonic neural network applications?
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Functional layers, in the transmissive metasurface context, are optical elements thin enough and transparent enough to be stacked in series along a beam path, so that the aggregate optical function is composed from several cascaded planar devices rather than a single bulk element. Active transmissive metasurfaces are described as central building blocks for compact, cascadable optical systems, with the stacking of multiple functional layers enabling dynamic beam shaping, photonic neural networks, depth sensing and holography.

The reported implementation uses silicon-on-lithium-niobate: an array of silicon waveguides carrying periodic perturbations supports guided-mode resonances (GMRs) with quality factors above 2000. The perturbations are individually controlled at the 100 pm scale, so the resonance condition of each radiative element is set by geometry at picometre precision.

Modulation is electro-optic. Interdigitated push-pull electrodes sit between subwavelength-spaced GMR elements and locally tune the refractive index of the lithium niobate substrate, shifting the GMR resonance. Because the electrodes drive neighbouring elements in opposition, adjacent radiative elements acquire opposite phase and amplitude modulation, which is the mechanism used to break spatial symmetry in an otherwise geometrically symmetric array.

Key parameters for this class of device are therefore resonance Q (here >2000), the geometric control resolution of the perturbation (100 pm), element pitch relative to wavelength (subwavelength), and the electro-optic index shift achievable per applied voltage in the substrate.

## Competitive landscape

The supplied source addresses only one point in the design space: high-Q guided-mode resonances in silicon-on-lithium-niobate driven electro-optically. It positions transmissive operation, rather than reflective, as the property that permits cascading into multiple functional layers. No comparative data on alternative active metasurface platforms, modulation mechanisms or reflective architectures is present in the sources, so no ranking can be drawn here.

## Evidence base

- A transmissive electro-optic metasurface on silicon-on-lithium-niobate supports guided-mode resonances with Q >2000 (5 June 2026).
- Periodic perturbations on the silicon waveguide array are individually controlled at the 100 pm scale.
- Interdigitated push-pull electrodes between subwavelength-spaced GMR elements locally tune the lithium niobate refractive index to shift the resonance.
- The push-pull drive produces opposite phase and amplitude modulation between neighbouring radiative elements, breaking spatial symmetry in a geometrically symmetric array.
- Stated target applications for stacked functional layers are dynamic beam shaping, photonic neural networks, depth sensing and holography.

## Frontier (open questions)

- What insertion loss per layer does the silicon-on-lithium-niobate GMR metasurface incur, and how many layers can be cascaded before throughput or wavefront fidelity collapses?
- What drive voltage and modulation bandwidth accompany the reported resonance shift, and how do they trade against the Q >2000 operating point?
- Can 100 pm perturbation control be held across a full-aperture array in a repeatable fabrication process, and what is the yield?
- What is the measured phase and amplitude range per element, and is it sufficient for the claimed holography and photonic neural network applications?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
