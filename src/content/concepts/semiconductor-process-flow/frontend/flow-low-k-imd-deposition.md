---
type: concept
slug: flow-low-k-imd-deposition
canonical_name: Low-k dielectric (IMD) deposition (process step)
seq: 33
phase: beol
related_concepts:
- low-k-dielectrics
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
- slug: low-k-dielectrics
  name: Low-K Dielectrics
  path: /materials/functional-layers/low-k-dielectrics/
  macro: materials
---
> Step 33 of 56 in the semiconductor flow (BEOL). Prev: [Contact & middle-of-line (silicide, contact fill) (process step)](/semiconductor-process-flow/frontend/flow-contact-mol-silicide/) · Next: [Damascene patterning (via/trench) (process step)](/semiconductor-process-flow/frontend/flow-damascene-patterning/)

## What this step does
This is the first deposition step of the back-end-of-line (BEOL) interconnect stack. It lays down the insulating film that sits between copper wires, both laterally (intermetal dielectric, IMD) and vertically (interlayer dielectric, ILD). The goal is a dielectric with as low a permittivity (k) as possible, because the RC delay and crosstalk of modern chips is dominated by interconnect parasitics, not transistor switching. The classic film is a carbon-doped oxide (SiOCH, "organosilicate glass") deposited by plasma-enhanced CVD, then made porous to push k lower.

Sub-processes inside this step:
- PECVD of a dense SiOCH "backbone" plus a sacrificial labile organic phase (a "porogen").
- UV cure that burns out the porogen, creating nano-pores and re-crosslinking the matrix for strength (k drops from ~3.0 to ~2.5 to ~2.2).
- Cap / etch-stop and barrier dielectric layers (SiCN, SiC, "BLOk"-type films) deposited in the same tool family.
- At leading nodes: air-gap formation, where the dielectric is deliberately removed between the tightest wires to push effective k toward 1.

## Where it sits and why it matters
Below ~28nm, wire delay overtakes gate delay, so every fraction of a k-point is worth real performance and power. This step is where that fight is won or lost. It is tightly coupled to the next step ([Damascene patterning (via/trench) (process step)](/semiconductor-process-flow/frontend/flow-damascene-patterning/)): the low-k film is fragile and porous, so it has to survive etch, ash, CMP and metal fill without absorbing moisture or cracking. That integration difficulty is precisely why a single vendor has owned the recipe for two decades.

## Equipment market
Dielectric deposition here is overwhelmingly a PECVD (plus a slice of ALD for the thinnest barrier/cap layers) problem. The standalone "low-k deposition equipment" market is not cleanly broken out by credible analysts; it sits inside the broader deposition segment. Anchors: 2024 wafer-fab equipment was ~$115B of equipment (~$140B including services), and the deposition segment was ~$14B (Yole; growing toward ~$24.5B by mid-2030s, roughly 5-6% CAGR). Low-k IMD/ILD PECVD is a low-single-digit-billion slice of that deposition pool, and a rough estimate.

| Vendor | HQ | Est. share (dielectric PECVD) | Notable |
|---|---|---|---|
| Applied Materials | US | dominant, ~majority | Producer Black Diamond is the de facto BEOL low-k standard (BD1 k~3.0, BD2 ~2.5, BD3 ~2.2); also BLOk barrier films |
| Lam Research | US | #2 challenger | Strong in dielectric PECVD + gap-fill; leads adjacent etch/clean |
| Tokyo Electron (TEL) | JP | minority | Broad CVD/coater portfolio; stronger in other deposition niches |
| ASM International | NL | small here | ALD leader; relevant for ultrathin barrier/cap, not the bulk IMD film |
| Kokusai (Hitachi Kokusai) | JP | small | Batch/furnace dielectric CVD |

Concentration note: this is one of the most concentrated steps in the whole flow. Applied Materials' Black Diamond family has been the BEOL low-k workhorse since the 65nm node and remains the production standard at the most advanced logic and memory nodes. AMAT is the deposition leader overall (Lam leads etch); within dielectric PECVD for interconnect, AMAT's position is closer to a near-monopoly than a duopoly. Exact step-level share is not publicly disclosed and the majority figure is an estimate.

## Materials & consumables
Each tool runs continuously on precursor gases and consumables, so the recurring spend is meaningful and stickier than the one-time tool sale. What this step consumes:
- Organosilicon precursors (carbon source for SiOCH): DEMS (diethoxymethylsilane), OMCTS, trimethylsilane/3MS, plus the labile porogen.
- Process gases: oxygen, helium, ammonia, plus etch-stop/barrier precursors.
- UV-cure lamps and chamber kits / parts.

Precursor supply is its own oligopoly. DEMS-class precursors come from Merck KGaA (which owns the former Versum / Air Products electronic-materials line and markets DEMS), Air Liquide (Versum's other heritage), and specialty houses such as Gelest. The precursor is often co-developed and qualified with the tool recipe, which locks the materials vendor in alongside the equipment vendor. The low-k precursor materials pool is a sub-billion-dollar slice of the much larger electronic-specialty-materials market; precise sizing is not cleanly published (rough estimate).

## Volumes, revenue, profitability
Volume scales with BEOL metal layers: an advanced logic chip has 12-18 metal levels, each needing an IMD/ILD deposition pass, so a single advanced wafer can see a dozen-plus passes through this tool family. With ~16M wafer-starts-per-month of capacity industry-wide and rising metal-layer counts, throughput here is large and structurally growing with logic complexity.

Revenue pool: the equipment slice is low-single-digit billions per year (a fraction of the ~$14B deposition segment); the recurring precursor/parts pool is smaller but higher-quality. The margin profile is excellent at the capturing layer. Applied Materials runs ~47-48% gross and ~29-30% operating margins at the corporate level, and its leadership PECVD products plus the attached service/spares revenue sit at or above that. Precursor suppliers (Merck Electronics, Air Liquide Advanced Materials) earn high-recurring, lower-gross chemicals margins. The margin accrues to the tool vendor (AMAT first) and, more durably, to the qualified service/precursor annuity, not to the fab.

## Competitive landscape & value capture
The moat is integration knowledge, not the chemistry alone. A low-k recipe is co-engineered with the etch, ash, cure and CMP steps; switching vendors means requalifying the whole BEOL module, so the incumbent (Black Diamond) has compounded share across nodes for ~20 years. Value accrues to (1) Applied Materials, the dominant tool + recipe owner, (2) the precursor oligopoly (Merck/Versum, Air Liquide, Gelest) on a recurring basis, and (3) the fab, which captures the device-performance upside but pays the toll. The frontier moving from porous low-k toward air-gap and alternative interconnect materials keeps the difficulty (and the moat) intact.

## Market drivers, constraints & trends
Net read: the served market grows with leading-edge logic, but it is cyclical and the RC fight is migrating away from the dielectric, so the dielectric slice grows slower than the deposition pool around it.

- **Drivers**
  - Sub-2nm / GAA capacity build-out is the prime pull: SEMI puts 300mm fab equipment at ~$133B in 2026 rising to ~$151B in 2027, with Logic & Micro the lead segment (~$175B invested 2026-2028), and foundry sub-2nm the driver [11][12].
  - Metal-layer count keeps rising at advanced logic (12-18+ levels), so each new node multiplies IMD/ILD passes per wafer [14].
  - Backside power delivery adds a *new* dielectric module: a back-side ILD plus backside-RDL build, a net-additive deposition step that did not exist on frontside-only flows [13].
  - Advanced-packaging RDL pulls an adjacent low-Dk pool (photo-imageable dielectrics, Dk ~2.9 at 10GHz) as AI/HPC heterogeneous integration scales [15].

- **Constraints**
  - The physics is capping out: porous low-k below k~2.2 is mechanically fragile (peeling, package-stress failure), so each further k-point is harder and slower to qualify [14][16].
  - The RC battle has shifted to the *metal* side (thinner/barrier-free liners, Cu to Ru/Mo/Rh) where the incremental spend is now going, not to the dielectric film [17][18].
  - Near-monopoly capture (AMAT Black Diamond) means a stable but not expanding vendor TAM, and the whole step rides WFE cyclicality.

- **Trends & inflections to watch**
  - Advanced low-k (ALK): IBM showed a high-modulus dense (k~3.2) / lightly-porous (k~2.8-3.0) ILD for 2nm-and-beyond at IITC 2025 (Busan, 2-5 Jun 2025). Tripwire: a foundry naming an ALK-class film in a qualified 1.4nm/A14-era flow [16][18].
  - Air-gap integration at 18-26nm metal pitch in semi-damascene is in R&D. Tripwire: first air-gap module in a volume node [14][16].
  - GAA-plus-backside-power: TSMC A16 is slated for H2 2026. Tripwire: A16 reaching HVM, which makes the back-side ILD a recurring line item [13].
  - Barrier-free / post-Cu metallisation (Ru, Rh damascene) at 2nm. Tripwire: a post-Cu metal in production, which re-rates spend toward the conductor and away from this step [17][18].

## Connections
- [Low-K Dielectrics](/materials/functional-layers/low-k-dielectrics/)
- **Deposition Materials Process Market**
- Prev: [Contact & middle-of-line (silicide, contact fill) (process step)](/semiconductor-process-flow/frontend/flow-contact-mol-silicide/) · Next: [Damascene patterning (via/trench) (process step)](/semiconductor-process-flow/frontend/flow-damascene-patterning/)
- Related deposition steps: [CVD / PECVD deposition (process step)](/semiconductor-process-flow/frontend/flow-cvd-pecvd/), [Atomic layer deposition (ALD) (process step)](/semiconductor-process-flow/frontend/flow-ald-atomic-layer-deposition/), [PVD / sputtering (process step)](/semiconductor-process-flow/frontend/flow-pvd-sputtering/)

## Sources
1. Yole Group / Electronics Weekly, WFE 2024 ~$115B equipment (~$140B incl. services), deposition segment ~$14B: https://www.electronicsweekly.com/news/business/fab-equipment-sales-to-top-184bn-in-2030-2025-08/
2. Yole, "Wafer Fab Equipment market to hit $184 billion by 2030": https://www.yolegroup.com/press-release/wafer-fab-equipment-wfe-market-to-hit-184-billion-by-2030-for-equipment-and-services-driven-by-specialized-segment-growth-and-global-manufacturing-shifts/
3. Applied Materials, Producer Black Diamond PECVD product page (k-values, node coverage): https://www.appliedmaterials.com/us/en/product-library/producer-black-diamond-pecvd.html
4. Applied Materials, Producer BLOk PECVD (barrier dielectric): https://www.appliedmaterials.com/us/en/product-library/producer-blok-pecvd.html
5. PMC review, "The Evolution of Organosilicon Precursors for Low-k Interlayer Dielectric Fabrication": https://pmc.ncbi.nlm.nih.gov/articles/PMC8432693/
6. Merck KGaA (EMD), DEMS precursor product page: https://www.emdgroup.com/en/expertise/semiconductors/offering/diethoxymethylsilane.html
7. SemiEngineering, "Reducing BEOL Parasitic Capacitance Using Air Gaps": https://semiengineering.com/reducing-beol-parasitic-capacitance-using-air-gaps/
8. Yole, "Semiconductor equipment market share reshuffles" (vendor shares, Lam/TEL deposition share moves): https://www.yolegroup.com/strategy-insights/semiconductor-equipment-market-share-reshuffles-amid-memory-demand-decline/
9. Marketresearchfuture, CVD equipment market ~$23B 2024 (report-mill, treat as loose upper bound for whole CVD incl. tube/furnace): https://www.marketresearchfuture.com/reports/semiconductor-chemical-vapor-deposition-equipment-market-29126
10. AIP Applied Physics Reviews, "Progress in advanced low-k and ultralow-k dielectrics for VLSI interconnects": https://pubs.aip.org/aip/apr/article/1/1/011306/123919/Progress-in-the-development-and-understanding-of
11. NineScrolls / SEMI, "Global 300mm Fab Equipment Spending to Hit $133 Billion in 2026, $151 Billion in 2027 — AI Triggers Historic Investment Cycle": https://ninescrolls.com/news/semi-global-300mm-fab-equipment-spending-to-hit-133-billion-in-2026-151-billion-
12. SEMI, "Global Semiconductor Equipment Sales Projected to Reach a Record of $156 Billion in 2027" (Logic & Micro lead, sub-2nm foundry driver): https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports
13. SemiAnalysis, "Clash of the Foundries: Gate All Around + Backside Power at 2nm" (back-side ILD, TSMC A16 GAA+BSPDN H2 2026, N2 ramp): https://newsletter.semianalysis.com/p/clash-of-the-foundries
14. Semiconductor Digest, "Scaling the BEOL: A Toolbox Filled with New Processes, Boosters and Conductors" (air-gap at 18-26nm pitch semi-damascene, mechanical stability limits, rising layer count): https://www.semiconductor-digest.com/scaling-the-beol-a-toolbox-filled-with-new-processes-boosters-and-conductors/
15. ScienceDirect, "Low-temperature photo imageable dielectric for redistribution layers in advanced packaging application" (low-Dk PID ~2.9 at 10GHz for AI/HPC RDL): https://www.sciencedirect.com/science/article/abs/pii/S136980012400979X
16. IBM Research, "Novel Advanced Low-k Dielectric for 2 nm and Beyond Cu and Post Cu Dual Damascene BEOL Interconnect" (ALK dense k~3.2 / porous k~2.8-3.0, high modulus, VLSI/IITC 2025): https://research.ibm.com/publications/novel-advanced-low-k-dielectric-for-2-nm-and-beyond-cu-and-post-cu-dual-damascene-beol-interconnect-technologies
17. Mark Lapedus, "Scaling Copper Interconnects To 2nm And Beyond" (Cu to Ru/Mo, RuCo liner, barrier-free, spend migrating to metal): https://marklapedus.substack.com/p/scaling-copper-interconnects-to-2nm
18. TSPA Semiconductor, "From Barrier-Limited to Barrier-Free: IBM's New Blueprint for BEOL Scaling" (ALK + Rhodium damascene post-Cu, 1.4nm targets, IITC 2025 Busan 2-5 Jun): https://tspasemiconductor.substack.com/p/from-barrier-limited-to-barrier-free
