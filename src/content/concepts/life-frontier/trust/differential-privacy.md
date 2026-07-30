---
type: concept
slug: differential-privacy
canonical_name: Differential Privacy
aliases: []
kind: technology
parent_concepts:
- life-frontier
- trust
related_concepts: []
sources:
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2023-09-28-e16-in-conversation-with-shiv-malik]]'
- '[[2021-07-21-why-privacy-tech-is-actually-collaborative]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 12
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 4
recent_mentions:
- slug: 2025-10-09-a-specific-theory-of-sovereign-ai
  title: A Specific Theory of Sovereign AI
  date: '2025-10-09'
  kind: substack
- slug: 2023-09-28-e16-in-conversation-with-shiv-malik
  title: '☎️ E17: In Conversation with Shiv Malik, CEO of Pool.io on the State of Data Unions 🤝₿'
  date: '2023-09-28'
  kind: substack
- slug: 2023-06-08-three-overrated-technologies-from
  title: '💡E03: Three Overrated Technologies from the Future Fusion, Bitcoin & LEO Internet + Ultrasound for Hibernation; Wind Power; Skeletal Editing; Carbon Pricing; & Psychedelics++'
  date: '2023-06-08'
  kind: substack
- slug: 2021-07-21-why-privacy-tech-is-actually-collaborative
  title: 💡Collaborative Computing
  date: '2021-07-21'
  kind: substack
neighbors: []
---
## Physics / mechanism

Differential privacy (DP) adds calibrated statistical noise to query outputs or training gradients so that the presence or absence of any single record changes the output distribution by at most a multiplicative factor e^ε — the privacy budget. Smaller ε means stronger privacy, larger noise, lower utility. The Gaussian and Laplace mechanisms are workhorses; the Rényi DP and zero-concentrated DP variants offer tighter composition accounting. Local DP (noise at source) versus central DP (noise at aggregator) is the key architectural split. Google, Apple, and the US Census Bureau deploy central/local DP at scale; state-of-the-art ML training (DP-SGD via Opacus/TF Privacy) achieves ImageNet-class accuracy at ε ≈ 8–10 with clipping norm ~1.0.

## Competitive landscape

Competing approaches: secure multi-party computation (MPC) and homomorphic encryption (HE) preserve exact outputs but carry 10³–10⁶× compute overhead. Federated learning reduces data exposure but provides no formal privacy guarantee without DP layered on top. Synthetic data generation (e.g., SDV, Gretel) is easier to deploy but lacks composable, auditable guarantees. Trusted execution environments (TEEs — Intel TDX, AMD SEV) protect computation rather than the statistical output. In practice, most enterprise deployments combine DP + federated learning + TEEs.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
