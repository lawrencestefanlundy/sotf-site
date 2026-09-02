---
type: concept
slug: federated-learning
canonical_name: Federated Learning
aliases: []
kind: technology
parent_concepts:
- life-frontier
- trust
related_concepts: []
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2023-02-05-interview-flavio-bergamaschi-private]]'
- '[[2023-09-28-e16-in-conversation-with-shiv-malik]]'
- '[[2021-07-21-why-privacy-tech-is-actually-collaborative]]'
- '[[2025-02-05-you-like-ai-agents-you-are-gonna]]'
- '[[2023-06-30-e06-the-model-t-moment-for-bits-llms]]'
- '[[2023-04-04-learnings-from-a-deep-tech-horizon]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2023-01-05-interview-christine-huang-data-privacy]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2023-07-06-e07-decentralised-ai]]'
- '[[2023-03-05-interview-dr-hyoduk-shin-professor]]'
- '[[2023-05-05-interview-rick-hao-partner-at-speedinvest]]'
frontier:
- Do the reported gains of federated over centralised training on 5G jamming detection (97% accuracy and F1) replicate on real multi-user handset populations with non-IID data, or are they an artefact of the SSB IQ dataset split? 2026 05 05 toward resilient 5g networks comparative analysis of federat
- Can hardware-enforced differential privacy of the DataGuard type be integrated into commodity mobile and accelerator silicon at acceptable area and performance cost, and who certifies the guarantee? 2026 06 16 dataguard guaranteeing private training in systolic array ba
- Does the CHRONOS result (74% active-phase latency reduction, sub-1.1 KB Secure World footprint) hold beyond 32 nodes and under realistic client churn? 2026 07 28 chronos a hardware assisted phase decoupled framework for se
- Is there any aggregation rule that bounds worst-case damage from a single malicious client without assuming a trusted enrolment process for clients? 2026 05 28 can quantum federated learning withstand circuit level backd
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 33
last_reorg_date: '2026-05-13'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 2
sources_30d: 5
recent_mentions:
- slug: 2025-10-09-a-specific-theory-of-sovereign-ai
  title: A Specific Theory of Sovereign AI
  date: '2025-10-09'
  kind: substack
- slug: 2025-02-05-you-like-ai-agents-you-are-gonna
  title: Decentralised AI (Feat. Richard Blythman of Naptha)
  date: '2025-02-05'
  kind: substack
- slug: 2024-11-05-confidential-ai-the-dog-that-didnt
  title: Confidential AI
  date: '2024-11-05'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2023-09-28-e16-in-conversation-with-shiv-malik
  title: '☎️ E17: In Conversation with Shiv Malik, CEO of Pool.io on the State of Data Unions 🤝₿'
  date: '2023-09-28'
  kind: substack
- slug: 2023-07-06-e07-decentralised-ai
  title: '🔮E07: Decentralised AI'
  date: '2023-07-06'
  kind: substack
- slug: 2023-06-30-e06-the-model-t-moment-for-bits-llms
  title: '🔮 E06: Large Language Models and the Assembly Line'
  date: '2023-06-30'
  kind: substack
- slug: 2023-06-08-three-overrated-technologies-from
  title: '💡E03: Three Overrated Technologies from the Future Fusion, Bitcoin & LEO Internet + Ultrasound for Hibernation; Wind Power; Skeletal Editing; Carbon Pricing; & Psychedelics++'
  date: '2023-06-08'
  kind: substack
neighbors: []
---
**Federated learning trains a shared model across devices that keep their raw data local, exchanging only model updates; it now works well enough to beat centralised baselines in specific edge tasks, but its privacy and robustness guarantees depend on cryptography and hardware that are still being built.**

## Summary

Federated learning (FL) inverts the usual machine learning pipeline. Instead of pooling data in a central store and training there, each participating device trains on its own data locally and sends only model updates to a server, which averages them into a global model. Federated Averaging (FedAvg) is the canonical aggregation rule. The claimed benefit is that raw data never leaves the device, so the approach fits domains where pooling is illegal, commercially impossible or physically impractical: patient signals, handset radio measurements, vehicle sensor streams, industrial telemetry.

The mechanism creates three new problems in place of the one it solves. First, model updates are not private by construction: gradients can be inverted to recover training data, which is why deployments layer on differential privacy, secure aggregation or secure multiparty computation. Second, those defences cost bandwidth and latency that edge devices often do not have; secure multiparty computation in particular imposes communication overhead described as prohibitive against IoT latency and energy budgets. Third, the system trusts its clients. Because the server sees only updates, a malicious participant can poison the global model, and recent work shows that in the quantum FL setting a single malicious client can cut accuracy by up to 50% under FedAvg even with popular Byzantine-robust defences in place.

The parameters that decide whether FL is the right choice are therefore: how heterogeneous and non-IID the client data is, how much communication per round the network can afford, whether the privacy claim needs to be enforceable rather than asserted, and how many clients can be assumed honest. A recurring theme in the current literature is that the answers are being pushed into hardware. Proposals include a hardware mechanism that guarantees only differentially private results can leave a device, removing the need to trust a third-party FL application that today is given full access to sensitive data, a TrustZone-based framework that moves cryptographic setup into idle windows and cuts active-phase latency by up to 74% versus synchronous secure aggregation, and a 65-nm neuromorphic encoder that supports federated learning at 357.32 nJ per training update.

A longer-standing framing places FL inside the wider privacy-enhancing technology (PET) stack alongside multiparty computation, homomorphic encryption and zero-knowledge proofs, on the thesis that securing data during processing unlocks a new market in confidential data collaboration <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup>. Practitioners in that stack caution that decentralisation is not automatically privacy: there is no general principle that distributed computing is more private than centralised computing, and it depends on system configuration, application requirements and the specific threat <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-flavio-bergamaschi-private" title="☎️ Interview: Flavio Bergamaschi, Private AI and Analytics at Intel on the State of Privacy-Enhancing Technologies #002" rel="noopener">ref</a></sup>.

## Viability (3/5)

The core training loop works. An FL framework on over-the-air IQ samples from 5G synchronisation signal blocks reached 97% accuracy and 97% F1 for jamming detection, reported as outperforming centralised MLP, 1DCNN, SVM and logistic regression baselines. A fabricated 65-nm encoder with federated learning support hit 93.2% accuracy on EMG and 96.1% on UCI-HAR, which is meaningful because it is silicon rather than simulation. A federated quantum feature-sketching pipeline was evaluated on NGSIM trajectories, SUMO and IBM Quantum hardware.

What is not viable yet is the guarantee. Gradients remain susceptible to inversion attacks, real deployments assume a third-party FL application correctly implements differential privacy while giving it full access to sensitive data, and defences including Krum, Multi-Krum, FoolsGold, FLGuardian and Mud-HoG reduce but do not eliminate worst-case poisoning failures. A system that trains accurately but cannot substantiate its privacy or integrity claims is only half viable for the regulated use cases that motivate it.

**TLDR: Task-level accuracy is demonstrated repeatedly; the security and robustness layer is not settled.**

## Drivers (3/5)

Supply side: 2026 NSF awards cluster around exactly the problems FL creates. A back-propagation-free split learning project targets the communication cost of collaborative training on wearables and mobile devices ($199,494); two REU sites fund edge intelligence and trustworthy edge sensing at $464,400 and $464,999; and the VINES NextG programme funds AI-enabled, quantum-ready cellular network security at $559,850 and $307,250, with explicit intent to release open-source software, protocols and datasets to inform standards development. These are academic-scale sums, not industrial commitment.

Demand side: the pull comes from settings where centralisation is a liability. Hospital robotics must keep working through disrupted connectivity without compromising patient confidentiality, driving lightweight on-robot models that talk to the cloud only when needed ($592,000). Industrial and autonomous systems face latency and external dependency when operational data must traverse a central platform before decisions can be made. Against that, the PET interviews argue the binding constraint is not technical: data sharing is cultural, incentives need realignment, and selling data collaboration software means convincing five distinct internal groups <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-christine-huang-data-privacy" title="☎️ Interview: Christine Huang, Data Privacy & Protection at SAP on the State of Privacy-Enhancing Technologies #001" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-dr-hyoduk-shin-professor" title="☎️ Interview: Dr Hyoduk Shin, Professor of Innovation at UC San Diego on the State of Privacy-Enhancing Technologies #00" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-flavio-bergamaschi-private" title="☎️ Interview: Flavio Bergamaschi, Private AI and Analytics at Intel on the State of Privacy-Enhancing Technologies #002" rel="noopener">ref</a></sup>. The sources contain no revenue, procurement or production-deployment figures for FL.

**TLDR: Steady public research funding on the supply side; demand is asserted from regulated edge applications rather than evidenced by deployments.**

## Novelty (3/5)

The caution is that each of these is one paper on one benchmark, and the counter-argument from industry is structural: there is no general principle that distributed computing is more private than centralised computing, it depends on configuration, requirements and threat model <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-flavio-bergamaschi-private" title="☎️ Interview: Flavio Bergamaschi, Private AI and Analytics at Intel on the State of Privacy-Enhancing Technologies #002" rel="noopener">ref</a></sup>. FL is also not the only route to the same outcome; homomorphic encryption, multiparty computation and blind delegated computation address overlapping problems <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup>.

**TLDR: Better than centralised learning on specific edge tasks and much cheaper on communication than secure MPC, but the margins are single-benchmark.**

## Diffusion (2/5)

The non-technical barrier may dominate. The PET interviews argue data sharing is fundamentally cultural and requires legal, compliance, technical and business functions to align before onboarding partners <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-christine-huang-data-privacy" title="☎️ Interview: Christine Huang, Data Privacy & Protection at SAP on the State of Privacy-Enhancing Technologies #001" rel="noopener">ref</a></sup>, that incentives must be realigned toward sharing <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-dr-hyoduk-shin-professor" title="☎️ Interview: Dr Hyoduk Shin, Professor of Innovation at UC San Diego on the State of Privacy-Enhancing Technologies #00" rel="noopener">ref</a></sup>, and that a globally fragmented data economy is the likely outcome because values differ across jurisdictions <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-christine-huang-data-privacy" title="☎️ Interview: Christine Huang, Data Privacy & Protection at SAP on the State of Privacy-Enhancing Technologies #001" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-dr-hyoduk-shin-professor" title="☎️ Interview: Dr Hyoduk Shin, Professor of Innovation at UC San Diego on the State of Privacy-Enhancing Technologies #00" rel="noopener">ref</a></sup>. Nothing in the supplied sources documents a commercial FL rollout at scale, so this score reflects demonstrated diffusion, which is low, not potential.

**TLDR: Barriers are trust, communication budget and organisational culture; the sources show research testbeds, not fielded systems.**

## Impact (3/5)

Where centralisation is legally or physically blocked, FL changes what is buildable: collaborative jamming detection across handsets without collecting user RF data, cold-start personalisation and continual learning across multiple users of a wearable bio-signal device, roadside cooperative-manoeuvre gating where raw observations, vehicle records and event traces stay local, and hospital robots that keep patient data on-device through connectivity loss. The energy numbers matter for the wearable case specifically: 7.13 nJ per encoding, 76.44 nJ per prediction and 357.32 nJ per training update.

The expansive claim, that privacy-enhancing technologies create a new collaborative computing market worth a trillion dollars by letting data be shared without barriers <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-christine-huang-data-privacy" title="☎️ Interview: Christine Huang, Data Privacy & Protection at SAP on the State of Privacy-Enhancing Technologies #001" rel="noopener">ref</a></sup>, is an investment thesis from 2021 to 2023 and the sources supply no subsequent market data to test it. FL is one component of that stack, not the whole of it. Judged on what is demonstrated, the impact is domain-specific and substantial rather than economy-wide.

**TLDR: Real value in domains where pooling is blocked; the trillion-dollar framing in the sources is a thesis, not a measurement.**

## Timing Soon (2-5yr)

The learning side is ready today: working prototypes span 5G RF detection, fabricated 65-nm hardware and a 32-node heterogeneous IoT testbed. What is not ready is the part a regulated buyer would need: hardware-enforced differential privacy is a proposal, and poisoning defences still admit worst-case accuracy drops of up to 50%.

The institutional clock points to the same window. The 2026 NSF VINES awards commit to releasing open-source implementations, formal models and evaluation tools to inform industrial adoption and standards development, and the REU awards are workforce pipeline investments. Research-to-standards-to-product on that path is multi-year. Quantum federated variants sit further out again: they are being probed for vulnerabilities and lack tooling, with the first blind-computation transpiler library only now appearing.

**TLDR: Accuracy is there now; the enforceable-privacy and Byzantine-robustness layer is the pacing item, and it is currently at prototype silicon and testbed stage.**

## Overrated or underrated? Fairly rated

FL is treated in the current literature as a default building block for edge AI rather than a breakthrough, and that is about right. It reliably solves one problem, keeping raw data local, and it does so with competitive accuracy in narrow tasks. It does not by itself deliver privacy or integrity, and the honest reading of the 2026 work is that the field has moved from proving FL trains to admitting that FL as commonly deployed trusts too much: the application implementing differential privacy, the clients not being malicious, and the network affording secure aggregation.

The position to take is that the interesting investment surface is no longer FL algorithms but the enforcement layer beneath them: trusted execution, hardware-guaranteed privacy budgets, cheap masking schemes and communication-light training such as back-propagation-free split learning. The 2021 to 2023 framing that PETs would open a trillion-dollar collaborative computing market <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup> remains untested in these sources, and the practitioner view that the blockers are cultural and organisational rather than cryptographic <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-christine-huang-data-privacy" title="☎️ Interview: Christine Huang, Data Privacy & Protection at SAP on the State of Privacy-Enhancing Technologies #001" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/interview-dr-hyoduk-shin-professor" title="☎️ Interview: Dr Hyoduk Shin, Professor of Innovation at UC San Diego on the State of Privacy-Enhancing Technologies #00" rel="noopener">ref</a></sup> has not been contradicted by anything since. Expect FL to be everywhere as a feature and rarely the reason a system gets bought.

## Prediction

By the end of 2028, published benchmarks will still show software-only Byzantine-robust aggregation (Krum, Multi-Krum, FoolsGold and successors) failing to eliminate worst-case accuracy degradation from a single malicious client under non-IID FedAvg, and the credible mitigations shipped in products will be hardware-rooted (trusted execution or accelerator-enforced privacy budgets) rather than purely algorithmic.

## Evidence base

- 5 May 2026: a FedAvg-trained 1DCNN on over-the-air 5G SSB IQ samples reached 97% accuracy and 97% F1 for jamming detection, reported to outperform centralised MLP, 1DCNN, SVM and logistic regression baselines without sharing raw RF data 
- 28 May 2026: under a circuit-level backdoor threat model on MNIST and CIFAR-10 with non-IID splits, a single malicious client degraded FedAvg accuracy severely, and Krum, Multi-Krum, FoolsGold, FLGuardian and Mud-HoG failed to eliminate worst cases where accuracy dropped up to 50% 
- 16 June 2026: a fabricated 65-nm privacy-preserving neuromorphic encoder with federated learning support achieved 7.13 nJ per encoding, 76.44 nJ per prediction, 357.32 nJ per training update, 93.2% EMG accuracy and 96.1% UCI-HAR accuracy 
- 16 June 2026: real-life FL deployments are described as assuming a third-party application can be trusted to implement differential privacy correctly, and are therefore given full access to sensitive data, motivating hardware-enforced privacy budgets 
- 28 July 2026: CHRONOS reduced active-phase latency by up to 74% versus synchronous secure aggregation on a 32-node Rock Pi 4 and Orange Pi 5 testbed with a persistent Secure World footprint under 1.1 KB, on the premise that existing secure MPC defences exceed IoT latency and energy budgets 
- 3 August 2026: FedQML-Edge reduced test log loss by 14.4% versus the strongest matched classical sketch on NGSIM and used 7 to 28 times less communication per round than larger MLPs on SUMO, sharing only classifier updates 
- 2 August 2026: NSF VINES NextG awards of $559,850, $307,250 and $592,000 fund AI-enabled, quantum-secure cellular networks and secure hospital robotics with commitments to release open-source software and evaluation tools for standards development 

## Open questions

- Do the reported gains of federated over centralised training on 5G jamming detection (97% accuracy and F1) replicate on real multi-user handset populations with non-IID data, or are they an artefact of the SSB IQ dataset split? 
- Can hardware-enforced differential privacy of the DataGuard type be integrated into commodity mobile and accelerator silicon at acceptable area and performance cost, and who certifies the guarantee? 
- Does the CHRONOS result (74% active-phase latency reduction, sub-1.1 KB Secure World footprint) hold beyond 32 nodes and under realistic client churn? 
- Is there any aggregation rule that bounds worst-case damage from a single malicious client without assuming a trusted enrolment process for clients? 

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
