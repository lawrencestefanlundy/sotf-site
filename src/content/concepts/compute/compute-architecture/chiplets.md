---
type: concept
slug: chiplets
canonical_name: Chiplets
aliases: []
kind: technology
parent_concepts:
- compute
- compute-architecture
related_concepts: []
sources:
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-03-26-sotf-interview-dorian-haci-mintneuro]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-03-02-chiplets-architecture-share-rebellions-rebel-100-industry-s]]'
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-03-05-chiplets-architecture-share-chiplet-summit-2026-ucie]]'
- '[[2026-07-02-semianalysis-ectc2026-advanced-packaging]]'
- '[[2024-yole-advanced-packaging-2024]]'
- '[[2025-12-31-chiplets-architecture-share-chiplet-market-size-share]]'
- '[[2026-05-30-intel-glass-substrates-program]]'
- '[[2026-05-28-europes-semiconductor-strategy-chiplets-ecosystem-integratio]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
- '[[2024-tsmc-cowos-roadmap-disclosure]]'
- '[[2026-03-31-semianalysis-nvidia-blackwell-dissection]]'
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 107
sources_7d: 2
sources_30d: 4
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2026-05-28-europes-semiconductor-strategy-chiplets-ecosystem-integratio
  title: 'Europe’s Semiconductor Strategy: Chiplets, Ecosystem Integration, and Chips Act 2.0 in 2026 - News and Statistics - IndexBox'
  date: '2026-05-28'
  kind: web
- slug: 2026-04-15-semianalysis-isscc-2026
  title: 'ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More'
  date: '2026-04-15'
  kind: web
- slug: 2026-03-31-semianalysis-nvidia-blackwell-dissection
  title: Dissecting Nvidia Blackwell - Tensor Cores, PTX Instructions, SASS, Floorsweep, Yield
  date: '2026-03-31'
  kind: web
- slug: 2026-03-26-sotf-interview-dorian-haci-mintneuro
  title: 'Chips for the Brain: Modular Semiconductors for Neural Interfaces (MintNeuro) / Dorian Haci)'
  date: '2026-03-26'
  kind: substack
- slug: 2026-03-05-chiplets-architecture-share-chiplet-summit-2026-ucie
  title: 'Chiplet Summit 2026: UCIe Momentum Across Growing Ecosystem (UCIe Consortium)'
  date: '2026-03-05'
  kind: web
neighbors: []
---
**Chiplets replace a single large monolithic die with several smaller dies co-packaged on an interposer or 3D stack, trading a new set of packaging, thermal and tooling problems for better yield, cost and heterogeneity, and the AI architecture literature now treats them as the default substrate for large accelerators.**

## Summary

A chiplet is a die that is deliberately built smaller than the system it belongs to, then joined to other dies inside one package via an interposer (2.5D), by stacking (3D), or on large-area substrates approaching panel or wafer scale. The motivation is arithmetic: defect density means yield falls with die area, and each new node adds cost and complexity, so partitioning a design into smaller dies and reassembling them in the package recovers yield while allowing each piece to be built on the node that suits it. Sources describing the move from 3 nm toward sub-nanometre nodes and from FinFETs to GAAFETs position 3D chiplet approaches explicitly as the response to falling yields and rising manufacturing complexity, and a carbon-aware design framework frames the same shift as an industry-wide transition to heterogeneous integration driven by the yield and cost limits of monolithic scaling.

The second, arguably larger, motive is heterogeneity. Once dies are separable, they can be specialised. Proposed designs assign prefill and decode phases of LLM inference to different packages, one built from systolic-array chiplets with off-package memory and one from vector-unit arrays with in-package memory; decouple DRAM banks from logic into chiplets on separate process nodes joined by an interposer to build a processing-in-memory module; co-locate heterogeneous modules of a Mixture-of-Experts model on specialised chiplets in a 3.5D wafer-scale package; and amortise the non-recurring engineering cost of bespoke ASICs by reusing a curated ecosystem of chiplets. The same logic reappears outside AI: petabit-per-second internet routers built from chiplets, HBM and in-package optics, and modular superconducting quantum processors where chiplets are linked by long-range couplers.

The parameters that decide the outcome are mostly not logic parameters. First, interconnect: electrical links between chiplets are the stated bottleneck, which is why photonic interposers, glass panel-scale switch fabrics and in-package optics recur across these sources. Second, interface overhead: ESD protection and inter-chiplet signalling circuitry has been identified as the constraint preventing chiplets from shrinking below roughly 100 mm2, and therefore limits how fine-grained and reusable the building blocks can be. Third, thermal and mechanical reliability: peak temperature and package warpage become first-order placement objectives once dozens of chiplets sit close together. Fourth, tooling and trust: design automation for these packages is incomplete, and multi-vendor plug-and-play integration on reconfigurable interposers creates an authentication problem that does not exist in a monolithic die.

## Viability (4/5)

Two things need separating. The base capability, partitioning a system into 2.5D/3D co-packaged dies, is assumed rather than argued across the whole source set: reliability work on 3D VLSI describes chiplets as key enablers against falling yields at sub-nanometre nodes, a placement paper states that AI and automotive demand is accelerating 2.5D IC adoption with dozens of chiplets per package, and packaging-scaling work reasons about how much further chiplets can shrink rather than whether they exist. That is consistent, multi-group agreement that the substrate works.

The architectures built on it are less proven. DUET's 4x faster time-to-first-token and 1.5x lower time-between-tokens versus a B200 GPU are evaluation results on three models; PICNIC's 3.95x speedup and 30x efficiency gain over an A100, and 57x efficiency over an H100, are simulation results; Sangam is a proposed CXL-attached module. The one measured hardware result here is a photonic chiplet demonstration reaching 6-bit precision at 128 GS/s with 6 ns AI-processing latency using lithium niobate photonics. The sources contain no fabrication, yield or volume data for commercial chiplet products, so the 4 reflects the substrate, not the proposals stacked on it.

**TLDR: The packaging approach is treated as an ongoing industry transition by independent groups; the specific chiplet architectures in these sources are still simulation results.**

## Drivers (4/5)

Supply: the stated driver is that monolithic scaling is running into yield and cost limits as processes move from 3 nm toward sub-nanometre and from FinFETs to GAAFETs, with chiplets presented as the mitigation. A second supply-side driver is packaging itself: advanced packaging now provides abundant interconnection resources for 2.5D/3D integration, which is what makes fine-grained partitioning worth attempting. A third is economic: chiplet reuse is explicitly framed as the way to amortise non-recurring engineering cost across bespoke designs.

Demand: LLM inference dominates. The recurring argument is that decode is memory-bandwidth-bound with low operational intensity while prefill is compute-bound, so a homogeneous die cannot serve both, and that KV-cache growth with context length makes the mismatch worse. MoE sparsity adds communication and locality pressure that maps onto modular packages. Non-AI demand is thinner but present: automotive is named alongside AI as accelerating 2.5D adoption, and networking and quantum computing appear as further pulls.

**TLDR: Supply side pushed by monolithic yield and node cost; demand side pulled by LLM memory bandwidth and, separately, automotive.**

## Novelty (3/5)

The comparator is a monolithic die on a single node. Against that, the claimed advantages are qualitative in these sources: better yield at advanced nodes, the ability to mix technology nodes, and reuse that amortises NRE. No source here quantifies the yield or cost delta of partitioning as such. What is quantified is what happens when chiplets are combined with something else: decoupling DRAM banks from logic into separate chiplets on heterogeneous nodes enables systolic arrays and SRAM buffers that were not feasible inside DRAM-process PIM; adding silicon photonic interconnect and in-memory compute gives 3.95x speedup over an A100 in simulation; phase-specialised packages give 4x time-to-first-token over a B200.

The second novelty is in the tooling layer, and it is measurable. A thermo-mechanical-aware analytical placer for 2.5D reports 146% and 52% geometric-mean wirelength improvement over two prior chiplet placers, 3-13% lower temperature, 5-27% less warpage, about 10x faster, and a mapping-space explorer for multi-chiplet LLM serving reports 63.12% average energy-delay-product reduction versus prior work. Those margins over recent baselines indicate the design methods are immature, which is itself informative: the hardware idea is ahead of the tools.

**TLDR: Clearly better than a monolithic die on yield, cost and heterogeneity, but the headline multiples in these sources come from chiplets plus photonics or in-memory compute, not chiplets alone.**

## Diffusion (3/5)

The barriers in these sources are specific. Interface overhead: conventional I/O, ESD protection and signalling occupy enough area that prior work identified it as the major constraint on reducing chiplet size below 100 mm2, and the proposed relief is simplification enabled by future packaging rather than anything available today. Thermal and mechanical: peak temperature and operational warpage must become explicit placement objectives, and existing tools were limited by poor scalability and slow simulation; accurate 3D transient thermal simulation including BEOL structure in stacked chiplets is described as an open challenge. Tooling: for electronic-photonic chiplets specifically, adoption is said to be limited by the absence of a unified, fabrication-aware physical design automation stack.

The hardest barrier for the open-market version of chiplets is trust. Reconfigurable interposers for plug-and-play integration across heterogeneous multi-vendor ecosystems break conventional authentication schemes, which fail to scale in decentralised, post-fabrication programmable environments; the proposed fix embeds a PUF across the interconnect with multi-party computation at 0.23% area and 0.072% power overhead, but it is a research proposal. Sustainability adds a further constraint, since embodied carbon of packaging and multiple dies must be traded against operational carbon. Diffusion inside single vendors is credible now; a genuine multi-vendor chiplet marketplace is not evidenced here.

**TLDR: Adoption of coarse-grained chiplets is under way; fine-grained, multi-vendor, plug-and-play chiplet markets face interface, thermal and trust barriers that are named but unsolved.**

## Impact (4/5)

The breadth in this source set is the argument. The same partitioning idea underwrites wafer-scale 3.5D MoE training packages, CXL-attached PIM memory modules, a petabit/sec router in a single package, panel-scale glass interposers of 500 mm x 500 mm or larger integrating commercial processor chiplets with HBM stacks, hybrid-bonded memory chiplets using IGZO FeFETs, and modular superconducting quantum processors linked over more than one centimetre with sub-100 ns gates and intrinsic errors below 1e-4.

The value is best read as enabling rather than incremental: chiplets are the route by which systems escape single-die area and single-node constraints, and the claimed system-level gains (up to 57x efficiency over an H100 in one simulated photonic-chiplet design) only exist because heterogeneity is possible. It is not a 5 because the sources contain no economic or deployment measurement of that value, only architectural and simulated performance evidence.

**TLDR: If the tooling and interconnect problems are solved, chiplets are the mechanism by which packages keep scaling past the reticle and the node, across AI, networking and quantum.**

## Timing Now (0-2yr)

The near-term band is justified by how the sources treat the baseline: AI and automotive demand is already accelerating 2.5D adoption with multiple tightly placed chiplets, and industry is described as transitioning to heterogeneous integration now. The active work in 2025-2026 is not proving chiplets work, it is placement, mapping, thermal analysis, security and yield tooling around them, which is what a technology in the adoption phase looks like.

The more aggressive variants sit further out and the sources say why. Electronic-photonic chiplets lack a unified fabrication-aware design automation stack; panel-scale glass photonic interposers are explicitly envisioned rather than built; chiplet miniaturisation below 100 mm2 depends on future packaging technologies simplifying ESD and signalling; and modular fluxonium chiplet coupling is a proposal under realistic assumptions. Treat those as 5-10 year items.

**TLDR: Coarse-grained 2.5D chiplet integration is being adopted now; photonic interposers, panel-scale substrates and sub-100 mm2 tiny chiplets are the later half of the story.**

## Overrated or underrated? Fairly rated

Chiplets are no longer a bet in the computer architecture literature; they are the assumed substrate. Across eighteen independent tier-1 papers here, nobody argues for partitioning, they argue about what to put on the pieces and how to place, map, cool, authenticate and carbon-account for them. That consistency is why the headline concept is fairly rated rather than underrated: the direction is settled and priced in.

Where the assessment is more interesting is one layer down. The size of the improvements reported against very recent baselines, 146% wirelength over one prior 2.5D placer and 63.12% EDP over state-of-the-art mapping, plus open problems in transient 3D thermal simulation, missing photonic design automation and unsolved multi-vendor authentication, say that the enabling stack is immature. The honest position is that chiplet packaging will be adopted regardless, and that most of the remaining value and risk sits in interfaces, thermo-mechanical design and the tooling that decides whether fine-grained, reusable, multi-vendor chiplets ever exist, or whether chiplets stay a within-vendor cost trick.

## Prediction

By June 2028, academic multi-chiplet LLM accelerator claims of the kind published in 2025-2026 (for example 4x time-to-first-token versus a B200 and 57x efficiency versus an H100) will still rest on simulation, with no fabricated academic multi-chiplet photonic or PIM-chiplet LLM accelerator reporting measured performance within a factor of two of those figures.

## Evidence base

- 2026-01-20: 3D chiplet-based approaches are presented as key enablers against the falling yields and rising complexity of the move from 3 nm toward sub-nanometre nodes and FinFET-to-GAAFET transition.
- 2025-11-21: rising AI and automotive demand is described as accelerating 2.5D IC adoption, with placement of dozens of chiplets now requiring joint optimisation of wirelength, peak temperature and warpage; the reported placer gives 146% and 52% wirelength improvement over two prior tools, 3-13% lower temperature, 5-27% less warpage, about 10x faster.
- 2026-03-16: a disaggregated design assigning prefill to systolic-array chiplets and decode to vector-unit arrays with in-package memory reports 4x faster time to first token, 1.4x higher throughput and 1.5x lower time between tokens over a B200 GPU on Nemotron-H-56B, Zamba2-7B and Llama3-8B.
- 2025-11-15: decoupling logic and DRAM into chiplets on heterogeneous nodes joined by an interposer is claimed to enable systolic arrays and SRAM buffers inside a memory module, capabilities not feasible in prior processing-in-memory architectures.
- 2025-11-13: prior work identified I/O, ESD protection and signalling area overhead as the major constraint on reducing chiplet size below 100 mm2; SPICE and parasitic-extraction analysis argues these can be simplified in future 2.5D/3D packaging to permit smaller, more composable chiplets.
- 2026-01-16: reconfigurable interposers for plug-and-play, multi-vendor chiplet integration break conventional authentication; the proposed PUF plus multi-party computation scheme costs 0.23% area and 0.072% power across diverse chiplets.
- 2026-02-09: a measured demonstration across photonic chiplets achieves 9-bit amplitude-phase decoupled linear multiplication with 6-bit homodyne precision at 128 GS/s and 6 ns AI-processing latency.

## Open questions

- Can ESD and inter-chiplet signalling really be simplified enough in production packaging to push chiplets below 100 mm2, or does interface area keep the granularity coarse and reuse limited?
- Do the thermal and warpage penalties of packing dozens of chiplets, plus the open problem of accurate transient 3D thermal simulation including BEOL structures, cap achievable power density in 3D stacks?
- Does a genuine multi-vendor chiplet market emerge, and does interposer-resident authentication with sub-1% area and power overhead prove sufficient in practice?
- Do photonic interposers move from proposal to fabricated large-scale systems, given that adoption is currently blocked by the absence of a fabrication-aware physical design automation stack?
- How does embodied carbon from additional packaging and multiple dies net against operational savings once heterogeneous integration is optimised end to end?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
