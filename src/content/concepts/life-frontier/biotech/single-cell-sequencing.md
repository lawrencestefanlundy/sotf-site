---
type: concept
slug: single-cell-sequencing
canonical_name: Single-Cell Sequencing
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
- 10x-genomics
- bd-biosciences
- bgi-genomics-mgi-tech
- bioskryb-genomics
- cartana-acquired-by-10x-genomics
- cellenion
- curio-bioscience
- droplet-genomics
- fluent-biosciences
- genome-biologics
- illumina
- nanostring-technologies-acquired-by-bruker
- omniscope
- oxford-nanopore-technologies
- pacific-biosciences-pacbio
- parse-biosciences
- proteintech-chromotek
- readcoor-acquired-by-10x-genomics
- rebus-biosystems
- resolve-biosciences
- scale-biosciences
- singleron-biotechnologies
- singular-genomics
- takara-bio
- vizgen
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

# Single-Cell Sequencing

*Kind: technology*

## Physics / mechanism

Single-cell sequencing resolves genomic, transcriptomic, or epigenomic information at the resolution of individual cells rather than bulk averages. The dominant workflow: cell isolation (microfluidics, droplet-based or combinatorial barcoding), lysis, reverse transcription (for scRNA-seq), library prep, and short- or long-read sequencing. Key parameters — cell capture rate (typically 50–80%), doublet rate (<5% target), UMI sensitivity (~1,000–5,000 genes/cell for 10x Chromium), and throughput (10x Chromium X: ~20k cells/run, Parse Biosciences: ~1M+ cells/run). Long-read single-cell (PacBio MAS-seq, Oxford Nanopore) now resolves full-length isoforms. Cost sits ~$0.01–0.05/cell at scale; sensitivity is the persistent engineering constraint.

## Competitive landscape

The primary competitive axis is spatial vs. non-spatial resolution. Bulk RNA-seq loses cell identity; spatial transcriptomics (10x Visium, Vizgen MERFISH, Nanostring CosMx) adds positional context but sacrifices throughput or depth. Proteomics alternatives: mass cytometry (CyTOF) and CITE-seq (protein + RNA co-measurement). Microfluidic competitors include Becton Dickinson Rhapsody and Fluent BioSciences PIP-seq. CRISPR-based perturbation screens (Perturb-seq) extend the modality into functional genomics.

## Cloudberry relevance

| Approach | Resolution | Spatial context | Throughput |
|---|---|---|---|
| scRNA-seq (droplet) | Single cell | None | High |
| Spatial transcriptomics | Sub-cellular | Yes | Medium |
| Mass cytometry | Single cell | None | Medium |


Cloudberry relevance sits in the enabling hardware layer, not the assay biology. Microfluidic chip fabrication (MEMS, nanofabrication), photonic integrated circuits for on-chip fluorescence detection, and ASIC/FPGA read-processing are all semiconductor-adjacent. GlobalFoundries-LP fund could see deal flow in photonic biosensor startups, microfluidic foundry plays, or edge sequencing compute. Lunar Ventures' software-first lens applies to single-cell data infrastructure — compression, multimodal alignment, foundation models trained on cell atlases. The instrumentation-to-data pipeline is the durable margin layer.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
