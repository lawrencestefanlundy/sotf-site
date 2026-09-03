---
type: concept
slug: flow-foundry-fabrication-services
canonical_name: Wafer foundry / fabrication services (process step)
seq: 19
phase: fabservices
related_concepts:
- foundry
- specialty-foundries
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
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors:
- slug: foundry
  name: Semiconductor Foundries
  path: /manufacturing/foundry-design/foundry/
  macro: manufacturing
- slug: specialty-foundries
  name: Specialty Foundries (TFLN, GaN, SiC, photonic)
  path: /manufacturing/foundry-design/specialty-foundries/
  macro: manufacturing
---
> Step 19 of 56 in the semiconductor flow (FabServices). Prev: [Epitaxial deposition (epi) (process step)](/semiconductor-process-flow/frontend/flow-epitaxy/) · Next: [Wafer cleaning & surface prep (process step)](/semiconductor-process-flow/frontend/flow-wafer-cleaning/)

## What this step does
This is not a single physical step but the business layer that wraps the entire front-end-of-line (transistors) and back-end-of-line (interconnect) into a contract-manufacturing service: a fabless customer (Nvidia, Apple, Qualcomm) hands over a chip design and the foundry runs every wafer process to deliver finished wafers. The foundry sells access to a qualified process flow plus the capital, yield learning and process design kit (PDK) that make a design manufacturable. It bundles, in sequence, hundreds of individual unit steps already mapped in this flow:
- Lithography / patterning, etch, deposition, ion implant, CMP, cleaning, metrology and inspection (the per-step physics)
- Process integration: tying ~1,000+ steps into a yielding flow at a named node (N3, N5, 28nm)
- PDK + IP libraries, multi-project-wafer (MPW) shuttle runs, test, and increasingly advanced packaging (CoWoS, chiplets)

## Where it sits and why it matters
The foundry is the single largest profit pool in the whole flow because it captures the integration premium: equipment and materials vendors sell tools and inputs, but the foundry is the only layer that converts them into yielding chips at scale. It is the chokepoint of the entire electronics economy. Leading-edge logic (5nm and below) is effectively a monopoly held by TSMC, which makes this step the most geopolitically contested node in the supply chain and the anchor for **Sovereign Electronics Manufacturing**.

## Equipment market
The foundry IS the buyer of wafer fab equipment (WFE), so the "equipment market" here is the tool spend foundries make. WFE was roughly USD 86bn in 2024 and is forecast by Yole toward ~USD 184bn (equipment + services) by 2030, a high-single-digit CAGR pulled by the AI capex super-cycle [1][2]. The "Big Five" hold ~70% of WFE [2].

| Vendor | HQ | Est. share of WFE | Notable |
|---|---|---|---|
| Applied Materials | US | ~18-20% | Deposition, etch, implant, process integration breadth |
| ASML | Netherlands | ~18-22% | Lithography monopoly; sole EUV supplier (leading-edge gatekeeper) |
| Lam Research | US | ~12-15% | Etch + deposition, strongest in memory/3D |
| Tokyo Electron (TEL) | Japan | ~12-15% | Coat/develop track, etch, deposition, cleaning |
| KLA | US | ~6-8% | Process control, metrology, inspection (near-monopoly in inspection) |

Concentration note: each sub-step is itself an oligopoly or monopoly (ASML in EUV, KLA in inspection), so the foundry faces near-zero supplier substitutability on the critical tools. That pricing power is why WFE vendors run 45-50%+ gross margins and is the cleanest public-markets exposure to the foundry build-out (the "picks and shovels"). Shares are rough estimates blended across report sources.

## Materials & consumables
Running the flow consumes a continuous stream of inputs the foundry buys every wafer-start: bare/epi silicon wafers, photoresists and EUV resist, wet chemicals, electronic/specialty gases, CMP slurries and pads, photomasks, sputter targets and electrostatic chucks. SEMI put the 2024 global semiconductor materials market at ~USD 67.5bn (fab/front-end materials ~USD 45-46bn of that), growing ~6% CAGR [3][7]. Global silicon wafer area shipments were ~13.4 billion square inches in 2024 [3]. Unlike the one-time tool purchase, materials are recurring revenue that scales with wafer volume and utilisation, which makes leaders (Shin-Etsu and SUMCO in wafers, JSR/TOK/Shin-Etsu in resist, Merck/Linde/Air Liquide in gases and specialty chemistry) defensive, annuity-like businesses. Air Liquide and Merck KGaA are the European-listed names with direct foundry-materials pull.

## Volumes, revenue, profitability
The pure-play foundry revenue pool was ~USD 122bn in 2024 and grew to roughly USD 165-170bn in 2025 on AI demand [1][4][8]. The leading-edge vs mature split is starkly two-tier: advanced nodes run >90% utilisation and carry the growth, while mature nodes (28nm and above) sat at only ~65-70% utilisation in 2024-25 with margin pressure and overcapacity [9][10]. Mature-node share of foundry revenue is falling from ~54% (2021) toward ~36% (2025) [9].

Margins split the same way. The margin earner is the leading-edge integrator:
- TSMC 2024: revenue USD 90.1bn, gross margin 56.1%, operating margin 45.7%, capex USD 29.8bn (~33% of revenue) [5][6]. 2025 gross margin rose to ~60% on utilisation [4]. Roughly three-quarters of revenue is 7nm-and-below.
- GlobalFoundries 2024 (mature/specialty): revenue USD 6.75bn, gross margin ~24.5%, operating margin ~10% [11].
- UMC: gross margin ~29% at ~79% utilisation [12].
- Samsung Foundry and Intel Foundry are loss-making at the leading edge; Intel Foundry lost ~USD 2.2bn in 2024 [13].

So the foundry layer earns the margin only where it holds a process-node lead; mature-node contract manufacturing is a thin-margin, capital-heavy commodity. Capex intensity (~30-35% of revenue at the leading edge) is the structural barrier and the reason the layer consolidates.

## Competitive landscape & value capture
The moat is cumulative: hundreds of billions in capex, a decade of yield learning, a deep PDK/IP ecosystem and customer switching costs that compound at each node. Value accrues overwhelmingly to TSMC (~64% of foundry revenue in 2024, ~70% in 2025) [1][8], and within the supply chain to the monopoly tool vendors (ASML, KLA) and annuity materials suppliers. Europe / seed-relevant: the European edge is in specialty foundries, not leading-edge logic. X-FAB (Erfurt, ~USD 700-750m revenue) leads analog / high-voltage BCD-on-SOI; STMicroelectronics and Infineon run IDM-plus-foundry capacity in BCD and FD-SOI; Tower (now Israeli/under Intel-adjacent ownership) does analog, RF, power and silicon photonics. These are the natural home for **Specialty Silicon Non Leading Edge** and **New Uk Fab** thinking.

## Market drivers, constraints & trends
Net read: the served market (equipment plus materials the foundry buys) is in a structural up-slice, but a two-tier one where almost all the growth concentrates at the leading edge and in packaging while mature-node tool demand softens.

- **Drivers** — Total semiconductor equipment sales are forecast to a record ~USD 156bn in 2027, with the WFE segment growing ~9.0% in 2026 and ~7.3% in 2027, and SEMI projecting double-digit 300mm fab-equipment spend growth in both years [15][16]. The AI capex super-cycle is the pull: pure-play foundry revenue grew ~30% year-on-year in Q1 2026 on AI GPU/ASIC orders [17]. Materials are the recurring annuity riding wafer volume: the market reached ~USD 73.2bn in 2025 (+6.8%), fab materials ~USD 45.8bn (+5.4%) with lithography materials posting double-digit growth as process intensity climbs [18].
- **Constraints** — Mature-node (28nm+) overcapacity, much of it Chinese build-out, caps the trailing-edge tool/materials pool; China equipment spend is falling from its 2024 record of ~USD 49.5bn after front-loaded buying ahead of controls [17][19]. US export controls (24 tool types, 140+ Entity List additions) ring-fence leading-edge tool sales [19]. Capex intensity (~30-35% of revenue) and deep cyclicality keep the layer concentrated and sensitive to a single AI-capex air-pocket.
- **Trends & inflections to watch** — Advanced packaging is the second engine: TSMC is quadrupling CoWoS toward ~130k wafers/month by late 2026, and packaging materials grew ~9.3% to USD 27.4bn in 2025 with advanced-packaging materials compounding ~12% [18][20]; tripwire: HBM4 hybrid-bonding moving to volume on the Nvidia Rubin / N3P ramp through 2026 [20]. High-NA EUV (EXE:5200B, 175 wph, in commercial production Jan 2026) is the leading-edge re-rater; tripwire: first high-volume High-NA node in 2027-28, given TSMC kept 0.33-NA for N2/A16 and pushed A16 to 2027 [21][22].

## Connections
[Semiconductor Foundries](/manufacturing/foundry-design/foundry/) · [Specialty Foundries (TFLN, GaN, SiC, photonic)](/manufacturing/foundry-design/specialty-foundries/) · theses: **Specialty Silicon Non Leading Edge** · **New Uk Fab** · **Sovereign Electronics Manufacturing**

## Sources
1. Astute Group / TrendForce, "$165B in 2025: Advanced Nodes Drive Foundry Revenue" — https://www.astutegroup.com/news/industrial/165b-in-2025-advanced-nodes-drive-foundry-revenue-to-record-high/
2. Yole Group, "Wafer Fab Equipment (WFE) market to hit $184 billion by 2030" — https://www.yolegroup.com/press-release/wafer-fab-equipment-wfe-market-to-hit-184-billion-by-2030-for-equipment-and-services-driven-by-specialized-segment-growth-and-global-manufacturing-shifts/
3. SEMI, 2024 Silicon Shipment Data / materials market — https://www.semi.org/en/products-services/market-data/materials
4. Foundry market outlook 2025 (PCIM/Mesago) — https://news.pcim.mesago.com/foundry-market-outlook-2025-ai-and-advanced-technologies-drive-growth-a-99123fe2cd554408653ccfe4ae7d890c/
5. TSMC FY2024 6-K (SEC) — https://www.sec.gov/Archives/edgar/data/0001046179/000104617925000004/a4q24e_withguidancexfinal.htm
6. TrendForce, "TSMC Projects Q1 Gross Margin... 2025 CapEx" — https://www.trendforce.com/news/2025/01/16/news-tsmc-projects-q1-gross-margin-to-hold-steady-at-58-with-2025-capex-rising-up-to-usd-42-billion/
7. Research and Markets / SEMI, Semiconductor Fabrication Materials market — https://www.researchandmarkets.com/report/semiconductor-fabrication-material
8. Design-Reuse / Counterpoint, "Global foundry revenue Q2 2025, TSMC 70% share" — https://www.design-reuse.com/news/202529294-global-foundry-revenue-surged-to-41-7-billion-in-q2-2025-with-tsmc-capturing-a-record-70-percent-market-share/
9. Tom's Hardware, "Trailing-edge foundry roadmaps (GF, UMC, SMIC)" — https://www.tomshardware.com/tech-industry/semiconductors/the-trailing-edge-foundry-roadmap-examined
10. EE Times Asia, "AI, Smartphone Demand in Leading Edge Nodes... 3Q 2024" — https://www.eetasia.com/ai-smartphone-demand-in-leading-edge-nodes-propel-global-foundry-industry-in-3q-2024/
11. GlobalFoundries 4Q/FY2024 6-K (SEC) — https://www.sec.gov/Archives/edgar/data/0001709048/000170904825000017/globalfoundries4q2024earni.htm
12. Mark Lapedus / Semiecosystem, Q1 '25 foundry earnings — https://marklapedus.substack.com/p/q1-25-foundry-earnings-hit-or-miss-b51
13. Mark Lapedus / Semiecosystem, foundry rankings + Intel Foundry losses — https://marklapedus.substack.com/p/tsmc-tops-new-foundry-rankings-samsung
14. X-FAB corporate (specialty foundry) — https://www.xfab.com/
15. SEMI, "Global Semiconductor Equipment Sales Projected to Reach a Record of $156 Billion in 2027" (Dec 2025) — https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports
16. SEMI, "SEMI Projects Double-Digit Growth in Global 300mm Fab Equipment Spending for 2026 and 2027" — https://www.semi.org/en/semi-press-release/semi-projects-double-digit-growth-in-global-300mm-fab-equipment-spending-for-2026-and-2027
17. Deloitte, "2026 Semiconductor Industry Outlook" (foundry/AI demand, mature-node) — https://www.deloitte.com/us/en/insights/industry/technology/technology-media-telecom-outlooks/semiconductor-industry-outlook.html
18. SEMI, 2025 Semiconductor Materials Market ($73.2bn; fab materials $45.8bn; packaging materials $27.4bn) — https://www.semi.org/en/products-services/market-data/materials
19. CSIS, "China's Mature Semiconductor Overcapacity: Does It Exist and Does It Matter?" + US export-control scope — https://www.csis.org/analysis/chinas-mature-semiconductor-overcapacity-does-it-exist-and-does-it-matter
20. FinancialContent, "TSMC to Quadruple Advanced Packaging Capacity: 130,000 CoWoS Wafers Monthly by Late 2026" (HBM4 hybrid bonding) — https://markets.financialcontent.com/stocks/article/tokenring-2026-2-5-tsmc-to-quadruple-advanced-packaging-capacity-reaching-130000-cowos-wafers-monthly-by-late-2026
21. FinancialContent, "ASML's $350M High-NA EUV Machines Hit the Production Floor" (EXE:5200B, 175 wph) — https://markets.financialcontent.com/stocks/article/tokenring-2026-1-26-printing-the-2nm-era-asmls-350-million-high-na-euv-machines-hit-the-production-floor
22. TrendForce, "TSMC Latest Roadmap: A16 Volume Production Delayed to 2027; N2/A16 without High-NA" — https://www.trendforce.com/news/2026/04/23/news-tsmc-unveils-latest-roadmap-a12-a13-set-for-2029-without-high-na-euv-a16-volume-production-delayed-to-2027/
