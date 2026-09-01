---
type: concept
slug: rad-hard-compute
canonical_name: Rad Hard Compute
aliases: []
parent_concepts:
- in-orbit
- life-frontier
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
frontier:
- What total-ionising-dose and single-event-upset specifications does the D3 part actually meet, and at what LET threshold, compared with established space-grade parts?
- Does first D3 silicon appear by early 2027 as targeted, and does it demonstrate measured performance per watt within a stated factor of ground-based AI accelerators?
- What junction temperature and radiator area per chip does "high-temperature vacuum operation" imply, and how does that constrain compute density per satellite?
- Will rad hard 2nm parts be sold to third parties, or is output fully absorbed by SpaceX's own constellation, and what does that mean for non-SpaceX orbital compute entrants?
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Rad hard compute refers to processors and memory engineered to keep functioning under ionising radiation, vacuum and thermal extremes rather than in the controlled environment of a terrestrial data hall. In orbit the design envelope shifts: there is no convective cooling, so heat must be radiated; there is no atmospheric or geomagnetic shielding equivalent to ground level, so trapped protons, heavy ions and solar particle events drive single-event effects and cumulative total-ionising-dose degradation. A part that is nominally the same node as a commercial chip therefore needs different transistor, layout and packaging choices to survive a multi-year mission.

The current commercial push treats radiation hardening as a co-design problem with the thermal environment. The D3 chip described for the Terafab facility is specified as radiation-hardened and engineered for high-temperature vacuum operation, indicating that the target failure modes are radiation-induced upsets and the elevated junction temperatures that follow from radiative-only heat rejection.

The economically relevant parameter is not survivability alone but survivability at a competitive process node and at volume. Rad hard space parts have historically trailed leading-edge logic by several generations, which caps performance per watt for AI workloads. Terafab is described as a 2nm fab with 100k wafer starts per month initially and first silicon targeted early 2027, with 80% of output aimed at orbital AI satellites. That combination, leading-edge node plus dedicated volume, is the mechanism by which orbital compute would close the performance gap against ground-based accelerators.

## Competitive landscape

The sources describe a vertically integrated, single-vendor approach rather than a market of competing rad hard suppliers. Terafab is a $20-25B Tesla/SpaceX/xAI fab in Austin, and the SpaceX acquisition of xAI in February 2026 (all-stock, $1.25T combined entity) was explicitly justified by Musk as enabling orbital data centres. The implied alternative is unhardened commercial silicon flown with shielding and redundancy, or conventional heritage space-grade parts at trailing nodes; neither is compared directly in the available material.

Demand scale is set by the satellite side rather than the chip side: SpaceX's 30 January 2026 FCC filing covers up to 1,000,000 satellites operating as orbital data centres at 500-2,000 km sun-synchronous with optical inter-satellite links to Starlink. Any independent rad hard supplier would be competing for a fraction of a captive internal order book.

## Evidence base

- SpaceX acquired xAI in February 2026 in an all-stock merger forming a $1.25T entity, justified by Musk as enabling orbital data centres.
- A SpaceX FCC filing of 30 January 2026 requests up to 1,000,000 satellites as orbital data centres at 500-2,000 km sun-synchronous with optical ISLs to Starlink.
- Terafab, announced March 2026, is a $20-25B Tesla/SpaceX/xAI 2nm fab in Austin.
- The Terafab D3 chip is described as radiation-hardened and engineered for high-temperature vacuum operation.
- 80% of Terafab output is targeted at orbital AI satellites, with 100k wafer starts per month initially and first silicon targeted early 2027.
- All 11 original xAI co-founders had departed by late March 2026.

## Frontier (open questions)

- What total-ionising-dose and single-event-upset specifications does the D3 part actually meet, and at what LET threshold, compared with established space-grade parts?
- Does first D3 silicon appear by early 2027 as targeted, and does it demonstrate measured performance per watt within a stated factor of ground-based AI accelerators?
- What junction temperature and radiator area per chip does "high-temperature vacuum operation" imply, and how does that constrain compute density per satellite?
- Will rad hard 2nm parts be sold to third parties, or is output fully absorbed by SpaceX's own constellation, and what does that mean for non-SpaceX orbital compute entrants?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
