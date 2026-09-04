---
type: concept
slug: quantum-software
canonical_name: Quantum Software
aliases: []
kind: technology
parent_concepts:
- compute
- quantum-computing
related_concepts: []
sources:
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2026-06-08-quantum-roadmap-funded-not-demand-funded-quantum-computing]]'
scorecard:
  viability: null
  drivers: null
  novelty: null
  diffusion: null
  impact: null
  timing_band: Unclear
  verdict: ''
scorecard_status: draft
mention_count: 32
sources_7d: 0
sources_30d: 6
recent_mentions:
- slug: 2026-06-08-quantum-roadmap-funded-not-demand-funded-quantum-computing
  title: Quantum Computing Startup Funding 2025-2026 – New Market Pitch
  date: '2026-06-08'
  kind: web
- slug: 2024-12-16-willow-and-the-race-to-quantum-advantage
  title: Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)
  date: '2024-12-16'
  kind: substack
neighbors: []
---
**Quantum software is the engineering layer between quantum algorithms and quantum hardware, compilers, testing frameworks, provenance and CI/CD, and a 2026 wave of work shows it is currently immature enough that correct-looking quantum programs can be silently wrong.**

## Summary

Quantum software is not the algorithms themselves. It is the stack that turns an algorithm into something that executes on a real device: SDKs and frameworks (Qiskit, Cirq, PennyLane, Qrisp, TensorCircuit-NG), transpilers that map an abstract circuit onto a device's native gate set and coupling graph, simulators that stand in for hardware, decoders that process error-correction syndromes, and the surrounding software engineering apparatus of testing, benchmarking, provenance capture and continuous integration. The field now calls itself quantum software engineering and has begun to acquire its own courses, benchmarks and security rubrics.

The mechanics that make this hard are specific to the paradigm. Programs are probabilistic, so a single run tells you little. Many important programs have no known correct answer to compare against: a variational quantum eigensolver computes a ground-state energy that is itself unknown, which is the oracle problem in testing terms. The compiled artefact is not stable: an unchanged circuit can transpile into a different physical realisation after a change in SDK version, basis gates, coupling map or backend description, altering depth, gate composition and qubit mapping. And results depend on a long tail of interacting choices, ansatz, Hamiltonian, optimiser, backend, shot count, noise model, mitigation method, random seed, stopping criteria and software versions, which in current practice are scattered across code, configs, logs and papers.

The parameters that decide whether this layer matters are: whether quantum hardware ever reaches the point where application results are worth auditing; whether the toolchains converge on shared contracts rather than fifteen incompatible provider APIs; and whether verification catches the class of bug that invalidates a scientific claim. The last is not hypothetical. A semantics-first audit of a compilable Shor oracle for the elliptic-curve discrete logarithm problem built on Qrisp found that the core point-update primitive agreed with a classical reference on well-formed inputs, yet controlled execution violated the expected control law under the evaluated toolchain, despite passing a trivial control sanity check. Resource estimates for breaking cryptography are built on oracles like this one.

## Viability (unscored)

## Drivers (unscored)

## Novelty (unscored)

## Diffusion (unscored)

## Impact (unscored)

## Timing Unclear

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
