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

## Connections
[Semiconductor Foundries](/manufacturing/foundry-design/foundry/) · [Specialty Foundries (TFLN, GaN, SiC, photonic)](/manufacturing/foundry-design/specialty-foundries/) · theses: **Specialty Silicon Non Leading Edge** · **New Uk Fab** · **Sovereign Electronics Manufacturing**