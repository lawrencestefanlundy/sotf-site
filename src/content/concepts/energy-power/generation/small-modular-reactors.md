---
type: concept
slug: small-modular-reactors
canonical_name: Small Modular Reactors (SMRs)
aliases:
- SMR
- SMRs
- advanced nuclear fission
- microreactors
- advanced fission
kind: technology
parent_concepts:
- energy-power
- generation
related_concepts:
- datacentre-cloud-infrastructure
- ai-thermal-management
sources:
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2023-08-18-e11-in-conversation-with-lux-capital]]'
- '[[2025-01-27-ai-for-nuclear-fusion-feat-martin]]'
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2023-04-04-learnings-from-a-deep-tech-horizon]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2023-09-24-e16-in-conversation-with-john-waite]]'
- '[[2024-11-12-atomic-energy-can-nuclear-power-our]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-06-13-smr-datacentre-baseload-research]]'
- '[[2026-02-16-energy-buildout-keeps-pace-interconnection-queue-and-grid]]'
- '[[2025-12-09-energy-buildout-keeps-pace-gas-turbine-capacity-constraints]]'
- '[[2026-05-09-energy-buildout-keeps-pace-behind-the-meter-gas-turbine]]'
frontier:
- Does X-energy receive its Xe-100 construction permit and does the Dow Texas first unit hold its ~2028 date, or does it slip into the 2030s with the rest of the fleet?
- What is the delivered PPA price of the first commercial SMR, and how far above the ~$65/MWh Three Mile Island restart benchmark does it land?
- Can HALEU enrichment scale from Centrus's 900 kg delivery and 12 MT/yr build-out to the tonnage required by an 11.5 GW pipeline, and on what schedule?
- If gas turbine supply normalises after 2029 as forecast, do hyperscalers hold their SMR offtake commitments or renegotiate them?
- Does any non-LWR SMR (molten-salt, HTGR/TRISO, sodium-fast, heat-pipe) reach commercial operation this decade, or do only de-risked LWR designs (GE Hitachi BWRX-300, Rolls-Royce, NuScale) actually get built by 2032?
- Is the HALEU (high-assay low-enriched uranium) fuel supply chain the binding constraint? Most advanced designs need HALEU; near-term Western supply is thin (Centrus, Urenco ramp), Russia is the incumbent supplier. Whoever owns qualified HALEU/TRISO fabrication has the chokepoint.
- Do hyperscaler datacentre PPAs (Google-Kairos, Amazon-X-energy, Microsoft-Constellation, Meta) actually convert to delivered MWe, or do they slip the way first-of-kind nuclear always has?
- 'Factory-built economics: does the modular/learning-curve promise (build in a factory, ship LEGO modules) materialise, or does first-of-a-kind cost (NuScale''s cancelled UAMPS project at ~$89/MWh and rising) keep killing projects?'
- 'Where is the deep-tech, venture-shaped wedge, if any? The reactor itself is utility/government/strategic-funded and capital-intensive ($1B+ to first unit) — wrong cheque size for a pre-seed fund. The candidate wedges are upstream/adjacent: HALEU/TRISO fuel materials, structural/cladding materials qualification, radiation-hard instrumentation and sensors, reactor I&C / control silicon, and digital-twin/simulation.'
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 19
descendants: []
scorecard:
  viability: 3
  drivers: 4
  novelty: 2
  diffusion: 3
  impact: 4
  timing_band: Later (5-10yr)
  verdict: Overrated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-13-smr-datacentre-baseload-research
  title: SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)
  date: '2026-06-13'
  kind: web
- slug: 2026-05-09-energy-buildout-keeps-pace-behind-the-meter-gas-turbine
  title: 'Behind-the-meter gas turbine workaround cannot scale: fuel cells offer potential but at 40% higher LCOE than gas turbines currently'
  date: '2026-05-09'
  kind: web
- slug: 2026-02-16-energy-buildout-keeps-pace-interconnection-queue-and-grid
  title: Interconnection queue and grid constraints hard-capping datacentre construction timelines
  date: '2026-02-16'
  kind: web
- slug: 2025-12-09-energy-buildout-keeps-pace-gas-turbine-capacity-constraints
  title: 'Gas turbine capacity constraints: delivery windows pushed 5-7 years, peak power crunch 2028-29'
  date: '2025-12-09'
  kind: web
- slug: 2025-01-27-ai-for-nuclear-fusion-feat-martin
  title: AI for Nuclear Fusion (Feat. Martin Riedmiller, Google DeepMind)
  date: '2025-01-27'
  kind: substack
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
- slug: 2024-11-12-atomic-energy-can-nuclear-power-our
  title: 'Nuclear Fission: A Primer'
  date: '2024-11-12'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
neighbors:
- slug: datacentre-cloud-infrastructure
  name: Datacentre & Cloud Infrastructure
  path: /life-frontier/ai-infrastructure/datacentre-cloud-infrastructure/
  macro: life-frontier
- slug: ai-thermal-management
  name: Ai Thermal Management
  path: /energy-power/thermal-management/ai-thermal-management/
  macro: energy-power
---
**Small modular reactors are factory-built fission plants of roughly 50-350 MWe sold as firm 24/7 power for datacentres, backed by hyperscaler PPAs worth a ~$6.8B market in 2025 but with first deployments not expected before 2030 and bulk delivery in 2031-2035 <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.**

## Summary

A small modular reactor is a fission plant designed to be built in a factory rather than on site, shipped in modules, and deployed in multiples to reach the required output. The bet is that serial manufacture replaces the bespoke megaproject engineering that has made large nuclear slow and expensive, and that smaller units simplify siting, financing and licensing. Designs differ substantially: NuScale's 77 MWe light-water module is the only fully design-certified SMR in the US (2023), while X-energy's Xe-100 is a high-temperature gas-cooled design in an approximately 18-month NRC construction-permit review, and Kairos and Oklo remain in pre-licensing <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

The demand story is entirely about datacentres. Firm round-the-clock capacity has become the binding constraint on AI buildout: gas turbine delivery windows have stretched to 5-7 years with the power crunch most severe through 2028-29 <sup class="ref"><a href="https://www.spglobal.com/en/research-insights/special-reports/look-forward/data-center-frontiers/navigating-us-data-center-energy-demand" title="Gas turbine capacity constraints: delivery windows pushed 5-7 years, peak power crunch 2028-29" rel="noopener">ref</a></sup>, average interconnection waits run to five years <sup class="ref"><a href="https://www.hanwhadatacenters.com/blog/data-center-grid-limitations-the-power-bottleneck/" title="Interconnection queue and grid constraints hard-capping datacentre construction timelines" rel="noopener">ref</a></sup>, and the leading behind-the-meter alternative to gas, fuel cells, currently carries around 40% higher LCOE than simple-cycle gas turbines <sup class="ref"><a href="https://www.techinvestments.io/p/power-bottlenecks-and-the-ai-data" title="Behind-the-meter gas turbine workaround cannot scale: fuel cells offer potential but at 40% higher LCOE than gas turbine" rel="noopener">ref</a></sup>. Into that gap hyperscalers have signed offtake: Google-Kairos for up to seven units and 500 MW with the first in 2030 and completion in 2035; Amazon-X-energy for four Xe-100s, with X-energy claiming visibility on roughly 11.5 GW across 144 reactors in the early 2030s; and Oklo with a 500 MW Equinix PPA and 100 MW to Prometheus Hyperscale <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

Three parameters decide the outcome. First, schedule: the only near-term firm nuclear power for a hyperscaler is the Microsoft-Constellation Three Mile Island restart in 2028, which is an existing reactor, not an SMR, and it sets a ~$65/MWh PPA benchmark that new-build SMRs must approach <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. Second, cost: NuScale spent about 15 years reaching regulatory approval and then cancelled its first project for lack of customer interest, and the LCOE case for new nuclear has been the persistent weak point even where the baseload argument is strong <sup class="ref"><a href="https://stateofthefuture.substack.com/p/atomic-energy-can-nuclear-power-our" title="Nuclear Fission: A Primer" rel="noopener">ref</a></sup>. Third, fuel: HALEU is the binding constraint, with DOE committing $2.7B over ten years in January 2026 for domestic enrichment, the NDAA directing at least 21 MT to developers by June 2026, and Centrus having delivered 900 kg while building toward 12 MT/yr <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

## Viability (3/5)

There is no science risk here in the fusion sense. The open question is whether a modular fission plant can be licensed, built and fuelled at a price a datacentre will pay. The evidence is mixed. One design, NuScale's 77 MWe module, has full NRC design certification as of 2023, which proves the regulatory path exists; the same company then cancelled its first project for lack of interest after roughly 15 years of work, which is the clearest signal that certification and commercial viability are different things <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/atomic-energy-can-nuclear-power-our" title="Nuclear Fission: A Primer" rel="noopener">ref</a></sup>. X-energy's Xe-100 is the nearest real construction test, in an approximately 18-month construction-permit review with a possible late-2026 decision and a first unit at Dow's Texas site around 2028 <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

**TLDR: The physics is settled; the licensing, first-of-a-kind cost and fuel supply are not.**

## Drivers (4/5)

On demand, hyperscalers have moved past letters of intent into offtake: Google-Kairos up to 500 MW, Amazon-X-energy four Xe-100 units, Oklo 500 MW to Equinix and 100 MW to Prometheus Hyperscale, with the SMR-for-datacentre market assessed at roughly $6.8B in 2025 counting signed PPAs, early EPC and government grants <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. That is a buyer set with balance sheets large enough to fund first-of-a-kind risk and a strategic reason to do so.

On supply, the alternatives are constrained in a way that pushes buyers toward nuclear even at bad prices. Gas turbine delivery windows have moved out 5-7 years <sup class="ref"><a href="https://www.spglobal.com/en/research-insights/special-reports/look-forward/data-center-frontiers/navigating-us-data-center-energy-demand" title="Gas turbine capacity constraints: delivery windows pushed 5-7 years, peak power crunch 2028-29" rel="noopener">ref</a></sup>, average interconnection queues run five years and are described as the defining constraint on whether datacentres come online at all <sup class="ref"><a href="https://www.hanwhadatacenters.com/blog/data-center-grid-limitations-the-power-bottleneck/" title="Interconnection queue and grid constraints hard-capping datacentre construction timelines" rel="noopener">ref</a></sup>, and fuel cells sit about 40% above simple-cycle gas turbines on LCOE with manufacturing expansion years behind demand <sup class="ref"><a href="https://www.techinvestments.io/p/power-bottlenecks-and-the-ai-data" title="Behind-the-meter gas turbine workaround cannot scale: fuel cells offer potential but at 40% higher LCOE than gas turbine" rel="noopener">ref</a></sup>. Policy is pushing the same direction through DOE HALEU funding and allocations to five advanced-reactor companies <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. The one deduction: none of this scarcity creates SMR capacity any faster, and scarcity-driven demand can evaporate if gas supply normalises after 2029.

**TLDR: Demand is unambiguous and contracted; supply of every competing form of firm power is rationed.**

## Novelty (2/5)

The claim SMRs make is factory serial production against bespoke gigawatt-scale construction. The sources do not contain a delivered cost figure for any SMR, so the advantage remains a design intent rather than a measured result. The only nuclear price anchor available is the ~$65/MWh PPA for the Three Mile Island restart in 2028, and that is an existing reactor being brought back, which is the cheapest possible form of nuclear and a hard benchmark for a first-of-a-kind modular plant to beat <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

Against non-nuclear alternatives the picture is worse on price and better on availability. Simple-cycle gas remains the cost reference point that fuel cells fail to beat by around 40% <sup class="ref"><a href="https://www.techinvestments.io/p/power-bottlenecks-and-the-ai-data" title="Behind-the-meter gas turbine workaround cannot scale: fuel cells offer potential but at 40% higher LCOE than gas turbine" rel="noopener">ref</a></sup>, and gas is only unavailable, not uneconomic <sup class="ref"><a href="https://www.spglobal.com/en/research-insights/special-reports/look-forward/data-center-frontiers/navigating-us-data-center-energy-demand" title="Gas turbine capacity constraints: delivery windows pushed 5-7 years, peak power crunch 2028-29" rel="noopener">ref</a></sup>. The prior assessment on this site was blunt: the baseload argument is good, the LCOE argument is bad, and nuclear is a partial answer at best <sup class="ref"><a href="https://stateofthefuture.substack.com/p/atomic-energy-can-nuclear-power-our" title="Nuclear Fission: A Primer" rel="noopener">ref</a></sup>. A 2 is what the evidence supports: a genuine improvement in construction model with no demonstrated economic edge yet.

**TLDR: Better than large nuclear on build model, but no demonstrated cost advantage over the alternatives it is sold against.**

## Diffusion (3/5)

Diffusion has an unusually favourable start: a handful of buyers taking most of the early volume, standardised designs suited to repeat orders, and a stated pipeline of 11.5 GW across 144 reactors in X-energy's case <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. Concentrated demand from four or five hyperscalers is the ideal condition for climbing a manufacturing learning curve, because it removes the customer fragmentation that killed earlier nuclear order books.

The barriers are licensing throughput, fuel and first-unit cost discovery. Only one design is fully certified, and Kairos and Oklo remain in pre-licensing, so most of the contracted capacity depends on regulatory outcomes not yet in hand <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. HALEU availability caps fleet size independently of how many reactors are ordered, and the domestic enrichment build-out is measured in years <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. The precedent risk is NuScale: certified, then cancelled when the numbers did not work for customers <sup class="ref"><a href="https://stateofthefuture.substack.com/p/atomic-energy-can-nuclear-power-our" title="Nuclear Fission: A Primer" rel="noopener">ref</a></sup>. First deployment in 2030 and bulk in 2031-2035 is the base case in the sources, which is slow diffusion by any AI-infrastructure standard.

**TLDR: Committed buyers and a licensing path exist, but nothing deploys before 2030 and fuel gates the fleet.**

## Impact (4/5)

The value at stake is large because the constraint is binding. Firm 24/7 capacity and interconnection are described as hard caps on datacentre construction, not cost inconveniences <sup class="ref"><a href="https://www.hanwhadatacenters.com/blog/data-center-grid-limitations-the-power-bottleneck/" title="Interconnection queue and grid constraints hard-capping datacentre construction timelines" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.spglobal.com/en/research-insights/special-reports/look-forward/data-center-frontiers/navigating-us-data-center-energy-demand" title="Gas turbine capacity constraints: delivery windows pushed 5-7 years, peak power crunch 2028-29" rel="noopener">ref</a></sup>. A colocated reactor supplying a campus behind the meter bypasses both the queue and the turbine backlog, and does so with no fuel-price or emissions exposure. X-energy's own visibility figure of 11.5 GW indicates the scale of demand the sellers believe exists in the early 2030s <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

The deduction from a 5 is that SMRs are not the only route to the same outcome and are not the cheapest. Gas will carry the load through the crunch, as the earlier analysis on this site conceded directly <sup class="ref"><a href="https://stateofthefuture.substack.com/p/ai-for-nuclear-fusion-feat-martin" title="AI for Nuclear Fusion (Feat. Martin Riedmiller, Google DeepMind)" rel="noopener">ref</a></sup>, and geothermal was flagged as the underpriced alternative for firm clean baseload <sup class="ref"><a href="https://stateofthefuture.substack.com/p/state-of-the-future-part-deux" title="An AI Thesis: State of the Future! Part Deux" rel="noopener">ref</a></sup>. SMRs would be a very large business and a material grid asset; they would not be the difference between the AI buildout happening and not happening.

**TLDR: If the cost lands, SMRs remove the firm-power ceiling on datacentre growth; if it does not, gas does the job less cleanly.**

## Timing Later (5-10yr)

The sources are consistent and specific. 2030 is described as the pivotal first-deployment year with bulk deployment in 2031-2035, and the only near-term firm nuclear power for a hyperscaler is the 2028 Three Mile Island restart of an existing reactor <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. Google-Kairos completes in 2035; Amazon-X-energy targets the early 2030s. The first genuinely informative milestone is nearer: an X-energy construction permit possibly late 2026 and a Dow Texas unit around 2028 <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.

That schedule sits behind the problem it is sold to solve. The power crunch is most severe through 2028-29, after which supply begins catching up <sup class="ref"><a href="https://www.spglobal.com/en/research-insights/special-reports/look-forward/data-center-frontiers/navigating-us-data-center-energy-demand" title="Gas turbine capacity constraints: delivery windows pushed 5-7 years, peak power crunch 2028-29" rel="noopener">ref</a></sup>. SMRs therefore arrive as the crunch eases, which means they must compete on economics against normalised gas supply rather than on availability during scarcity. That is a harder test than the current PPA momentum implies.

**TLDR: First units 2030, meaningful fleet 2031-2035; nothing arrives in time for the 2028-29 crunch.**

## Overrated or underrated? Overrated

Overrated as an answer to the 2028-29 power problem, which is the framing that drives most of the current enthusiasm. Nothing in the sources supports an SMR delivering commercial power to a datacentre before 2030, and the only near-term nuclear electron is a restarted existing reactor at ~$65/MWh <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. Meanwhile HALEU supply is at the 900 kg delivery stage against fleet plans of 144 reactors, and only one design is fully certified <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>. The honest near-term answer for datacentre baseload remains gas <sup class="ref"><a href="https://stateofthefuture.substack.com/p/ai-for-nuclear-fusion-feat-martin" title="AI for Nuclear Fusion (Feat. Martin Riedmiller, Google DeepMind)" rel="noopener">ref</a></sup>, and the market has already priced the SMR story following the Microsoft, Amazon and Google announcements <sup class="ref"><a href="https://stateofthefuture.substack.com/p/state-of-the-future-part-deux" title="An AI Thesis: State of the Future! Part Deux" rel="noopener">ref</a></sup>.

As a 2030s asset class the picture is more defensible: contracted offtake from creditworthy buyers, a regulatory path that has been walked at least once, and federal money behind the fuel chain. But the case rests on a cost outcome no one has yet demonstrated, and the cautionary precedent is a fully certified design whose first project was cancelled for lack of interest after fifteen years <sup class="ref"><a href="https://stateofthefuture.substack.com/p/atomic-energy-can-nuclear-power-our" title="Nuclear Fission: A Primer" rel="noopener">ref</a></sup>. Judgement changes when a first-of-a-kind unit prices out near the restart benchmark, not before.

## Prediction

No newly built SMR will be supplying commercial power to a US datacentre before 1 January 2030; any nuclear electrons reaching a hyperscaler by then will come from existing or restarted reactors such as Three Mile Island.

## Evidence base

- SMR-for-datacentre market assessed at roughly $6.8B in 2025 across signed PPAs, early EPC and government grants; 2030 is the pivotal first-deployment year with bulk deployment 2031-2035 <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- NuScale's 77 MWe design is the only fully design-certified SMR in the US (2023); X-energy's Xe-100 is in an ~18-month construction-permit review with a first unit at Dow Texas around 2028; Kairos and Oklo remain in pre-licensing <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- Google-Kairos covers up to seven SMRs and 500 MW with first unit 2030 and completion 2035; Amazon-X-energy covers four Xe-100s against a claimed 11.5 GW / 144-reactor pipeline in the early 2030s; Oklo has a 500 MW Equinix PPA <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- HALEU is the binding fuel constraint: DOE committed $2.7B over ten years in January 2026, the NDAA directed at least 21 MT to developers by June 2026, and Centrus has delivered 900 kg while building 12 MT/yr capacity <sup class="ref"><a href="https://www.datacenterfrontier.com/energy/article/55235902/" title="SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)" rel="noopener">ref</a></sup>.
- Gas turbine delivery windows have stretched to 5-7 years with the power crunch most severe through 2028-29, before supply begins catching up <sup class="ref"><a href="https://www.spglobal.com/en/research-insights/special-reports/look-forward/data-center-frontiers/navigating-us-data-center-energy-demand" title="Gas turbine capacity constraints: delivery windows pushed 5-7 years, peak power crunch 2028-29" rel="noopener">ref</a></sup>.
- Average interconnection waits of five years are described as the defining constraint on whether new datacentres can come online at all <sup class="ref"><a href="https://www.hanwhadatacenters.com/blog/data-center-grid-limitations-the-power-bottleneck/" title="Interconnection queue and grid constraints hard-capping datacentre construction timelines" rel="noopener">ref</a></sup>.

## Open questions

- Does X-energy receive its Xe-100 construction permit and does the Dow Texas first unit hold its ~2028 date, or does it slip into the 2030s with the rest of the fleet?
- What is the delivered PPA price of the first commercial SMR, and how far above the ~$65/MWh Three Mile Island restart benchmark does it land?
- Can HALEU enrichment scale from Centrus's 900 kg delivery and 12 MT/yr build-out to the tonnage required by an 11.5 GW pipeline, and on what schedule?
- If gas turbine supply normalises after 2029 as forecast, do hyperscalers hold their SMR offtake commitments or renegotiate them?

---
*Assessment drafted 2026-08-31 from up to 15 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
