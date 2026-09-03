---
type: concept
slug: ambient-energy-harvesting
canonical_name: Ambient energy harvesting
aliases:
- ambient power
- energy harvesting
- battery-free electronics
parent_concepts:
- generation
- energy-power
related_concepts:
- edge-compute
sources:
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-2026-european-next-gen-pv-cohort]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
frontier:
- Does the Fe2VAl module deliver competitive conversion efficiency and cost per watt in a real waste-heat application, or does the average zT of about 0.3 confine it to demonstration status 2026 06 16 high entropy fe2val based thermoelectric modules with improv?
- Can InAs or Weyl-semimetal thermoradiative devices close the two-orders-of-magnitude gap between measured reverse saturation current and the radiative limit, and if so at what device area and cost 2026 05 06 initial development of mbe grown inas diodes for thermoradia 2026 06 16 designing strong and broadband nonreciprocal thermal radiati?
- Does Dracula's stated 600M cm2/yr capacity translate into shipped volume and a cost per cm2 that undercuts a coin cell over the sensor's service life 2025 2026 european next gen pv cohort?
- Will unified SWIPT receivers that rectify power and demodulate information in the same analogue hardware reach a power budget compatible with a 452 nA quiescent node, or does the harvesting-plus-decoding overhead cancel the gain 2026 07 27 nsf 2616563 cif unified swipt emerging models and de 2026 06 16 a hardware based multi stage dynamic power management archit?
- 'Theme work-up ran 16 Jul 2026 and landed as energy harvesting no wedge: sub-venture market, incumbent-owned silicon socket, dated ambient-IoT re-open trigger. This concept page tracks the technology; the verdict lives there.'
- What does Casimir (the Q2 2026 'Ambient Power' fundraise) actually build? Unverified from the table alone.
last_updated: '2026-08-31'
tags:
- concept
- stub
mention_count: 33
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2025-2026-european-next-gen-pv-cohort
  title: European next-gen PV cohort 2025-2026, Dracula, SunXT/Solertix, Perovion, HyET Solaris, Sofab Inks, Coatema
  date: '2026-06-01'
  kind: web
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
neighbors:
- slug: edge-compute
  name: Edge Compute
  path: /compute/ai-edge/edge-compute/
  macro: compute
---
**Ambient energy harvesting is the extraction of microwatt-to-milliwatt electrical power from light, heat, vibration and radio waves already present in an environment, and its practical role is not grid generation but the elimination of batteries from very large numbers of sensors.**

## Summary

Ambient energy harvesting covers a family of transducers that convert whatever energy flux happens to be crossing a device into usable electricity: indoor light via organic or perovskite photovoltaics, temperature differences via thermoelectric or pyroelectric materials, mechanical vibration via piezoelectric elements, and incident radio waves via rectifying antennas. The physics differs entirely between branches, but the engineering problem is common: the available flux is small and intermittent, so the harvester, the storage element and the load must be co-designed around a power budget measured in microwatts.

Further out sit mechanisms that are still physics rather than engineering. Thermoradiative diodes, which generate power by emitting infrared into a cold sky, are at the point where 1x1 mm2 MBE-grown InAs devices show breakdown above 0.3 V but reverse saturation current densities 200 times the radiative limit. Magnet-free nonreciprocal thermal emitters based on magnetic Weyl semimetals such as Co3Sn2S2 are predicted from first principles to outperform InAs, a near-field photon Nernst effect has been proposed with efficiency bounded by Carnot, and an in-plane anomalous Nernst effect has been observed in ultrathin ferromagnetic oxide films, removing the orthogonality constraint on device geometry.

The decisive parameters are not the transducer figures of merit alone. They are power density per unit area or volume under realistic ambient conditions, the quiescent draw of the electronics being powered, and cost per cm2 at volume. A hardware-orchestrated power management architecture that cuts quiescent drain to 452 nA by fully power-gating the microcontroller illustrates the point: in low-light conditions the sleep current, not the harvester, sets autonomy.

## Viability (3/5)

Treated as a single concept, viability is genuinely mixed and the sources show it clearly. Printed indoor photovoltaics has products, funded factories and stated capacity targets **2025 2026 European Next Gen Pv Cohort**. Thermoelectrics have a full fabricated module from scaled-up material batches with properties matching laboratory samples, which is the reproducibility test that usually kills thermoelectric claims. Pyroelectric harvesting has a working multilayer device with a quantified 5.5% conversion efficiency and leakage suppressed by over two orders of magnitude at the optimal Sr0.19 composition. RF harvesting has been demonstrated end to end on real hardware with measured gains.

Against that, the newer mechanisms are at or before first-device stage. InAs thermoradiative diodes with reverse saturation currents 200 times the radiative limit are two orders of magnitude away from where the physics says useful power extraction begins. The nonreciprocal Weyl emitters, the photon Nernst effect and the shift-current material screening are computational predictions, not measured devices. A 3 reflects the average: the concept works at low power in commercial niches, and the routes to higher power remain unproven.

**TLDR: One branch is shipping, several are at credible module demonstrations, and the exotic thermal-radiative mechanisms are pre-device.**

## Drivers (4/5)

On the demand side the pull is specific and repeatedly stated: sensor nodes that cannot practically be maintained. The self-powered smart tire case is the clearest articulation, with tyre-embedded sensors on millions of vehicles at four tyres each, where battery depletion drives periodic replacement and substantial electronic waste. RF work is framed around billions of connected objects monitoring structural health, logistics, security, healthcare and agriculture. Wearables, soft robotics and IoT are cited as the pull for biomechanical piezoelectric harvesters.

**TLDR: Demand is driven by battery maintenance and e-waste in dense sensor deployments; supply is being funded by both public agencies and private capital.**

## Novelty (3/5)

The comparator for ambient harvesting is a primary battery with a finite service life, or mains wiring. Against a battery, the claim is elimination of replacement visits rather than higher performance, and the tyre project frames its ambition as extending battery life and potentially eliminating replacement, not as beating it on power. Within the field, several results are genuinely new mechanisms rather than tuning. Atomic chirality engineering changes piezoelectric response at identical chemical composition, with right-handed D-Se nanowires reaching a higher effective coefficient than their enantiomers, which is a new degree of freedom beyond composition, defect, strain and orientation control. Removing the orthogonality constraint on the anomalous Nernst effect changes what device geometries are possible. Magnet-free nonreciprocal emission removes the external magnet from thermal-radiative devices.

Quantified margins are more modest. Average zT of about 0.3 over 300-500 K in a cheap, non-toxic Fe2VAl system is competitive on cost and scalability rather than on efficiency. Pyroelectric conversion at 5.5% resolves an open question about first-order versus second-order transformations by finding an optimal transitional composition, which is a real design insight, but the absolute energy density of 1.6 mJ/cm3 per cycle remains small. The 12 dB harvesting gain from channel-aware beamforming is a system-level rather than device-level improvement. High-throughput screening of over 154,000 materials down to 32 with shift current above 100 µA/V2 and a maximum of 616 µA/V2 expands the candidate pool without yet delivering a device.

**TLDR: The alternative is a coin cell or a wire, and the recent gains are real but incremental within each mechanism.**

## Diffusion (3/5)

The clearest barrier in the sources is system-level rather than transducer-level. Conventional software-managed low-power states impose a persistent quiescent drain that becomes the dominant energy sink in energy-scarce conditions, which is why a hardware-orchestrated architecture achieving 452 nA total quiescent drain by fully power-gating the microcontroller and non-essential peripherals was needed to make photovoltaic-powered nodes autonomous in low light. This means every adopter must redesign the load, not just bolt on a harvester. RF harvesting faces a related integration barrier: prior architectures assume separate receivers for energy harvesting and information decoding, and unified low-power analogue front ends that do both are still a research objective.

The second barrier is manufacturing cost and area. The photovoltaic branch is the furthest along precisely because roll-to-roll printing gives a credible cost per cm2 path, with Dracula quadrupling to 600M cm2/yr and Coatema supplying roll-to-roll lines for organic, perovskite and DSSC processes **2025 2026 European Next Gen Pv Cohort**. Thermoelectrics are being steered toward low-cost, non-toxic, scalable compositions for the same reason, and piezoelectric work is being pushed toward lead-free oxides partly for compliance reasons. Environmental variability is a third barrier: harvesters designed for a nominal flux must tolerate stochastic real-world inputs, which is why the tyre work relies on stochastic resonance and bistable nonlinear dynamics rather than a tuned linear resonator.

**TLDR: Adoption is gated less by the harvester than by the power budget of everything attached to it, plus cost per unit area.**

## Impact (3/5)

The value case in the sources is displacement of batteries and the maintenance and waste they generate, quantified only qualitatively: millions of US vehicles with four tyres each generating substantial electronic waste from periodic battery replacement, and billions of envisioned connected objects across infrastructure, logistics, healthcare and agriculture whose deployment economics depend on not being wired or serviced. If harvesting reliably supports those loads, it unlocks sensing deployments that are otherwise uneconomic, which is a large second-order impact even though the power itself is trivial.

What the sources do not support is any claim about ambient harvesting contributing to energy supply. Reported device outputs are microamps and millijoules per cubic centimetre per cycle, and the most advanced thermoelectric modules sit at average zT around 0.3. Waste-heat recovery and radiative cooling harvesting are named as motivations for the low-grade heat and thermoradiative work, but no source quantifies recoverable energy at system or grid scale. The score reflects high value in the sensing niche and no demonstrated value beyond it.

**TLDR: Substantial value in enabling maintenance-free sensing at scale; the sources give no basis for impact on energy supply.**

## Timing Now (0-2yr)

For the photovoltaic branch the timing question is already settled: Dracula was founded in 2012, showed LAYER V2.0 at CES 2026 with a claimed 30% performance gain, and is scaling roll-to-roll capacity now, while HyET Solaris plans test production of flexible perovskite in mid-2026 and commercial output at end-2027 **2025 2026 European Next Gen Pv Cohort**. RF and backscatter harvesting has a real-time testbed operating with under 2 ms of airtime per excitation cycle, which is compatible with deployment timescales rather than research timescales. Thermoelectric and pyroelectric devices sit in the two to five year band, with module fabrication and reproducibility already demonstrated but efficiency and cost still under optimisation.

The thermal-radiative and magnetothermoelectric branches are much later. InAs thermoradiative diodes are described as initial development, with reverse saturation currents 200 times the radiative limit; the magnet-free nonreciprocal emitters and the near-field photon Nernst effect exist as first-principles predictions. The NSF awards funding the mechanistic work are early-career and initiation grants dated 2026, so their outputs land at the end of the decade at the earliest.

**TLDR: Indoor photovoltaic and RF harvesting are shipping or testbed-ready today; the thermal-radiative mechanisms are a decade or more behind.**

## Overrated or underrated? Fairly rated

Ambient energy harvesting is correctly valued if you judge it as a battery-elimination technology and overvalued if you judge it as generation, which is how the taxonomy files it. The evidence supports the first framing strongly: a funded, scaling manufacturing base for indoor photovoltaics **2025 2026 European Next Gen Pv Cohort**, measured system-level harvesting gains of 12 dB from channel-aware RF beamforming, a reproducible thermoelectric module from scaled-up batches, and a demonstrated 452 nA quiescent node architecture that makes microwatt harvest budgets actually usable. Nothing in the sources supports the second framing.

The useful discipline for an investor or engineer is to stop reading the field as one thing. The commercial value is concentrated in printed indoor photovoltaics and RF/backscatter, where the manufacturing and system integration problems are being solved. The physics interest is concentrated in thermoradiative, nonreciprocal and Nernst-effect devices, where the recent results are predictions and first diodes and where a 200-fold gap to the radiative limit stands between the current state and a useful device. Chirality-controlled piezoelectricity is the most genuinely novel mechanistic result here and the one worth watching, because it adds a design variable rather than tuning an existing one.

## Prediction

By 31 December 2029, no thermoradiative, photon-Nernst or nonreciprocal-thermal-emitter energy harvester will be commercially shipping, and commercial ambient harvesting will still be dominated by printed indoor photovoltaic modules and RF/backscatter devices.

## Evidence base

## Open questions

- Does the Fe2VAl module deliver competitive conversion efficiency and cost per watt in a real waste-heat application, or does the average zT of about 0.3 confine it to demonstration status?
- Can InAs or Weyl-semimetal thermoradiative devices close the two-orders-of-magnitude gap between measured reverse saturation current and the radiative limit, and if so at what device area and cost?
- Does Dracula's stated 600M cm2/yr capacity translate into shipped volume and a cost per cm2 that undercuts a coin cell over the sensor's service life **2025 2026 European Next Gen Pv Cohort**?
- Will unified SWIPT receivers that rectify power and demodulate information in the same analogue hardware reach a power budget compatible with a 452 nA quiescent node, or does the harvesting-plus-decoding overhead cancel the gain?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
