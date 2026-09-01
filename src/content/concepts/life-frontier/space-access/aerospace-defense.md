---
type: concept
slug: aerospace-defense
context_concept: true
canonical_name: Aerospace & Defense
aliases: []
kind: market
parent_concepts:
- life-frontier
- space-access
related_concepts: []
sources: []
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: null
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 80
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-31-what-happened-this-month-at-the-european-space-agency-august
  title: What happened this month at the European Space Agency? (August 2026)
  date: '2026-08-31'
  kind: web
- slug: 2026-08-28-nasa-awards-first-prize-in-phase-2-of-agencys-lunarecycle-ch
  title: NASA Awards First Prize in Phase 2 of Agency’s LunaRecycle Challenge
  date: '2026-08-28'
  kind: web
- slug: 2026-08-27-first-contracts-kick-off-european-launcher-challenge
  title: First contracts kick off European Launcher Challenge
  date: '2026-08-27'
  kind: web
- slug: 2026-08-12-nasa-data-helps-commercial-space-plan-living-off-our-moon
  title: NASA Data Helps Commercial Space Plan Living Off Our Moon
  date: '2026-08-12'
  kind: web
- slug: 2026-08-11-building-the-moon-base-nasa-stories-at-the-ion
  title: 'Building the Moon Base: NASA Stories at the Ion'
  date: '2026-08-11'
  kind: web
- slug: 2026-08-11-nasa-completes-astronaut-deployed-science-instrument-for-lun
  title: NASA Completes Astronaut-Deployed Science Instrument for Lunar Surface
  date: '2026-08-11'
  kind: web
- slug: 2026-08-07-nasas-lunar-development-and-test-facility-prepares-artemis-h
  title: NASA’s Lunar Development and Test Facility Prepares Artemis Hardware for Moon
  date: '2026-08-07'
  kind: web
- slug: 2026-08-07-iris2-reinforced-and-accelerated-as-implementation-advances
  title: IRIS² reinforced and accelerated as implementation advances
  date: '2026-08-07'
  kind: web
neighbors: []
---
**A cluster of subsystem research, spanning radiation- and heat-tolerant components, low-SWaP onboard computing and signal processing, distributed satellite sensing and autonomy assurance, that together defines how far aerospace and defence platforms are shifting from single large assets to many small, hardened, partly autonomous ones.**

## Summary

"Aerospace and defence" as represented in these sources is not one technology but the engineering base underneath space access and contested-environment systems. Three strands recur. First, materials and components that survive environments no commercial part is designed for: an aluminium nitride ultra-wide-bandgap photodetector that stays linear under blue light above 40 W/cm² and at temperatures to at least 300 °C; ultrafine-grained AA6061 whose deployment depends on resisting recrystallisation near the ~200 °C that aluminium components can reach in low Earth orbit under solar irradiation; cobalt-free CrMnFeNi high-entropy alloys aimed at radiation-tolerant structures; and variable-emissivity coatings intended to replace mechanical louvers on lunar habitats, where moving parts must survive dust contamination.

Second, doing more computation and sensing per watt and per kilogram. FPGAs are the focus for onboard neural inference because of flexibility, cost and radiation-tolerance potential. A lightweight classifier for onboard Earth observation reaches over 94% on EuroSAT and over 98% on PatternNet against 99% for MobileViT, but with 33x fewer parameters, 27x fewer FLOPs, roughly 6x lower power and about 3x faster inference, and runs at 852.30 mW on neuromorphic hardware. On the RF side, sparse digital pre-distortion cuts complexity by 2.77x with near-identical linearisation, addressing the same size, weight and power ceiling. Photonic integrated circuits are proposed to replace a telescope's large aperture with an array of small apertures combined interferometrically, precisely because weight and size dominate space mission design.

Third, the consequences of distribution: what many cheap platforms buy you, and what they cost you in trust. Using three months of Level 1 data from seven CYGNSS spacecraft, a full constellation cut median radio-frequency-interference detection latency by 4.7x versus one satellite, raised interception probability for a five-minute emission from 2% to 11.5%, and improved median footprint revisit from 5.8 hours to under 2.0 hours, with three satellites identified as the minimum effective number. Against that, orbit-based authentication of LEO satellites was shown to fail against attackers controlling multiple devices, with false positive rates up to 40%, and LLM-assisted ISR swarms can compose individually-compliant actions into mission-level policy violations that per-platform guardrails miss by construction.

The parameters that decide the field, as these sources frame it, are: performance per watt and per kilogram under fixed SWaP budgets; survivability against a named environment (radiation, atomic oxygen, thermal cycling, dust); the number of platforms needed before a distributed architecture beats a monolithic one; and whether autonomy and authentication can be verified rather than asserted.

## Viability (3/5)

The hardware claims are measured, not projected. The AlN detector shows non-saturating linear response above 40 W/cm² and undistorted linearity to at least 300 °C, with the mechanism attributed to deep-level-mediated photoresponse at a metal-AlN Schottky junction and a narrow space charge region. Ambient-pressure bilayer actuators were built, modelled, characterised for actuating force and assembled into deployable devices. A gravimeter collimator achieved 105 and 122 microradian divergence on a 16 mm beam under ISO11146-compliant measurement. Modulator half-wave voltage measurement methods were demonstrated experimentally from 100 MHz to 40 GHz by an industrial group.

The qualification gap is the limiting factor. The one result grounded in flight data is the CYGNSS analysis, and that reuses an existing NASA constellation rather than demonstrating new hardware. Atomic-oxygen durability, thermal stability and radiation tolerance are treated as open questions inside these same papers: CFRP zenith panels are predicted to erode 15.1 to 16.2 µm per year at 350 km despite receiving far lower fluence than ram-facing surfaces, and UFG aluminium deployment is explicitly described as contingent on thermal stability. Working on a bench is not the same as surviving a year in orbit, and the sources say so.

**TLDR: Bench and simulation results are real and quantified, but almost nothing here is shown flight-qualified.**

## Drivers (3/5)

On demand, the sources are consistent about what is pulling: missions described as increasingly ambitious require high-performance onboard computing; LEO satellites are drawing attention as PNT signal sources beyond conventional GNSS; lunar habitats are framed as the first platforms for long-term human presence beyond low Earth orbit and must handle extreme thermal swing; and ISR swarms in contested environments are described as increasingly proposed. Terrestrial GNSS interference is treated as a monitoring problem worth constellation-scale investment. Very low Earth orbit, with its distinct atomic-oxygen problem, is being modelled as a design regime rather than a curiosity.

On supply, the enabling inputs are largely borrowed: FPGAs valued for flexibility and cost-effectiveness, neuromorphic parts such as Akida running inference at 852.30 mW, and photonic integrated circuits arriving from telecom into imaging. What the sources do not contain is any budget, contract, launch-rate or market figure, so the strength of the pull cannot be sized from this evidence, only its direction.

**TLDR: Demand is stated clearly by the papers themselves; supply is commodity compute and photonics, but no funding or procurement data is present.**

## Novelty (3/5)

Where a baseline is named, the margin is stated. Least Squares Thresholding gives a 2.77x complexity reduction against Orthogonal Matching Pursuit at near-identical linearisation. ResNet-GLUSE trades one to five accuracy points against MobileViT for 33x fewer parameters, 27x fewer FLOPs and roughly 6x lower power. Seven CYGNSS satellites beat one by 4.7x on median detection latency and turn a 2% interception probability into 11.5%. Chi-MERA is positioned against prior orbit-based authentication schemes that produce false positive rates up to 40% under multi-device attack. These are engineering wins of the kind that shift a design point, not ones that create a new capability class.

The more architectural claims are less proven. Replacing a monolithic aperture with a PIC-combined array is a genuine break with conventional telescope design, but the source analyses signal-to-noise against a monolithic telescope at equal photon count rather than demonstrating an instrument. Variable-emissivity solid-state surfaces are novel against white paint, multi-layer insulation and mechanical louvers, and specifically against the dust-contamination failure mode of moving parts. Ambient-pressure bilayer actuators are notable for needing no separate power source or pump, but the paper describes their application space rather than a flown deployment.

**TLDR: Real, quantified multiples over named baselines, mostly within existing architectures rather than replacing them.**

## Diffusion (2/5)

The barriers appear inside the papers rather than needing to be inferred. Environmental qualification: atomic oxygen exposure varies by roughly an order of magnitude across a single spacecraft geometry, and material-specific erosion yields reorder the component risk ranking, meaning orbit-averaged fluence is not a usable acceptance criterion. Thermal qualification: LEO aluminium components sit close to the recrystallisation onset of severely deformed alloys, and conventional in situ TEM measurement of that onset is compromised by thin-film effects and small sampling volumes. Mechanism qualification: louvers and shutters work but depend on dust resilience.

For the software and autonomy strand the barrier is trust rather than physics. Established LEO authentication fails against multi-device attackers at up to 40% false positive rate, and swarm assurance failures are shown to be compositional, so per-platform guardrails cannot catch a prohibited objective split across platforms, with contested communications letting violations hide behind lost or delayed evidence. The counter-example is that a distributed sensing capability can be extracted from an already-flying constellation using archived Level 1 data, which is the fastest available adoption path: new processing on existing assets.

**TLDR: One flight-data result, everything else at bench or simulation, with qualification and assurance as the named barriers.**

## Impact (unscored)

Every source here is a technical preprint reporting device, algorithm or simulation performance. None contains a market size, programme budget, cost per kilogram, mission cost avoided, or any other figure from which economic or strategic value could be estimated. The closest to a value statement is the qualitative framing that ultra-wide-bandgap devices meet emerging needs in industrial process control, thermal and nuclear power generation, and aeronautics and spaceflight, which names sectors without sizing them.

What can be said is directional and should not be dressed up as a score. Capabilities addressed include detecting terrestrial GNSS jamming from orbit with a three-satellite minimum, positioning from a single LEO satellite despite severe cross-track error, and surviving lunar night without continuous internal heating. These are consequential problems. Their solution value is not quantified anywhere in this evidence base, so no score is given.

**TLDR: The sources do not support an assessment of how much value these results create.**

## Timing Soon (2-5yr)

The near end is already reachable. Sparse digital pre-distortion runs on satcom payload processors as a software change, data-aided channel and Doppler estimation for mMIMO LEO links is an algorithmic upgrade, and constellation-scale RFI detection has been evaluated on three months of archived data from seven flying spacecraft. Efficient onboard classifiers targeting FPGA and neuromorphic parts are at benchmark maturity with power and latency numbers attached, and the FPGA accelerator literature is mature enough to be surveyed for trends and gaps.

The far end is set by qualification cycles and by mission schedules that these sources do not date. Variable-emissivity lunar habitat surfaces depend on habitats that do not yet exist; PIC interferometric imagers are at concept analysis; radiation-tolerant Co-free high-entropy alloys are at the tensile-test and molecular-dynamics stage; and mission-level runtime assurance for LLM swarms is a framework proposal responding to failures that have already been demonstrated. Treat the band as covering the software and processing layer, with the materials and autonomy layers trailing.

**TLDR: Signal processing and onboard inference are close to fielding on existing platforms; hardened materials, PIC imagers and assured swarm autonomy are further out.**

## Overrated or underrated? Fairly rated

The honest read of this evidence is that the durable progress in aerospace and defence right now is unglamorous: components that stay linear at 300 °C, geometry-resolved erosion models that reorder which panel fails first, and processing that does the same job for a third of the power. None of that is oversold in these sources, and none of it is trivial. The distributed-sensing case is the strongest single result here because it is grounded in real flight data and yields a clean design rule: three satellites is the minimum effective constellation, with the largest gains between one and three.

Where expectations should be trimmed is autonomy. Two independent sources show that the trust layer for distributed systems is currently broken rather than merely immature: existing orbit-based authentication produces up to 40% false positives against a multi-device attacker, and LLM-assisted swarms fail at the mission level in ways that no per-platform guardrail can detect. Both papers propose fixes and both evaluate in simulation. Anyone pricing autonomous swarm ISR as near-term should read those two results as the schedule constraint. As a sector, fairly rated; as a bet on onboard autonomy specifically, ahead of its assurance evidence.

## Prediction

By 31 December 2028, at least one operational Earth-observation or GNSS-reflectometry constellation will publish flight results reporting neural-network inference executed onboard on FPGA or neuromorphic hardware at under 1 W, consistent with the 852.30 mW figure benchmarked on Akida.

## Evidence base

- 15 June 2026: seven-satellite CYGNSS constellation cut median RFI detection latency 4.7x versus a single satellite, raised five-minute-emission interception probability from 2% to 11.5%, improved median revisit from 5.8 hours to under 2.0 hours, and confirmed interference onset 39 days earlier; three satellites identified as the minimum effective constellation 
- 15 June 2026: sub-bandgap AlN photodetectors showed non-saturating linear response to blue light above 40 W/cm² and undistorted linearity to at least 300 °C, via deep-level photoresponse at a metal-AlN Schottky junction 
- 23 July 2026: ResNet-GLUSE exceeded 94% on EuroSAT and 98% on PatternNet against MobileViT's 99%, with 33x fewer parameters, 27x fewer FLOPs, roughly 6x lower power and 852.30 mW inference on Akida neuromorphic hardware 
- 22 July 2026: established orbit-based LEO satellite authentication schemes produced false positive rates up to 40% against attackers controlling multiple devices; the proposed Chi-MERA scheme uses multilateration and a reference-receiver-free signature to recover low FPR in simulation 
- 29 July 2026: one-year simulation of a 350 km Sun-synchronous orbit gave ram-facing atomic oxygen fluence of 6.9 to 7.5 x 10^21 atoms/cm², with side and zenith surfaces at 3 to 5% of that, yet a CFRP zenith panel predicted to erode 15.1 to 16.2 µm per year; a wedge geometry created about an order of magnitude spatial variation 
- 16 June 2026: Least Squares Thresholding for satellite power amplifier digital pre-distortion achieved a 2.77x complexity reduction against Orthogonal Matching Pursuit with near-identical linearisation, under strict SWaP constraints 
- 28 July 2026: mission-level assurance failures in LLM-assisted ISR swarms were shown to arise across platforms rather than within them, so per-platform guardrails miss prohibited objectives split across agents 

## Open questions

- Does the AlN photodetector's deep-level-mediated linearity survive radiation exposure and thermal cycling over mission-length durations, or only the 300 °C static condition demonstrated?
- Do the CYGNSS-derived constellation scaling results, including the three-satellite minimum and 4.7x latency gain, hold for deliberately evasive or short-burst emitters rather than the observed interference population?
- Can compositional runtime verification for LLM swarms be shown to catch mission-level violations on real contested links, given that the framework's guarantees depend on evidence loss and silence being observable?
- Does ultrafine-grained AA6061 retain its grain structure through the ~200 °C solar-irradiation condition in orbit, and does the in situ EBSD-derived recrystallisation onset match bulk behaviour in flight hardware?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
