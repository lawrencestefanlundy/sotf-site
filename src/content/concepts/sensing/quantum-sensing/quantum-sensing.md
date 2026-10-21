---
type: concept
slug: quantum-sensing
canonical_name: Quantum Sensing
aliases: []
kind: technology
parent_concepts:
- sensing
- quantum-sensing
related_concepts: []
sources:
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
frontier: []
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 219
descendants:
- atomic-clocks
- nv-diamond-sensing
- optomechanics
- quantum-gravimetry
- quantum-imaging
- quantum-magnetometry
- quantum-sensing
last_reorg_date: '2026-05-13'
scorecard:
  viability: null
  drivers: null
  novelty: null
  diffusion: null
  impact: null
  timing_band: Unclear
  verdict: ''
scorecard_status: draft
sources_7d: 3
sources_30d: 12
recent_mentions:
- slug: 2026-10-19-light-and-mirrors-move-large-quantum-computers-closer-to-rea
  title: Light and mirrors move large quantum computers closer to reality
  date: '2026-10-19'
  kind: web
- slug: 2026-10-18-hybrid-diamond-chip-strengthens-interactions-between-light-a
  title: Hybrid diamond chip strengthens interactions between light and quantum bits
  date: '2026-10-18'
  kind: web
- slug: 2026-10-18-new-monolithic-ion-trap-opens-quantum-simulations-to-more-re
  title: New monolithic ion trap opens quantum simulations to more researchers
  date: '2026-10-18'
  kind: web
- slug: 2026-10-16-new-chip-based-tape-measure-for-light-could-revolutionize-mo
  title: New Chip-Based ‘Tape Measure’ for Light Could Revolutionize Mobile Timekeeping and Enhance National Security
  date: '2026-10-16'
  kind: web
- slug: 2026-10-15-us-optical-chip-gyroscope-gets-2000-fold-sensitivity-boost-d
  title: US optical chip gyroscope gets 2,000-fold sensitivity boost, detects slow rotation
  date: '2026-10-15'
  kind: web
- slug: 2026-10-14-new-chip-scale-gyroscope-measures-rotation-with-unprecedente
  title: New chip-scale gyroscope measures rotation with unprecedented sensitivity
  date: '2026-10-14'
  kind: web
- slug: 2026-10-13-faster-molecular-simulations-identify-promising-diamond-defe
  title: Faster molecular simulations identify promising diamond defects for quantum computers and sensors
  date: '2026-10-13'
  kind: web
- slug: 2026-10-13-new-topological-microscope-tip-reveals-evidence-of-2d-alterm
  title: New topological microscope tip reveals evidence of 2D altermagnetism
  date: '2026-10-13'
  kind: web
neighbors: []
---
**Quantum sensing uses individual quantum systems (spin defects in crystals, cold atoms, squeezed light) as measurement probes whose coherence turns tiny fields into readable phase shifts; the diamond nitrogen-vacancy and cold-atom platforms now deliver real physics results, while the entangled-network promises remain largely theoretical.**

## Summary

A quantum sensor is a probe whose quantum state, rather than a bulk material property, carries the measurement. The dominant solid-state version is the nitrogen-vacancy (NV) centre, a point defect in diamond whose electron spin resonance frequency shifts with magnetic field and can be initialised and read out optically; NV centres are described in the current literature as the most important solid-state quantum sensors. The other main families are atomic: alkali vapour magnetometers operating in the spin-exchange relaxation-free regime, atom interferometers that split and recombine matter waves to sense forces and fields, and photonic or microwave schemes that use squeezed vacuum to beat shot noise.

The parameters that decide performance are few and physical. Sensitivity scales with coherence time, the number of probes, and readout contrast, which is why several current results attack contrast directly: embedding NV ensembles in a laser cavity so the magnetic resonance switches the laser off entirely gives 100 per cent optical contrast against a few per cent for conventional ensembles, with photon-shot-noise-limited sensitivity below 400 fT/√Hz on all vector components and output up to 50 mW. A separate protocol that purifies the NV charge state with a strong laser pulse before weak repumping improves readout contrast by 17 per cent and cuts initialisation error by more than half. Sensor-target distance matters as much as sensitivity, which motivates moving spin defects into atomically thin hosts, since NV performance degrades near surfaces and in nanoscale volumes.

Above the single-sensor level sits a second research programme: distributed and entangled sensing, where a network of probes estimates a non-local property of a field. Recent theory gives explicit conditions on sensor placement for error-free estimators and argues that entanglement yields maximal precision in distributed sensing under global resource constraints, and separate work shows that in Gaussian networks with more than two nodes perfect privacy is achievable only asymptotically in large photon number, while local homodyne detection is essentially optimal and gives quadratic scaling of precision with total photon number. This layer is analytical and simulated; the sources contain no experimental network.

The practical question for any application is whether the quantum probe reaches somewhere no classical instrument can. The clearest example in these sources is magnetometry inside a diamond anvil cell: NV centres fabricated directly on the anvil surface imaged the stray field of iron up to 30 GPa and resolved the α-ε magnetic transition, in a regime where magnetometry techniques were previously limited.

## Viability (unscored)

## Drivers (unscored)

## Novelty (unscored)

## Diffusion (unscored)

## Impact (unscored)

## Timing Unclear

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
