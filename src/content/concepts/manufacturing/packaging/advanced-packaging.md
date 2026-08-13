---
type: concept
slug: advanced-packaging
canonical_name: Advanced Packaging
aliases: []
kind: technology
parent_concepts:
- manufacturing
- packaging
related_concepts: []
sources:
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- 'Glass substrates: do TGV yield and reliability barriers hold CoPoS commercialisation to ~2030 as DigiTimes projects, or does China''s early sampling (Enflame at WAIC 2026) and equipment ordering pull the timeline in?'
- 'Pricing power vs capacity glut: ASE quote hikes above 20% plus record capex across ASE, Amkor, TSMC, SMIC and SK Hynix; does 2027-28 bring over-capacity in mature 2.5D flows, and who eats the margin compression first?'
- Does known-good-die screening extend to post-assembly reliability guarantees (KGRD), and does a mandatory new test step create a venture-scale wedge?
- 'What limits 3D stacking first in practice: TSV power delivery (IR drop) or heat extraction? Evidence would be qualified stacks failing thermal rather than electrical sign-off, or vice versa.'
- Do cross-chiplet side-channel attacks become a qualification requirement for multi-vendor chiplet packages (UCIe ecosystem), creating a security-test market?
- 'Photonic packaging: does flip-chip electrical interfacing at 50 GHz-class bandwidth to TFLN scale from lab platform to foundry-qualified flow, and which packaging house owns electro-optic assembly?'
last_updated: '2026-07-26'
tags:
- concept
- technology
mention_count: 178
descendants:
- 3d-monolithic-integration
- heterogeneous-integration
- micro-transfer-printing
- osat
last_reorg_date: '2026-05-13'
sources_7d: 5
sources_30d: 13
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-31-chips-act-equity-deals-us-gains-10-stake-in-intel-874m-for-s
  title: 'CHIPS Act Equity Deals: U.S. Gains 10% Stake in Intel, $874M for Seven Companies - News and Statistics - IndexBox'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-31-memory-optics-packaging-chips-act-targets-ais-compute-bottle
  title: 'Memory, optics, packaging: CHIPS Act targets AI''s compute bottleneck - Electronics360'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-31-tim-market-sizing-refresh
  title: TIM market sizing refresh — the definitional 2x split and the real addressable slot
  date: '2026-07-31'
  kind: web
- slug: 2026-07-30-commerce-dept-signs-874-million-in-chips-act-incentives-with
  title: Commerce Dept. Signs $874 Million in CHIPS Act Incentives With Seven Companies - Yahoo Finance
  date: '2026-07-30'
  kind: web
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-14-boschs-sic-fab-deal-adds-to-a-resurgence-in-chips-act-fundin
  title: Bosch's SiC fab deal adds to a resurgence in CHIPS Act funding - Electronics360
  date: '2026-07-14'
  kind: web
- slug: 2026-07-14-chips-act-20-ambition-requires-funding---digitaleurope
  title: 'Chips Act 2.0: Ambition requires funding - DigitalEurope'
  date: '2026-07-14'
  kind: web
neighbors: []
---
## Physics / mechanism

Advanced packaging integrates multiple dies (chiplets) into one module at interconnect densities far beyond a board, sidestepping the reticle-size and yield limits of monolithic SoCs. Two mechanism families: 2.5D places dies side by side on a silicon interposer or fan-out substrate; 3D bonds active dies vertically through-silicon vias (TSVs) or hybrid bonding. Die-crossing at roughly 10 µm pitch is routable in production-representative flows today, and architecture modeling shows 3D stacking buys up to 14% wirelength reduction and 6% critical-path improvement over 2D at that pitch, while 2.5D pays only a 2-4% overhead for the yield and capacity gain **2026 06 15 Modeling Optimizing And Exploring Multi Die Fpga Routing Arc**. TSMC CoWoS/SoIC, Intel EMIB/Foveros, Samsung X-Cube, and ASE/Amkor on the OSAT side still define the production envelope.

Superseded claim: this page previously stated hybrid bonding at "<1 µm pitch" and "~0.1 pJ/bit" as the current envelope, with a bandwidth-density table. Those figures were uncited and the current source set does not support them as production numbers; sub-micron pitch is a roadmap target. Confidence in the replacement 10 µm figure is moderate (single modeling source).

Where the 2025-26 tier-1 literature says the binding constraints now sit:

- I/O overhead. Conventional ESD protection and I/O circuitry is the main blocker to shrinking chiplets below ~100 mm²; simplified interfaces enabled by dense 2.5D/3D interconnect open the way to much smaller, composable chiplets **2026 06 05 Tiny Chiplets Enabled By Packaging Scaling Opportunities In **.
- Power delivery and heat. TSV planning against IR drop is a primary reliability problem in 3D power-delivery networks **2026 07 08 Gpu Accelerated Effective Resistance Analysis For 3D Ic Powe**, and thermal analysis of 3D stacks needs dedicated multiscale workflows **2026 06 05 A Multiscale Workflow For Thermal Analysis Of 3Di Chip Stack**.
- Test and reliability. Known-good-die screening guarantees pre-assembly function but says nothing about post-assembly lifetime; formal known-good-reliable-die (KGRD) screening is being proposed as the missing step for chiplet AI SoCs **2026 07 23 Formal Foundations For Known Good Reliable Die Screening In **.
- Software-visible non-uniformity. In multi-chiplet GPUs, remote-HBM traffic varies up to 58x with kernel mapping choices, so package topology has become a software design constraint, not only a hardware one **2026 06 15 A Fast Locality Simulator For Gemm Design Space Exploration ** **2026 06 15 Making Locality Aware Gemm Compatible With Page Granularity **.
- Security. Side-channel attacks can be mounted between chiplets inside one package, an attack surface unique to heterogeneous integration **2026 06 05 Spying Across Chiplets Side Channel Attacks In 253D Integrat**.
- Memory-centric architectures ride on packaging. 3D heterogeneous accelerators stacking FeFET and DRAM chiplets report order-of-magnitude gains for MoE inference **2026 07 21 Thame 3D Memory Enabled Heterogeneous Accelerator For Llm Mi**; startup architectures such as UAiM's per-bank-group DRAM read scheme depend entirely on bonding LPDDR dies to a compute die **2026 07 01 Uaim Call**.
- Photonics. Packaging is the gating step for electro-optic integration: a flip-chip platform now delivers 13 high-speed channels at up to 50 GHz to a centimetre-scale thin-film lithium niobate chip **2026 06 16 Multi Channel High Speed Flip Chip Packaging Platform For Th**. New interconnect physics (spoof-plasmon lines on silicon) attack the same bandwidth-plus-thermal problem **2026 06 05 Electrical And Thermal Performance Tuning Of Spoof Plasmonic**.

## Competitive landscape

Demand and pricing. Advanced packaging revenue is growing faster than front-end manufacturing **2026 07 16 Exclusive Advanced Packaging Outpaces Front End Growth While**, with forecasts around $79.4B by 2030 **2025 08 31 Advanced Packaging Market Set To Reach 794 Billion By 2030  ** and IDC running a 2025-2030 forecast line **2026 04 02 Worldwide Semiconductor Advanced Packaging Forecast And Anal** (headline-level citations; confidence in exact figures moderate). Supply is tight enough for pricing power: ASE reportedly raised packaging quotes by more than 20% in July 2026 **2026 07 01 News Ase Reportedly Raises Advanced Packaging Quotes By More** after lifting 2026 capex to a record $8.5B **2026 04 30 Ase Raises 2026 Capex To Record Us85 Billion On Strong Advan**. Amkor posted strong 2025 results on packaging growth **2026 02 10 Amkor Posts Strong 2025 Results As Advanced Packaging Drives** and widened its Nvidia AI-packaging partnership with US capacity **2026 07 24 Amkor Nvidia Widen Ai Packaging Partnership As Us Capacity E**.

Structure. TSMC remains the reference but is reshaping its expansion (AP8, AP7, US fab plans) **2026 01 29 Exclusive Tsmc Reshapes Advanced Packaging Expansion Shiftin**, and the trade press reads 2026 as a shift from TSMC dominance toward a broader collaborative supply base **2026 06 01 Analysis Advanced Packaging Shifts From Tsmc Dominance To In**. The entrant list is long: Intel courting entry-level packaging customers **2026 05 06 Intel Targets Entry Level Advanced Packaging Draws Interest **, SMIC scaling a packaging team for AI chips **2026 04 24 Smic Returns To Advanced Packaging Scales Team To Boost Ai C**, Chinese OSATs stepping up investment **2026 04 10 China Osats Step Up Investment Drive As Ai Demand Lifts Adva** including SJ Semiconductor's $1.5B build **2026 07 06 China Advanced Packaging Maker Sj Semiconductor Starts Us15B**, SK Hynix funding a new packaging plant **2026 01 14 Sk Hynix To Invest In New Advanced Packaging Plant Amid Ai M**, Japan targeting packaging to close the gap with TSMC **2026 01 03 Analysis Japan Targets Advanced Packaging To Crack Tsmcs Man**, and Southeast Asia moving from test-and-pack to multi-centre advanced packaging **2026 06 15 Southeast Asia Shifts From Test And Pack To Multi Center Adv**.

Substrates are the live materials contest. Huawei's "Tau law" framing has pushed the AI-chip race toward glass substrates and packaging rather than node scaling **2026 06 04 Huaweis Tau Law Shifts Ai Chip Race To Glass Substrates Adva**. Enflame showed China's first glass-based CoPoS AI chip sample at WAIC 2026 **2026 07 22 Waic 2026 Enflame Debuts Chinas First Glass Based Copos Ai C** and Chinese equipment makers are winning early TGV production orders **2026 07 22 Chinese Equipment Makers Win Early Production Orders As Tgv **, but through-glass vias still face technical barriers and DigiTimes puts CoPoS commercialisation around 2030 **2026 07 24 Tgv Still Faces Technical Barriers Copos Commercialization N**. The incumbent organic-substrate chain is meanwhile supply-constrained: a T-glass shortage rippled through memory and packaging in early 2026 **2026 01 15 Exclusive T Glass Shortage Ripples Through Memory And Advanc**.

## Investment routing (all vehicles)

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Glass substrates: do TGV yield and reliability barriers hold CoPoS commercialisation to ~2030 **2026 07 24 Tgv Still Faces Technical Barriers Copos Commercialization N**, or does China's early sampling and equipment ordering **2026 07 22 Waic 2026 Enflame Debuts Chinas First Glass Based Copos Ai C** **2026 07 22 Chinese Equipment Makers Win Early Production Orders As Tgv ** pull the timeline in?
- Pricing power vs capacity glut: quote hikes and record capex are running together **2026 07 01 News Ase Reportedly Raises Advanced Packaging Quotes By More** **2026 04 30 Ase Raises 2026 Capex To Record Us85 Billion On Strong Advan**; does 2027-28 bring over-capacity in mature 2.5D flows, and who eats the margin compression first?
- Does known-good-die screening extend to post-assembly reliability guarantees (KGRD) **2026 07 23 Formal Foundations For Known Good Reliable Die Screening In **, and does a mandatory new test step create a venture-scale wedge?
- What limits 3D stacking first in practice: TSV power delivery (IR drop) **2026 07 08 Gpu Accelerated Effective Resistance Analysis For 3D Ic Powe** or heat extraction **2026 06 05 A Multiscale Workflow For Thermal Analysis Of 3Di Chip Stack**?
- Do cross-chiplet side-channel attacks **2026 06 05 Spying Across Chiplets Side Channel Attacks In 253D Integrat** become a qualification requirement for multi-vendor chiplet packages, creating a security-test market?
- Photonic packaging: does flip-chip electrical interfacing at 50 GHz-class bandwidth to TFLN **2026 06 16 Multi Channel High Speed Flip Chip Packaging Platform For Th** scale from lab platform to foundry-qualified flow, and which packaging house owns electro-optic assembly?
