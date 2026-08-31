---
type: concept
slug: vector-databases
canonical_name: Vector Databases
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2023-06-15-e04-no10-downing-street-and-vector]]'
- '[[2023-09-18-e15-in-conversation-with-wisear-on]]'
- '[[2023-09-28-e16-in-conversation-with-shiv-malik]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2023-09-24-e16-in-conversation-with-john-waite]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 8
frontier:
- Do standalone vector databases retain measurable recall or latency advantages over native PostgreSQL and warehouse vector indexes at production scale, and by how much?
- Does revenue for standalone vector products grow or decline in absolute terms after native vector became universal in 2026, or does the market split by workload size?
- 'Which layer captures the margin on agentic retrieval: the write path and streaming ingestion now consolidating into platform owners, or the embedding and index layer?'
- Are there retrieval workloads (multi-modal, very high dimensionality, hybrid sparse-dense) where embedded implementations fail outright rather than merely underperform?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-26-postgres-absorption-vector-layer
  title: 'Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2023-09-28-e16-in-conversation-with-shiv-malik
  title: '☎️ E17: In Conversation with Shiv Malik, CEO of Pool.io on the State of Data Unions 🤝₿'
  date: '2023-09-28'
  kind: substack
- slug: 2023-09-24-e16-in-conversation-with-john-waite
  title: '☎️ E16: In Conversation with John Waite, Co-Founder and CEO of Phycobloom and a Breakthrough Energy Fellow on the State of Biofuels and Algae Fuel 🌱⛽'
  date: '2023-09-24'
  kind: substack
- slug: 2023-09-18-e15-in-conversation-with-wisear-on
  title: '☎️ E15: In Conversation with Wisear on The State of Hearables, Brain Computer Interfaces and Augmented Reality 👂🎧🧠'
  date: '2023-09-18'
  kind: substack
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
- slug: 2023-08-31-e13-chiplets-how-chip-lego-is-driving
  title: '🔮 E13: Chiplets - How Chip Lego is Driving AI Progress'
  date: '2023-08-31'
  kind: substack
- slug: 2023-08-25-e12-nanomechanical-computing-gears
  title: '🔮E12: Nanomechanical Computing- Gears of Space War? Old Ideas at New Scales'
  date: '2023-08-25'
  kind: substack
neighbors: []
---
## Physics / mechanism

A vector database is the retrieval layer of the AI application stack: the component that stores embeddings and serves similarity search to models at inference time. The sources treat it as an enabling layer rather than a model layer, positioned alongside LLMs and the rest of the "AI stack" e04 no10 downing street and vector.

The architectural question the sources address is not indexing method but packaging. Vector search can be delivered either as a standalone specialist system or as a data type and index inside an existing transactional or analytical database. By 2026 every major cloud and platform (AWS, Azure, Google Cloud, Snowflake, Databricks) shipped native vector capability, meaning similarity search sits next to the operational data it queries rather than in a separate service postgres absorption vector layer. The consequence is that the defensible asset shifts from the retrieval index to the write path that owns the underlying records, because whoever owns ingestion controls freshness, consistency and the point at which embeddings are generated.

The commercial evidence for this shift is M&A on PostgreSQL-first companies, which is the substrate on which native vector extensions are most commonly delivered. In 2025 Snowflake and Databricks spent roughly $1.25B combined acquiring PostgreSQL-first companies: Snowflake/Crunchy Data at about $250M and Databricks/Neon at about $1B, while Supabase raised a $100M Series E postgres absorption vector layer. The same absorption logic extends upstream to streaming ingestion: IBM acquired Confluent for about $11B at $31.00 per share in cash, completed 17 March 2026, folding the Kafka-based streaming write path into watsonx as a real-time data fabric for agentic AI postgres absorption vector layer.

## Competitive landscape

The comparison the sources support is between standalone retrieval products and vector search embedded in an incumbent database or platform. The 2026 evidence points to the second: absorption is documented through completed acquisitions rather than forecast, and native vector support is universal across the major clouds and data platforms postgres absorption vector layer. That leaves standalone vector databases competing on index performance and scale against a default option that is already inside the customer's system of record. The sources do not supply recall, latency or cost benchmarks for either side, so the relative technical merits of specialist versus embedded indexes remain unquantified here.

## Evidence base

- Vector databases were treated as a core enabling layer of the AI stack in June 2023, alongside LLMs e04 no10 downing street and vector.
- In 2025 Snowflake and Databricks spent about $1.25B on PostgreSQL-first acquisitions: Crunchy Data (~$250M) and Neon (~$1B) postgres absorption vector layer.
- Supabase raised a $100M Series E, in the same PostgreSQL-first cohort postgres absorption vector layer.
- IBM's ~$11B acquisition of Confluent ($31.00/share cash) completed 17 March 2026, described as the single largest write-path absorption datapoint available postgres absorption vector layer.
- By 2026 every major cloud and data platform (AWS, Azure, Google Cloud, Snowflake, Databricks) offered native vector capability postgres absorption vector layer.

## Frontier (open questions)

- Do standalone vector databases retain measurable recall or latency advantages over native PostgreSQL and warehouse vector indexes at production scale, and by how much?
- Does revenue for standalone vector products grow or decline in absolute terms after native vector became universal in 2026, or does the market split by workload size?
- Which layer captures the margin on agentic retrieval: the write path and streaming ingestion now consolidating into platform owners, or the embedding and index layer?
- Are there retrieval workloads (multi-modal, very high dimensionality, hybrid sparse-dense) where embedded implementations fail outright rather than merely underperform?

*Synthesised 2026-08-31 from 10 KB sources by the resynth pipeline; citations are KB source slugs.*
