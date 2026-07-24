---
type: concept
slug: ai-machine-learning
canonical_name: AI & Machine Learning
aliases: []
kind: technology
parent_concepts:
- life-frontier
- ai-infrastructure
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 26
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-23-datacenter-capex-is-spilling-over-into-a-chatgpt-of-robotics
  title: Datacenter Capex is Spilling over into a ChatGPT of Robotics Moment set for 2027 and this decade.
  date: '2026-07-23'
  kind: web
- slug: 2026-07-16-the-lab-of-the-future-should-feel-like-a-data-center-andy-be
  title: 🔬 The Lab of the Future Should Feel Like a Data Center — Andy Beam & Rafa Gómez-Bombarelli, Lila Sciences
  date: '2026-07-16'
  kind: web
- slug: 2026-06-24-arxiv-autospec-safety-rule-evolution-for-llm-agents-via-inductive-
  title: 'AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming'
  date: '2026-06-24'
  kind: paper
- slug: 2026-06-17-arxiv-breaking-the-code-security-assessment-of-ai-code-agents-thro
  title: 'Breaking the Code: Security Assessment of AI Code Agents Through Systematic Jailbreaking Attacks'
  date: '2026-06-17'
  kind: paper
- slug: 2026-06-16-arxiv-a-security-analysis-of-long-horizon-agentic-ai-systems-threa
  title: 'A Security Analysis of Long-Horizon Agentic AI Systems: Threats, Evaluation, and Framework Development'
  date: '2026-06-16'
  kind: paper
- slug: 2026-06-16-arxiv-benign-in-isolation-harmful-in-composition-security-risks-in
  title: 'Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosystems'
  date: '2026-06-16'
  kind: paper
- slug: 2026-06-16-arxiv-a-survey-on-agentic-security-applications-threats-and-defens
  title: 'A Survey on Agentic Security: Applications, Threats and Defenses'
  date: '2026-06-16'
  kind: paper
- slug: 2026-06-15-arxiv-hidden-in-plain-sight-benchmarking-agent-safety-against-deco
  title: 'Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH'
  date: '2026-06-15'
  kind: paper
neighbors: []
---
## Physics / mechanism

Transformer-based large language models dominate current AI: attention mechanisms scale as O(n²) in sequence length, mitigated by sparse attention, flash attention, and MoE routing. Training runs now exceed 10²³–10²⁴ FLOPs; inference is the cost-dominant phase at scale. Key parameters: model size (1B–1T+ parameters), context window (128k–1M tokens), quantisation precision (FP8/INT4 for edge), and memory bandwidth (HBM3e at ~1.2 TB/s). SotA: GPT-4o, Gemini 1.5, Llama 3, Mistral. The bottleneck has shifted from algorithms to silicon—compute density, memory bandwidth, and interconnect (NVLink, UCIe, CXL) now determine competitive position.

## Competitive landscape

The primary axis of competition is silicon architecture: GPU (NVIDIA H100/B200) vs. purpose-built AI accelerators (Groq, Cerebras, Tenstorrent, SambaNova) vs. in-memory compute and neuromorphic (Intel Loihi, IBM NorthPole). Photonic inference accelerators (Lightmatter, Luminous) attack the bandwidth wall via optical interconnect. At the algorithm layer, SSMs (Mamba) challenge transformers on long-context efficiency. Edge AI competes on power envelope: sub-10W inference on NPUs (Apple ANE, Qualcomm Hexagon).

| Axis | GPU (NVIDIA) | AI ASIC | Photonic |
|---|---|---|---|
| Throughput | High | Very high (narrow workload) | Bandwidth-limited currently |
| Power efficiency | Moderate | High | Potentially transformative |
| Flexibility | High | Low | Low |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
