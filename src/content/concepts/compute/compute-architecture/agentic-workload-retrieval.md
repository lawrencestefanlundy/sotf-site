---
type: concept
slug: agentic-workload-retrieval
canonical_name: Agentic-workload context retrieval
aliases:
- agent context retrieval
- agentic memory access
- agent retrieval layer
parent_concepts:
- memory
- graphrag
related_concepts:
- processing-in-memory
- graphrag
- vector-databases
sources:
- '[[2026-06-02-agentic-runtime-silicon-necessity]]'
- '[[2026-06-23-engram-98m-learned-memory-token-costs]]'
frontier:
- Does the agentic workload pattern hold at hyperscaler-scale (10K+ agents per workflow), or does it bifurcate into agent-cluster vs single-agent topologies?
- Will NVIDIA NeMo Retriever + NIM absorb the agentic-retrieval workload via software before specialist hardware reaches design-win volume? Resolution by GTC 2027 published benchmarks.
- What is the actual production agent-step-count distribution in 2026 enterprise deployments? JPMorgan 200-agent compliance workflow is one data point; we need 10+.
- Is content-addressable broadcast read across millions of tiny processors actually the right architecture, or does Atlas's PIM design lose to a different topology (CXL-attached fabric, in-network DPU offload, HBM-PIM)?
last_updated: 2026-06-02
tags:
- concept
public_expressions:
- 005930.KS
- NVDA
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-26-postgres-absorption-vector-layer
  title: 'Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere'
  date: '2026-07-26'
  kind: web
neighbors:
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /memory/emerging-memory/processing-in-memory/
  macro: memory
- slug: graphrag
  name: Graphrag
  path: /ai-software/models-inference/graphrag/
  macro: ai-software
- slug: vector-databases
  name: Vector Databases
  path: /ai-software/models-inference/vector-databases/
  macro: ai-software
---
## What it is

The retrieval layer for agentic AI workloads — distinct from chatbot inference and from the vector-DB / matmul memory-bandwidth bottlenecks that XCENA, D-Matrix, NeuroBlade address. Agent tasks consist of dozens-to-hundreds of small reasoning steps, each of which fetches a small set of semantically relevant tokens from external memory (knowledge graph, vector store, structured DB, prior agent state) before the model can act. The dominant query topology is many-small-queries-per-task, not one-large-context-window-per-query.

## Why now (May 2026)

- **Scale of workload shift.** Agentic inference consumes ~100x more tokens per inference than chatbot inference on average, up to 1,000x in the maximum case (arxiv 2509.09505, "Combating the Memory Walls for Long-Context Agentic LLM Inference").
- **Adoption trajectory.** Gartner forecasts 40% of enterprise apps with task-specific agents by end-2026, up from <5% in 2025. 17% of organisations have deployed agents; 60%+ expect to within two years.
- **Production existence-proof.** JPMorgan Chase scaled a single-agent compliance pilot to 200+ specialist agents reviewing documents in production.
- **Demand signal hardening.** Buyer-intent for hybrid (vector + graph) retrieval tripled from 10.3% to 33.3% Jan-Mar 2026; retrieval-optimisation spend rose from 19% to 28.9% in Q1 2026 and overtook evaluation spend for the first time.
- **Category framing.** VentureBeat: "context architecture is replacing RAG as agentic AI pushes enterprise retrieval to its limits".

## Why this is distinct from adjacent bottlenecks

## Hardware architectures candidate

- **Processing-in-memory (PIM).** Atlas's bet: millions of tiny processors mapped to graph topology executing content-addressable broadcast reads in parallel against memory chunks. Each agent step becomes a parallel broadcast across relevant memory partitions rather than a serial DRAM walk.
- **CXL-attached fabric.** Memory disaggregation across CXL with controller-side filtering. Reference point: Cassion (Lawrence angel investment).
- **In-network DPU offload.** BlueField-style retrieval offload at the NIC tier. Mid-term NVIDIA play.
- **HBM-PIM.** Samsung HBM-PIM and similar; general-purpose near-memory compute, not retrieval-specialised.

## The agentic-silicon screen (DD heuristic)

When a founder pitches "silicon for agents," locate the *claimed* bottleneck on this tree before anything else (evidence base:):

One-line version: **the silicon agents strain is memory, not the agent loop; and within memory, the measured bind is capacity, with access-pattern (retrieval) the least-evidenced of the three as of 2 Jun 2026.** When a deck says "agent chip," the first question is *compute or memory*, and the second is *capacity, bandwidth, or access-pattern*.

## Open questions

See frontier in frontmatter.

## First mention