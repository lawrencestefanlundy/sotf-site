---
type: concept
slug: heterogeneous-integration
canonical_name: Heterogeneous Integration
aliases:
- hetero-integration
- heterogeneous integration
- HI
parent_concepts:
- advanced-packaging
related_concepts:
- 3d-ic-stacking
- hybrid-bonding
- tsv-through-silicon-via
- cowos
- co-packaged-optics
- chiplets
sources:
- '[[2026-03-26-sotf-interview-dorian-haci-mintneuro]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-04-09-photonics-material-class-war-photonic-integrated-circuit]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-07-11-neutral-pdk-heterogeneous-integration-landscape]]'
- '[[2026-04-10-photonic-light-source-supply-co-packaged-optics-cpo-scaling]]'
frontier:
- Do the 200 mm micro-transfer-printing yields (>95 per cent, 420 nm 3-sigma placement) hold at 300 mm and across multiple modulator generations, or do they degrade with die count and thermal budget?
- Can the ESD and inter-chiplet signalling overhead actually be simplified enough in production packaging to take chiplets below 100 mm2, or does reliability qualification block the simplification proposed in simulation?
- Does anyone converge on standards for co-packaged optics serviceability and thermal interface, given that the sources name standardisation and serviceability as decisive for adoption but report no standards activity?
- Do the thermo-mechanical co-design tools (placement, TSV surrogates, digital twins) reach sign-off-grade accuracy, or do designers keep falling back on slow full-wave and finite-element flows that limit chiplet counts?
- What is the practical yield floor for heterogeneous integration of known-good-die at sub-10 µm bump pitch — is KGD test the binding constraint on cost?
- When do photonic chiplets enter heterogeneous integration production stacks alongside electronic logic and HBM?
- Does the CHIPS Act and EU Chips Act capex wave materially expand HI packaging capacity outside Taiwan/Korea by 2028?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 67
scorecard:
  viability: 4
  drivers: 4
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 10
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
- slug: 2026-04-10-photonic-light-source-supply-co-packaged-optics-cpo-scaling
  title: Co-Packaged Optics (CPO) – Scaling with Light for the Next Wave of Interconnect
  date: '2026-04-10'
  kind: web
- slug: 2026-04-09-photonics-material-class-war-photonic-integrated-circuit
  title: Photonic Integrated Circuit Technology Landscape 2026
  date: '2026-04-09'
  kind: web
- slug: 2026-03-26-sotf-interview-dorian-haci-mintneuro
  title: 'Chips for the Brain: Modular Semiconductors for Neural Interfaces (MintNeuro) / Dorian Haci)'
  date: '2026-03-26'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
neighbors:
- slug: 3d-ic-stacking
  name: 3D IC Stacking
  path: /manufacturing/packaging/3d-ic-stacking/
  macro: manufacturing
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
- slug: tsv-through-silicon-via
  name: TSV / Through-Silicon Via
  path: /manufacturing/packaging/tsv-through-silicon-via/
  macro: manufacturing
- slug: cowos
  name: CoWoS (TSMC)
  path: /manufacturing/packaging/cowos/
  macro: manufacturing
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: chiplets
  name: Chiplets
  path: /compute/compute-architecture/chiplets/
  macro: compute
---
**Heterogeneous integration is the practice of building a system from separately fabricated dies, materials and device layers joined in a package rather than on one monolithic wafer, and it has become the main route by which AI compute, optical interconnect and even quantum hardware keep scaling once single-die scaling stops paying.**

## Summary

Heterogeneous integration (HI) means assembling a working system from parts made in different processes, on different substrates, sometimes in different materials, and joining them at the package or wafer-bonding level. In the electrical domain this appears as chiplets on 2.5D interposers or 3D stacks, with high-bandwidth memory placed next to logic and different chiplets built on whatever technology node suits their function. In the photonic domain it appears as III-V gain material, thin-film lithium niobate (TFLN) or InGaAs/InP photodetectors bonded or transfer-printed onto silicon or silicon nitride waveguide circuits. The motive is the same in both cases: monolithic integration forces every function onto one process that is optimal for none of them, and yield and cost penalties grow with die area.

Mechanically, the enabling steps are attachment and interconnect. Die-to-wafer bonding, micro-transfer printing and through-substrate vias (TSVs) provide the physical joins; interposers, whether silicon, organic or glass, provide the wiring. Micro-transfer printing of TFLN onto 200 mm silicon photonics wafers has been shown with 3-sigma placement accuracy of 420 nm and printing yield above 95 per cent, giving insertion loss under 2 dB across 600 phase modulators and a half-wave voltage of 4 V. A separate group has bonded TFLN into the back end of line of a fully active silicon photonics platform, co-integrating 56 GHz germanium photodetectors and 100 GHz TFLN modulators on one chip.

The parameters that decide HI are not device parameters but system ones. First, cost: partitioning a design into chiplets with mixed technologies has been shown in simulation to cut cost by up to 43 per cent, 15 per cent geometric mean, relative to homogeneous partitioning. Second, thermo-mechanics: stacked and tightly placed dies produce hot spots and warpage that placement tools must now co-optimise alongside wirelength, and TSV arrays introduce coupling, insertion loss and self-heating that full-wave simulation cannot explore at scale. Third, interface overhead: electrostatic discharge protection and inter-chiplet signalling circuitry has been the main obstacle to shrinking chiplets below 100 mm2. Fourth, trust: multi-vendor assembly fragments the supply chain and opens routes to cloning, overproduction and chiplet substitution.

The frontier is moving from electrical chiplets, which are already commercial, to photonic and quantum HI, which is not. Examples in the literature include InGaAs-on-InP balanced photodetectors integrated onto ultra-low-loss thin-core silicon nitride delay-line interferometers, ytterbium gain in aluminium oxide designed to be compatible with heterogeneous integration into standard photonic platforms, modular chiplet-based trapped-ion processors and diamond colour-centre nanophotonics bonded to photonic integrated circuits for quantum network nodes.

## Viability (4/5)

The strongest evidence is manufacturing-grade rather than laboratory-grade. Micro-transfer printing of TFLN was run across four full 200 mm wafers with printing yield above 95 per cent and 420 nm 3-sigma placement accuracy, and the resulting population of 600 phase modulators held insertion loss below 2 dB. That is a yield and population statistic, not a hero device. Back-end-of-line TFLN bonding onto an already-active silicon photonics flow addresses the specific process incompatibility that previously confined TFLN to passive circuits, and delivers 100 GHz modulators alongside 56 GHz germanium detectors on the same die. On the electrical side, chiplet adoption is described as already growing in industry and 2.5D adoption as accelerating under AI and automotive demand.

What holds this short of 5 is that the hard problems have moved rather than disappeared. Multi-physics coupling in 3D stacks, manifesting as thermal hot spots, warpage-induced stress and interconnect ageing, is described as exceeding the reach of traditional offline metrology, with the digital-twin literature intended to address it still fragmented. Design-side tooling is visibly immature: new placers, partitioners and TSV surrogate models are all being proposed as first-of-kind. Photonic and quantum HI remain at the single-demonstration stage; the SiN balanced photodetector, for instance, is reported at 0.92 GHz bandwidth on a 15 m delay-line interferometer.

**TLDR: Wafer-scale demonstrations with quantified yield and loss exist; the electrical side is already in production use.**

## Drivers (4/5)

On the demand side the sources are unusually consistent. AI and datacentre growth is cited as driving the need for photonic interconnects combining high speed with low energy, as forcing a rethink of optical interconnect architecture in datacentres, and, alongside automotive, as accelerating 2.5D IC adoption specifically. The same pull extends beyond compute: a petabit-per-second single-package router architecture is proposed on the back of chiplet plus HBM integration and in-package optics.

On the supply side, the driver is that monolithic scaling now costs more than it returns. The industry transition to HI is framed explicitly as a response to the yield and cost challenges of monolithic scaling, and in the trapped-ion case as a response to CMOS flows that are simply not optimised for the device requirements at hand. A secondary and less mature driver is sustainability: embodied and operational carbon footprint is being treated as a first-class design constraint in HI pathfinding, though the sources give no evidence that carbon is yet a purchasing criterion.

**TLDR: Demand is AI datacentre bandwidth and compute; supply pull is the yield and cost wall of large monolithic dies.**

## Novelty (4/5)

The comparator is monolithic integration, and the margin is quantified in two places. In cost-aware partitioning, allowing heterogeneous manufacturing technologies across chiplets reduces cost by up to 43 per cent, 15 per cent geometric mean, over the homogeneous case. In devices, the argument is that no single platform provides everything: TFLN gives 100 GHz modulation that silicon cannot, while silicon provides low-loss fibre interfaces and germanium detectors, and back-end-of-line bonding lets you have both on one chip. The same logic underwrites III-V photodetectors on silicon nitride, where the SiN platform delivers ultra-low loss from visible to shortwave infrared but has lacked high-performance on-chip photodetection entirely.

The second novelty axis is modularity rather than performance. Chiplet-based trapped-ion processors allow each module to use its optimal material and fabrication route and allow new functionality to be added by changing only a subset of chiplets. Reducing chiplet interface overhead, currently the binding constraint below 100 mm2, would push composability and reuse further. HI is not a new idea in these sources; what is new is that it now works at wafer scale with reportable yield, and that the design tooling to exploit it is arriving.

**TLDR: Better than monolithic integration on cost, material choice and modularity, with quantified margins in partitioning studies and in TFLN-on-silicon device performance.**

## Diffusion (3/5)

The clearest statement of the adoption problem comes from the co-packaged optics critique: as optics move closer to compute, packaging, thermal management and system-level robustness come to dominate performance and scalability, and standardisation, serviceability and thermal-aware co-design will be decisive in whether CPO gets past early deployment. That is a diffusion argument, not a physics argument, and it applies to HI generally: the trade-offs it introduces are described as underappreciated in device-centric analyses.

The other barriers are structural. Multi-vendor assembly fragments the supply chain and creates cloning, overproduction and substitution risk, with existing authentication schemes depending on trusted integrators or centralised anchors; proposed alternatives claim area overhead as low as 0.48 per cent and authentication latency under 1 microsecond. Reliability management in 3D stacks needs closed-loop monitoring that current metrology does not provide. Material-level uncertainty persists in newer platforms: reported extinction coefficients for WS2 span orders of magnitude, leaving wafer-scale integration feasibility genuinely unresolved. And some coupling routes remain lossy, with a vertical grating coupler intended for VCSEL integration measuring 8.35 dB single-coupler insertion loss. A 3 reflects a genuinely split picture: adopted in one domain, contested in another.

**TLDR: Electrical chiplets are diffusing now; photonic and co-packaged HI face standardisation, serviceability, thermal and supply-chain-trust barriers that are explicitly unsolved.**

## Impact (4/5)

If HI works at scale, it becomes the mechanism by which system performance keeps improving after single-die scaling stops being economic, and the sources treat it as such: it is described as a central pillar of contemporary semiconductor scaling and as the industry's response to monolithic yield and cost limits. The claimed system-level payoffs are correspondingly large: a petabit-per-second router in a single package, and panel-scale glass interposers of 500 mm by 500 mm or larger hosting processor chiplets, HBM stacks and WDM optical links in one package.

The breadth matters as much as the depth. The same integration techniques underpin quantum network nodes built from diamond nanophotonics bonded to photonic integrated circuits, modular trapped-ion processors, and chip-scale rare-earth amplifiers reaching above 0.5 W output with over 70 per cent conversion efficiency and a 3.3 dB noise figure. A capability that is a prerequisite across compute, networking, sensing and quantum hardware is high-impact almost by definition. It falls short of 5 because much of the projected value, particularly the panel-scale and petabit-router claims, is architectural proposal rather than demonstrated result.

**TLDR: It is the substitute for monolithic scaling across AI compute, networking and integrated photonics, so the value is large and broad.**

## Timing Now (0-2yr)

The electrical half is not a forecast. Chiplet adoption is already growing for cost reasons and 2.5D adoption is described as accelerating under AI and automotive demand. What is in flight now is the supporting toolchain: thermo-mechanical-aware placement, carbon-aware pathfinding, TSV electro-thermal surrogates and chiplet authentication are all being published as new frameworks in 2025 and 2026.

The photonic half sits later. Wafer-scale TFLN printing on 200 mm silicon photonics was reported in May 2026 with production-relevant yield and back-end-of-line TFLN on active silicon photonics in December 2025, which puts foundry-offered heterogeneous photonics in the two-to-five-year window rather than now. Quantum applications of the same techniques, in diamond colour centres and trapped ions, are further out again and the sources do not date them.

**TLDR: Electrical 2.5D chiplet integration is being adopted today; the photonic layer is roughly a technology generation behind.**

## Overrated or underrated? Fairly rated

Heterogeneous integration is neither hype nor a secret. The industry has already decided it is the successor to monolithic scaling, and the evidence base here supports that: quantified cost advantages from heterogeneous partitioning, wafer-scale printing yields above 95 per cent, and device-level results such as 100 GHz TFLN modulators co-integrated with germanium detectors. Betting against it as a direction is not defensible.

Where expectations are miscalibrated is in what the bottleneck is. The literature here repeatedly says the limiting problems are no longer devices but packaging thermo-mechanics, design tooling, metrology, standardisation and supply-chain trust. That means the value accrues less to novel device demonstrations and more to whoever owns the assembly capacity, the interface standards and the co-design tools. Anyone underwriting HI on device performance alone is reading the wrong variable.

## Prediction

By the end of 2028, at least one commercial silicon photonics foundry will offer heterogeneously integrated thin-film lithium niobate modulators as a qualified process-design-kit element on a 200 mm wafer flow, with published yield at or above the 95 per cent printing yield already demonstrated in research.

## Evidence base

- May 2026: micro-transfer printing of TFLN across four full 200 mm silicon photonics wafers achieved 3-sigma placement accuracy of 420 nm, printing yield above 95 per cent, insertion loss under 2 dB across 600 phase modulators, and 4 V half-wave voltage.
- December 2025: first back-end-of-line heterogeneous integration of TFLN onto a fully active silicon photonics platform via trench-based die-to-wafer bonding, yielding 56 GHz germanium photodetectors and 100 GHz TFLN modulators on one chip.
- July 2025: cost-aware partitioning study finds heterogeneous integration reduces chiplet system cost by up to 43 per cent (15 per cent geometric mean) versus homogeneous technology assignment.
- November 2025: first analytical 2.5D placer jointly optimising wirelength, peak temperature and warpage reports 3 to 13 per cent lower temperature and 5 to 27 per cent less warpage than prior tools at roughly 10 times the speed, indicating that thermo-mechanics is now a first-order placement constraint.
- November 2025: ESD protection and inter-chiplet I/O circuitry identified as the main area constraint preventing chiplets shrinking below 100 mm2, with SPICE and parasitic-extraction analysis suggesting it can be simplified in future 2.5D/3D packaging.
- March 2026: co-packaged optics position paper argues packaging, thermal management and system robustness, not device performance, now dominate scalability, and that standardisation and serviceability will decide whether CPO moves beyond early deployment.

## Open questions

- Do the 200 mm micro-transfer-printing yields (>95 per cent, 420 nm 3-sigma placement) hold at 300 mm and across multiple modulator generations, or do they degrade with die count and thermal budget?
- Can the ESD and inter-chiplet signalling overhead actually be simplified enough in production packaging to take chiplets below 100 mm2, or does reliability qualification block the simplification proposed in simulation?
- Does anyone converge on standards for co-packaged optics serviceability and thermal interface, given that the sources name standardisation and serviceability as decisive for adoption but report no standards activity?
- Do the thermo-mechanical co-design tools (placement, TSV surrogates, digital twins) reach sign-off-grade accuracy, or do designers keep falling back on slow full-wave and finite-element flows that limit chiplet counts?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
