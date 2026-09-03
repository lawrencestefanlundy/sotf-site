---
type: concept
slug: flow-solder-ball-bga
canonical_name: Solder ball attach / BGA (process step)
seq: 49
phase: assembly
related_concepts:
- packaging
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 9
parent_concepts:
- packaging
sources_7d: 1
sources_30d: 2
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
- slug: packaging
  name: Semiconductor Packaging
  path: /manufacturing/packaging/packaging/
  macro: manufacturing
---
> Step 49 of 56 in the semiconductor flow (Assembly). Prev: [Molding / encapsulation (process step)](/semiconductor-process-flow/packaging/flow-molding-encapsulation/) · Next: [Advanced packaging: 2.5D (CoWoS / EMIB / interposer) (process step)](/semiconductor-process-flow/packaging/flow-advanced-pkg-2-5d/)

## What this step does

After the die is mounted and encapsulated, the package still needs a way to connect to the outside board. Ball grid array (BGA) attach forms that interface by placing a grid of tiny solder spheres on the underside of the package (or substrate, or wafer), then reflowing them so they wet to the pads and become the package's terminals. It is the dominant input/output scheme for high-pin-count parts (CPUs, GPUs, SoCs, memory, AI accelerators) because an area array of balls fits far more connections under a package than a perimeter of leads. The sub-processes inside this step:

- Flux application: pin-transfer dipping, jetting, or printing of tacky/liquid flux onto the pads to clean them and hold balls in place.
- Ball placement: a vacuum stencil/template or single-ball jetting head drops pre-formed spheres (typically 50-760 microns) into each flux site.
- Reflow: the whole assembly passes through a reflow oven so balls melt and self-align to the pads; flux residue is then cleaned.
- Inspection: 2D/3D vision checks for missing balls, bridges, coplanarity.

## Where it sits and why it matters

This is a back-end (OSAT or IDM assembly) step, low-margin and high-volume relative to the front end, but it is the physical gateway to the board. It is distinct from [Flip-chip bumping (C4 / Cu pillar / microbump) (process step)](/semiconductor-process-flow/packaging/flow-flip-chip-bumping/) (fine-pitch bumps on the die-to-substrate side); BGA attach is usually the coarser package-to-board side. As pitches shrink and balls get smaller, the line blurs toward wafer-level packaging, where this step migrates onto the wafer itself and overlaps with advanced packaging.

## Equipment market

The dedicated ball-mounter machine niche is small and the report mills disagree widely on boundaries. A narrow "solder ball mounting equipment" read puts 2024 at roughly US$89M growing to ~US$149M by 2032 at ~6.7% CAGR [1]. A broader "BGA/CSP/FCBGA automatic solder ball mounter" definition (which folds in flip-chip and wafer-level mounters) puts 2023 at ~US$691M heading to ~US$1.0B by 2030 at ~6.2% CAGR [2]. Treat both as rough. Machine prices run ~US$200k to >US$1M [1].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Shibuya Corp | Japan | high (top tier) | broad flux + ball-mount + reflow lines |
| Athlete FA | Japan | mid-high | mainstream BGA/CSP mounters |
| Hanmi Semiconductor | South Korea | mid | back-end equipment breadth |
| PacTech (ASMPT) | Germany | niche/specialist | laser solder-ball jetting (SB2), flux-free |
| ASMPT | Singapore/Germany | mid | assembly equipment platform, owns PacTech |
| Shinkawa / Athlete / others | Japan/Korea | tail | precision placement |

Concentration note: Japanese and Korean toolmakers dominate; shares are not cleanly published and the figures above are directional. The market is fragmented across a coarse mechanical-template tier and a higher-value jetting tier.

## Materials & consumables

This step consumes the spheres themselves plus ball-attach flux. Solder balls are the bigger pool: the solder ball / solder sphere market was ~US$365M in 2024, projected to ~US$537M by 2032 at ~4.9% CAGR [3]; a separate "small-diameter solder spheres" read reaches ~US$0.35B by 2031 [4]. Flux is a smaller adjacent consumable (Indium Corp, Inventec/Dehon, Senju). Spheres are SAC (tin-silver-copper) lead-free alloys, sized and sorted to tight tolerance.

| Vendor | HQ | Notable |
|---|---|---|
| Senju Metal | Japan | high-end micro-ball leadership |
| Nippon Micrometal | Japan | fine spheres, technical lead |
| DS HiMetal | South Korea | mainstream BGA/CSP volume |
| MK Electron | South Korea | volume spheres + bonding wire |
| Indium Corporation | USA | specialty spheres + ball-attach flux |
| Shenmao / PMTC / YCTC | Taiwan | mainstream BGA/CSP volume |

Recurring-revenue note: spheres and flux are pure consumables, reordered per package built, so the materials layer is annuity-like and tied directly to assembly unit volumes; the equipment is one-time capex.

## Volumes, revenue, profitability

BGA/CSP attach touches an enormous slice of packaged units (every high-pin-count logic and many memory parts), so even at fractions of a cent of solder per device the aggregate sphere pool reaches the ~US$365M scale [3]. The combined equipment-plus-materials pool for this specific step is therefore roughly US$0.5-1.5B depending on where you draw the equipment boundary. Margins: solder spheres are commodity-ish chemistry/metallurgy with gross margins typically in the ~20-35% range and thinner operating margins, since alloy (tin/silver) input cost passes through and Korean/Taiwanese volume players compete on price. The value-capturing layer is the few Japanese houses (Senju, Nippon Micrometal) at the fine-pitch, high-reliability end, and the equipment makers with jetting IP, not the bulk-sphere suppliers.

## Competitive landscape & value capture

Moat is modest and concentrated at the technical edge. Bulk spheres are a metallurgy commodity with low switching cost and metal-price pass-through; the durable position is fine-diameter, ultra-low-defect spheres for fine-pitch and wafer-level work (Japanese leadership) and flux-free laser jetting equipment (PacTech, the one materially EU-relevant name here, German, owned by ASMPT). The structural pull is fewer, smaller balls per package and the migration of attach onto the wafer, which favours jetting and high-precision suppliers over template mounters. EU / seed angle: thin. PacTech is the EU footprint but sits inside listed ASMPT, not investable independently; there is no obvious pre-seed wedge in a commodity-sphere market with entrenched Asian incumbents.

## Market drivers, constraints & trends

Net read: a steady-to-firming consumable annuity, lifted at the high-reliability edge by AI packaging but with a slow-fuse displacement risk underneath.

- **Drivers** — The advanced-packaging-grade slice is the fast bit: solder ball for advanced packaging was ~US$121M in 2024, projected to ~US$240M by 2034 at ~10.4% CAGR, far ahead of the bulk-sphere pool's ~5% [9]. FCBGA substrates (the thing these balls attach to) are growing ~10.6% CAGR to ~US$9.5B by 2032 on AI/datacentre pull [10], dragging high-reliability sphere and jetting demand with them. OSAT capex is in an arms race: Amkor guides US$2.5-3.0B 2026 capex for AI advanced packaging incl. its Arizona plant [11]; reshoring final assembly to the US (CHIPS-backed) builds out new attach lines closer to TSMC/Intel fabs [11].
- **Constraints** — The bulk-sphere layer is a metal-price-pass-through commodity, capping margin and CAGR at the low single digits [9]. The step is back-end, cyclical, and low value-add per device. The structural threat is hybrid bonding: at sub-10um pitch direct Cu-Cu bonds remove solder entirely, and the trend of fewer, smaller balls per package erodes consumable tonnage even where attach persists [12].
- **Trends & inflections to watch** — HBM4 staying on microbumps (JEDEC raised the stack-height limit 720um to 775um) postpones the solder-displacement hit; tripwire: HBM4E volume hybrid bonding from ~2028, or Samsung 16-Hi hybrid-bond yield crossing ~50% from today's ~10% [12]. Panel-level packaging migrates attach onto large panels (Yole: ~US$160M 2024 to ~US$650M 2030); tripwire: TSMC CoPoS production start ~2027 with Rubin Ultra [13]. Glass-core substrates ramp from small-scale 2026 shipments to fast growth 2028-30 (>10% glass-wafer CAGR, ~33% for HBM/logic glass) [13], favouring precision jetting over template mounters.

## Connections

- [Semiconductor Packaging](/manufacturing/packaging/packaging/)
- [Molding / encapsulation (process step)](/semiconductor-process-flow/packaging/flow-molding-encapsulation/)
- [Flip-chip bumping (C4 / Cu pillar / microbump) (process step)](/semiconductor-process-flow/packaging/flow-flip-chip-bumping/)
- [Advanced packaging: 2.5D (CoWoS / EMIB / interposer) (process step)](/semiconductor-process-flow/packaging/flow-advanced-pkg-2-5d/)

- Owning idea: **Legacy Assembly Commoditised** (commodity assembly (recorded pass)).

## Sources

1. Solder Ball Mounting Equipment market (~US$89.4M 2024 to ~US$149.3M 2032, 6.7% CAGR; tool prices US$200k-$1M+): https://semiconductorinsight.com/report/solder-ball-mounting-equipment-for-semiconductor-packaging-market/
2. BGA/CSP/FCBGA Automatic Solder Ball Mounter (broader def, ~US$691M 2023 to ~US$1,023M 2030, 6.2% CAGR; vendor list): https://www.globalinforesearch.com/reports/2376126/bga-csp-fcbga-automatic-solder-ball-mounter
3. Solder balls market (~US$364.82M 2024 to ~US$536.55M 2032, 4.94% CAGR; Senju, DS HiMetal, MK Electron, Nippon Micrometal, Indium): https://www.verifiedmarketresearch.com/product/solder-balls-market/
4. Small-diameter solder spheres market (~US$0.35B by 2031): https://www.openpr.com/news/4323803/small-diameter-solder-spheres-market-report-the-global-market
5. BGA solder ball market (~US$509.3M by 2032, 6.7% CAGR): https://www.prophecymarketinsights.com/PressRelease/BGA-Solder-Ball-Market-2837
6. Indium Corporation ball-attach flux + solder spheres (process + consumable): https://www.indium.com/applications/semiconductor-packaging-and-assembly/ball-attach/
7. PacTech SB2 laser solder-ball jetting (flux-free attach equipment, EU/Germany): https://www.inseto.com/equipment/wafer-solder-bumping-equipment-and-services-by-pactech/solder-jetting-systems/
8. Ball-attach process (flux dip / jet, placement, reflow): https://www.inventec.dehon.com/solutions/soldering/ball-attach-semiconductor-packaging-process/
9. Solder ball for advanced packaging market (~US$121M 2024 to ~US$240M 2034, 10.4% CAGR; bifurcation into commodity vs AI-premium segment): https://www.intelmarketresearch.com/solder-ball-for-advanced-packaging-market-24672
10. FC BGA market (~US$4,890M 2024 to ~US$9,548M 2032, 10.6% CAGR; AI/datacentre/HBM substrate pull): https://www.intelmarketresearch.com/fc-bga-market-21985
11. Amkor 2026 capex US$2.5-3.0B for AI advanced packaging + Arizona reshoring plant (~US$400M federal grant): https://markets.financialcontent.com/stocks/article/marketminute-2026-2-12-amkor-technology-shatters-expectations-ai-driven-advanced-packaging-boom-triggers-massive-2026-investment-surge
12. HBM4 sticks with microbumps (JEDEC 720um to 775um stack-height relax; hybrid bonding mainstream from HBM4E ~2028; Samsung 16-Hi hybrid-bond yield ~10%): https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/
13. Panel-level packaging (~US$160M 2024 to ~US$650M 2030, Yole) + glass-core substrates (small-scale 2026, fast growth 2028-30, >10% glass-wafer CAGR / ~33% HBM-logic; TSMC CoPoS ~2027): https://www.yolegroup.com/press-release/glass-core-substrates-and-glass-interposers-new-growth-engines-for-glass-in-advanced-packaging-for-ai-and-hpc/
