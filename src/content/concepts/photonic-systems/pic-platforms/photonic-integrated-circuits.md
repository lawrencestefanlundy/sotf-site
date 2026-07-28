---
type: concept
slug: photonic-integrated-circuits
canonical_name: Photonic Integrated Circuits
aliases: []
kind: technology
parent_concepts:
- photonic-systems
- pic-platforms
related_concepts: []
sources:
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-03-30-photonics-material-class-war-silicon-photonics-and-photonic]]'
- '[[2026-03-31-memq-10m-series-a]]'
- '[[2026-06-01-nibras-ucl-chipstart]]'
frontier:
- Does any single material platform take >70% of PIC volume by 2030, or do SiPh, InP and TFLN keep distinct segments as the IDTechEx 2026-2036 view projects? Watch datacom design wins and TFLN foundry capacity announcements.
- When does co-packaged optics cross from NPO pilots to volume, and does glass-substrate CoPoS clear its through-glass-via barriers before the ~2030 date supply-chain reporting now expects?
- Does 300 mm SiPh capacity (ST, UMC Singapore, GlobalFoundries, TSMC) commoditise the passive PIC die and push value into packaging, fibre attach and the laser, and what evidence would show PIC design margins compressing?
- Can monolithic integration close the remaining off-chip gaps at production loss levels? Lab isolators on Si still carry >20 dB insertion loss; watch for a foundry PDK offering an integrated isolator or on-chip laser as standard.
- Do integrated-photonics loss budgets reach what fault-tolerant photonic quantum computing needs? Nonlinear architectures claim ~12% loss tolerance; a foundry-fabricated demonstration at that budget would move the picture.
last_updated: '2026-07-26'
tags:
- concept
- technology
mention_count: 115
last_reorg_date: '2026-05-13'
descendants:
- avalanche-photodiode
- fiber-to-chip-coupling
- glass-photonics
- mid-ir-photonics
- photodetector
- pic-packaging-stack
- uni-traveling-carrier-photodiode
sources_7d: 3
sources_30d: 12
recent_mentions:
- slug: 2026-06-01-nibras-ucl-chipstart
  title: UCL EEE ventures selected for national ChipStart programme (incl. Nibras Communications)
  date: '2026-06-01'
  kind: web
- slug: 2026-03-31-memq-10m-series-a
  title: memQ Raises $10 Million in Series A
  date: '2026-03-31'
  kind: web
- slug: 2026-03-30-photonics-material-class-war-silicon-photonics-and-photonic
  title: 'Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts'
  date: '2026-03-30'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
neighbors: []
---
## Physics / mechanism

Photonic integrated circuits (PICs) route, modulate, and detect light on a chip using waveguides, splitters, modulators, and photodetectors fabricated in a common substrate. Silicon photonics dominates volume production with waveguide losses around 1-2 dB/cm and Mach-Zehnder or microring modulators at 50-100+ Gb/s per lane; silicon nitride offers roughly 0.1 dB/cm for passive, loss-critical functions; InP gives monolithic gain; thin-film lithium niobate (TFLN) gives high-bandwidth electro-optic modulation. Key metrics remain insertion loss, modulation bandwidth, fibre coupling efficiency, and yield.

Three mechanism-level threads stand out in the recent tier-1 literature:

Quantum photonics is now the dominant tier-1 research stream tagged to this concept. Representative results: a chiral quantum-dot interface at telecom O-band with 0.985 emission directionality on an InP microdisk coupled to a waveguide **2026 07 24 Directional Telecom Photons From A Chirally Coupled Quantum **; a PPLN microresonator quantum frequency comb with 461 frequency bins and coincidence-to-accidental ratio up to 16,000 **2026 07 23 Quantum Frequency Comb With Pump Selectable Bin Pairing And **; a nonlinear photonic fault-tolerance architecture claiming ~12% optical loss tolerance versus far tighter budgets for linear-optics schemes **2026 07 23 Nonlinear Photonic Architecture For Fault Tolerant Quantum C**; and trap-integrated photonics projected to lift remote-entanglement rates and fidelity (99.9% Bell pairs) in modular trapped-ion machines, so the PIC becomes the interconnect layer for other qubit modalities too **2026 07 22 Remote Entanglement Need Not Be The Bottleneck For Modular T**. Trainability analysis of photonic variational circuits identifies regimes with polynomial sample cost **2026 07 24 The Trainability Of Photonic Quantum Circuits**, and Quandela-platform work on hybrid photonic quantum ML is active but shows modest, dataset-dependent gains **2026 07 23 Pn Qnn Harnessing Physical Noise As A Native Regularizer In ** **2026 07 23 Q Photonas Hybrid Quantum Neural Architecture Search Framewo**.

## Competitive landscape

The platform battle has not resolved. The IDTechEx 2026-2036 view has silicon photonics, InP, and TFLN competing with distinct positions rather than a single winner, which is evidence against the winner-take-all reading of the material-class war **2026 03 30 Photonics Material Class War Silicon Photonics And Photonic**.

| Platform | Advantage | Limitation |
|---|---|---|
| Silicon photonics | CMOS-compatible, 300 mm volume path, low cost | No native laser or isolator, two-photon absorption at high power |
| InP | Monolithic laser + gain, telecom heritage | Small wafers, expensive, niche foundry base |
| Silicon nitride | Ultralow loss, wide transparency window | Passive-only without heterogeneous integration |
| TFLN | >100 GHz electro-optic bandwidth, strong chi(2) for quantum light sources | Immature foundry base, fibre coupling and cost still open |

**Foundry access.** The AI-datacentre interconnect pull is dragging silicon photonics into mainstream 300 mm logic fabs: ST is pushing 300 mm SiPh for denser optical links **2026 07 16 Ai Data Centers Push Silicon Photonics Toward 300 Mm Scale**, UMC has started photonic chip production in Singapore **2026 07 14 Taiwans No 2 Chipmaker Umc Starts Photonic Chip Production I**, and GlobalFoundries continues to build out its Fotonix SiPh platform for AI-era connectivity **2026 06 30 Globalfoundries Advances Silicon Photonics Platform For Ai E**. In Europe, TNO and ASML have joined to scale photonic chip manufacturing **2026 06 30 Tno Asml Join Forces To Scale Europes Photonic Chip Manufact**, alongside the established imec, Leti and PhotonDelta routes. Direction of travel: the passive SiPh die is becoming a foundry commodity, and differentiation is migrating to what the big fabs do not supply (light source, isolation, packaging, novel modulator materials).

**Packaging is where the fight moved.** Supply-chain reporting has advanced packaging growing faster than front-end, with near-packaged optics (NPO) as the commercial stepping-stone to co-packaged optics **2026 07 16 Exclusive Advanced Packaging Outpaces Front End Growth While**, and CPO commercialization opening a new SiPh packaging race among Taiwan OSATs **2026 07 22 Cpo Commercialization Opens New Siph Packaging Race For Taiw**. The next substrate battle is glass: Enflame showed China's first glass-based CoPoS AI-chip sample at WAIC 2026 **2026 07 22 Waic 2026 Enflame Debuts Chinas First Glass Based Copos Ai C**, but through-glass-via (TGV) barriers push CoPoS commercialization out to around 2030 **2026 07 24 Tgv Still Faces Technical Barriers Copos Commercialization N**. Confidence note: these four are headline-level DigiTimes/analyst items, directionally consistent with each other but thin on detail; treat the 2030 CoPoS date as one analyst's estimate, not consensus.

## Where value pools

The concept sits under the **Optical Interconnect Cpo Transition**, **Photonic Foundry Capacity**, **Pic Market Structure 2030**, **Photonic Packaging Cpo**, **Photonic Compute Market** and **Photonic Quantum Displacement** ideas. The structural read: with 300 mm SiPh capacity arriving from ST, UMC, GF and TSMC, a standard PIC design is on its way to being a commodity, and value pools in the layers the big fabs do not own, meaning packaging and fibre attach, the integrated light source and isolator, TFLN and other modulator materials, and quantum-photonic components. Note the volume of photonic quantum computing activity this concept attracts; the tier-1 stream above gives the technical baseline for evaluating those claims.

Routing (all vehicles): the incumbent capacity build-out (foundries, OSATs, optics suppliers) is primarily a public-markets expression; the non-commodity wedges above are where startup capture is plausible, with GF Fotonix and the European access routes (imec, Leti, PhotonDelta, the TNO-ASML effort) as the realistic production paths for an EU pre-seed company, and angel as the route for anything outside that cheque or geography.

Superseded claims removed in this pass: the old page's Lunar Ventures sourcing line (the Lunar route was retired 31 Jul 2026) and the SiN "no active modulation" limitation stated without qualification (heterogeneous and thermo-optic actives on SiN are routine; the honest limitation is passive-only without heterogeneous integration).

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)