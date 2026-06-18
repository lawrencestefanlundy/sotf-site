---
type: concept
slug: processing-in-memory
canonical_name: Processing-in-Memory (PIM)
aliases:
- pim
- processing in memory
- near-memory-compute
kind: technology
parent_concepts:
- memory
- in-memory-computing
related_concepts:
- in-memory-computing
- memcapacitor
- sram-cim
- charge-domain-compute
- hbm
- 3d-dram
sources:
- '[[2024-yole-emerging-memories-2024]]'
frontier:
- Do the memory IDMs (SK AiM, Samsung HBM-PIM) ever ship PIM in volume, or does it stay a decade-long demo? Every generation since 2021 has been "almost productised."
- Does a hyperscaler design PIM into a shipping system, the event that would make it real — and if so does that validate or kill the startup CIM cohort?
- Where is the line between PIM (logic near memory, IDM) and CIM (the cell computes, startup) actually drawn in products, and does it blur?
last_updated: '2026-06-14'
tags:
- concept
- in-memory-compute
- pim
- memory-idm
- map
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-16-cim-landscape-2026
  title: 'Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM'
  date: '2026-06-16'
  kind: web
neighbors:
- slug: in-memory-computing
  name: In-Memory Computing
  path: /sotf-site/memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: memcapacitor
  name: Memcapacitor
  path: /sotf-site/memory/emerging-memory/memcapacitor/
  macro: memory
- slug: sram-cim
  name: SRAM Compute-in-Memory
  path: /sotf-site/memory/emerging-memory/sram-cim/
  macro: memory
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /sotf-site/compute/non-conventional/charge-domain-compute/
  macro: compute
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /sotf-site/memory/mainstream-memory/hbm/
  macro: memory
- slug: 3d-dram
  name: 3D DRAM
  path: /sotf-site/memory/mainstream-memory/3d-dram/
  macro: memory
---
## The distinction that matters: PIM vs CIM

## The memory-IDM PIM landscape (verified June 2026)

- ****Sk Hynix** — AiM (Accelerator-in-Memory).** GDDR6-AiM (claimed up to 16× AI speedup, ~80% lower power for LLMs), the AiMX accelerator card, plus LPDDR6-PIM and CXL-CMM. Positioning itself as "full-stack AI memory creator." The most product-shaped IDM PIM effort.
- ****Samsung Electronics** — HBM-PIM (Aquabolt-XL).** The PIM research leader: HBM2-PIM (32 processing units between bank pairs, ~2.5× system gain, >60% energy cut on a Xilinx accelerator), LPDDR5-PIM, and AXDIMM (DDR5 acceleration DIMM). PIM roadmap spans HBM3 / DDR5 / GDDR6 / LPDDR5.
- ****Micron Technology** — lighter on public PIM.** Focused on winning the HBM4 socket; explores 4F2 / CBA / 3D DRAM but has not pushed a branded PIM product the way the Korean two have.
- ****Upmem** — the commercial DRAM-PIM startup** (French): general-purpose processors placed in standard DRAM DIMMs. The one independent company that actually ships DRAM-PIM hardware.
- ****Neuroblade**** (Israel): "computational memory" SPU, pivoted toward data-analytics acceleration.

## The honest caveat

PIM has been "almost productised" at every Hot Chips since 2021. The binding question for the whole category — IDM PIM and startup CIM alike — is not "does it work in a demo" (it does) but "does a host system design it in at volume." No one has cleared that bar yet.
