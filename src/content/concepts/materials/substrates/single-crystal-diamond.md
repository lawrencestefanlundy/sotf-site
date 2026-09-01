---
type: concept
slug: single-crystal-diamond
canonical_name: Single Crystal Diamond
aliases: []
parent_concepts:
- substrates
- materials
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 2
frontier:
- What uncertainty is achieved on d_NV and on the NV azimuthal orientation using the stripe-and-disc calibration, and how does it compare with vector-magnet-based determination?
- How reproducible are these parameters across nanostructures fabricated from the same single crystal diamond substrate, and how much of the spread is attributable to substrate quality versus fabrication?
- Does the calibration remain valid as probes wear or are exchanged, and what re-calibration interval is required for traceable measurements?
- Can the same method be transferred to polycrystalline or heteroepitaxial diamond hosts, or does it depend on the single crystal lattice fixing the NV symmetry axis?
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Single crystal diamond is a substrate material in which the carbon lattice is continuous and free of grain boundaries, distinguishing it from polycrystalline or nanocrystalline diamond films. In quantum sensing applications the crystal serves as a host matrix for point defects, most prominently the nitrogen vacancy (NV) centre, a substitutional nitrogen atom adjacent to a carbon vacancy. Because the defect sits in a defined crystallographic setting, its high symmetry axis is fixed relative to the lattice, and the crystal orientation therefore determines the vector projection axis along which magnetic fields are measured.

The substrate can be micro- and nanostructured while retaining the optical and spin properties of embedded defects. Individual, scannable NV centres in single crystal diamond nanostructures allow nanoscale, quantitative imaging of magnetic stray fields. In this geometry the diamond nanostructure acts simultaneously as the mechanical scanning probe, the optical waveguide collecting NV fluorescence, and the crystalline reference frame that sets the sensing axis.

Two parameters dominate quantitative use of such probes: the distance between the NV centre and the sample surface, d_NV, and the azimuthal orientation of the NV high symmetry axis. These are frequently unknown with precision and are absorbed into data evaluation as free fitting parameters, which limits traceability of the reconstructed field. Calibration against known magnetisation patterns, specifically micro-patterned, perpendicularly magnetised stripes and discs, allows both d_NV and the azimuthal orientation to be inferred directly without an external vector magnet.

## Competitive landscape

The supplied source does not compare single crystal diamond against alternative substrates or sensor hosts. Its positioning is narrower: single crystal diamond is treated as the enabling host for individual, addressable NV centres in scanning-probe form, where defect placement and crystal axis orientation must be controlled at the level of a single emitter. Competing calibration strategies within the same platform are distinguished by whether an external vector magnet is required to establish the NV orientation; the reported method does not need one.

## Evidence base

- Individual, scannable NV centres in single crystal diamond nanostructures enable nanoscale, quantitative imaging of magnetic stray fields (announced 6 August 2026).
- NV-sample distance and the orientation of the NV high symmetry axis are often not known precisely and enter data evaluation as free fitting parameters.
- Scanning NV imaging of micro-patterned, perpendicularly magnetised stripes and discs was used to infer d_NV and the NV azimuthal orientation directly.
- The reported determination of orientation and distance does not require control of an external vector magnet.
- The work is framed as a set of methods for traceable scanning magnetometry, covering orientation, distance and localisation.

## Frontier (open questions)

- What uncertainty is achieved on d_NV and on the NV azimuthal orientation using the stripe-and-disc calibration, and how does it compare with vector-magnet-based determination?
- How reproducible are these parameters across nanostructures fabricated from the same single crystal diamond substrate, and how much of the spread is attributable to substrate quality versus fabrication?
- Does the calibration remain valid as probes wear or are exchanged, and what re-calibration interval is required for traceable measurements?
- Can the same method be transferred to polycrystalline or heteroepitaxial diamond hosts, or does it depend on the single crystal lattice fixing the NV symmetry axis?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
