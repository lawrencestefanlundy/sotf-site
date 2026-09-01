---
type: concept
slug: simulation
canonical_name: Simulation
aliases:
- computational simulation
- engineering simulation
- CAE
parent_concepts: []
related_concepts:
- physics-ai
- neural-operators
- plasma-simulation
- machine-learning
sources:
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-01-27-ai-for-nuclear-fusion-feat-martin]]'
- '[[2023-05-25-interview-ben-mildenhall-co-inventor]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-11-12-atomic-energy-can-nuclear-power-our]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
scorecard:
  viability: 4
  drivers: 3
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
descendants:
- neural-operators
- physics-ai
- plasma-simulation
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-10-inference-silicon-deep-research
  title: 'Deep research: measured vs claimed inference-silicon economics (adversarially verified, 23/25 claims confirmed)'
  date: '2026-07-10'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-physics-ai-comp-landscape
  title: Physics-AI / ML-surrogate simulation competitive landscape (Zenithon comp set beyond PhysicsX)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-16-cim-landscape-2026
  title: 'Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM'
  date: '2026-06-16'
  kind: web
- slug: 2026-06-16-phasecraft-appointed-by-arpa-e-to-advance-catalyst-simulatio
  title: Phasecraft Appointed by ARPA-E to Advance Catalyst Simulation Frameworks for Hydrogen Electrolysis - Quantum Computing Report
  date: '2026-06-16'
  kind: web
- slug: 2026-06-13-private-fusion-2026-update
  title: Private fusion — 2026 progress update (Helion Polaris D-T, CFS $863M)
  date: '2026-06-13'
  kind: web
neighbors:
- slug: physics-ai
  name: Physics AI
  path: /ai-software/ai-applications/physics-ai/
  macro: ai-software
- slug: neural-operators
  name: Neural Operators
  path: /ai-software/ai-applications/neural-operators/
  macro: ai-software
- slug: plasma-simulation
  name: Plasma Simulation
  path: /ai-software/ai-applications/plasma-simulation/
  macro: ai-software
- slug: machine-learning
  name: Machine Learning
  path: /ai-software/models-inference/machine-learning/
  macro: ai-software
---
**Numerical simulation is the substrate on which most deep-tech engineering claims are now built, and the live questions are not whether it works but how far machine-learned surrogates can replace it, how much of a simulated result survives contact with hardware, and whether quantum or physics-based processors will ever take over the hardest simulation workloads.**

## Summary

"Simulation" here means computing the behaviour of a physical or engineered system from a model rather than measuring it. In practice this covers three quite different things that the sources treat as one continuum. First, classical numerical solvers: finite-element and multi-physics codes that discretise a domain and integrate governing equations. A study of hexagonal boron nitride as a heat spreader for optically heated gold nanospheres used finite-element simulation to quantify how flake thickness, in-plane thermal conductivity and interfacial thermal conductance affect cooling, then checked it experimentally with wavefront-microscopy nanothermometry. A thermomagnetic generator study built a digital twin coupling magnetic, thermal, fluid-flow and electrical domains, argued that three-dimensional treatment is necessary, and validated it against the highest-power-density prototype using only known geometry and material parameters.

Second, surrogates: cheap learned or reduced models trained on simulation output. A Deep Operator Network was trained on physics-based predictions of process-induced deformation in AS4 carbon fibre/epoxy prepreg to predict deformation probabilistically across non-isothermal cure cycles. A two-compartment model of affinity biosensors combining simplified mass transport, Langmuir kinetics and mass conservation reproduced finite-element results with more than a hundredfold reduction in computational time, and yielded closed-form expressions for equilibration time as a function of the Damkohler number.

Third, simulation as the target workload for new hardware. A coalition preprint on physics-based ASICs names materials and molecular simulation alongside AI inference and sampling as the applications that justify relaxing statelessness, unidirectionality, determinism and synchronisation in chip design <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>. Quantum simulation is the same argument in a different technology: nanographene pi-systems are proposed as a scalable bridge problem between early and large-scale fault-tolerant machines, with a tensor-network method for Trotter eigenvalue errors and an observed error-cancellation effect that cuts quantum phase estimation circuit depth by roughly an order of magnitude. A Schrodingerisation-based Hamiltonian simulation of time-domain Maxwell's equations was run on IonQ hardware, recovering signed field directions and agreeing with analytical benchmarks in two dimensions, with three dimensions still on simulators.

The parameters that decide the field are therefore: how tightly a simulation is anchored to measurement, how far a surrogate can be trusted outside its training distribution, and how large the gap remains between simulated and measured performance for whatever the simulation is being used to justify. That last parameter is the one most often left unstated.

## Viability (4/5)

The corpus contains several clean validation loops rather than simulation-only claims. The thermomagnetic generator digital twin was validated against experimental data from the highest-power-density prototype available, using only known geometry and material parameters, and was used to diagnose where energy is lost. The plasmonic heating study paired finite-element predictions with cross-grating wavefront microscopy measurements of temperature around heated nanoparticles. A safe active learning framework for Ga2O3 sensor reliability was first evaluated in simulation and then run on a real automated high-temperature probe station. Surrogate fidelity is also demonstrated rather than asserted: the biosensor two-compartment model reproduces finite-element behaviour at over a hundred times lower cost.

The deduction is for how much spread the error analyses reveal. Trotter error estimates for nanographene simulation vary by orders of magnitude depending on whether worst-case, average-case or eigenvalue errors are used, which means a resource estimate is only as good as its error metric. And the corpus contains at least one prominent case where the headline numbers are simulated only: the 64:64:10 two-layer all-optical InP neural network reports 89.5% best-case MNIST accuracy at 10 GS/s, 47 TMAC/s and 12 pJ/MAC from simulation, not measurement. Simulation is a reliable tool; simulated performance is not the same as demonstrated performance, and the sources show both patterns side by side.

**TLDR: Repeatedly validated against experiment in these sources, but with documented error ranges spanning orders of magnitude.**

## Drivers (3/5)

On supply, three separate accelerants appear. Learned surrogates collapse the cost per evaluation, enabling design-space sweeps and probabilistic prediction that direct solvers cannot afford, as in the DeepONet trained across diverse non-isothermal cure cycles and the analytical biosensor model at over a hundredfold speed-up. Algorithmic improvements reduce quantum resource requirements, with Trotter error cancellation giving about an order of magnitude circuit depth reduction for phase estimation. New hardware paradigms are being proposed explicitly with simulation as a named application, in a paper co-authored across Normal Computing, ARIA and four US academic groups <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>.

On demand, the same physics-based ASIC paper frames a "compute crisis" of unsustainable energy consumption, high training costs and CMOS scaling limits, and lists materials and molecular simulation among the workloads that motivate the shift <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>. Domain pull is visible in the breadth of the corpus itself: composites manufacturing, biosensor design, LEO satellite beamforming, modulation recognition and quantum error decoding all lean on it. What the sources do not provide is any spending, procurement or market-size figure, so the strength of the commercial pull cannot be scored higher than moderate on this evidence.

**TLDR: Clear technical supply-side push and a stated compute-cost demand story, but the sources give no market or spending data.**

## Novelty (3/5)

Judged as a category, simulation is not novel and the sources make no claim that it is. Novelty has to be assessed at the increment. Against direct finite-element solution, the reduced two-compartment biosensor model achieves more than a hundredfold reduction in computational time while still predicting equilibration time and required volume, and additionally yields analytical expressions parameterised by the Damkohler number, which a solver does not give you. Against deterministic physics-based prediction, the DeepONet adds probabilistic output over a set of cure cycles. Against prior simulation practice in its own field, the thermomagnetic generator work argues that earlier two-dimensional or decoupled approaches were inadequate and that full magnetic-thermal-fluid-electrical coupling in three dimensions is required.

On the quantum side the increments are also specific and modest in absolute terms. Trotter error cancellation for energy differences between low-lying eigenstates gives roughly an order of magnitude circuit depth reduction, and the tensor-network approach enables spectral analysis of product formulas beyond brute force. The Maxwell's equations work is described as the first quantum-hardware implementation of this class of Hamiltonian simulation producing signed vector-field solutions, but validated in two dimensions with three dimensions still simulator-only. A hybrid qutrit algorithm for three-flavour supernova neutrinos tracks exact numerical integration only out to t of about 30 inverse omega-zero. These are real firsts on small problems, not displacement of classical simulation.

**TLDR: Simulation itself is old infrastructure; the genuinely new increments are surrogate speed-ups of roughly 100x and quantum-algorithmic depth reductions of roughly 10x.**

## Diffusion (4/5)

Diffusion is effectively complete in research practice. Every domain represented here uses simulation as the primary evidence channel: decentralised satellite beamforming algorithms are evaluated by simulation, sparse array designs for direction-of-arrival estimation likewise, deep-learning modulation recognition reports simulation results for both its architecture and its data augmentation scheme, and quantum error correction work now contributes a decoding simulator as a first-class artefact alongside the decoder and architecture. Simulation is also becoming the safety layer for autonomous experimentation, screened in simulation before being let loose on hardware.

The score is held at 4 rather than 5 because the corpus is a research sample and says almost nothing about industrial deployment, procurement or workflow integration outside the lab. The real adoption barriers are downstream. Surrogates need error bounds before they can substitute for solvers in qualification decisions, and the composites paper positions its DeepONet on top of a physics model validated against manufacturing trials precisely because that anchor is required. Where a simulation is used to justify a hardware roadmap rather than a design choice, adoption of the conclusion outruns the evidence, as with the fully simulated multi-layer all-optical neural network figures.

**TLDR: Already the default method across every domain in this corpus; the barrier is trust and validation, not access.**

## Impact (4/5)

The leverage is visible in how often a simulation output is the actionable result. The hBN work quantifies which of thickness, in-plane conductivity and interfacial conductance actually controls cooling efficiency, which is a materials-selection decision. The thermomagnetic generator digital twin identifies where efficiency is lost in a device class whose two known problems are low efficiency and low cycle frequency, which is a development-priority decision. The biosensor model makes sample volume a first-class design parameter with an analytical prediction of required volume, which changes diagnostics design where sample is scarce. Simulation of composites cure cycles feeds directly into mitigating process-induced deformation.

The same leverage cuts the other way and is part of why impact is high. Whole investment theses rest on simulated numbers: the case that optical compute can beat electronics rests substantially on a simulated 64:64:10 network reporting 47 TMAC/s and under 20 pJ per operation at full system level, and the case for physics-based ASICs rests on argued suitability for simulation and AI workloads rather than measured throughput <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>. A technology that determines both engineering choices and capital allocation is high-impact by construction. The score is not 5 because the sources contain no quantification of economic value, only of computational cost savings.

**TLDR: Simulation is what determines design parameters and what gates investment decisions across the whole corpus, though the sources quantify the value only indirectly.**

## Timing Now (0-2yr)

The classical and surrogate layers are already operational. Validated multi-physics digital twins exist for real prototypes, surrogates trained on validated physics models are being used for probabilistic design prediction, and simulation is already the pre-screen for autonomous experimental campaigns on real hardware. Nothing needs to be invented for this to matter; it already does.

The hardware-acceleration layers are on a much longer clock. Quantum simulation demonstrations here are two-dimensional benchmark problems on trapped-ion hardware with three dimensions still on simulators, hybrid qutrit neutrino simulation matching exact integration only over a limited time window, and nanographene pi-systems being proposed specifically as bridge problems because the gap between hardware capability and requirement for the usual targets remains significant. Physics-based ASICs are at manifesto stage as of July 2025 <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>. Treat those as Later at best on this evidence.

**TLDR: Classical simulation and learned surrogates are in production use today; quantum simulation of useful systems is not close.**

## Overrated or underrated? Fairly rated

Simulation as a capability is correctly valued and correctly ubiquitous. The sources show it doing exactly what it should: producing design parameters, being validated against measurement, and being compressed into cheaper surrogates with quantified speed-ups. There is no bubble here and no neglect either.

The mis-rating is in how simulated results are read. A well-validated digital twin of an existing prototype and a system-level simulation of a chip that has not been built are epistemically very different objects, and both circulate as "results". The nanographene analysis makes the point quantitatively from inside the field: change which Trotter error metric you use and the resource estimate moves by orders of magnitude. The practical discipline for an investor reading this corpus is to ask, for every number, whether the thing being simulated exists. Where it does, the simulation is usually trustworthy. Where it does not, the number is a hypothesis with error bars nobody has stated.

## Prediction

By 31 December 2027, no peer-reviewed measurement of a monolithically integrated multi-layer photonic neural network will match the 89.5% MNIST accuracy at 10 GS/s reported from simulation for the 64:64:10 InP all-optical network.

## Evidence base

- A transient multi-physics digital twin of a thermomagnetic generator, coupling magnetic, thermal, fluid-flow and electrical domains in three dimensions, was validated against experimental data from the highest-power-density prototype using only known geometry and material parameters (4 May 2026).
- A reduced two-compartment biosensor model reproduced finite-element binding kinetics with more than a hundredfold reduction in computational time and yielded analytical expressions for equilibration time and required volume versus Damkohler number (5 May 2026).
- Trotter error cancellation for energy differences between low-lying nanographene eigenstates gave approximately an order of magnitude circuit depth reduction for quantum phase estimation, while worst-case, average-case and eigenvalue Trotter error estimates varied by orders of magnitude (4 May 2026).
- The first quantum-hardware implementation of a Hamiltonian simulation algorithm producing signed vector-field solutions to time-domain Maxwell's equations agreed with analytical benchmarks in two dimensions on an IonQ QPU, with three-dimensional results obtained on simulators (5 May 2026).
- A coalition preprint including an ARIA programme director and four US academic groups named materials and molecular simulation as target applications for physics-based ASICs, framed against unsustainable energy consumption and CMOS scaling limits (14 July 2025) <sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>.
- Headline performance for a two-layer all-optical InP neural network, 89.5% best-case MNIST accuracy at 10 GS/s, 47 TMAC/s and under 20 pJ per operation at full system level, was obtained from simulation rather than measurement (13 January 2022).
- A safe active learning framework for Ga2O3 sensor reliability was first evaluated in simulation, then demonstrated on an automated high-temperature probe station with a Pt/Cr2O3:Mg/beta-Ga2O3 device (5 May 2026).

## Open questions

- Do learned surrogates such as the composites DeepONet carry usable error bounds outside their training distribution of cure cycles, and can they be certified for qualification decisions rather than exploration only?
- Does the Schrodierisation-based Maxwell solver extend from two-dimensional benchmarks on IonQ hardware to three dimensions on hardware, and at what circuit depth and error rate?
- Which Trotter error metric should resource estimates use, given that worst-case, average-case and eigenvalue estimates differ by orders of magnitude for the same nanographene problem?
- Do physics-based ASICs produce any measured speed-up or energy advantage on a materials or molecular simulation benchmark, as opposed to an architectural argument?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
