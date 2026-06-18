---
type: concept
slug: in-memory-computing
canonical_name: In-Memory Computing
aliases:
- in-memory compute
kind: technology
parent_concepts:
- memory
- emerging-memory
related_concepts:
- memcapacitor
- analog-computing
- memory-wall
- von-neumann-bottleneck
- processing-in-memory
sources:
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
frontier:
- Does digital IMC plus 3D stacking close the energy gap before analog CIM scales out of the edge?
- Which analog-CIM device family (SRAM-analog, RRAM, flash, memcapacitor) reaches volume first?
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 33
descendants:
- adc-bottleneck
- analog-in-memory-compute
- capram
- charge-domain-compute
- digital-in-memory-compute
- processing-in-memory
- sram-cim
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 11
recent_mentions:
- slug: 2026-01-22-ai-chips-computeram-and-the-future
  title: 'AI Chips, ComputeRAM and the Future of Data Movement: A Conversation with Manu, Founder of Synthara'
  date: '2026-01-22'
  kind: substack
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-12-04-cubits-in-a-fridge-why-is-nobody
  title: Silicon Spin Quantum Computing (Feat. Himadri Majumdar, SemiQon)
  date: '2024-12-04'
  kind: substack
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2023-11-20-e21-can-we-make-enough-ai-chips
  title: Can we make enough AI chips?
  date: '2023-11-20'
  kind: substack
- slug: 2023-07-23-analog-computing-the-once-and-future
  title: '🔮 E09: Analog Computing: The Once and Future King'
  date: '2023-07-23'
  kind: substack
neighbors:
- slug: memcapacitor
  name: Memcapacitor
  path: /sotf-site/memory/emerging-memory/memcapacitor/
  macro: memory
- slug: analog-computing
  name: Analog Computing
  path: /sotf-site/compute/non-conventional/analog-computing/
  macro: compute
- slug: memory-wall
  name: The Memory Wall
  path: /sotf-site/compute/compute-architecture/memory-wall/
  macro: compute
- slug: von-neumann-bottleneck
  name: Von Neumann Bottleneck
  path: /sotf-site/compute/compute-architecture/von-neumann-bottleneck/
  macro: compute
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /sotf-site/memory/emerging-memory/processing-in-memory/
  macro: memory
---
## Physics / mechanism

Conventional compute separates memory and logic, forcing data across the von Neumann bottleneck—dominant cost in AI inference workloads. In-memory computing (IMC) embeds arithmetic directly in the memory array, typically using analog crossbar structures where Ohm's law and Kirchhoff's current summation perform matrix-vector multiplication (MVM) in O(1) time per layer. Key device substrates: SRAM-based digital IMC (Samsung, TSMC N5/N3), and analog non-volatile variants using PCM, RRAM, or OTS-based selectors. SRAM IMC achieves ~10–50 TOPS/W at 28–5nm; analog NVM claims 100+ TOPS/W but suffers weight precision limits (~4–6 bit effective), conductance drift, and write endurance constraints. Closest to productization: Mythic (RRAM), Syntiant (SRAM), Untether AI (SRAM near-memory).

## Competitive landscape

SRAM digital IMC is conservative but foundry-compatible and production-ready. Analog NVM IMC promises highest efficiency but requires custom fab and error-correction overhead. Near-memory compute (HBM + logic die, e.g., SK Hynix AiMX) is a softer alternative—no array-level compute but cuts bandwidth cost. PIM (Processing-in-Memory) from Samsung/SK overlaps significantly. Neuromorphic (Intel Loihi, IBM NorthPole) shares the co-location principle but targets spiking networks.

| Approach | TOPS/W | Precision | Foundry risk |
|---|---|---|---|
| SRAM IMC | 10–50 | 8-bit native | Low |
| Analog NVM IMC | 100+ | 4–6 bit effective | High |
| Near-memory (HBM+PIM) | 5–20 | Full | Low |

## Investment relevance (all routes)

In-memory compute attacks the [The Memory Wall](/sotf-site/compute/compute-architecture/memory-wall/) and [Von Neumann Bottleneck](/sotf-site/compute/compute-architecture/von-neumann-bottleneck/) directly; the open question is who captures the value, and through which vehicle.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Does digital IMC plus 3D stacking close the energy gap before analog CIM scales out of the edge?
- Which analog-CIM device family (SRAM-analog, RRAM, flash, memcapacitor) reaches volume first?
