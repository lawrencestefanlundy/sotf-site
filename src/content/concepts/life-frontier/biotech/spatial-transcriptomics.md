---
type: concept
slug: spatial-transcriptomics
canonical_name: Spatial Transcriptomics
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
- agilent-technologies
- akoya-biosciences
- bgi-genomics-stomics
- bioptigen-leica-biosystems-danaher
- bioxcel-therapeutics-ultivue
- bruker
- cartana-acquired-by-10x-genomics
- curio-bioscience
- molecula-now-part-of-parse-biosciences
- nanostring-technologies
- nuvation-bio-novaseq-based-spatial-startups-miltenyi-biotec
- omnitura-therapeutics
- panomic-bio
- pixel-genomics
- resolve-biosciences
- scilifelab-spatial-omics-sweden-academic-industry-hub
- singular-genomics
- spatial-biology-biopharma-ai-singlera-genomics
- spatial-transcriptomics-acquired-by-10x-genomics
- synectics-bio-scinai-former-kamedis-spin
- tissue-biosciences
- visiopharm
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

# Spatial Transcriptomics

*Kind: technology*

## Physics / mechanism

Spatial transcriptomics maps gene expression while preserving the physical coordinates of cells within tissue. Sequencing-based methods (10x Genomics Visium, Slide-seq) capture mRNA by hybridising transcripts to spatially barcoded arrays; imaging-based methods (MERFISH, seqFISH+, Xenium) use iterative fluorescent in-situ hybridisation cycles to resolve individual transcripts optically. Key parameters: spatial resolution (Visium ~55 µm spots vs. Xenium sub-cellular ~200 nm), gene panel size (targeted panels 300–5,000 genes vs. whole-transcriptome sequencing), and throughput (tissue area per run, cost per mm²). Current frontier: single-cell resolution across cm²-scale tissue sections, with multiplexed protein co-detection emerging.

## Competitive landscape

Sequencing-based and imaging-based platforms compete directly on resolution vs. throughput trade-off. Adjacent: single-cell RNA-seq (no spatial context), multiplexed immunofluorescence (protein-level, not transcriptomic), and spatial proteomics (e.g., Deep Visual Proteomics). CRISPR spatial screens are an emerging orthogonal approach.

## Cloudberry relevance

| Method | Resolution | Gene Coverage | Cost/run |
|---|---|---|---|
| 10x Visium HD | 8 µm bins | Whole transcriptome | ~$800 |
| 10x Xenium | Sub-cellular | ~5,000 genes | ~$1,500 |
| MERFISH (Merscope) | Single-cell | ~1,000 genes | ~$2,000 |


Cloudberry relevance sits in the instrumentation stack, not biology. Spatial transcriptomics instruments are photonics-intensive: high-NA fluorescence optics, laser multiplexing, SPAD or sCMOS detector arrays, and microfluidic flow cells. GF-compatible photonic integrated circuits could replace bulk optics in next-gen benchtop instruments, reducing cost and form factor. Deal-flow angle: fabless instrument startups needing semiconductor photonics foundry partners, detector ASIC designers, and microfluidic chip manufacturers — all within Cloudberry's strike zone.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
