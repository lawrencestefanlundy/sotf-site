---
type: concept
slug: nuclear-instrumentation
canonical_name: Nuclear Instrumentation
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2026-06-13-smr-datacentre-baseload-research]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 1
frontier:
- Which neutron-flux and in-core temperature sensor technologies are specified in the NRC submissions for Xe-100, Kairos and Oklo designs, and do they differ materially from light-water-reactor practice?
- Do high-temperature, non-water-cooled designs require qualification of instrumentation beyond existing NRC-accepted envelopes, and does that add schedule risk to the ~18-month construction-permit reviews?
- Is instrumentation supply a separable commercial market, or is it captured inside reactor-vendor scope for the 2031-2035 build wave?
- What instrumentation replacement or upgrade scope is involved in the 2028 Three Mile Island restart, and does it set a cost benchmark for other restarts?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-13-smr-datacentre-baseload-research
  title: SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)
  date: '2026-06-13'
  kind: web
neighbors: []
---
## Physics / mechanism

Nuclear instrumentation covers the sensing, measurement and signal-processing hardware used to monitor a reactor core and its supporting systems: neutron flux and power level, temperature, pressure, coolant flow, and radiation fields inside and outside containment. Outputs feed protection and control systems, so the instrument chain sits inside the licensing boundary rather than alongside it.

The supplied source set does not contain technical detail on detector types, sensor physics, qualification envelopes or signal-chain architecture for this concept. What the sources establish is the regulatory and deployment context in which any new instrumentation must be certified: the US Nuclear Regulatory Commission design-certification and construction-permit pathways that gate advanced reactor builds <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

That context matters for instrumentation because certification is granted at the level of the reactor design, not the component. NuScale's 77 MWe design was the only fully design-certified SMR as of 2023, while X-energy's Xe-100 was in an approximately 18-month construction-permit review with a possible late-2026 outcome, and Kairos and Oklo remained in pre-licensing <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. Instrumentation choices are effectively frozen into those submissions.

## Competitive landscape

No comparison between instrumentation approaches is supported by the available sources. The adjacent commercial signal is demand-side: hyperscaler power purchase agreements imply a build wave whose first deployments are expected in 2030, with bulk activity in 2031-2035, and the only near-term firm nuclear power is the Microsoft-Constellation Three Mile Island restart in 2028 at a roughly $65/MWh PPA benchmark <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. Instrumentation suppliers therefore face a demand profile concentrated in the early 2030s, with one restart-driven refurbishment opportunity before it.

## Evidence base

- The SMR-for-datacentre market was estimated at roughly $6.8B in 2025, counting signed PPAs, early EPC and government grants <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- NuScale's 77 MWe design was the only fully design-certified SMR with the NRC as of 2023 <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- X-energy's Xe-100 was in an approximately 18-month NRC construction-permit review, with a possible decision in late 2026 and a first unit at Dow Texas around 2028 <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- Google contracted with Kairos for up to 7 SMRs totalling 500 MW, first unit 2030, complete 2035 <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- Amazon contracted for 4x Xe-100 units; X-energy reported approximately 11.5 GW / 144 reactors of pipeline visibility for the early 2030s <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- HALEU was identified as the binding fuel constraint, with DOE committing $2.7B over 10 years <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

## Frontier (open questions)

- Which neutron-flux and in-core temperature sensor technologies are specified in the NRC submissions for Xe-100, Kairos and Oklo designs, and do they differ materially from light-water-reactor practice?
- Do high-temperature, non-water-cooled designs require qualification of instrumentation beyond existing NRC-accepted envelopes, and does that add schedule risk to the ~18-month construction-permit reviews?
- Is instrumentation supply a separable commercial market, or is it captured inside reactor-vendor scope for the 2031-2035 build wave?
- What instrumentation replacement or upgrade scope is involved in the 2028 Three Mile Island restart, and does it set a cost benchmark for other restarts?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
