---
type: concept
slug: flow-mask-data-prep-opc
canonical_name: Mask data prep & computational litho (OPC/ILT) (process step)
seq: 13
phase: design
related_concepts:
- computational-lithography
- eda-design-tools
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
- slug: computational-lithography
  name: Computational Lithography
  path: /manufacturing/lithography/computational-lithography/
  macro: manufacturing
- slug: eda-design-tools
  name: EDA & Design Tools
  path: /manufacturing/foundry-design/eda-design-tools/
  macro: manufacturing
---
> Step 13 of 56 in the semiconductor flow (Design). Prev: [Physical verification (DRC/LVS/DFM) (process step)](/semiconductor-process-flow/design/flow-physical-verification-drc-lvs/) · Next: [Photomask manufacturing (process step)](/semiconductor-process-flow/frontend/flow-photomask-manufacturing/)

## What this step does
This is where a verified, clean physical layout is turned into the corrected data a photomask writer can actually shoot. Because the printed pattern bears little resemblance to the drawn polygons (light diffracts, neighbouring features interfere), the layout has to be deliberately distorted so it prints correctly on the wafer. This is the most compute-intensive software step in the entire flow, run on large CPU/GPU farms for days per advanced-node tapeout. Sub-processes inside it:
- **OPC (optical proximity correction)** - nudge edges and add serifs so corners and line-ends print on target.
- **SRAF / assist features** - sub-resolution shapes that do not print but improve the process window of nearby features.
- **SMO (source-mask optimisation)** - co-optimise the illumination source shape and the mask pattern together.
- **ILT (inverse lithography technology)** - solve backwards from the desired wafer image to a (usually curvilinear) ideal mask; the gold standard for high-NA EUV.
- **MPC / MDP (mask process correction, mask data prep)** - correct for the mask writer's own e-beam effects, then fracture/format the data into the writer's job deck.
- **Lithography simulation and mask rule check (MRC)** verify the result before tapeout.

## Where it sits and why it matters
This is the bridge between design (steps 1-12) and manufacturing. Output here defines the [Photomask manufacturing (process step)](/semiconductor-process-flow/frontend/flow-photomask-manufacturing/) step that follows: a single set of EUV reticles for one advanced product can cost tens of millions of dollars, and the photomask market was about USD 5.15bn in 2024 [6]. Computational litho is the software layer that decides whether those masks yield. As nodes move to high-NA EUV, curvilinear ILT shifts from optional to a practical necessity to solve depth-of-focus [5], which both raises compute demand and tightens coupling to ASML's scanners.

## Equipment market
"Equipment" here is software plus the compute it runs on. The computational lithography software market is roughly USD 1.3-1.5bn (2023) heading toward ~USD 4bn by the early 2030s, with most credible estimates clustering at a 12-14% CAGR; faster (~22%) figures come from report-mills and should be discounted [1].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Siemens EDA (Calibre) | US/Germany | leader in mask synthesis | 85%+ in physical-verification DRC/LVS; industry leader in curvilinear ILT data prep [3] |
| Synopsys (Proteus + Mask Synthesis) | US | co-leader | ~20yr-tested OPC/MDP, foundry tool of choice; cuLitho/GPU integration [2] |
| ASML Brion (Tachyon) | Netherlands | scanner-coupled leader | SMO + EUV (Tachyon NXE) tied to ASML installed base; acquired Brion 2006 [2] |
| KLA / D2S / others | US | niche | mask-shop point tools, ILT engines |

Concentration note: this is a near-oligopoly. The same three names that dominate EDA overall (Synopsys ~31%, Cadence ~30%, Siemens ~13% of total EDA) split mask synthesis, except Cadence is largely absent and ASML Brion enters via its scanner lock-in [3]. The blocking position is foundry qualification: TSMC, Samsung and Intel specify which tools are certified for tapeout, so a new entrant cannot sell around them.

## Materials & consumables
This step consumes no physical materials. What it consumes is **compute**: CPU/GPU cycles, often the largest single software-licence and datacentre line in a fab's design-to-tapeout flow. NVIDIA's cuLitho (2023, with TSMC/Synopsys/ASML) claims up to 40-60x speed-ups, letting ~500 DGX H100 systems do the work of ~40,000 CPU servers and produce 3-5x more masks/day at ~9x less power [4][7]. The recurring-revenue analogue is the software licensing model: time-based EDA licences plus, increasingly, GPU-hours. As ILT and curvilinear masks generalise, compute intensity per tapeout rises, which is the durable demand tailwind here.

## Volumes, revenue, profitability
Volume is measured in tapeouts and mask sets, not units. A leading-edge logic tapeout can need 80-100+ masks; only a few hundred advanced-node tapeouts happen per year, so this is low-volume, extremely high-value software. The revenue pool is the ~USD 1.5bn computational-litho software segment [1] sitting inside the ~USD 18bn EDA+IP market [3]. Margins are software margins: the big-three EDA vendors run 80%+ gross and ~30-40%+ operating margins at the corporate level. The margin is earned by the tool vendors (Siemens, Synopsys, ASML Brion) and, increasingly, by the compute platform (NVIDIA) underneath them.

## Competitive landscape & value capture
The moat is foundry qualification plus 20+ years of calibrated models tied to specific scanners and processes; you cannot bootstrap that from a clean sheet. Value accrues to (1) the certified EDA incumbents, (2) ASML via Brion's scanner coupling, and (3) NVIDIA as the compute substrate. The interesting structural shift is AI/ML for OPC/ILT (GANs, RL, surrogate models) collapsing runtime and quality trade-offs [8]; this is where a smaller player could win a wedge, though distribution still runs through foundry qualification. EU-relevant: ASML Brion (Netherlands) is the marquee name; otherwise this is a US-software-dominated step with thin independent-startup ground.

## Market drivers, constraints & trends
Net read: a small but structurally accelerating served market, because compute-per-tapeout is rising faster than tapeout count. Each advanced node consumes more correction compute even if unit volumes stay flat.

- **Drivers**
  - Node transition is the engine: TSMC N2 hit HVM in late 2025 (fully booked, faster ramp through 2026), A16 with backside power enters mass production Q4 2026, and A14 / High-NA arrives 2027-28 [9][13]. Each step adds EUV mask layers and tighter process windows, lifting correction compute per design.
  - Curvilinear ILT moves from optional to mandatory for High-NA EUV (process-window and stitching needs) [10]; a single ILT mask can already consume 10K+ CPU cores for days, so compute demand scales super-linearly with adoption [10].
  - GPU acceleration plus generative AI is expanding the addressable pool, not just cutting cost: cuLitho is in TSMC/Synopsys production, and a generative-AI workflow adds ~2x on top of the ~40x GPU speed-up, making ILT-everywhere economically feasible and pulling spend toward GPU-hours [11].
  - AI/HPC demand: 2nm initial capacity is fully booked on HPC/AI accelerators and chiplets, so the high-value advanced-tapeout mix (the segment that needs the most correction) is the part growing [12].

- **Constraints**
  - Only a few hundred advanced-node tapeouts happen per year, so the unit base is thin and cyclical with foundry capex; a leading-edge digestion pause hits this step directly [12].
  - Foundry qualification is the chokepoint: TSMC/Samsung/Intel certify which tools may tapeout, capping share gains and entrant access [10].
  - China / export-control whiplash: EDA-to-China was restricted May 2025 then rescinded July 2025; China is ~16% of Synopsys and ~12% of Cadence revenue, so policy can swing the addressable base sharply [14].
  - Tool-side dependency: curvilinear masks need multibeam e-beam writers, tying compute-litho demand to a separate, capacity-constrained equipment ramp [10].

- **Trends & inflections to watch**
  - Generative/ML ILT collapsing the runtime-quality trade-off [11] — tripwire: a foundry qualifies a full-chip ML-ILT flow for a production node (named, dated), which would re-rate the GPU/software pool.
  - Backside power and CFET adding mask layers and 3D-aware correction [13] — tripwire: A16/SF2Z volume ramp in 2026-27 disclosing higher mask-layer counts per tapeout.
  - High-NA EUV insertion — tripwire: first High-NA logic node in HVM (Intel/TSMC, 2027-28) shipping curvilinear-ILT reticles at scale [9][10].

## Connections
- [Computational Lithography](/manufacturing/lithography/computational-lithography/) - parent concept cluster.
- [EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/) - the design-side software this step extends.
- **Computational Litho Ai For Mask** - thesis: AI/ML compressing OPC/ILT runtime and the compute-substrate value shift.
- **Lithography Patterning Market** - thesis: the broader patterning value pool this feeds.

## Sources
1. Multiple market reports on computational lithography software size/CAGR (USD 1.3-1.5bn 2023, ~USD 4bn early 2030s, 12-14% CAGR mainstream; treat 22% as report-mill). https://datahorizzonresearch.com/computational-lithography-software-market-46063 and https://dataintelo.com/report/global-computational-lithography-software-market
2. Synopsys Mask Solutions (Proteus/MDP); ASML Brion Tachyon. https://www.synopsys.com/manufacturing/mask-solutions.html and https://www.asml.com/en/news/press-releases/2010/asml-and-brion-unveil-software
3. SemiAnalysis EDA Market Primer (Big-3 shares; Calibre 85%+ physical verification, mask-synthesis leadership). https://newsletter.semianalysis.com/p/eda-market-primer
4. NVIDIA cuLitho launch with TSMC/ASML/Synopsys (40x, power/throughput claims). https://nvidianews.nvidia.com/news/nvidia-asml-tsmc-and-synopsys-set-foundation-for-next-generation-chip-manufacturing
5. Curvilinear ILT a practical necessity for high-NA EUV; multibeam mask writers. https://semiengineering.com/the-benefits-of-curvilinear-full-chip-inverse-lithography-technology-with-mask-wafer-co-optimization/
6. Photomask market ~USD 5.15bn 2024, ~4.3% CAGR. https://www.globenewswire.com/news-release/2025/08/18/3134697/0/en/Photomask-Market-Size-to-Surpass-USD-7-22-Billion-by-2032-at-a-CAGR-of-4-31-Research-by-SNS-Insider.html
7. cuLitho adoption / GPU-accelerated OPC 40-60x speed-ups in production. https://www.datacenterdynamics.com/en/news/tsmc-and-synopsys-use-nvidia-culitho-in-chip-production-explore-generative-ai-for-computational-lithography/
8. AI/ML for ILT/OPC acceleration and quality (GAN, RL approaches). https://ijrpr.com/uploads/V6ISSUE9/IJRPR52523.pdf
9. ASML High-NA EUV volume timeline 2026-28; Intel/TSMC/Samsung adoption for 2nm/1.4nm. https://www.trendforce.com/news/2026/02/16/news-asmls-high-na-euv-for-2027-28-which-giants-are-betting-big-intel-samsung-sk-hynix-or-tsmc/ and https://www.tomshardware.com/tech-industry/semiconductors/asml-lithograpy-roadmap-examined-from-duv-to-hyper-na
10. ILT under chip-manufacture context: curvilinear mandatory for High-NA; single ILT mask 10K+ CPU cores for days; multibeam mask writers; GPU-accelerated ILT. https://pmc.ncbi.nlm.nih.gov/articles/PMC12843865/ and https://www.nature.com/articles/s41377-025-01923-w
11. cuLitho in TSMC/Synopsys production; generative-AI workflow ~2x on top of ~40x GPU speed-up; 350 H100 replace 40,000 CPU systems. https://nvidianews.nvidia.com/news/tsmc-synopsys-nvidia-culitho and https://www.datacenterdynamics.com/en/news/tsmc-and-synopsys-use-nvidia-culitho-in-chip-production-explore-generative-ai-for-computational-lithography/
12. TSMC N2 HVM late 2025, 2nm capacity fully booked on HPC/AI + chiplets, faster ramp 2026. https://www.tomshardware.com/tech-industry/semiconductors/tsmc-begins-quietly-volume-production-of-2nm-class-chips-first-gaa-transistor-for-tsmc-claims-up-to-15-percent-improvement-at-iso-power and https://www.marketsandmarkets.com/Market-Reports/advanced-process-nodes-market-92100832.html
13. Backside power / CFET adding mask layers + 3D-aware correction; TSMC A16 (Super Power Rail) mass production Q4 2026; Samsung SF2Z 2027. https://semiengineering.com/powering-cfets-from-the-backside/ and https://newsletter.semianalysis.com/p/clash-of-the-foundries
14. EDA export controls to China restricted May 2025, rescinded July 2025; China ~16% of Synopsys, ~12% of Cadence revenue. https://www.eetimes.com/u-s-restricts-eda-software-sales-to-china/ and https://sourceability.com/post/why-the-u-s-lifted-its-design-ban-and-what-it-means
