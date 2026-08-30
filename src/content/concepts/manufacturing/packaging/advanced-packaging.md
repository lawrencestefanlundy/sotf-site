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
mention_count: 180
descendants:
- 3d-monolithic-integration
- heterogeneous-integration
- micro-transfer-printing
- osat
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 5
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

Advanced packaging integrates multiple dies (chiplets) into one module at interconnect densities far beyond a board, sidestepping the reticle-size and yield limits of monolithic SoCs. Two mechanism families: 2.5D places dies side by side on a silicon interposer or fan-out substrate; 3D bonds active dies vertically through-silicon vias (TSVs) or hybrid bonding. Die-crossing at roughly 10 µm pitch is routable in production-representative flows today, and architecture modeling shows 3D stacking buys up to 14% wirelength reduction and 6% critical-path improvement over 2D at that pitch, while 2.5D pays only a 2-4% overhead for the yield and capacity gain modeling optimizing and exploring multi die fpga routing arc. TSMC CoWoS/SoIC, Intel EMIB/Foveros, Samsung X-Cube, and ASE/Amkor on the OSAT side still define the production envelope.

Superseded claim: this page previously stated hybrid bonding at "<1 µm pitch" and "~0.1 pJ/bit" as the current envelope, with a bandwidth-density table. Those figures were uncited and the current source set does not support them as production numbers; sub-micron pitch is a roadmap target. Confidence in the replacement 10 µm figure is moderate (single modeling source).

Where the 2025-26 tier-1 literature says the binding constraints now sit:

- I/O overhead. Conventional ESD protection and I/O circuitry is the main blocker to shrinking chiplets below ~100 mm²; simplified interfaces enabled by dense 2.5D/3D interconnect open the way to much smaller, composable chiplets tiny chiplets enabled by packaging scaling opportunities in .
- Power delivery and heat. TSV planning against IR drop is a primary reliability problem in 3D power-delivery networks gpu accelerated effective resistance analysis for 3d ic powe, and thermal analysis of 3D stacks needs dedicated multiscale workflows a multiscale workflow for thermal analysis of 3di chip stack.
- Test and reliability. Known-good-die screening guarantees pre-assembly function but says nothing about post-assembly lifetime; formal known-good-reliable-die (KGRD) screening is being proposed as the missing step for chiplet AI SoCs formal foundations for known good reliable die screening in .
- Software-visible non-uniformity. In multi-chiplet GPUs, remote-HBM traffic varies up to 58x with kernel mapping choices, so package topology has become a software design constraint, not only a hardware one a fast locality simulator for gemm design space exploration  making locality aware gemm compatible with page granularity .
- Security. Side-channel attacks can be mounted between chiplets inside one package, an attack surface unique to heterogeneous integration spying across chiplets side channel attacks in 253d integrat.
- Memory-centric architectures ride on packaging. 3D heterogeneous accelerators stacking FeFET and DRAM chiplets report order-of-magnitude gains for MoE inference thame 3d memory enabled heterogeneous accelerator for llm mi; startup architectures such as UAiM's per-bank-group DRAM read scheme depend entirely on bonding LPDDR dies to a compute die uaim call.
- Photonics. Packaging is the gating step for electro-optic integration: a flip-chip platform now delivers 13 high-speed channels at up to 50 GHz to a centimetre-scale thin-film lithium niobate chip multi channel high speed flip chip packaging platform for th. New interconnect physics (spoof-plasmon lines on silicon) attack the same bandwidth-plus-thermal problem electrical and thermal performance tuning of spoof plasmonic.

## Competitive landscape

Demand and pricing. Advanced packaging revenue is growing faster than front-end manufacturing exclusive advanced packaging outpaces front end growth while, with forecasts around $79.4B by 2030 advanced packaging market set to reach 794 billion by 2030   and IDC running a 2025-2030 forecast line worldwide semiconductor advanced packaging forecast and anal (headline-level citations; confidence in exact figures moderate). Supply is tight enough for pricing power: ASE reportedly raised packaging quotes by more than 20% in July 2026 news ase reportedly raises advanced packaging quotes by more after lifting 2026 capex to a record $8.5B ase raises 2026 capex to record us85 billion on strong advan. Amkor posted strong 2025 results on packaging growth amkor posts strong 2025 results as advanced packaging drives and widened its Nvidia AI-packaging partnership with US capacity amkor nvidia widen ai packaging partnership as us capacity e.

Structure. TSMC remains the reference but is reshaping its expansion (AP8, AP7, US fab plans) exclusive tsmc reshapes advanced packaging expansion shiftin, and the trade press reads 2026 as a shift from TSMC dominance toward a broader collaborative supply base analysis advanced packaging shifts from tsmc dominance to in. The entrant list is long: Intel courting entry-level packaging customers intel targets entry level advanced packaging draws interest , SMIC scaling a packaging team for AI chips smic returns to advanced packaging scales team to boost ai c, Chinese OSATs stepping up investment china osats step up investment drive as ai demand lifts adva including SJ Semiconductor's $1.5B build china advanced packaging maker sj semiconductor starts us15b, SK Hynix funding a new packaging plant sk hynix to invest in new advanced packaging plant amid ai m, Japan targeting packaging to close the gap with TSMC analysis japan targets advanced packaging to crack tsmcs man, and Southeast Asia moving from test-and-pack to multi-centre advanced packaging southeast asia shifts from test and pack to multi center adv.

Substrates are the live materials contest. Huawei's "Tau law" framing has pushed the AI-chip race toward glass substrates and packaging rather than node scaling huaweis tau law shifts ai chip race to glass substrates adva. Enflame showed China's first glass-based CoPoS AI chip sample at WAIC 2026 waic 2026 enflame debuts chinas first glass based copos ai c and Chinese equipment makers are winning early TGV production orders chinese equipment makers win early production orders as tgv , but through-glass vias still face technical barriers and DigiTimes puts CoPoS commercialisation around 2030 tgv still faces technical barriers copos commercialization n. The incumbent organic-substrate chain is meanwhile supply-constrained: a T-glass shortage rippled through memory and packaging in early 2026 exclusive t glass shortage ripples through memory and advanc.

## Investment routing (all vehicles)

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Glass substrates: do TGV yield and reliability barriers hold CoPoS commercialisation to ~2030 tgv still faces technical barriers copos commercialization n, or does China's early sampling and equipment ordering waic 2026 enflame debuts chinas first glass based copos ai c chinese equipment makers win early production orders as tgv  pull the timeline in?
- Pricing power vs capacity glut: quote hikes and record capex are running together news ase reportedly raises advanced packaging quotes by more ase raises 2026 capex to record us85 billion on strong advan; does 2027-28 bring over-capacity in mature 2.5D flows, and who eats the margin compression first?
- Does known-good-die screening extend to post-assembly reliability guarantees (KGRD) formal foundations for known good reliable die screening in , and does a mandatory new test step create a venture-scale wedge?
- What limits 3D stacking first in practice: TSV power delivery (IR drop) gpu accelerated effective resistance analysis for 3d ic powe or heat extraction a multiscale workflow for thermal analysis of 3di chip stack?
- Do cross-chiplet side-channel attacks spying across chiplets side channel attacks in 253d integrat become a qualification requirement for multi-vendor chiplet packages, creating a security-test market?
- Photonic packaging: does flip-chip electrical interfacing at 50 GHz-class bandwidth to TFLN multi channel high speed flip chip packaging platform for th scale from lab platform to foundry-qualified flow, and which packaging house owns electro-optic assembly?
