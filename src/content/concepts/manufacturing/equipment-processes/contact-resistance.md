---
type: concept
slug: contact-resistance
canonical_name: Contact resistance
aliases:
- silicide contact resistance
- FEOL contact resistance
parent_concepts:
- semiconductor-materials-equipment
related_concepts:
- electron-scale-metrology
- semiconductor-equipment
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2026-01-13-semianalysis-interconnects-beyond-copper]]'
- '[[2026-06-22-tim-approaches-full-sweep]]'
frontier:
- What's the current best contact resistance achieved at 2nm-node by TSMC / Intel / Samsung internally?
- How much of the 35–40% contact-resistance fraction is recoverable in production (vs theoretical)?
- Which foundry signs the first IP licence for a new contact material? When?
- Are alternative-silicide solutions (NiSi₂, CoSi₂, replacement-metal-gate variants) already addressing this internally?
last_updated: 2026-05-27
tags:
- concept
- semiconductors
- front-end-of-line
public_expressions:
- INTC
- TSM
mention_count: 22
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
- slug: 2026-01-13-semianalysis-interconnects-beyond-copper
  title: Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More
  date: '2026-01-13'
  kind: web
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
neighbors:
- slug: electron-scale-metrology
  name: Electron-scale metrology
  path: /manufacturing/equipment-processes/electron-scale-metrology/
  macro: manufacturing
- slug: semiconductor-equipment
  name: Semiconductor Equipment
  path: /manufacturing/equipment-processes/semiconductor-equipment/
  macro: manufacturing
---
The resistance at the silicon-metal interface in modern transistors — specifically where the silicon source/drain meets the metal interconnect (today, typically through a titanium silicide layer).

## Why it's growing as a problem

For a 3 kΩ device:
- ~1 kΩ from silicon itself
- ~1 kΩ from copper interconnect
- ~1 kΩ from the silicide-silicon interface — *atomically thin, the dominant remaining bottleneck*

## Theoretical ceiling

- **Ballistic transport limit** (T=0K, perfect material): ~1000× lower than current production
- **Practical limit** (room temperature, realistic mobility): ~50–100× lower
- **Conservative pitch** (half the current value): ~2× improvement, translating to ~15–20% device-level performance unlock

## Why it persists

Titanium silicide has been the industry default for ~50 years. Alternative silicides (NiSi₂, CoSi₂) have been explored but selection has been driven by atomic-scale stability, thermal budget, and yield — not by electron-band-structure matching. The fundamental energy-barrier mismatch between silicon and silicide hasn't been systematically addressed because the metrology to measure it directly ([Electron-scale metrology](/manufacturing/equipment-processes/electron-scale-metrology/)) hasn't existed in semiconductor toolchains.

## Active approaches