---
type: concept
slug: deposition
canonical_name: Deposition
aliases: []
parent_concepts: []
related_concepts:
- chemical-vapor-deposition
- initiated-cvd-icvd
- powder-metallurgy
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
auto_stub: false
last_updated: '2026-07-31'
tags:
- concept
mention_count: 189
descendants:
- ald-atomic-layer-deposition
- chemical-vapor-deposition
- cvd-growth
- pvd-sputtering
sources_7d: 0
sources_30d: 14
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-22-physics-ai-comp-landscape
  title: Physics-AI / ML-surrogate simulation competitive landscape (Zenithon comp set beyond PhysicsX)
  date: '2026-06-22'
  kind: web
- slug: 2026-05-18-deposition-materials-process-market-applied-materials
  title: Applied Materials Announces Record Q2 FY2026 Results and Guides for Greater Than 30% Equipment Growth in Calendar 2026
  date: '2026-05-18'
  kind: web
- slug: 2026-05-02-initiated-cvd-overview-wiley-analytical-science-2024
  title: Initiated CVD overview (Wiley Analytical Science 2024)
  date: '2026-05-02'
  kind: web
- slug: 2026-02-22-deposition-materials-process-market-companies-that-master
  title: Companies that master AS-ALD today specifically ASM and AMAT are positioned to dominate the $15B deposition market of the late 2020s
  date: '2026-02-22'
  kind: web
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2025-07-01-a-primer-carbon-nanotubes
  title: 'A Primer: Carbon Nanotubes'
  date: '2025-07-01'
  kind: substack
- slug: 2025-03-11-deposition-materials-process-market-atlant-3d-secures-15-m
  title: ATLANT 3D Secures $15 M Series A+ as Demand Grows for its Atomic Layer Processing Technology
  date: '2025-03-11'
  kind: web
neighbors:
- slug: chemical-vapor-deposition
  name: CVD (Chemical Vapor Deposition)
  path: /manufacturing/equipment-processes/chemical-vapor-deposition/
  macro: manufacturing
- slug: initiated-cvd-icvd
  name: Initiated CVD (iCVD)
  path: /manufacturing/equipment-processes/initiated-cvd-icvd/
  macro: manufacturing
- slug: powder-metallurgy
  name: Powder Metallurgy
  path: /manufacturing/equipment-processes/powder-metallurgy/
  macro: manufacturing
---
## The three modalities, and the trade between them

Every deposition method is a different answer to one question: how do the atoms arrive?

| | [PVD](/manufacturing/equipment-processes/pvd-sputtering/) | [CVD](/manufacturing/equipment-processes/chemical-vapor-deposition/) | [ALD](/manufacturing/equipment-processes/ald-atomic-layer-deposition/) |
|---|---|---|---|
| Arrival | Atoms knocked off a target, ballistic | Gas molecules react on a hot surface | One self-limiting monolayer per cycle |
| Rate | Fast | Fast | Slow (the permanent constraint) |
| Conformality | Poor, line-of-sight | Good | Near-perfect |
| Chemistry | None: no precursor | Precursor-defined | Precursor-defined |
| Wins | Metals, seeds, barriers, specialty | Dielectrics, gap-fill, epi, bulk layers | Thin critical layers, high aspect ratios |

## Why deposition is a rising locus of value

Deposition is no longer just a step that follows patterning. GAA transistors, 3D-NAND at ever-higher aspect ratios, backside power delivery, hybrid-bonding dielectrics and the copper-to-ruthenium/molybdenum interconnect transition ([Ru / W / Co Metallisation](/manufacturing/equipment-processes/ru-w-co-metallisation/)) all multiply the number and difficulty of deposited layers per wafer.

**One correction the KB keeps on the record** (17 Jun 2026): rising intensity is not the same as being the binding constraint. "Patterning has outrun materials, so deposition is the bottleneck" is a vendor pitch, not verified market structure. The industry's binding constraints are power and grid, HBM supply, advanced packaging and liquid cooling; where deposition bites, it usually bites inside those, not standalone. See **Datacentre Compute Supply Chain Map**.

## Market structure

Semiconductor deposition equipment is ~**$22.5-25.9B** (2025) growing ~7-7.8%, up to ~$63B on the widest definitions that fold in adjacent coating industries. It is an **oligopoly, not a monopoly** (unlike ASML in scanners), which is exactly why a startup deposition tool can exist where a startup scanner cannot, and also why it tops out at specialty scale:

- **Applied Materials** ~21% of deposition overall, and effectively unchallenged in semiconductor PVD
- **Lam Research** ~18%, strongest in etch and in tungsten/molybdenum fill
- **Tokyo Electron Tel** ~16%
- **Asm International** the ALD leader (>55% share by its own 2025 reporting), in the fastest-growing sub-segment
- **Aixtron** ~70% of MOCVD for compound-semi epitaxy
- Below the tools, the consumable layer: ALD/CVD precursors ~$1.7B (2024) at ~10.4%, Merck/EMD ~30% on the advanced cut, top-5 ~58%. CMP consumables ~$3.4B, **Entegris** ~23%.
- Niche and specialty: **Veeco Instruments** in ion beam deposition (EUV mask blanks; two IBD300 systems under evaluation at leading DRAM customers into 2026), plus the European specialty tier (Evatec, Von Ardenne, Singulus).

## The deposition-tool wedge test

The reusable screen from **Deposition Materials Process Market**, because "can it outcompete AMAT/Lam?" is the wrong bar. Only two shapes work: **Wedge A**, own a process step the incumbents do not have and exit to them; **Wedge B**, own the consumable molecule. A tool failing both is a public-equity read, not a seed cheque.

## Tracked deposition companies (the three-way split)