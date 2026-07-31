---
type: concept
slug: homomorphic-encryption
canonical_name: Homomorphic Encryption
aliases: []
kind: technology
parent_concepts:
- life-frontier
- trust
related_concepts: []
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2023-10-19-e20-the-state-of-privacy-enhancing]]'
- '[[2023-02-05-interview-flavio-bergamaschi-private]]'
- '[[2021-07-21-why-privacy-tech-is-actually-collaborative]]'
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2023-07-06-e07-decentralised-ai]]'
- '[[2023-03-05-interview-dr-hyoduk-shin-professor]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-04-05-interview-stijn-christiaens-ceo-of]]'
- '[[2023-05-05-interview-rick-hao-partner-at-speedinvest]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 38
last_reorg_date: '2026-05-13'
sources_7d: 7
sources_30d: 15
recent_mentions:
- slug: 2025-10-09-a-specific-theory-of-sovereign-ai
  title: A Specific Theory of Sovereign AI
  date: '2025-10-09'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2024-11-05-confidential-ai-the-dog-that-didnt
  title: Confidential AI
  date: '2024-11-05'
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
- slug: 2023-05-24-launching-state-of-the-future
  title: '💡 E01: Launching State of the Future: The Worlds First Deep Tech Tracker'
  date: '2023-05-24'
  kind: substack
neighbors: []
---
## Physics / mechanism

Homomorphic encryption (HE) allows computation on ciphertext such that decrypting the result equals applying the same function to plaintext. Fully homomorphic encryption (FHE) supports arbitrary operations via lattice-based constructions (CKKS, BFV, TFHE schemes). The core mechanism relies on learning-with-errors (LWE) hardness; noise accumulates with each operation and must be managed via bootstrapping. Current SOTA: TFHE bootstrapping ~1–10 ms per gate on CPU; GPU-accelerated libraries (OpenFHE, HEIR) cut this 10–100×. Practical deployments remain 3–6 orders of magnitude slower than plaintext compute. Key parameters: polynomial modulus degree (n = 2¹⁴–2¹⁶), noise budget, and multiplicative depth.

## Competitive landscape

The primary competitive tension is between FHE, secure multi-party computation (MPC), and trusted execution environments (TEEs like Intel TDX, AMD SEV). Each occupies a different point on the trust-vs-performance curve.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*

## Merged from root duplicate (homomorphic-encryption.md at concepts/ root, 2026-06-10)

# Homomorphic Encryption (FHE)

Encryption that allows computation directly on ciphertext, so data stays encrypted in use. The blocker is compute cost (orders of magnitude over plaintext), which drives the **Fhe Acceleration Silicon** thesis: purpose-built accelerators for the polynomial/NTT bottleneck. A pillar of confidential computing alongside TEEs.
