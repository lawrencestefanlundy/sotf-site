---
type: concept
slug: co-packaged-optics
canonical_name: Co-Packaged Optics
aliases:
- cpo
kind: technology
parent_concepts:
- manufacturing
- packaging
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-03-12-optical-displaces-copper-broadcom-ships-tomahawk-6-world-s]]'
- '[[2026-05-02-co-packaged-optics-2026-2036-idtechex]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-07-26-ai-backend-network-optics-2026]]'
- '[[2026-06-17-sjtu-ge-si-photodetector-110ghz-fowlp]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-05-26-optical-displaces-copper-the-global-co-packaged-optics]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
- '[[2026-04-10-photonic-light-source-supply-co-packaged-optics-cpo-scaling]]'
- '[[2026-05-30-senko-gf-cpo-detachable-fiber]]'
- '[[2026-06-23-photonic-foundry-capacity-co-packaged-optics-is-not-delayed]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 62
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 4
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-26-ai-backend-network-optics-2026
  title: 'Dell''Oro: AI back-end switching past $100B by 2030, optical transport $16B in 2025'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-23-photonic-foundry-capacity-co-packaged-optics-is-not-delayed
  title: Co-Packaged Optics Is Not Delayed. SemiAnalysis Is Just Wrong
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
neighbors: []
---
## Physics / mechanism

Co-packaged optics (CPO) integrates optical I/O directly with the switch/compute ASIC, replacing pluggable optical modules. The market is forecast to reach ~$5.5B by 2027 and >$20B by 2036 (37% CAGR per IDTechEx). The defining contest is **material class for the in-package waveguides and bonds**: polymer (cheap, low-CTE-mismatch, but Telcordia-qualification-unproven for production AI interconnect) vs inorganic (TFLN, BTO, SiN — higher cost, higher reliability bar, foundry-compatible). Real volume deployment is 2027-2028 timeframe. NVIDIA, Broadcom, and the major foundries each have distinct platform strategies.

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

Co-packaged optics (CPO) integrates optical I/O directly with the switch/compute ASIC, replacing pluggable optical modules. The market is forecast to reach ~$5.5B by 2027 and >$20B by 2036 (37% CAGR per IDTechEx). The defining contest is **material class for the in-package waveguides and bonds**: polymer (cheap, low-CTE-mismatch, but Telcordia-qualification-unproven for production AI interconnect) vs inorganic (TFLN, BTO, SiN — higher cost, higher reliability bar, foundry-compatible). Real volume deployment is 2027-2028 timeframe. NVIDIA, Broadcom, and the major foundries each have distinct platform strategies.

## Further reading

- [Co-Packaged Optics 2026-2036 (IDTechEx)](https://www.idtechex.com/en/research-report/co-packaged-optics-cpo/1138) — tier 2
- [CPO Book (SemiAnalysis)](https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling) — tier 5
- [CPO market and tech update (Cignal AI, Feb 2025)](https://cignal.ai/2025/02/co-packaged-optics-market-and-technology-update/) — tier 5
- [CPO market to grow at 37% CAGR (Semiconductor Today)](https://www.semiconductor-today.com/news_items/2025/dec/idtechex-291225.shtml) — tier 5

## Merged from root duplicate (co-packaged-optics.md at concepts/ root, 2026-06-10)

# Co-Packaged Optics (CPO)

Integrating the optical engine (photonic IC plus driver/TIA) into the same package as the switch or accelerator ASIC, replacing pluggable optics to cut the energy-per-bit and reach of the electrical link at the package edge. The convergence point of silicon photonics, advanced packaging and [Chiplets](/compute/compute-architecture/chiplets/); central to the AI-fabric and switch-bandwidth roadmaps that 11 active theses bet on (packaging, foundry, interconnect, photonic-compute).
