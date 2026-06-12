---
type: concept
slug: coherent-ising-machine
canonical_name: Coherent Ising Machine
aliases:
- CIM
- OIM
- Oscillator Ising Machine
parent_concepts:
- non-conventional-computing
- analog-computing
- compute-paradigms
related_concepts:
- stochastic-ising-machines
- probabilistic-computing
- thermodynamic-computing
- quantum-annealing
- near-field-rf-coupling
- fdtd-calibration-wall
sources: []
frontier:
- Does RF substrate (Vega) close the FDTD-J-to-realised-J calibration gap at N>=256 on real silicon?
- Does the Chris Kim / Minnesota wired-CMOS coupled-oscillator approach ship chip-integrable production hardware before Vega?
- Does the Litman et al. 2025 SDPA ≡ EOT result drive a new wave of inference-primitive-as-CIM startups?
last_updated: 2026-05-22
tags:
- concept
- compute
- ising-machine
- analog-computing
descendants:
- coupled-oscillator-networks
- near-field-rf-coupling
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: stochastic-ising-machines
  name: Stochastic / Ising Machines
  path: /sotf-site/compute/non-conventional/stochastic-ising-machines/
  macro: compute
- slug: probabilistic-computing
  name: Probabilistic Computing
  path: /sotf-site/compute/non-conventional/probabilistic-computing/
  macro: compute
- slug: thermodynamic-computing
  name: Thermodynamic Computing
  path: /sotf-site/compute/non-conventional/thermodynamic-computing/
  macro: compute
- slug: quantum-annealing
  name: Quantum Annealing
  path: /sotf-site/compute/quantum-computing/quantum-annealing/
  macro: compute
- slug: near-field-rf-coupling
  name: Near-Field RF Coupling (as compute substrate)
  path: /sotf-site/compute/non-conventional/near-field-rf-coupling/
  macro: compute
- slug: fdtd-calibration-wall
  name: FDTD-to-Hardware Calibration Wall
  path: /sotf-site/compute/non-conventional/fdtd-calibration-wall/
  macro: compute
---
A class of analog optimisation computer that solves Ising-model problems by letting the physics of an oscillator network relax to its ground state. Same maths as a [Stochastic / Ising Machines](/sotf-site/compute/non-conventional/stochastic-ising-machines/) (the energy function is identical), but the dynamics are **deterministic** (parametric oscillators settling into a phase configuration) rather than stochastic (sampled bit flips). The substrate-class can be optical, electrical, or RF.

## Architecture (canonical)

The dynamics follow the slow-envelope ODE from Wang and Roychowdhury OIM 2019:

```
dA/dt = −Γ A + p(t) conj(A) + J A − α |A|² A + noise
```

- A: complex envelope of each oscillator
- Γ: damping (drives the system toward zero)
- p(t): parametric pump (drives gain, eventually binarises phases to ±1)
- J: coupling matrix (encodes the Ising problem)
- α: nonlinear saturation
- noise: thermal / quantum noise

The parametric pump binarises the phases (each oscillator settles to ±1), the J matrix encodes the problem, and the array's stable phase configuration encodes the ground-state spin configuration — the answer.

## Substrate classes

## Key distinction vs related computer classes

- **CIM vs p-computer ([Stochastic / Ising Machines](/sotf-site/compute/non-conventional/stochastic-ising-machines/)):** CIM is deterministic, the system has one natural ground state and relaxes there. p-computer is stochastic, the system samples many configurations and you collect statistics. Speed regime differs: CIM in nanoseconds, p-computer in microseconds to milliseconds for the same Ising problem.
- **CIM vs quantum annealer:** Same problem class (Ising minimisation), different physics. Quantum annealer exploits tunneling through energy barriers; CIM uses dissipation to drive to the lowest stable phase configuration. Quantum annealers need cryogenics; CIM doesn't.
- **CIM vs digital annealer (Toshiba SBM, Fujitsu DA):** Digital annealers simulate the Ising dynamics on classical hardware (FPGA / GPU cluster) at millisecond scale. CIM runs the dynamics in physics at nanosecond scale.
- **CIM vs [Thermodynamic Computing](/sotf-site/compute/non-conventional/thermodynamic-computing/):** Thermodynamic computers (Extropic, Normal Computing) use thermal noise as the compute resource — stochastic sampling. CIM uses dissipation to drive to a deterministic minimum.

## The calibration problem

The historical analog computing graveyard (Mythic AI, HP Labs memristor, Lightelligence) is largely populated by companies that died on this gap. See [FDTD-to-Hardware Calibration Wall](/sotf-site/compute/non-conventional/fdtd-calibration-wall/).

## Sources

<!-- dataview block stripped for public site -->
