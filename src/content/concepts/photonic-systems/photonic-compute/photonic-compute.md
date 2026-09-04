---
type: concept
slug: photonic-compute
canonical_name: Photonic Compute
aliases:
- photonic processor
- optical computing
kind: technology
parent_concepts:
- photonic-systems
- photonic-compute
related_concepts: []
sources:
- '[[2025-03-12-project-mayhem-ai-inward-collapse]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2026-07-07-the-asml-killer]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-05-24-mose2-exciton-polariton-all-optical-switch]]'
- '[[2025-07-14-solving-compute-crisis-physics-based-asics]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2023-03-29-oxford-spinout-lumai-secures-11m-grant-to-power-optical-comp]]'
scorecard:
  viability: 2
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: null
  timing_band: Later (5-10yr)
  verdict: Too early to say
scorecard_status: draft
mention_count: 105
descendants:
- diffractive-deep-neural-network
- diffractive-deep-neural-networks
- optical-neural-networks
- photonic-compute
- photonic-compute-memory
- photonic-tensor-cores
sources_7d: 3
sources_30d: 9
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-31-inference-silicon-roster-sprint
  title: 'Inference-silicon roster verification sprint: 10 companies for the competitive-analysis capital map'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-07-the-asml-killer
  title: The ASML Killer?
  date: '2026-07-07'
  kind: substack
- slug: 2026-05-24-mose2-exciton-polariton-all-optical-switch
  title: New light-based switch could cut chip energy use and speed future AI photonics
  date: '2026-05-24'
  kind: web
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2025-07-14-solving-compute-crisis-physics-based-asics
  title: Solving the compute crisis with physics-based ASICs
  date: '2025-07-14'
  kind: web
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
neighbors: []
---
**Photonic compute performs linear algebra by letting light propagate and interfere rather than by switching transistors, and the 2026 literature shows working but small classifiers, real scaling arguments against electronic meshes, and no demonstrated system-level win over digital accelerators.**

## Summary

Photonic compute encodes numbers in the amplitude and phase of light and lets the physics of propagation do the arithmetic. A vector is imprinted on an optical field, the field passes through a structure whose transmission implements a matrix, and photodetectors read out the result. Because propagation is passive and parallel across space and wavelength, the multiply-accumulate itself costs almost no energy and completes in the time light takes to cross the device. Four architectural families appear in the current literature: programmable integrated meshes on silicon photonics, typically Mach-Zehnder interferometer (MZI) networks; free-space diffractive optics, including 2f and 4f lens systems and multi-layer diffractive surfaces; disordered or scattering media used as fixed random projections, read out by a trained linear layer,; and reprogrammable continuous media such as a slab waveguide whose refractive index is modulated across roughly 10^4 spatial degrees of freedom. A fifth, adjacent family uses single photons in mode registers for quantum or quantum-inspired processing,.

The intellectual framing for the whole area is set out in a 2025 coalition preprint on physics-based ASICs, which argues that AI's energy and cost trajectory plus CMOS scaling limits justify chips that are "exact realizations of physical processes", relaxing statelessness, unidirectionality, determinism and synchronisation <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>. The authorship spans Normal Computing, ARIA and four US academic groups, including an ARIA programme director, which makes it a statement of intent for a funded research direction rather than one company's pitch <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>.

The parameters that decide whether any of this becomes useful are unglamorous. First, programmable degrees of freedom per chip and how their count scales with matrix size: conventional MZI meshes need O(N^2) active components, while a multiport-directional-coupler architecture reportedly covers the N-dimensional unitary group with 3N phase shifters and implements an N x N matrix-vector multiply with 7N. Second, loss and crosstalk, which accumulate across cascaded components and cap integration density, and which appear again at the package boundary, where a laser-written interposer routing 40 channels from six multi-core fibres still averages 5.0 dB single-pass insertion loss. Third, memory: photonic processors have no efficient non-volatile weight storage, so weights are held electronically and repeated optical-electrical conversion imposes energy, latency and architectural overheads. Fourth, nonlinearity, which optics does not naturally provide at low power and which current work obtains from detection nonlinearity or coherent interference tricks rather than from nonlinear materials.

Everything demonstrated in these sources is small. Reported results include 94.8% blind-test MNIST accuracy from a volumetric scattering network occupying about 3.8 x 10^-4 mm^3, 93 plus or minus 3% on a two-spiral classification task with event-based readout, and single-pass inference on vectors up to 49 dimensions in a reprogrammable slab. No source in this set reports an end-to-end energy or throughput comparison against a digital accelerator.

## Viability (2/5)

The hardware is real and measured, not simulated: fabricated scattering volumes classifying MNIST at 94.8%, a reprogrammable slab waveguide with about 10^4 spatial degrees of freedom running inference on 49-dimensional vectors in a single pass with no digital pre- or post-processing, an experimentally demonstrated self-configuring processor performing optical singular-value decomposition over spatial and polarisation dimensions, and cloud-accessible photonic processors logging hundreds of thousands of detections. That is genuine engineering maturity at the component level.

What is not demonstrated is a computer. Two gaps are called out in the sources themselves: the absence of efficient, scalable non-volatile photonic memory, described as a fundamental limitation on fully programmable and adaptive photonic systems, and accumulated crosstalk that degrades fidelity as systems scale in complexity. Packaging loss of 3.2 to 5.0 dB per pass is tolerable for interconnect but material for a cascaded compute pipeline. One reported result also flags analogue drift directly: regression performance in a photonic extreme learning machine was sensitive to systematic optical-intensity drift. Score 2 reflects credible early evidence against obstacles that are architectural rather than yield-related.

**TLDR: Devices work and hit their stated benchmarks, but the benchmarks are toy-scale and the missing pieces are structural, not incremental.**

## Drivers (3/5)

On the demand side, the case is the "compute crisis": unsustainable energy consumption, high training costs and CMOS scaling limits, argued as justification for heterogeneous physics-based ASICs by a coalition spanning Normal Computing, ARIA and academic groups at Cornell, Yale, UCSB and UPenn <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>. The presence of a sitting ARIA programme director on that byline indicates public research funding is being steered towards the area <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>. A second demand channel is adjacent rather than AI-specific: optical receivers, where a disordered photonic processor recovers high-dimensional direct-detection symbols in a single shot and reduces receiver complexity, and interconnect densification for datacentres.

On the supply side, the enabling trend visible here is foundry compatibility. Zero-crosstalk operation was demonstrated using standard rib waveguides across silicon-on-insulator and other material platforms without specialised nanostructures, explicitly to remain compatible with standard foundry processes; a self-configuring processor is described as CMOS-compatible; a quantum photonic processor is built on standard CMOS-compatible manufacturing and runs at room temperature. What the sources do not show is any commercial pull: no volumes, no revenue, no customer deployment. Score 3 is capped by that absence.

**TLDR: Demand pull from AI energy costs is asserted by a credible coalition; supply-side progress is steady but comes from research groups, not product lines.**

## Novelty (3/5)

The strongest novelty claims are photonics-versus-photonics and they are specific. Against MZI meshes, whose active component count scales as O(N^2), a cascade of multiport directional couplers with compact phase-shifter arrays is reported to need 3N phase shifters for uniform coverage of the N-dimensional unitary group and 7N for an N x N matrix-vector multiply. Against universal multiport interferometers, wave-optics simulation of 2f and 4f free-space architectures finds many orders of magnitude less optical attenuation per multiply for matrix dimensions above about a thousand. Against planar circuits and discretely spaced diffractive layers, a volumetric scattering network claims a record neuron density of 1.0 x 10^9 per mm^3 while relaxing alignment requirements. And against the assumption that nonlinear optical computing needs nonlinear materials or layer cascades, a single phase-only diffractive plane with co-located encoder and decoder is proved to be a universal approximator for band-limited real-valued nonlinear functions.

Two further contributions widen the design space rather than beating a baseline: engineered non-Hermitian dissipation used as a functional resource to synchronise multimode fields on a silicon processor, and material anisotropy instead of geometric symmetry breaking to obtain quasi-BIC spatial differentiation for optical edge detection, with Q of about 181. The score stops at 3 because the reference point is always another optical scheme. Nothing here quantifies joules per operation or throughput against an electronic accelerator on a task anyone runs in production.

**TLDR: Clear, quantified advantages over other photonic architectures; no quantified advantage over digital accelerators anywhere in the sources.**

## Diffusion (2/5)

Two adoption enablers are visible. First, several groups are deliberately staying inside standard processes: crosstalk cancellation via slab thickness in ordinary rib waveguides across multiple material platforms, and CMOS-compatible, room-temperature photonic quantum processors. Second, remote access already exists: an external team characterised parity-check filters on Quandela's Belenos cloud photonic processor across more than 340,000 detections, and a photonic quantum processor supplied latent samples to a biological generative design pipeline across 131 HLA alleles. That is how a platform starts to acquire users who did not build it.

The barriers are heavier. Without non-volatile photonic memory, weights live in electronics and every reload pays optical-electrical conversion in energy, latency and architecture. Fibre-to-chip coupling at 5.0 dB average insertion loss constrains how many optical stages can be cascaded. Analogue stability is an open operational risk, evidenced by drift sensitivity in regression tasks; self-configuration in situ is one mitigation being explored. The sources say nothing about compilers, model portability, cost or supply chains, so the commercial diffusion path cannot be assessed from this evidence at all. Score 2.

**TLDR: Foundry compatibility and cloud access lower the entry barrier, but weights, loss, drift and toolchain gaps keep this in the lab.**

## Impact (unscored)

The claimed value is large in principle. Encoding computation in light propagation is presented as a route to low-latency, energy-efficient inference,, and the physics-based ASIC manifesto positions such hardware against AI's energy consumption, training costs and CMOS scaling limits, with target applications in diffusion models, sampling, optimisation, inference and molecular simulation <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>. If a photonic matrix-vector engine of useful size worked with digital-comparable accuracy, the addressable workload would be a large fraction of AI inference.

But the sources do not support a score. There is no measured energy per operation, no throughput figure, no comparison against a GPU or an inference ASIC, no cost data, and no benchmark larger than MNIST-class classification or 49-dimensional vectors,. The one head-to-head comparison in this set is narrow and from the quantum branch: a photonic processor reported higher accuracy than classical networks of comparable size on several machine-learning tasks and better noise tolerance than a superconducting processor, which speaks to a different value proposition. Scoring impact from asserted motivation would be scoring the press release, so the score is null.

**TLDR: The prize is asserted, never measured: no source here quantifies the end-to-end gain over digital compute.**

## Timing Later (5-10yr)

Split the technology in two. Narrow, fixed-function optical processing that sits in front of a detector already looks close: optical compressed imaging at 1 micrometre effective resolution with average FSIM of 0.93, metasurface edge detection, and single-shot recovery of high-dimensional symbols at an optical receiver to avoid dimension-by-dimension demultiplexing. These need no weight updates, no cascaded nonlinearity and no compiler, and they exploit foundry-compatible processes.

General programmable photonic compute is further out. The blocking items are named in the sources: non-volatile memory is absent, insertion loss at the package boundary remains multi-dB, and the largest reprogrammable demonstration handles 49-dimensional vectors with about 10^4 spatial degrees of freedom. Favourable scaling arguments exist for both integrated meshes and free-space optics above matrix dimension one thousand, but these are architecture-level claims awaiting experimental confirmation at scale. Five to ten years is the honest band for that transition, and the funding signal implied by ARIA involvement suggests the work will be resourced through it <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>.

**TLDR: Fixed-function optical front-ends could land sooner; programmable photonic compute at useful scale needs memory and loss problems solved first.**

## Overrated or underrated? Too early to say

The physics is not in doubt and the engineering is competent. What is missing is the one measurement that would settle the question: an end-to-end comparison of a photonic processor against a digital accelerator on a workload of commercial size, including the cost of getting data in and out and of holding weights. Not one of the eighteen sources here provides it. Until then, the internal scaling wins are real but self-referential: 3N phase shifters instead of O(N^2) is only interesting if the resulting engine is competitive with silicon logic, and many orders of magnitude less attenuation than a universal multiport interferometer above dimension one thousand is only interesting if such an interferometer was ever going to be the alternative.

Two asymmetries in the evidence are worth acting on. Fixed-function optical front-ends for imaging and optical receivers are being undersold relative to the AI-accelerator narrative: they need no memory, no reprogramming and no nonlinearity, and they already work,. Conversely, the field's own authors identify photonic memory as the fundamental limitation, which means progress there, and not another MNIST record, is the variable to watch. Anyone underwriting photonic compute as a GPU substitute is underwriting an unmeasured claim.

## Prediction

By 31 December 2028, no publicly reported programmable photonic compute chip will have demonstrated single-pass inference on vectors above 1,000 dimensions with on-chip non-volatile weight storage, leaving electronic weight loading and its optical-electrical conversion overhead in place as identified in.

## Evidence base

- July 2025: a coalition preprint from Normal Computing, ARIA and four US academic groups argues that ASICs built around intrinsic physical dynamics can address AI's energy, cost and CMOS scaling limits <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>.
- 14 May 2026: a fabricated volumetric optical scattering network with a volume of about 3.8 x 10^-4 mm^3 and neuron density of 1.0 x 10^9 per mm^3 achieves 94.8% blind-test MNIST accuracy and 1 micrometre effective imaging resolution with average FSIM 0.93.
- 7 March 2026 (announced June 2026): a multiport-directional-coupler optical unitary converter is reported to need only 3N phase shifters, and 7N for an N x N matrix-vector multiply, against O(N^2) for MZI meshes.
- 15 June 2026: a two-dimensional programmable waveguide with about 10^4 programmable spatial degrees of freedom runs neural network inference on up to 49-dimensional vectors in a single pass without digital pre- or post-processing.
- 2 June 2026: a review identifies the absence of efficient, scalable non-volatile photonic memory as a fundamental limitation on fully programmable photonic systems, with electronic memory imposing energy, latency and conversion overheads.
- 24 June 2026: wave-optics simulations find 2f and 4f free-space matrix-vector architectures suffer many orders of magnitude less attenuation than universal multiport interferometers for matrix dimensions above about one thousand.

## Open questions

- What is the measured end-to-end energy per multiply-accumulate, including modulators, detectors, data conversion and electronic weight storage, for any of these architectures at a fixed accuracy?
- Do non-volatile opto-electronic resistive memories reach the endurance, retention and analogue precision needed to hold weights on-chip, and at what cell density?
- Does the 3N phase-shifter scaling of multiport-directional-coupler meshes survive experimentally at large N once crosstalk, fabrication variation and phase drift accumulate,?
- Do interference-based or detection-based nonlinearities support deep, many-layer networks, or do they only work for the shallow tasks demonstrated so far,?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
