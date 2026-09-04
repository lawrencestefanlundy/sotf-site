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
- slug: 2026-09-02-chips-act-20-part-3-can-europe-compete---eenews-europe
  title: 'Chips Act 2.0, Part 3: Can Europe compete? ... - eeNews Europe'
  date: '2026-09-02'
  kind: web
- slug: 2026-09-01-nvidia-earnings-dollars-per-gigawatt-open-and-hugging-face
  title: Nvidia Earnings, Dollars Per Gigawatt, Open and Hugging Face
  date: '2026-09-01'
  kind: web
- slug: 2026-09-01-chinas-ai-rally-is-real-most-global-investors-are-missing-it
  title: China’s AI Rally Is Real. Most Global Investors Are Missing It.
  date: '2026-09-01'
  kind: web
- slug: 2026-09-01-chinas-rare-earths-duopoly
  title: China's Rare Earths Duopoly
  date: '2026-09-01'
  kind: web
- slug: 2026-08-29-us-commerce-department-moves-to-block-china-ai-firms-from-re
  title: U.S. Commerce Department moves to block China AI firms from remote access to advanced chips - 디지털투데이
  date: '2026-08-29'
  kind: web
- slug: 2026-08-28-the-us-is-building-chips-act-fabs-but-neglecting-rd---aolcom
  title: The U.S. Is Building CHIPS Act Fabs but Neglecting R&D - AOL.com
  date: '2026-08-28'
  kind: web
- slug: 2026-08-27-gao-warns-chips-rd-stall-could-cost-us-chip-leadership---iee
  title: GAO Warns CHIPS R&D Stall Could Cost U.S. Chip Leadership - IEEE Spectrum
  date: '2026-08-27'
  kind: web
- slug: 2026-08-27-when-chips-run-short-the-crisis-regime-of-the-chips-act-20--
  title: 'When Chips Run Short: The Crisis Regime of the Chips Act 2.0 - Freshfields'
  date: '2026-08-27'
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

A second theme is control of excitons, the bound electron-hole pairs that dominate optical response in these thin materials. A charge-tunable MoSe2 monolayer coupled to a photonic crystal nanocavity produced all-optical switching of the cavity spectrum at excitation energies down to about 4 fJ on picosecond timescales, with the nonlinearity traced to exciton dephasing breaking the strong-coupling condition. In monolayer WSe2 phototransistors, circularly polarised excitation selects a single valley and produces a two-fold enhancement of sublinear photocurrent scaling, giving all-optical rather than electrical control of many-body exciton interactions.

A third theme is defect and dopant engineering, and the theory and metrology needed to support it. Dopant distribution in 2D semiconductors is usually assumed random, but vanadium in CVD-grown WS2 monolayers segregates along crystallographic bisectors, producing tensile strain channels of about 0.70%. In vacancy-doped 1T-TiS2, half-metallic ferromagnetism only appears once the defect network percolates, at a critical vacancy concentration near 12.5%. On the measurement side, contact-free terahertz time-domain spectroscopy has been given a sensitivity metric that maps which doping levels and layer thicknesses are actually accessible in SiC, Si and GaN stacks.

## Viability (3/5)

There is genuine experimental substance. The MoSe2 nanocavity polariton switch is a measured device with quantified switching energy (~4 fJ) and picosecond response, published in Physical Review Letters. MoS2 layer-dependent gaps were measured in situ by STS on MBE-grown films and cross-checked against DFT and GW. The DNTT polymorph was isolated and its structure resolved by X-ray diffraction, Raman and terahertz spectroscopy. The ScAlN permittivity discrepancy between calculated 11.7 and measured values near 15 is resolved by an analytical model that reproduces experiment across the alloy range. This is a healthy, self-correcting literature.

What is absent is any evidence of scale. Growth is by molecular beam epitaxy or chemical vapour deposition on small substrates; the photovoltaic work is a thermodynamic framework rather than a fabricated stack; and several papers are purely first-principles. A 3 reflects credible laboratory viability of the physics with no demonstrated path, in these sources, to yield, uniformity or wafer scale.

**TLDR: The individual physics results are real, measured and peer-reviewed, but nothing here goes beyond single devices or small samples.**

## Drivers (unscored)

Every supplied source is a research paper on materials physics, device physics or electronic-structure methodology. None reports funding flows, production capacity, customer demand, pricing, policy, or company activity. The only demand-side signal is indirect and qualitative: authors state that TMDs are rising as 2D semiconductors for device applications, that colloidal quantum dots are increasingly replacing bulk semiconductors in electronic and photonic devices, that organic semiconductors are widely explored for flexible optoelectronics, and that reports of large photonic nonlinearities in integrated devices are creating a need for tailored design frameworks.

Those are researchers describing their own field's momentum, not evidence of commercial pull. On the supply side there is nothing on equipment, precursors, substrates or fab economics. A score here would be fabricated, so it is null.

**TLDR: The sources contain no market, demand, capital or supply-chain information at all.**

## Novelty (3/5)

Several results are explicitly better than a stated alternative and by a stated margin. The k-point extension of the co-iterative augmented Hessian method for Pipek-Mezey Wannier functions runs roughly two to three times faster than first-order k-space approaches and orders of magnitude faster than Gamma-point CIAH for 1000 to 5000 orbitals. A tuned hybrid functional reproduces CrSBr optical gaps and exciton-magnetism coupling at substantially lower cost than self-consistent many-body perturbation theory. Terahertz spectroscopy is better than four-point probe and capacitance-voltage measurement in one specific respect, being contact-free, and the new contribution is a sensitivity metric that says where it can be used.

Other novelty claims overturn a working assumption rather than beat a benchmark: dopant distribution in 2D semiconductors is normally assumed stochastic, and the WS2 work shows growth kinetics make it deterministic; DNTT was long considered monomorphic and is not; optical control of exciton-exciton interactions had previously relied on electrical gating or van der Waals engineering, and valley-selective excitation replaces that. The theory side tightens foundations rather than replacing them, proving that band analyticity holds at non-degenerate extrema so that non-analyticity is intrinsically tied to degeneracy. Solid, cumulative, not revolutionary.

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

The device physics is much further out. Monolayer growth is by MBE and CVD at research scale, the multijunction photovoltaic case is a thermodynamic framework awaiting a fabricated stack, and heat removal from quantum-dot films remains an open problem. No supplied source gives a commercialisation date, a yield figure or a pilot line, so the 5 to 10 year band is inferred from the maturity of the demonstrations rather than from any stated roadmap.

**TLDR: Metrology and simulation tooling could land now; the 2D and organic device work has no stated route to product in any source.**

## Overrated or underrated? Too early to say

The concept as a whole cannot be judged from these sources, because none of them touch the semiconductor industry: no fabs, no volumes, no costs, no companies. What can be judged is the beyond-silicon materials frontier they document, and there the position is that the physics is now well enough characterised to be engineering-relevant while the manufacturing question has not been asked. The strongest single result is the MoSe2 nanocavity switch at roughly 4 fJ and picosecond speed; the most commercially useful is probably the least glamorous, a sensitivity framework telling engineers when contact-free terahertz doping measurement will and will not work on SiC, Si and GaN stacks.

Two findings should temper enthusiasm about 2D and organic semiconductors specifically. A benchmark organic semiconductor turned out to have an overlooked, thermodynamically stable polymorph sitting in commercial powder and changing transport dimensionality, and dopants in CVD-grown WS2 segregate systematically rather than randomly. Both mean the field is still discovering that its materials are not what it assumed they were. That is a normal and healthy stage, but it is a long way from a process of record.

## Prediction

By 31 December 2028 no peer-reviewed experimental demonstration will report a transfer-printed five-junction transition metal dichalcogenide photovoltaic stack matching the 2.10, 1.78, 1.50, 1.24, 1.00 eV ladder identified in.

## Evidence base

- All-optical switching of a photonic crystal nanocavity spectrum was demonstrated at excitation energies down to about 4 fJ on picosecond timescales using a charge-tunable MoSe2 monolayer, with the nonlinearity attributed to exciton dephasing breaking strong coupling.
- A conservative TMD bandgap window of 1.0 to 2.1 eV plateaus near 63.4% efficiency at 50 junctions under full concentration against 84.5% for unconstrained ladders, with an achievable five-junction ladder at 2.10, 1.78, 1.50, 1.24 and 1.00 eV.
- Thermal conductivity in an optically pumped CdSe/CdS quantum-dot film was measured at 0.55 W/m/K by sub-nanosecond time-resolved X-ray diffraction, attributed to poor heat flow in close-packed dot solids.
- In vacancy-doped monolayer 1T-TiS2, half-metallicity requires a percolating defect network at a critical vacancy concentration of about 12.5%, above which the majority-spin band widens to 1.5 eV with 100% spin polarisation and a 1.0 eV minority gap.
- The long-standing ScAlN permittivity discrepancy, calculated 11.7 versus measured near 15, is accounted for by inverse piezoelectric lattice inflation under stress-free boundary conditions.
- STS on MBE-grown MoS2 from one to five layers shows the band gap falling with layer number to below the bulk value, with conduction-band pinning disappearing above four layers.

## Open questions

- Does the ~4 fJ, picosecond all-optical switching seen in a single MoSe2 photonic crystal nanocavity survive integration into a multi-element circuit, and at what insertion loss and repetition rate?
- Can the deterministic dopant segregation and 0.70% strain channels found in vanadium-doped WS2 be controlled to specification across a wafer, or does the kinetic mechanism only reproduce at small flake scale?
- How many other benchmark organic semiconductors have unrecognised stable polymorphs in commercial supply, and does polymorph control change reported mobility rankings?
- Is the 0.55 W/m/K thermal conductivity of close-packed quantum-dot films a hard ceiling set by the dot-solid geometry, or can ligand and matrix engineering raise it enough for continuous-wave operation?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
