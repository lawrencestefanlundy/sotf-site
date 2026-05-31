---
type: concept
slug: coupled-oscillator-networks
canonical_name: Coupled Oscillator Networks
aliases:
- coupled oscillator Ising machine
- oscillator-based compute
- OIM
- ring oscillator Ising
kind: technology
parent_concepts:
- physics-native-compute
- analog-computing
- coherent-ising-machine
related_concepts:
- coherent-ising-machine
- near-field-rf-coupling
- stochastic-ising-machines
- fdtd-calibration-wall
sources: []
frontier:
- Does the Chris Kim Minnesota wired-CMOS coupled-oscillator approach ship chip-integrable production hardware before Vega?
- Does VO2 phase-change oscillator (Shukla / Notre Dame) ever scale beyond academic prototypes?
- Can Kuramoto-style synchronisation be exploited for compute beyond Ising minimisation?
last_updated: '2026-05-27'
tags:
- concept
- compute
- ising-machine
- oscillator
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors:
- slug: coherent-ising-machine
  name: Coherent Ising Machine
  path: /sotf-site/compute/non-conventional/coherent-ising-machine/
  macro: compute
- slug: near-field-rf-coupling
  name: Near-Field RF Coupling (as compute substrate)
  path: /sotf-site/compute/non-conventional/near-field-rf-coupling/
  macro: compute
- slug: stochastic-ising-machines
  name: Stochastic / Ising Machines
  path: /sotf-site/compute/non-conventional/stochastic-ising-machines/
  macro: compute
- slug: fdtd-calibration-wall
  name: FDTD-to-Hardware Calibration Wall
  path: /sotf-site/compute/non-conventional/fdtd-calibration-wall/
  macro: compute
---
The broader academic substrate class that contains the [Coherent Ising Machine](/sotf-site/compute/non-conventional/coherent-ising-machine/) family plus adjacent oscillator-coupling dynamics. The compute mechanism is **phase relaxation in a network of weakly-coupled nonlinear oscillators**: each oscillator settles to a phase that minimises some collective energy function defined by the coupling matrix.

Different families of coupled-oscillator network share the maths but differ in:
1. **What oscillates** (LC tank, ring oscillator, VO₂ phase-change, spin-torque oscillator, microstrip antenna)
2. **How they couple** (wired electrical, wireless near-field RF, optical fibre, magnetic flux)
3. **What scale they reach** (10s of nodes academic, 100s prototype, 1000s+ chip-integrable production)

## Family tree

## Wang & Roychowdhury OIM 2019

The OIM formulation shows that a Kuramoto-style oscillator network with appropriate forcing settles into a phase configuration that minimises a quadratic energy function — exactly the Ising Hamiltonian. The coupling matrix J becomes the Ising J. Any hardware that implements an oscillator network with programmable J solves Ising.

## DARPA QuICC programme

## Sources

<!-- dataview block stripped for public site -->
