---
type: concept
slug: 3d-dram
canonical_name: 3D DRAM
aliases:
- vertical dram
- 4f2 dram
- cba dram
- vertical-channel-transistor
kind: technology
parent_concepts:
- memory
related_concepts:
- hbm
- 3d-monolithic-integration
- processing-in-memory
- memcapacitor
- chiplets-architecture-share
frontier:
- Which vertical-DRAM cell architecture wins (4F2 / vertical-channel-transistor / CBA-stacked), and which IDM gets to volume first (~2030)?
- Does true 3D DRAM arrive before the HBM scarcity window closes, or does HBM + hybrid bonding carry the load through the decade?
- Does monolithic-3D startup memory (Vertical Compute) or compute-in-memory (SEMRON) reach the socket before the IDMs ship 3D DRAM?
last_updated: '2026-06-14'
tags:
- concept
- memory
- 3d
- map
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /sotf-site/memory/mainstream-memory/hbm/
  macro: memory
- slug: 3d-monolithic-integration
  name: 3D Monolithic Integration
  path: /sotf-site/compute/compute-architecture/3d-monolithic-integration/
  macro: compute
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /sotf-site/memory/emerging-memory/processing-in-memory/
  macro: memory
- slug: memcapacitor
  name: Memcapacitor
  path: /sotf-site/memory/emerging-memory/memcapacitor/
  macro: memory
---
The "3D stacking of memory" map. DRAM has stayed essentially 2D while NAND went vertical a decade ago; closing that gap is the memory industry's defining roadmap of the late 2020s, and it sits directly under the **Hbm Bottleneck** and **Hbm Free Inference Architectures** theses. Four distinct things get called "3D memory" — keep them separate.

## The four layers of "3D memory"

## Who has what (verified June 2026)

- ****Samsung Electronics**** — 3D DRAM R&D leader; VCT / 4F2 roadmap toward ~2030; also the PIM leader ([Processing-in-Memory (PIM)](/sotf-site/memory/emerging-memory/processing-in-memory/)).
- ****Sk Hynix**** — HBM leader carrying the volume; HBM4E now, HBM5 / DDR6 from ~2029; 3D DRAM in research.
- ****Micron Technology**** — HBM4 (1ß process, six customers); 4F2 / CBA + 3D DRAM exploration.
- ****Cxmt**** (China) — 4th-largest DRAM by capacity; HBM2E mass production H1 2026, HBM3 2026, HBM3E 2027 (≈3–4 yrs behind); 3D DRAM ambitions. The sovereignty wildcard (see **Sovereignty Semi Bifurcation**).
- ****Winbond**** (Taiwan) — **CUBE** custom ultra-bandwidth DRAM, 3D-stackable, aimed squarely at **edge AI** (256Mb–8Gb/die, 20nm→16nm). The tier-2 edge-AI memory play.
- ****Nanya**** (Taiwan) — custom edge-AI HBM via an NT$500M JV with Etron; products targeted end-2026.