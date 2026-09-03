---
type: concept
slug: etch
canonical_name: Etch
aliases: []
parent_concepts:
- equipment-processes
- manufacturing
related_concepts: []
sources:
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2026-07-07-the-asml-killer]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-07-28-laser-on-a-chip-w-matt-crowley-scintil]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-06-22-thermal-stack-layer-landscape]]'
- '[[2026-07-09-in-die-microfluidic-cooling-sprint]]'
- '[[2026-07-31-etched-research-sprint]]'
- '[[2026-06-22-physics-ai-comp-landscape]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 45
frontier:
- What taper angle is achievable at production throughput for high-aspect-ratio stack etches, and at what layer count does the resulting die-cost minimum fall for current 3D memory nodes walker 2013 rigorous 3d nand flash cost analysis?
- Can SC-1 wet etching of Nb and TiN be shown to improve superconducting resonator or qubit coherence relative to plasma-etched controls, with quantitative loss-tangent comparison 2026 05 28 sc 1 etching of niobium and titanium nitride thin films?
- Does lithography-guided anisotropic TMD etching retain atomically sharp zigzag edges over extended, non-confined geometries at wafer scale 2026 06 24 precise one dimensional nanochannels in transition metal dic?
- What etch-depth and sidewall-angle tolerance windows do inverse-designed TFLN and SiN devices survive before measured performance departs from the reduced-order model prediction 2026 08 14 inverse designed lithium niobate wavelength demultiplexer vi?
sources_7d: 0
sources_30d: 6
recent_mentions:
- slug: 2026-07-31-etched-research-sprint
  title: Etched research sprint — tape-out speed, HBM supply, customer orders (4-lane web sweep)
  date: '2026-07-31'
  kind: web
- slug: 2026-07-28-laser-on-a-chip-w-matt-crowley-scintil
  title: Laser on a Chip w/ Matt Crowley @ Scintil Photonics
  date: '2026-07-28'
  kind: substack
- slug: 2026-07-09-in-die-microfluidic-cooling-sprint
  title: In-die microfluidic cooling — cluster research sprint
  date: '2026-07-09'
  kind: web
- slug: 2026-07-07-the-asml-killer
  title: The ASML Killer?
  date: '2026-07-07'
  kind: substack
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-physics-ai-comp-landscape
  title: Physics-AI / ML-surrogate simulation competitive landscape (Zenithon comp set beyond PhysicsX)
  date: '2026-06-22'
  kind: web
- slug: 2026-04-14-the-photonic-foundry-fallacy
  title: The Photonic Foundry Fallacy
  date: '2026-04-14'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors: []
---
## Physics / mechanism

Etch is the subtractive patterning step in microfabrication: material is removed from a substrate, either everywhere or selectively through a lithographically defined mask, to transfer a pattern into a film or into the bulk. The dominant industrial family is dry (plasma) etching, in which reactive species and ions generated in a discharge combine chemical attack with directional ion bombardment to produce anisotropic profiles. The alternative family is wet etching, in which a liquid chemistry dissolves the exposed material, generally with higher selectivity between materials but weaker directional control unless the etch follows crystallographic planes.

The parameters that matter are etch rate, selectivity to mask and underlying layers, achievable depth, sidewall angle, and induced damage. Sidewall angle is not a cosmetic detail. Any deep etch has a non-zero taper angle, so a hole or slit is wider at the top of a stack than at the bottom, and it is the pitch at the *top* of the stack that sets the footprint projected onto the wafer; in 3D NAND this taper is a first-order term in die cost, and its interaction with layer count produces a minimum in die cost per bit rather than monotonically falling cost as layers are added **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. Etch depth also functions as a design variable in photonics: inverse-designed thin-film lithium niobate devices show explicit etch-depth dependence, and fabrication-induced slanted sidewalls must be represented in the model cross-section for the design to be accurate. A bilayer silicon-nitride grating for trapped-ion addressing encodes its coupling envelope in discrete etch levels rather than sub-resolution linewidths, using two etch depths per film so that every feature satisfies a 125 nm deep-UV minimum rule.

Plasma-induced damage is the recurring failure mode when the etched material carries a quantum or optical function. Dry etching often leaves challenging levels of undesired collateral damage, which motivates wet alternatives such as SC-1 (Standard Clean 1) solution for patterning niobium and titanium nitride thin films, where etch dynamics are linked to native oxides and film microstructure and the attraction is manageable rates, safe operation and high material selectivity. In conventional lithography plus dry etch on van der Waals crystals, edge roughness limits optical confinement and reproducibility, whereas anisotropic wet etching of multilayer transition metal dichalcogenides gives crystallographically defined, atomically sharp zigzag edges.

Deep etches are also used as isolation and field-management structures. A deep mesa etch that removes epitaxial material except at the device allows low-microwave-loss circuit elements to be placed on the exposed substrate, addressing semiconductor microwave loss in voltage-tunable Josephson junctions on germanium quantum wells. In vertical gallium oxide devices, multi-fin channels 200 nm wide were etched to a trench depth of about 1.2 µm to give enhancement-mode operation with a 2 V threshold voltage and on/off ratio above 10^7.

## Competitive landscape

The practical choice is between plasma (dry) etching, which gives directionality and depth but risks surface and subsurface damage, and wet or thermally activated chemical etching, which gives selectivity and damage-free surfaces at the cost of profile control. Recent results in wide-bandgap and quantum materials sit at this boundary.

| Approach | Reported strength | Reported limitation |
|---|---|---|
| ICP-RIE plasma etch (diamond) | Thins direct-bonded single-crystal diamond membranes (<50 µm) into large-area diamond-on-insulator; recipe preserves diamond quality and yields free-standing photonic chiplets | Substrate size from heteroepitaxial growth remains the integration constraint |
| Wet SC-1 etch (Nb, TiN) | Manageable rates, safe operation, high selectivity, avoids plasma damage | Dynamics depend on native oxides and film microstructure |
| Anisotropic wet etch (TMDs) | Atomically sharp crystallographic zigzag edges, no edge roughness | Intrinsically limited to confined geometries set by stacking symmetry; lithography-guided variants extend this |
| Plasma-free Ga-assisted thermal etch (β-Ga2O3) | Deep mesa field termination with diode characteristics closely matching unetched planar devices | Requires LPCVD thermal activation rather than a standard plasma tool |

## Evidence base

- Deep-etch taper angle means the top-of-stack cell pitch defines the array footprint, so 3D NAND die cost passes through a minimum and then rises with each added layer, contradicting the monotonic cost-per-bit premise **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.
- SC-1 solution demonstrated as a wet-etch alternative for patterning Nb and TiN thin films, with etch dynamics linked to native oxides and film microstructure, published 28 May 2026.
- An ICP-RIE recipe thinned direct-bonded (100) single-crystal diamond membranes below 50 µm into large-area diamond-on-insulator substrates and produced free-standing photonic chiplets, 19 June 2026.
- Plasma-free Ga-assisted etching in an LPCVD system formed deep mesa field terminations on β-Ga2O3 Schottky barrier diodes with 1.14 V turn-on, 1.15 eV barrier height, ideality factor 1.20 and 3.72 mΩ·cm² specific on-resistance, matching unetched planar devices, 30 June 2026.
- Vertical Ga2O3 ISEFETs used 200 nm-wide multi-fin channels etched to ~1.2 µm trench depth, giving 2 V threshold voltage and >10^7 on/off ratio without planarization etch-back, 14 August 2026.
- A DUV-compatible bilayer grating used two etch depths per silicon-nitride film, with all features meeting a ≥125 nm rule, to route 729.4 and 854.2 nm fields through one electrode aperture, 28 July 2026.

## Frontier (open questions)

- What taper angle is achievable at production throughput for high-aspect-ratio stack etches, and at what layer count does the resulting die-cost minimum fall for current 3D memory nodes **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**?
- Can SC-1 wet etching of Nb and TiN be shown to improve superconducting resonator or qubit coherence relative to plasma-etched controls, with quantitative loss-tangent comparison?
- Does lithography-guided anisotropic TMD etching retain atomically sharp zigzag edges over extended, non-confined geometries at wafer scale?
- What etch-depth and sidewall-angle tolerance windows do inverse-designed TFLN and SiN devices survive before measured performance departs from the reduced-order model prediction?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
