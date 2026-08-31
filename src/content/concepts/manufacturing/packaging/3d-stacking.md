---
type: concept
slug: 3d-stacking
canonical_name: 3d Stacking
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2024-yole-emerging-memories-2024]]'
- '[[2026-01-13-semianalysis-interconnects-beyond-copper]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 23
frontier:
- At what layer count does the die-cost minimum actually fall for current multi-deck processes, and has deck-splitting moved that minimum relative to Walker's 2013 model, or merely deferred it walker 2013 rigorous 3d nand flash cost analysis?
- Does the ~30%-steps-for-~44%-density ratio at 321 layers hold, degrade or improve at the next deck addition 2026 01 13 semianalysis interconnects beyond copper?
- Has any lithography-intensive layered 3D memory been demonstrated in volume at lower cost per bit than vertical-channel NAND, as Walker's model predicts is possible?
- Can NOR-type stacked arrays suppress sneak current enough to preserve sensing margin at full monolithic 3D layer counts, rather than only at the single-layer or few-layer BEOL level 2026 06 05 dtco of nor type igzo fefets for 3d heterogeneous ai memorie?
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-01-13-semianalysis-interconnects-beyond-copper
  title: Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More
  date: '2026-01-13'
  kind: web
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
- slug: 2023-08-31-e13-chiplets-how-chip-lego-is-driving
  title: '🔮 E13: Chiplets - How Chip Lego is Driving AI Progress'
  date: '2023-08-31'
  kind: substack
neighbors: []
---
## Physics / mechanism

3D stacking builds device layers vertically rather than shrinking features laterally, so density scales with deck count instead of lithographic pitch. In memory this splits into two families: vertical-channel schemes such as BiCS, p-BiCS and TCAT, where a single deep etch defines strings running through many stacked layers, and lithography-intensive layered schemes, where each device layer is patterned individually **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.

The governing physical constraint on vertical-channel stacking is etch taper. Any deep etch has a non-zero taper angle θ, so holes and slits are wider at the top of the stack than at the bottom. Because the array footprint is set by the cell pitch at the *top* of the stack, adding layers widens the top-side pitch and inflates die area. The consequence is that die cost per bit does not fall monotonically with layer count: there is a minimum, beyond which each additional layer raises cost. A layered approach using three critical masks per device layer can reach a smaller die and undercut vertical-channel stacking on total cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.

Production stacking now proceeds in decks rather than a single continuous etch. SK Hynix's 321-layer V9 NAND adds a third processing deck, buying roughly 44% higher density for roughly 30% more process steps semianalysis interconnects beyond copper. This step-count-versus-density trade is the industrial form of Walker's cost minimum.

Beyond NAND, 3D stacking spans on-chip back-end-of-line (BEOL) memory, hybrid-bonded memory chiplets, and monolithically integrated 3D arrays. IGZO-channel FeFETs have been evaluated across all three tiers, with NOR-type bitcells projected down to about 0.016 µm² (10-A SRAM-equivalent area) at 7-nm ground rules while holding sub-5 ns random access latency; the limiting factor in NOR arrays is sensing margin loss from sneak current dtco of nor type igzo fefets for 3d heterogeneous ai memorie. Ferroelectric non-volatile capacitance devices are also framed as having 3D stacking potential via non-destructive readout, constrained by a memory window of 1-10 fF/µm defect aware physics based compact model for ferroelectric n.

## Competitive landscape

| Approach | Density lever | Binding constraint (per sources) |
|---|---|---|
| Vertical-channel 3D NAND (BiCS, p-BiCS, TCAT) | Layers per deep etch | Etch taper θ widens top-of-stack pitch; die cost has a minimum vs layer count **Walker 2013 Rigorous 3D Nand Flash Cost Analysis** |
| Lithography-intensive layered 3D | Independently patterned device layers | Three critical masks per layer, but smaller die and lower total cost in Walker's model **Walker 2013 Rigorous 3D Nand Flash Cost Analysis** |
| Multi-deck NAND (e.g. 321-layer V9) | Additional processing decks | ~30% more process steps for ~44% density semianalysis interconnects beyond copper |
| BEOL / monolithic 3D emerging memory | Layers above logic | Writability, sneak-current sensing margin dtco of nor type igzo fefets for 3d heterogeneous ai memorie |
| Hybrid-bonded memory chiplets | Die-to-die bonding | Assessed alongside BEOL RAM in the same DTCO frame dtco of nor type igzo fefets for 3d heterogeneous ai memorie |

3D stacking also functions as a life-extension mechanism for incumbent nodes rather than only a leading-edge technique: eFlash is projected to retain more than 50% of embedded non-volatile memory units at 40 nm and above via 3D stacking **2024 Yole Emerging Memories 2024**. On the logic and system side, chiplets pursue modularity by decomposing monolithic dies into smaller connected pieces e13 chiplets how chip lego is driving, and HBM applies stacking to the memory-bandwidth bottleneck in AI systems e14 the real ai bottleneck high bandwidth.

## Evidence base

- Walker's cost model shows 3D NAND die cost per bit reaches a minimum and then rises with each additional device layer, contradicting the monotonic-decline premise on which vertical-channel 3D NAND was sold **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.
- The same analysis identifies non-zero etch taper angle θ as the mechanism: top-of-stack cell pitch defines the memory array footprint **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.
- SK Hynix's 321-layer V9 3D NAND adds a third processing deck for approximately 44% higher density at approximately 30% more process steps semianalysis interconnects beyond copper.
- NOR-type IGZO FeFETs are projected to reach ~0.016 µm² bitcell area at 7-nm ground rules with sub-5 ns random access latency, across BEOL RAM, hybrid-bonded chiplet and monolithic 3D FeNOR storage-class memory tiers dtco of nor type igzo fefets for 3d heterogeneous ai memorie.
- Ferroelectric non-volatile capacitance memories are described as having 3D stacking potential, with memory window limited to 1-10 fF/µm and requiring material-device-circuit co-optimisation defect aware physics based compact model for ferroelectric n.
- Yole projects eFlash retaining over 50% of embedded non-volatile memory at 40 nm and above through 3D stacking **2024 Yole Emerging Memories 2024**.
- NSF awarded $366,820 (Award 2543547, 13 May 2026) to Haitong Li at Purdue for neuro-symbolic computing built on advanced three-dimensional integration nsf 2543547 career efficient and scalable neuro symb.

## Frontier (open questions)

- At what layer count does the die-cost minimum actually fall for current multi-deck processes, and has deck-splitting moved that minimum relative to Walker's 2013 model, or merely deferred it **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**?
- Does the ~30%-steps-for-~44%-density ratio at 321 layers hold, degrade or improve at the next deck addition semianalysis interconnects beyond copper?
- Has any lithography-intensive layered 3D memory been demonstrated in volume at lower cost per bit than vertical-channel NAND, as Walker's model predicts is possible?
- Can NOR-type stacked arrays suppress sneak current enough to preserve sensing margin at full monolithic 3D layer counts, rather than only at the single-layer or few-layer BEOL level dtco of nor type igzo fefets for 3d heterogeneous ai memorie?

*Synthesised 2026-08-31 from 11 KB sources by the resynth pipeline; citations are KB source slugs.*
