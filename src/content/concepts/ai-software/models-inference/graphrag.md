---
type: concept
slug: graphrag
canonical_name: Graphrag
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2025-08-12-ai-and-junior-white-collar-automation]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
descendants:
- agentic-workload-retrieval
mention_count: 3
frontier:
- What is the measured traversal latency and energy per linknode hop for the Views model on real hardware, and how does it compare with a conventional property-graph engine on the same query set?
- Has the Views preprint passed peer review, and have any of its ISA operations, including CAR, been implemented in silicon rather than simulated?
- Do graph-structured retrieval pipelines built on such a store show measurable answer-quality or cost gains over vector-index RAG on a published benchmark?
- At what graph size does the claim of traversal without whole-memory broadcast break down, and what is the memory-capacity ceiling per device?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-08-12-ai-and-junior-white-collar-automation
  title: 'AI and Junior White Collar Automation: Update after EIG’s New Report'
  date: '2025-08-12'
  kind: substack
neighbors: []
---
## Physics / mechanism

GraphRAG denotes retrieval-augmented generation in which the retrieval substrate is a graph of entities and relations rather than a flat vector index. The supplied sources do not describe a GraphRAG pipeline, its indexing procedure or its query-time behaviour; they cover only the storage layer such a system would sit on. What follows is therefore restricted to that layer.

The one substantive source is a hardware-first graph database model called Views, from Serb's Edinburgh CEF group, published as arXiv preprint 2508.18123, submitted 25 August 2025 with a v2 revision on 13 November 2025 and carrying a header stating it is a preprint, not submitted and not peer-reviewed. Data is stored as chains of **linknodes** with the field layout `[head ID, primID1, prop1, primID2, prop2, next]`, encoding ternary source-edge-destination relationships in which properties are recursively nestable, so a property can itself carry properties via subordinate chains.

The structural claim against RDF and property graphs is that edges and destination vertices are treated as equivalent entities inside a source-centred structure, and that the linked-list organisation allows traversal to follow `next` pointers without broadcasting the whole memory. The paper specifies hardware operations rather than a schema alone, including a content-addressable read (CAR) primitive. The relevance to GraphRAG is indirect: cost per traversal step, and whether traversal can be localised in memory, set the economics of graph-structured retrieval at scale. The sources supply no measured figures on that.

## Competitive landscape

## Evidence base

## Frontier (open questions)

- What is the measured traversal latency and energy per linknode hop for the Views model on real hardware, and how does it compare with a conventional property-graph engine on the same query set?
- Has the Views preprint passed peer review, and have any of its ISA operations, including CAR, been implemented in silicon rather than simulated?
- Do graph-structured retrieval pipelines built on such a store show measurable answer-quality or cost gains over vector-index RAG on a published benchmark?
- At what graph size does the claim of traversal without whole-memory broadcast break down, and what is the memory-capacity ceiling per device?

*Synthesised 2026-08-31 from 2 KB sources by the resynth pipeline; citations are KB source slugs.*
