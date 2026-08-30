---
type: concept
slug: flow-copper-electroplating-ecd
canonical_name: Copper electroplating (ECD) (process step)
seq: 36
phase: beol
related_concepts:
- ru-w-co-metallisation
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
- slug: ru-w-co-metallisation
  name: Ru / W / Co Metallisation
  path: /manufacturing/equipment-processes/ru-w-co-metallisation/
  macro: manufacturing
---
> Step 36 of 56 in the semiconductor flow (BEOL). Prev: [Barrier / liner / seed deposition (process step)](/semiconductor-process-flow/frontend/flow-barrier-liner-seed/) · Next: [Metrology (CD, overlay, film, OCD) (process step)](/semiconductor-process-flow/test-metrology/flow-metrology-cd-overlay/)

## What this step does
Electrochemical deposition (ECD), also called electroplating or electrofill, grows the bulk copper that fills the trenches and vias defined earlier in the dual-damascene flow. The wafer (already carrying the barrier and a thin copper seed from the previous step) is the cathode in an acidic copper-sulfate bath; current drives copper ions onto the seed, and a tuned mix of organic additives forces the fill to grow from the bottom up so features close void-free. This is the workhorse metal-fill step repeated at every interconnect level. Sub-processes inside it:
- Wafer entry, edge-bevel handling and pre-wet/de-gas to wet the high-aspect-ratio features
- The plating cell itself (anode, bath, anolyte/catholyte separation on modern cells)
- Bottom-up "superfill" driven by accelerator/suppressor/leveler additives
- Overburden plate plus edge/bevel removal, then rinse and dry; the overburden is taken off downstream at CMP (step 37 area)

## Where it sits and why it matters
ECD is the value-adding heart of BEOL metallisation. It pairs tightly with the prior barrier/seed step ([Barrier / liner / seed deposition (process step)](/semiconductor-process-flow/frontend/flow-barrier-liner-seed/)) and with the downstream CMP that planarises the overburden, then feeds metrology ([Metrology (CD, overlay, film, OCD) (process step)](/semiconductor-process-flow/test-metrology/flow-metrology-cd-overlay/)). Plating quality (void-free fill, low defectivity, uniform thickness) directly sets interconnect resistance and yield. The same cells, scaled up, do the copper pillars, micro-bumps, redistribution layers (RDL) and through-silicon vias (TSV) that power advanced packaging, so ECD straddles front-end damascene and the fast-growing packaging side.

## Equipment market
Two distinct sub-markets sit under "ECD equipment." (1) Front-end damascene plating for logic/memory interconnects, a slow-growing, highly concentrated pool. (2) Advanced-packaging plating (bump/pillar/RDL/TSV), faster-growing and more contested. Broad ECD equipment is roughly USD 3bn/year [1]; the wider electroplating-systems market (semiconductor) is forecast around USD 1.0bn by 2033 at ~4.2% CAGR on a narrow definition [2], while packaging-heavy TSV plating runs ~USD 256m (2024) at 6.7% CAGR [3]. Treat all of these as report-mill estimates with wide spread; the directional read (low-single to mid-single-digit CAGR, packaging faster than front-end) is robust.

| Vendor | HQ | est. share | notable |
|---|---|---|---|
| Lam Research | US | front-end damascene leader (~60-70% of damascene ECD, rough) | SABRE / SABRE 3D platform; pioneered Cu damascene fill [4] |
| Applied Materials | US | leader in packaging ECD; broad #2 overall | Raider Edge ECD; Semitool legacy in packaging [5] |
| ACM Research | US/China | rising; >1,500 plating chambers shipped | Ultra ECP front-end + packaging; panel-level ECP; China-driven [6] |
| Tokyo Electron / Ebara / EEJA | Japan | mid-tier, packaging-weighted | Ebara also dominant in Cu CMP; EEJA plating cells [5] |
| ASMPT (NEXX), Technic, ClassOne | US | niche / specialty packaging | TSV, RDL, advanced-packaging fill [3] |

Concentration note: front-end damascene ECD is close to a Lam-led duopoly with Applied Materials; packaging ECD is more fragmented (top 5 hold only ~40-45% of TSV plating revenue [3]), which is where ACM is taking share fastest off a China base.

## Materials & consumables
Each plated wafer consumes copper-sulfate electrolyte and, critically, the proprietary organic additive package: accelerators, suppressors and levelers that make bottom-up superfill work. Additives are a few percent of the bath by volume but carry most of the IP and margin. Vendors: DuPont (Qnity electronics business) and Atotech (now MKS Instruments) are the leading damascene additive houses [7]; Entegris, Resonac, Umicore, Technic, MacDermid Alpha, and Chinese suppliers (Sinyang, PhiChem) also compete [8][9]. The copper plating-chemicals market was ~USD 696m in 2024 rising to ~USD 1.17bn by 2032 at ~6.8% CAGR [9]. This is recurring revenue: chemistry is consumed every wafer and re-qualified rarely once locked into a node, so the chemical layer is a sticky annuity bolted to the installed tool base.

## Volumes, revenue, profitability
ECD touches essentially every logic and DRAM wafer, at every metal level (10+ plating passes on advanced logic), so unit exposure scales with total wafer-level interconnect demand plus the packaging wave. Revenue pool: roughly USD 1-3bn/year of equipment plus ~USD 0.7bn/year of plating chemistry, with chemistry growing faster. Margins: front-end WFE leaders (Lam, Applied Materials) run ~45-48% gross and ~30%+ operating margins corporate-wide; ECD is a high-value, IP-rich line within that. Specialty plating chemistry (DuPont/Atotech-MKS) typically earns ~35-45% gross at the electronics-materials segment level, lower than tools but with annuity quality. The margin is earned by whoever owns the qualified recipe-plus-hardware lock-in, not by the commodity copper-sulfate base.

## Market drivers, constraints & trends
Net read: steady-to-accelerating, with the growth weighted to the packaging and 3D side rather than front-end damascene. The served pool is being pulled up by AI/HPC interconnect density even as front-end faces a long-dated copper-displacement risk.

- **Drivers**
  - Copper plating chemistry hit ~USD 1.38bn in 2025, up 9.3% YoY, split roughly evenly between device interconnects (~USD 495m) and advanced packaging (~USD 509m), with TECHCET pinning the pull to "rising interconnect densities in advanced logic, demand from HPC and AI, and increasing adoption of advanced packaging" [10].
  - Backside power delivery (Intel 18A PowerVia now, TSMC A16 Super Power Rail in H2 2026) adds nano-TSV (<100nm) plating as a new copper-fill step on leading-edge wafers, on top of the existing 10+ damascene passes [11].
  - Hybrid bonding turns ECD into a precision step: fine-grain (<0.2um), (111)-textured copper enabling sub-10um pitch and 12+ layer HBM stacks, which raises chemistry value-per-wafer well above commodity electrofill [12].
  - Capacity is being committed: MKS/Atotech USD 40m chemicals plant (Thailand), Moses Lake USD 100m Arizona electrolyte/Cu R&D site, plus TSMC/Amkor/ASE US packaging build-out [10].
- **Constraints**
  - Front-end is the structural threat: below ~10nm line width copper loses to ruthenium/molybdenum, and chipmakers may swap copper at some levels as early as 2nm, so the narrowest, highest-value damascene lines migrate off ECD over the decade [13].
  - The pool stays cyclical and capex-gated on WFE; front-end damascene plating is a near-saturated Lam/Applied duopoly with little unit-growth headroom.
  - Smaller features leave less room for the organic inhibitor molecules that drive bottom-up superfill, raising the technical bar (seedless plating, new seed/barrier) just to hold the existing copper window [13].
- **Trends & inflections to watch**
  - Copper-to-ruthenium displacement at narrow lines. Tripwire: a foundry confirming Ru (not Cu) for the tightest metal layers at the 2nm/A16 node in production (watch TSMC A16 / Intel 14A disclosures through 2026-27) [13].
  - Panel-level packaging on glass shifting plating off round wafers. Tripwire: volume POs / customer qualification of ACM's horizontal panel ECP (first tool shipped Nov 2025) over the next 6-18 months [14].
  - Hybrid-bonding migration in HBM. Tripwire: a memory maker moving an HBM generation from micro-bump to Cu-Cu hybrid bonding in volume, lifting fine-grain chemistry demand [12].

## Connections
[Ru / W / Co Metallisation](/manufacturing/equipment-processes/ru-w-co-metallisation/) · [Barrier / liner / seed deposition (process step)](/semiconductor-process-flow/frontend/flow-barrier-liner-seed/) · [Metrology (CD, overlay, film, OCD) (process step)](/semiconductor-process-flow/test-metrology/flow-metrology-cd-overlay/)

- Owning idea: **Deposition Materials Process Market** (materials/process tool layer).

## Sources
1. Verified Market Reports / Verified Market Research, Electrochemical Deposition (ECD) Market (semiconductor ECD equipment ~USD 3bn/yr; ECD market USD 5.8bn 2023 to USD 8.4bn 2031, 4.4% CAGR). https://www.verifiedmarketresearch.com/product/electrochemical-deposition-ecd-market/
2. Business Research Insights, Semiconductor Electroplating Systems (Plating Equipment) Market (~USD 1,054.6m by 2033, 4.2% CAGR; Lam, Applied Materials, ACM >70% combined). https://www.businessresearchinsights.com/market-reports/semiconductor-electroplating-systems-plating-equipment-market-106021
3. Intel Market Research, TSV Copper-Filled Plating System Market (USD 256m 2024 to USD 401m 2034, 6.7% CAGR; top 5 ~40-45%). https://www.intelmarketresearch.com/tsv-copper-filled-plating-system-market-24919
4. Lam Research, SABRE Product Family / ECD technology (pioneered Cu damascene fill). https://www.lamresearch.com/product/sabre/
5. SemiEngineering, Electroplating IC Packages (Applied Materials leads packaging ECD, then Lam and TEL; Ebara, EEJA, Atotech also compete; Applied Raider Edge vs Lam 3D SABRE). https://semiengineering.com/electroplating-ic-packages/
6. ACM Research, Q4/FY2025 results and panel ECP release (FY25 revenue USD 901.3m +15.2%; 1,500th plating chamber; first horizontal panel ECP). https://www.globenewswire.com/news-release/2025/11/17/3188771/0/en/ACM-Research-Delivers-First-Horizontal-Panel-Electroplating-Tool-Strengthening-Its-Leadership-in-Fan-Out-Panel-Level-Packaging.html
7. DuPont, Dual Damascene Copper / Atotech Everplate (sub-20nm void-free bottom-up fill additive suites). https://www.dupont.com/electronics-industrial/damascene.html
8. Atotech (MKS Instruments), Semiconductor pad metallization & pillar plating chemistry. https://www.atotech.com/products/electronics/semiconductor/
9. 24chemicalresearch, Copper Plating Solutions for Semiconductor Market (USD 695.7m 2024 to USD 1.17bn 2032, 6.8% CAGR; Entegris, DuPont, MKS/Atotech, Umicore, Resonac-adjacent, Technic, Sinyang, PhiChem). https://www.24chemicalresearch.com/reports/265625/global-copper-plating-solutions-for-semiconductor-market
10. Semiconductor Digest / TECHCET, Rising Copper Plating Demand Driven by Advanced Packaging and FE Interconnects (plating chemistry ~USD 1.38bn 2025 +9.3% YoY; ~USD 495m interconnects + ~USD 509m packaging; MKS/Atotech USD 40m Thailand plant; Moses Lake USD 100m Arizona site; TSMC/Amkor/ASE US build-out). https://www.semiconductor-digest.com/rising-copper-plating-demand-in-semiconductors-driven-by-advanced-packaging-and-fe-interconnects/
11. SemiEngineering / aminext, Backside Power Delivery for 2nm (Intel 18A PowerVia nano-TSV <100nm; TSMC A16 Super Power Rail mass production H2 2026; new backside copper-fill plating step). https://semiengineering.com/backside-power-delivery-gears-up-for-2nm-devices/
12. 3D InCites, Engineering Copper Grain Structure for High-Yield Hybrid Bonding (fine grain <0.2um, (111) texture; sub-10um pitch; bonding at 180C; HBM stacks 12+ layers; sub-micron pad pitch roadmap). https://www.3dincites.com/2025/09/engineering-copper-grain-structure-for-high-yield-hybrid-bonding-in-3d-packaging/
13. SemiEngineering, The End of Copper Interconnects? / Extending Copper to 2nm (below ~10nm line width Cu loses to Ru/Mo; hybrid Ru-narrow/Cu-wide; possible Cu swap at some 2nm levels; less room for inhibitor molecules, seedless plating R&D). https://semiengineering.com/the-end-of-copper-interconnects/
14. ACM Research, First Horizontal Panel Electroplating Tool (Ultra ECP ap-p) for Fan-Out Panel-Level Packaging (first commercial panel Cu deposition system, organic + glass substrates, shipped to lead customer Nov 2025; watch qualification/POs over 6-18 months). https://ir.acmr.com/news-releases/news-release-details/acm-research-delivers-first-horizontal-panel-electroplating-tool
