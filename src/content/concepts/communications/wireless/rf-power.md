---
type: concept
slug: rf-power
canonical_name: RF Power
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2026-06-11-a-new-approach-to-designing-rf-power-amplifiers-for-modern-m]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-06-11-a-new-approach-to-designing-rf-power-amplifiers-for-modern-m
  title: A New Approach to Designing RF Power Amplifiers for Modern Military Systems - Tech Briefs
  date: '2026-06-11'
  kind: web
- slug: 2026-06-11-darpa-threads-the-needle-on-thermal-barriers-to-rf-power---d
  title: DARPA THREADS the needle on thermal barriers to RF power - darpa.mil
  date: '2026-06-11'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
neighbors: []
---
## Physics / mechanism

RF power refers to the generation, routing, amplification and detection of energy carried by radiofrequency electromagnetic fields. In transmit chains the dominant device-level concern is the power amplifier, where DC supply energy is converted into RF output at a target frequency, with efficiency losses appearing as heat in a small semiconductor volume. AlGaN/GaN high electron mobility transistors (HEMTs) are the mainstream device family for high-power RF amplification in satellite communications, defence radar and deep-space missions nsf 2625165 radiation aware transport modeling of al. The relevant physics spans carrier transport in the two-dimensional electron gas at the AlGaN/GaN heterointerface, radiation-induced defect formation that alters that transport, and thermal transport out of the active region.

Thermal resistance is a first-order limit on deliverable RF power: DARPA's THREADS programme is framed explicitly around thermal barriers to RF power, with phase-change materials among the approaches considered darpa threads the needle on thermal barriers to rf power   d. Radiation hardness is the second limit for space and defence use; existing prediction methods for radiation damage rely on approximate, trial-and-error models rather than fundamental physical understanding of how charge transport changes at the atomic level, which forces per-mission qualification testing nsf 2625165 radiation aware transport modeling of al.

On the routing side, RF power can be redistributed rather than amplified. A proposed narrowband fully-analog N-antenna transmitter synthesises an arbitrary complex excitation vector x[m] in C^N with prescribed total power ||x[m]||² = P from a single RF tone, using only tunable phase-control elements in a passive interferometric programmable network excited through one input port while the remaining N−1 input ports are impedance matched a narrowband fully analog multi antenna transmitter. In the ideal lossless case the network transfer is unitary, so RF power is redistributed among antenna ports without dissipative amplitude control, and beam synthesis becomes a unitary state-preparation problem a narrowband fully analog multi antenna transmitter.

On the receive side, the figure of merit shifts from field sensitivity to power sensitivity. Nitrogen-vacancy (NV) centres in diamond detect RF signals via coupling of the RF magnetic field to NV spins with optical readout of the spin state; sensitivity has mostly been characterised as magnetic field sensitivity, which is the relevant metric only when the source is in the near field power sensitivity of broadband radiofrequency detectors base. For externally delivered RF inputs, input RF power sensitivity is the appropriate quantity, and it scales with the geometry of the RF-spin interface; scaling laws have been derived for both slope-detection and variance-detection protocols power sensitivity of broadband radiofrequency detectors base.

## Competitive landscape

The sources touch three distinct layers of the RF power stack rather than direct competitors. At the device layer, GaN-based HEMTs are the incumbent for high-power RF amplification in space and radar systems nsf 2625165 radiation aware transport modeling of al, and GaN is discussed more broadly as a compound semiconductor with a different trade-off set from silicon gallium nitride photonics w james. At the architecture layer, fully-analog interferometric networks are positioned against fully-digital multi-antenna transmitters, which require a full RF chain per antenna; the analog approach targets equivalent functionality from a single RF tone plus phase shifters, trading digital flexibility for reduced chain count and no dissipative amplitude control a narrowband fully analog multi antenna transmitter. At the sensing layer, NV-diamond RF detectors compete with conventional electronic receivers, but the sources characterise only the NV case and only theoretically power sensitivity of broadband radiofrequency detectors base.

Thermal management is treated as a shared bottleneck rather than a differentiator: DARPA frames thermal barriers as the constraint on RF power across applications darpa threads the needle on thermal barriers to rf power   d.

## Evidence base

- A theoretical analysis published 15 May 2026 derives power sensitivity scaling laws for NV-diamond broadband RF detectors as a function of RF-spin interface geometry, for slope-detection and variance-detection protocols power sensitivity of broadband radiofrequency detectors base.
- A narrowband fully-analog N-antenna transmitter design (revised version, 16 June 2026) claims emulation of fully-digital transmitter functionality using a passive unitary programmable network driven by a single RF tone a narrowband fully analog multi antenna transmitter.
- NSF award 2625165, dated 4 August 2026, funds $450,000 to Taewoo Kim at Texas Tech University for radiation-aware transport modelling of AlGaN/GaN HEMTs aimed at radiation-hardened RF power amplifiers nsf 2625165 radiation aware transport modeling of al.
- The same award states that current radiation-damage prediction relies on approximate, trial-and-error models, forcing costly per-mission testing nsf 2625165 radiation aware transport modeling of al.
- DARPA publicised the THREADS effort on thermal barriers to RF power on 11 June 2026, with phase-change materials among the concepts referenced darpa threads the needle on thermal barriers to rf power   d.
- A trade article dated 11 June 2026 reports a new approach to designing RF power amplifiers for modern military systems, associated with DARPA small business innovation activity a new approach to designing rf power amplifiers for modern m.

## Frontier (open questions)

- What measured power sensitivity, in W/√Hz, do NV-diamond RF detectors achieve for externally delivered inputs, and does it match the derived geometric scaling laws?
- Does the interferometric fully-analog transmitter retain its power-redistribution advantage once realistic network insertion loss, phase-shifter resolution and port mismatch are included, and at what antenna count N does it beat a fully-digital chain?
- Can atomistic transport models of irradiated AlGaN/GaN predict measured RF power amplifier degradation accurately enough to replace per-mission radiation qualification testing?
- What junction temperature reduction and corresponding RF output power gain do phase-change-material thermal solutions deliver in a packaged GaN amplifier, and over how many thermal cycles do they survive?

*Synthesised 2026-08-31 from 6 KB sources by the resynth pipeline; citations are KB source slugs.*
