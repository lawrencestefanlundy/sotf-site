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
frontier:
- Does anyone demonstrate integrated, on-chip sub-diffraction magneto-optical addressing? This is the field-wide open gap and the single observable that converts the density argument from physics-in-principle into a device.
- Does optical (not electrical/Hall) readout of a magnetic bit get integrated on a PIC? The strongest demo in the class (arXiv 2511.02440) still reads out electrically.
- Is the integration process cornerable by a startup, or is it the kind of process moat only a capex-heavy incumbent holds?
last_updated: '2026-07-15'
tags:
- concept
- core-concept
descendants:
- all-optical-switching
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
The memory medium where **the bit is a magnetic domain, not an optical mode**. Light is used to write (and ideally read) the state, but the state itself lives in magnetisation. This distinction is the whole reason the concept matters, and it is the core of **Optical Dram**.

## Why the distinction is load-bearing

Store-it-in-light memory (optical modes, resonators, PCM in a waveguide) is confined by the diffraction limit: the bit cannot be much smaller than roughly the wavelength, which puts the cell around 750 nm and up, orders of magnitude away from a DRAM cell. That density ceiling is the standard, correct reason to dismiss optical memory as cache-only.

Magneto-optical escapes the miniaturisation leg of that ceiling. Magnetic domains are nm-scale and can in principle be addressed sub-diffraction; **HAMR is the shipped precedent** (Seagate's near-field transducer takes an 830 nm source to a ~35 nm spot, in a product). What it concedes is multiplexing: a magnetic domain is stateful and cannot be wavelength-multiplexed the way light in a waveguide can.

So the density argument is a trade, not a free win, and the binding constraint moves from the medium to the **addressing**: how one diffraction-limited optical port serves many nanoscale domains on a photonic IC. Nobody has shown this integrated and at scale. Racetrack/domain-wall shifting is proposed in the literature as the route, not demonstrated.

## State of the art (as of Jul 2026)

**The field-wide gap: optical readout integration.** Everyone can write with light. Reading the bit back optically, on-chip, at density, is unshown.

## Research lineage

**Corrected 15 Jul 2026 by the sourcing sprint** (optical dram lab map). The prior KB claim — that a Dutch axis is the whole field, with TU/e producing AIMA and Radboud producing MemStera — is wrong twice over.

There are **two disjoint communities that barely co-author**, and they own opposite halves of the product:

| | Optical WRITE | Optical READ |
|---|---|---|
| **TU Eindhoven** (Koopmans, Lavrijsen, Jiao) + LioniX | On-chip AOS, Co/Gd on SiN waveguide, 90% contrast at 500 nm (arXiv 2511.02440) | No. Readout is electrical (Hall). |
| **UCSB / Pittsburgh** (Pintus, Youngblood, Bowers) + AIST/Tokyo Tech | No. Write is an integrated gold electromagnet. | Ce:YIG on Si microring, **2.4 billion cycles, ~1 ns, 143 fJ/bit** (Nature Photonics 2025) |

Nobody has demonstrated optical write **and** optical read of a sub-diffraction magnetic bit on chip. The gap is not closed — but both halves exist, in labs on different continents with no incentive to combine. That is the sprint's central structural finding.

**IP caution:** Radboud's AOS estate likely traces to **SPICE** (EU Horizon 2020 FET-Open), co-partied with **Aarhus, imec and CEA-Spintec**, and rated "Excellent Innovation" by the EC Innovation Radar in Feb 2021. Any licence may carry co-rights. Unresolved; needs an Espacenet inventor search.

## Position

Full argument, sizing, and the capture risk: **Optical Dram**.
