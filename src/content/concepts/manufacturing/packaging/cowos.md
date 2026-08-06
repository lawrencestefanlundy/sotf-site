---
type: concept
slug: cowos
canonical_name: CoWoS (TSMC)
aliases: []
kind: technology
parent_concepts:
- manufacturing
- packaging
related_concepts: []
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2026-03-26-sotf-interview-dorian-haci-mintneuro]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-05-consensus-capital]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 933
last_reorg_date: '2026-05-13'
sources_7d: 4
sources_30d: 8
recent_mentions:
- slug: 2026-07-31-etched-research-sprint
  title: Etched research sprint — tape-out speed, HBM supply, customer orders (4-lane web sweep)
  date: '2026-07-31'
  kind: web
- slug: 2026-07-31-inference-silicon-roster-sprint
  title: 'Inference-silicon roster verification sprint: 10 companies for the competitive-analysis capital map'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-10-inference-silicon-deep-research
  title: 'Deep research: measured vs claimed inference-silicon economics (adversarially verified, 23/25 claims confirmed)'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-09-in-die-microfluidic-cooling-sprint
  title: In-die microfluidic cooling — cluster research sprint
  date: '2026-07-09'
  kind: web
- slug: 2026-07-05-semianalysis-kyber-nvl144-delayed-2028
  title: 'SemiAnalysis: NVIDIA Kyber NVL144 delayed >12 months to 2028; NVL72x2 cancelled'
  date: '2026-07-05'
  kind: web
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-07-01-sensifai-memo-streaming-physical-ai
  title: SensifAI — Purpose-Built Silicon for Streaming Physical AI (funding memo)
  date: '2026-07-01'
  kind: web
neighbors: []
---
## Physics / mechanism

CoWoS (Chip-on-Wafer-on-Substrate) is TSMC's mature 2.5D advanced packaging platform. A silicon interposer (passive or active) is fabricated on a standard wafer, then known-good dies—logic, HBM, SerDes chiplets—are flip-chip bonded onto it before dicing and substrate attachment. The interposer provides ultra-fine RDL wiring (≤0.4 µm line/space in CoWoS-S) and microbumps at ~40–55 µm pitch, enabling die-to-die bandwidth densities impossible on organic substrates. HBM3/3E stacks connected via CoWoS deliver ~1.2 TB/s per stack. Interposer sizes have scaled to ~120 mm × 120 mm (reticle-stitched) to accommodate multi-chiplet AI accelerators. CoWoS-R replaces the passive Si interposer with an RDL-only interposer; CoWoS-L embeds a bridge die for heterogeneous integration. TSMC's CoWoS capacity was ~13,000 wspm in 2023, scaling aggressively under AI demand pressure.

## Competitive landscape

| Platform | Interposer type | Bump pitch | Key user |
|---|---|---|---|
| CoWoS-S | Passive Si | ~40 µm | NVIDIA H/B series |
| Intel EMIB | Si bridge embedded in organic | ~55 µm | Intel Ponte Vecchio |
| ASE/Amkor FOCoS | Fan-out RDL | ~100–130 µm | Broader merchant |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
