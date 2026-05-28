---
type: concept
slug: eda-design-tools
canonical_name: EDA & Design Tools
aliases: []
kind: technology
parent_concepts:
- manufacturing
- foundry-design
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 25
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-05-20-imec-ceo-calls-for-stronger-ai-design-push-in-eus-chips-act-
  title: Imec CEO calls for stronger AI design push in EU's Chips Act - ET Telecom
  date: '2026-05-20'
  kind: web
neighbors: []
---
## Physics / mechanism

Electronic Design Automation encompasses the software stack that converts circuit intent into manufacturable geometry. At the transistor level, SPICE-derived solvers model device physics (IV curves, parasitics, noise) against PDK-supplied foundry models. At the physical level, place-and-route engines minimize wirelength and timing slack under DRC constraints encoded in technology files. Modern signoff flows close multiple corners simultaneously: timing (STA), power (IR drop, EM), signal integrity, and DFM. State-of-the-art tools now embed ML-assisted prediction (Synopsys DSO.ai, Cadence Cerebrus) to navigate the optimization space faster than classical engines. Key metrics: PPA (power, performance, area), closure time, and PDK coverage across nodes from 3 nm to mature 180 nm geometries.

## Competitive landscape

---

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
