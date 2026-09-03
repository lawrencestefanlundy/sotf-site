---
type: concept
slug: quantum
canonical_name: Quantum technologies
aliases:
- quantum-technologies
- quantum-tech
- quantum-technology
parent_concepts:
- quantum-computing
- compute
related_concepts:
- quantum-computing
- quantum-sensing
- quantum-error-correction
- photonic-quantum-computing
sources:
- '[[2023-06-15-e04-no10-downing-street-and-vector]]'
- '[[2023-10-19-e20-the-state-of-privacy-enhancing]]'
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2025-01-07-fund-frontier-expeditions-otherwise]]'
- '[[2023-08-18-e11-in-conversation-with-lux-capital]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-01-27-ai-for-nuclear-fusion-feat-martin]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2023-04-04-learnings-from-a-deep-tech-horizon]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2022-12-15-im-doing-research-in-venture-capital]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2025-02-25-data-driven-vc-is-over]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-07-17-the-once-and-future-kimi]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2025-03-05-occupational-downgrading]]'
scorecard:
  viability: 3
  drivers: null
  novelty: 4
  diffusion: 2
  impact: 3
  timing_band: Unclear
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-03-spad-single-photon-market-scan
  title: SPAD / single-photon detector market scan — incumbent structure and company cohort
  date: '2026-08-03'
  kind: web
- slug: 2026-07-24-18b-illinois-chips-act-supports-zero-point-cryogenics-us-ent
  title: $1.8B Illinois Chips Act Supports Zero Point Cryogenics’ U.S. Entry - Quantum Zeitgeist
  date: '2026-07-24'
  kind: web
- slug: 2026-07-21-d-wave-quantum-chips-act-backing-and-nasdaq-shift-fail-to-re
  title: 'D-Wave Quantum: CHIPS Act Backing and Nasdaq Shift Fail to Reverse a Brutal Selloff - Ad-hoc-news.de'
  date: '2026-07-21'
  kind: web
- slug: 2026-07-21-applied-crypto-spinout-sourcing-map
  title: Applied-cryptography academic spinouts in financial infrastructure — sourcing map
  date: '2026-07-21'
  kind: web
- slug: 2026-07-17-the-once-and-future-kimi
  title: The Once and Future Kimi
  date: '2026-07-17'
  kind: substack
- slug: 2026-07-16-when-will-quantum-computing-have-its-breakout-moment---latit
  title: When will quantum computing have its breakout moment? - Latitude Media
  date: '2026-07-16'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
neighbors:
- slug: quantum-computing
  name: Quantum Computing
  path: /compute/quantum-computing/quantum-computing/
  macro: compute
- slug: quantum-sensing
  name: Quantum Sensing
  path: /sensing/quantum-sensing/quantum-sensing/
  macro: sensing
- slug: quantum-error-correction
  name: Quantum Error Correction
  path: /compute/quantum-computing/quantum-error-correction/
  macro: compute
- slug: photonic-quantum-computing
  name: Photonic Quantum Computing
  path: /compute/quantum-computing/photonic-quantum-computing/
  macro: compute
---
**Quantum technologies use controllable quantum states as computational, communication and sensing resources; the sources show sensing and memory hardware already delivering measurable results while the computing part remains at 6-to-10-qubit demonstrations plus simulator-stage error-correction theory.**

## Summary

"Quantum technologies" is not one product but three distinct engineering stacks that share a physics base. **Computing** encodes information in two-level (or multi-level) quantum systems and drives them through interference to solve problems classical machines find hard. The leading solid-state route is superconducting circuits: Josephson junctions embedded in microwave resonators behave as artificial atoms with anharmonic spectra, controlled and read out within circuit quantum electrodynamics, a framework that has underpinned the transmon and fluxonium platforms since the early 2000s. **Communication** moves quantum states between nodes, which requires memories that store a photon and give it back on demand with high efficiency, at telecom wavelength, ideally on a chip <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>. **Sensing and metrology** exploit the fragility of quantum states as a feature: nitrogen-vacancy centres in diamond act as nanoscale magnetometers, and entanglement can be engineered to push measurement precision past classical limits.

The binding constraint on the computing part is decoherence. Physical qubits fail, so useful computation requires quantum error correction: encode one logical qubit across many physical ones, measure syndromes repeatedly, and infer the error in real time. Decoding is a hard classical inference problem in its own right, and existing decoders (clustering, matching, belief propagation, neural networks) each trade accuracy against cost or generality across the main code families, including surface, toric and bivariate bicycle codes; the stated target is fault tolerance on millions of qubits decoded in real time. Theory is now describing decoherence itself as a phase transition in mixed-state topological order, with the loss of protected information classified by anyon condensation at a critical coupling. That is the intellectual frame; the practical question is whether decoders can be built into local hardware at latency.

The parameters that decide each part are different. For computing: physical error rate, decoder accuracy and latency, and the qubit cost of encoding a real problem, which is why work on compact encodings matters (reducing the travelling salesman problem from the O(n²) qubits of one-hot encoding to O(n log n)). For algorithms: whether speedups survive outside structured problem classes; Decoded Quantum Interferometry has strong evidence of a superpolynomial advantage on the optimal polynomial intersection problem, while broad practical optimisation advantage is still described as challenging. For memory: the four-way trade of efficiency, wavelength, temperature and integration, which no single platform currently satisfies <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>. And competitively, quantum is not the only physics-based computing bet: thermodynamic hardware proposes to exploit noise as a resource for AI workloads, positioning itself explicitly against quantum computing with the analogy that thermodynamic chips emulate Langevin's equations as quantum computers emulate Schrödinger's <sup class="ref"><a href="https://arxiv.org/abs/2302.06584" title="Thermodynamic AI and the Fluctuation Frontier" rel="noopener">ref</a></sup>.

## Viability (3/5)

The evidence splits sharply by part. Sensing is working hardware producing new physics: an NV-centre ensemble fabricated directly on a diamond anvil surface imaged the stray field of iron to 30 GPa and resolved the α-ε magnetic transition, a measurement that was previously hard to make. Memory is a credible component technology: an integrated Eu:YSO device reached 80.3(7)% storage-retrieval efficiency for weak coherent pulses and 69.8(1.6)% for telecom-heralded single photons, with 20 temporal modes at 51.3% average efficiency <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>.

Computing is much earlier. On-hardware optimisation results in these sources are tiny: a divide-and-conquer TSP scheme was executed as a two-qubit implementation on SpinQ NMR machines for a five-city instance, with the 4/5/6-city success rates of 100%, 100% and 95.5% coming from numerical simulation; quantum imaginary time evolution for unit-disk maximum independent set was simulated on 6-, 8- and 10-qubit graphs. The Lottery BP decoder claims 2 to 8 orders of magnitude accuracy improvement over belief propagation for topological codes, but that is a decoder plus an architecture plus a simulator, not a result from a running fault-tolerant machine. A 3 reflects real, replicated capability in the non-computing parts and a large unclosed gap in the computing part.

**TLDR: Sensing and memory hardware work now; the computing part is still at single-digit-qubit demonstrations with decoding solved only in simulation.**

## Drivers (unscored)

These sources do not support an assessment of drivers. There is no information here on public or private investment, national programmes, customer demand, supply chains or component availability. The only driver-like statement is a technical requirement pull: scalable decoding is presented as necessary to enable fault tolerance on millions of qubits in real time, which implies that decoder work is being organised around anticipated hardware scale rather than existing hardware.

On the supply side the sources do show a broad and active research base spanning superconducting circuits and hybrid electromechanics, Rydberg tweezer arrays, waveguide QED, rare-earth photonic memories <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup> and enabling materials work such as the UTe2 superconducting memory effect. That indicates healthy scientific supply but says nothing about the economics, so no score is given.

**TLDR: The sources are almost entirely technical papers and contain no funding, market or procurement data.**

## Novelty (4/5)

The comparisons here are unusually explicit. Lottery BP is measured against belief propagation, the incumbent scalable decoder, and reports 2 to 8 orders of magnitude better decoding accuracy for topological codes, plus syndrome voting that compresses multiple measurement rounds into one to increase latency margin and mitigate the decoding backlog problem. On encodings, the compact binary register cuts TSP qubit requirements from O(n²) to O(n log n) versus standard one-hot encoding. On algorithms, Decoded Quantum Interferometry has strong evidence of superpolynomial speedup over the best classical methods for approximate solutions to the optimal polynomial intersection problem, which is a genuine, if narrow, claim of advantage.

The memory result is better characterised as closing a gap than opening one: cold-atom (~90%) and warm-vapour (~82%) memories still win raw efficiency, but only at near-infrared wavelengths (Rb ~795 nm) and as bulk free-space systems, whereas the Eu:YSO device delivers 80.3% while being chip-integrated and telecom-relevant <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>. Elsewhere the novelty is capability-first rather than benchmarked: room-temperature on-chip magnetic levitation of a nanogram ferromagnetic microsphere with librational modes above 10 kHz, explicitly overcoming the low eigenfrequencies, bulky coils and cryogenic requirement of diamagnetic and Meissner approaches, and squeezing in qudit rather than qubit systems with quantum Fisher information reaching F_Q ∝ N².

**TLDR: Several sources quantify the margin over the incumbent method, from 2-8 orders of magnitude in decoding accuracy to record integrated-memory efficiency.**

## Diffusion (2/5)

The barriers are stated in the sources themselves. The memory work names the four-way filter for a manufacturable network component (efficiency, telecom wavelength, near-room-temperature operation, integration) and states plainly that no single platform yet holds all four together: Eu:YSO is cryogenic, the higher-efficiency cold-atom and warm-vapour systems are near-IR and free-space <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>. In computing, decoding must be accurate, fast, general and scalable simultaneously across code families, and the proposed answer requires a dedicated architecture to implement the decoder locally, meaning new silicon rather than software rollout.

Problem sizes reachable on real machines are the other barrier: five-city TSP via a two-qubit hardware implementation with classical post-processing, framed as a way to study small instances on resource-constrained devices, and 6-to-10-qubit MIS simulations. The nearest thing to a diffusing product in these sources is diamond quantum sensing, which is already being applied as a measurement tool inside another experimental apparatus. The sources contain no data on commercial deployments, standards or user counts, so the score rests on stated technical barriers alone.

**TLDR: Cryogenics, wavelength mismatch, qubit budgets and unbuilt decoder hardware all sit between these results and any deployed system.**

## Impact (3/5)

The upside case has partial support. On optimisation, the only clean advantage claim is on a structured instance: superpolynomial speedup evidence for optimal polynomial intersection within the max-LINSAT class, with the same review conceding that a clear and scalable advantage on broadly useful practical optimisation remains challenging. That is enough to justify continued investment and not enough to underwrite a general-purpose compute market. If decoders such as Lottery BP do generalise across surface, toric and bivariate bicycle codes at millions of qubits, the impact would be enabling for everything above them.

The demonstrated impact today is in measurement and networking. Diamond sensing extended magnetometry into a pressure regime where techniques were limited, resolving a magnetic transition in iron at up to 30 GPa; multimode storage at 20 temporal modes is explicitly repeater-relevant, the missing component for long-distance quantum networks <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>. Against that, quantum is not the only claimant on physics-based computing: thermodynamic hardware targets generative diffusion models, Bayesian neural networks, Monte Carlo sampling and annealing natively, which would erode part of the sampling and optimisation case for quantum machines if it works <sup class="ref"><a href="https://arxiv.org/abs/2302.06584" title="Thermodynamic AI and the Fluctuation Frontier" rel="noopener">ref</a></sup>.

**TLDR: Large if fault tolerance and repeater-grade memory land, but the sources evidence advantage only on structured problems and on measurement.**

## Timing Unclear

The three parts are on different clocks and only one has evidence that pins a date. Diamond quantum sensing is producing results in published experiments today, and integrated telecom-relevant memory is at record component-level performance with a clearly named remaining gap (cryogenics) <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>. Those read as Now and Soon respectively.

For computing, the sources supply no schedule. Fault tolerance on millions of qubits is stated as the motivating target, not as a dated expectation, and the decoder that would serve it exists as an algorithm, an architecture proposal and a simulator. The hardware results present are single-digit-qubit. Assigning a band to the field as a whole would be inventing a roadmap the sources do not contain, so the honest answer is Unclear, with the caveat that nothing here suggests a compute payoff inside two years.

**TLDR: Sensing delivers now, memory components are close, and the sources give no dated roadmap at all for fault-tolerant computing.**

## Overrated or underrated? Fairly rated

Taken as a whole the field is roughly correctly valued, but the internal weighting looks wrong. The compute part absorbs most of the attention while, in this evidence base, it consists of theory and simulation (decoders improving accuracy by 2 to 8 orders of magnitude in software, one structured problem with superpolynomial speedup evidence) sitting above hardware executions of five-city TSP on two qubits. That is a healthy research pipeline, not a near-term compute industry.

The sensing and memory parts are the underrated part. NV magnetometry is already an instrument that answers questions other techniques could not reach, and integrated rare-earth memory is converging on the specification a real network component needs, with only the temperature axis clearly unsolved <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>. Investors treating "quantum" as a single bet on gate-model computing are mispricing the parts of the stack that already ship measurable performance. The competitive risk to the compute thesis from adjacent physics-based computing, such as thermodynamic hardware aimed at the same sampling and optimisation workloads, should also be priced in <sup class="ref"><a href="https://arxiv.org/abs/2302.06584" title="Thermodynamic AI and the Fluctuation Frontier" rel="noopener">ref</a></sup>.

## Prediction

By 31 December 2027 no peer-reviewed demonstration will report a single quantum memory platform simultaneously achieving above 80% storage-retrieval efficiency, telecom-wavelength operation, chip integration and non-cryogenic operation, the four-way combination identified as unmet as of November 2025 <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>.

## Evidence base

- 4 May 2026: Lottery BP reports 2-8 orders of magnitude decoding accuracy improvement over belief propagation for topological codes, with syndrome voting to mitigate the decoding backlog, targeting fault tolerance on millions of qubits in real time.
- 8 November 2025: integrated Eu:YSO quantum memory achieves 80.3(7)% storage-retrieval efficiency, 69.8(1.6)% for telecom-heralded single photons and 20 temporal modes at 51.3% average efficiency, but requires cryogenic operation; cold-atom (~90%) and warm-vapour (~82%) rivals are more efficient yet near-IR and free-space <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>.
- 4 May 2026: NV-centre ensembles fabricated on a diamond anvil surface image iron's stray magnetic field up to 30 GPa and resolve the α-ε magnetic transition.
- 4 May 2026: a compact-encoding variational TSP framework reduces data qubits from O(n²) to O(n log n) and reports simulated success rates of 100%, 100% and 95.5% for 4, 5 and 6 cities, with hardware validation only as a two-qubit implementation on SpinQ NMR machines.
- 4 May 2026: a review of Decoded Quantum Interferometry states strong evidence of superpolynomial speedup on the optimal polynomial intersection problem while noting that clear, scalable advantage on broadly useful practical optimisation remains challenging.
- 4 May 2026: room-temperature on-chip magnetic levitation of a 6.5 µm-radius ferromagnetic microsphere with librational eigenfrequencies above 10 kHz, avoiding the cryogenic requirement of Meissner levitation.

## Open questions

- Does the 2-8 orders of magnitude accuracy gain of Lottery BP survive implementation in the PolyQec architecture at real-time latency on live syndrome data, rather than in simulation?
- Does the DQI superpolynomial speedup extend beyond structured instances such as optimal polynomial intersection to problems with commercial demand, or does it stay confined to the max-LINSAT class?
- Can rare-earth integrated memories retain ~80% efficiency and telecom operation while relaxing the cryogenic requirement, or does the four-way trade force hybrid architectures <sup class="ref"><a href="https://arxiv.org/abs/2511.05928" title="Efficient integrated quantum memory for light (¹⁵¹Eu³⁺:Y₂SiO₅, AFC, telecom-heralded)" rel="noopener">ref</a></sup>?
- Do compact encodings such as O(n log n) TSP registers combined with divide-and-conquer execution scale past toy instances on hardware, or does the classical post-processing dominate the result?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
