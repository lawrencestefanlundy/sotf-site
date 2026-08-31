---
type: concept
slug: heterogeneous-computing
canonical_name: Heterogeneous Computing
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 10
frontier:
- What end-to-end inference latency reduction does ILP-based CPU-CIM partitioning deliver versus accelerator-only or CPU-only baselines, on which model families and at what problem sizes does the ILP solve become intractable? 2026 07 07 optimizing ml workload partitioning between cpus and cim acc
- Does accounting for RRAM write endurance change the optimal partition materially, and how many re-mappings can a deployed CIM array sustain before latency or accuracy degrades?
- Can coherent-interconnect zero-copy state sharing meet microsecond-level reflex deadlines in a physical RAN deployment, or does cache coherence traffic reintroduce the bottleneck it removes? 2026 06 05 bridging the cognitive gap a unified memory paradigm for 6g
- What fraction of heterogeneity-related AI compilation bugs are silent output changes rather than crashes, and can automated testing detect them without a trusted reference platform? 2026 05 11 nsf 2541224 career redefining testing foundations fo
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-02-12-how-to-invest-in-ai-sovereignty-sovereign
  title: How to Invest in AI Sovereignty — Sovereign Albion w/ Andrew Bennett
  date: '2026-02-12'
  kind: substack
- slug: 2025-12-19-lfg-for-semiconductors
  title: LFG (for semiconductors)
  date: '2025-12-19'
  kind: substack
- slug: 2023-07-23-analog-computing-the-once-and-future
  title: '🔮 E09: Analog Computing: The Once and Future King'
  date: '2023-07-23'
  kind: substack
neighbors: []
---
## Physics / mechanism

Heterogeneous computing describes systems that combine multiple distinct classes of compute unit within a single machine or fabric, so that each workload segment is executed on the substrate best matched to it. The canonical case in current research is a general-purpose CPU paired with a specialised accelerator: for machine learning inference, a Computing-in-Memory (CIM) accelerator executes matrix-vector multiplications directly in memory, while the CPU remains available as a complementary compute resource for the parts of the graph that map poorly onto the accelerator.

The central engineering problem is partitioning: deciding which operators run where, in what order, and with what data movement. For CPU-CIM systems the constraints are set by the memory technology itself. Resistive Random Access Memory (RRAM) arrays impose limited capacity, high write latency and limited write endurance, which means a partitioner must treat mapping decisions as expensive and semi-permanent rather than freely re-assignable. An Integer Linear Programming formulation has been proposed to minimise end-to-end inference latency under these RRAM constraints while capturing parallelism and low-level architectural effects, combining empirical profiling with analytical modelling rather than relying on either alone.

A second mechanism-level concern is state sharing across the heterogeneous fabric. In the 6G radio access network context, a proposed unified memory paradigm maps biological memory hierarchies onto heterogeneous computing fabrics, using emerging coherent interconnects so that microsecond-level reflexes, millisecond-level reasoning and long-term evolution share state across time scales. The argument is that message passing between disaggregated components forces the physical layer to compress high-dimensional states into low-dimensional metrics, creating a semantic bottleneck; replacing message passing with zero-copy observability removes that compression step.

Heterogeneity also shifts risk into the compilation and deployment toolchain. Software that adapts trained models to target devices is described as complex and fragile, with models that appear valid at a high level failing during deployment because of hidden resource limits, data layout requirements and platform-specific transformations. These failures can silently alter outputs rather than crash, which makes them difficult to detect and diagnose.

## Competitive landscape

The sources frame heterogeneous computing not as a competitor to specific accelerator types but as the integration layer above them. CIM/RRAM accelerators are positioned as compelling for ML because they perform MVMs in memory, yet the same source argues that prior partitioning work is deficient precisely because it neglects the CPU as a complementary resource, implying that accelerator-only designs underperform mixed designs on end-to-end latency. Adjacent exotic substrates covered elsewhere in this knowledge base include analog, neuromorphic and optical computing, with mixed-signal analog-digital ICs discussed as an edge AI play <sup class="ref"><a href="https://stateofthefuture.substack.com/p/analog-computing-the-once-and-future" title="🔮 E09: Analog Computing: The Once and Future King" rel="noopener">ref</a></sup>.

The differentiating axis between approaches is therefore the interconnect and memory model rather than the arithmetic unit. Architectures that rely on interface-bound disaggregation trade away high-dimensional state visibility for modularity; memory-centric architectures built on coherent interconnects trade modularity for a shared cognitive continuum.

## Evidence base

- An ILP-based workload partitioning framework for heterogeneous CPU-CIM systems, minimising end-to-end inference latency under RRAM constraints (limited memory, high write latency, limited endurance) while capturing parallelism, was announced on arXiv on 7 July 2026.
- The same work states that existing CIM partitioning approaches neglect parallelism, low-level architectural effects, or the CPU as a complementary compute resource.
- A position paper published 11 May 2026 proposes mapping biological memory hierarchies onto heterogeneous computing fabrics via coherent interconnects, replacing message passing with zero-copy observability for 6G agentic AI-RAN.
- That paper identifies the failure mode of current disaggregated architectures as interfaces forcing the physical layer to compress high-dimensional states into low-dimensional metrics.
- NSF awarded $315,154 under Award ID 2541224 (dated 05/07/2026) to Qian Zhang at UC Riverside for testing foundations for heterogeneity-aware AI compilation, targeting silent output changes across diverse hardware platforms.

## Frontier (open questions)

- What end-to-end inference latency reduction does ILP-based CPU-CIM partitioning deliver versus accelerator-only or CPU-only baselines, on which model families and at what problem sizes does the ILP solve become intractable? 
- Does accounting for RRAM write endurance change the optimal partition materially, and how many re-mappings can a deployed CIM array sustain before latency or accuracy degrades?
- Can coherent-interconnect zero-copy state sharing meet microsecond-level reflex deadlines in a physical RAN deployment, or does cache coherence traffic reintroduce the bottleneck it removes? 
- What fraction of heterogeneity-related AI compilation bugs are silent output changes rather than crashes, and can automated testing detect them without a trusted reference platform? 

*Synthesised 2026-08-31 from 7 KB sources by the resynth pipeline; citations are KB source slugs.*
