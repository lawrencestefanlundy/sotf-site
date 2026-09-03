---
type: concept
slug: proteomics
canonical_name: Proteomics
aliases: []
parent_concepts:
- biotech
- life-frontier
related_concepts: []
sources:
- '[[2026-04-22-detecting-proteins-in-blood-with]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 7
frontier:
- Do the reported in-memory acceleration figures hold on measured silicon rather than simulated PCM and SOT-MRAM arrays, and what are the endurance and drift limits of superlattice PCM under repeated analog spectral matching?
- Is a 0.3% increase in clustering error and 96% search overlap acceptable at the proteoform level, or does the loss fall preferentially on low-abundance and modified peptides?
- Can incremental clustering initialised from pre-clustered reference data generalise to samples whose spectra are poorly represented in the initialisation set, for example novel post-translational modifications?
- What throughput and cost per sample would be needed for MS proteomics to resolve the modification states that programmable dCas13-kinase systems are designed to install?
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-04-22-detecting-proteins-in-blood-with
  title: Detecting Proteins in Blood with Photonics w/ Prateek of Proteins1
  date: '2026-04-22'
  kind: substack
neighbors: []
---
## Physics / mechanism

Proteomics is the systematic measurement of the protein complement of a biological sample. In its dominant experimental form the workhorse instrument is mass spectrometry (MS), which ionises peptides and measures mass-to-charge ratios to produce spectra; MS is described as essential to both proteomics and metabolomics. Interpretation of the raw output rests on two computational primitives: database search, in which an observed spectrum is matched against theoretical or reference spectra derived from known protein sequences, and spectral clustering, in which near-duplicate spectra are grouped so that redundant identifications are collapsed and consensus spectra formed.

The binding constraint on the field is increasingly data volume rather than instrumentation: mass spectrometry "faces impending challenges in efficiently processing the vast volumes of data" it generates, and conventional full clustering and search algorithms carry high resource usage and long latencies. This has pulled proteomics into the domain of specialised computing hardware. Both search and clustering reduce to massively parallel similarity comparison over high-dimensional vectors, a pattern that maps onto in-memory and content-addressable memory architectures where the comparison is performed where the data is stored rather than moved to a processor.

Two device routes appear in the current literature. SpecPCM performs analog processing at low voltage swing using phase change memory (PCM) devices based on superlattice materials optimised for low-voltage, low-power programming, with a hyperdimensional computing representation of spectra and co-design across application, algorithm, circuit, device and instruction-set levels. HERP instead uses a 3T2MTJ SOT-MRAM based content-addressable memory in 7 nm technology, combined with a lightweight incremental clustering method: a single hardware initialisation with pre-clustered proteomics data supports continuous database search plus local re-clustering, with heuristics from the pre-clustered set guiding the incremental step.

Alongside measurement, proteomics abuts the problem of protein modification state. Post-translational modifications regulate function, availability, recycling and structure, and classical study methods are described as not scalable and prone to modifying proteins outside the intended experimental scope. Any protein inventory is therefore incomplete without proteoform-level resolution of such modifications.

## Competitive landscape

Within MS data processing, the sources support a narrow comparison between two in-memory acceleration approaches rather than between proteomics platforms as a whole.

| Approach | Device / node | Method | Reported result |
|---|---|---|---|
| SpecPCM | Superlattice PCM, analog low-voltage swing | Hyperdimensional computing for clustering and DB search; multi-level co-design | Targets energy and delay efficiency gains for both clustering and DB search |
| HERP | 3T2MTJ SOT-MRAM CAM, 7 nm | Incremental clustering from a pre-clustered initialisation, parallel DB search | 20x faster clustering for a 0.3% increase in clustering error; 96% overlap of DB search results with state-of-the-art algorithms |

Both are positioned against conventional software pipelines running full clustering and search from scratch on general-purpose hardware, which the authors characterise as resource-heavy and high-latency. The wider biological approaches represented in the sources, such as proximity- and complex-based identification of signalling components and programmable enzymatic modification of nascent proteins, are complementary rather than competing: they generate the biological questions that MS proteomics is used to answer.

## Evidence base

- Mass spectrometry is described as essential for proteomics and metabolomics while facing impending challenges in processing its data volumes; SpecPCM was proposed as a PCM-based in-memory computing accelerator for both spectral clustering and database search (arXiv:2411.09760v2, announced 4 June 2026).
- HERP reports 20x acceleration of clustering at the cost of a 0.3% increase in clustering error, with database search results overlapping 96% with state-of-the-art algorithms, using 3T2MTJ SOT-MRAM CAM in 7 nm technology (published 5 November 2025, listed 5 June 2026).
- HERP's evaluation references a 131 GB human proteomics dataset scale for continuous DB search after a single hardware initialisation.
- NSF award 2550649 ($299,599, 13 July 2026) funds CRISPR/dCas13 fused to protein-modifying enzymes such as kinases to phosphorylate target proteins during translation, on the grounds that classical protein modification methods are not scalable.
- NSF award 2541651 ($998,752, 15 July 2026) funds identification of the molecular components of phytochrome B signalling complexes, including nuclear photobodies, under varying light, temperature and amino acid conditions.
- NSF award 2545583 ($500,000, 1 June 2026) targets form-specific functions of nuclear actin in the nucleolus, the site of rRNA synthesis and ribosome formation, using Drosophila oogenesis.

## Frontier (open questions)

- Do the reported in-memory acceleration figures hold on measured silicon rather than simulated PCM and SOT-MRAM arrays, and what are the endurance and drift limits of superlattice PCM under repeated analog spectral matching?
- Is a 0.3% increase in clustering error and 96% search overlap acceptable at the proteoform level, or does the loss fall preferentially on low-abundance and modified peptides?
- Can incremental clustering initialised from pre-clustered reference data generalise to samples whose spectra are poorly represented in the initialisation set, for example novel post-translational modifications?
- What throughput and cost per sample would be needed for MS proteomics to resolve the modification states that programmable dCas13-kinase systems are designed to install?

*Synthesised 2026-08-31 from 5 KB sources by the resynth pipeline; citations are KB source slugs.*
