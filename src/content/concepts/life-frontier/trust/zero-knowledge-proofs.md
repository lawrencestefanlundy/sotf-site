---
type: concept
slug: zero-knowledge-proofs
canonical_name: Zero-Knowledge Proofs
aliases: []
kind: technology
parent_concepts:
- life-frontier
- trust
related_concepts: []
sources:
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2023-10-19-e20-the-state-of-privacy-enhancing]]'
- '[[2021-07-21-why-privacy-tech-is-actually-collaborative]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2023-07-06-e07-decentralised-ai]]'
- '[[2023-05-05-interview-rick-hao-partner-at-speedinvest]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 11
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-10-09-a-specific-theory-of-sovereign-ai
  title: A Specific Theory of Sovereign AI
  date: '2025-10-09'
  kind: substack
- slug: 2023-10-19-e20-the-state-of-privacy-enhancing
  title: Understanding Privacy Enhancing Technology (Feat. Karim Eldefrawy, Confidencial.io)
  date: '2023-10-19'
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
- slug: 2021-07-21-why-privacy-tech-is-actually-collaborative
  title: 💡Collaborative Computing
  date: '2021-07-21'
  kind: substack
neighbors: []
---
## Physics / mechanism

Zero-knowledge proofs (ZKPs) let a prover convince a verifier that a statement is true without revealing any information beyond its truth. Formally: a protocol is ZK if it satisfies completeness, soundness, and zero-knowledge. Modern constructions—zk-SNARKs (Groth16, PLONK), zk-STARKs, and Bulletproofs—reduce proof size and verification cost via polynomial commitment schemes and elliptic-curve pairings or hash-based arithmetic. Current benchmarks: zk-SNARKs generate proofs in ~100ms–10s depending on circuit depth; STARKs are slower to prove (~10×) but avoid trusted setup and are post-quantum candidate-compatible. Proof sizes range from ~200 bytes (Groth16) to ~100 KB (STARKs). Prover compute remains the bottleneck—GPU/FPGA acceleration is actively reducing latency toward real-time thresholds.

## Competitive landscape

The primary axis is proof system choice: SNARKs (small proofs, pairing-dependent, trusted setup) vs. STARKs (larger proofs, hash-only, no setup) vs. Bulletproofs (no setup, logarithmic size, slower verification). Adjacent: secure multi-party computation (MPC) and fully homomorphic encryption (FHE) address overlapping confidentiality use cases but differ sharply on latency and composability.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
