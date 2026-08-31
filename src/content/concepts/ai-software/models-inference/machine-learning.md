---
type: concept
slug: machine-learning
canonical_name: Machine Learning
aliases:
- ML
- deep learning
- neural networks
parent_concepts: []
related_concepts:
- physics-ai
- neural-operators
- simulation
- plasma-simulation
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2023-06-15-e04-no10-downing-street-and-vector]]'
- '[[2023-09-18-e15-in-conversation-with-wisear-on]]'
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2023-05-20-interview-jordan-brandt-ceo-of-inpher]]'
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2021-07-21-why-privacy-tech-is-actually-collaborative]]'
- '[[2023-08-18-e11-in-conversation-with-lux-capital]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2023-06-30-e06-the-model-t-moment-for-bits-llms]]'
- '[[2023-05-25-interview-ben-mildenhall-co-inventor]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2022-12-15-im-doing-research-in-venture-capital]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2023-05-31-three-underrated-technologies-from]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2023-07-06-e07-decentralised-ai]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2023-05-05-interview-rick-hao-partner-at-speedinvest]]'
scorecard:
  viability: 5
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-06-willdepue-stargate-for-data
  title: A Stargate for Data — will depue (OpenAI) on >$100B/year data spend by 2030
  date: '2026-07-06'
  kind: web
- slug: 2025-08-04-google-expands-demand-response-to-target-machine-learning-wo
  title: Google expands demand response to target machine learning workloads - Latitude Media
  date: '2025-08-04'
  kind: web
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
- slug: 2024-12-16-willow-and-the-race-to-quantum-advantage
  title: Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)
  date: '2024-12-16'
  kind: substack
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
- slug: 2024-11-05-confidential-ai-the-dog-that-didnt
  title: Confidential AI
  date: '2024-11-05'
  kind: substack
- slug: 2023-11-20-e21-can-we-make-enough-ai-chips
  title: Can we make enough AI chips?
  date: '2023-11-20'
  kind: substack
neighbors:
- slug: physics-ai
  name: Physics AI
  path: /ai-software/ai-applications/physics-ai/
  macro: ai-software
- slug: neural-operators
  name: Neural Operators
  path: /ai-software/ai-applications/neural-operators/
  macro: ai-software
- slug: simulation
  name: Simulation
  path: /ai-software/ai-applications/simulation/
  macro: ai-software
- slug: plasma-simulation
  name: Plasma Simulation
  path: /ai-software/ai-applications/plasma-simulation/
  macro: ai-software
---
**Machine learning is the practice of fitting parameterised models to data rather than hand-coding rules, and by 2026 it has become the default computational method across materials science, quantum error correction, wireless systems and imaging, with the open questions now about data economics, verification and where the arithmetic physically runs.**

## Summary

Machine learning (ML) replaces explicitly programmed rules with a parameterised function whose parameters are fitted to data. The family covers supervised learning (fit a labelled input-output map, as in the 1D convolutional network trained to detect RF jamming from IQ samples), unsupervised learning (find structure without labels, as in the PCA plus K-means framework used to characterise die-to-die variability in ferroelectric HfZrO capacitors and predict the behaviour of unseen dies), and large-scale self-supervised pretraining, where a single model is trained on a broad corpus and then adapted to many downstream tasks. WiFo-2, pretrained on 11.6 billion channel state information points, is the wireless instance: it shows scaling-law behaviour, performs zero-shot channel reconstruction better than fully supervised task-specific models, and reaches state-of-the-art results on nine tasks using 1% of the training samples supervised models need.

Three things decide whether an ML model works on a given problem. The first is the hypothesis class and its inductive bias: neural networks, kernel machines and Gaussian processes each encode different assumptions, and injecting known physics sharpens them. A tensorial kernel support vector machine, an interpretable unsupervised method, identified string order in symmetry-protected topological phases directly from trapped-ion experimental data; symmetry-equivariant quantum circuit ansaetze built by twirling encode finite-group and Lie-group symmetries of a PDE as a bias; and quantum Gaussian processes use a physics-informed prior over unknown quantum transformations.

The second is data. Training sets are expensive to produce, and the emerging finding is that much of the cost is wasted: electronic structure datasets generated by Kohn-Sham DFT contain large redundancies attributable to low intrinsic dimensionality, so even random pruning barely degrades accuracy, and coverage-based pruning preserves chemical accuracy while using up to two orders of magnitude less data and cutting training time by a factor of three or more. Where raw data cannot be pooled at all, federated learning trains a shared model across devices without moving the data.

The third is where the arithmetic runs. Digital electronics is the incumbent, but the same mathematics has been mapped onto other physical substrates: passive diffractive layers that compute at the speed of light with no power beyond the illumination, multiple scattering through modulation planes that synthesises both linear and nonlinear transforms at milliwatt continuous-wave power, InP photonic integrated neurons projected at 47 TMAC/s and 12 pJ/MAC, and thermodynamic hardware that treats noise as a computational resource for diffusion models, Bayesian networks and Monte Carlo sampling <sup class="ref"><a href="https://arxiv.org/abs/2302.06584" title="Thermodynamic AI and the Fluctuation Frontier" rel="noopener">ref</a></sup>. Substrate choice does not change what ML is; it changes the energy and latency at which it can be deployed.

## Viability (5/5)

The evidence base is not a single benchmark but repeated independent demonstrations in fields that share nothing except the method. A federated 1DCNN reaches 97% accuracy and 97% F1 on RF jamming detection while beating centralised MLP, 1DCNN, SVM and logistic regression baselines. A DFT-accurate machine learning force field drives large-scale molecular dynamics that resolves twin-domain structure in formamidinium lead iodide across mesoscopic length scales and below roughly 100 K. A learned fast-forward operator, trained on diverse ptychographic datasets and validated on experimental data taken in a different year, reduces the iterations needed for convergence while preserving the physical consistency of the underlying solver. These are working systems on real data, not proofs of concept.

Two qualifications keep this from being a blank cheque. Quantum machine learning is explicitly described by practitioners as a field that is 'in many ways stuck', lacking learning frameworks that are simultaneously simple, interpretable and scalable, and it has attracted parallel work on certified training and mutation testing precisely because correctness cannot yet be assumed. And ML does not automatically win: in quantum error decoding, neural network decoders are grouped with clustering, matching and belief propagation as suffering from inaccuracy, cost or incompatibility, and the improvement of 2 to 8 orders of magnitude for topological codes comes from a randomised belief-propagation variant rather than from a learned model.

**TLDR: Demonstrated, quantified results across unrelated domains, with quantum ML the clear exception.**

## Drivers (4/5)

On the demand side, the sources describe pull from several directions at once. Semiconductor manufacturing cites a 'skyrocketing' AI workload driving exponential growth in demand for non-volatile and computational memory. Fault-tolerant quantum computing needs real-time decoding across millions of qubits, a hard latency and throughput requirement. Sixth-generation wireless is becoming heterogeneous enough that per-configuration supervised models no longer generalise, which is the explicit motivation for a generalist foundation model. Materials discovery is pulling ML into database expansion and catalyst screening, with 228 dual-atom candidate structures narrowed to 24 highly active ones by a combined first-principles and ML pipeline.

On the supply side, the binding constraints named in the sources are the cost of generating training data (expensive Kohn-Sham DFT calculations), the legal or privacy inability to pool it, and energy per operation. Each has an active answer: coverage-based pruning cuts the data requirement by up to two orders of magnitude, federated averaging removes the need to share raw samples, and alternative substrates target the energy term, with a full-system photonic figure below 20 pJ/op once synapses per neuron exceed 18, itself around six times the optical-engine-only number. The sources do not quantify capital flows or market size, so this score rests on technical demand signals only.

**TLDR: Demand is broad and stated; supply constraints are shifting from raw data volume to data curation and energy per operation.**

## Novelty (3/5)

As a category, machine learning is mature and in most of these papers it is the baseline that something else has to beat. What the sources do quantify is the delta over the non-learned alternative in each niche. Against task-specific supervised models, a pretrained wireless foundation model wins zero-shot and matches state of the art with 1% of the samples. Against centralised classical baselines including SVM and logistic regression, a federated CNN reaches 97% accuracy while keeping data local. Against conventional iterative ptychographic solvers, an ML-augmented operator converges in fewer iterations on real experimental data. Against brute-force DFT sampling, ML force fields extend molecular dynamics to mesoscopic scales at DFT accuracy.

The genuinely new material is elsewhere: in how much data ML actually needs (the low intrinsic dimensionality result reframes dataset construction as an over-provisioning problem), in substrates that change the cost function (diffractive layers computing at the speed of light with no power beyond illumination; nonlinearity synthesised from linear optics at milliwatt power; thermodynamic hardware that runs sampling workloads natively by treating noise as a resource <sup class="ref"><a href="https://arxiv.org/abs/2302.06584" title="Thermodynamic AI and the Fluctuation Frontier" rel="noopener">ref</a></sup>), and in verification methods borrowed into new domains. Where ML competes head-on with a well-tuned classical algorithm it can lose, as in topological-code decoding.

**TLDR: ML is now the incumbent, not the novelty; the measurable deltas are large but sit in specific couplings to physics, data and hardware.**

## Diffusion (4/5)

Diffusion within technical practice is close to complete: in the sources, ML appears as a standard tool in condensed matter, catalysis, semiconductor metrology, coherent imaging, wireless signal processing and quantum information, and in several cases it is used without argument as to whether ML is appropriate. There is also evidence of movement beyond simulation: WiFo-2 is accompanied by a functional hardware prototype demonstrating real-world deployability across diverse wireless tasks, and unsupervised variability analysis is framed against the practical problem of high-volume manufacturing yield.

The barriers named in the sources are specific. Data cannot always be centralised, for privacy reasons on user equipment or cost reasons where each sample is a DFT calculation. Models trained for one system setting generalise poorly to others, which is the stated failure mode of existing deep learning in wireless design. Assurance is immature: certified training under adversarial perturbation is only now being extended to quantum models via interval bound propagation, and mutation testing for quantum neural networks is being defined from scratch. For safety-critical or regulated deployment those gaps, not model quality, are the rate limiter. The sources say nothing about commercial procurement, skills or regulation, so this score reflects technical diffusion only.

**TLDR: Already diffused through research practice; the remaining barriers are data access, generalisation and the absence of mature verification.**

## Impact (4/5)

The impact visible here is compression of expensive processes. Two orders of magnitude less training data and a threefold cut in training time for electronic structure models directly reduce the DFT compute bill for materials ML. A screening pipeline that reduces a 228-structure library to 24 high-activity bifunctional water-splitting candidates converts a synthesis problem into a shortlist. Predicting the performance of unseen dies from data on other dies attacks a barrier explicitly called formidable in high-volume semiconductor manufacturing. Reaching state-of-the-art on nine wireless tasks with 1% of the supervised sample budget changes the economics of deploying learned components in networks.

On the hardware side the potential multiplier is energy: the InP photonic analysis reports 47 TMAC/s, roughly 2.5 times a then-state-of-the-art GPU, and 12 pJ/MAC, roughly twice better, with a full-system figure below 20 pJ/op. That is a simulated two-layer network on MNIST at 89.5% accuracy, so it bounds the promise rather than proving it. No source in this set quantifies revenue, cost savings in currency, or macroeconomic effect, so the score is a judgement about technical leverage, not measured value capture.

**TLDR: Large, measured multipliers on scientific and engineering throughput; the sources do not price them.**

## Timing Now (0-2yr)

Nothing here is waiting on a breakthrough. The classical results are on experimental data and, in the wireless case, on a hardware prototype. Dataset pruning, ML force fields, learned reconstruction operators and unsupervised variability analysis are all deployable techniques today.

The adjacent items sit further out. Alternative substrates remain at component and simulation stage: the photonic multi-layer network result is a simulated 64:64:10 network reaching 89.5% on MNIST, and the diffractive and multiple-scattering approaches are physics demonstrations rather than products. Quantum machine learning, by its own practitioners' framing, is not near application. Treat the core method as Now and its exotic substrates as a separate, later question.

**TLDR: ML is already the working method; the live 0-2 year questions are data efficiency and verification, not feasibility.**

## Overrated or underrated? Fairly rated

As a general capability, ML is neither under- nor over-valued in this evidence base: it is simply the default, and it earns that position with quantified wins across unrelated fields. The useful position to take is about where the remaining margin sits. It is no longer principally in model architecture. It is in data economics, where the finding that electronic structure datasets are massively redundant because the underlying data lies on a low-dimensional non-linear manifold implies that a large fraction of current training spend in scientific ML is buying nothing; and in inductive bias, where pretraining on heterogeneous data or encoding known symmetries buys order-of-magnitude sample efficiency.

Two corrections to the consensus follow. First, ML is not automatically the best answer even in data-rich, pattern-heavy problems: neural network decoders are listed among the inadequate options for quantum error correction, and the large accuracy gain came from a randomised classical algorithm. Second, the assurance layer lags badly. Certified training and mutation testing are still being defined for newer model classes, which is a real obstacle to deployment anywhere a wrong answer is expensive. Anyone valuing ML on capability alone, without discounting for verification and data-access costs, is over-paying.

## Prediction

By 31 December 2028, no quantum machine learning method will have been demonstrated to beat a strong classical ML baseline on a classical dataset of practical size, leaving demonstrated QML value confined to learning on quantum data and quantum processes.

## Evidence base

- 2026-05-05: WiFo-2, pretrained on 11.6 billion CSI points, shows scaling-law behaviour, beats fully supervised task-specific models at zero-shot channel reconstruction, and reaches state of the art on nine wireless tasks with 1% of the supervised training samples, with a functional hardware prototype.
- 2026-05-04: Coverage-based pruning of electronic structure datasets preserves chemical accuracy and generalisability while using up to two orders of magnitude less data and cutting training time by a factor of three or more, explained by the low intrinsic dimensionality of the data.
- 2026-05-05: A federated 1DCNN trained on over-the-air IQ samples achieves 97% accuracy and 97% F1 for 5G RF jamming detection, outperforming centralised MLP, 1DCNN, SVM and logistic regression baselines without sharing raw data.
- 2026-05-04: In quantum error decoding, neural network decoders are grouped with clustering, matching and belief propagation as inadequate, and a randomised belief-propagation variant delivers a 2 to 8 order-of-magnitude accuracy gain for topological codes.
- 2022-01-13: A simulated 64:64:10 all-optical InP neural network reaches 89.5% best-case MNIST accuracy at 10 GS/s, with 47 TMAC/s (about 2.5x a then-state-of-the-art GPU), 12 pJ/MAC (about 2x better) and full-system energy below 20 pJ/op above 18 synapses per neuron.
- 2026-05-04: Quantum machine learning is described by its own practitioners as 'in many ways stuck', with quantum Gaussian processes proposed to supply a simple, interpretable and scalable framework for learning on quantum data.

## Open questions

- Does the low intrinsic dimensionality finding generalise beyond electronic structure data, or are the two-orders-of-magnitude pruning ratios specific to DFT-generated datasets?
- Does the scaling-law behaviour reported for a wireless foundation model hold when the pretraining corpus is broadened beyond 11.6 billion CSI points, and does the zero-shot advantage survive on hardware in the field rather than on a prototype?
- Can any alternative substrate move from simulated multi-layer networks and MNIST-scale tasks to a fabricated system that holds the claimed 12 pJ/MAC and 47 TMAC/s at useful model sizes?
- Will certified-training and mutation-testing methods mature fast enough to let learned components enter safety-critical or regulated loops, or will hand-verified classical algorithms keep winning those slots as they did in topological-code decoding?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
