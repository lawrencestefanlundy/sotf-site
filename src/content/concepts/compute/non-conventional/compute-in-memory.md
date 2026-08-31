---
type: concept
slug: compute-in-memory
canonical_name: Compute in Memory
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
frontier:
- How many stable, retention-verified conductance levels do opto-electronic resistive memories achieve per device, and what bit-equivalent precision does that give a crossbar multiply-accumulate?
- What is the measured energy per operation and insertion loss penalty of a photonic in-memory compute tile relative to an electronic resistive crossbar of the same weight count?
- Are the memory materials in these devices compatible with standard silicon photonics back-end thermal budgets and foundry process flows, and at what yield?
- Does any funded company, rather than an academic group, have a compute-in-memory product shipping into the edge silicon demand identified in Q2 2026?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
neighbors: []
---
## Physics / mechanism

Compute in memory places arithmetic where data already resides, removing the round trip between a separate memory array and a logic unit. The canonical primitive is a resistive crossbar: programmable conductances hold matrix weights, applied voltages act as the input vector, and the summed currents on each column perform a multiply-accumulate in the analogue domain. Non-volatility matters because weights must persist without refresh or standby power, so the array can be read repeatedly at low energy per operation.

The photonic variant of this idea is the subject of the available source material. Photonic integrated circuits offer large bandwidth, low latency and inherent parallelism for communication, sensing and information processing, but lack efficient, scalable, non-volatile memory elements on chip emerging non volatile opto electronic resistive memories for. Opto-electronic resistive memories are proposed as the missing element: a device whose resistance state, and hence optical response, can be set electrically or optically and retained without power, allowing weights to be stored in the same structure that modulates the light carrying the data.

Key parameters for any such device family are the number of distinguishable conductance or transmission states, retention and endurance, switching energy, the insertion loss added to the photonic path, and whether programming is compatible with foundry back-end processing. The source frames the problem as one of efficiency, scalability and non-volatility simultaneously, which implies that partial solutions on any one axis have not been sufficient emerging non volatile opto electronic resistive memories for.

## Competitive landscape

The sources support only a narrow comparison: electronic resistive memory arrays versus opto-electronic resistive memories embedded in photonic integrated circuits. The photonic route is motivated by bandwidth, latency and parallelism advantages of the optical domain, and is bottlenecked by the absence of a suitable non-volatile memory element rather than by the arithmetic itself emerging non volatile opto electronic resistive memories for. No comparative performance data across device stacks is present in the supplied material.

For funding context, semiconductor startup capital in the quarter was concentrated in AI hardware, with edge silicon re-emerging on physical-AI and real-time on-device demand semiengineering startup funding q2 2026. Compute in memory is usually pitched into that edge and datacentre-accelerator demand, but the source does not name compute-in-memory companies.

## Evidence base

- Photonic integrated circuits are identified as a platform for high-speed communication, sensing and information processing on the basis of large bandwidth, low latency and inherent parallelism, published 2 June 2026 emerging non volatile opto electronic resistive memories for.
- The same review states that efficient, scalable and non-volatile memory is absent from the photonic platform, positioning it as the limiting gap for next-generation photonic ICs emerging non volatile opto electronic resistive memories for.
- The work is a cross-institution effort spanning North Carolina State University, IIT Indore and Hewlett Packard Labs' Large-Scale Integrated Photonics Laboratory, indicating industrial as well as academic interest in opto-electronic resistive memory emerging non volatile opto electronic resistive memories for.
- In Q2 2026, 80 semiconductor startups raised over $6.0B, down from $8.4B across 80 startups in Q1 2026, with AI hardware still dominant and edge silicon re-emerging on physical-AI and on-device demand semiengineering startup funding q2 2026.

## Frontier (open questions)

- How many stable, retention-verified conductance levels do opto-electronic resistive memories achieve per device, and what bit-equivalent precision does that give a crossbar multiply-accumulate?
- What is the measured energy per operation and insertion loss penalty of a photonic in-memory compute tile relative to an electronic resistive crossbar of the same weight count?
- Are the memory materials in these devices compatible with standard silicon photonics back-end thermal budgets and foundry process flows, and at what yield?
- Does any funded company, rather than an academic group, have a compute-in-memory product shipping into the edge silicon demand identified in Q2 2026?

*Synthesised 2026-08-31 from 2 KB sources by the resynth pipeline; citations are KB source slugs.*
