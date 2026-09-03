---
type: concept
slug: power-electronics
canonical_name: Power Electronics
aliases: []
kind: technology
parent_concepts:
- energy-power
- power-electronics
related_concepts: []
sources:
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-03-08-diamonds-are-semiconductors-best-friend]]'
- '[[2025-09-11-power-electronics-researchers-awarded-15m-to-advance-energy-]]'
- '[[2024-yole-power-gan-2024]]'
- '[[2026-05-26-semianalysis-800vdc-revolution]]'
- '[[2024-omdia-power-electronics-forecast]]'
- '[[2026-02-19-the-rise-of-grid-power-electronics-with-drew-baglino---latit]]'
- '[[2026-07-26-humanoid-duty-cycle-thermal-constraint]]'
- '[[2026-09-02-vertical-power-delivery-thermal-limits]]'
scorecard:
  viability: 5
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 5
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
mention_count: 62
descendants:
- ai-power-delivery
- aluminium-gallium-nitride
- diamond-fet
- electric-motors-drives
- gallium-nitride
- gan-on-si
- gw-scale-power-delivery
- indium-gallium-nitride
- integrated-voltage-regulator
- power
- power-electronics
- power-management-ic
- solid-state-circuit-breakers
- vertical-gan
- wireless-power-transfer
sources_7d: 2
sources_30d: 4
recent_mentions:
- slug: 2026-09-02-vertical-power-delivery-thermal-limits
  title: 'Vertical power delivery: the thermal limit at the 48V-to-point-of-load stage'
  date: '2026-09-02'
  kind: web
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-05-26-semianalysis-800vdc-revolution
  title: Inside the 800VDC Revolution – Part 1
  date: '2026-05-26'
  kind: web
- slug: 2026-03-08-diamonds-are-semiconductors-best-friend
  title: Diamonds are Semiconductors' Best Friend 2026
  date: '2026-03-08'
  kind: web
- slug: 2026-02-19-the-rise-of-grid-power-electronics-with-drew-baglino---latit
  title: The rise of grid power electronics with Drew Baglino - Latitude Media
  date: '2026-02-19'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
- slug: 2025-09-11-power-electronics-researchers-awarded-15m-to-advance-energy-
  title: Power electronics researchers awarded $1.5M to advance energy technologies - University of Colorado Boulder
  date: '2025-09-11'
  kind: web
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors: []
---
**Power electronics is the switching, conversion and control layer that moves electrical energy between sources and loads, and it has become the binding constraint on both AI datacentre buildout and vehicle electrification: a roughly $45B market in 2024 forecast to reach ~$70B by 2030, with wide-bandgap devices and 800V DC architectures the contested frontier **2024 Omdia Power Electronics Forecast** <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup>.**

## Summary

Power electronics is the engineering of controlled electrical energy conversion: semiconductor switches (MOSFETs, IGBTs, HEMTs) chopped at high frequency, wrapped in magnetics and capacitors, under closed-loop control, to convert AC to DC, step voltages up or down, and drive motors. Almost every unit of electricity that reaches a chip, a motor or a battery passes through several such conversion stages. Each stage dissipates a few percent of the energy it handles, so the field's whole economic logic is loss reduction and power density: fewer watts wasted as heat, and fewer kilograms and litres of magnetics and heatsink per kilowatt delivered.

The parameters that decide everything are: the switch's on-resistance at a given breakdown voltage (set by material bandgap), the switching frequency it tolerates (higher frequency shrinks the magnetics), and how fast heat can be pulled out of the die. Silicon is the incumbent. Silicon carbide and gallium nitride are the commercial wide-bandgap challengers, GaN growing at 25-30% CAGR and SiC at around 30% through 2030 on analyst models **2024 Omdia Power Electronics Forecast**. Behind them sit ultra-wide-bandgap materials, principally beta-Ga2O3 and cubic boron nitride, which promise higher blocking fields but whose research literature is dominated by unsolved problems: Ga2O3/SiC heterointegration is described as bottlenecked by interfacial thermal boundary conductance as the heat-removal path, and c-BN is still at the stage of high-throughput defect screening rather than devices.

The second frontier is architectural rather than material. Rising GPU rack power, heading towards roughly 600kW, makes 48-54V distribution unworkable; moving datacentre distribution to 800V DC cuts current and resistive losses and reportedly shaves several percent off facility power, with a projected ~39GW of incremental capacity on 800VDC by 2030 and two new equipment markets: power racks and sidecars peaking near $11B around 2028, and solid-state transformers at $13B-$32B by 2030 depending on the source <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup>. A third, less discussed consequence is that as grids themselves become power-electronic-dominated, they inherit new failure modes: harmonic distortion and dynamic instability in multi-terminal transmission, and a demonstrated cyber-physical attack path in which GPU workload manipulation induces high-frequency power modulation that destabilises local infrastructure.

## Viability (5/5)

Power electronics is not a speculative technology. It is a ~$45B market in 2024 on analyst tracking, with silicon, SiC and GaN all shipping in volume and hyperscaler design wins already shifting from silicon to GaN across 2024-2025 **2024 Omdia Power Electronics Forecast** **2024 Yole Power Gan 2024**. Viability questions therefore apply to specific layers rather than the category. GaN is credited with reaching device cost parity with silicon MOSFETs in the 600V class by 2027 **2024 Yole Power Gan 2024**, which is the relevant viability test for that segment.

The research-stage tiers are earlier but showing device-level results rather than only materials characterisation. Vertical GaN-on-silicon, long blocked by high-resistance buffer layers, has been demonstrated with a sub-nanometre (0.5nm) silicide template formed by rapid thermal annealing, giving ohmic vertical conduction across 25 different metallic species and serving as a platform for MOCVD overgrowth. On gallium oxide, LPCVD Sn-doped homoepitaxy has produced controlled carrier concentrations from 1.17e17 to 3.06e18 cm-3 with Hall mobilities of 113 down to 63 cm2/Vs and films 1.66 to 11.3 microns thick at 6.4 to 16.6 microns per hour, and a vertical Ga2O3 transistor architecture avoiding planarization etch-back has shown enhancement-mode operation at 2V threshold with on-off ratio above 1e7. These are first-device results, not qualified parts, and the recurring limiter across the corpus is heat: interfacial thermal conductance at Ga2O3/SiC and the thermal limits of III-nitride HEMTs at elevated temperature.

**TLDR: The field is deployed at industrial scale; only the ultra-wide-bandgap tier is unproven.**

## Drivers (4/5)

Demand: two independent analyst houses converge on a power semiconductor market moving from ~$45B in 2024 to ~$70B by 2030, with GaN at 25-30% CAGR and SiC around 30% **2024 Omdia Power Electronics Forecast**, and Yole puts GaN specifically on a ~$0.5B to ~$5B+ path with datacentre PSU, 48V intermediate bus and point-of-load as the fastest-growing segment **2024 Yole Power Gan 2024**. The AI datacentre pull is the sharpest single driver: rack power heading to ~600kW forces a distribution voltage change, with a phased retrofit wave starting in 2026 and ~39GW of incremental 800VDC capacity projected by 2030, led by Google and Meta through OCP working groups and the Diablo 400 spec with Microsoft <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup>. Vehicle electrification supplies the SiC demand base.

Supply: consolidation and capacity are already committed, with the Infineon-GaN Systems acquisition and a 200mm ramp at Villach cited as the structural moves **2024 Yole Power Gan 2024**. The counterweight is price: Omdia models SiC oversupply arriving earlier than Yole and expects China to capture at least 50% of global silicon power device unit volume by 2028 **2024 Omdia Power Electronics Forecast**. That combination points to volume growth with compressing margins, which is why this scores 4 rather than 5. A second-order driver appears on the grid side: the proliferation of power electronics is itself generating harmonic distortion and stability problems that create demand for analysis and control tooling.

## Novelty (3/5)

The comparison that matters is against silicon MOSFETs and IGBTs, and against legacy AC/48V system architecture. At system level the margin is stated: 800VDC cuts current and resistive losses relative to 48-54V distribution and shaves several percent off facility power, and ±400VDC bipolar has the additional advantage of reusing EV-grade 400V parts <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup>. At device level the sources are more about cost than physics: the load-bearing claim is GaN reaching cost parity with silicon in the 600V class by 2027 **2024 Yole Power Gan 2024**, which implies GaN's efficiency advantage becomes free rather than paid for.

The research-tier novelty is genuine but narrow. The sputtered silicide template for vertical GaN-on-Si is presented as removing a specific bottleneck, the high electrical resistance of conventional epitaxial buffers, and as bridging low-cost silicon substrates to device-grade vertical performance. The Ga2O3 ISEFET is claimed as the first vertical gallium oxide architecture needing neither planarization etch-back nor mid-gap acceptor blocking layers, and is described as comparable to, not better than, existing vertical transistors. Similarly, active passivation that shifts a GaN transistor's hotspot from the gate edge to the drain-side passivation edge is a useful new design knob rather than a step change. No source in this set gives a quantified figure-of-merit advantage of Ga2O3 or c-BN devices over shipping SiC or GaN parts.

**TLDR: Real gains over silicon and over 48V architectures, but the sources quantify them thinly at device level.**

## Diffusion (4/5)

Diffusion evidence is stronger here than for most deep-tech categories because named buyers are already switching: hyperscaler design wins moving from silicon to GaN through 2024-2025 **2024 Yole Power Gan 2024**, and Google, Meta and Microsoft driving 800VDC specification through OCP and the Diablo 400 spec <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup>. The retrofit path is deliberately incremental: white-space power racks and sidecars first, then facility-level DC, then solid-state transformers post-2029, which lets adoption proceed without rebuilding facilities at once <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup>.

The barriers are institutional. Regulatory and safety standards, specifically DC arc-flash, busway, NEC and UL, are identified as the real bottleneck rather than component availability <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup>. Behind that sit qualification cycles for new switch technologies in mission-critical power paths, and the reliability question that the thermal literature keeps raising: III-nitride HEMTs need explicit barrier, channel, substrate and passivation engineering to hold performance at high temperature, and the remaining challenges are described as open. For the ultra-wide-bandgap tier there is no diffusion evidence at all in these sources; the work is at epitaxy, doping and defect-screening stage.

**TLDR: Adoption is already under way and hyperscaler-led; standards and safety codes, not device physics, are the named bottleneck.**

## Impact (5/5)

If the conversion layer improves, the effects compound across every electrified system: a few percent of facility power in a datacentre, range and inverter mass in a vehicle, and the amount of GPU capacity that can be energised behind a given feeder. The direct market value is measurable: ~$45B to ~$70B for power semiconductors by 2030 **2024 Omdia Power Electronics Forecast**, plus two new equipment categories created by the architectural shift, power racks and sidecars peaking near $11B around 2028 and solid-state transformers at $13B-$32B by 2030 <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup>. The framing that power delivery rather than generation is the binding datacentre constraint is what makes the impact case unusually strong.

There is a negative-impact tail that belongs in the same assessment. A power-electronic-dominated grid is more susceptible to harmonic distortion and damping degradation, and the Bit2Watt work shows an adversary operating purely as a legitimate cloud tenant can modulate GPU workloads to amplify fluctuations and destabilise local infrastructure, with the distinctive signature concentrated in high-frequency components that routine telemetry captures poorly. Analysing these resonances at scale is itself becoming computationally hard enough that quantum-classical hybrid eigensolvers are being proposed, so far validated only on a 5-bus system.

**TLDR: Power delivery, not generation or compute, is the constraint that gates AI capacity, and the market numbers are large and convergent.**

## Timing Now (0-2yr)

The GaN and 800VDC transitions have specific near-term dates attached. The 800VDC retrofit wave is framed as starting in 2026 with white-space power racks and sidecars, moving to facility-level DC and only reaching solid-state transformers post-2029 <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup>. GaN device cost parity with silicon in the 600V class is placed at 2027, with datacentre PSU as the fastest-growing segment **2024 Yole Power Gan 2024**. Both imply the decisions that determine market share are being made now, not later.

Ultra-wide-bandgap materials sit on a different clock. Gallium oxide work in this set is at the level of record LPCVD mobilities and first vertical device architectures, with heat removal at the Ga2O3/SiC interface still unsolved and being probed by machine-learned potentials rather than by measurement. Cubic boron nitride is at high-throughput defect screening, over 8000 defects calculated. Nothing in the sources supports a commercial date for either.

**TLDR: The commercial inflection is dated to 2026-2028; the ultra-wide-bandgap tier is a separate, much later question.**

## Overrated or underrated? Underrated

Two qualifications keep this from being an unqualified bull case. First, segment-level overrating is real: Omdia already models SiC oversupply arriving earlier than Yole assumes, and Chinese capture of at least 50% of global silicon power device unit volume by 2028 points to a volume-up, margin-down outcome for commoditised parts **2024 Omdia Power Electronics Forecast**. Second, the ultra-wide-bandgap tier is over-narrated relative to its evidence; the honest reading of the Ga2O3 and c-BN literature here is early-stage materials work with an unsolved thermal problem, not a near-term successor to SiC and GaN. The investable claim is the architecture shift and the GaN cost-parity crossover, not the exotic materials.

## Prediction

By 31 December 2028, at least one hyperscaler-operated datacentre white space will be running production 800V DC distribution built on GaN or SiC switches, while no commercially shipping datacentre power rack or solid-state transformer will use Ga2O3 or cubic boron nitride power devices.

## Evidence base

- Total power electronics market forecast to grow from ~$45B in 2024 to ~$70B in 2030, with GaN at 25-30% CAGR and SiC around 30% but with earlier modelled oversupply **2024 Omdia Power Electronics Forecast** (2024-11-01).
- GaN power revenue projected from ~$0.5B in 2024 to ~$5B+ in 2030, cost parity with silicon MOSFETs in the 600V class by 2027, and hyperscaler design wins shifting from silicon to GaN through 2024-2025 **2024 Yole Power Gan 2024** (2024-09-15).
- Racks heading towards ~600kW make 48-54V distribution unworkable; ~39GW of incremental 800VDC capacity projected by 2030, power racks/sidecars peaking ~$11B around 2028 and SSTs at $13B-$32B by 2030, with DC arc-flash, busway, NEC and UL standards the real bottleneck <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup> (2026-05-26).
- Vertical GaN-on-Si demonstrated with a 0.5nm silicide template formed by rapid thermal annealing, giving ohmic low-resistance vertical conduction across 25 metallic species and supporting MOCVD overgrowth (2026-05-04).
- LPCVD Sn-doped (010) beta-Ga2O3 achieved carrier concentrations of 1.17e17 to 3.06e18 cm-3 with Hall mobilities of 113 down to 63 cm2/Vs and films 1.66-11.3 microns thick at 6.4-16.6 microns per hour (2026-08-11).
- First vertical Ga2O3 architecture without planarization etch-back or mid-gap acceptor regions showed enhancement-mode operation at 2V threshold and on-off ratio above 1e7 using 200nm fins and ~1.2 micron trenches (2026-08-14).
- Bit2Watt demonstrated that a legitimate cloud tenant manipulating GPU workloads can induce high-frequency power modulation that degrades damping and destabilises power-electronic-dominated local grids, poorly captured by routine telemetry (2026-07-08).

## Open questions

- Do the DC arc-flash, busway, NEC and UL standards land in time for the 2026-2028 power-rack phase, given that these and not components are named as the bottleneck <sup class="ref"><a href="https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part" title="Inside the 800VDC Revolution – Part 1" rel="noopener">ref</a></sup>?
- Does GaN actually cross silicon device cost in the 600V class in 2027, and does the crossover hold once Chinese silicon capacity reaches 50%+ of unit volume by 2028 **2024 Yole Power Gan 2024** **2024 Omdia Power Electronics Forecast**?
- Can interfacial thermal boundary conductance at Ga2O3/SiC be raised enough experimentally, not just in simulation, to make ultra-wide-bandgap power devices thermally viable?
- Does the sputtered silicide template for vertical GaN-on-Si reproduce at production wafer scale and yield, or remain a laboratory epitaxy result?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
