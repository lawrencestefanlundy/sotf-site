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
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 14
last_reorg_date: '2026-05-13'
sources_7d: 2
sources_30d: 2
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
## Physics / mechanism

Multi-party computation is a cryptographic protocol family allowing *n* parties to jointly compute a function over private inputs without any party revealing its data to others. Core mechanism: secret sharing (Shamir, additive) splits each input into shares distributed across parties; computation proceeds on shares via arithmetic or Boolean circuits, with results reconstructed only at output. Variants include garbled circuits (Yao, two-party, constant rounds), GMW protocol (multi-party, linear rounds), and SPDZ (preprocessing model, malicious security). Performance benchmarks: AES evaluation ~0.1–1ms in semi-honest LAN settings; malicious-secure protocols add 5–10× overhead. Homomorphic encryption (FHE) handles single-party computation on encrypted data and is often conflated but distinct. MPC maturity is high for specific applications (threshold signatures, private set intersection); general-purpose MPC remains latency-constrained.

## Competitive landscape

| Approach | Security model | Latency | Compute overhead |
|---|---|---|---|
| MPC (SPDZ/GMW) | Multi-party, malicious | Medium–High | 10–100× vs plaintext |
| FHE (CKKS/BFV) | Single-party compute | High | 1000–10000× |
| TEE (SGX/TrustZone) | Hardware attestation | Low | ~1–2× |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
