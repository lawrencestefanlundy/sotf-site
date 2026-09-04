---
type: concept
slug: flow-wire-bonding
canonical_name: Wire bonding (process step)
seq: 44
phase: assembly
related_concepts:
- bonding-dicing-equipment
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 21
parent_concepts:
- packaging
sources_7d: 1
sources_30d: 3
recent_mentions:
- slug: 2023-08-31-e13-chiplets-how-chip-lego-is-driving
  title: '🔮 E13: Chiplets - How Chip Lego is Driving AI Progress'
  date: '2023-08-31'
  kind: substack
neighbors:
- slug: bonding-dicing-equipment
  name: Bonding & Dicing Equipment
  path: /manufacturing/equipment-processes/bonding-dicing-equipment/
  macro: manufacturing
---
> Step 44 of 56 in the semiconductor flow (Assembly). Prev: [Die attach / pick-and-place (process step)](/semiconductor-process-flow/packaging/flow-die-attach-pick-place/) · Next: [Flip-chip bumping (C4 / Cu pillar / microbump) (process step)](/semiconductor-process-flow/packaging/flow-flip-chip-bumping/)

## What this step does
After a die is attached to a leadframe or substrate, wire bonding forms the electrical connections between the chip bond pads and the package leads using fine metal wire. It is the oldest and still the highest-volume first-level interconnect method, dominant in commodity, power, automotive, optoelectronic and memory packages where the speed and density of flip-chip are not required. Sub-processes inside the step:
- Ball bonding (thermosonic): melt a free-air ball at the wire tip, bond it to the pad, loop the wire, then form a stitch/wedge at the lead. Used with gold, copper and silver fine wire.
- Wedge bonding (ultrasonic): bond flat without a ball, used for aluminium and heavy wire/ribbon in power and RF.
- Heavy-wire and ribbon bonding: thick aluminium/copper for high-current power modules.
- Bond verification: pull/shear test, wire-loop inspection.

## Where it sits and why it matters
Wire bonding is the workhorse of the back-end. Most of the world's packaged transistors are still wire-bonded, not flip-chipped. Two things make this step investable: it is a recurring-consumable business (every package burns metal wire and a capillary tool), and it is in the middle of a multi-year material substitution (gold to copper/PCC and silver) driven by the gold price. The next step, [Flip-chip bumping (C4 / Cu pillar / microbump) (process step)](/semiconductor-process-flow/packaging/flow-flip-chip-bumping/), is where high-performance/AI packaging migrates away from wire, so wire bonding is a mature-but-huge pool rather than the growth frontier.

## Equipment market
Wire-bonder equipment is roughly USD 1.0-1.6bn/year depending on definition; one mid-point estimate puts it at ~USD 1.62bn in 2025 growing to ~USD 1.72bn in 2026 (~6% CAGR) [1]. Treat the higher report-mill figures (USD 3-4bn) with suspicion as they bundle adjacent die-bonder/TCB equipment. The segment is moderately concentrated: ball bonders are a near-duopoly, while wedge/heavy-wire is more fragmented.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| ASMPT | Singapore / Hong Kong | ~50-60% of wire bonders [4] | Largest back-end assembly equipment vendor overall (~USD 1.69bn group rev 2024) [5] |
| Kulicke & Soffa | US / Singapore | ~30-40%; historic 60-70% ball-bonder peaks [3][4] | Pure-play bonder leader, ball-bonder pioneer (FY24 rev USD 706.2m) [2] |
| BE Semiconductor (Besi) | Netherlands | minor in wire; leads flip-chip/TCB | More exposed to advanced packaging |
| Hesse (Mechatronics) | Germany | leader in wedge/heavy-wire niche [6] | EU; power/automotive/RF wedge + ribbon |
| F&K Delvotec | Germany | wedge/fine-wire niche [6] | EU; ultrasonic bonders since 1978 |

Concentration note: ASMPT plus K&S take the large majority of unit volume in fine-wire ball bonding; the European players (Hesse, F&K Delvotec) own the specialised wedge/heavy-wire and power-module corners, not the volume centre.

## Materials & consumables
The recurring pool dwarfs the tool pool. Each bonder consumes bonding wire (gold, copper, palladium-coated copper "PCC", silver, aluminium) plus capillaries/wedges (ceramic/tungsten-carbide tooling). Bonding-wire market estimates diverge widely by scope: precious-metal-heavy definitions reach ~USD 9-13bn for 2024 (the gold-loaded number rides the gold price), while tighter "semiconductor packaging bonding wire" cuts are ~USD 4bn [7][8]. A defensible read is a multi-billion-dollar materials market several times the equipment market, growing low-to-mid single digits, with the value mix shifting from gold (~55% of wire by type in 2023) to copper/PCC as gold passed USD 2,000/oz [8][9]. Vendors: Heraeus (Germany), Tanaka (Japan), Nippon Micrometal/Nippon Steel Chemical, Tatsuta, MK Electron (Korea), plus Chinese suppliers (Yantai, Ningbo Kangqiang, Niche-Tech). Heraeus, Tanaka and MK Electron together hold ~29% of all bonding wire; Heraeus plus Tanaka hold over 40% of the gold-wire segment [7]. This is a true razor-and-blades business: the wire is bought every shift, forever.

## Volumes, revenue, profitability
Volume scale: hundreds of billions of wire bonds per year (modern memory/logic packages run dozens to hundreds of bonds each; high-speed bonders place 20-30+ wires/second). Revenue pool: ~USD 1-1.6bn equipment + multi-billion (USD 4-13bn depending on definition, gold-price-sensitive) materials. Profitability splits sharply by layer:
- Equipment: K&S FY2024 gross margin 44.4% on USD 706.2m revenue, but a net loss of USD 69.0m through the down-cycle, with Q4 GAAP operating margin only ~1.5% (non-GAAP ~7%) [2]. Bonder equipment is cyclical and capital-light to buy but thin at the bottom of the cycle.
- Materials: precious-metal converters run high revenue but structurally thin gross margins because most of the price is pass-through metal; the spread is on conversion/yield/alloy IP, not the gold itself.
Who earns the durable margin: the equipment duopoly captures the IP rent (placement speed, loop control, copper-bonding process), while wire suppliers earn a smaller but far more recurring annuity on consumable volume.

## Competitive landscape & value capture
Moat in equipment is process know-how (copper bonding is harder than gold: oxidation, pad cratering, forming-gas control) plus a large installed base and service tie-in, which is why ASMPT and K&S persist as a duopoly. Moat in materials is alloy/PCC metallurgy and qualification lock-in at the OSAT/IDM. Value accrues to (a) the two bonder OEMs and (b) the handful of precious-metal wire houses; everyone else is a niche or commodity follower. EU / seed angle: the seed-relevant openings are not in volume ball bonding (locked) but in adjacent corners. Germany's Hesse and F&K Delvotec show a real EU foothold in wedge/heavy-wire for power and automotive; Heraeus is the EU materials anchor. A genuinely novel pre-seed bet would be in copper/silver wire metallurgy, low-cost in-line bond inspection/AI metrology, or power-module heavy-wire/ribbon tooling, not a me-too bonder.

## Market drivers, constraints & trends
Net read: a steady-to-cyclical mature pool, not a decliner. The volume centre keeps growing low-to-mid single digits while the value mix re-rates harder than the unit count, and the feared displacement is slipping right.
- **Drivers** — Power electronics and automotive pull heavy-wire/ribbon and copper bonding: IGBT/SiC module growth and EV electrification are the explicit demand engines, and copper at ~20-25% of gold's cost speeds high-volume conversion [10][11]. Wire bonding stays essential in legacy, high-volume, cost-sensitive packaging, with the domain still growing to ~USD 978m equipment revenue by 2030 (Yole) [13]. Yole's headline equipment segment is ~USD 1.62bn 2025 → ~USD 2.47bn 2032 (~6.2% CAGR) [10].
- **Constraints** — Advanced packaging (flip-chip, TCB, hybrid bonding) caps the high-performance ceiling: AI/HBM/chiplet dollars route to TCB (~USD 936m by 2030) and hybrid bonding (21.1% CAGR) instead of wire [13]. The materials pool is gold-price-whipsawed (gold passed USD 4,500/oz early 2026), so revenue can swell on metal while volume stalls [12]. Equipment is sharply cyclical (K&S swung to a net loss through the last trough).
- **Trends & inflections to watch** — Gold→copper/PCC value migration: PCC is the fastest-growing wire segment (~8.1% CAGR) [12]. Tripwire: gold-wire share dropping below ~45% of wire by type (was ~55% in 2023). Displacement-slip is the non-consensus bull: HBM4 16-high stays on MR-MUF/microbumps, and TrendForce (1 Apr 2026) flagged JEDEC may relax package height to ~900um from HBM4E, pushing full hybrid-bonding adoption past 2028 to HBM5 20-hi [14]. Tripwire: a confirmed HBM5 hybrid-bonding production date past 2028 extends the wire/microbump annuity another generation.

## Connections
- [Bonding & Dicing Equipment](/manufacturing/equipment-processes/bonding-dicing-equipment/)
- Prev: [Die attach / pick-and-place (process step)](/semiconductor-process-flow/packaging/flow-die-attach-pick-place/) · Next: [Flip-chip bumping (C4 / Cu pillar / microbump) (process step)](/semiconductor-process-flow/packaging/flow-flip-chip-bumping/)

- Owning idea: **Legacy Assembly Commoditised** (commodity assembly (recorded pass)).

## Sources
1. 360iResearch / mid-point wire-bonder equipment sizing (~USD 1.62bn 2025, ~6% CAGR) — https://www.360iresearch.com/library/intelligence/wire-bonder-equipment
2. Kulicke & Soffa FY2024 Q4 results (rev USD 706.2m, GM 44.4%, net loss USD 69.0m, Q4 op margin ~1.5%) — https://www.prnewswire.com/news-releases/kulicke--soffa-reports-fourth-quarter-2024-results-302304678.html
3. K&S ball-bonder historic share (near 60-70% peaks) — https://portersfiveforce.com/blogs/competitors/kns
4. Wire-bonder competitive landscape (ASMPT largest back-end vendor; K&S, Hesse, F&K Delvotec, Palomar) — https://www.maximizemarketresearch.com/market-report/global-wire-bonder-equipment-market/72738/
5. ASMPT 2024 annual results (group rev ~USD 1.69bn; largest back-end assembly equipment vendor) — https://www.asmpt.com/en/investor-relations/news-events/asmpt-announces-2024-fourth-quarter-results/
6. Hesse & F&K Delvotec (German wedge/heavy-wire bonder leaders) — https://www.hesse-mechatronics.com/en/; https://www.fkdelvotec.com/en/
7. Bonding-wire market size and share (Heraeus/Tanaka/MK Electron ~29%; Heraeus+Tanaka >40% of gold wire; ~USD 9-13bn 2024 scope-dependent) — https://reports.valuates.com/market-reports/QYRE-Auto-26Y16315/global-semiconductor-packaging-bonding-wire
8. Tighter semiconductor packaging bonding-wire sizing (~USD 4bn cut; gold ~55% of wire by type 2023) — https://www.verifiedmarketreports.com/product/bonding-wires-market/
9. Gold-to-copper/PCC transition drivers (gold > USD 2,000/oz; PCC fastest growth) — https://www.intelmarketresearch.com/palladium-coated-copper-bonding-wires-market-15387
10. Wire-bonder equipment ~USD 1.62bn 2025 → USD 2.47bn 2032 (~6.18% CAGR); power-electronics/automotive/IGBT drivers — https://www.360iresearch.com/library/intelligence/wire-bonder-equipment
11. Copper wire bonding equipment ~USD 461m 2025 → USD 751m 2034 (7.4% CAGR); copper ~20-25% of gold cost; IGBT/automotive substitution — https://www.intelmarketresearch.com/copper-wire-bonding-equipment-market-42690
12. Gold > USD 4,500/oz early 2026; PCC fastest-growing wire segment (~8.1% CAGR); secular gold→copper/PCC value migration — https://www.futuremarketinsights.com/reports/gold-palladium-plated-copper-wire-market
13. Yole back-end equipment: wire bonding ~USD 978m by 2030 (legacy/automotive/industrial); TCB ~USD 936m and hybrid bonding ~USD 397m (21.1% CAGR) take advanced-packaging dollars — https://www.yolegroup.com/press-release/advanced-packaging-fuels-transformation-in-back-end-equipment-tcb-and-hybrid-bonding-to-lead-1-3-billion-market-expansion-by-2030/
14. HBM4 16-high stays on MR-MUF/microbumps; TrendForce (1 Apr 2026) JEDEC ~900um height relaxation from HBM4E; full hybrid bonding pushed past 2028 to HBM5 20-hi — https://www.trendforce.com/news/2026/01/13/news-sk-hynix-may-stick-with-mr-muf-for-hbm4-16-high-despite-asmpt-tc-bonder-orders/
