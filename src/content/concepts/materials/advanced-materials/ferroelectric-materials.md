---
type: concept
slug: ferroelectric-materials
canonical_name: Ferroelectric Materials
aliases:
- ferroelectric
- ferroelectrics
- FE materials
parent_concepts:
- advanced-materials
- materials
related_concepts:
- hafnium-oxide
- barium-titanate
- piezoelectric
- aluminium-scandium-nitride
- high-k-dielectrics
sources:
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- Can HZO device-to-device variability be reduced by direct process control (oxygen partial pressure, laser energy density window, film thickness uniformity) to the point that per-die statistical screening becomes unnecessary, or is screening a permanent feature of the technology?
- Do the ML-screened candidates, in particular AuCrP2S6 with its 7.46 pC/m polarisation and ~130 meV/f.u. switching barrier, survive attempted synthesis and show the predicted four-state behaviour with bulk-photovoltaic readout?
- How many published thin-film and 2D ferroelectricity claims survive re-measurement using piezoelectric strain loops rather than polarisation loops alone, given that series capacitance can mimic hysteresis even under the double-wave method?
- Can charged domain wall conductivity in a perovskite be made robust across phase transitions and ordinary temperature swings, or does the fragmentation observed at the tetragonal-orthorhombic transition rule out domain wall interconnect?
- Does any ferroelectric material class beyond HfO2 reach CMOS-compatible integration — specifically, can sub-20 nm BaTiO3 films be ALD-deposited with device-grade phase control?
- 'Neuromorphic / analogue computing: can multi-state FeFET polarisation (partial switching) be used for reliable weight storage in edge-AI inference — what is the practical bit precision ceiling?'
- What is the commercialisation path for AlScN ferroelectric (CMOS-compatible, high coercive field) as a piezo-MEMS alternative to PZT — does it reach MEMS foundry production by 2028?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 194
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 8
sources_30d: 21
recent_mentions:
- slug: 2025-26-lapedus-next-gen-ferroelectric-memory
  title: Next-Gen Ferroelectric Memory Still A Work In Progress
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
neighbors:
- slug: hafnium-oxide
  name: Hafnium Oxide
  path: /materials/functional-layers/hafnium-oxide/
  macro: materials
- slug: barium-titanate
  name: Barium Titanate
  path: /materials/functional-layers/barium-titanate/
  macro: materials
- slug: piezoelectric
  name: Piezoelectric
  path: /materials/functional-layers/piezoelectric/
  macro: materials
- slug: aluminium-scandium-nitride
  name: Aluminium Scandium Nitride
  path: /materials/functional-layers/aluminium-scandium-nitride/
  macro: materials
- slug: high-k-dielectrics
  name: High-K Dielectrics (HfO2, ZrO2)
  path: /materials/functional-layers/high-k-dielectrics/
  macro: materials
---
**Ferroelectrics are insulators whose electric polarisation can be flipped by a voltage and stays flipped without power, and the current research front is dominated by hafnium-zirconium oxide for CMOS-compatible embedded memory plus a fast-growing set of layered van der Waals and quantum ferroelectrics for memory, photonics and magnetoelectric devices.**

## Summary

Underneath both branches, the field is re-tooling its theory and its measurement hygiene. A unified definition of ferroelectricity based on switchable polarisation differences between energetically equivalent states, rather than polar space-group membership, has been used to screen synthesised materials and identify new quantum ferroelectrics including Ba3I6 and Cs2PdC2. Finite-temperature behaviour can now be predicted from ground-state properties alone, without the fitted temperature-dependent parameters that Landau-Ginzburg treatments require, with quantitative agreement for PbTiO3, SrTiO3 and KTaO3. On the sceptical side, series capacitance artefacts can produce apparent polarisation hysteresis loops even under the double-wave method, and loops of that kind appear in the published literature; and a 25-year-old prediction of room-temperature out-of-plane ferroelectricity in compressively strained SrTiO3 has been re-examined at up to -3% strain, where butterfly capacitance-voltage hysteresis and domain-like piezoresponse were found to be inconsistent with a stable ferroelectric state.

## Viability (3/5)

**TLDR: Real switching in real devices, but phase metastability, wafer-scale variability and false-positive measurements all remain live.**

## Drivers (3/5)

Demand side is thinner in this corpus. The only explicit statement is that AI workloads are driving exponentially growing demand for non-volatile and computational memory, given as motivation in an abstract rather than as market evidence. No source here contains foundry roadmaps, product announcements, capacity commitments or pricing. The score is capped at 3 for that reason: the push is demonstrable, the pull is plausible but unmeasured in the supplied material.

**TLDR: Strong and diverse supply-side push across many independent groups; demand is asserted rather than quantified in these sources.**

## Novelty (3/5)

At device level the ferroelectric junction FET memory is described as a fundamentally different device rather than an increment, with 900 meV of barrier modulation and near-ideal junction behaviour, and the AuCrP2S6 proposal solves a named problem in multiferroic memory, the lack of non-destructive readout, using photocurrent sign and spin channel as two independent probes. What is missing is any benchmark against the technologies these would displace: no endurance, retention, energy per bit or density comparison against existing memory appears in these sources, so the novelty cannot be scored above contested.

**TLDR: Clear, specific gains over named prior methods in theory, process and device architecture; almost no head-to-head comparison against incumbent memory technologies.**

## Diffusion (2/5)

Other barriers are visible across the corpus. Several effects are not room-temperature or not robust: charged domain wall conductivity in BaTiO3 falls by orders of magnitude below about 5 C as the wall fragments into micron-scale segments at the tetragonal-orthorhombic transition, and oxygen-vacancy-doped EuTiO3-delta reaches a maximum Curie temperature of only about 11 K at n approximately 10^21 cm^-3. Van der Waals devices are exfoliated-stack demonstrations with no manufacturability evidence here. And the measurement-artefact problem plus the strained-SrTiO3 reassessment mean adopters cannot take literature claims at face value without independent verification, which itself slows transfer.

**TLDR: Manufacturing variability is the acknowledged blocker for the near-term HZO path, and the exotic branches are single-flake demonstrations.**

## Impact (4/5)

The functional breadth here is unusual for one material class. In memory, HZO targets embedded non-volatile and computational memory directly in the CMOS back end, and vdW junction transistor memory demonstrates a 1.8 V window with picoamp leakage. In magnetoelectronics, electric-field control of the anomalous Hall effect has been shown at room temperature in Py/BaTiO3/La0.7Sr0.3MnO3 heterostructures on MgO and LaAlO3, and polar distortions have been observed coexisting with altermagnetic order in MnTe at atomic resolution, both routes to voltage-controlled spintronics. In photonics, NbOI2 offers record optical nonlinearities and dielectric anisotropy with sub-micrometre spin-orbit control for on-chip polarisation handling and beam steering. Reconfigurable conductive channels written optically into an insulator add a further device class.

The score is 4 rather than 5 because none of these sources quantifies economic value, addressable market or system-level gain. The judgement rests on the number of independent, room-temperature-capable device functions demonstrated from one materials family, not on any financial evidence.

**TLDR: If the manufacturing problem is solved, ferroelectrics touch memory, logic-adjacent compute, photonics and magnetoelectronics from a single materials base.**

## Timing Soon (2-5yr)

Everything else is earlier. The 2D multiferroic candidates are computational predictions awaiting synthesis, the newly identified quantum ferroelectrics are screening hits selected for experimental viability rather than demonstrated devices, and domain wall electronics still loses its conductive channel across an ordinary phase transition near 5 C. For context on how slow this can be: room-temperature out-of-plane ferroelectricity in compressively strained SrTiO3 was predicted 25 years ago and is still not established.

**TLDR: HZO is at the manufacturing-yield stage now; the van der Waals and quantum-ferroelectric branches are a decade out.**

## Overrated or underrated? Fairly rated

Where expectations should be discounted is the exploratory tail. The corpus itself supplies the discount: series-capacitance artefacts can manufacture convincing hysteresis loops that appear in published work, and a flagship strained-perovskite target turns out to show polarity from inhomogeneous internal fields rather than a stable switchable state. Treat any new claimed ferroelectric, especially thin-film or 2D, as unconfirmed until strain-based (S-E) or structural evidence accompanies the polarisation loop. Correspondingly, the ML-screened multiferroic and quantum-ferroelectric candidates should be read as a widened search space, not as devices.

## Prediction

By 31 December 2028, no independently reproduced demonstration of stable room-temperature out-of-plane ferroelectric switching in compressively strained SrTiO3 capacitors will have been published, and published wafer-scale HZO capacitor studies will still report device-to-device variability large enough to require statistical or machine-learning screening rather than deterministic process control.

## Evidence base

## Open questions

- Can HZO device-to-device variability be reduced by direct process control (oxygen partial pressure, laser energy density window, film thickness uniformity) to the point that per-die statistical screening becomes unnecessary, or is screening a permanent feature of the technology?
- Do the ML-screened candidates, in particular AuCrP2S6 with its 7.46 pC/m polarisation and ~130 meV/f.u. switching barrier, survive attempted synthesis and show the predicted four-state behaviour with bulk-photovoltaic readout?
- How many published thin-film and 2D ferroelectricity claims survive re-measurement using piezoelectric strain loops rather than polarisation loops alone, given that series capacitance can mimic hysteresis even under the double-wave method?
- Can charged domain wall conductivity in a perovskite be made robust across phase transitions and ordinary temperature swings, or does the fragmentation observed at the tetragonal-orthorhombic transition rule out domain wall interconnect?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
