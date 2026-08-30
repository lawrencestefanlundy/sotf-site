---
type: concept
slug: cxl
canonical_name: Compute Express Link (CXL)
aliases:
- CXL
- memory pooling
- memory disaggregation
parent_concepts:
- storage-class-memory
related_concepts:
- dram
- storage-class-memory
- computational-storage
sources:
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-07-31-positron-research-sprint]]'
frontier: []
last_updated: 2026-06-03
tags:
- concept
mention_count: 5
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-31-positron-research-sprint
  title: 'Positron AI research sprint: architecture, funding, customers, manufacturing'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
neighbors:
- slug: dram
  name: DRAM
  path: /memory/mainstream-memory/dram/
  macro: memory
- slug: storage-class-memory
  name: Storage-Class Memory
  path: /memory/emerging-memory/storage-class-memory/
  macro: memory
- slug: computational-storage
  name: Computational / Near-Storage Processing
  path: /memory/emerging-memory/computational-storage/
  macro: memory
---
Open cache-coherent interconnect standard built on PCIe physicals, whose main economic promise is **memory disaggregation**: pooling DRAM behind a switch so hosts share capacity instead of stranding it per-server. CXL 3.x adds fabric topologies and peer-to-peer sharing; CXL 3.2 is the current revision new silicon targets.

**Why the page exists now.** Q2 2026 put real capital on the *computational* variant: ****Xcena**** raised a $135M Series B for CXL 3.2 pooled DDR5 with near-data processing (thousands of embedded RISC-V cores doing KV-cache management and preprocessing on the memory tier), and Dnotitia (Seoul, ~$61M Series A, no KB page yet) is building a vector-processing unit on the same disaggregated-memory logic. Both are Korean, so the non-area's European re-open trigger is unfired, but the incumbent-capture premise now has a well-funded independent counter-example to watch. Evidence lands on the non-area's ledger; papers and standards activity tagged here join it via the graph index.
