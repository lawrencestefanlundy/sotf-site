---
type: concept
slug: flow-barrier-liner-seed
canonical_name: Barrier / liner / seed deposition (process step)
seq: 35
phase: beol
related_concepts:
- diffusion-barriers
- ru-w-co-metallisation
- pvd-sputtering
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
- slug: diffusion-barriers
  name: Diffusion Barriers (TiN, TaN)
  path: /materials/coatings-interfaces/diffusion-barriers/
  macro: materials
- slug: ru-w-co-metallisation
  name: Ru / W / Co Metallisation
  path: /manufacturing/equipment-processes/ru-w-co-metallisation/
  macro: manufacturing
- slug: pvd-sputtering
  name: PVD / Sputtering
  path: /manufacturing/equipment-processes/pvd-sputtering/
  macro: manufacturing
---
> Step 35 of 56 in the semiconductor flow (BEOL). Prev: [Damascene patterning (via/trench) (process step)](/semiconductor-process-flow/frontend/flow-damascene-patterning/) · Next: [Copper electroplating (ECD) (process step)](/semiconductor-process-flow/frontend/flow-copper-electroplating-ecd/)

## What this step does

After the damascene trenches and vias are etched, the wafer gets a thin multi-layer metal lining before copper goes in. The barrier stops copper atoms diffusing into the surrounding low-k dielectric (copper poisons silicon and dielectric). The liner helps copper wet and adhere. The seed gives the electroplating bath something conductive to grow copper onto. Sub-processes inside this one step:

- Diffusion **barrier** deposition (historically TaN, ~tantalum nitride) [1].
- **Liner** deposition (historically Ta, now shifting to cobalt and ruthenium) [2][6].
- Copper **seed** deposition (ionised PVD copper, sometimes a CVD/ALD assist for void-free fill) [1][3].
- An integrated pre-clean / degas inside the same vacuum cluster so air never touches the stack.

## Where it sits and why it matters

This is the gatekeeper between an etched cavity and the copper that carries the signal. As wires shrink below ~20nm wide, the barrier/liner stack eats a brutal share of the available cross-section: a 2nm-thick liner inside a 12nm wire is a fifth of the metal width, and that volume carries far worse current than copper. So every angstrom shaved off the liner is a direct resistance and power win. This is why the step has become one of the most actively re-engineered in the whole flow, and why a precious metal (ruthenium) is being designed into volume logic for the first time [2][6].

## Equipment market

The tool of record is **physical vapour deposition** (sputtering) inside a multi-chamber vacuum cluster, increasingly paired with ALD and CVD chambers for the conformal liner. The PVD equipment segment was ~$5.65B in 2024 and is one of the more concentrated parts of the deposition market; analysts describe it as "almost a monopoly" controlled by Applied Materials [4][5]. Within the broader deposition-equipment market, Applied Materials holds ~21% of all deposition, Lam ~18%, Tokyo Electron ~16%, but for *metal* PVD specifically Applied's share is far higher [5].

| Vendor | HQ | Est. share (metal PVD / this step) | Notable |
|---|---|---|---|
| Applied Materials | US | ~80-85% (rough; "near-monopoly") | Endura platform; Endura Copper Barrier Seed IMS with Volta Ruthenium CVD; 3,000+ Endura systems shipped [4][7][8] |
| Lam Research | US | mid-single-digit to ~10% | ALD/CVD liner and seed-assist, ECD adjacency [5] |
| Tokyo Electron | JP | small in metal PVD | stronger in ALD broadly [5] |
| ASM International | NL | small here | ALD leadership sits more in dielectrics/high-k [5] |
| Evatec / Ulvac | CH / JP | niche | specialty and compound-semi PVD |

Concentration note: this is among the most lopsided steps in the entire flow. Applied's Endura is effectively the standard, and the barrier-seed module is sold as an integrated six-process cluster, which deepens lock-in [7].

## Materials & consumables

The recurring spend is **sputter targets and precursors**: tantalum and TaN targets, copper targets for seed, and now cobalt and ruthenium precursors / targets for the new liner chemistries. The ruthenium shift turns a cheap-metal step into one exposed to a thin, volatile precious-metals market. Ruthenium is a platinum-group byproduct: only ~30-35 tonnes mined a year, ~80% from South Africa, and the price ran from roughly $500/oz to over $1,400-1,700/oz across 2025-2026 on data-storage and interconnect demand [10][11]. The ruthenium-for-interconnects sub-market was ~$220M in 2024 and is forecast toward ~$1.15B by 2030 at ~32% CAGR (a report-mill figure, treat as directional) [9]. Precursor suppliers (e.g. Merck/Versum, Entegris, Adeka, and PGM refiners like Heraeus and Johnson Matthey feeding the metal) capture a steady consumables annuity that scales with wafer starts.

## Volumes, revenue, profitability

Every advanced-logic and DRAM wafer with copper BEOL passes through this step many times (one barrier/seed pass per metal level, ~10-15+ levels on a leading-logic part). So unit volume tracks total leading-edge wafer starts. The equipment revenue pool sits inside the ~$5-6B metal-PVD line plus the fast-growing conformal ALD/CVD liner spend; the consumables pool is the targets-plus-precursors annuity layered on top [4][9]. Margin sits overwhelmingly with the equipment maker: Applied Materials runs ~47-48% gross and high-20s to ~30% operating margin at the corporate level, and its metal-deposition franchise is at the premium end of that. The materials/precursor layer earns lower product gross margin but very sticky, qualified, recurring revenue. The fab itself captures the value downstream as yield.

## Competitive landscape & value capture

The moat is integration and qualification, not any single chamber. Applied wins because the barrier, liner, seed, pre-clean and now ruthenium CVD live in one qualified vacuum cluster (the Endura Copper Barrier Seed IMS with Volta Ruthenium CVD), and that module is being adopted across leading logic makers starting at 3nm, shrinking the liner ~33% to 2nm and cutting line resistance up to ~25% [7][8]. Displacing it means re-qualifying a whole module against the industry incumbent, which almost never happens at a leading node. Value accrues, in order: (1) the equipment maker (Applied, dominant), (2) the precious-metal and precursor suppliers riding the ruthenium transition, (3) the fab as yield.

## Market drivers, constraints & trends

Net read: the served market (metal-PVD plus the fast-growing conformal liner ALD/CVD and the ruthenium/cobalt precursor annuity) is set to grow faster than the wider deposition pool, because this is the one BEOL step where physics is forcing a materials and tool re-buy at every leading node, on top of an AI-driven wafer-fab-equipment supercycle.

- **Drivers** —
  - WFE crossed $100B for the first time in 2025 and is forecast to reach ~$145B in 2026 and peak ~$156B in 2027 on AI/datacentre demand; leading-edge logic and HBM wafer starts (which run this step 10-15+ times each) are the fastest-growing slice [12][13].
  - Each node transition re-qualifies the barrier/liner/seed module: RuCo liners are now in high-volume use at 2nm across all leading logic makers, a brand-new tool and precursor buy versus the old TaN/Ta scheme [14][16].
  - Backside power delivery (2nm-era) adds new low-resistance power vias and rails that need their own tailored barrier/liner and fill, expanding the served process count per wafer [15].

- **Constraints** —
  - Ruthenium is a hard supply chokepoint: ~32 tonnes/yr, ~80% South African by-product, a 7th straight deficit and a ~203k oz shortfall forecast for 2026, with price up from ~$500 to >$1,700/oz in a year, much of it pulled by HDD/HAMR storage demand competing with interconnects [17][18].
  - Demand tracks leading-edge capex, so the pool is cyclical and concentrated on a handful of fabs; an AI-capex digestion phase would hit it hard.
  - The core tool layer is a near-monopoly, so most equipment upside accrues to one incumbent, not a broad supplier base (capped competitive entry).

- **Trends & inflections to watch** —
  - Barrierless/subtractive metal: below ~20nm CD, barrierless Ru and molybdenum beat lined copper, and Intel showed a subtractive-Ru scheme at IEDM 2024. Tripwire: a foundry disclosing Mo or barrierless-Ru on a *production* metal level (not just local interconnect) by IEDM 2026-2027 would shrink the classic barrier/seed module and re-rate the precursor mix [14][16].
  - Semi-damascene with fully self-aligned vias: imec has two-layer Ru at 16-18nm pitch, >80% yield. Tripwire: first HVM semi-damascene metal level at a leading fab (~A14/2027) flips this step from PVD-barrier toward Ru-fill plus area-selective deposition [16][19].
  - Area-selective deposition eliminating the via-bottom barrier. Tripwire: an ASD fully-self-aligned-via process entering a production flow would directly cannibalise the barrier sub-step while growing ALD precursor spend [19].

## Connections

- [Diffusion Barriers (TiN, TaN)](/materials/coatings-interfaces/diffusion-barriers/) - the TaN/Ta-to-Co/Ru barrier physics this step implements
- [Ru / W / Co Metallisation](/manufacturing/equipment-processes/ru-w-co-metallisation/) - the metal-transition thesis driving the ruthenium and cobalt shift
- [PVD / Sputtering](/manufacturing/equipment-processes/pvd-sputtering/) - the dominant deposition method for the barrier and seed
- **Deposition Materials Process Market** - the cross-step deposition equipment + materials investment thesis
- Adjacent steps: [Damascene patterning (via/trench) (process step)](/semiconductor-process-flow/frontend/flow-damascene-patterning/) (prev), [Copper electroplating (ECD) (process step)](/semiconductor-process-flow/frontend/flow-copper-electroplating-ecd/) (next), [PVD / sputtering (process step)](/semiconductor-process-flow/frontend/flow-pvd-sputtering/), [Atomic layer deposition (ALD) (process step)](/semiconductor-process-flow/frontend/flow-ald-atomic-layer-deposition/), [CVD / PECVD deposition (process step)](/semiconductor-process-flow/frontend/flow-cvd-pecvd/)

## Sources

1. USPTO 9,926,639, "Methods for forming barrier/seed layers for copper interconnect structures" (PVD TaN/Ta thicknesses, ionised PVD seed). https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9926639
2. USPTO 12,094,770, "Ruthenium-based liner for a copper interconnect" (Ru as seed/liner replacing Ta/TaN). https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12094770
3. AIP, "The role of Ru passivation and doping on the barrier and seed layer properties of Ru-modified TaN for copper interconnects." https://pubs.aip.org/aip/jcp/article/152/14/144701/197924/
4. MarketResearchFuture / industry sizing: PVD segment ~$5.65B (2024); CVD ~$5.64B (2024); ALD ~$11.6B (2024). https://www.marketresearchfuture.com/reports/semiconductor-cvd-and-pvd-equipment-market-29126
5. TechInvestments.io, "A Primer on the Deposition Market" (AMAT ~21%, Lam ~18%, TEL ~16% of deposition; PVD an AMAT near-monopoly; ALD led by TEL/ASM). https://www.techinvestments.io/p/a-primer-on-the-deposition-market
6. SemiEngineering, "Ruthenium Liners Give Way To Ruthenium Lines." https://semiengineering.com/ruthenium-liners-give-way-to-ruthenium-lines/
7. Applied Materials, "Applied Materials Unveils Chip Wiring Innovations for More Energy-Efficient Computing" (Endura Copper Barrier Seed IMS with Volta Ruthenium CVD; RuCo liner; 33% thinner to 2nm; up to 25% lower resistance; shipping at 3nm; six processes integrated). https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-chip-wiring-innovations-more-energy/
8. BALD Engineering, "Applied Materials Unveils Industry-First Ruthenium-Cobalt Liner..." https://www.blog.baldengineering.com/2025/04/applied-materials-unveils-industry.html
9. Mobility Foresights, "Ruthenium Based Interconnects Market" (~$220M 2024 to ~$1.15B 2030, ~31.7% CAGR; report-mill, directional). https://mobilityforesights.com/product/ruthenium-based-interconnects-market
10. IMARC, "Ruthenium Price Index / Pricing Report" (price run to >$1,400/oz; ~32 tonnes 2025 supply). https://www.imarcgroup.com/ruthenium-pricing-report
11. Discovery Alert, "Ruthenium: The Ultra-Rare Metal Powering AI's Data Boom" (~30-35 t/yr, ~80% South Africa, price spike, data-storage + interconnect demand). https://discoveryalert.com.au/ruthenium-rare-metal-ai-data-storage-2025/
12. EE Times, "AI Drives CapEx Chip Equipment to Record $156B in 2027" (WFE >$100B in 2025, ~$145B 2026, peak ~$156B 2027). https://www.eetimes.com/ai-drives-capex-chip-equipment-to-record-156b-in-2027/
13. SEMI / Semiconductor Intelligence, "CapEx Up for Foundry, Memory" (foundry + memory capex rising on AI; leading-edge prioritised). https://www.semiconductorintelligence.com/capex-up-for-foundry-memory/
14. SemiEngineering, "Extending Copper Interconnects To 2nm" (Cu replaced by Ru or Mo at some levels as soon as 2nm; barrierless materials win below ~20nm CD; Intel subtractive Ru at IEDM 2024). https://semiengineering.com/extending-copper-interconnects-to-2nm/
15. SemiEngineering, "Backside Power Delivery Creates Fab Tool, Thermal Dissipation Barriers" (BPDN power vias/rails need tailored barrier/liner and fill). https://semiengineering.com/backside-power-delivery-creates-fab-tool-thermal-dissipation-barriers/
16. Lam Research Newsroom, "A Deep Dive into Ruthenium's Superiority and Process Modeling" (barrierless Ru lowest line resistance at <~20nm CD; BEOL metal-scheme transition). https://newsroom.lamresearch.com/Analysis-BEOL-Metal-Schemes-Process-Modeling
17. Technology.org, "Ruthenium Prices Triple in One Year as AI Hunger Drains a Metal Nobody Talks About" (price ~$500 to >$1,700/oz; AI/data-storage pull). https://www.technology.org/2026/03/16/ruthenium-prices-triple-in-one-year-as-ai-hunger-drains-a-metal-nobody-talks-about/
18. IMARC, "Ruthenium Price Index, Chart 2026, Trend and Forecast" (Metals Focus ~203k oz 2026 deficit; 7th consecutive deficit; ~32 t 2025 supply). https://www.imarcgroup.com/ruthenium-pricing-report
19. imec, "Imec demonstrates semi-damascene interconnects with fully self-aligned vias at 18nm metal pitch" (two-layer Ru at 16-18nm pitch, >80% yield; ASD-enabled FSAV). https://www.imec-int.com/en/articles/imec-demonstrates-semi-damascene-interconnects-fully-self-aligned-vias-18nm-metal-pitch
