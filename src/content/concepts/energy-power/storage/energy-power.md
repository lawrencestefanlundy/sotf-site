---
type: concept
slug: energy-power
canonical_name: Energy & Power
aliases: []
kind: technology
parent_concepts:
- energy-power
- storage
related_concepts: []
sources: []
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
mention_count: 63
descendants:
- advanced-nuclear
- ai-power-delivery
- ai-thermal-management
- aluminium-gallium-nitride
- ambient-energy-harvesting
- batteries-energy-storage
- beccs
- carbon
- carbon-capture
- ccus
- closed-loop-geothermal
- compressed-air-energy-storage
- cryogenic-cooling
- cryogenics
- datacentre-power-shell
- deep-geothermal
- diamond-fet
- diamond-heat-spreader
- dilution-refrigerators
- direct-air-capture
- electric-motors-drives
- energy-generation
- energy-harvesting
- energy-materials
- energy-power
- energy-storage
- floating-offshore-platform
- flow-batteries
- fusion
- fusion-frc
- fusion-inertial-confinement
- fusion-magnetic-confinement
- fusion-stellarators
- fusion-z-pinch
- gallium-nitride
- gan-on-si
- generation
- geothermal
- graphene-thermal-films
- gravity-thermal-storage
- gw-scale-power-delivery
- haleu
- heat-pipes
- heterojunction-solar-hjt
- iec-61215-qualification
- immersion-cooling
- indium-gallium-nitride
- integrated-voltage-regulator
- lead-fast-reactor
- liquid-cooling
- liquid-cooling-datacentre
- lithium-sulphur-batteries
- long-duration-energy-storage
- long-duration-storage
- microfluidic-cooling
- mineralisation
- molten-salt-reactor
- nuclear-instrumentation
- ocean-alkalinity
- organic-photovoltaics
- pem-electrolysers
- perovskite
- perovskite-solar
- perovskite-stabilisation
- phase-change-materials
- photovoltaics
- power
- power-electronics
- power-management-ic
- pumped-hydro
- pv-cost-down-curve
- radiative-cooling
- renewable-electricity
- shockley-queisser-limit
- silicon-photovoltaics
- small-modular-reactors
- sodium-fast-reactor
- sodium-ion-batteries
- solar-photovoltaic
- solid-oxide-fuel-cells
- solid-state-batteries
- solid-state-circuit-breakers
- solid-state-cooling
- space-solar
- storage
- tandem-solar
- tandem-solar-cells
- thermal
- thermal-interface-materials
- thermal-management
- thermal-stack-map
- thermoelectric
- tim-approach-map
- topcon
- triso-fuel
- two-phase-cooling
- vapor-chambers
- vertical-gan
- wave-tidal
- wireless-power-transfer
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-09-03-what-comes-after-the-data-center-backlash---latitude-media
  title: What comes after the data center backlash? - Latitude Media
  date: '2026-09-03'
  kind: web
- slug: 2026-09-03-gridsight-raises-26m-series-b-to-unlock-electric-grid-capaci
  title: Gridsight raises $26M series B to unlock electric grid capacity and affordability - Latitude Media
  date: '2026-09-03'
  kind: web
- slug: 2026-09-03-three-questions-left-open-by-trumps-bulk-power-executive-ord
  title: Three questions left open by Trump’s bulk power executive order - Latitude Media
  date: '2026-09-03'
  kind: web
- slug: 2026-09-01-chinas-rare-earths-duopoly
  title: China's Rare Earths Duopoly
  date: '2026-09-01'
  kind: web
- slug: 2026-08-31-qcells-tandem-iec-ul-certification-tuv-rheinland
  title: Qcells secures TUV Rheinland certification for perovskite-silicon tandem solar tech (pv magazine, 16 Jul 2026; pv-tech corroborating)
  date: '2026-08-31'
  kind: web
- slug: 2026-08-31-ferc-206-show-cause-orders-large-load-interconnection
  title: FERC Issues Section 206 Show Cause Orders Directing All Six RTOs/ISOs to Justify or Reform Large Load Integration Rules (McGuireWoods client alert; FERC docket RM26-4 page corroborating)
  date: '2026-08-31'
  kind: web
- slug: 2026-08-27-the-case-against-relying-on-behind-the-meter-power-for-data-
  title: The case against relying on behind-the-meter power for data centers - staging.latitudemedia.com
  date: '2026-08-27'
  kind: web
- slug: 2026-08-26-making-data-centers-flexible-so-they-can-serve-the-grid-rath
  title: Making data centers flexible so they can serve the grid rather than stress it out
  date: '2026-08-26'
  kind: web
neighbors: []
---
**A cluster of 2026 research spanning heat-to-electricity materials, chip and data-centre power management, and computational tools for power systems, unified by one fact: energy and power, not silicon area or core count, are now the binding constraints on both compute and energy conversion hardware.**

## Summary

"Energy & Power" as represented in these sources is not a single technology but three loosely coupled research fronts that share a constraint. The first is **energy conversion and harvesting materials**: high-entropy engineered Fe2VAl full-Heusler thermoelectrics taken from powder to a fabricated module, high-entropy perovskite electrolytes printed at 6 to 10 microns for solid oxide fuel cells, bulk-scale spin Seebeck composites that escape thin-film diffusion limits, and a proposed near-field photon Nernst effect for probing nonreciprocal radiative transfer and harvesting energy. These convert thermal or chemical gradients into electricity, and the parameters that decide them are the thermoelectric figure of merit zT, lattice thermal conductivity, areal power density, and operating temperature.

The second front is **power as a first-class resource in computing**. Google's five-generation TPU retrospective reports a 3600x increase in supercomputer performance and a 100x increase in peak node performance over eight years alongside substantial gains in performance per Watt and carbon per floating point operation. Below that system level, work targets the same problem at finer granularity: component-level dynamic voltage and frequency scaling inside NPUs with sub-microsecond control, monolithic 3D cache scaling to cut off-chip data movement, racetrack memory caches to kill SRAM leakage, measured backend-specific energy attribution for mobile LLM inference, hardware-orchestrated power gating down to 452 nA quiescent drain for photovoltaic-harvesting sensor nodes, and thermodynamic computing that uses stochastic analog physics instead of digital arithmetic. One paper makes the framing explicit: on modern multicore parts the shared package power and thermal budget, not core occupancy, is the fundamental resource.

One caveat on taxonomy: this concept sits under *storage*, but the sources contain no energy storage work. The only storage discussed is data storage (racetrack memory, M3D cache, HBM). Nothing here supports a view on batteries, thermal stores or grid-scale storage.

## Viability (3/5)

Evidence quality splits sharply by strand. Compute power management is real and measured: five TPU generations in production with quantified performance-per-Watt and carbon-per-FLOP improvements, a hardware power-gating architecture with a measured 452 nA quiescent drain, and measurements on a recent AMD EPYC part showing how waiting strategy and topology trade against the package power budget. Mobile LLM energy attribution is empirical across five frameworks and three backends.

**TLDR: Demand-side power engineering is demonstrated in shipped silicon; the conversion materials and quantum strands are lab-stage.**

## Drivers (4/5)

Demand is stated plainly and repeatedly. LLM serving energy is described as a major system challenge driven by hardware power and thermal constraints and rising electricity costs; NPU power consumption is called a limiting factor for LLM service scaling; on-device inference is described as severely bottlenecked by hardware inefficiency; sensor-network autonomy is limited by quiescent current in low-light harvesting conditions; and rising distributed energy penetration is given as the driver for intentional islanding capability. That is unusually consistent demand signalling across independent groups and disciplines.

On the supply side, the enablers are named: optical circuit switches, built-in self test and hardware replay for resilience at scale, BEOL monolithic 3D integration for denser on-chip cache, and high-entropy alloy design plus hot pressing and high-pressure torsion for scaled material batches. The sources say nothing about cost curves, supply chains or capital availability, so the supply-side judgement is limited to technical feasibility.

**TLDR: Demand pull is explicit and documented across the sources; supply-side capability is uneven.**

## Novelty (3/5)

The clearest quantified improvements are in computing. Component-level DVFS is proposed against conventional chip-wide DVFS on the grounds that tensor operators bottleneck on different NPU components; framework-induced performance gaps on NPUs reach up to 10x depending on offloading and quantization strategy, which is a measurement of how much headroom current stacks waste; racetrack memory placement is improved against conventional placement strategies that trigger redundant shifts; and the polling paper inverts a standing assumption that idle cores are wasted compute. Virtual sensing is positioned against classical state estimation and pointwise soft sensing, claiming mesh-independent inference at arbitrary interior coordinates without per-instance retraining.

In materials the novelty is narrower. The Fe2VAl work claims one of the lowest lattice thermal conductivities reported for full-Heusler systems at about 2.3 W per metre-Kelvin, but the resulting zT_ave of roughly 0.3 is modest in absolute terms and the sources give no comparison against incumbent thermoelectric materials. The spin Seebeck result is genuinely architectural, moving from diffusion-limited thin films to bulk three-dimensional composites, and the photon Nernst effect is a new physical channel bounded by Carnot, but neither reports competitive output power against any incumbent.

**TLDR: Real incremental advances over named baselines; the largest claimed margins are in software and hardware power control, not in materials.**

## Diffusion (2/5)

The single confirmed diffusion case is the TPU line, where five generations of deployed training supercomputers are documented and the authors go so far as to name six features they expect to characterise successful future designs. Everything else carries an explicit adoption barrier. Component-level DVFS requires refactoring the NPU core pipeline into separate voltage and frequency domains plus ISA extensions, which is a new-silicon decision rather than a firmware update. M3D cache expansion depends on BEOL integration maturing and is evaluated in simulation. Racetrack memory still pays a serialised shift penalty in energy and latency.

**TLDR: Only the large-scale accelerator strand is demonstrably deployed; everything else faces hardware, temperature or integration barriers the sources do not clear.**

## Impact (4/5)

The upside is largest and best evidenced in computing. The TPU retrospective ties a 3600x supercomputer performance gain to concurrent improvements in performance per Watt and carbon emissions per floating point operation, which is the clearest demonstration in these sources that energy efficiency is the lever that converts into usable scale. Data movement between on-chip cache and off-chip HBM is identified as a key contributor to chip energy dissipation, so on-chip memory scaling attacks a first-order term rather than a rounding error. At the other end of the scale, cutting quiescent drain to 452 nA is what determines whether a harvesting sensor node survives low light at all, a binary outcome rather than a marginal one.

The negative-impact case is also worth weighing. Bit2Watt shows a tenant acting entirely within the cyber layer can induce power modulations that degrade damping and propagate harmonic distortion into a high-DER grid, and that routine cloud and facility monitoring is poorly placed to detect it because the signature sits in high-frequency components. That is a systemic risk created by the same coupling the efficiency work exploits. The conversion materials strand, at the performance levels reported here, does not yet support a large impact claim on its own.

**TLDR: If power is the binding constraint on compute scaling, efficiency work compounds directly into deliverable capability.**

## Timing Now (0-2yr)

The demand-side strand is not a forecast. Five TPU generations are already deployed with power efficiency as an explicit design axis, mobile inference energy is being profiled on shipping CPUs, GPUs and NPUs, and the package power budget is measurably the limiting resource on current server parts. Decisions made in the next two years about accelerator power domains, cache hierarchy and scheduling policy will be made under this constraint whether or not the specific mechanisms in these papers are adopted.

**TLDR: Power is already the binding design variable in compute; the materials and quantum strands are 5 to 10 years behind it.**

## Overrated or underrated? Underrated

The chip-efficiency story is well covered and roughly correctly valued. What is underrated in these sources is the reframing of power as an allocatable system resource and the two-way coupling between computing load and the grid. Two independent papers point the same way: on current server silicon the shared package power budget, not core occupancy, is the fundamental resource, which makes waiting policy a first-class design choice rather than an implementation detail; and a legitimate tenant manipulating GPU workloads can push high-frequency power modulations back into a high-DER local grid in a way that common telemetry does not capture. If both hold, the accounting unit for data-centre design shifts from FLOPS and cores to watts and grid impedance, and neither cloud operators nor utilities currently instrument for it.

The conversion materials half of this concept is, on this evidence, fairly rated or mildly overrated. A zT_ave of about 0.3 over 300 to 500 K in a fabricated module is credible engineering but far from a displacement threat to any incumbent, and the spin Seebeck and photon Nernst results are physics demonstrations with no output power comparison offered. Investors reading "energy and power" as a materials play are looking at the slower half.

## Prediction

By 31 July 2028, no peer-reviewed publication will report a fabricated Fe2VAl-based full-Heusler thermoelectric module with zT_ave above 0.6 across 300 to 500 K, leaving the 2026 figure of about 0.3 as the same order of magnitude.

## Evidence base

- 16 June 2026: Google reports 10x HBM capacity and bandwidth per node, 100x peak node performance and 3600x supercomputer performance across five TPU generations in eight years, alongside performance-per-Watt and carbon-per-FLOP improvements.
- 16 June 2026: high-entropy engineered Fe2VAl full-Heusler alloys reach lattice thermal conductivity of about 2.3 W per metre-Kelvin and zT_ave of about 0.3 from 300 to 500 K, with a full module fabricated from scaled-up hot-pressed batches.
- 16 June 2026: a hardware-orchestrated dynamic power management architecture achieves 452 nA quiescent drain by fully power-gating the microcontroller, with wake-up handled by an ultra-low-power PMIC, RTC and custom latch.
- 8 July 2026: cross-layer profiling of mobile LLM inference across five frameworks and three backends finds framework-induced performance gaps up to 10x on NPUs, and that NPUs win compute-bound prefill while CPUs win memory-bound decode.
- 8 July 2026: Bit2Watt demonstrates, via impedance-based analysis and power system simulation, that a legal tenant modulating GPU workloads can amplify fluctuations, harmonic distortion and damping degradation in high-DER-penetration grids while evading routine telemetry.
- 21 July 2026: measurements on a recent AMD EPYC processor support the claim that shared package power and thermal budget, not core occupancy, is the limiting resource, so reclaiming idle cores often yields less benefit than assumed.
- 21 July 2026: high-entropy perovskite electrolytes printed at 6 to 10 microns reach a maximum power density of 0.53 W per square centimetre at 973 K in a Ni-based anode, Ba0.5La0.5CoO3 cathode SOFC stack.

## Open questions

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
