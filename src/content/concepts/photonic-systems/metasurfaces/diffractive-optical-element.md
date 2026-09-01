---
type: concept
slug: diffractive-optical-element
canonical_name: Diffractive Optical Element
aliases: []
parent_concepts:
- metasurfaces-flat-optics
- photonic-systems
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 5
frontier:
- How far can the number of write spots and the number of simultaneously addressed axial planes be scaled in DOE-based 2PP before spot uniformity or cross-talk between planes degrades feature fidelity beyond tolerance?
- What is the measured diffraction efficiency and energy-uniformity spread of the multi-spot DOEs reported, and how do these compare with metalens equivalents at the same aperture?
- Does DOE-generated multi-plume beam splitting yield a quantified net gain in LIBS emission per unit pulse energy relative to a single Gaussian spot of equal fluence?
- Can DOEs fabricated in high-thermal-conductivity materials match the 25 W, 1 h focal stability demonstrated for diamond metalenses, or is survivability at that power specific to metasurface nanopillar geometries?
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

A diffractive optical element (DOE) is a passive, typically static component that imposes a designed phase (and sometimes amplitude) profile on an incident beam, so that interference in the propagated field produces a target intensity distribution. Because the function is encoded in surface relief or a multilevel phase mask rather than in bulk refraction, one thin element can replace a train of lenses, beamsplitters and apertures. The most common use is beam splitting and beam shaping: converting a single Gaussian input into an array of foci, or into a structured probe with properties unattainable by focusing alone.

Multi-spot generation is the workhorse mode. A DOE can transform a Gaussian beam into a 2x2 array of co-propagating spots, which in laser-induced breakdown spectroscopy produces multiple ablation plumes that expand simultaneously and interact. The same principle extends into the third dimension: a single static DOE can be designed to place two independent focal-spot arrays in distinct axial planes, with 29 write spots split across two planes separated by 1.8 µm demonstrated for two-photon polymerization. Key design parameters are therefore the number and geometry of spots, the axial separation between planes, the uniformity of energy distribution, and the diffraction efficiency into the wanted orders.

Beyond replication of foci, multilevel DOEs can synthesise fields whose local structure beats the conventional focusing limit. In super-oscillatory label-free inertia-free scanning (SOLIS) microscopy, a static multilevel DOE generates compressed super-oscillatory probes, and a digital micromirror device selects among them so that scanning requires no stage motion; a 25-position scan yields one averaged map every 3.58 ms, or 279 reconstructed frames per second. On nanofabricated line-pair targets the approach retained measurable label-free contrast at a 253 nm period and resolved modulation at 270 nm.

The practical trade-off is that a static DOE fixes its function at fabrication time. Throughput gains come from parallelism rather than from reconfigurability: dual-plane multi-spot 2PP achieved an effective writing speed of 1 mm² in 90 s for four-layer woodpile structures while retaining a simple scanning strategy.

## Competitive landscape

DOEs sit between fully refractive multi-beam optics and actively addressed modulators. Conventional multifocal systems built from bulk optics remain constrained by bulky architectures, stringent alignment requirements and susceptibility to laser-induced degradation under intense irradiation. Metasurfaces are the closest structural competitor: a monolithic diamond metalens with a 7.2 mm aperture and high-aspect-ratio truncated-cone nanopillars produced two focal spots separated by 200 µm at a 4 mm focal length, and under 25 W pulsed irradiation for 1 h showed a focal shift of only 25.5 µm. That points to material choice, not diffractive versus metasurface phase encoding, as the determinant of high-power survivability.

| Approach | Reconfigurable | Demonstrated role in sources |
|---|---|---|
| Static DOE | No | 2x2 beam splitting for LIBS; 29-spot dual-plane 2PP; super-oscillatory probes |
| DOE plus DMD | Probe selection only | Inertia-free scanning without stage motion |
| Diamond metalens | No | Multifocal high-power laser processing with thermal stability |

## Evidence base

- 2026-06-05: A single static DOE generated 29 write spots across two planes 1.8 µm apart, enabling four-layer woodpile fabrication at an effective writing speed of 1 mm² in 90 s.
- 2026-06-05: The authors note that DOE multi-spot generation in a single plane still leaves three-dimensional structures to be built sequentially layer by layer, which is the limitation the dual-plane design addresses.
- 2026-07-07: A DOE converted a Gaussian Nd:YAG beam (1064 nm, 5 ns, 10 J/cm²) into a 2x2 array to study interacting ablation plumes from Cu and Si targets in vacuum.
- 2026-07-22: SOLIS microscopy used a static multilevel DOE plus DMD to reach 279 reconstructed fps (3.58 ms per 25-position scan) with label-free contrast at a 253 nm line-pair period.
- 2026-07-29: A 7.2 mm-aperture diamond metalens produced two foci 200 µm apart at 4 mm focal length and drifted only 25.5 µm after 1 h at 25 W, giving 33.2 µm maximum processing-depth variation in 4H-SiC scribing.

## Frontier (open questions)

- How far can the number of write spots and the number of simultaneously addressed axial planes be scaled in DOE-based 2PP before spot uniformity or cross-talk between planes degrades feature fidelity beyond tolerance?
- What is the measured diffraction efficiency and energy-uniformity spread of the multi-spot DOEs reported, and how do these compare with metalens equivalents at the same aperture?
- Does DOE-generated multi-plume beam splitting yield a quantified net gain in LIBS emission per unit pulse energy relative to a single Gaussian spot of equal fluence?
- Can DOEs fabricated in high-thermal-conductivity materials match the 25 W, 1 h focal stability demonstrated for diamond metalenses, or is survivability at that power specific to metasurface nanopillar geometries?

*Synthesised 2026-08-31 from 4 KB sources by the resynth pipeline; citations are KB source slugs.*
