---
type: concept
slug: ai-power-delivery
canonical_name: AI Power Delivery
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 1
frontier:
- Which intermediate and rack-level bus voltages are actually being deployed, and what end-to-end efficiency is measured from grid input to accelerator core rail?
- How much of the conversion stack moves into or onto the accelerator package, and what does that do to package thermal budgets?
- Which switching device technologies win at each conversion stage, and at what cost per delivered watt?
- How large is the funding and revenue for power delivery specifically, as distinct from the aggregated datacentre-infrastructure category reported in Q2 2026 2026 07 13 semiengineering startup funding q2 2026?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
neighbors: []
---
## Physics / mechanism

AI power delivery refers to the power electronics chain that moves electrical energy from a datacentre's supply into AI accelerator packages. The design problem is set by the current drawn at the low core voltages of large digital logic: as accelerator power rises, delivering it at conventional distribution voltages implies proportionally larger currents, and therefore larger conduction losses and copper cross-section in busbars, connectors and board planes. Raising the distribution voltage upstream and converting closer to the load reduces those currents for the same delivered power, which is why the current wave of datacentre infrastructure work is described as moving to higher-voltage power delivery <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>.

The engineering variables are therefore the choice of intermediate bus voltage, the number and placement of conversion stages, the switching devices and topologies used at each stage, and the thermal and mechanical integration of the final conversion stage near or within the accelerator package. Each additional conversion stage adds loss and volume, so the trade is between transmission loss at low voltage and conversion loss at high voltage.

The sources available treat AI power delivery as an investment category rather than describing a specific device architecture, so the mechanism detail above is limited to what the higher-voltage framing supports.

## Competitive landscape

The single available source positions higher-voltage power delivery alongside interconnect as one of two strands of a continuing datacentre-infrastructure funding wave, itself sitting beside AI hardware proper and a re-emerging edge silicon segment <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>. No comparison of competing conversion topologies, semiconductor material systems or vendors can be drawn from the sources supplied.

## Evidence base

- 80 semiconductor startups raised over $6.0B in Q2 2026, down from $8.4B across 80 startups in Q1 2026 <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>.
- Higher-voltage power delivery is named, with interconnect, as part of the continuing datacentre-infrastructure funding wave in Q2 2026 <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>.
- AI hardware still dominated Q2 2026 semiconductor startup funding, with edge silicon re-emerging on physical-AI and real-time on-device demand <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>.
- 18 companies raised $100M or more in Q2 2026, several at early stage <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>.

## Frontier (open questions)

- Which intermediate and rack-level bus voltages are actually being deployed, and what end-to-end efficiency is measured from grid input to accelerator core rail?
- How much of the conversion stack moves into or onto the accelerator package, and what does that do to package thermal budgets?
- Which switching device technologies win at each conversion stage, and at what cost per delivered watt?
- How large is the funding and revenue for power delivery specifically, as distinct from the aggregated datacentre-infrastructure category reported in Q2 2026 <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
