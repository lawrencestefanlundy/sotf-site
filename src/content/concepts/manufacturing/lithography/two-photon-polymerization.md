---
type: concept
slug: two-photon-polymerization
canonical_name: Two-Photon Polymerization
aliases:
- 2pp
- tpp
- two-photon polymerisation
kind: technology
parent_concepts:
- manufacturing
- lithography
related_concepts: []
sources:
- '[[2026-05-24-mose2-exciton-polariton-all-optical-switch]]'
- '[[2026-05-30-intel-optoscribe-acquisition]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 56
last_reorg_date: '2026-05-13'
sources_7d: 3
sources_30d: 29
recent_mentions:
- slug: 2026-05-24-mose2-exciton-polariton-all-optical-switch
  title: New light-based switch could cut chip energy use and speed future AI photonics
  date: '2026-05-24'
  kind: web
- slug: 2026-05-30-intel-optoscribe-acquisition
  title: Intel Acquires Optoscribe (3D glass photonics, Livingston, Scotland)
  date: '2022-01-27'
  kind: web
neighbors: []
---
## Physics / mechanism

Two-photon polymerization (2PP, also TPP) uses a focused femtosecond laser to selectively cross-link a photopolymer at the focal volume — sub-micron 3D resolution. In photonic packaging it's used for **photonic wire bonding**: directly writing polymer waveguide bonds between photonic ICs and fibres/lenses. Best lab-stage prototypes show <1.6 dB insertion loss and aggregate data rates of 5+ Tbps. The structural reliability question is the bottleneck: Telcordia GR-468 / HTOL / TC / HAST qualification historically takes 7-15 years for new optical materials, and polymer 2PP bond reliability is bounded by CTE mismatch, moisture sensitivity, and thermal-cycle aging. Pre-seed companies have at most ~3000 hours of aging data.

## Competitive landscape

*Adjacent material classes / techniques.*

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*

## Primer (web-enriched)

*Sourced 2026-05-02. See `sources/web/` for full citations.*

Two-photon polymerization (2PP, also TPP) uses a focused femtosecond laser to selectively cross-link a photopolymer at the focal volume — sub-micron 3D resolution. In photonic packaging it's used for **photonic wire bonding**: directly writing polymer waveguide bonds between photonic ICs and fibres/lenses. Best lab-stage prototypes show <1.6 dB insertion loss and aggregate data rates of 5+ Tbps. The structural reliability question is the bottleneck: Telcordia GR-468 / HTOL / TC / HAST qualification historically takes 7-15 years for new optical materials, and polymer 2PP bond reliability is bounded by CTE mismatch, moisture sensitivity, and thermal-cycle aging. Pre-seed companies have at most ~3000 hours of aging data.

## Further reading

- [Two-photon lithography for integrated photonic packaging (Light: AM 2023)](https://www.light-am.com/article/doi/10.37188/lam.2023.032) — tier 1
- [Reliability of adhesive bonded fiber array (Telcordia ref)](https://www.researchgate.net/publication/289873692) — tier 1
- [Plug-and-play sub-dB photonic packaging (PubMed 2025)](https://pubmed.ncbi.nlm.nih.gov/41004590/) — tier 1
- [Ranno PhD thesis (MIT, 2025)](https://dspace.mit.edu/bitstream/handle/1721.1/162334/ranno-lranno-phd-dmse-2025-thesis%20Luigi%20Ranno.pdf) — tier 1

## Merged from root duplicate (two-photon-polymerization.md at concepts/ root, 2026-06-10)

# Two-Photon Polymerization (2PP)

Direct-write 3D microfabrication that uses femtosecond-laser two-photon absorption to cure photoresist only at the focal voxel, giving sub-micron, free-form structures without a mask. Core to photonic packaging (free-form micro-optics, fibre-to-chip coupling) and the throughput bet in **Parallel Foci 2Pp Scaling**. The scaling lever is parallelising foci (SLM / diffractive multi-spot) to lift it from prototyping to volume.
