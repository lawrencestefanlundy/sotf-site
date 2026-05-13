---
type: concept
slug: cell-free-systems
canonical_name: Cell-Free Systems
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- biotech
related_concepts: []
companies_using:
- arbor-biosciences
- arcturus-bioscience
- biomilq
- bioneer
- cellectis
- cellfree-sciences
- enzymit
- genomatica
- greenlight-biosciences
- inari-agriculture
- iosbio-formerly-oxford-biomedica-solutions
- jeane-bio
- kairos-therapeutics
- leniobio
- molecular-assemblies
- newcells-biotech
- scinai-immunotherapeutics
- stemloop
- synthecon
- synvitrobio
- tierra-biosciences
- touchlight
- viral-vectors-labs-vvl
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Cell-Free Systems

*Kind: technology*

## Physics / mechanism

Cell-free systems (CFS) execute biological synthesis — proteins, nucleic acids, small molecules — outside living cells. The core machinery is a cell extract (typically *E. coli*, wheat germ, or CHO-derived) containing ribosomes, tRNA, polymerases, and co-factors, supplemented with an energy regeneration system (phosphocreatine, 3-PGA) and a DNA or mRNA template. Reaction volume spans nanolitres to litres. Protein yields have reached 2–4 mg/mL in optimised *E. coli* PURE-system batches; wheat-germ platforms hit ~1 mg/mL with eukaryotic folding fidelity. Synthesis cycles run 2–8 hours. Key parameters: ATP regeneration rate, template concentration, chaperone availability, and redox balance. Commercial platforms: Sutro Biopharma, Synvitrobio, Arbor Biosciences, New England Biolabs.

## Competitive landscape

Cell-based expression (CHO, HEK293, yeast) dominates industrial protein manufacture — lower COGS at scale but 2–6 week development cycles and containment overhead. CFS trades unit economics for speed, programmability, and open-reaction access. Adjacent: ribosome display and mRNA display (selection, not production); solid-phase peptide synthesis (short peptides only, no folded domains); and microfluidic droplet encapsulation, which can host CFS reactions at femtolitre scale. The hardest competitive moat question is whether CFS yield economics close enough to justify platform switching for therapeutic proteins beyond early discovery.

## Cloudberry relevance

| Approach | Throughput | Complexity limit | Cycle time |
|---|---|---|---|
| Cell-free (extract) | Medium | Full-length proteins | Hours |
| CHO/HEK cell culture | High | Complex glycoproteins | Weeks |
| SPPS | Low | ~50 AA unfolded | Hours |


Cloudberry relevance sits at the hardware and instrumentation layer, not the biology. CFS workflows demand precise temperature control, nanolitre dispensing, and integrated optical readout — creating pull for photonic biosensors, microfluidic chips, and custom ASIC-controlled synthesis reactors. GlobalFoundries-compatible silicon photonics for label-free protein detection is a direct adjacency. Deal-flow angles: fabless instrument companies building CFS-native hardware, and semiconductor firms enabling high-density parallel synthesis arrays where photonic integration differentiates from incumbent plate-reader infrastructure.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
