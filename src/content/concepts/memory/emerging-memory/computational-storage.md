---
type: concept
slug: computational-storage
canonical_name: Computational / Near-Storage Processing
aliases:
- computational storage
- near-storage compute
- CSD
parent_concepts:
- storage-class-memory
related_concepts:
- nand-flash
- cxl
- storage-class-memory
sources: []
frontier:
- ''
last_updated: 2026-06-03
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: nand-flash
  name: NAND Flash
  path: /sotf-site/memory/mainstream-memory/nand-flash/
  macro: memory
- slug: cxl
  name: Compute Express Link (CXL)
  path: /sotf-site/memory/emerging-memory/cxl/
  macro: memory
- slug: storage-class-memory
  name: Storage-Class Memory
  path: /sotf-site/memory/emerging-memory/storage-class-memory/
  macro: memory
---
Pushing compute (filtering, search, compression) into or next to the SSD to cut data movement. Commercially a commodity NAND drive plus an FPGA/ARM controller (ScaleFlux, Pliops, NGD, Enfabrica) — a module/system layer whose value-capture is weak for a deep-tech device fund.

*Concept stub created 2026-06-03 from the semi+photonics gap-map research (segment backfill).*

## Merged from root duplicate (computational-storage.md at concepts/ root, 2026-06-10)

# Computational Storage

Pushing compute into the storage device (SSD controller or an attached accelerator) so filtering, search and decompression run next to the data instead of across the bus. Targets data-movement-bound workloads; one lane in the memory/storage-disaggregation map.
