---
type: concept
slug: fusion
canonical_name: Fusion Energy
aliases: []
kind: category
parent_concepts:
- energy-power
- generation
related_concepts: []
sources:
- '[[2023-04-04-learnings-from-a-deep-tech-horizon]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2023-05-31-three-underrated-technologies-from]]'
- '[[2025-03-04-doe-funds-uk-research-on-critical-materials-for-commercial-f]]'
frontier:
- Does the precipitate dissolution seen under heavy-ion irradiation and helium implantation reproduce at reactor dose rates, or is it an artefact of accelerated ion irradiation shifting the ballistic mixing versus thermal back-diffusion balance 2026 07 21 cucrzr heat sink irradiation performance reveals new challen?
- Is there a heat-sink material or a non-precipitation strengthening route that retains strength and thermal conductivity under fusion neutron and helium loading, and what is its demonstrated component life?
- Can architectures with open ports, beamlines and ducts achieve mean neutron leakage of order 10^-6, and will regulators actually treat fusion-derived atmospheric carbon-14 as a licensable source term 2026 06 24 atmospheric carbon 14 production from neutron leakage in fus?
- What is the delivered cost per MWh of a first-of-a-kind 1 GWe plant, given that no source here provides any cost or LCOE figure?
last_updated: '2026-08-31'
tags:
- concept
- category
mention_count: 14
descendants: []
last_reorg_date: '2026-05-14'
scorecard:
  viability: 2
  drivers: 2
  novelty: null
  diffusion: 2
  impact: 4
  timing_band: Distant (10yr+)
  verdict: Overrated
scorecard_status: draft
sources_7d: 1
sources_30d: 1
recent_mentions:
- slug: 2025-03-04-doe-funds-uk-research-on-critical-materials-for-commercial-f
  title: DOE funds UK research on critical materials for commercial fusion energy - UKNow
  date: '2025-03-04'
  kind: web
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
- slug: 2023-05-31-three-underrated-technologies-from
  title: '💡E02: Three Underrated Technologies from the Future: Brain Recording; Deep Geothermal; IVF + Updates BCI; Clean Meat; LEO Internet++'
  date: '2023-05-31'
  kind: substack
- slug: 2023-04-04-learnings-from-a-deep-tech-horizon
  title: 💡(Early) Learnings from a Deep Tech Horizon Scanning Project
  date: '2023-04-04'
  kind: substack
neighbors: []
---
**Fusion energy aims to generate grid electricity by fusing light nuclei, and the 2026 literature suggests its binding constraints are shifting from plasma physics to neutron-damaged structural materials and the licensing consequences of neutron leakage rather than to plasma performance alone.**

## Summary

Fusion energy proposes to make electricity by fusing light nuclei rather than splitting heavy ones. The mainstream fuel cycle is deuterium-tritium, which releases most of its energy as 14.1 MeV neutrons. Those neutrons are simultaneously the product and the problem: they must be captured to deposit heat that can be converted to electricity, while the surrounding structure has to survive the bombardment. As one 2026 materials paper puts it, commercial fusion requires materials that survive intense neutron bombardment whilst extracting extreme heat loads for conversion to electricity.

The engineering therefore decomposes into three separate problems. First, plasma physics and confinement, which is still supported by basic research: plasma-surface interactions and the electrical sheath that forms where plasma touches a solid are described in 2026 NSF awards as not yet fully understood, and related work is funded on warm dense matter relevant to laser-driven approaches. Second, the plasma-facing and heat-extraction materials. The leading heat-sink candidate, CuCrZr, gets its strength from nano-precipitates formed by heat treatment, and whether that precipitation-hardening strategy survives fusion-relevant irradiation had not been tested; in situ TEM under heavy-ion irradiation plus helium implantation shows the hardening precipitates dissolve, by ballistic dissolution at low temperature and by dissolution and re-precipitation at high temperature. Third, effluents and licensing. Leaked neutrons hitting nitrogen in air produce carbon-14, with a conversion probability of 0.25 to 0.50 for 14.1 MeV DT neutrons and higher for softer spectra; percent-level leakage from a 1 GWe plant would put atmospheric radiocarbon within a factor of a few of natural global production, and a 2500 GWe fleet would need mean leakage of order 10^-6 to stay under 10% of the natural source.

The parameters that decide fusion, on the available evidence, are not only energy gain. They are: how long a heat sink and first wall last under neutron and helium loading before their strengthening mechanism disappears; how tightly neutron streaming through ports, beamlines and ducts can be controlled, since architectures with open streaming paths are singled out as the concern in the radiocarbon analysis; and the lag between a scientific milestone and a licensed, dispatchable plant. Earlier assessment on this site put publicly funded projects at 2035 to 2050 against private claims of within a decade, and argued there would be a long lag between net gain and commercial electricity, of order the best part of a decade even if net gain arrived immediately <sup class="ref"><a href="https://stateofthefuture.substack.com/p/nuclear-fusion-the-state-of-play" title="Nuclear Fusion: A Primer" rel="noopener">ref</a></sup>.

## Viability (2/5)

The honest reading of these sources is that fusion's viability question has moved downstream. The leading heat-sink material for fusion reactors relies on a nano-precipitate dispersion whose stability under fusion-relevant irradiation was untested, and the 2026 evidence is that those precipitates dissolve under two distinct kinetic regimes depending on temperature. That is a direct hit on the mechanism that makes the component strong, and the paper is explicit that accelerated ion dose rates shift the balance between ballistic mixing and thermal back-diffusion, so the mapping to real reactor conditions is itself an open modelling problem. In parallel, a screening-level source term shows that neutron leakage carries a licensing-relevant atmospheric consequence that scales with fleet size.

The sources supplied contain no measurements of energy gain, confinement time, tritium breeding or plant availability, so this score is not a judgement on whether the plasma works. It is a judgement that two necessary conditions for a commercial plant, a heat sink with a qualified life and a neutron-tight envelope, currently have negative or unresolved evidence, and that basic plasma-surface science is still being funded at the level of new diagnostic development. Anyone assessing viability seriously needs plasma performance data that these sources do not provide.

**TLDR: Serious, newly quantified obstacles in materials and effluent control; the sources contain no plasma performance data at all.**

## Drivers (2/5)

On the supply side, the evidence is of steady, distributed, upstream funding rather than of a build-out. Multiple 2026 NSF awards cite fusion energy as a motivating application while actually funding diagnostics, plasma theory or computation, at $633,833 for plasma sheath quantum sensing, $639,322 for warm dense matter studies and $389,392 for nanodiamond plasma sensors; fusion also appears as a motivating domain in tensor-solver and scientific data infrastructure awards. The DOE has also funded UK research on critical materials for commercial fusion <sup class="ref"><a href="https://news.google.com/rss/articles/CBMinAFBVV95cUxObnRXWDRhSU9iWFB6YWVVMDF4T01DaG56VWVxbmlzY1BJS2hNb1p0bEFCUWNyUlZSa0I2VDR6UGxzbVZ4M2JNRlJtMC00TXZ3bzdUbXFPNGtBUFFwUDd4bjBzcDA3ckI4T19tYl9TX3luUVBUODFKWEFEQU5iVmZvc245T2ZFUXp3Y3pEazBCcnRCOHRwTHRFTFk4V3M?oc=5" title="DOE funds UK research on critical materials for commercial fusion energy - UKNow" rel="noopener">ref</a></sup>. That is a healthy research base, not a demand signal.

On the demand side the sources are close to silent. The only relevant material is the earlier argument that datacentre power demand timelines are mismatched even against small modular reactors, and worse against fusion, and that huge demand does not shorten the lag to grid supply <sup class="ref"><a href="https://stateofthefuture.substack.com/p/nuclear-fusion-the-state-of-play" title="Nuclear Fusion: A Primer" rel="noopener">ref</a></sup>. There is no cost, LCOE, offtake or procurement evidence in the supplied sources, so the pull side of this score should be treated as unassessed rather than weak.

**TLDR: Public research funding is continuous but small-ticket and upstream; the sources say almost nothing about who buys the electricity.**

## Novelty (unscored)

A novelty score requires knowing what fusion beats and by how much. The supplied sources do not provide it. There is no cost per MWh, capacity factor, land use, fuel supply or waste comparison against fission, small modular reactors, geothermal or firmed renewables anywhere in the set. The nearest thing is a framing that fusion sits behind SMRs on timelines, and a rhetorical question about whether anyone will think about LCOE when fusion arrives <sup class="ref"><a href="https://stateofthefuture.substack.com/p/nuclear-fusion-the-state-of-play" title="Nuclear Fusion: A Primer" rel="noopener">ref</a></sup>, which is a statement of scepticism rather than a comparison.

What the sources do add is a novel qualification to the usual claim of clean operation: neutron-producing fusion architectures have an atmospheric radiocarbon source term that scales with leakage fraction and fleet size. That does not settle the comparison with fission waste, but it means the environmental case has to be argued with numbers rather than asserted. Until such numbers exist in the record, this dimension is left null.

**TLDR: The sources contain no comparison against fission, SMRs or renewables on any measurable basis.**

## Diffusion (2/5)

Against that, diffusion also depends on the gap between demonstration and dispatch. The prior view on this site was that even immediate net gain leaves the best part of a decade before material grid impact, with publicly funded programmes targeting 2035 to 2050 <sup class="ref"><a href="https://stateofthefuture.substack.com/p/nuclear-fusion-the-state-of-play" title="Nuclear Fusion: A Primer" rel="noopener">ref</a></sup>. Nothing in the 2026 sources shortens that. The score is 2 rather than 1 because the barriers identified are engineering and regulatory rather than physical impossibilities, and because a live materials research pipeline exists, including DOE-funded UK work on critical fusion materials <sup class="ref"><a href="https://news.google.com/rss/articles/CBMinAFBVV95cUxObnRXWDRhSU9iWFB6YWVVMDF4T01DaG56VWVxbmlzY1BJS2hNb1p0bEFCUWNyUlZSa0I2VDR6UGxzbVZ4M2JNRlJtMC00TXZ3bzdUbXFPNGtBUFFwUDd4bjBzcDA3ckI4T19tYl9TX3luUVBUODFKWEFEQU5iVmZvc245T2ZFUXp3Y3pEazBCcnRCOHRwTHRFTFk4V3M?oc=5" title="DOE funds UK research on critical materials for commercial fusion energy - UKNow" rel="noopener">ref</a></sup>.

**TLDR: Fleet-scale deployment implies a neutron leakage budget of order 10^-6 and a heat-sink material that does not yet have a demonstrated life.**

## Impact (4/5)

The scale at which researchers are now framing fusion externalities is itself informative: the radiocarbon screening study runs its fleet-level case at 2500 GWe. A technology whose environmental accounting has to be done at thousands of gigawatts of electrical output is, if delivered, a substitute for a large fraction of world generation. The reference plant used in the same analysis is 1 GWe, which is utility scale rather than niche. That is the basis for a high impact score.

The caveat is that impact here is potential, not demonstrated, and the sources give no economics. There is also a second-order impact channel worth noting: the diagnostics and computational methods being funded with fusion as a motivation have declared spillovers into semiconductor plasma processing and spacecraft propulsion and into high-dimensional simulation and AI pipelines, so some value is realised even if fusion power is late. The score is 4 rather than 5 because no source in this set demonstrates that fusion electricity can be produced at a price anyone would pay.

**TLDR: The relevant unit of analysis in the literature is a 2500 GWe fleet, which is global-scale baseload; the value if it works is very large, though unpriced in these sources.**

## Timing Distant (10yr+)

The only explicit timelines in the sources put publicly funded projects in the EU, China and the UK between 2035 and 2050, against private claims of within a decade, with the argument that even immediate net gain leaves roughly a decade before material grid supply <sup class="ref"><a href="https://stateofthefuture.substack.com/p/nuclear-fusion-the-state-of-play" title="Nuclear Fusion: A Primer" rel="noopener">ref</a></sup>. Measured from 2026, that places meaningful grid contribution beyond ten years.

The 2026 tier-1 results push in the same direction. Discovering that the baseline heat-sink material's hardening mechanism dissolves under irradiation adds a qualification loop, not a shortcut, and a fleet-scale leakage budget of order 10^-6 is the kind of constraint that gets settled through regulation and design revisions over years. Near-term activity in the 0 to 5 year window is best understood as diagnostics, materials science and modelling.

**TLDR: Public programmes are aimed at 2035 to 2050 and the 2026 evidence adds materials qualification and leakage-control work rather than removing steps.**

## Overrated or underrated? Overrated

Overrated on timing and on the cleanliness narrative, not on ultimate significance. The claim that fusion is nearly here rests on plasma milestones, but the 2026 evidence in this set concerns the parts of the plant that come after the plasma. The leading heat-sink alloy loses the precipitates that make it strong under fusion-relevant irradiation, and the effect operates by different mechanisms at low and high temperature, which means the fix is not a single materials substitution. Meanwhile the assumption that neutron-producing fusion has no atmospheric effluent is now quantified and non-trivial: 0.25 to 0.50 conversion probability for leaked 14.1 MeV neutrons into carbon-14, with a fleet-level leakage budget of order 10^-6. Both are the sort of finding that lengthens programmes.

This is consistent with the earlier position taken on this site, that fusion belongs on a 2030-plus timeframe with a hard-to-see venture funding path <sup class="ref"><a href="https://stateofthefuture.substack.com/p/nuclear-fusion-the-state-of-play" title="Nuclear Fusion: A Primer" rel="noopener">ref</a></sup>, and with listing it among the most overrated technologies <sup class="ref"><a href="https://stateofthefuture.substack.com/p/three-underrated-technologies-from" title="💡E02: Three Underrated Technologies from the Future: Brain Recording; Deep Geothermal; IVF + Updates BCI; Clean Meat; LE" rel="noopener">ref</a></sup>. The distinction that matters for investors is between fusion the power source, which these sources place beyond a decade, and fusion the demand driver for diagnostics, radiation-tolerant materials and simulation, which is being funded now and has semiconductor and space spillovers. The second is investable on a normal horizon; the first is not, on this evidence.

## Prediction

No fusion device will export electricity to a public grid before 1 January 2035, consistent with the 2035 to 2050 window given for publicly funded programmes <sup class="ref"><a href="https://stateofthefuture.substack.com/p/nuclear-fusion-the-state-of-play" title="Nuclear Fusion: A Primer" rel="noopener">ref</a></sup>.

## Evidence base

- 24 June 2026: MCNP6.2 transport calculations give a 0.25 to 0.50 probability that leaked 14.1 MeV DT neutrons produce carbon-14 in air via 14N(n,p)14C, with softer spectra giving larger yields.
- 24 June 2026: percent-level neutron leakage from a 1 GWe fusion plant would produce an atmospheric carbon-14 source within a factor of a few of natural global production; a 2500 GWe fleet limited to 10% of the natural source implies mean leakage of order 10^-6.
- 21 July 2026: in CuCrZr, the leading fusion heat-sink alloy, hardening nano-precipitates dissolve under irradiation, by ballistic dissolution at low temperature and by dissolution and re-precipitation at high temperature; whether the precipitation-hardening strategy survives fusion-relevant irradiation had previously been untested.
- 15 May 2026: a $633,833 NSF award describes plasma sheath formation and plasma-surface interaction as not yet fully understood, with fusion energy research named as a beneficiary.
- 4 March 2025: DOE funded UK research on critical materials for commercial fusion energy <sup class="ref"><a href="https://news.google.com/rss/articles/CBMinAFBVV95cUxObnRXWDRhSU9iWFB6YWVVMDF4T01DaG56VWVxbmlzY1BJS2hNb1p0bEFCUWNyUlZSa0I2VDR6UGxzbVZ4M2JNRlJtMC00TXZ3bzdUbXFPNGtBUFFwUDd4bjBzcDA3ckI4T19tYl9TX3luUVBUODFKWEFEQU5iVmZvc245T2ZFUXp3Y3pEazBCcnRCOHRwTHRFTFk4V3M?oc=5" title="DOE funds UK research on critical materials for commercial fusion energy - UKNow" rel="noopener">ref</a></sup>.
- 20 November 2024: publicly funded fusion projects in the EU, China and the UK were targeting 2035 to 2050 against private claims of within a decade, with an expected lag of the best part of a decade between net gain and material grid impact <sup class="ref"><a href="https://stateofthefuture.substack.com/p/nuclear-fusion-the-state-of-play" title="Nuclear Fusion: A Primer" rel="noopener">ref</a></sup>.

## Open questions

- Does the precipitate dissolution seen under heavy-ion irradiation and helium implantation reproduce at reactor dose rates, or is it an artefact of accelerated ion irradiation shifting the ballistic mixing versus thermal back-diffusion balance?
- Is there a heat-sink material or a non-precipitation strengthening route that retains strength and thermal conductivity under fusion neutron and helium loading, and what is its demonstrated component life?
- Can architectures with open ports, beamlines and ducts achieve mean neutron leakage of order 10^-6, and will regulators actually treat fusion-derived atmospheric carbon-14 as a licensable source term?
- What is the delivered cost per MWh of a first-of-a-kind 1 GWe plant, given that no source here provides any cost or LCOE figure?

---
*Assessment drafted 2026-08-31 from up to 12 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
