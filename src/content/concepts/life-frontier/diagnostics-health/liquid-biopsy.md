---
type: concept
slug: liquid-biopsy
canonical_name: Liquid Biopsy
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- diagnostics-health
related_concepts: []
companies_using:
- angle-plc
- biofidelity
- bluestar-genomics
- burning-rock-biotech
- chronix-biomedical
- dna-script-cfdna-synthesis-tools-for-lbx-workflows
- earli
- exact-sciences
- foundation-medicine-roche
- geneseeq-technology
- genoptix-novartis-spin-out-now-clearnote-health
- grail
- guardant-health
- illumina
- inivata-neogenomics
- lexent-bio
- mainz-biomed-partnership-with-thermo-fisher-for-liquid-biops
- menarini-silicon-biosystems
- novogene
- nucleix
- oncobiologics-champions-oncology-now-precipio-diagnostics
- personal-genome-diagnostics-pgdx-now-part-of-labcorp
- singlera-genomics
- sysmex-inostics
- volition
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


# Liquid Biopsy

*Kind: technology*

## Physics / mechanism

Liquid biopsy detects circulating tumour DNA (ctDNA), circulating tumour cells (CTCs), exosomes, or cell-free RNA in peripheral blood, urine, or CSF — avoiding surgical tissue access. ctDNA fragments (~160 bp) are isolated via ultracentrifugation or size-exclusion, then sequenced (ddPCR, NGS, or methylation arrays). Key parameters: variant allele frequency (VAF) sensitivity floor ~0.01–0.1% for leading platforms; turnaround 3–7 days; specificity varies with tumour shedding rate. State of the art: Foundation Medicine's FoundationOne Liquid CDx, Guardant360, and GRAIL's Galleri (multi-cancer early detection via methylation signatures, ~50 cancer types, sensitivity 67% at >1.4% specificity).

## Competitive landscape

Tissue biopsy remains gold standard — higher tumour DNA yield, spatial heterogeneity data, direct histology. Competing molecular approaches: imaging (PET/CT, MRI) for structural detection; proteomics-based serum markers (PSA, CA-125) — cheaper but lower specificity. Within liquid biopsy, ddPCR competes on sensitivity for known variants; NGS panels compete on breadth. Emerging: single-molecule sequencing (PacBio, ONT) for long-read methylation phasing. GRAIL vs. Exact Sciences (Oncotype) vs. Guardant is the core commercial contest.

## Cloudberry relevance

| Approach | Sensitivity (early-stage) | Cost | Throughput |
|---|---|---|---|
| ctDNA NGS | Moderate (~55–70%) | $1,000–5,000 | High |
| CTC capture | Low–moderate | $500–2,000 | Low |
| Methylation array | High (~67% multi-cancer) | $2,000–6,000 | Medium |


Cloudberry relevance is upstream: liquid biopsy throughput and sensitivity are gated by semiconductor and photonics infrastructure. Nanopore sequencing chips, integrated photonic flow cytometry for CTC enumeration, and low-noise CMOS sensors for single-molecule fluorescence are direct deep-tech entry points. GlobalFoundries' specialty process nodes (FDX, photonic PDK) could serve biosensor ASIC or integrated optic readout suppliers — a credible fabless biosemiconductor deal-flow angle worth tracking.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
