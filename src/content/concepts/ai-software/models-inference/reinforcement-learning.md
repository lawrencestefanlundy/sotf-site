---
type: concept
slug: reinforcement-learning
canonical_name: Reinforcement Learning
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-01-27-ai-for-nuclear-fusion-feat-martin]]'
- '[[2023-06-30-e06-the-model-t-moment-for-bits-llms]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2022-12-15-im-doing-research-in-venture-capital]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
scorecard:
  viability: 3
  drivers: 3
  novelty: 4
  diffusion: 2
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 117
sources_7d: 6
sources_30d: 20
recent_mentions:
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
- slug: 2025-01-27-ai-for-nuclear-fusion-feat-martin
  title: AI for Nuclear Fusion (Feat. Martin Riedmiller, Google DeepMind)
  date: '2025-01-27'
  kind: substack
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2023-08-31-e13-chiplets-how-chip-lego-is-driving
  title: '🔮 E13: Chiplets - How Chip Lego is Driving AI Progress'
  date: '2023-08-31'
  kind: substack
- slug: 2023-06-30-e06-the-model-t-moment-for-bits-llms
  title: '🔮 E06: Large Language Models and the Assembly Line'
  date: '2023-06-30'
  kind: substack
- slug: 2022-12-15-im-doing-research-in-venture-capital
  title: 🔮 I’m doing research in venture capital, AMA
  date: '2022-12-15'
  kind: substack
neighbors: []
---
**Reinforcement learning is a family of methods that learn a decision policy by trial and reward rather than from labelled examples, and across the 2026 literature it is being used less as an AI research topic in itself and more as a general-purpose replacement for hand-written heuristics in wireless precoding, quantum compilation, materials search and hardware parameter tuning.**

## Summary

Reinforcement learning (RL) trains a *policy*: a function that maps an observed state to an action, optimised to maximise a cumulative reward signal. Unlike supervised learning there is no ground-truth label for each input; the learner must explore, observe consequences, and attribute credit backwards through a sequence of decisions. The two dominant families are value-based methods, which learn the expected return of state-action pairs and act greedily (Deep Q-Networks), and policy-gradient methods, which parameterise the policy directly and adjust it along the gradient of expected reward (Proximal Policy Optimization, twin delayed deep deterministic policy gradient, normalised advantage functions). Both appear repeatedly in the sources, sometimes compared head to head within one problem.

What makes RL attractive to engineers is structural, not cognitive. Many design problems are non-convex, sequential and state-dependent, so classical optimisation either does not apply or must be re-solved from scratch for every instance. RL instead amortises the cost: you pay once to train a policy in a simulator, then get near-instant decisions that generalise across instances. That framing recurs almost verbatim across unrelated fields. Cell-free massive MIMO precoding in O-RAN is formulated as a nonconvex throughput-maximisation problem and handed to multi-agent deep RL because centralised solutions do not scale and fully distributed ones cause interference. Continuous power allocation in an optical wireless NOMA system is described as "computationally prohibitive" to optimise dynamically, so a deep RL agent learns it instead. Quantum circuit compilation is cast as combinatorial optimisation and solved by a trained policy rather than a heuristic pass.

The parameters that decide whether it works are consistent across these papers. First, simulator fidelity: the policy is only as good as the environment it was trained in, and one source explicitly studies behaviour under domain shift. Second, action-space design, which one paper elevates to the central contribution, showing that reformulating the action space plus action masking materially changes achievable performance on the same underlying task. Third, sample efficiency and reward shaping: a quantum error-correction paper uses curriculum learning plus an analytical master-equation solution specifically to accelerate training, and a molecular agent replaces per-step energy rewards with energy- and validity-based rewards over multiple compositions to get generalisation. Fourth, inference-time cost, which becomes a hard constraint when the policy sits inside a real control loop.

A separate thread worth flagging: a 2025 theory paper argues that transformer attention is the exact solution to a degenerate one-sided entropic optimal transport problem, and that its backward pass yields gradients mathematically identical to advantage-based policy gradients from RL. The same source cautions that the claim is narrower than a general attention-optimal-transport equivalence and has been mis-cited elsewhere. If it holds, it is a statement about why the two learning paradigms share machinery, not an engineering result.

## Viability (3/5)

The volume and consistency of positive results is the strongest evidence here. Independent groups in signal processing, quantum information and materials science report RL policies beating the incumbent method on their own problem, with numbers: 65-85% reduction in SWAP overhead versus existing quantum compilers on MQTBench and Queko circuits, a 14-25% increase in median secure key rate and QBER falling from 3.0% to 1.5% for a PPO-based QKD tuner, up to an order of magnitude more valid isomers on unseen formulas than single-composition RL baselines, and a discovered bosonic code surpassing the AQEC breakeven point. RL as a training method is clearly not in question.

What is in question is everything past the simulator. The wireless papers report simulation results; the emitter-localisation work is evaluated on a simulated setup and treats domain shift as an open behaviour to study. The one source that pushes to physical hardware finds exactly the problems you would expect: hardware latency, noise susceptibility and convergence, with balancing stability strongly dependent on both inference control frequency and measurement shot count. A 3 is the honest reading: the method demonstrably solves the posed problems, and the sources do not show it solving the deployed versions of those problems.

**TLDR: Works reliably in simulation across many domains; almost nothing in the sources is a deployed system.**

## Drivers (3/5)

On demand, the pull is well documented and specific. 6G and O-RAN architectures create decentralised, high-dimensional control problems that centralised optimisation cannot scale to, and V2X systems are described as defeating conventional machine learning through high-dimensional state spaces, slow convergence and heterogeneous nodes. Quantum computing supplies a second demand pool: as monolithic scaling gets harder, distributed architectures shift compilation into a state-dependent networking-decision problem that RL is described as a natural framework for. Materials and chemistry supply a third, where the stated motivation is escaping the bias of pre-curated training datasets entirely. In every case the driver is the same: the problem is nonconvex or unlabelled, and there is a cheap simulator that can generate reward.

On supply, the sources say very little. There is no information here on training compute cost, funding, talent availability, tooling maturity or commercial vendors. The only supply-side signals are indirect: papers investing effort in curriculum learning and analytical shortcuts to cut training time and in parameter-shift gradient estimation for hybrid quantum policies imply that sample cost is a live constraint rather than a solved one. Score reflects demand evidence only.

**TLDR: Demand is genuine and comes from problems that are provably intractable to solve exactly; supply-side economics are absent from the sources.**

## Novelty (4/5)

The comparisons in these sources are unusually explicit about what RL is better than. Versus conventional quantum compilers that assign logical-to-physical qubit mappings randomly or heuristically, a trained policy plus local-search post-processing reports 65-85% fewer SWAPs. Versus fully centralised or fully distributed precoding, multi-agent RL with limited information exchange targets the middle ground both incumbents miss. Versus a classical actor-critic on CartPole, a single-qubit hybrid agent solves the environment in substantially fewer episodes. Versus classical MAA2C on cooperative navigation, quantum multi-agent RL reports roughly 2x success rate, about 0.85 against 0.40. Versus prior RL baselines in molecular generation, up to an order of magnitude more valid isomers.

Two discounts apply. First, baselines are chosen by the authors and, in the quantum compilation case, the incumbent is admitted to be random or heuristic assignment, which is a low bar. Second, one source in this set explicitly attacks the field's evaluation hygiene: it notes that most prior quantum multi-agent RL work evaluates policies without provable baselines, making it impossible to distinguish advantage from algorithmic coincidence, and responds by testing against the CHSH game's mathematically proven classical ceiling of 0.75, reaching 0.854 near the Tsirelson limit. That critique generalises: the margins in this literature are believable in direction and unverified in magnitude.

**TLDR: Where the incumbent is a hand-written heuristic, the reported margins are large and repeatedly so across unrelated fields.**

## Diffusion (2/5)

Adoption barriers here are named clearly by the papers themselves. Latency and inference budget: on real hardware, control-loop rate trades directly against measurement shot count, and both strongly affect stability. Distribution shift: a policy trained in a simulator faces changing channel conditions and multipath ambiguity in the field, which is why the emitter-localisation work reaches for meta-RL and recurrent policies and studies domain shift as a first-class question. Constraint satisfaction: safety- and security-critical deployments require guarantees, and the QKD framework has to keep a learned controller strictly inside composable security constraints. Problem-specific engineering: the fact that action-space formulation and masking are the headline contribution of an entire paper tells you these policies do not transfer between problems without redesign.

Against that, one diffusion path looks comparatively easy. Where RL sits inside an offline design or compilation step rather than a live control loop, the deployment risk collapses: a qubit mapper only has to produce a valid circuit, and a discovered bosonic code only has to be a code. Expect adoption there first. The sources contain no evidence of any production or vendor deployment, so the score is held to 2.

**TLDR: Nothing in the sources shows adoption outside research code, and the specific barriers named are the hard ones.**

## Impact (4/5)

If the reported margins survive contact with hardware, the value is structural rather than incremental. SWAP overhead is a first-order determinant of what circuits can run on a near-term quantum processor at all, so a 65-85% reduction converts directly into executable depth. Autonomous quantum error correction that avoids the extra errors introduced by active measurement, with codes discovered rather than hand-derived under Knill-Laflamme conditions, addresses a bottleneck on the whole fault-tolerance roadmap. Aggregate throughput in cell-free massive MIMO under minimum-rate guarantees is the metric operators buy spectrum and hardware for. Generating stable molecules with no training data at all would remove the dataset-bias ceiling on generative chemistry.

The caveats: no source in this set quantifies economic value, market size or cost saving, so the impact judgement is inferred from the technical position of the metrics rather than measured. Impact is also broad and shallow rather than concentrated. RL is not creating a new capability in any of these papers; it is displacing a heuristic or an intractable solver inside an existing pipeline. That pattern generates a lot of aggregate value and no single defensible product.

**TLDR: The quantities being improved sit on critical paths in 6G capacity, usable quantum circuit depth and materials search throughput.**

## Timing Soon (2-5yr)

RL as a technique needs no waiting. What is pending is validation outside simulators. The offline uses can arrive fastest, because an RL-designed compiler pass or an RL-discovered error-correcting code can be verified by conventional means before use, and the compilation work is already benchmarked against real circuit datasets. Live control uses are slower: the one attempt at physical execution in this set is an end-to-end study explicitly framed as addressing the gap between idealised simulation and a physical QPU, and it stops short of the real-time control demonstration, instead mapping out the trade-offs an eventual demonstration must respect.

The wireless applications have a timing dependency outside RL itself. Cell-free massive MIMO in O-RAN, integrated sensing and covert communication in low-altitude networks, and quantum-enhanced V2X aggregation are all positioned against 6G deployment. The RL controller cannot arrive before the radio architecture it controls.

**TLDR: The method is mature; the specific applications in these sources are one hardware-validation step away from mattering.**

## Overrated or underrated? Fairly rated

The interesting thing in these sources is not that RL works, it is where it has migrated to. RL has become the default tool for any engineering problem that is nonconvex, sequential and equipped with a simulator, and the same paragraph of motivation now appears in papers on precoding, optical power allocation, quantum compilation, QKD parameter tuning and molecular construction. That is the signature of a maturing general-purpose method rather than a frontier. Treating it as an AI story is a category error; it is closer to a numerical-methods story.

Where caution is warranted is in the reported margins. This is a preprint literature with author-chosen baselines, and one paper in the set makes precisely that criticism of its own subfield, noting that policies are routinely evaluated without provable baselines so quantum advantage cannot be distinguished from algorithmic coincidence. A 65-85% improvement over a random-or-heuristic incumbent is a real result about the incumbent as much as about RL. On the theory side, the claimed identity between attention gradients and advantage-based policy gradients is intellectually interesting but should be cited accurately and narrowly, as one-sided entropic optimal transport and a single author, not the general equivalence it has been reported as. Fairly rated: the technique deserves its position, the individual claims do not yet deserve to be taken at face value.

## Prediction

By 31 December 2027, no source in this line of work will report an RL-trained policy running as the default production path in a commercially deployed O-RAN precoder or a vendor quantum compiler; the results will remain simulation-benchmarked or hardware-demonstration-only.

## Evidence base

- 14 May 2026: an RL policy for logical-to-physical qubit mapping, with local-search post-processing, reports 65-85% reduction in SWAP overhead versus existing quantum compilers on MQTBench and Queko circuits.
- 2 June 2026: a PPO-based QKD parameter tuner with TCN forecasting reports a 14-25% increase in median secure key rate and median QBER falling from 3.0% to 1.5%, with an exploratory quantum RL extension claiming 29.2% throughput gain on E91.
- 15 May 2026: entangled quantum multi-agent RL reaches 0.854 win rate on CHSH against a proven classical ceiling of 0.75, and about 0.85 versus 0.40 success on cooperative navigation against classical MAA2C, while the same paper criticises the field for evaluating without provable baselines.
- 28 May 2026: an agent trained exclusively online with no pretraining discovers up to an order of magnitude more valid isomers on unseen chemical formulas than single-composition RL baselines using per-step energy rewards.
- 5 May 2026: on a physical superconducting QPU, a single-qubit hybrid agent solves CartPole in substantially fewer episodes than a comparable classical actor-critic, but stability depends strongly on both inference control frequency and measurement shot count, and a real-time control demonstration remains future work.
- 11 August 2025 (revised 29 December 2025): a single-author paper proves attention's forward pass is the exact solution to a degenerate one-sided entropic optimal transport problem and argues its backward pass yields gradients identical to advantage-based policy gradients, while warning the claim is narrower than commonly cited.

## Open questions

- Do the reported margins survive independent reimplementation against strong classical baselines rather than the random or heuristic incumbents used in the source papers, particularly the 65-85% SWAP reduction?
- How much do these policies degrade under domain shift between the training simulator and measured hardware or channel conditions, which the emitter-localisation work raises but does not settle?
- Can learned controllers meet hard real-time and formal-constraint requirements, given that inference frequency and shot budget already dominate stability in the only physical-hardware study here?
- How much of the performance is attributable to RL rather than to problem-specific engineering of the action space, masking and reward, which one paper treats as the primary lever?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
