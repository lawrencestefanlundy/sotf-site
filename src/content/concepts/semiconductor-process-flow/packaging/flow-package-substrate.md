---
type: concept
slug: flow-package-substrate
canonical_name: Package substrate manufacturing (ABF / glass) (process step)
seq: 46
phase: assembly
related_concepts:
- substrate-bt-abf
- glass-interposers
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 7
parent_concepts:
- packaging
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors:
- slug: substrate-bt-abf
  name: BT / ABF Substrates
  path: /manufacturing/packaging/substrate-bt-abf/
  macro: manufacturing
- slug: glass-interposers
  name: Glass Interposers
  path: /manufacturing/packaging/glass-interposers/
  macro: manufacturing
---
> Step 46 of 56 in the semiconductor flow (Assembly). Prev: [Flip-chip bumping (C4 / Cu pillar / microbump) (process step)](/semiconductor-process-flow/packaging/flow-flip-chip-bumping/) · Next: [Lead frame manufacturing (process step)](/semiconductor-process-flow/packaging/flow-leadframe/)

## What this step does
The package substrate is the laminated multilayer board the bumped die sits on; it fans the die's micron-pitch bumps out to the millimetre-pitch solder balls that meet the motherboard, and carries power and signal between them. High-end logic (CPUs, GPUs, AI accelerators) uses flip-chip BGA (FC-BGA) substrates built by laminating dielectric build-up layers around a rigid core. Sub-processes inside the step:
- Core fabrication: drill and plate a rigid core (organic glass-fibre/BT laminate today; a thin glass panel in the emerging glass-core route).
- Build-up: laminate Ajinomoto Build-up Film (ABF) dielectric, then laser-drill microvias, copper-plate, and pattern fine lines, repeated layer by layer (often 10-20+ layers).
- Surface finish, solder-mask, ball-attach, electrical test and optical/X-ray inspection before the substrate ships to OSAT/assembly.

## Where it sits and why it matters
This is the most supply-constrained, highest-margin link in the back-end. The substrate, not the die, has been the gating bottleneck for AI accelerators: lead times for 14-layer ABF substrates stretched to ~28 weeks in early 2025 as demand outran supply by double-digit percentage points [5]. Substrate area and layer count scale with chiplet count, so every move to bigger reticle-limited packages (and 2.5D/3D stacks) pulls more substrate and far more ABF. It matters economically because value concentrates twice: a handful of Asian substrate makers hold the manufacturing, and a single Japanese chemical company (Ajinomoto) holds >95% of the dielectric they all build on [4].

## Equipment market
There is no single "substrate tool" market; spend is spread across laser drilling, panel lithography, plating, lamination and inspection lines, and the glass-core route is creating a brand-new toolset. The advanced IC substrate market overall (the substrates themselves, not the tools) was ~$16.6bn in 2024 growing ~9% CAGR to 2029, reaching ~$31bn by 2030 on AI/HPC and glass core [1][6]. Equipment is a fraction of that, lumpy with capacity builds. Vendors below are the value-capturing tool layer.

| Vendor | HQ | Est. share | Notable |
|--------|----|-----------|---------|
| Onto Innovation | US | Leader in panel litho + inspection | JetStep X500 stepper (sub-2um), Firefly G3 / PrimaScan inspection [3] |
| LPKF | Germany | Pioneer in glass via formation | LIDE laser modification for through-glass vias; Onto partnership Apr 2025 [3] |
| SCHMID Group | Germany | Glass wet-etch + panel plating | InfinityLine TGV etch + panel-level electroplating [3] |
| Disco | Japan | Singulation / thinning | Blade dicing of substrate/glass panels [3] |
| Philoptics / E&R | Korea / Taiwan | Challengers in TGV laser | Glass via drilling alternatives to LPKF [3] |

Concentration note: organic-substrate tooling is mature and fragmented (laser drillers, platers, AOI from many suppliers). The interesting concentration is in glass-core, where the new TGV + panel-litho + panel-plating line is forming around a small set (LPKF, Onto, SCHMID, TRUMPF) before any volume market exists [3]. Treat these as positions, not hard shares.

## Materials & consumables
This step's defining consumable is ABF dielectric film, plus copper foil/plating chemistry, the organic core laminate (BT resin), solder mask, and the glass core in the new route. ABF is the chokepoint: Ajinomoto holds >95% of the build-up film used in CPU/GPU substrates [4]. Ajinomoto's electronic-materials segment did ~JPY 100.7bn revenue (FY ending early 2026), up ~31%, at a >50% operating margin [4][7]. This is recurring, per-substrate consumption that scales directly with layer count and package area, so AI's appetite for bigger substrates compounds straight into ABF volume. The glass-core route swaps the organic core for thin glass panels (Corning-class glass, plus Sumitomo Chemical's JV with Samsung Electro for core glass material [2]), creating a parallel materials supply chain.

## Volumes, revenue, profitability
The revenue pool sits in the substrate itself: ~$16.6bn (2024) heading to ~$31bn (2030) for advanced IC substrates, of which FC-BGA for AI/HPC is the fast-growing core [1][6]. A single AI-accelerator substrate can carry 16-20+ build-up layers and cost orders of magnitude more than a commodity substrate, so dollar growth outruns unit growth. Margins differ sharply by layer: substrate makers (Unimicron, Ibiden, Shinko) run cyclical board-economics, mid-teens to ~20%+ operating margins in up-cycles on the highest-end FC-BGA; the ABF materials layer (Ajinomoto) earns a near-monopoly >50% operating margin [4][7]. Who earns the margin: the chemical monopoly (Ajinomoto) per-unit, the top substrate makers on capacity scarcity, and the equipment vendors on each capacity build.

## Market drivers, constraints & trends
Net read: accelerating into a multi-year up-cycle. ABF substrates re-entered shortage in H1 2026 and the served pool (substrate makers' capex plus per-unit ABF) is forecast to widen its supply gap through 2027-2028 [9][11].

- **Drivers**
  - AI accelerator packages are climbing from 3+3 to 11+11 and toward 13+13 build-up layers, so substrate area and ABF volume per chip rise simultaneously, not linearly [9]. AI-packaging demand is forecast at ~30% annual growth over the next two years [12].
  - Capex is committing ahead of revenue: Ibiden is spending ~$3.3bn (JPY 500bn) over three years from FY2026, Unimicron and Kinsus have raised 2026 capex, and Morgan Stanley models a ~105% earnings CAGR for Unimicron 2025-2028 [11]. Each build pulls equipment spend (litho, plating, inspection).
  - The glass-core route opens a second, parallel toolset and materials chain on top of organic, not a substitution [13].

- **Constraints**
  - Announced capacity and real supply are ~36 months apart, gated by a yield learning curve money cannot compress; upside is materials-limited (Ibiden has secured ABF for guidance but "not yet" for upside) [9].
  - ABF is a single-vendor chokepoint: Ajinomoto (>95% share) hiked film prices ~30% and only adds ~50% capacity by ~2030, its third plant not online until 2032 [10][11].
  - Board-economics cyclicality: a >30% annual demand swing can flip the pool from shortage to overbuild fast [12].

- **Trends & inflections to watch**
  - Glass-core qualification: 2026-2027 is the qualification phase, 2027-2028 the start of high-volume manufacturing. Tripwire: Absolics commercial output to AMD by end-2026; Samsung SEMCO mass production post-2027 [13][14].
  - Panel-level scale-up to ~600mm formats (Onto JetStep S3500, Dragonfly G5 shipping June 2026). Tripwire: first AI substrate qualified on panel rather than strip [12].
  - Sub-30um line/space FC-BGA for 2.5D/3D. Tripwire: a 13+13-layer substrate in volume confirms the layer-count ramp [9].

## Connections
[BT / ABF Substrates](/manufacturing/packaging/substrate-bt-abf/) · [Glass Interposers](/manufacturing/packaging/glass-interposers/) · thesis: **Advanced Packaging Market**