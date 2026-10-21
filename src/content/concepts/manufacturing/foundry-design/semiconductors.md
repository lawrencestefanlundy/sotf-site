---
type: concept
slug: semiconductors
canonical_name: Semiconductors
aliases:
- semiconductor
- semis
- semiconductor-industry
- chips
- chip-industry
parent_concepts:
- foundry-design
- manufacturing
related_concepts:
- logic
- advanced-packaging
- emerging-memory
- electronics-manufacturing
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2023-06-15-e04-no10-downing-street-and-vector]]'
- '[[2025-09-23-the-compute-gradient]]'
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-08-18-e11-in-conversation-with-lux-capital]]'
- '[[2026-03-26-sotf-interview-dorian-haci-mintneuro]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-05-consensus-capital]]'
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-02-25-data-driven-vc-is-over]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
scorecard:
  viability: 3
  drivers: null
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Later (5-10yr)
  verdict: Too early to say
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-10-20-the-lithography-lever
  title: The Lithography Lever
  date: '2026-10-20'
  kind: web
- slug: 2026-10-20-new-brain-for-galileo
  title: New brain for Galileo
  date: '2026-10-20'
  kind: web
- slug: 2026-10-18-a-single-microwave-line-runs-five-silicon-spin-qubits-with-9
  title: A single microwave line runs five silicon spin qubits with 99.9% accuracy
  date: '2026-10-18'
  kind: web
- slug: 2026-10-17-the-case-for-duv-controls
  title: The Case for DUV Controls
  date: '2026-10-17'
  kind: web
- slug: 2026-10-16-cambridge-enterprise-contributes-to-162m-series-a-for-paragr
  title: Cambridge Enterprise contributes to £16.2m Series A for Paragraf - Cambridge Enterprise
  date: '2026-10-16'
  kind: web
- slug: 2026-10-15-writing-electronic-phases-into-atomic-layers
  title: Writing electronic phases into atomic layers
  date: '2026-10-15'
  kind: web
- slug: 2026-10-15-us-urges-chipmakers-to-use-domestic-capacity-as-chips-act-st
  title: US urges chipmakers to use domestic capacity as CHIPS Act strategy shifts from fab subsidies to securing orders - digitimes
  date: '2026-10-15'
  kind: web
- slug: 2026-10-15-gate-tunable-chiral-spin-mode-in-wse2ws2-moire-superlattices
  title: Gate-tunable chiral spin mode in WSe2/WS2 moiré superlattices
  date: '2026-10-15'
  kind: web
neighbors:
- slug: logic
  name: Compute & Logic
  path: /compute/conventional-logic/logic/
  macro: compute
- slug: advanced-packaging
  name: Advanced Packaging
  path: /manufacturing/packaging/advanced-packaging/
  macro: manufacturing
- slug: emerging-memory
  name: Emerging Memory
  path: /memory/emerging-memory/emerging-memory/
  macro: memory
- slug: electronics-manufacturing
  name: Electronics Manufacturing
  path: /manufacturing/equipment-processes/electronics-manufacturing/
  macro: manufacturing
---
**Semiconductors are materials whose conductivity can be tuned by doping, gating, thickness and defect engineering, and the current research literature is mostly about extending that control beyond silicon into monolayer dichalcogenides, organic crystals, quantum-dot solids and polar nitrides, where the physics is now well characterised at lab scale but manufacturing is not addressed at all.**

## Summary

A semiconductor is a solid with an energy gap between its filled valence states and empty conduction states. Everything useful follows from being able to move that gap around and to put controlled numbers of carriers into it: dope it, gate it, strain it, thin it, put it in a cavity. The engineering parameters that decide device behaviour are the size and directness of the band gap, the effective mass of electrons and holes (which sets mobility), the carrier density achievable by doping, the dielectric response, and how efficiently heat leaves the active region.

The sources collected here are almost entirely condensed-matter and optics papers from 2024 to 2026, and they map the frontier rather than the industry. A large fraction concerns two-dimensional transition metal dichalcogenides, where the gap depends on layer count: scanning tunnelling spectroscopy on MBE-grown MoS2 from one to five layers shows the gap falling sharply with thickness, to values below the bulk gap, with conduction-band pinning vanishing above four layers. Others deal with organic molecular semiconductors, where crystal packing rather than molecular design governs transport: a previously unrecognised and thermodynamically stable polymorph of the benchmark material DNTT was found coexisting in commercial powders, and it changes the dimensionality of charge transport. Colloidal quantum-dot films, increasingly used in place of bulk semiconductors, were measured at thermal conductivities as low as 0.55 W/m/K because heat moves poorly through close-packed dot solids.

## Viability (3/5)

What is absent is any evidence of scale. Growth is by molecular beam epitaxy or chemical vapour deposition on small substrates; the photovoltaic work is a thermodynamic framework rather than a fabricated stack; and several papers are purely first-principles. A 3 reflects credible laboratory viability of the physics with no demonstrated path, in these sources, to yield, uniformity or wafer scale.

**TLDR: The individual physics results are real, measured and peer-reviewed, but nothing here goes beyond single devices or small samples.**

## Drivers (unscored)

Those are researchers describing their own field's momentum, not evidence of commercial pull. On the supply side there is nothing on equipment, precursors, substrates or fab economics. A score here would be fabricated, so it is null.

**TLDR: The sources contain no market, demand, capital or supply-chain information at all.**

## Novelty (3/5)

Several results are explicitly better than a stated alternative and by a stated margin. The k-point extension of the co-iterative augmented Hessian method for Pipek-Mezey Wannier functions runs roughly two to three times faster than first-order k-space approaches and orders of magnitude faster than Gamma-point CIAH for 1000 to 5000 orbitals. A tuned hybrid functional reproduces CrSBr optical gaps and exciton-magnetism coupling at substantially lower cost than self-consistent many-body perturbation theory. Terahertz spectroscopy is better than four-point probe and capacitance-voltage measurement in one specific respect, being contact-free, and the new contribution is a sensitivity metric that says where it can be used.

**TLDR: Real advances over prior lab practice, quantified in a few cases, but each is an increment inside a subfield rather than a step change.**

## Diffusion (2/5)

The obstacles are named in the sources themselves. Quantum-dot films conduct heat at 0.55 W/m/K, which the authors attribute to poor heat flow within close-packed dot solids and flag as a thermal management problem for devices. Half-metallicity in vacancy-doped TiS2 requires a defect network above a 12.5% percolation threshold, meaning defect density must be held in a narrow window across a whole film. Multijunction TMD photovoltaics rely on transfer-printed stacking of many junctions, and the analysis shows radiative quality and optics, not bandgap choice, dominate beyond five junctions. Polymorphism that goes unnoticed in a commercial powder is precisely the kind of process-control failure mode that stops organic semiconductors reaching reproducible manufacture.

The partial exception is metrology. Contact-free terahertz doping measurement is a drop-in inspection technique for materials already in production, SiC, Si and GaN, and the sensitivity heat maps validated against existing measurements are the kind of output a process engineer can act on. Design tooling for photonic circuits characterised against GaAs-based samples is similarly close to existing industrial materials. Those two lift the score off the floor; the rest of the corpus does not.

**TLDR: Nothing in these sources has left the laboratory, and several papers identify physical barriers that would block scale-up.**

## Impact (3/5)

The largest quantified prize is photovoltaic. Under full concentration, unconstrained bandgap ladders approach 84.5% efficiency at 50 junctions, whereas the conservative TMD bandgap window of 1.0 to 2.1 eV plateaus near 63.4%, with an experimentally achievable five-junction ladder identified at 2.10, 1.78, 1.50, 1.24 and 1.00 eV. That is both the case for the technology and the statement of its ceiling: the accessible gap window costs roughly 21 percentage points against an unconstrained stack. On the switching side, 4 fJ per switching event on picosecond timescales is a meaningful figure of merit for optical interconnect or optical logic if it survives integration.

Beyond those two, impact is mostly enabling rather than direct. Faster Wannier localisation and cheaper hybrid-functional workflows shorten the design loop for anyone doing first-principles materials screening. Symmetry constraints on the effective mass tensor for all 32 crystallographic point groups give a consistency check that catches errors in ab initio calculations. Topological and chiral phenomena such as Chern insulator phases in GdGaI and enantiomer-dependent sign reversal of spin and orbital Hall conductivity in trigonal Se and Te are, on this evidence, physics results without stated applications. A 3 is the honest reading.

**TLDR: The ceilings claimed are large, notably in photovoltaics and low-energy optical switching, but the same sources put hard limits on them.**

## Timing Later (5-10yr)

The corpus splits cleanly. Contact-free terahertz doping characterisation is validated against a variety of existing measurements on materials already in volume production and could be adopted as soon as the sensitivity limits are accepted. Computational tooling, whether faster Wannier function generation or gradient-based optimisation of quantum photonic circuits, diffuses at the speed of code release.

## Overrated or underrated? Too early to say

The concept as a whole cannot be judged from these sources, because none of them touch the semiconductor industry: no fabs, no volumes, no costs, no companies. What can be judged is the beyond-silicon materials frontier they document, and there the position is that the physics is now well enough characterised to be engineering-relevant while the manufacturing question has not been asked. The strongest single result is the MoSe2 nanocavity switch at roughly 4 fJ and picosecond speed; the most commercially useful is probably the least glamorous, a sensitivity framework telling engineers when contact-free terahertz doping measurement will and will not work on SiC, Si and GaN stacks.

## Prediction

By 31 December 2028 no peer-reviewed experimental demonstration will report a transfer-printed five-junction transition metal dichalcogenide photovoltaic stack matching the 2.10, 1.78, 1.50, 1.24, 1.00 eV ladder identified in.

## Evidence base

## Open questions

- Does the ~4 fJ, picosecond all-optical switching seen in a single MoSe2 photonic crystal nanocavity survive integration into a multi-element circuit, and at what insertion loss and repetition rate?
- Can the deterministic dopant segregation and 0.70% strain channels found in vanadium-doped WS2 be controlled to specification across a wafer, or does the kinetic mechanism only reproduce at small flake scale?
- How many other benchmark organic semiconductors have unrecognised stable polymorphs in commercial supply, and does polymorph control change reported mobility rankings?
- Is the 0.55 W/m/K thermal conductivity of close-packed quantum-dot films a hard ceiling set by the dot-solid geometry, or can ligand and matrix engineering raise it enough for continuous-wave operation?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
