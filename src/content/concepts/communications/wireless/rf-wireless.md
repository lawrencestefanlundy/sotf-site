---
type: concept
slug: rf-wireless
canonical_name: RF & Wireless
aliases: []
kind: technology
parent_concepts:
- communications
- wireless
related_concepts: []
sources: []
frontier:
- Does the reciprocity result for a finite RIS with one particular unit-cell design generalise to commercial panel sizes and heterogeneous unit cells, or does it need re-establishing per design 2026 06 15 implications of the reciprocity theorem for reconfigurable i?
- Can pilot overhead for extremely large passive arrays and SIM layers be reduced enough that near-field beamfocusing is affordable with realistic RF chain counts 2026 06 15 dual transformer aided hierarchical deep reinforcement learn 2026 06 16 sparse channel estimation for sim based mmwave near field co?
- Does sub-THz presence detection survive the empty-room drift observed under small environmental changes, and what false-alarm rate does that imply in an unattended deployment 2026 06 16 on the feasibility of human presence detection using ceiling?
- Do magnonic phase shifters retain their footprint and tuning advantages once insertion loss, MEMS reliability and array-scale integration are accounted for 2026 06 15 microscaled tunable magnonic rf phase shifters?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 44
descendants: []
last_reorg_date: '2026-05-13'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-09-01-nasa-selects-blue-origin-as-mars-telecommunications-network-
  title: NASA Selects Blue Origin as Mars Telecommunications Network Provider
  date: '2026-09-01'
  kind: web
- slug: 2026-08-27-opener-is-an-open-source-reference-implementation-of-the-dec
  title: Opener is an open-source reference implementation of the DECT NR+ massive IoT, low-latency standard - CNX Software
  date: '2026-08-27'
  kind: web
- slug: 2026-08-21-dect-nr-gateway-brings-deterministic-wireless-to-industrial-
  title: DECT NR+ gateway brings deterministic wireless to industrial automation - eeNews Europe
  date: '2026-08-21'
  kind: web
- slug: 2026-08-19-wi-fi-7-breaks-into-the-mcu-field-next-gen-wireless-connecti
  title: 'Wi-Fi 7 Breaks into the MCU Field: Next-Gen Wireless Connectivity for Microcontroller Applications - 36 Kr'
  date: '2026-08-19'
  kind: web
- slug: 2026-08-18-wi-fi-7-accelerates-into-the-mcu-space-as-infineon-and-synap
  title: Wi-Fi 7 Accelerates into the MCU Space as Infineon and Synaptics Move First - finance.biggo.com
  date: '2026-08-18'
  kind: web
- slug: 2026-08-12-viavi-introduces-industrys-first-channel-emulator-for-6g-and
  title: VIAVI Introduces Industry's First Channel Emulator for 6G and Wi-Fi 7/8 - barchart.com
  date: '2026-08-12'
  kind: web
- slug: 2026-08-11-anybus-communicators-are-cra-ready---august-2026---industria
  title: Anybus Communicators are CRA-ready - August 2026 - Industrial Data Xchange (IDX) - SA Instrumentation & Control
  date: '2026-08-11'
  kind: web
- slug: 2026-08-03-quectel-adds-wi-fi-7-and-bluetooth-60-modules-for-consumer-a
  title: Quectel Adds Wi-Fi 7 and Bluetooth 6.0 Modules for Consumer and Edge Devices - IoT Business News
  date: '2026-08-03'
  kind: web
neighbors: []
---
**RF and wireless is the engineering layer where 6G ambitions meet physics: a June 2026 snapshot of the research front shows credible hardware progress in filters, phase shifters and linearisation alongside system-level concepts (reconfigurable surfaces, integrated sensing, sub-THz links) that are still mostly testbed and simulation work.**

## Summary

"RF and wireless" here covers the radio-frequency signal chain and the propagation environment it works in: the analogue components that generate, filter, steer and linearise GHz-to-sub-THz signals; the antenna and metasurface structures that shape the channel; the channel models and estimation algorithms that make the link usable; and the growing use of the same radio hardware for sensing rather than just data transport. The current research front, judged from arXiv output on 15-16 June 2026, splits into three fairly distinct layers with different maturity.

At the architecture layer sit the reconfigurable-surface and analogue-computing ideas. Reconfigurable intelligent surfaces (RIS) are passive or semi-passive panels of tunable unit cells that redirect incident waves, used to build non-line-of-sight paths around blockages; stacked intelligent metasurfaces (SIM) extend this to multiple layers doing beamforming in the wave domain, which forces channel estimation with fewer RF chains than meta-atoms. Microwave linear analog computers (MiLAC) push beamforming into a tunable admittance network, where a stem-connected topology reduces the count of tunable admittances from quadratic to linear in antenna number while still matching fully-connected sum-rate when the antenna count is at least 2K-1 for K users. A foundational dispute in this layer was addressed directly: claims that RIS reflection breaks transmit/receive reciprocity when reflection phase is angle-dependent are attributed to idealised reflection coefficients that ignore mutual coupling, surface truncation and structural scattering, with full-wave simulation and reciprocity integrals showing reciprocity does hold.

## Viability (3/5)

The hardware end has real numbers behind it. The magnonic phase shifter is an experimental device with a stated phase range, centre frequency, tuning band and footprint; the XBAR Q anisotropy study characterises fabricated resonators across in-plane orientations; sub-THz channel sounding uses a VNA with frequency extenders and mechanically scanned virtual arrays in three real indoor environments; passive LoRa sensing was confirmed on two USRP B210 radios. These are believable, if small-scale.

Against that, the system-level layer is not yet settled. A basic electromagnetic property of RIS was still being contested in mid-2026 and required full-wave modelling to resolve, which indicates how much of the RIS literature rests on idealised unit-cell models. Near-field XL-MIMO and RIS control schemes are proposed as learning frameworks evaluated against models and digital-twin priors rather than deployed networks, and biomedical sensing claims rest on 15 healthy participants in a controlled study. Some entries are explicitly illustrative modelling with representative parameters rather than measurement, such as the helical carbon coil absorber study. A 3 reflects a field where the components work and the systems are unproven.

**TLDR: Device-level results are measured and specific; system-level 6G concepts remain simulation and testbed grade.**

## Drivers (3/5)

On the supply side the sources show an unusually wide and simultaneous push: spin-wave and MEMS device physics, lithium niobate thin-film acoustics, metasurface electromagnetics, analogue microwave computing, machine learning for channel estimation and pre-distortion, and measurement campaigns using commodity SDRs and VNA-based sub-THz sounders. Author lists span multiple institutions and countries, and the work engages the standards baseline directly: one ISAC channel framework extends 3GPP TR38.901 with hybrid deterministic and stochastic clustering while keeping communication performance parity with the standard model.

Demand evidence is weaker and mostly declarative. The stated pulls are 6G near-field deployments, mission-critical networks including the internet of vehicles and the low-altitude economy, ceiling-mounted distributed indoor radio units, contactless healthcare monitoring, and size, weight and power limits in satellite payloads. There are no operator commitments, volumes, prices or funding figures in the sources, so the demand side of this score is an inference from research framing, not from market data.

**TLDR: Broad, coordinated research supply; demand is stated as 6G and sensing use cases rather than demonstrated.**

## Novelty (3/5)

Elsewhere the novelty is conceptual reframing rather than measured advantage: event-level sensing positioned against target-level ISAC parameter estimation, polar-domain against angular-domain sparse channel representation for near-field SIM links, and Rydberg atomic receivers presented as compatible with the classical RF framework but with explicitly bounded linear dynamic range. Useful, but not yet a demonstrated step change over conventional receivers.

**TLDR: Real, quantified gains over specific incumbents at component level; the system-level claims are mostly better-than-simulation.**

## Diffusion (2/5)

Two things in the sources lower adoption friction. Sensing that reuses signals already transmitted by deployed networks, with no waveform change and no interference to normal operation, avoids the need for new spectrum or new radios. And ISAC channel modelling built as an extension of 3GPP TR38.901, preserving communication performance parity, is the right shape for standardisation rather than a parallel track.

The obstacles are also stated plainly by the same literature. Acquiring instantaneous channel state information for massive passive arrays carries prohibitive pilot overhead, and blockage from moving scatterers is unpredictable. SIM architectures create an underdetermined estimation problem because base stations have fewer RF chains than meta-atoms per layer, and near-field XL-MIMO tracking is described as time-consuming and hardware-intensive, needing subarray hybrid beamforming and time multiplexing to compensate for limited RF chains. Sub-THz sensing is sensitive to target position and antenna beamwidth, and even repeated empty-room measurements shift with minor environmental change, which is a hard problem for products that must work unattended. Nothing in the sources addresses cost, manufacturability at volume, or regulatory approval, so this score covers technical adoption barriers only.

**TLDR: Barriers are named by the sources themselves: channel-knowledge overhead, environmental fragility and RF chain scarcity.**

## Impact (3/5)

The strongest impact argument the sources support is marginal-cost capability: if sensing can be extracted from existing unmodified communication transmissions and if ISAC channel models can add sensing evaluation while holding communication performance parity with the standard baseline, then networks acquire a second function without a second infrastructure. The named beneficiaries are vehicular networks and low-altitude airspace operations, contactless vital-sign monitoring in real living environments including non-line-of-sight cases, and satellite payloads where linearisation complexity is constrained by size, weight and power.

What the sources do not provide is any quantification of that value: no throughput, coverage, energy or cost deltas at network level, no addressable market, no comparison against simply deploying more conventional radio units. The blood-pressure feasibility study is 15 participants, which cannot carry a clinical impact claim. A 3 is therefore a judgement that the mechanisms of value are plausible and specific, while the magnitude is not evidenced here.

**TLDR: The value case is credible in kind but unquantified in the sources.**

## Timing Soon (2-5yr)

The device and algorithm work is closest. Sparse DPD is a drop-in change to an existing signal-processing block with a measured complexity saving, and XBAR orientation-dependent Q is design guidance for filter synthesis in a material system already being fabricated at 500 nm on silicon. The magnonic phase shifter is a working single device with system-level characterisation reported, but is a long way from a qualified RF part.

The architecture layer is later and the sources do not date it. RIS and SIM depend on solving channel estimation with fewer RF chains than tunable elements and on tolerable pilot overhead for very large passive arrays; sub-THz indoor deployment is at the stage of first channel characterisation campaigns in offices, laboratories and ventilation rooms; Rydberg receivers are at wireless-model and dynamic-range-bounding stage. Read the band as applying to the parts of this field that ship inside conventional radios, not to the 6G system concepts.

**TLDR: Component-level results could reach products on a short cycle; RIS, SIM and sub-THz systems are further out and gated on channel knowledge.**

## Overrated or underrated? Fairly rated

Taken as a whole the field is priced about right, but the internal distribution is skewed. The visible attention sits on reconfigurable surfaces, near-field XL-MIMO and ISAC as 6G system concepts, where the June 2026 evidence is dominated by simulation, learning frameworks and digital-twin priors, and where a foundational reciprocity question was only just closed out with full-wave modelling. That is not fatal, but it means the RIS/SIM literature is still partly built on idealised element models, and the practical blocker named repeatedly is channel knowledge cost, not element performance.

The underweighted parts are unglamorous: acoustic filter design in lithium niobate, tunable analogue phase shifting in micron-scale footprints, cheaper linearisation for power-constrained payloads, and topologies that turn quadratic hardware scaling into linear. Those are where measured advantages over named baselines actually exist, and they will decide whether the system-level concepts are affordable. The other genuinely interesting near-term line is sensing that piggybacks on already-deployed waveforms, because it sidesteps the deployment problem entirely.

## Prediction

By June 2029, RIS and stacked-intelligent-metasurface links will still be reported predominantly in simulation and small testbed studies rather than in commercially deployed networks, with channel-state acquisition overhead cited as the limiting factor.

## Evidence base

- 15 June 2026: full-wave electromagnetic simulation of transmit/receive antennas with a finite-size RIS shows reciprocity holds even with incident-angle-dependent reflection phase; prior claims to the contrary are attributed to idealised reflection coefficients ignoring mutual coupling, surface truncation and structural scattering.
- 15 June 2026: a micron-scale magnonic RF phase shifter demonstrates more than 360 degrees of phase shift at 6.1 GHz in under 0.02 mm squared, experimentally confirmed from 3 to 8.2 GHz with simulations extending to 14 GHz.
- 15 June 2026: stem-connected MiLAC beamforming reduces tunable admittance count from quadratic to linear in antenna number and matches fully-connected sum-rate when the antenna count is at least 2K-1 for K users.
- 15 June 2026: passive bistatic Doppler sensing using unmodified LoRa signals is validated with measurements on two USRP B210 software-defined radios, without modifying the communication waveform or interfering with network operation.
- 16 June 2026: ceiling-mounted channel sounding at 134 to 146 GHz detects human presence, but detectability depends strongly on target position and antenna beamwidth, and repeated empty-room measurements vary with small environmental changes.
- 16 June 2026: least-squares thresholding for generalised memory polynomial digital pre-distortion gives a 2.77x complexity reduction versus orthogonal matching pursuit with near-identical linearisation, targeted at size, weight and power constrained satellite payloads.

## Open questions

- Does the reciprocity result for a finite RIS with one particular unit-cell design generalise to commercial panel sizes and heterogeneous unit cells, or does it need re-establishing per design?
- Can pilot overhead for extremely large passive arrays and SIM layers be reduced enough that near-field beamfocusing is affordable with realistic RF chain counts?
- Does sub-THz presence detection survive the empty-room drift observed under small environmental changes, and what false-alarm rate does that imply in an unattended deployment?
- Do magnonic phase shifters retain their footprint and tuning advantages once insertion loss, MEMS reliability and array-scale integration are accounted for?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
