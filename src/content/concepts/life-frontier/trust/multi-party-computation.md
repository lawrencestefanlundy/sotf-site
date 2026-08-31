---
type: concept
slug: multi-party-computation
canonical_name: Multi-Party Computation (MPC)
aliases: []
kind: technology
parent_concepts:
- life-frontier
- trust
related_concepts: []
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2021-07-21-why-privacy-tech-is-actually-collaborative]]'
- '[[2025-02-05-you-like-ai-agents-you-are-gonna]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2023-07-06-e07-decentralised-ai]]'
- '[[2022-12-15-unbundling-the-database]]'
- '[[2023-05-05-interview-rick-hao-partner-at-speedinvest]]'
frontier: []
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 14
last_reorg_date: '2026-05-13'
scorecard:
  viability: null
  drivers: null
  novelty: null
  diffusion: null
  impact: null
  timing_band: Unclear
  verdict: ''
scorecard_status: draft
sources_7d: 0
sources_30d: 0
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
- slug: 2023-10-13-e19-trusted-execution-environments
  title: Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)
  date: '2023-10-13'
  kind: substack
- slug: 2023-07-06-e07-decentralised-ai
  title: '🔮E07: Decentralised AI'
  date: '2023-07-06'
  kind: substack
- slug: 2023-06-08-three-overrated-technologies-from
  title: '💡E03: Three Overrated Technologies from the Future Fusion, Bitcoin & LEO Internet + Ultrasound for Hibernation; Wind Power; Skeletal Editing; Carbon Pricing; & Psychedelics++'
  date: '2023-06-08'
  kind: substack
- slug: 2023-05-05-interview-rick-hao-partner-at-speedinvest
  title: '☎️ Interview: Rick Hao, Partner at SpeedInvest on the State of Privacy-Enhancing Technologies #005'
  date: '2023-05-05'
  kind: substack
- slug: 2022-12-15-unbundling-the-database
  title: '💡Thesis: Unbundling the Database: Serverless, Edge and Secure'
  date: '2022-12-15'
  kind: substack
neighbors: []
---
**Multi-party computation lets several parties jointly compute a result over private inputs without any of them revealing those inputs, and recent work shows it working cheaply in hardware authentication while still fighting accuracy and speed penalties in machine learning.**

## Summary

Secure multi-party computation (MPC) is a cryptographic technique in which several parties each hold a private input, jointly compute an agreed function, and learn only the output. Inputs are typically split into shares distributed across the participants so that no single party, and no subset below a threshold, can reconstruct anything sensitive. It sits inside the wider family of privacy-enhancing technologies alongside homomorphic encryption, zero-knowledge proofs and verifiable computation. The problem this family addresses is the gap in the standard communication chain: data can be encrypted at rest on a device and protected in transit with TLS, but it is normally decrypted during processing, which is where the exposure sits <sup class="ref"><a href="https://stateofthefuture.substack.com/p/why-privacy-tech-is-actually-collaborative" title="💡Collaborative Computing" rel="noopener">ref</a></sup>.

Two quite different application classes appear in the current literature. The first is machine learning. In MPC-based ML, a model owner and a data owner run inference or training without either surrendering their asset: the model owner keeps proprietary weights, the user keeps private samples. The engineering difficulty is that cryptographic protocols cannot execute arbitrary non-linear operators cheaply, so frameworks apply a chain of MPC-specific transformations, notably operator approximation, which introduce both error and overhead and are largely opaque to the user.

The second class is hardware trust. Chiplet-based heterogeneous integration fragments the semiconductor supply chain across multiple vendors and post-fabrication assembly, opening the door to cloning, overproduction and chiplet substitution, and existing authentication schemes rely on trusted integrators or centralised anchors that create single points of failure. Here MPC is used to verify device signatures collaboratively across several chiplets so that raw signatures are never exposed, in one case combined with a route-based delay physically unclonable function embedded in a reconfigurable interposer.

The parameters that decide MPC's fate are the same in both cases: how much computation and communication overhead the protocol adds versus the plaintext baseline, how much accuracy is lost to approximation, whether a credible set of mutually non-colluding parties exists, and whether trusted hardware (a TEE, treated in this knowledge base as the practical route to confidential cloud computing) solves the same problem more cheaply <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e19-trusted-execution-environments" title="Understanding Confidential Computing (feat. Ilja Aizenberg, M Ventures)" rel="noopener">ref</a></sup>.

## Viability (unscored)

## Drivers (unscored)

## Novelty (unscored)

## Diffusion (unscored)

## Impact (unscored)

## Timing Unclear

---
*Assessment drafted 2026-08-31 from up to 13 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
