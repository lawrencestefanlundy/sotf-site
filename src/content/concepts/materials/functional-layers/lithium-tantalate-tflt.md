---
type: concept
slug: lithium-tantalate-tflt
canonical_name: Thin-Film Lithium Tantalate (TFLT)
aliases:
- LiTaO3
- lithium tantalate
- TFLT
- thin-film lithium tantalate
kind: technology
parent_concepts:
- materials
- functional-layers
related_concepts:
- lithium-niobate-tfln
- electro-optic-modulators
- piezoelectric
sources: []
frontier:
- Does TFLT's better thermal stability (vs TFLN) drive adoption in high-power or wide-temperature-range applications?
- Smart-Cut process maturity — does TFLT-on-insulator wafer supply scale alongside TFLN-on-insulator (Soitec)?
- Does any commercial foundry (Lightium, GF Fotonix) add TFLT as a module — or does TFLN's first-mover advantage block adoption?
- Pyroelectric noise — TFLT has pyroelectric tail that adds modulator drift; does packaging compensation solve this at production scale?
last_updated: 2026-05-08
tags:
- concept
- photonics
- lithium-tantalate
- electro-optic
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: lithium-niobate-tfln
  name: Lithium Niobate (TFLN)
  path: /sotf-site/materials/functional-layers/lithium-niobate-tfln/
  macro: materials
- slug: piezoelectric
  name: Piezoelectric
  path: /sotf-site/materials/functional-layers/piezoelectric/
  macro: materials
---
*TFLN cousin with better thermal + lower-cost wafer supply*

## Physics / mechanism

LiTaO₃ is a ferroelectric crystal closely related to LiNbO₃ — same family, slightly different optical and piezoelectric properties. Pockels coefficient ~26 pm/V (vs LiNbO₃'s 32 pm/V). Lower pyroelectric coefficient and better thermal stability, but slightly higher loss.

In thin-film form (TFLT-on-insulator), it competes directly with TFLN. The pitch is: marginally better thermal stability + cheaper wafer supply (smaller specialty crystal-growth ecosystem but Soitec-style smart-cut maturing) + lower regulatory risk than lead-based alternatives.

## Competitive landscape

Research stage commercially. Several universities and small companies in China and the US working on TFLT modulators. Soitec has published TFLT-on-insulator wafer development. As of 2026, no commercial photonic foundry has TFLT in its PDK.

## Frontier (open questions)

See frontmatter `frontier:` block.
