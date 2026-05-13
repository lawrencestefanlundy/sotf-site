---
type: concept
slug: digital-pathology
canonical_name: Digital Pathology
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
- 3dhistech
- aiforia-technologies
- aignostics
- aiosyn
- contextvision
- deep-bio
- gradient-health
- hamamatsu-photonics
- histolab-part-of-visiopharm
- histowiz
- ibex-medical-analytics
- keen-eye-technologies
- leica-biosystems-danaher
- lunit
- magen-medical
- mindpeak
- nucleai
- paigeai
- pathai
- pathomics-now-part-of-roper-technologies-clarapath
- philips-digital-pathology
- pixelgen-technologies
- proscia
- tribun-health
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


# Digital Pathology

*Kind: technology*

## Physics / mechanism

Digital pathology converts glass histology slides into high-resolution whole-slide images (WSIs) via brightfield or fluorescence scanning at 20×–40× magnification (0.25–0.5 µm/pixel). Scanners use line-scan CMOS sensors, precision z-stack autofocus, and stitching algorithms to produce 1–4 GB TIFF/SVS files per slide. AI inference layers (CNNs, vision transformers) then perform cell segmentation, biomarker quantification, and grading. Current SOTA: Philips IntelliSite, Leica Aperio GT 450 (400 slides/day throughput), Hamamatsu NanoZoomer. FDA cleared WSI platforms now accepted as primary diagnosis. Compute bottleneck is shifting from scanning to GPU-accelerated inference at scale.

## Competitive landscape

Incumbents: Philips, Leica Biosystems, Roche (iScan), Hamamatsu. AI software layer: Paige.AI (FDA-cleared for prostate cancer), PathAI, Aiforia, Owkin. Competing diagnostic modalities include multiplexed immunofluorescence (Akoya CODEX, 40+ markers vs. standard IHC 4–6), spatial transcriptomics (10x Visium, higher molecular resolution but 10–100× cost), and flow cytometry for liquid biopsy. Key differentiator axes:

## Cloudberry relevance

| Approach | Spatial resolution | Throughput | Cost/slide |
|---|---|---|---|
| WSI brightfield | 0.25 µm | High | $1–5 |
| Multiplex IF | 0.25 µm | Low | $50–200 |
| Spatial transcriptomics | 10–50 µm | Very low | $500–2000 |


Cloudberry relevance sits at the imaging hardware layer: custom CMOS line sensors, photonics-integrated illumination modules, and objective lens assemblies are semiconductor-adjacent procurement. GlobalFoundries-LP context — specialty imaging sensors (BSI CMOS, NIR-enhanced) fabbed at specialty nodes are a credible supply-chain angle. Deal-flow watch: fabless sensor startups optimizing for WSI throughput, low-coherence interferometry for label-free pathology, and edge inference ASICs for on-scanner AI acceleration.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
