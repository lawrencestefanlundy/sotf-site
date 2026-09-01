---
type: concept
slug: haleu
canonical_name: Haleu
aliases: []
parent_concepts:
- generation
- energy-power
related_concepts: []
sources:
- '[[2024-11-12-atomic-energy-can-nuclear-power-our]]'
- '[[2026-06-23-baseload-supply-side-catalysts-2026]]'
- '[[2026-06-13-smr-datacentre-baseload-research]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 4
frontier:
- What is the actual installed and contracted HALEU enrichment capacity in tonnes per year, and does it cover the fuel load of the reactors scheduled for first criticality in 2028-2031?
- How much of the DOE's $2.7bn has been obligated to specific enrichment or deconversion facilities, and what are their commissioning dates?
- Do the fuel-form requirements diverge enough between designs (Xe-100 TRISO, Kairos, Oklo, NuScale) that fabrication capacity cannot be pooled across the pipeline?
- What price per kilogram of HALEU do announced SMR PPAs (for example the Oklo-Equinix 500 MW and Google-Kairos 500 MW agreements) implicitly assume, and how does that compare with the ~$65/MWh existing-reactor restart benchmark?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-23-baseload-supply-side-catalysts-2026
  title: Baseload firm-power supply-side catalysts and SMR market sizing (2026 update)
  date: '2026-06-23'
  kind: web
- slug: 2026-06-13-smr-datacentre-baseload-research
  title: SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)
  date: '2026-06-13'
  kind: web
- slug: 2024-11-12-atomic-energy-can-nuclear-power-our
  title: 'Nuclear Fission: A Primer'
  date: '2024-11-12'
  kind: substack
neighbors: []
---
## Physics / mechanism

HALEU (high-assay low-enriched uranium) is the enriched uranium feedstock specified by most advanced and small modular reactor designs. In the sources reviewed it appears not as a reactor physics topic but as a supply-chain variable: HALEU is described as the binding fuel constraint on the advanced-nuclear build-out, meaning that reactor licensing and construction schedules can be met while fuel availability still gates first criticality and refuelling <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

The consequence is that the fuel leg of the advanced-nuclear stack moves on a different clock from the reactor leg. Reactor vendors are working through multi-year regulatory reviews (only one SMR design, NuScale's 77 MWe unit, was fully design-certified as of 2023; X-energy's Xe-100 was in an approximately 18-month construction-permit review with a possible late-2026 decision) while the enrichment and fuel-fabrication capacity that those reactors require is being funded separately <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. Public capital has been directed at this bottleneck: the US Department of Energy committed $2.7bn over ten years to HALEU supply <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

Fuel materials is characterised as the fastest-moving component leg of the advanced-nuclear investment landscape, with Standard Nuclear (Oak Ridge) named as an example of a private company operating in that wedge <sup class="ref"><a href="https://market.us/report/nuclear-small-modular-reactors-market/" title="Baseload firm-power supply-side catalysts and SMR market sizing (2026 update)" rel="noopener">ref</a></sup>. That component wedge, including fuel materials, is a small fraction of the headline SMR market and is not separately sized in the available market data <sup class="ref"><a href="https://market.us/report/nuclear-small-modular-reactors-market/" title="Baseload firm-power supply-side catalysts and SMR market sizing (2026 update)" rel="noopener">ref</a></sup>.

The sources do not specify HALEU enrichment assay, fabrication routes (metal, oxide, TRISO), per-reactor loading requirements, or existing installed enrichment capacity. Those parameters should be treated as unresolved on this page.

## Competitive landscape

HALEU sits upstream of the SMR and advanced-fission designs that create demand for it, so it is complementary rather than competitive with them. Within the wider firm-power set, its exposure is indirect: if HALEU supply slips, the beneficiaries are alternatives that do not need it, including existing-reactor restarts (the Microsoft-Constellation Three Mile Island restart, targeted for 2028 at a roughly $65/MWh PPA benchmark, is the only near-term firm power identified) and next-generation geothermal <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://market.us/report/nuclear-small-modular-reactors-market/" title="Baseload firm-power supply-side catalysts and SMR market sizing (2026 update)" rel="noopener">ref</a></sup>. The demand pull is real but almost entirely forward-dated: 2030 is described as the pivotal first-deployment year for SMRs, with the bulk of deployments in 2031-2035 <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

## Evidence base

- HALEU is identified as the binding fuel constraint on SMR and advanced-nuclear deployment <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- The US Department of Energy committed $2.7bn over ten years to HALEU (announcement dated January in the source) <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- Fuel materials is described as the fastest-moving component leg of the advanced-nuclear supply chain, with Standard Nuclear (Oak Ridge) named <sup class="ref"><a href="https://market.us/report/nuclear-small-modular-reactors-market/" title="Baseload firm-power supply-side catalysts and SMR market sizing (2026 update)" rel="noopener">ref</a></sup>.
- The component wedge including fuel materials is a small fraction of the SMR market and is not separately sized in available reports <sup class="ref"><a href="https://market.us/report/nuclear-small-modular-reactors-market/" title="Baseload firm-power supply-side catalysts and SMR market sizing (2026 update)" rel="noopener">ref</a></sup>.
- Demand-side pull: datacentre-SMR conditional-offtake pipeline grew from roughly 25 GW at end-2024 to roughly 45 GW in 2026 (Build.inc / World Nuclear Association tracker, industry-tracker grade) <sup class="ref"><a href="https://market.us/report/nuclear-small-modular-reactors-market/" title="Baseload firm-power supply-side catalysts and SMR market sizing (2026 update)" rel="noopener">ref</a></sup>.
- Reactor-side timing that fuel must meet: X-energy's first unit at Dow Texas around 2028; Google-Kairos first unit 2030, fleet complete 2035 <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

## Frontier (open questions)

- What is the actual installed and contracted HALEU enrichment capacity in tonnes per year, and does it cover the fuel load of the reactors scheduled for first criticality in 2028-2031?
- How much of the DOE's $2.7bn has been obligated to specific enrichment or deconversion facilities, and what are their commissioning dates?
- Do the fuel-form requirements diverge enough between designs (Xe-100 TRISO, Kairos, Oklo, NuScale) that fabrication capacity cannot be pooled across the pipeline?
- What price per kilogram of HALEU do announced SMR PPAs (for example the Oklo-Equinix 500 MW and Google-Kairos 500 MW agreements) implicitly assume, and how does that compare with the ~$65/MWh existing-reactor restart benchmark?

*Synthesised 2026-08-31 from 4 KB sources by the resynth pipeline; citations are KB source slugs.*
