---
type: concept
slug: carbon-capture
canonical_name: Carbon Capture
aliases: []
parent_concepts:
- energy-power
related_concepts: []
sources:
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2025-04-17-serving-data-center-load-with-carbon-capture---latitude-medi]]'
- '[[2019-02-21-asu-nau-and-ut-austin-awarded-15m-from-doe-to-transform-ener]]'
mention_count: 4
descendants:
- beccs
- carbon
- ccus
- direct-air-capture
- mineralisation
- ocean-alkalinity
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-04-17-serving-data-center-load-with-carbon-capture---latitude-medi
  title: Serving data center load with carbon capture - Latitude Media
  date: '2025-04-17'
  kind: web
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
- slug: 2019-02-21-asu-nau-and-ut-austin-awarded-15m-from-doe-to-transform-ener
  title: ASU, NAU and UT Austin awarded $1.5M from DOE to transform energy technology with new carbon capture concept - ASU News
  date: '2019-02-21'
  kind: web
neighbors: []
---
## Physics / mechanism

Carbon capture covers processes that separate CO2 from a gas stream (flue gas from combustion, or ambient air) so it can be concentrated for storage or use. The supplied sources touch on two families: electrochemical capture in molten salt media, and capture attached to thermal generation serving data centre load.

In electrochemical carbon capture using molten carbonates, a molten salt such as lithium carbonate (Li2CO3) acts as both electrolyte and CO2 carrier: CO2 is absorbed into the carbonate melt and released or reduced under an applied potential at high temperature. Li2CO3 is described as a cornerstone material for clean energy technologies spanning high-temperature molten carbonate fuel cells, electrochemical carbon capture and lithium-based batteries. The governing performance parameters are therefore the structure and ionic transport of the melt (ion diffusivity, conductivity, local coordination), which set the achievable current density and the energy penalty per tonne of CO2.

Modelling those melts is the bottleneck addressed in the source. Ab initio molecular dynamics captures the many-body interactions in molten Li2CO3 but is computationally expensive, while classical force fields are cheaper but less accurate. Equivariant graph-based machine-learned interatomic potentials, specifically the multi atomic cluster expansion (MACE) and neural equivariant interatomic potential (NequIP) architectures, were trained on melt-quench ab initio molecular dynamics data, with MACE reported to give superior transferability and precision. This positions machine-learned potentials as a screening tool for carbonate melt compositions before experimental work.

## Competitive landscape

## Evidence base

## Frontier (open questions)

- What ionic conductivity and CO2 diffusivity do the MACE-derived molten Li2CO3 models predict, and do they match experimental melt measurements within stated error bars?
- What is the energy penalty per tonne of CO2 for molten carbonate electrochemical capture relative to amine scrubbing, on a like-for-like flue gas composition?
- Did the DOE-funded ASU/NAU/UT Austin concept progress beyond the $1.5M award to a pilot, and at what capture rate and cost?
- For data centre applications, what capture fraction and levelised cost of electricity does capture-equipped generation achieve compared with nuclear or firmed renewables on the same interconnection timeline?

*Synthesised 2026-08-31 from 4 KB sources by the resynth pipeline; citations are KB source slugs.*
