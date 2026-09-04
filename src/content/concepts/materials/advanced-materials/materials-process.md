---
type: concept
slug: materials-process
context_concept: true
canonical_name: Materials & Process
aliases: []
kind: technology
parent_concepts:
- materials
- advanced-materials
related_concepts: []
sources: []
frontier:
- Do the fixes for universal-potential failure under melt-quench, pressure-targeted fine-tuning and revised NVT-quench/NPT-equilibration, generalise beyond IrO2, or does each new amorphous system need its own diagnosis 2026 06 16 melt quench failures and practical solutions for universal m?
- Can in-situ diagnostics in epitaxy be extended to predict the metrics RHEED currently misses, notably surface roughness, which correlated only weakly with RHEED embeddings for GaSe 2026 06 15 multi modal machine learning analysis of gase molecular beam?
- Does the closed-loop waveform-discovery result on ferroelectric thin films transfer to processing variables that are slower, costlier and less reversible than a scanning-probe tip bias 2026 06 15 closed loop discovery of out of distribution processing prot?
- Does XRDiff's structure recovery hold on experimental powder patterns with real peak broadening, impurity phases and background, rather than the simulated spectrum-structure pairs it is benchmarked on 2026 06 15 xrdiff crystal structure prediction from powder x ray diffra?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 71
descendants: []
last_reorg_date: '2026-05-13'
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-07-nasas-lunar-development-and-test-facility-prepares-artemis-h
  title: NASA’s Lunar Development and Test Facility Prepares Artemis Hardware for Moon
  date: '2026-08-07'
  kind: web
- slug: 2026-07-31-tb-26-04-webbings-for-use-in-elevated-oxygen-environments
  title: TB 26-04 Webbings for Use in Elevated Oxygen Environments
  date: '2026-07-31'
  kind: web
- slug: 2026-07-08-the-chemistry-of-chips
  title: The Chemistry of Chips
  date: '2026-07-08'
  kind: web
- slug: 2026-07-02-fusion-bionic-secures-8m-for-laser-texturing---opticsorg
  title: Fusion Bionic secures €8M for laser texturing - Optics.org
  date: '2026-07-02'
  kind: web
- slug: 2026-03-25-sallea-extends-salt-based-templating-technology-to-advanced-
  title: Sallea extends salt-based templating technology to advanced composites manufacturing - CompositesWorld
  date: '2026-03-25'
  kind: web
- slug: 2025-12-04-extracting-rare-earth-elements-from-us-wastewaters---univers
  title: Extracting rare earth elements from U.S. wastewaters - University of California
  date: '2025-12-04'
  kind: web
- slug: 2021-05-06-weav3d-awarded-nsf-funding-to-further-develop-next-generatio
  title: WEAV3D awarded NSF funding to further develop next-generation composite forming machine - Design World
  date: '2021-05-06'
  kind: web
- slug: 2017-05-04-making-3-d-printing-as-simple-as-printing-on-paper---mit-new
  title: Making 3-D printing as simple as printing on paper - MIT News
  date: '2017-05-04'
  kind: web
neighbors: []
---
**Materials and Process covers how a material is actually made, and the growing body of work using machine-learned potentials, generative models and closed-loop robotic search to make processing route, not just composition, the designed variable.**

## Summary

A material's properties are set as much by its processing history as by its chemical formula. The same stoichiometry can be an amorphous glass or a dense crystal, a rough film or a single-crystalline one, depending on temperature ramp, flux ratio, quench rate or applied field waveform. "Materials & Process" is the part of materials science that treats those synthesis and processing variables as the object of study: growth windows, nucleation pathways, grain-boundary segregation, pore architecture, network topology in polymers.

The current research front is the attempt to put this domain under computational and automated control. Three layers are visible in recent literature. First, cheap surrogates for quantum mechanics: machine-learned interatomic potentials such as MACE and NequIP now simulate molten lithium carbonate structure and transport at near-ab-initio accuracy, and machine-learned polaron dynamics extends sampling of reduced rutile TiO2(110) from the picoseconds accessible to ab initio molecular dynamics to several nanoseconds. Second, inverse and search tools: diffusion models that recover crystal structure from powder X-ray diffraction patterns, and hybrid solid-state nudged elastic band frameworks that reach the same minimum energy pathways as DFT with up to a 7-fold speedup. Third, closed-loop experiment: evolutionary search over scanning-probe tip-bias waveforms with uncertainty-aware deep kernel learning, validated experimentally on ferroelectric thin films, and open-source software to connect AI planners to heterogeneous lab robots.

Underneath this sits conventional process craft that still delivers most of the demonstrated results: molecular beam epitaxy of Mn2In2Se5 via Mn intercalation into In2Se3, with growth windows of 250-450 degC and Se:Mn flux ratios of 1.1-3.1, yielding 1.5 nm RMS roughness and 0.35 degree rocking-curve FWHM for the MnSe overlayer; parts-per-million cobalt chain-transfer catalyst to lower crosslink density, glass transition and modulus in methacrylate nematic elastomers; carbonisation and pore-closure strategies for hard carbon sodium-ion anodes.

The parameters that decide whether the automated layer displaces the craft layer are: whether surrogate models stay accurate away from their training distribution, whether in-situ diagnostics carry enough signal to close a loop, and whether process knowledge transfers between tools and labs.

## Viability (3/5)

The experimental side is unambiguous. Epitaxial growth windows, intercalation routes and film quality metrics are reported with measured roughness and rocking-curve widths; grain-boundary segregation mechanisms for boron and carbon in Ni-Cr alloys are resolved by hybrid Monte Carlo molecular dynamics; measurement artefacts in spin-orbit torque studies are removed by purpose-built detector stacks, which then attribute the torque in alpha-W to the spin Hall effect and tie its thickness dependence to the beta-to-alpha structural transition above 5 nm. These are working, checkable results.

The computational layer is more contested. Eight leading universal machine-learning interatomic potentials all produced unphysically expanded amorphous IrO2 under a conventional melt-quench protocol, with densities of 1-4 g/cm3 against an ab initio reference of 10.04 g/cm3, and accurate energies and forces alone did not guarantee stable NPT dynamics. Agentic automation of atomistic simulation has to be explicitly engineered to suppress "silent errors", plausible but physically wrong results. At the far end, positionally controlled atom-by-atom donation of carbon and abstraction of silicon has been demonstrated only on a model build site. The honest reading is a field where the tooling is real but its failure modes are still being catalogued.

**TLDR: Conventional process science delivers reproducible results; the machine-learning layer on top works in-distribution and fails visibly outside it.**

## Drivers (4/5)

On supply, the cost curve has moved. Universal machine-learning interatomic potentials offer near-quantum accuracy across chemical spaces at a fraction of ab initio cost, to the point that the stated bottleneck has shifted to human input preparation and analysis. Pretrained models such as EquiformerV2 and eSEN can be dropped into existing pathway calculations. Open-source middleware now exists specifically to decouple AI planners from heterogeneous robotic hardware, shipping with twelve algorithms and demonstrated across six self-driving-lab implementations covering electrolytes, organic synthesis, thin films, fuel-cell process informatics, coffee-ring phase exploration and legacy liquid handling.

**TLDR: Supply of cheap surrogate models and open automation software is rising fast; demand comes from batteries, catalysis and semiconductor films.**

## Novelty (3/5)

The clearest gains are against ab initio baselines. Machine-learned polaron dynamics extends accessible timescales from the picoseconds of ab initio molecular dynamics to several nanoseconds, enough to show that small-polaron mobility at the reduced rutile TiO2(110) surface is suppressed by several orders of magnitude relative to bulk, a result that was previously unreachable. The hybrid SSNEB framework is up to 7 times faster than pure DFT while converging to the same pathways for CsPbI3, GaN and TiO2. XRDiff attacks a genuinely underdetermined inverse problem, structure from powder diffraction with phase information lost, and is benchmarked with all polymorphs of a composition held out together so that success cannot come from memorising the composition.

On the synthesis side the novelty is route-level rather than order-of-magnitude: Mn intercalation as a way to reach a ternary chalcogenide that is awkward to grow directly; field enhancement at pores in nanoporous silica localising femtosecond laser energy to nucleate stishovite sub-nanosecond, faster than in homogeneous silica; ppm-level cobalt chain transfer to soften methacrylate nematic elastomers while preserving nematic order; exploratory chemistry yielding new niobium oxyiodide cluster compounds. Genuinely discontinuous work, mechanosynthetic atom placement, is at the single-model-site demonstration stage.

**TLDR: Real, quantified step changes in simulation throughput and inverse structure solution, but each is a delta on a mature discipline rather than a new capability class.**

## Diffusion (3/5)

The software layer diffuses easily and the sources show active work to lower the barrier: modular AI-robot decoupling via plain CSV exchange, a discrete candidate-pool architecture that absorbs domain knowledge, a unified Python interface, and demonstrated interoperability with an external orchestration system. That such a platform is needed is itself the diagnosis: the bottleneck is bridging diverse algorithms to heterogeneous robotic hardware across labs.

The harder barriers are physical and epistemic. Autonomous synthesis applied to molecular beam epitaxy "remains underdeveloped", and where it has been tried the in-situ signal is only partly informative: unsupervised learning on RHEED patterns separated high- from low-quality GaSe samples and correlated strongly with rocking-curve FWHM, but correlated only weakly with AFM roughness. Trust is the other barrier. Practitioners now have documented evidence that leading universal potentials fail on a standard amorphous-generation protocol and require pressure-targeted fine-tuning or a revised NVT-quench/NPT-equilibration sequence, and that agentic workflows need explicit harnesses against physically incorrect but plausible outputs. Neither kills adoption, but both slow the transition from expert-supervised to unsupervised use. The sources say nothing about industrial deployment or scale-up beyond noting scale gaps from atoms to industrial systems as an open challenge.

**TLDR: Simulation tooling is spreading quickly; closed-loop experimental control is blocked by hardware heterogeneity and thin in-situ signal.**

## Impact (4/5)

The breadth is the argument. The same processing-science toolkit is being applied to fuel-cell and carbon-capture electrolytes, catalytically relevant oxides, sodium-ion anodes where a pore-architecture change targets the ICE versus capacity trade-off directly, superalloy grain boundaries, spintronic heterostructures and switchable adhesives. Anything that compresses the design-synthesise-characterise loop touches all of these.

What the sources do not provide is a quantified downstream economic effect. The reported numbers are internal to the method: a 7-fold pathway-calculation speedup, nanoseconds instead of picoseconds of sampling, a 0.35 degree rocking-curve FWHM. There is one explicitly unaddressed impact channel, environmental performance, where the sources argue that no current generative or active-learning pipeline treats life cycle assessment as an in-loop constraint, blocked by data scarcity, atom-to-system scale gaps, and uncertainty in synthesis pathways. A 4 reflects breadth and demonstrated method-level gains, not a measured product-level return.

**TLDR: Process control is upstream of most energy and electronics materials, so gains here propagate widely, though the sources quantify few end-application deltas.**

## Timing Now (0-2yr)

Machine-learned interatomic potentials, pretrained models plugged into pathway searches, and diffusion-model structure solution are being published as working methods with benchmarks now. Closed-loop experimental protocol discovery has already produced experimentally validated waveform families on ferroelectric thin films, and six distinct self-driving-lab implementations are documented running on shared open software. That is a present capability, not a forecast.

The timeline splits sharply after that. Autonomous molecular beam epitaxy is described as underdeveloped, with in-situ diagnostics that predict some quality metrics and not others, which suggests years of instrumentation work before growth chambers self-optimise. Integrating life cycle assessment into the design loop is framed as an unsolved framework problem. Mechanosynthetic atom-by-atom fabrication, demonstrated for single donation and abstraction events on a clean silicon build site, belongs in a distant band on this evidence.

**TLDR: The simulation and closed-loop tooling is already in working use; the autonomous-synthesis and atom-by-atom ends are much further out.**

## Overrated or underrated? Underrated

The visible narrative in AI-for-materials is composition discovery: generate a stable structure with a desirable property. The sources here point at a different and less-covered constraint. Uncertainty in synthesis pathways is named as one of four fundamental blockers; the same chemistry gives Mn2In2Se5 or rock-salt alpha-MnSe depending on deposition time; torque sign and magnitude in tungsten track a beta-to-alpha phase transition with thickness; hard-carbon performance is set by orientation and closed-pore architecture rather than composition. Treating the processing history itself as the optimisation variable, as the ferroelectric waveform work does, is the more interesting and less crowded move.

The qualifier is that the surrogate models this depends on are not yet trustworthy at the non-equilibrium conditions processing actually involves. A protocol as standard as melt-quench broke all eight universal potentials tested. So the correct reading is that process is the right thing to work on and is under-instrumented, not that it is solved. Anyone marketing autonomous materials process discovery as a finished product is ahead of this evidence.

## Prediction

By 30 June 2028, at least one published benchmark will show a universal machine-learning interatomic potential reproducing melt-quench amorphous IrO2 density within 10% of the 10.04 g/cm3 ab initio reference under a standard NPT protocol without system-specific fine-tuning.

## Evidence base

- 15 June 2026: a hybrid SSNEB framework combining pretrained EquiformerV2 and eSEN with DFT reached up to 7-fold speedup while converging to the same minimum energy pathways as first principles for CsPbI3, GaN and TiO2.
- 16 June 2026: all eight leading universal machine-learning interatomic potentials tested produced amorphous IrO2 densities of 1-4 g/cm3 under conventional melt-quench, against an ab initio reference of 10.04 g/cm3.
- 15 June 2026: machine-learned polaron dynamics reached several nanoseconds of sampling at oxygen-deficient rutile TiO2(110), beyond the picosecond limit of ab initio molecular dynamics, showing small-polaron mobility suppressed by several orders of magnitude versus bulk.
- 15 June 2026: MBE via Mn intercalation produced single-crystalline (0001) Mn2In2Se5 with 1.5 nm RMS roughness over growth windows of 250-450 degC and Se:Mn flux ratios of 1.1-3.1, with extended deposition giving alpha-MnSe(111) up to 8 nm and 0.35 degree rocking-curve FWHM.
- 16 June 2026: the NIMO open-source platform reported a unified interface with twelve AI algorithms driving six self-driving-lab implementations, from electrolyte discovery to fuel-cell process informatics.
- 15 June 2026: positionally controlled mechanosynthetic donation of carbon and abstraction of silicon was demonstrated with inverted-mode STM and functionalised molecular tools on a clean model build site.

## Open questions

- Do the fixes for universal-potential failure under melt-quench, pressure-targeted fine-tuning and revised NVT-quench/NPT-equilibration, generalise beyond IrO2, or does each new amorphous system need its own diagnosis?
- Can in-situ diagnostics in epitaxy be extended to predict the metrics RHEED currently misses, notably surface roughness, which correlated only weakly with RHEED embeddings for GaSe?
- Does the closed-loop waveform-discovery result on ferroelectric thin films transfer to processing variables that are slower, costlier and less reversible than a scanning-probe tip bias?
- Does XRDiff's structure recovery hold on experimental powder patterns with real peak broadening, impurity phases and background, rather than the simulated spectrum-structure pairs it is benchmarked on?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
