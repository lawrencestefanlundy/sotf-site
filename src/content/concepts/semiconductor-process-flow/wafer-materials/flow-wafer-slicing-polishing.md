---
type: concept
slug: flow-wafer-slicing-polishing
canonical_name: Wafer slicing, lapping & polishing (process step)
seq: 17
phase: wafer
related_concepts:
- cmp-chemical-mechanical-planarisation
- materials-process
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
sources_7d: 1
sources_30d: 2
recent_mentions:
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
neighbors:
- slug: cmp-chemical-mechanical-planarisation
  name: Chemical Mechanical Planarisation
  path: /manufacturing/equipment-processes/cmp-chemical-mechanical-planarisation/
  macro: manufacturing
- slug: materials-process
  name: Materials & Process
  path: /materials/advanced-materials/materials-process/
  macro: materials
---
> Step 17 of 56 in the semiconductor flow (Wafer). Prev: [Crystal growth & ingot (Czochralski/Float-Zone) (process step)](/semiconductor-process-flow/wafer-materials/flow-crystal-growth-ingot/) · Next: [Epitaxial deposition (epi) (process step)](/semiconductor-process-flow/frontend/flow-epitaxy/)

## What this step does
This step turns a single-crystal silicon ingot (boule) into the flat, mirror-finish bare wafers that fabs buy. The ingot is cropped, ground to a precise diameter, oriented (notch/flat), and then sliced into thin discs, after which each disc is flattened, etched, polished and cleaned to angstrom-level smoothness. The output is a "prime" 300mm polished wafer ready for epitaxy or device fabrication. Sub-processes:
- Cropping and outer-diameter grinding, notch grinding, orientation.
- Slicing the ingot into wafers (diamond multi-wire saw).
- Edge profiling/grinding, lapping or double-side fine grinding to remove saw damage and improve flatness.
- Wet etch to relieve subsurface damage, then double-side and final single-side polish (a bare-wafer CMP step).
- Cleaning, metrology (flatness/nanotopography), sorting, packaging.

## Where it sits and why it matters
It is the back half of wafer manufacturing, between [Crystal growth & ingot (Czochralski/Float-Zone) (process step)](/semiconductor-process-flow/wafer-materials/flow-crystal-growth-ingot/) and [Epitaxial deposition (epi) (process step)](/semiconductor-process-flow/frontend/flow-epitaxy/). Everything downstream inherits the flatness, nanotopography and defectivity set here, so at advanced nodes (2nm/3nm logic, HBM stacks) the flatness and edge spec out of this step directly caps lithography depth-of-focus and device yield. It is also where most of the value of a finished bare wafer is added: slicing and polishing are the capital- and consumable-intensive part of converting a cheap polysilicon ingot into a high-spec wafer.

## Equipment market
There is no clean public number for "slicing + lapping + polishing tools" in isolation; report-mill TAMs disagree by 3x depending on whether back-end dicing and advanced-packaging thinning are bundled in. Best triangulation: the wafer polishing-and-grinding equipment segment is roughly $2.8B (2024), at a mid-single-digit CAGR of ~4.7% to ~$3.7B by 2030 [4]; diamond-wire slicing tools add another roughly $0.5-1B. So the front-end-wafer-making slice of this step is a ~$2-3B/yr equipment pool, modest versus litho or deposition, and cyclical with wafer-maker capex.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| DISCO | Japan | Leader in grinders/dicers (>70% in grinding) | Grinders, grinding wheels, laser saws, planarisation; ~36% operating margin [2] |
| Tokyo Seimitsu (Accretech) | Japan | #2 grinding/dicing | DISCO + Tokyo Seimitsu ~most of grinding/dicing [2] |
| Komatsu NTC | Japan | Leading slicer | Diamond multi-wire saws (ND-series) for ingot slicing [3] |
| Takatori | Japan | Leading slicer | Diamond-wire and slurry slicing of hard materials [3] |
| Lapmaster Wolters (ex-Peter Wolters) | Germany | Leader in DSP/lapping | Double-side polish/lap; AC-series prime-wafer tools [5] |

Concentration note: tool supply is a Japan-dominated oligopoly (DISCO, Tokyo Seimitsu, Komatsu NTC, Takatori) with one significant European exception in double-side polishing/lapping (Lapmaster Wolters, ~EUR250m revenue). DISCO is the standout franchise (near-lockdown on grinding, ~36% operating margin [2]).

## Materials & consumables
This step is consumable-heavy, which is where the recurring revenue sits. Per-wafer it consumes: diamond cutting wire (single-use, kerf now ~60-80um vs 200um for old slurry wire [3]), grinding wheels (DISCO supplies its own), lapping abrasives, polishing pads, and final-polish slurry. The relevant slurry here is colloidal-silica chemistry for bare-silicon stock removal and final polish, a subset of the broader CMP slurry market (~$2.2B in 2024, ~$3.1B by 2032 [6]); bare-wafer polish is a few hundred million of that. Top slurry/pad suppliers: DuPont/CMC Materials (ex-Cabot Microelectronics, share leader), Fujimi (strong in bare-silicon final polish), Resonac (ex-Hitachi Chemical), Versum/Merck, Saint-Gobain [6]. Consumables are the attractive layer: razor-and-blades economics, qualified-in per recipe, sticky once spec'd.

## Volumes, revenue, profitability
Unit volume is enormous: worldwide silicon shipped ~12,973 million square inches in 2025 (+5.8% YoY), up from 12,174 MSI in 2024 [7], the majority 300mm. The wafer (materials) revenue pool is ~$14.6B in 2025, forecast ~$20.2B by 2030 at ~6.7% CAGR [1]; slicing/lapping/polishing is the value-add core of that pool. Margins split by layer:
- Wafer makers (Shin-Etsu, SUMCO): cyclical. Both saw operating profit fall sharply in the 2024 trough (Shin-Etsu wafer/silicones operating profit down ~55% H1 2024) [8], recovering on AI/HBM demand into 2025-26. Through-cycle operating margins are typically high-teens to ~30% in upcycles for the leaders.
- Tool vendors: DISCO earns ~36% operating margin [2], best-in-class; lapping/polishing tool makers are lower.
- Consumables: slurry/pad/wire suppliers run structurally high gross margins (frequently 40%+) on recurring volume.
The margin accrues to (a) DISCO on grinders/wheels and (b) the consumables suppliers, more reliably than to the cyclical wafer makers themselves.

## Market drivers, constraints & trends
Net read: the served pool splits into a cyclical, oversupply-threatened bare-wafer part and a structurally accelerating thinning/grinding part, so the blended trajectory is steady-to-accelerating, paced by advanced-packaging tool intensity.
- **Drivers** — AI/HBM and sub-2nm logic are pulling polished-wafer and grinding demand: silicon shipments resumed growth to ~13,076 MSI in 2025 (+5.4%), led by a ~7% rise in 300mm for AI/HPC and HBM [9], and SEMI projects 300mm fab equipment spend at $133B in 2026 (+18%) and $151B in 2027 (+14%) [10]. The high-margin layer is wafer thinning: this back-end pool is ~$582M in 2025 growing to ~$845M by 2030 as TSV-reveal grinding and sub-100um dies go mainstream across HBM stacks and logic [11]. HBM4 raises per-wafer grind/CMP intensity over standard DRAM [9].
- **Constraints** — Chinese bare-wafer capacity is the bear: Eswin alone targets 1.2M 12-inch wafers/month by 2026 (>10% global share) and 6-inch is already in discounted oversupply [12], capping bare-wafer pricing and slicing-tool capex even as units rise. GlobalWafers saw prices bottoming only in 1Q26 [12]; the wafer-maker part eats the cycle.
- **Trends & inflections to watch** — Backside power delivery at 2nm forces new ultra-thin grinding/CMP to ~500nm remaining silicon, with imec and DISCO co-developing uniformity [13]; tripwire: TSMC/Samsung/Intel 2nm BSPDN volume ramp confirmed 2026-27. Glass-substrate panel-level packaging (Intel Clearwater Forest shipping, Samsung 2027 ramp [14]) shifts value toward panel tools and away from round-wafer processing; tripwire: a 2027 high-volume glass-PLP AI part. Hybrid bonding scaling (bonders ~$152M→$397M, 21% CAGR [11]) lifts demand for sub-1um wafer flatness and thinning.

## Connections
[Chemical Mechanical Planarisation](/manufacturing/equipment-processes/cmp-chemical-mechanical-planarisation/) (final polish is a bare-wafer CMP step; same slurry/pad supply chain) · [Materials & Process](/materials/advanced-materials/materials-process/) (slurries, abrasives, diamond wire as process materials) · thesis: **Specialty Silicon Non Leading Edge** (200mm wafer supply, where SUMCO is exiting 200mm to chase 300mm AI-grade [1], tightens specialty-node substrate availability).

## Sources
1. Mordor Intelligence, Semiconductor Silicon Wafer Market ($14.6B 2025 → $20.2B 2030, 6.7% CAGR; five-firm shares; SUMCO 200mm exit). https://www.mordorintelligence.com/industry-reports/semiconductor-silicon-wafer-market
2. SemiAnalysis, "DISCO Corporation: The World Leader In Semiconductor Capital Equipment For Cutting, Grinding, Polishing" (leadership, ~36% operating margin). https://newsletter.semianalysis.com/p/disco-corporation-the-world-leader
3. Valuates / industry sources, diamond wire saw and slicer vendors (Komatsu NTC, Takatori, Toyo; kerf 60-80um). https://reports.valuates.com/market-reports/QYRE-Auto-7Z16813/global-semiconductor-diamond-wire-saw
4. Research and Markets, Semiconductor Wafer Polishing and Grinding Equipment ($2.80B 2024 → $3.66B 2030, 4.7% CAGR). https://www.researchandmarkets.com/reports/6055983/semiconductor-wafer-polishing-grinding-equipment
5. Lapmaster Wolters (double-side polish/lap tools; ~EUR250m turnover; AC-series prime-wafer machines). https://www.lapmaster-wolters.com/
6. Coherent / industry sources, CMP slurry market (~$2.16B 2024 → $3.13B 2032; top-5 ~64%; Fujimi, CMC/DuPont, Resonac). https://www.coherentmarketinsights.com/market-insight/cmp-slurry-market-4039
7. SEMI, 2025 Annual Silicon Wafer Shipments (12,973 MSI 2025, +5.8%; 12,174 MSI 2024). https://www.semi.org/en/semi-press-release/semi-reports-2025-annual-worldwide-silicon-wafer-shipments-and-revenue-results
8. SemiMedia, Shin-Etsu / SUMCO 2024 wafer-demand decline (operating profit down ~55% H1 2024). https://www.semimedia.cc/17352.html
9. Semiconductor Digest / SEMI, AI and 300mm drive 2025 silicon wafer growth (13,076 MSI 2025, +5.4%; 300mm +7%; HBM4 higher per-wafer grind/CMP intensity). https://www.semiconductor-digest.com/ai-and-300mm-demand-drive-2025-silicon-wafer-growth/
10. SEMI / PR Newswire, Global 300mm fab equipment spending ($133B 2026 +18%, $151B 2027 +14%; AI logic + HBM). https://www.prnewswire.com/news-releases/semi-projects-double-digit-growth-in-global-300mm-fab-equipment-spending-for-2026-and-2027-302730416.html
11. Yole / industry sources via search, wafer thinning equipment (~$582M 2025 → ~$845M 2030; hybrid bonders ~$152M 2025 → ~$397M 2030, 21.1% CAGR; DISCO leads thinning, Accretech #2). https://www.yolegroup.com/strategy-insights/advanced-packaging-is-the-engine-driving-back%E2%80%91end-equipment-growth/
12. AsiaNews / Digitimes, China silicon-wafer expansion + oversupply (Eswin 1.2M 12-inch wpm by 2026, >10% global share; 6-inch discounted oversupply; GlobalWafers prices bottoming 1Q26). https://asianews.network/chinas-silicon-wafer-rise-adds-pressure-in-ai-chip-race/
13. Semiconductor Engineering, Backside power delivery at 2nm (thinning to ~500nm remaining Si; imec + DISCO uniformity work; new grinding/CMP/etch in fab). https://semiengineering.com/backside-power-delivery-gears-up-for-2nm-devices/
14. TrendForce / FinancialContent, Glass-substrate panel-level packaging (Intel Clearwater Forest shipping glass core; Samsung 2027 mass-production ramp; 2026 "year of validation"). https://www.financialcontent.com/article/tokenring-2026-2-2-glass-substrates-intel-and-samsung-pivot-to-next-gen-ai-packaging
