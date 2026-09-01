---
type: concept
slug: communications
canonical_name: Communications
aliases: []
kind: technology
parent_concepts:
- communications
- fibre-and-free-space
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2025-09-02-13-drop-in-employment-for-young-workers]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: null
  timing_band: Soon (2-5yr)
  verdict: Too early to say
scorecard_status: draft
descendants:
- 5g-nr-advanced
- beamforming-ics
- communications
- communications-equipment
- dark-fibre-submarine-cables
- datacenter-network-stack
- dect-nr
- diffractive-deep-neural-network
- digital-rf
- fiber-connectors
- fiber-optics
- fibre-and-free-space
- free-space-optics
- free-space-photonics
- gan-rf
- iot-connected-devices
- lpo-linear-pluggable-optics
- mmwave
- networking-wireless
- optical-circuit-switching
- optical-interconnect
- optical-io-chip-level
- optical-packet-switching
- phased-array-antennas
- phased-array-beamforming
- pll
- pluggable-transceivers
- qkd
- qrng
- quantum-comms
- quantum-communications
- quantum-key-distribution
- quantum-networks
- quantum-random-number-generation
- quantum-repeaters
- rack-scale-interconnect
- rf-frontend
- rf-over-dielectric-waveguide
- rf-power
- rf-wireless
- rfic
- serdes
- software-defined-radio
- sub-thz-6g
- timing-clock-generation
- timing-synchronization
- ultra-low-power-rf
- wireless
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-27-opener-is-an-open-source-reference-implementation-of-the-dec
  title: Opener is an open-source reference implementation of the DECT NR+ massive IoT, low-latency standard - CNX Software
  date: '2026-08-27'
  kind: web
- slug: 2026-08-05-spooky-particles-transit-dc-suburbs-a-step-toward-a-quantum-
  title: ‘Spooky’ Particles Transit DC Suburbs, a Step Toward a Quantum Network
  date: '2026-08-05'
  kind: web
- slug: 2026-07-24-nasa-announces-new-spacecraft-technology-demonstration-missi
  title: NASA Announces New Spacecraft Technology Demonstration Mission at Moon
  date: '2026-07-24'
  kind: web
- slug: 2026-07-09-non-cellular-5g-networks-simplified---hacksterio
  title: Non-Cellular 5G Networks Simplified - Hackster.io
  date: '2026-07-09'
  kind: web
- slug: 2026-06-12-hku-sic-cryogenic-neuromorphic-chip-10mk
  title: HKU world-first cryogenic neuromorphic chip at 10 mK (silicon carbide, impact-ionisation spiking)
  date: '2026-06-12'
  kind: web
- slug: 2026-06-05-nasa-concludes-antenna-mishap-investigation-releases-report
  title: NASA Concludes Antenna Mishap Investigation, Releases Report
  date: '2026-06-05'
  kind: web
- slug: 2026-06-01-ncsc-nsa-qkd-vs-pqc
  title: 'NCSC / NSA position: QKD not endorsed, post-quantum cryptography is the recommended mitigation'
  date: '2026-06-01'
  kind: web
- slug: 2026-06-01-nibras-ucl-chipstart
  title: UCL EEE ventures selected for national ChipStart programme (incl. Nibras Communications)
  date: '2026-06-01'
  kind: web
neighbors: []
---
**"Communications" here is the research frontier of moving bits over fibre, free space and radio: the supplied evidence shows a field whose centre of gravity has shifted from raw capacity to controlling the channel itself, fusing sensing with transmission, and replacing hand-designed physical-layer maths with learned models.**

## Summary

Communications, as populated by the sources supplied, is the layer of technology that gets information from one place to another over a physical medium: guided light in fibre and integrated photonics, unguided light through the atmosphere, and radio. The taxonomy places this under "fibre-and-free-space", but the evidence base is dominated by radio-frequency wireless research, with only two items touching photonic or free-space optical hardware directly. Any assessment below is therefore weighted towards the RF and physical-layer-algorithm end of the field.

Four distinct threads run through the material. First, treating the propagation channel as a controllable object rather than a given: reconfigurable intelligent surfaces, fluid antennas that reposition, pinching antennas that move the radiation point along a waveguide, and a proposal to do the same job purely in the frequency domain by sliding a signal's spectrum along the frequency axis to avoid reconfigurable hardware entirely. Second, integrated sensing and communications (ISAC), where the same waveform and hardware both carry data and act as radar; this is being positioned as a 6G feature, with work spanning information-theoretic limits, industrial testbeds and multi-static localisation. Third, an AI-native physical layer: foundation models trained on channel-state information, diffusion models that reconstruct meaning rather than bits, learned codes for secrecy, and Bayesian estimators for near-field arrays. Fourth, quantum and photonic hardware: entanglement multiplexing schemes for repeaters, satellite quantum links, and integrated modulators pushing into the ultraviolet.

The parameters that decide each thread differ. For channel-shaping and ISAC it is whether the gain over a well-tuned conventional baseline survives real hardware, real clutter and real signalling overhead, and whether the extra components can be built cheaply enough to deploy at macro-network scale. For the AI physical layer it is generalisation: whether one model works across configurations and sites without per-cell retraining, and whether inference fits the latency and power budget of a baseband unit. For photonic modulators it is the product of drive voltage and length against bandwidth, insertion loss and extinction ratio. For quantum links it is loss, pointing accuracy and synchronisation across a turbulent atmosphere. The sources give hard numbers on some of these and none at all on cost, volume or deployment.

## Viability (3/5)

Two results in the supplied set are genuinely measured hardware. A thin-film lithium tantalate ultraviolet electro-optic modulator was reported with a VπL of 85 mV·cm at 375 nm, an extinction ratio of 22.7 dB, insertion loss of 1.3 dB and Vπ of 4.2 V. A millimetre-wave ISAC proof-of-concept detected moving targets behind occlusions by using reflections off a large surface, validated at the ARENA2036 industrial research campus, and held up against synthetically injected false peaks. The WiFo-2 channel foundation model is also backed by a functional hardware prototype rather than simulation alone. On the quantum side, compatibility of time-bin pulses with spectral shearing was verified experimentally, with no appreciable phase shift when the same shearing is applied to both time bins.

Against that, most of the set is numerical: outage-probability analysis for hybrid pinching-fluid antennas, simulated backscatter index modulation on RIS-based radars, regression on ray-traced channel data, and a converse bound on the sensing-constrained diversity-multiplexing tradeoff. A 3 reflects that: the physics is not in doubt, individual demonstrations are real, but the field-level claim that these techniques work in deployed networks is not evidenced here.

**TLDR: A handful of measured devices and testbeds; the majority of the frontier is still simulation.**

## Drivers (3/5)

The supply side is visible directly in the evidence. A single week of preprints covers channel shaping, ISAC, semantic communications, physical-layer security, near-field estimation, antenna arrays and quantum links, which indicates a large and well-funded research base. Data availability is scaling with it: WiFo-2 was pretrained on 11.6 billion channel-state-information points and reports scaling-law behaviour, meaning the field now has corpora large enough to support foundation-model methods. Ray-tracing pipelines are being used to synthesise training data where measurement is impractical.

Demand is stated, not shown. The stated pulls are that wireless systems are approaching theoretical capacity limits, pushing interest towards meaning-centric rather than bit-accurate transmission; that 6G applications such as extended reality and massive digital twins need low-latency ISAC; that antenna counts are growing to the point where users fall inside the near field and the planar-wave assumption breaks; and that tactical and disaster-response users need lightweight secure links where infrastructure is absent. None of these is quantified with operator spend, traffic growth or procurement data in the sources, so the score stops at 3.

**TLDR: Strong and well-documented supply-side push; demand is asserted by authors rather than measured in these sources.**

## Novelty (3/5)

Where the sources do state what they are better than and by how much, the margins are large. The ultraviolet modulator claims up to four orders of magnitude improvement in bandwidth per VπL over bulk crystal technologies, which is the strongest single quantified advance in the set and is measured on a device. WiFo-2 reports zero-shot channel reconstruction that outperforms fully supervised task-specific models, and state-of-the-art results across nine wireless tasks using 1% of the training samples supervised models needed. Cooperative multi-static ISAC localisation cut root-mean-square error by nearly two orders of magnitude within six sensing iterations, reaching about 45 cm in cluttered industrial conditions.

Other novelty claims are narrower or comparative against modest baselines: movable signals achieve higher average received power than quantised equal gain transmission; a hybrid pinching-fluid antenna beats pinching-only or fluid-only systems in the authors' own channel model; linear regression beats support vector and decision-tree regression for channel prediction at 7 GHz, with MAE 7.5155×10⁻⁵, a result whose interest lies more in the simplicity of the winning model than in a step change. One conceptual novelty is worth flagging: on reversely-degraded secure channels the secrecy capacity is zero without feedback, so adding channel-output feedback changes what is possible rather than merely improving a rate. A 3 is right for the aggregate: real advances, unreplicated, baseline-relative.

**TLDR: Several specific, quantified beats over named baselines, but almost all from single groups and mostly in simulation.**

## Diffusion (2/5)

The clearest statement of the barrier comes from within the field: reconfigurable intelligent surfaces and flexible antennas rely on electronically reconfigurable or movable components, and that introduces implementation challenges which could hinder commercialisation, which is the stated reason for proposing a frequency-domain alternative instead. Quantum satellite communications has an even longer list: atmospheric loss, beam pointing and tracking, payload constraints, synchronisation, scalability and integration with terrestrial infrastructure, with daylight operation still a future direction.

For the AI physical layer the barrier is generalisation and integration rather than physics. Existing deep-learning approaches are trained for specific system settings with limited generalisability, which is exactly the problem a foundation model is meant to remove. The diffusion-based semantic communications literature is at the stage of needing its first comprehensive tutorial to connect techniques to system design, which is not the profile of a technology near deployment. Nothing in the set reports standardisation status, vendor commitment, field trials in live networks, or cost. The most deployment-adjacent items are a hardware prototype for WiFo-2 and a testbed ISAC demonstration. That supports a 2, not more.

**TLDR: The sources name the adoption blockers explicitly and offer almost no evidence of anything crossing into deployment.**

## Impact (unscored)

Every impact statement in the supplied material is an assertion of use case rather than a measure of value. ISAC is said to increase the value provided in future 6G networks and to enable intrusion detection in occluded areas; quantum satellite communications is described as strategic for secure global networking and long-distance quantum connectivity; integrated ultraviolet modulation is said to be pivotal for quantum information processing, portable atomic clocks and solar-blind secure communications. Useful signposts, but none is attached to a market size, a cost saving, a spectrum-efficiency figure at system level, or an energy figure.

The one quasi-quantitative impact statement is technical rather than economic: about 45 cm localisation error in cluttered industrial environments and a 1 to 1.5 km line-of-sight range for a wearable encrypted LoRa link. Those bound capability, not value. Scoring impact here would be inventing a number, so the score is null.

**TLDR: The sources do not support an assessment: no source quantifies economic or capability value.**

## Timing Soon (2-5yr)

The ISAC work is framed explicitly against future 6G cellular networks and already has an industrial testbed behind it, and the AI physical-layer work has moved from bespoke per-task models to a general model with a functional hardware prototype. Data-driven channel estimation is being positioned for deployment as a digital twin inside 5G and beyond networks, which is an incremental software insertion rather than new hardware. Those are the items that could plausibly reach products within a 6G cycle.

The rest is slower. Reconfigurable surfaces and movable or fluid antennas still have unresolved implementation and commercialisation problems by their proponents' own account. Quantum satellite communications remains a research programme with daylight operation, satellite-supported repeaters and terrestrial integration listed as future directions rather than achieved capability, and entanglement multiplexing for repeaters is at the stage of verifying component compatibility. The ultraviolet modulator is a first-of-kind device, so a commercial timescale cannot be read from the source.

**TLDR: The AI physical layer and ISAC are on a 6G standardisation timescale; quantum links and exotic antennas are further out.**

## Overrated or underrated? Too early to say

At the level of the concept as a whole, the supplied evidence is a snapshot of preprints from a single window, and it cannot settle whether the field is over- or under-rated. What it does show is a clear internal reordering: the assumption that gains come from more spectrum and more antennas is being replaced by three different bets, namely shaping the channel with new hardware, sharing the waveform between sensing and communication, and replacing hand-designed estimators and codes with learned models.

If forced to rank those bets on this evidence, the learned physical layer looks the strongest and the least discussed outside the field. A model pretrained on 11.6 billion CSI points that beats supervised task-specific models zero-shot, holds across nine tasks with 1% of the samples, shows scaling-law behaviour and runs on a hardware prototype is a different class of claim from a simulated outage-probability improvement. The channel-shaping hardware bet is the weakest, and its own advocates say so when they propose doing the job in the frequency domain specifically to avoid reconfigurable or movable components. Quantum satellite links remain a national-capability programme rather than a commercial technology on this evidence.

## Prediction

By 31 December 2028, at least one network equipment vendor will ship a baseband or radio product whose channel estimation is performed by a pretrained cross-configuration neural model of the WiFo-2 type, while no reconfigurable intelligent surface will be in commercial service in a macro cellular network at national scale.

## Evidence base

- 5 May 2026: WiFo-2, a space-time-frequency foundation model pretrained on 11.6 billion CSI points, reports zero-shot channel reconstruction beating fully supervised task-specific models, state-of-the-art results on nine wireless tasks with 1% of the supervised training samples, scaling-law behaviour, and a functional hardware prototype.
- 5 May 2026: first integrated ultraviolet electro-optic modulator on thin-film lithium tantalate, VπL of 85 mV·cm at 375 nm, up to four orders of magnitude improvement in bandwidth per VπL over bulk technologies, 22.7 dB extinction ratio, 1.3 dB insertion loss, Vπ of 4.2 V.
- 8 May 2026: cooperative multi-static ISAC localisation in cluttered industrial IoT settings reduced localisation RMSE by nearly two orders of magnitude within six sensing iterations, to about 45 cm.
- 4 May 2026: a millimetre-wave ISAC proof-of-concept detected moving targets in non-line-of-sight industrial clutter by exploiting reflections off a large surface, validated at the ARENA2036 campus and robust to synthetically generated false peaks.
- 4 May 2026: proponents of smart radio environments state that RIS and flexible antennas depend on electronically reconfigurable or movable components whose implementation challenges could hinder commercialisation, motivating a frequency-domain alternative based on movable signals.
- 5 May 2026: a review of quantum satellite communications lists atmospheric loss, beam pointing and tracking, payload constraints, synchronisation, scalability and terrestrial integration as unresolved barriers to large-scale deployment, with daylight operation and satellite-supported repeaters treated as future directions.

## Open questions

- Does the WiFo-2 result replicate outside the authors' own 11.6 billion-point CSI corpus, and does zero-shot performance hold on measured channels from sites and configurations absent from pretraining?
- Do the reported channel-shaping gains, such as movable signals beating quantised equal gain transmission, survive on hardware once signalling overhead, quantisation and control latency are counted?
- What is the communication rate actually sacrificed when a transmitter is constrained to sensing-optimal waveforms, given the converse bound on the sensing-constrained diversity-multiplexing tradeoff, and is the ISAC bargain net-positive for an operator?
- Can the thin-film lithium tantalate ultraviolet modulator's 85 mV·cm VπL and 1.3 dB insertion loss be reproduced at wafer scale and yield, and is there a solar-blind communications market that pays for it?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
