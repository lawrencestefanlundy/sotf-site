---
type: concept
slug: magneto-optical
canonical_name: Magneto-Optical Memory
aliases:
- magneto-optic
- magnetooptical
- MO
- MO switching
- magneto-optical switching
- magneto-optical recording
- all-optical magnetic switching
- AOMS
- opto-magnetism
- ultrafast magnetism
- magneto-photonic
parent_concepts:
- spintronics
related_concepts:
- all-optical-switching
- photonic-memory
- hamr
- thin-film-magnetics
- magnetic-tunnel-junction
sources:
- '[[2026-04-29-optical-dram-everspin-reports-q1-2026-financial-results]]'
- '[[2024-10-23-optical-dram-integrated-non-reciprocal-magneto-optics-with]]'
- '[[2024-08-30-optical-dram-integrated-magneto-photonic-non-volatile-multi]]'
- '[[2026-04-20-optical-dram-photonic-memory-device-technology-2026-patsnap]]'
- '[[2026-05-07-optical-dram-startup-funding-q1-2026]]'
scorecard:
  viability: 2
  drivers: 2
  novelty: 3
  diffusion: 2
  impact: null
  timing_band: Later (5-10yr)
  verdict: Too early to say
scorecard_status: draft
mention_count: 23
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-05-07-optical-dram-startup-funding-q1-2026
  title: 'Startup Funding: Q1 2026'
  date: '2026-05-07'
  kind: web
- slug: 2026-04-29-optical-dram-everspin-reports-q1-2026-financial-results
  title: Everspin Reports Q1 2026 Financial Results
  date: '2026-04-29'
  kind: web
- slug: 2026-04-20-optical-dram-photonic-memory-device-technology-2026-patsnap
  title: Photonic Memory Device Technology 2026 — PatSnap Eureka
  date: '2026-04-20'
  kind: web
- slug: 2024-10-23-optical-dram-integrated-non-reciprocal-magneto-optics-with
  title: Integrated non-reciprocal magneto-optics with ultra-high endurance for photonic in-memory computing
  date: '2024-10-23'
  kind: web
- slug: 2024-08-30-optical-dram-integrated-magneto-photonic-non-volatile-multi
  title: Integrated magneto-photonic non-volatile multi-bit memory
  date: '2024-08-30'
  kind: web
neighbors:
- slug: all-optical-switching
  name: All-Optical Switching
  path: /memory/emerging-memory/all-optical-switching/
  macro: memory
- slug: photonic-memory
  name: Photonic Memory
  path: /memory/emerging-memory/photonic-memory/
  macro: memory
- slug: hamr
  name: Hamr
  path: /memory/mainstream-memory/hamr/
  macro: memory
- slug: thin-film-magnetics
  name: Thin Film Magnetics
  path: /materials/functional-layers/thin-film-magnetics/
  macro: materials
- slug: magnetic-tunnel-junction
  name: Magnetic Tunnel Junction (MTJ)
  path: /memory/emerging-memory/magnetic-tunnel-junction/
  macro: memory
---
**Magneto-optical memory stores bits in the magnetisation of a material and writes or reads them with light on a photonic chip; cell-level demonstrations and wafer-scale garnet films on silicon now exist, but nothing resembling an addressable array does.**

## Summary

Magneto-optical (MO) memory combines two mature ideas. The storage element is magnetic and therefore non-volatile: a magnetic tunnel junction, a ferrimagnetic garnet film, or a two-dimensional magnet. The access mechanism is optical: light either flips the magnetisation directly (all-optical switching, typically with femtosecond pulses) or senses it through the Faraday and Kerr effects, in which magnetisation rotates the polarisation of transmitted or reflected light. Put on a photonic integrated circuit, the appeal is that a photonic processor could keep its weights or state in place without converting to the electrical domain to read or write them.

## Viability (2/5)

**TLDR: Working single cells and wafer-scale films; no addressable array and no solution to sub-diffraction addressing.**

## Drivers (2/5)

On the supply side there is a coherent push: wafer-scale garnet on silicon with the metrology needed to qualify it, a steady flow of magnetic-materials work that improves the underlying switching physics (strain tuning of demagnetisation in a room-temperature van der Waals ferromagnet, with 1.2% tensile strain cutting demagnetisation time by about 20%; magnetically switchable chiral second-harmonic emission with remanent states in bilayer CrSBr), and adjacent chip-scale light modulation capability such as a non-suspended push-pull TFLN acousto-optic modulator at 1.004 V cm and 132.5 MHz bandwidth.

On the demand side the evidence points elsewhere. Money is flowing into photonic compute boxes with integrated memory (Olix raised $220M Series A for an optical tensor processing unit with integrated memory <sup class="ref"><a href="https://semiengineering.com/startup-funding-q1-2026/" title="Startup Funding: Q1 2026" rel="noopener">ref</a></sup>) and into electrically-addressed MRAM, where Everspin reported 238 design wins in 2025 ramping to production <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/0001438423/000162828026028376/mram-20260331xexx991.htm" title="Everspin Reports Q1 2026 Financial Results" rel="noopener">ref</a></sup>. Neither is a customer asking for optically addressed magnetic memory; both are plausible acquirers of the IP. Score 2 because pull is inferred, not observed.

**TLDR: Supply-side materials and metrology progress is genuine; the sources show no demand pull for MO memory specifically.**

## Novelty (3/5)

**TLDR: One quantified 100x speed advantage over incumbent photonic memory, with an unnamed comparator and no comparison against electronic memory.**

## Diffusion (2/5)

**TLDR: The garnet process is heading for isolators, not memory; MO memory has no product channel in the sources.**

## Impact (unscored)

A score here would be invented. It is left null deliberately. The specific numbers that would allow one are listed in the open questions.

**TLDR: The sources do not size the system-level gain or the market, so no defensible score.**

## Timing Later (5-10yr)

Even on an optimistic reading in which that milestone clears in 2027, the path from a sub-diffraction single-cell write to an array with characterised read margin, retention and yield is a multi-year programme, and the sources give no evidence that any organisation is running one. Later (5-10yr) is the honest band for a memory product; anyone promising sooner should be asked for the addressing scheme.

## Overrated or underrated? Too early to say

## Prediction

## Evidence base

## Open questions

---
*Assessment drafted 2026-08-31 from up to 11 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
