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
- At what scale, filter selectivity and write-churn rate does a purpose-built vector engine measurably beat pgvector/pgvectorscale or warehouse-native vector search on recall, tail latency and total cost? No supplied source contains this comparison.
- What share of the ~$3.73B 2026 vector database market is standalone vendor revenue versus vector features bundled into cloud and data platform contracts?
- Do agentic workloads change the retrieval access pattern enough (long-lived memory, high update rates, per-agent isolation) to re-open a specialist opportunity that RAG alone did not sustain?
- Does the write-path absorption pattern continue after the IBM/Confluent close, or was 2025-26 a one-off consolidation window driven by cheap targets?
- Do standalone vector databases retain measurable recall or latency advantages over native PostgreSQL and warehouse vector indexes at production scale, and by how much?
- Does revenue for standalone vector products grow or decline in absolute terms after native vector became universal in 2026, or does the market split by workload size?
- 'Which layer captures the margin on agentic retrieval: the write path and streaming ingestion now consolidating into platform owners, or the embedding and index layer?'
- Are there retrieval workloads (multi-modal, very high dimensionality, hybrid sparse-dense) where embedded implementations fail outright rather than merely underperform?
scorecard:
  viability: 4
  drivers: 4
  novelty: null
  diffusion: 5
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Overrated
scorecard_status: draft
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
**Vector databases store high-dimensional embeddings and retrieve them by similarity rather than exact match, making them the retrieval substrate for RAG and agent memory; the capability is now proven and ubiquitous, but by 2026 it ships natively inside every major cloud and data platform, which is a problem for the standalone category rather than for the technology.**

## Summary

A vector database stores items as embeddings: fixed-length numeric vectors produced by a model, where semantic similarity corresponds to geometric proximity. Instead of a query returning rows matching an exact predicate, it returns the *k* nearest vectors under a distance metric. Because exhaustive comparison across hundreds of millions of vectors is too slow, these systems rely on approximate nearest-neighbour index structures that trade a controlled amount of recall for large speed gains, plus filtering to combine similarity search with ordinary metadata predicates. This is the retrieval half of retrieval-augmented generation, and the persistence layer behind most agent memory designs.

The technology entered the deep-tech conversation early in the current AI cycle as the missing enabling layer of the AI stack <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e04-no10-downing-street-and-vector" title="🔮 E04: No10 Downing Street and Vector Databases (titles you never expect)" rel="noopener">ref</a></sup>. The interesting question in 2026 is no longer whether similarity search works, but where it lives. By 2026 every major cloud and platform (AWS, Azure, Google Cloud, Snowflake, Databricks) shipped native vector search, and PostgreSQL carries the pgvector and pgvectorscale extensions <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. A capability that was a product category in 2023 is a feature checkbox on the incumbent write path in 2026.

The parameters that decide the outcome are therefore commercial rather than algorithmic. First, whether workloads are large or specialised enough that a purpose-built engine beats a bolt-on extension on cost, recall and latency at scale. Second, whether the operational simplicity of keeping vectors next to transactional data (one system, one consistency model, no dual-write) outweighs any such advantage for the median application. Third, whether the owners of the write path buy rather than build: in 2025 Snowflake and Databricks spent roughly $1.25B acquiring PostgreSQL-first companies (Snowflake/Crunchy Data ~$250M, Databricks/Neon ~$1B), Supabase raised a $100M Series E, and IBM acquired Confluent for about $11B at $31.00 per share cash, completing 17 March 2026 and folding the Kafka streaming write path into watsonx as a real-time data fabric for agentic AI <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>.

The tension is that the standalone layer is still growing while being absorbed. The vector database market is put at about $3.73B in 2026 growing at roughly 23.5% CAGR, with an alternative series of about $2.7B in 2025 rising to about $8.9B in 2030 <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. Growth of the category and commoditisation of the capability are happening simultaneously, which is exactly the pattern that separates a durable infrastructure business from a feature.

## Viability (4/5)

Viability here is close to settled by deployment evidence. By 2026 AWS, Azure, Google Cloud, Snowflake and Databricks all offer native vector search, and PostgreSQL supports it through pgvector and pgvectorscale <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. Platforms of that size do not add a retrieval primitive to general availability unless it is operationally stable and there is customer pull. A market of roughly $3.73B in 2026 is revenue from working systems, not pilots <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>.

The reservation, and the reason this is not a 5, is that the sources contain no performance evidence at all: no recall-versus-latency curves, no cost per billion vectors, no comparison of a bolt-on extension against a purpose-built engine under filtered search or high write churn. Those are precisely the conditions under which vector retrieval is known to be hard, and the supplied material is silent on them. The judgement is that the category works, not that any particular architecture is proven best.

**TLDR: The capability is shipping in production across every major data platform; the sources show deployment, not benchmarks.**

## Drivers (4/5)

On demand, the pull is the AI application stack: the technology was framed from the start as the enabling retrieval layer for LLM applications <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e04-no10-downing-street-and-vector" title="🔮 E04: No10 Downing Street and Vector Databases (titles you never expect)" rel="noopener">ref</a></sup>, and by 2026 the framing has moved to agentic AI, with IBM positioning its ~$11B Confluent acquisition (completed 17 March 2026) as a real-time data fabric for agentic AI inside watsonx <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. The reported ~23.5% CAGR on a ~$3.73B 2026 base, and the alternative ~$2.7B (2025) to ~$8.9B (2030) series, both describe sustained demand growth <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>.

On supply, the driver cuts against standalone vendors. Native vector search across every hyperscaler and data platform, plus pgvector in the default open-source relational database, means the marginal cost of acquiring the capability for most teams is close to zero and involves no new vendor, no new failure domain and no dual-write pipeline <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. Capital is also flowing to the write path rather than the read path: roughly $1.25B of PostgreSQL-first M&A in 2025 and a $100M Supabase Series E <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. Strong demand for the function, weak structural support for the standalone product.

**TLDR: Demand is pulled by RAG and agentic workloads; supply is now free with the database you already run.**

## Novelty (unscored)

The central novelty question for this concept is narrow and empirical: at what scale, filter selectivity and update rate does a purpose-built vector engine beat pgvector, pgvectorscale or a warehouse-native index, and by what factor on recall, tail latency and cost? None of the supplied sources report a single benchmark, index-build time, recall figure or cost comparison. They establish that both options exist and that the extension route is now universally available <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>, which hints at commoditisation but does not measure it.

An absorption pattern is circumstantial evidence that the differentiation is not large enough to sustain independence, but circumstantial is the right word: platforms also acquire capabilities that are genuinely hard. Scoring this dimension on that inference alone would be guesswork, so it is left null. Anyone underwriting a standalone vector database should treat obtaining that comparison as the first piece of diligence.

**TLDR: The sources contain no comparative performance data, so there is no defensible view on how much better a dedicated engine is than an extension.**

## Diffusion (5/5)

Diffusion is the strongest dimension. The capability is available by default to anyone running PostgreSQL, and natively inside AWS, Azure, Google Cloud, Snowflake and Databricks as of 2026 <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. There is no hardware dependency, no regulatory gate, no new skill set beyond choosing an embedding model, and no procurement step for the majority of teams because the vector index is a feature of a system they already run and already trust with their transactional data.

The barriers that remain are commercial and architectural rather than adoption barriers in the usual sense. A standalone vector store must justify a second system, a synchronisation path from the source of truth, and a separate consistency and backup story, against an incumbent that offers 'good enough' retrieval in the same transaction. That is a switching-cost argument that runs against the newcomer. Note also the data-gravity thesis that value migrates away from standalone retrieval towards whoever owns the write path, of which the 2025-26 M&A is presented as direct evidence <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>.

**TLDR: Adoption is essentially complete at the platform layer; the barrier is not adoption but who captures it.**

## Impact (3/5)

By value captured in the named layer, the impact is moderate. The vector database market is put at about $3.73B in 2026, with a path to roughly $8.9B by 2030 on the alternative series <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. Set against an ~$11B single acquisition on the streaming write path <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>, the retrieval layer is not where the large numbers sit, and the growth it does show is being competed for by platform incumbents rather than reserved for specialists.

By function, the impact is larger than the revenue line suggests. Similarity retrieval is the mechanism that lets a fixed-weight model use private, current data, and it was identified as a core enabling piece of the AI stack early in the cycle <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e04-no10-downing-street-and-vector" title="🔮 E04: No10 Downing Street and Vector Databases (titles you never expect)" rel="noopener">ref</a></sup>. Agentic systems make it more load-bearing still, since memory and tool grounding both route through retrieval <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. A technology can be indispensable and still be a feature: that is the position here, and a 3 reflects the gap between systemic importance and capturable value.

**TLDR: Functionally load-bearing for RAG and agent memory, but the measurable standalone market is small relative to the platforms absorbing it.**

## Timing Now (0-2yr)

There is no future readiness date to wait for. Native vector search is present in every major cloud and data platform as of 2026, and pgvector/pgvectorscale put it in the default open-source relational database <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. Revenue of roughly $3.73B in 2026 confirms production use today <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>.

What is still in play on a two-to-five year horizon is consolidation. The 2025 PostgreSQL-first M&A of roughly $1.25B and the IBM/Confluent close on 17 March 2026 are the visible early moves in write-path owners buying the read path <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. If the pattern continues, the standalone category resolves into a small number of specialist survivors serving the largest or most latency-sensitive workloads, with the rest absorbed. Investors should treat the technology decision as made and the ownership decision as the live one.

**TLDR: Already deployed at platform scale; the open question is market structure over the next two to four years, not technical readiness.**

## Overrated or underrated? Overrated

As a technology, vector retrieval is real, deployed and load-bearing. As an independent product category, it is overrated, and the 2026 evidence is unusually clean because it is completed M&A rather than forecast. Every major cloud and data platform now ships vector search natively, PostgreSQL has it via extension, and roughly $1.25B was spent in 2025 by Snowflake and Databricks acquiring PostgreSQL-first companies, with IBM paying about $11B for Confluent and closing on 17 March 2026 <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. Buyers who own the write path are assembling the read path around it, and the default architecture for a new application is now 'vectors in the database you already have'.

The counter-case is the growth: a ~$3.73B 2026 market compounding at ~23.5% is not a category dying <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>. Both things can be true. The category grows because AI applications grow, while the fraction of that growth reaching standalone vendors shrinks. The honest caveat is that the supplied sources contain no performance comparison between dedicated engines and extensions, so if a large and durable performance gap exists at the top end of scale, the specialist tier survives on merit. On the evidence available, that is a hypothesis rather than a demonstrated fact, and the burden of proof sits with the standalone vendor.

## Prediction

By 31 December 2028, at least one leading standalone vector database vendor will have been acquired by a write-path owner (a hyperscaler, data warehouse, streaming or PostgreSQL platform company) rather than remaining independent or listing publicly.

## Evidence base

- By 2026 every major cloud and platform (AWS, Azure, Google Cloud, Snowflake, Databricks) shipped native vector search, and PostgreSQL carries pgvector and pgvectorscale <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>.
- In 2025 Snowflake and Databricks spent roughly $1.25B acquiring PostgreSQL-first companies: Snowflake/Crunchy Data at about $250M and Databricks/Neon at about $1B <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>.
- IBM acquired Confluent for about $11B ($31.00 per share, cash), completed 17 March 2026, folding the Kafka-based streaming write path into watsonx as a real-time data fabric for agentic AI <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>.
- The vector database market is put at about $3.73B in 2026 growing at roughly 23.5% CAGR, with an alternative series of about $2.7B in 2025 rising to about $8.9B in 2030 <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>.
- Supabase raised a $100M Series E, further capitalising the PostgreSQL write-path layer rather than standalone retrieval <sup class="ref"><a href="https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026" title="Write-path owners absorb the retrieval layer: $1.25B of PostgreSQL-first M&A, native vector everywhere" rel="noopener">ref</a></sup>.
- Vector databases were identified as an enabling layer of the AI stack as early as June 2023, at the start of the current cycle <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e04-no10-downing-street-and-vector" title="🔮 E04: No10 Downing Street and Vector Databases (titles you never expect)" rel="noopener">ref</a></sup>.

## Open questions

- At what scale, filter selectivity and write-churn rate does a purpose-built vector engine measurably beat pgvector/pgvectorscale or warehouse-native vector search on recall, tail latency and total cost? No supplied source contains this comparison.
- What share of the ~$3.73B 2026 vector database market is standalone vendor revenue versus vector features bundled into cloud and data platform contracts?
- Do agentic workloads change the retrieval access pattern enough (long-lived memory, high update rates, per-agent isolation) to re-open a specialist opportunity that RAG alone did not sustain?
- Does the write-path absorption pattern continue after the IBM/Confluent close, or was 2025-26 a one-off consolidation window driven by cheap targets?

---
*Assessment drafted 2026-08-31 from up to 10 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
