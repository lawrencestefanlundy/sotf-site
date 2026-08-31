---
type: concept
slug: flow-flip-chip-bumping
canonical_name: Flip-chip bumping (C4 / Cu pillar / microbump) (process step)
seq: 45
phase: assembly
related_concepts:
- advanced-packaging
- hybrid-bonding
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
- slug: advanced-packaging
  name: Advanced Packaging
  path: /manufacturing/packaging/advanced-packaging/
  macro: manufacturing
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
---
> Step 45 of 56 in the semiconductor flow (Assembly). Prev: [Wire bonding (process step)](/semiconductor-process-flow/packaging/flow-wire-bonding/) · Next: [Package substrate manufacturing (ABF / glass) (process step)](/semiconductor-process-flow/packaging/flow-package-substrate/)

## What this step does
Bumping puts conductive interconnects on the face of the die so it can be flipped and joined directly to a substrate or another die, replacing the long gold wires of [Wire bonding (process step)](/semiconductor-process-flow/packaging/flow-wire-bonding/). It is a wafer-level step done before [Wafer dicing / singulation (process step)](/semiconductor-process-flow/packaging/flow-wafer-dicing-singulation/). The classic flavour is the C4 solder ball (controlled-collapse chip connection); the modern workhorse is the copper pillar (a plated Cu post capped with SnAg solder); the densest flavour is the microbump for die stacking. Sub-processes inside this step:
- Under-bump metallisation (UBM): sputter a Ti/Cu seed, then plate adhesion/barrier layers ([PVD / sputtering (process step)](/semiconductor-process-flow/frontend/flow-pvd-sputtering/) + [Copper electroplating (ECD) (process step)](/semiconductor-process-flow/frontend/flow-copper-electroplating-ecd/)).
- Photoresist patterning to define bump openings ([Photolithography (coat / expose / develop) (process step)](/semiconductor-process-flow/frontend/flow-photolithography/)).
- Electroplating of the Cu pillar and solder cap.
- Resist strip, seed etch, and reflow to shape the solder.

## Where it sits and why it matters
Bumping is the gateway to every high-performance package. Logic-on-logic chiplets, HBM stacks, CoWoS and every AI accelerator route signal and power through bumps or their successor, the bondless hybrid joint. Pitch is the whole game: C4 solder balls sit around 100-150um, copper pillars push to ~40um, microbumps reach ~10um, and below that you transition to [Hybrid Bonding (Cu-Cu)](/manufacturing/packaging/hybrid-bonding/) (direct Cu-Cu, no bump, sub-5um pitch). The shrink from solder to pillar to microbump to bondless is the central scaling axis of [Advanced Packaging](/manufacturing/packaging/advanced-packaging/). Copper pillar already held ~46% of flip-chip bump revenue in 2024 [1].

## Equipment market
There is no clean "bumping tool" line item; the spend rides inside wafer-level packaging plating and the die/flip-chip bonders. The semiconductor electroplating systems market (the deposition engine for UBM, pillars and RDL) was ~USD 5.9B in 2024, growing ~6.5% CAGR to ~USD 9.8B by 2032 [2]; copper pillar was ~23% of plating-system demand [3]. On the join side, Yole expects TCB and hybrid-bonding back-end equipment to lead a ~USD 1.3B expansion to 2030, with hybrid-bonding tools at ~21% CAGR 2025-2030 [4]. Thermocompression-bonder market shares below are rough.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Lam Research | US | plating leader | SABRE 3D ECD for pillars/TSV/RDL |
| Applied Materials | US | plating co-leader | Nokota/ECD + integrated WLP |
| ACM Research | US/China | rising | Ultra ECP ap; ~USD 430M revenue, fast in AP plating |
| EBARA | Japan | plating | Cu plating + CMP for packaging |
| ASMPT (incl. AMICRA) | HK/Germany | ~28% TCB | high-accuracy flip-chip/TC bonders |
| BESI | Netherlands | ~22% TCB | TCB + hybrid-bonding placement, partner with AMAT |

Concentration note: plating is a US-led near-duopoly (Lam, AMAT) with ACM and EBARA gaining; flip-chip/TC bonding placement is a tighter oligopoly (top four ~70%) led by ASMPT and BESI [5].

## Materials & consumables
This step consumes plating chemistries (Cu, SnAg solder, Ni/Au UBM), photoresist, and the sputter targets for seed. These are recurring per-wafer spend, the annuity layer of the value chain. Suppliers: Element Solutions (MacDermid Alpha), MKS/Atotech (Xenolyte UBM), DuPont/Qnity (Solderon BP Cu-pillar and SnAg cap), Technic (Elevate Tin), plus Tama Chemicals, ADEKA and Shanghai Sinyang [6][7]. The solder-bump-plating-chemicals niche is small in absolute dollars but high-margin and qualification-locked: once a chemistry is designed into a flow it rarely changes, so incumbents earn durable share.

## Volumes, revenue, profitability
Bumping is performed almost entirely captive: TSMC and Samsung bump in-house; advanced OSATs (ASE, Amkor, JCET) run wafer-bump lines at their packaging sites [8]. So the revenue pool splits three ways. (1) Tool vendors: plating + bonder equipment, the figures above; plating-tool gross margins run ~45-50% (Lam/AMAT corporate level). (2) Chemistry vendors: smaller pool, gross margins typically 30-40% but sticky. (3) The bumping service itself sits inside foundry/OSAT wafer-level-packaging revenue, where OSAT operating margins are thin (high-single to mid-teens %) and foundry captive bumping is bundled into the much richer logic wafer price. Microbump itself was a ~USD 0.75B market in 2024 on a Yole read, growing ~28% CAGR to 2030 [9] (rough; pulled from a secondary citation of the Yole deck). The broader flip-chip market was ~USD 38-40B in 2024-25 at ~6-7% CAGR [1][10].

## Market drivers, constraints & trends
Net read: the served market (plating tools + bonders + bump chemistry) is in an accelerating up-cycle, but with a structural ceiling that arrives at the bottom of the pitch ladder. Every advanced AI package still routes through a bumping step, and the near-term scaling of that step is faster than the headline 6-7% flip-chip CAGR suggests.

- **Drivers** — CoWoS, the largest bump consumer, is scaling from ~35k wafers/month (late 2024) toward ~115-130k by end-2026, with total demand roughly tripling from ~370k wafers (2024) to ~1.0M (2026); advanced-packaging allocation, not wafer starts, is the binding constraint on AI hardware [11][14]. HBM is the second pull: bump count per stack rises as layers go 12→16, and SK hynix HBM is sold out through 2025 with ~60%/yr demand growth [12]. Pitch shrink itself lifts plating/chemistry value-add: HBM3E sits at 30-20um, HBM4 moves to ~10um microbumps [12].
- **Constraints** — Hybrid bonding is the structural displacement risk: below ~10um pitch the bondless Cu-Cu joint dissolves the bump-plating step and shifts spend to surface-prep and alignment tools [4]. Bumping inside foundry/OSAT cost-of-goods stays commoditised, so margin accrues only at the tool/chemistry ends [5][6]. Capex intensity and AI cyclicality mean the up-cycle is concentrated and reversible if accelerator demand stalls [11].
- **Trends & inflections to watch** — HBM4 staying on solder microbumps (JEDEC relaxed module height 720→775um, with ~900um mooted for HBM4E) extends the bump-chemistry annuity and pushes full hybrid bonding past ~2028; tripwire: an HBM maker qualifying hybrid-bonded HBM in volume before HBM4E [13]. Panel-level packaging (600x600mm yields 5-6x more units, ~20-30% cost savings, needs slit-coat not spin-coat plating lines) re-tools the bumping/RDL step; tripwire: TSMC or Samsung moving an AI GPU to FOPLP/CoPoS volume in 2027-28 [15]. Glass-core substrate adoption (TSMC) reshapes downstream bump-to-substrate join; tripwire: first AI accelerator shipping on a glass-core panel [15].

## Connections
[Advanced Packaging](/manufacturing/packaging/advanced-packaging/) · [Hybrid Bonding (Cu-Cu)](/manufacturing/packaging/hybrid-bonding/) · **Advanced Packaging Market** · [Copper electroplating (ECD) (process step)](/semiconductor-process-flow/frontend/flow-copper-electroplating-ecd/) · [PVD / sputtering (process step)](/semiconductor-process-flow/frontend/flow-pvd-sputtering/) · [Wire bonding (process step)](/semiconductor-process-flow/packaging/flow-wire-bonding/) · [Package substrate manufacturing (ABF / glass) (process step)](/semiconductor-process-flow/packaging/flow-package-substrate/) · [Wafer dicing / singulation (process step)](/semiconductor-process-flow/packaging/flow-wafer-dicing-singulation/)

## Sources
1. Precedence Research, Flip Chip Market (copper pillar ~46% 2024 share). https://www.precedenceresearch.com/flip-chip-market
2. Verified / Credence Research, Semiconductor Electroplating Systems Market (~USD 5.9B 2024 → ~USD 9.8B 2032, ~6.5% CAGR). https://www.credenceresearch.com/report/semiconductor-electroplating-systems-plating-equipment-market
3. SNS Insider / Maximize, Semiconductor Plating System Market (copper pillar ~23% of plating demand 2024; electroplating ~67%). https://www.maximizemarketresearch.com/market-report/semiconductor-plating-system-market/195202/
4. Yole Group press release, "Advanced packaging fuels transformation in back-end equipment: TCB and hybrid bonding to lead $1.3 billion market expansion by 2030" (hybrid-bonding equipment ~21% CAGR 2025-2030). https://www.yolegroup.com/press-release/advanced-packaging-fuels-transformation-in-back-end-equipment-tcb-and-hybrid-bonding-to-lead-1-3-billion-market-expansion-by-2030/
5. Market Growth Reports / IndexBox, Thermo Compression Bonder & Flip Chip Bonder Market (ASMPT ~28%, BESI ~22%, top four ~70%). https://www.marketgrowthreports.com/market-reports/thermo-compression-bonder-market-101323
6. DataInsights / DuPont-Qnity / Atotech / Technic, Solder Bump Plating Chemicals (Element Solutions, MKS/Atotech, DuPont, Technic, Tama, ADEKA, Sinyang). https://www.dupont.com/electronics-industrial/solder-bump-plating.html
7. Atotech (MKS) semiconductor chemistries, Xenolyte UBM / pillar plating. https://www.atotech.com/products/electronics/semiconductor/
8. Yole / SEMI / SemiconductorX, wafer bumping captive at foundries (TSMC, Samsung) and advanced OSATs (ASE, Amkor, JCET); ASE flip-chip/bumping at full load. https://semiconductorx.com/mfg-back-end-flip-chip-bonding.html
9. Yole Group via SEMI 2025 deck (secondary citation), microbump ~USD 0.75B 2024, ~28% CAGR to 2030 (rough estimate). https://www.semi.org/sites/semi.org/files/2025-06/21_Vishal%20Saroha.pdf
10. Precedence Research, Flip Chip Market (~USD 38-40B 2024-25, ~6.5% CAGR to 2034). https://www.precedenceresearch.com/flip-chip-market
11. DigiTimes / FinancialContent, TSMC CoWoS capacity ramp (~35k→~115-130k wafers/month 2024-2026; demand ~370k→~1.0M wafers; allocation is the binding AI constraint; NVIDIA booked >50% of 2026). https://markets.financialcontent.com/wral/article/tokenring-2026-1-1-the-great-packaging-pivot-how-tsmc-is-doubling-cowos-capacity-to-break-the-ai-supply-bottleneck-through-2026
12. Semiconductor Engineering / Wevolver, HBM bump pitch (HBM3E 30-20um, HBM4 ~10um; SK hynix sold out through 2025, ~60%/yr demand growth). https://semiengineering.com/hbm-leads-the-way-to-defect-free-bumps/
13. Semiconductor Engineering, "HBM4 Sticks With Microbumps, Postponing Hybrid Bonding" (JEDEC height 720→775um, ~900um mooted for HBM4E; full hybrid bonding pushed past ~2028). https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/
14. DigiTimes, TSMC expands CoWoS/SoIC on AI boom (NVIDIA >50% of 2026-27 CoWoS). https://www.digitimes.com/news/a20251210PD218/tsmc-cowos-capacity-nvidia-equipment.html
15. TechTimes / WCCFTech, TSMC FOPLP and CoPoS glass-core panel-level packaging (600x600mm 5-6x units, ~20-30% cost savings, slit-coat vs spin-coat; TSMC glass vs Samsung organic; AI GPU volume 2027-28). https://www.techtimes.com/articles/318385/20260615/tsmc-readies-panel-level-packaging-ai-chips-setting-showdown-samsung.htm
