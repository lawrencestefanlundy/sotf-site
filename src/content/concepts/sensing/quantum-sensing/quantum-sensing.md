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
mention_count: 164
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
sources_7d: 6
sources_30d: 16
recent_mentions:
- slug: 2026-07-21-precision-astrometry-using-optically-independent-spacecraft-
  title: Precision Astrometry Using Optically Independent Spacecraft for Graviational Wave Detection
  date: '2026-07-21'
  kind: web
- slug: 2026-03-08-diamonds-are-semiconductors-best-friend
  title: Diamonds are Semiconductors' Best Friend 2026
  date: '2026-03-08'
  kind: web
- slug: 2024-12-16-willow-and-the-race-to-quantum-advantage
  title: Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)
  date: '2024-12-16'
  kind: substack
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
