---
type: concept
slug: printed-circuit-board
canonical_name: Printed Circuit Board
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2026-06-13-sovereign-electronics-manufacturing-the-achilles-heel-of]]'
- '[[2024-01-23-normal-computing-first-thermodynamic-computer]]'
- '[[2025-04-15-nature-comm-thermodynamic-computing-system]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 14
frontier:
- Can PCB-based reconfigurable surfaces retain the 100 GHz wideband performance demonstrated at prototype scale once switch parasitics and control routing are scaled to full apertures 2026 06 05 a 100 ghz wideband reconfigurable intelligent surface based ?
- Do buffer-parameterised surrogate models generalise to IC buffer technologies outside their training distribution without retraining, and with what error on eye height and eye width 2026 06 05 buffer parameterized machine learning surrogate models for c?
- What electron lifetime and coherence can monolithic PCB Paul traps reach, and does the 2.13 ms lifetime limit stem from board materials, vacuum or RF heating 2026 07 22 monolithic printed circuit board rf trap for electrons?
- What accuracy do current language models achieve on PCB-QA, and which design-file representations (schematic, netlist, layout, SPICE output) are the binding constraint 2026 06 24 pcb qa evaluating llms over the first printed circuit board ?
- At what distance and through what enclosure materials does reflective backscatter recovery of user activity remain reliable, and which PCB layout countermeasures suppress it 2026 07 27 nsf 2555491 collaborative research satc 20 res model?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-13-sovereign-electronics-manufacturing-the-achilles-heel-of
  title: The Achilles' heel of European defence—printed circuit board. Why environmental regulations are strangling PCB production in EU
  date: '2026-06-13'
  kind: web
- slug: 2025-04-15-nature-comm-thermodynamic-computing-system
  title: Thermodynamic computing system for AI applications
  date: '2025-04-15'
  kind: web
- slug: 2024-01-23-normal-computing-first-thermodynamic-computer
  title: Normal Computing Unveils the First-ever Thermodynamic Computer
  date: '2024-01-23'
  kind: web
- slug: 2023-08-31-e13-chiplets-how-chip-lego-is-driving
  title: '🔮 E13: Chiplets - How Chip Lego is Driving AI Progress'
  date: '2023-08-31'
  kind: substack
neighbors: []
---
## Physics / mechanism

A printed circuit board is a laminated substrate carrying patterned copper conductors (traces) on one or more layers, used to interconnect and mechanically support electronic components. Layer count is the primary complexity and cost driver: double-layer boards restrict routing to planar graphs, while dense interconnection between many nodes forces multi-layer stacks and raises fabrication difficulty low complexity planar beyond diagonal ris architecture desig. Graph theory can be used to characterise which interconnection topologies are realisable without crossings, and hence on double-layer boards low complexity planar beyond diagonal ris architecture desig.

At high frequency, PCB traces stop behaving as ideal wires and become transmission lines and radiating structures. Signal integrity analysis of PCB interconnects predicts metrics such as inner eye contour, eye height, eye width and transient waveform features, and depends jointly on board parameters and on the driving IC buffer's clock frequency, supply voltage, rise and fall times, jitter, and internal resistors and capacitors, plus manufacturing tolerances buffer parameterized machine learning surrogate models for c. The same electromagnetic behaviour is a security liability: illuminating a device with a low-power radio signal from several meters away lets an attacker measure reflections scattered from internal cables and PCB traces, whose amplitude varies with user activity, enabling recovery of typing or other actions without line of sight nsf 2555491 collaborative research satc 20 res model.

Because copper patterning on a dielectric is cheap, dimensionally controlled and scalable, PCBs are increasingly used as the functional physical layer of devices rather than only as interconnect. Examples in the sources include RLC circuits as unit cells on a printed circuit board operated as a parallelised Langevin sampler in a continuous-variable thermodynamic computer nature comm thermodynamic computing system; a radio-frequency photonic higher-order topological metasurface of split-ring resonators verified experimentally at 1.5 to 1.7 GHz higher order topological metasurface based on split ring res; and a monolithic single-board Paul trap for electrons requiring no assembly, whose rigid design minimises manufacturing intolerances, reaching trapped-electron lifetimes of 2.13 ms and secular frequencies up to 90 MHz monolithic printed circuit board rf trap for electrons.

Pushing PCB technology to sub-terahertz frequencies is constrained by fabrication limits, limited switch availability, switch size relative to the unit cell, switch parasitics and control complexity; a wideband PCB-based reconfigurable intelligent surface operating around 100 GHz was demonstrated using orthogonal-polarisation slot-coupled patch structures and sub-array partitioning a 100 ghz wideband reconfigurable intelligent surface based .

## Competitive landscape

PCB fabrication sits below integrated-circuit processes in resolution but far above them in cost per unit area, which is why it is chosen for large-area RF structures, resonator arrays and trap electrodes where feature sizes of hundreds of micrometres suffice. For reconfigurable intelligent surfaces, standard PCB technology is described as attractive for its low cost and scalability, with the trade-off being fabrication and switch-integration limits at around 100 GHz a 100 ghz wideband reconfigurable intelligent surface based . Within PCB design itself, the trade-off is layer count versus achievable degrees of freedom: planar-connected beyond-diagonal RIS architectures give up interconnection richness in exchange for double-layer manufacturability low complexity planar beyond diagonal ris architecture desig.

Design automation for PCBs lags that for integrated circuits. Generative AI work in hardware has concentrated on IC design automation with hardware description languages, while PCB coverage across supply chain, specification, circuit design, layout, validation, test and assembly is only now being surveyed and taxonomised surveying genai based automation in printed circuit board de. Text-based PCB datasets for evaluating language models were absent until PCB-QA pcb qa evaluating llms over the first printed circuit board .

## Evidence base

- A continuous-variable thermodynamic computer used RLC circuits as unit cells on a printed circuit board, run as a parallelised Langevin sampler, published in Nature Communications on 15 April 2025 nature comm thermodynamic computing system.
- A monolithic single-PCB Paul trap for electrons, requiring no assembly, reported trapped-electron lifetimes of 2.13 ms and secular frequencies up to 90 MHz (22 July 2026) monolithic printed circuit board rf trap for electrons.
- A wideband PCB-based reconfigurable intelligent surface operating around 100 GHz was demonstrated using orthogonal polarisation and sub-array partitioning, against fabrication and switch-parasitic limits (published 24 May 2026) a 100 ghz wideband reconfigurable intelligent surface based .
- Graph theory was used to identify which beyond-diagonal RIS architectures are realisable on double-layer PCBs, and which of those retain the most degrees of freedom (4 May 2026) low complexity planar beyond diagonal ris architecture desig.
- PCB-QA, described as the first text-based PCB design question-answer dataset, comprises 480 manually created question-answer pairs derived from 8 open-source hardware projects, covering component connections, datasheet examination and SPICE simulation data (24 June 2026) pcb qa evaluating llms over the first printed circuit board .
- Two NSF SaTC awards of $299,999 and $300,000 dated 25 July 2026 fund modelling and mitigation of reflective backscatter side channels arising from internal cables and PCB traces nsf 2555492 collaborative research satc 20 res model nsf 2555491 collaborative research satc 20 res model.
- Europe's share of global bare board PCB production is reported to have fallen from 16% in 2000 to roughly 2.3% in 2022, attributed in part to regulatory barriers on domestic capacity (13 June 2026, low-tier industry source) sovereign electronics manufacturing the achilles heel of.

## Frontier (open questions)

- Can PCB-based reconfigurable surfaces retain the 100 GHz wideband performance demonstrated at prototype scale once switch parasitics and control routing are scaled to full apertures a 100 ghz wideband reconfigurable intelligent surface based ?
- Do buffer-parameterised surrogate models generalise to IC buffer technologies outside their training distribution without retraining, and with what error on eye height and eye width buffer parameterized machine learning surrogate models for c?
- What electron lifetime and coherence can monolithic PCB Paul traps reach, and does the 2.13 ms lifetime limit stem from board materials, vacuum or RF heating monolithic printed circuit board rf trap for electrons?
- What accuracy do current language models achieve on PCB-QA, and which design-file representations (schematic, netlist, layout, SPICE output) are the binding constraint pcb qa evaluating llms over the first printed circuit board ?
- At what distance and through what enclosure materials does reflective backscatter recovery of user activity remain reliable, and which PCB layout countermeasures suppress it nsf 2555491 collaborative research satc 20 res model?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
