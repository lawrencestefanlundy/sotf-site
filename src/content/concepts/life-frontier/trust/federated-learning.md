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
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 30
last_reorg_date: '2026-05-13'
sources_7d: 0
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
## Physics / mechanism

Federated learning (FL) trains a shared model across distributed data sources without moving raw data to a central server. Each node runs local SGD on its own dataset, then transmits only gradient updates or model weight deltas to an aggregator (commonly FedAvg). The aggregator averages updates—optionally weighted by local dataset size—and pushes the revised global model back. Key parameters: communication rounds (typically 50–1000), client participation fraction, local epochs per round, and differential privacy noise budget (ε, δ). State of the art: Google's production FL on Gboard handles ~500M devices; academic benchmarks show <2% accuracy gap vs. centralized training on IID data, larger gaps on non-IID distributions. Secure aggregation adds cryptographic overhead of ~10–30% latency.

## Competitive landscape

Central server training with strict data-sharing contracts is the direct alternative—lower complexity, higher accuracy, but legally untenable under GDPR/HIPAA in many verticals. Split learning partitions the model itself rather than data. Swarm learning removes the central aggregator via blockchain coordination. On-device inference (TinyML) is adjacent but orthogonal—inference, not training.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
