---
type: concept
slug: contact-resistance
canonical_name: Contact resistance
aliases:
- silicide contact resistance
- FEOL contact resistance
parent_concepts:
- semiconductor-materials-equipment
related_concepts:
- electron-scale-metrology
- semiconductor-equipment
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2026-01-13-semianalysis-interconnects-beyond-copper]]'
- '[[2026-10-12-cnt-electronics-market-research]]'
- '[[2026-06-22-tim-approaches-full-sweep]]'
frontier:
- What p-type contact resistance, in ohm-micrometres and at a stated channel length, has actually been measured for WSe2 or another TMD, and how far is it from the value the self-consistent model says is needed to avoid source-limited saturation below 10 nm 2026 08 10 ultralow p type contact resistance for ultra nanoscaled 2d m?
- Do the contact schemes implied by the MIGS dimensionality scaling law survive foundry constraints on thermal budget, contamination and wafer-scale uniformity, or do they only work in single-device demonstrations 2026 06 16 contacts to low dimensional semiconductors physical theory a?
- Does the width-scaling benefit observed in 30-40 nm MoS2 nanoribbons persist when channel length is also scaled, where the fixed contact term dominates total resistance 2026 05 05 scaling two dimensional semiconductor nanoribbons for high p?
- How much of the diamond diode's gap to its theoretical limit is attributable to contact resistance rather than defect density, and which is the cheaper term to reduce 2026 07 02 diamond diode for extreme venus environments?
- What's the current best contact resistance achieved at 2nm-node by TSMC / Intel / Samsung internally?
- How much of the 35–40% contact-resistance fraction is recoverable in production (vs theoretical)?
- Which foundry signs the first IP licence for a new contact material? When?
- Are alternative-silicide solutions (NiSi₂, CoSi₂, replacement-metal-gate variants) already addressing this internally?
last_updated: '2026-08-31'
tags:
- concept
- semiconductors
- front-end-of-line
public_expressions:
- INTC
- TSM
mention_count: 25
scorecard:
  viability: 2
  drivers: 4
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-10-12-cnt-electronics-market-research
  title: 'Carbon nanotube electronics: market, cohort and M&A research (web sweep, 82 sources)'
  date: '2026-10-12'
  kind: web
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
- slug: 2026-01-13-semianalysis-interconnects-beyond-copper
  title: Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More
  date: '2026-01-13'
  kind: web
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
neighbors:
- slug: electron-scale-metrology
  name: Electron-scale metrology
  path: /manufacturing/equipment-processes/electron-scale-metrology/
  macro: manufacturing
- slug: semiconductor-equipment
  name: Semiconductor Equipment
  path: /manufacturing/equipment-processes/semiconductor-equipment/
  macro: manufacturing
---
## Summary

Why it has become a gating parameter rather than a nuisance: as logic moves to gate-all-around nanoribbons and complementary FETs (CFETs), channel widths fall into the tens of nanometres and channel resistance falls with them, so the fixed contact term comes to dominate total device resistance. Atomically thin transition-metal dichalcogenide (TMD) channels are attractive for those architectures because a sub-nanometre body suppresses leakage, but there is very little material into which to inject carriers. A 2026 trade analysis lists contact resistance, weak p-type behaviour and integration as the three blockers keeping TMD channels out of production <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>. The same analysis notes copper interconnect hitting its own nanoscale resistance wall, with ruthenium and molybdenum offering large reductions in ultra-fine lines, so the resistance problem is arriving at both ends of the wire-to-channel path.

Contact resistance is not only a logic problem. A diamond Schottky PIN diode reporting ~116 kA/cm2 and 0.05 mOhm-cm2 specific on-resistance identifies defect density and contact resistance as the two terms that must fall for the device to approach its theoretical material limit. Interfacial charge-transfer resistance is also the framing concern in electrode/electrolyte pairing for solid oxide cells, where surface energy and roughness descriptors are proposed as early screens.

## Viability (2/5)

**TLDR: n-type contacts are demonstrably workable at scaled widths; p-type and sub-10 nm remain unsolved and are the binding constraint.**

## Drivers (4/5)

Demand side. The pull is architectural rather than speculative. Three-dimensional logic architectures, GAA nanoribbon and CFET, require channel widths in the tens of nanometres to hit density targets, which is precisely the regime where atomically thin channels become attractive and where fixed contact resistance stops being amortised over a wide channel. CFET is framed as the successor to gate-all-around, with reported better-than-expected ring-oscillator and SRAM progress at a leading foundry <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>, so the architecture that creates the contact problem is advancing on its own schedule. The same resistance pressure is visible in interconnect, where copper's nanoscale limits are pushing ruthenium and molybdenum for ultra-fine lines.

**TLDR: Demand is structural and dated: CFET and GAA density targets force tens-of-nanometre widths, where the contact term dominates.**

## Novelty (3/5)

**TLDR: The new thing is predictive contact modelling where none existed; the improvement over prior practice is qualitative, not quantified.**

## Diffusion (2/5)

## Impact (4/5)

The value is not confined to logic. Contact resistance is one of two terms standing between a demonstrated diamond power diode and its theoretical performance limit, and interfacial charge-transfer resistance is the central concern in electrode/electrolyte compatibility for solid oxide fuel and reversible cells, where surface free energy and ISO 25178 roughness descriptors are proposed as early screening criteria. The mechanisms differ, but the pattern of a fixed interfacial resistance capping an otherwise good material recurs across electronics and electrochemistry, which broadens the addressable value of better interface theory.

**TLDR: It is the gate on whether atomically thin channels can ever replace silicon at CFET-era dimensions, and it caps several other device families too.**

## Timing Soon (2-5yr)

**TLDR: The problem bites now; the evidence needed to judge whether it is solvable at sub-10 nm p-type should arrive within two to five years.**

## Overrated or underrated? Fairly rated

## Prediction

## Evidence base

## Open questions

---
*Assessment drafted 2026-08-31 from up to 11 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
