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
- Does the slab-engineered zero-crosstalk approach survive process-corner variation and enter a commercial PDK, or does the cancellation condition prove too tight to hold across a wafer 2026 05 28 universal zero crosstalk photonic integration via slab engin?
- Do photonics-informed inverse lithography and automated placement measurably raise fabricated yield on large inverse-designed circuits, and by what factor against hand-designed baselines 2026 06 03 prism photonics informed inverse lithography for manufactura 2026 06 05 end to end physical design automation flow for yield optimiz?
- Can any of the emerging non-volatile opto-electronic resistive memory candidates meet endurance, retention and insertion-loss requirements simultaneously in a PIC process 2026 06 02 emerging non volatile opto electronic resistive memories for?
- Does the noise-compression result that permits deep all-optical cascades hold in a physically fabricated multi-layer chip rather than an OSNR recursion emulation 2022 shi soa aonn noise depth scaling?
- Does room-temperature SPAD coupling scale to high mode counts, or do superconducting nanowire detectors and their cryogenics remain unavoidable for serious quantum photonics 2026 06 05 laser written reconfigurable photonic integrated circuit dir 2026 05 15 superconducting single photon detectors for integrated quant?
- Does any single material platform take >70% of PIC volume by 2030, or do SiPh, InP and TFLN keep distinct segments as the IDTechEx 2026-2036 view projects? Watch datacom design wins and TFLN foundry capacity announcements.
- When does co-packaged optics cross from NPO pilots to volume, and does glass-substrate CoPoS clear its through-glass-via barriers before the ~2030 date supply-chain reporting now expects?
- Does 300 mm SiPh capacity (ST, UMC Singapore, GlobalFoundries, TSMC) commoditise the passive PIC die and push value into packaging, fibre attach and the laser, and what evidence would show PIC design margins compressing?
- Can monolithic integration close the remaining off-chip gaps at production loss levels? Lab isolators on Si still carry >20 dB insertion loss; watch for a foundry PDK offering an integrated isolator or on-chip laser as standard.
- Do integrated-photonics loss budgets reach what fault-tolerant photonic quantum computing needs? Nonlinear architectures claim ~12% loss tolerance; a foundry-fabricated demonstration at that budget would move the picture.
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 126
last_reorg_date: '2026-05-13'
descendants:
- avalanche-photodiode
- fiber-to-chip-coupling
- glass-photonics
- mid-ir-photonics
- photodetector
- pic-packaging-stack
- uni-traveling-carrier-photodiode
scorecard:
  viability: 4
  drivers: 3
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 1
sources_30d: 6
recent_mentions:
- slug: 2026-07-29-aeluma-signs-letter-of-intent-for-30m-chips-act-funding---in
  title: Aeluma signs letter of intent for $30M CHIPS Act funding - Investing.com
  date: '2026-07-29'
  kind: web
- slug: 2026-07-29-aeluma-signs-letter-of-intent-for-30-million-in-chips-act-fu
  title: Aeluma Signs Letter of Intent for $30 Million in CHIPS Act Funding - marketscreener.com
  date: '2026-07-29'
  kind: web
- slug: 2026-07-29-aeluma-secures-loi-for-up-to-30-million-in-chips-act-funding
  title: Aeluma Secures LOI for Up to $30 Million in CHIPS Act Funding to Advance Photonics Semiconductor R&D - Quiver Quantitative
  date: '2026-07-29'
  kind: web
- slug: 2026-06-16-coherent-signs-loi-for-up-to-50m-chips-act-grant-to-expand-t
  title: Coherent signs LOI for up to $50M CHIPS Act grant to expand Texas indium phosphide fab - Dealroom
  date: '2026-06-16'
  kind: web
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
neighbors: []
---
**Photonic integrated circuits route and manipulate light in lithographically defined waveguides on a chip, and the 2026 literature shows the field has moved from proving individual devices to fighting the system-level problems (crosstalk, fabrication variability, tuning drift, missing memory, detector integration) that decide whether large circuits can be built at all.**

## Summary

A photonic integrated circuit (PIC) is the optical analogue of an electronic IC: waveguides etched into a thin high-index film on a wafer replace wires, and the circuit's function comes from splitters, interferometers, ring resonators, modulators, amplifiers and detectors patterned alongside them. Where an electronic IC moves charge, a PIC moves optical fields, which buys enormous bandwidth per channel, wavelength-division parallelism and low latency, at the cost of components that are large compared with transistors and exquisitely sensitive to nanometre-scale geometry.

There is no single PIC platform. Silicon-on-insulator gives density and CMOS foundry compatibility; silicon nitride gives low loss and access to visible wavelengths; thin-film lithium niobate gives a strong Pockels effect for fast modulation; indium phosphide gives gain; and femtosecond-laser-written glass gives three-dimensional routing. Newer entrants are being pushed for specific failures of the incumbents: thin-film lithium tantalate has been demonstrated with dB/cm-scale loss and modulators flat to about 50 GHz at 532 nm, holding 5 dBm of modulated optical power for an hour where thin-film lithium niobate devices of similar structure could not, and driving 112 Gb/s over a 3 m underwater link and 64 Gb/s over 9 m. Low-confinement silicon nitride waveguides have been made by etching trenches only tens of nanometres deep in Borofloat 33 glass, filling with 50 nm of nitride and fusion-bonding two wafers to form a thick symmetric cladding, explicitly as a cost-reduction route.

The parameters that decide a PIC are propagation loss per centimetre, fibre or free-space coupling efficiency, the strength and power cost of the tuning mechanism (thermal, electro-optic, pressure, phase-change), inter-channel crosstalk, and reproducibility across a wafer. Each of these is now an active failure mode at scale. Crosstalk accumulates across cascaded components and caps integration density, which a 2026 result addresses by tailoring rib-waveguide slab thickness so that mode hybridisation cancels coupling between neighbours, demonstrated across silicon-on-insulator and silicon nitride in standard foundry processes. Fabrication deviations cause large optical response drift that compounds in cascades, and inverse-designed subwavelength geometries are the worst affected. Even thermal tuning models are wrong at the level that matters: material thermo-refractive coefficients of Si3N4 and SiO2 vary by 7% between telecom and visible wavelengths, and that material variation contributes 1.3 times more to dneff/dT than modal confinement does.

Two structural gaps recur. There is no established non-volatile memory element in photonics, so programmable circuits pay repeated optical-electrical conversion and electronic hold-power overheads. And there is no unified, fabrication-aware physical design automation stack of the kind electronics has, which is named as the limiting factor for large heterogeneous electronic-photonic chiplets.

## Viability (4/5)

The sources are dominated by fabricated, measured devices rather than proposals. Zero crosstalk was demonstrated experimentally across multiple material platforms in standard rib waveguides; a visible-band lithium tantalate modulator drove a working 112 Gb/s underwater link; a laser-written PIC coupled directly to a room-temperature silicon single-photon avalanche diode array reached 41.0% system detection efficiency at 561 nm, reported as the highest for such systems; and a fully on-chip spatio-temporal encoding microscope replaced the bulky free-space optics of high-speed flow imaging. That is a technology that works at the scale of tens to hundreds of elements.

What is not yet viable is the large, programmable, high-yield circuit. Manufacturability is explicitly described as the bottleneck for inverse-designed PICs, with irregular subwavelength geometries producing low yield and a persistent simulation-to-silicon gap. Mach-Zehnder mesh architectures, the standard route to programmability, are said to hit loss, fabrication and scalability bottlenecks from beam splitting and light bending, which is the motivation for programmable waveguide arrays as an alternative that is itself still early. Characterisation drift is severe enough that conventional DC voltage scanning of lithium niobate nanocavities yields unreliable electro-optic tuning numbers, established across 35 devices. A 4 reflects strong demonstrated results at device and subsystem level with the scaling question open.

**TLDR: Component and subsystem performance is demonstrated repeatedly on real wafers; large-circuit yield and programmability are not.**

## Drivers (3/5)

On demand, the clearest statement is that as AI systems scale to multi-chiplet and wafer-level architectures, the requirement for ultra-high bandwidth and system scalability has outpaced electrical interconnects and computing units, with heterogeneous electronic-photonic chiplets offered as the answer. Quantum technologies supply a second pull: scalability and practical deployment are driving detector integration onto PICs, and heterogeneous integration of diamond nanophotonics with PICs is presented as the route to scalable quantum processor and network nodes. Application niches with their own pull include visible-band AR/VR and quantum control, high-throughput cell imaging, and underwater optical links.

On supply, the sources show the shape of the constraint rather than its size: foundry compatibility is treated as a precondition for adoption of any new technique, repeated fabrication cycles for model calibration are described as costly and inaccessible to most designers, and reducing fabrication cost is the explicit motivation for glass-bonded nitride waveguides. There are no capacity figures, wafer volumes, funding numbers or market sizes in these sources, so the score is capped at 3.

**TLDR: Demand pull from AI interconnect and quantum systems is stated in the sources; supply-side and market data are absent.**

## Novelty (4/5)

The methodological novelty is at least as significant as the device novelty. Crosstalk suppression that works in standard rib waveguides across several material systems is a different proposition from crosstalk suppression that needs bespoke nanostructures, because it can enter existing foundry flows. Inverse design is claimed to give orders-of-magnitude improvement in spatial and spectral density over hand-designed components, and photonics-informed inverse lithography is the first systematic mask optimisation flow offered for the field, an explicit borrowing from what electronics already has. Novel tuning physics is also appearing: hydrostatic pressure up to 5 GPa shifts a Fabry-Perot resonance by up to 30 nm in silicon nitride with a 4% relative index decrease, without injecting free carriers. Not a 5, because the sources do not show any of this displacing an incumbent in production.

**TLDR: Better than electrical interconnect for bandwidth and better than free-space optics for robustness, with several 2026 results beating their own platform's incumbent by a measurable margin.**

## Diffusion (3/5)

Four adoption barriers are named directly. First, design automation: practical adoption of large heterogeneous electronic-photonic chiplets is limited by the absence of a unified, fabrication-aware physical design stack covering inverse design, placement and routing. Second, yield and manufacturability: fabrication deviations cause large optical response drift and compounding error in cascaded circuits, and calibrating fabrication models is costly and expertise-heavy. Third, memory: without efficient, scalable non-volatile elements, fully programmable and adaptive photonic systems carry energy, latency and architectural penalties from conventional electronic memory and repeated optical-electrical conversion. Fourth, metrology: visible PICs have lacked a high-resolution nondestructive diagnostic comparable to the optical frequency-domain reflectometry used in infrared silicon photonics, a gap only now being filled by spectral-domain OCT with 50 dB dynamic range, 8 um axial resolution in silicon nitride and 2 mm imaging depth.

The encouraging pattern is that several 2026 solutions are being designed for adoptability rather than record-setting: foundry-process compatibility for crosstalk cancellation, cost reduction and technological simplicity for glass-bonded nitride, room-temperature detectors to escape cryogenics, and measurement methods designed to make published tuning-efficiency numbers trustworthy. Against that, none of these has been shown to be in a released process design kit in the sources, and quantum-network integration still faces challenges described as fundamental as well as experimental. Credible but contested.

**TLDR: The barriers are unusually well characterised in these sources, and they are tooling and yield barriers rather than physics barriers.**

## Impact (4/5)

The breadth of the source set is itself the impact argument: the same waveguide technology underpins high-speed communication, sensing and information processing, quantum simulation, photonic neural networks, topological photonics and nonlinear optics, metropolitan-scale quantum networks and distributed quantum computing, AR/VR and quantum control, clinical-scale cell imaging and underwater links. A platform technology that is the enabling layer for that many distinct fields has high expected value if the yield problem is solved.

There are also specific results suggesting the value is not merely additive. In all-optical neural networks based on semiconductor optical amplifiers, M-to-1 cross-gain-modulation wavelength conversion compresses input noise so that below roughly 19 dB input optical signal-to-noise ratio the output OSNR is higher than the input, meaning amplified spontaneous emission need not accumulate fatally across cascaded layers **2022 Shi Soa Aonn Noise Depth Scaling**. That is a depth-scaling argument specific to photonic hardware with no electronic analogue. The score is held at 4 rather than 5 because the sources contain no quantified system-level comparison against an electronic baseline: no energy per operation, no cost per bit, no throughput ratio.

**TLDR: If large-scale programmable PICs become manufacturable, they sit on the critical path for AI interconnect, optical computing and quantum systems; the sources assert this rather than size it.**

## Timing Now (0-2yr)

For narrow, single-function circuits the technology matters now. A visible-band integrated modulator has already carried 112 Gb/s over a 3 m underwater link and 64 Gb/s over 9 m, a monolithic PIC microscope reconstructs images of cells in flow, and room-temperature detector coupling at 41.0% efficiency removes a major practical obstacle from integrated quantum optics. The design-automation and metrology layers needed to industrialise these are appearing in the same period.

The larger prize is on a slower clock. Wafer-scale electronic-photonic chiplets are gated on a design stack that is being proposed, not deployed; non-volatile photonic memory is still classed as emerging; programmable waveguide arrays are a perspective on a next-generation architecture with modelling, fabrication and control problems unsolved; and quantum network nodes retain fundamental open challenges. Expect the split to persist: shipping components now, credible large-scale programmable photonics later in the decade.

**TLDR: Point applications are already at working-system level; the large programmable and quantum-scale circuits are a 5-10 year proposition.**

## Overrated or underrated? Fairly rated

The 2026 literature reads like a field that has stopped arguing about whether light can be guided usefully on a chip and started doing the unglamorous work that decides whether it can be manufactured: mask optimisation and yield, placement and routing automation, foundry-compatible crosstalk cancellation, honest tuning-efficiency metrology, corrected thermal models and nondestructive diagnostics. That is what maturation looks like, and it is a reason for confidence in the platform and for scepticism about any near-term claim of large-scale programmable optical computing.

The honest position is that PICs as a category are not overhyped, but specific branches are ahead of their evidence. Modulators, links, sensing and imaging are real. Programmable meshes are conceded by their own advocates to hit loss and scalability limits, and the proposed alternative is still a perspective paper. Anything requiring non-volatile state on chip is waiting on a memory element that does not yet exist in mature form. Judge individual PIC claims by which of those buckets they fall into.

## Prediction

By 31 December 2028, at least one foundry-accessible PIC process will offer a qualified non-volatile phase or memory element as a standard library component; absent that, published large-scale programmable photonic processors will continue to depend on continuously powered electronic tuning control.

## Evidence base

- 14 May 2026: thin-film lithium tantalate waveguides with dB/cm-scale loss and modulators flat to ~50 GHz at 532 nm sustained 5 dBm modulated power for an hour, unlike comparable thin-film lithium niobate devices, and delivered 112 Gb/s over 3 m and 64 Gb/s over 9 m underwater.
- 28 May 2026: complete cancellation of coupling between adjacent standard rib waveguides via slab-thickness-engineered mode hybridisation, demonstrated experimentally across silicon-on-insulator and silicon nitride in foundry-compatible geometries.
- 5 June 2026 (posted from 6 Dec 2025 work): a femtosecond-laser-written PIC directly coupled to a room-temperature silicon SPAD array reached 41.0% system detection efficiency at 561 nm, reported as the highest among heterogeneous, hybrid and directly coupled systems, with robustness to misalignment.
- 5 June 2026: measured 7% variation in Si3N4 and SiO2 thermo-refractive coefficients between telecom and visible bands, with the material contribution to dneff/dT 1.3 times that of modal confinement, invalidating the usual non-dispersive assumption in tuning design.
- 2 June 2026: across 35 devices, conventional quasi-static DC scanning of lithium niobate photonic crystal nanobeam cavities was shown to give unreliable electro-optic tuning efficiencies due to DC drift, requiring high-frequency triangular-wave sweeps instead.
- 2 September 2022: in an SOA all-optical neuron with 7 WDM channels at 10 Gbit/s and -17.5 dBm per channel, cross-gain-modulation noise compression makes the output OSNR exceed the input OSNR when input OSNR is below about 19 dB, so amplified spontaneous emission does not accumulate without limit across layers **2022 Shi Soa Aonn Noise Depth Scaling**.

## Open questions

- Does the slab-engineered zero-crosstalk approach survive process-corner variation and enter a commercial PDK, or does the cancellation condition prove too tight to hold across a wafer?
- Do photonics-informed inverse lithography and automated placement measurably raise fabricated yield on large inverse-designed circuits, and by what factor against hand-designed baselines?
- Can any of the emerging non-volatile opto-electronic resistive memory candidates meet endurance, retention and insertion-loss requirements simultaneously in a PIC process?
- Does the noise-compression result that permits deep all-optical cascades hold in a physically fabricated multi-layer chip rather than an OSNR recursion emulation **2022 Shi Soa Aonn Noise Depth Scaling**?
- Does room-temperature SPAD coupling scale to high mode counts, or do superconducting nanowire detectors and their cryogenics remain unavoidable for serious quantum photonics?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
