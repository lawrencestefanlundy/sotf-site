---
type: concept
slug: liquid-cooling
canonical_name: Liquid Cooling (cold plate, immersion, two-phase)
aliases: []
kind: technology
parent_concepts:
- energy-power
- ai-thermal-management
related_concepts: []
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-05-05-thermal-stack-arms-race-ai-datacenter-liquid-cooling-market]]'
- '[[2026-03-11-ai-power-thermal-binding-direct-to-chip-liquid-cooling]]'
- '[[2026-03-08-diamonds-are-semiconductors-best-friend]]'
- '[[2026-07-09-in-die-microfluidic-cooling-sprint]]'
- '[[2025-08-01-thermal-stack-arms-race-why-liquid-cooling-is-becoming-the]]'
- '[[2026-04-10-thermal-stack-arms-race-liquid-cooling-for-ai-data-centers]]'
- '[[2026-04-08-datacentre-thermal-power-market-microsoft-liquid-cooling-a]]'
- '[[2026-01-08-datacentre-thermal-power-market-data-center-liquid-cooling]]'
- '[[2026-04-19-datacentre-thermal-power-market-trendforce-liquid-cooling]]'
- '[[2024-yole-thermal-management-2024]]'
- '[[2026-06-01-ai-power-thermal-binding-ai-data-center-liquid-cooling]]'
- '[[2026-05-19-ai-power-thermal-binding-liquid-cooling-solidifying-as]]'
- '[[2026-07-26-humanoid-duty-cycle-thermal-constraint]]'
- '[[2025-07-03-datacentre-thermal-power-market-cooling-is-the-new]]'
- '[[2026-04-01-ai-power-thermal-binding-market-projection-35-of-new-ai]]'
- '[[2026-04-02-datacentre-thermal-power-market-goldman-sachs-forecasts]]'
- '[[2026-03-25-thermal-stack-arms-race-why-ai-rack-densities-make-liquid]]'
- '[[2025-05-03-datacentre-thermal-power-market-intel-foundry-thermal]]'
- '[[2026-05-22-ai-power-thermal-binding-goldman-sachs-ai-infrastructure]]'
- '[[2026-02-15-ai-power-thermal-binding-oracle-announces-direct-to-chip]]'
frontier:
- Does the gap between TrendForce's observed 33% penetration in AI datacentres and Goldman's forecast 76% of AI servers by end-2026 close, or was the forecast an over-extrapolation?
- How much of the cooling value pool migrates into the package? Does a second top-tier foundry or OSAT beyond TSMC and Intel qualify an in-package microfluidic option, and do design wins follow?
- What is the retrofit economics of converting existing air-cooled halls, and what share of installed capacity is simply stranded for AI workloads? None of the sources address this.
- Does two-phase immersion stay under 15% of new builds through 2030, or does a specific flux or fluid constraint break Yole's segmentation view?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 30
last_reorg_date: '2026-05-13'
scorecard:
  viability: 5
  drivers: 5
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-09-in-die-microfluidic-cooling-sprint
  title: In-die microfluidic cooling — cluster research sprint
  date: '2026-07-09'
  kind: web
- slug: 2026-06-01-ai-power-thermal-binding-ai-data-center-liquid-cooling
  title: 'AI Data Center Liquid Cooling Market: Hyperscaler Adoption Analysis'
  date: '2026-06-01'
  kind: web
- slug: 2026-05-22-ai-power-thermal-binding-goldman-sachs-ai-infrastructure
  title: 'Goldman Sachs AI Infrastructure Analysis: Liquid Cooling as Non-Discretionary'
  date: '2026-05-22'
  kind: web
- slug: 2026-05-19-ai-power-thermal-binding-liquid-cooling-solidifying-as
  title: Liquid cooling solidifying as direct-to-chip industry standard for hyperscale AI deployments
  date: '2026-05-19'
  kind: web
- slug: 2026-05-05-thermal-stack-arms-race-ai-datacenter-liquid-cooling-market
  title: AI Datacenter Liquid Cooling Market to Reach USD 17.8 Billion by 2036
  date: '2026-05-05'
  kind: web
- slug: 2026-04-19-datacentre-thermal-power-market-trendforce-liquid-cooling
  title: TrendForce liquid cooling penetration in AI-focused data centers climbed from 14% to 33%
  date: '2026-04-19'
  kind: web
- slug: 2026-04-10-thermal-stack-arms-race-liquid-cooling-for-ai-data-centers
  title: Liquid Cooling For AI Data Centers Market Growth Analysis - Size and Forecast 2026-2030
  date: '2026-04-10'
  kind: web
neighbors: []
---
**Liquid cooling replaces air as the heat-removal path in AI datacentres by moving coolant to the chip (cold plates), around the chip (immersion) or into the die (microfluidics), and analysts now describe it as non-discretionary above roughly 100kW per rack rather than an efficiency option.**

## Summary

Air cooling removes heat from a server by blowing it across heatsinks. That works while rack power stays modest, but AI accelerator racks have moved from roughly 40kW to 140kW <sup class="ref"><a href="https://vocal.media/futurism/data-center-liquid-cooling-market-outlook-efficient-thermal-management-and-growth-opportunities" title="TrendForce liquid cooling penetration in AI-focused data centers climbed from 14% to 33%" rel="noopener">ref</a></sup>, and above about 100kW per rack the air path runs out of practical headroom <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup>. Liquid cooling substitutes a fluid loop with far higher volumetric heat capacity. There are three main architectures. **Direct-to-chip (cold plate)** clamps a liquid-carrying plate onto the package lid and pipes heat to a coolant distribution unit; it is the mainstream option and reported to fill the 100 to 175kW density band <sup class="ref"><a href="https://www.networkworld.com/article/4149069/why-ai-rack-densities-make-liquid-cooling-nonnegotiable.html" title="Why AI rack densities make liquid cooling nonnegotiable" rel="noopener">ref</a></sup>. **Single-phase immersion** submerges whole boards in dielectric fluid. **Two-phase immersion** uses a fluid that boils on the hot surface, exploiting latent heat for the highest flux, at the cost of exotic fluids and containment.

A fourth layer is emerging inside the package. TSMC's IMC-Si etches 30 to 150 µm microchannels into a silicon lid fusion-bonded to the die backside, reporting thermal resistance of about 0.055 °C/W, roughly 15% better than the best external cold plate, and more than 7 W/mm² on logic backside with deionised water; it is now described as part of the CoWoS packaging process <sup class="ref"><a href="https://tspasemiconductor.substack.com/p/cooling-is-the-new-architecture-tsmcs" title="Cooling is the New Architecture: TSMC's IMC-Si and the Future of AI Packaging" rel="noopener">ref</a></sup>. Intel showed in-package liquid cooling and liquid-metal TIM options as qualified foundry package options in 2025 <sup class="ref"><a href="https://www.servethehome.com/intel-foundry-thermal-capabilities-with-tim-options-and-in-package-liquid-cooling-shown/" title="Intel Foundry Thermal Capabilities with TIM Options and In-Package Liquid Cooling Shown" rel="noopener">ref</a></sup>. Corintis, an EPFL spinout, raised a $24M Series A in September 2025, co-develops with Microsoft, has shipped over 10,000 cold plates and targets over 1M units a year by end-2026.

The parameters that decide the outcome are rack power density, the thermal resistance budget from junction to coolant, whether the binding resistance sits at the lid TIM or the cold plate (Yole puts the lid TIM as the binding layer above 1.5kW package TDP **2024 Yole Thermal Management 2024**), water and facility constraints (Oracle's February 2026 campuses use closed-loop non-evaporative direct-to-chip <sup class="ref"><a href="https://nextwavesinsight.com/ai-data-center-liquid-cooling-infrastructure/" title="Oracle Announces Direct-to-Chip Cooling for AI Campuses" rel="noopener">ref</a></sup>), and retrofit economics in existing air-cooled halls.

The same physics appears outside the datacentre: in humanoid robots, continuous torque is limited by winding insulation and magnet temperature rather than pack energy, and Musk has said the contribution of liquid cooling systems for humanoids is no less significant than battery breakthroughs <sup class="ref"><a href="https://airobotseidos.com/liquid-cooling-systems-for-humanoid-robots/" title="What actually limits a humanoid to minutes: the thermal cliff, not the battery" rel="noopener">ref</a></sup>.

## Viability (5/5)

Adoption numbers, not demonstrations, carry this. Goldman Sachs puts liquid-cooled AI servers at 15% in 2024 rising to 76% by end-2026 <sup class="ref"><a href="https://www.lombardodier.com/insights/2026/january/ai-supercharges-the-race.html" title="Goldman Sachs forecasts liquid-cooled AI servers will increase from 15% in 2024 to 76% in 2026" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html" title="Goldman Sachs AI Infrastructure Analysis: Liquid Cooling as Non-Discretionary" rel="noopener">ref</a></sup>; TrendForce measures penetration in AI-focused datacentres climbing from 14% to 33%, with liquid-based cooling at 46% of the total datacentre cooling market <sup class="ref"><a href="https://vocal.media/futurism/data-center-liquid-cooling-market-outlook-efficient-thermal-management-and-growth-opportunities" title="TrendForce liquid cooling penetration in AI-focused data centers climbed from 14% to 33%" rel="noopener">ref</a></sup>. The market is described as past the experimental phase and consolidating around direct-to-chip <sup class="ref"><a href="https://iot-analytics.com/7-data-center-trends-to-watch/" title="Liquid cooling solidifying as direct-to-chip industry standard for hyperscale AI deployments" rel="noopener">ref</a></sup>, with Vertiv analysis calling it non-discretionary for AI GPU clusters <sup class="ref"><a href="https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html" title="Goldman Sachs AI Infrastructure Analysis: Liquid Cooling as Non-Discretionary" rel="noopener">ref</a></sup>. Named deployment: Oracle's February 2026 AI campuses <sup class="ref"><a href="https://nextwavesinsight.com/ai-data-center-liquid-cooling-infrastructure/" title="Oracle Announces Direct-to-Chip Cooling for AI Campuses" rel="noopener">ref</a></sup>.

The caveat is that this score is earned by cold plates. Two-phase immersion is projected to stay specialty at under 15% of new builds by 2030 **2024 Yole Thermal Management 2024**, and the sources give no performance or reliability data on two-phase fielded systems. In-die microfluidics has published thermal numbers and a foundry integration path but no disclosed volume production.

**TLDR: Direct-to-chip is shipping at hyperscale volume today; the debate is mix, not whether it works.**

## Drivers (5/5)

Demand: rack densities beyond 40kW toward 140kW <sup class="ref"><a href="https://vocal.media/futurism/data-center-liquid-cooling-market-outlook-efficient-thermal-management-and-growth-opportunities" title="TrendForce liquid cooling penetration in AI-focused data centers climbed from 14% to 33%" rel="noopener">ref</a></sup> push air past practical limits <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup>, and AI-specific capacity additions are projected to account for over 60% of new global datacentre capex by 2026, with more than 35% of new AI-optimised capacity specifying liquid cooling as primary thermal management <sup class="ref"><a href="https://marketintelo.com/report/ai-data-center-liquid-immersion-cooling-market" title="Market projection: 35%+ of new AI datacenter capacity specifying liquid cooling by 2026" rel="noopener">ref</a></sup>. By 2026 the vast majority of new hyperscaler AI construction specifications are reported to mandate liquid cooling <sup class="ref"><a href="https://marketintelo.com/report/ai-data-center-liquid-cooling-infrastructure-market" title="AI Data Center Liquid Cooling Market: Hyperscaler Adoption Analysis" rel="noopener">ref</a></sup>. This is a physics-forced substitution: the buyer cannot deploy the accelerator it has already bought without it.

Supply: Dell'Oro puts the datacentre liquid cooling market near $7B by 2029 <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup>, and Yole has total AI accelerator thermal management growing from roughly $8B in 2024 to over $25B by 2030 **2024 Yole Thermal Management 2024**. Suppliers span facility vendors, cold-plate manufacturers, foundries and startups; Corintis alone claims a path from 10,000 shipped cold plates to over 1M units a year by end-2026. Note that published market sizings diverge wildly (one forecast quotes growth of USD 2.48 trillion over 2026-2030 at 31.7% CAGR <sup class="ref"><a href="https://www.technavio.com/report/liquid-cooling-for-ai-data-centers-market-industry-analysis" title="Liquid Cooling For AI Data Centers Market Growth Analysis - Size and Forecast 2026-2030" rel="noopener">ref</a></sup>, another $17.8B by 2036 <sup class="ref"><a href="https://www.morningstar.com/news/accesswire/1163831msn/ai-datacenter-liquid-cooling-market-to-reach-usd-178-billion-by-2036-as-hyperscale-ai-infrastructure-drives-thermal-management-transformation" title="AI Datacenter Liquid Cooling Market to Reach USD 17.8 Billion by 2036" rel="noopener">ref</a></sup>); treat the revenue pool as poorly bounded even where the direction is not in doubt.

**TLDR: Demand is set by accelerator TDP and rack density, not by preference; supply is a large, fast-growing vendor market.**

## Novelty (3/5)

Against air cooling the margin is categorical rather than incremental: air simply does not serve the 100 to 175kW band that direct-to-chip now occupies <sup class="ref"><a href="https://www.networkworld.com/article/4149069/why-ai-rack-densities-make-liquid-cooling-nonnegotiable.html" title="Why AI rack densities make liquid cooling nonnegotiable" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup>. But the sources describe cold-plate liquid cooling as an architecture consolidating into an industry standard <sup class="ref"><a href="https://iot-analytics.com/7-data-center-trends-to-watch/" title="Liquid cooling solidifying as direct-to-chip industry standard for hyperscale AI deployments" rel="noopener">ref</a></sup>, which is the language of commoditisation, not invention. Yole expects no single material or architecture to capture more than 40% of premium thermal stack revenue by 2030 **2024 Yole Thermal Management 2024**, and one 2026 analysis identifies no single winner among direct-to-chip and immersion approaches <sup class="ref"><a href="https://www.morningstar.com/news/accesswire/1163831msn/ai-datacenter-liquid-cooling-market-to-reach-usd-178-billion-by-2036-as-hyperscale-ai-infrastructure-drives-thermal-management-transformation" title="AI Datacenter Liquid Cooling Market to Reach USD 17.8 Billion by 2036" rel="noopener">ref</a></sup>.

The genuinely new content sits at the die, and its measured advantage is modest: TSMC's IMC-Si reports about 0.055 °C/W, roughly 15% better than the best external cold plate, and over 7 W/mm² on logic backside. That 15% matters because it is at the binding layer (Yole puts the lid TIM as the constraint above 1.5kW package TDP **2024 Yole Thermal Management 2024**) and because integration into CoWoS moves the cooling primitive inside the foundry's process, alongside Intel offering in-package liquid cooling as a qualified package option <sup class="ref"><a href="https://www.servethehome.com/intel-foundry-thermal-capabilities-with-tim-options-and-in-package-liquid-cooling-shown/" title="Intel Foundry Thermal Capabilities with TIM Options and In-Package Liquid Cooling Shown" rel="noopener">ref</a></sup>. Where the value accrues, board vendor or foundry, is the live question rather than whether liquid works.

**TLDR: Decisively better than air in the density band that matters, but the technology is engineering integration rather than new science, and the next step gains only about 15%.**

## Diffusion (4/5)

Diffusion into new AI capacity is fast and observable. Yole expected direct-to-chip to be the default in AI training builds by 2027 **2024 Yole Thermal Management 2024**; a 2025 assessment put over 50% of new hyperscale capacity as liquid-cooled by 2027, though across all liquid types rather than direct-to-chip alone <sup class="ref"><a href="https://www.datacenters.com/news/why-liquid-cooling-is-becoming-the-new-standard" title="Why Liquid Cooling Is Becoming the Data Center Standard" rel="noopener">ref</a></sup>; by 2026 most new hyperscaler specifications are reported to mandate it <sup class="ref"><a href="https://marketintelo.com/report/ai-data-center-liquid-cooling-infrastructure-market" title="AI Data Center Liquid Cooling Market: Hyperscaler Adoption Analysis" rel="noopener">ref</a></sup>. Standardisation around one architecture <sup class="ref"><a href="https://iot-analytics.com/7-data-center-trends-to-watch/" title="Liquid cooling solidifying as direct-to-chip industry standard for hyperscale AI deployments" rel="noopener">ref</a></sup> lowers the integration barrier further, and closed-loop non-evaporative designs address the water objection <sup class="ref"><a href="https://nextwavesinsight.com/ai-data-center-liquid-cooling-infrastructure/" title="Oracle Announces Direct-to-Chip Cooling for AI Campuses" rel="noopener">ref</a></sup>.

What holds it back from a 5 is the gap between the aggressive and the measured numbers. Goldman's 76% of AI servers by end-2026 <sup class="ref"><a href="https://www.lombardodier.com/insights/2026/january/ai-supercharges-the-race.html" title="Goldman Sachs forecasts liquid-cooled AI servers will increase from 15% in 2024 to 76% in 2026" rel="noopener">ref</a></sup> sits against TrendForce's observed 33% penetration in AI-focused datacentres <sup class="ref"><a href="https://vocal.media/futurism/data-center-liquid-cooling-market-outlook-efficient-thermal-management-and-growth-opportunities" title="TrendForce liquid cooling penetration in AI-focused data centers climbed from 14% to 33%" rel="noopener">ref</a></sup>, which implies either a very steep late-2026 ramp or forecaster optimism. The sources also say nothing about retrofit cost, leak liability, service model, CDU supply or skilled-labour constraints, and immersion in particular remains penned into a minority segment **2024 Yole Thermal Management 2024**.

**TLDR: Greenfield AI builds are already specifying it as default; brownfield air-cooled capacity is the drag the sources do not quantify.**

## Impact (4/5)

The leverage is enabling rather than economic: if the thermal path fails, the accelerators cannot be commissioned, and AI capacity additions are projected at over 60% of new global datacentre capex <sup class="ref"><a href="https://marketintelo.com/report/ai-data-center-liquid-immersion-cooling-market" title="Market projection: 35%+ of new AI datacenter capacity specifying liquid cooling by 2026" rel="noopener">ref</a></sup>. Liquid cooling is characterised as a foundational requirement for deploying next-generation AI infrastructure <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup> and as non-discretionary for GPU clusters <sup class="ref"><a href="https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html" title="Goldman Sachs AI Infrastructure Analysis: Liquid Cooling as Non-Discretionary" rel="noopener">ref</a></sup>. Off the datacentre floor, the same constraint gates humanoid robot duty cycle, where continuous torque limits rather than pack energy set the shift length <sup class="ref"><a href="https://airobotseidos.com/liquid-cooling-systems-for-humanoid-robots/" title="What actually limits a humanoid to minutes: the thermal cliff, not the battery" rel="noopener">ref</a></sup>.

Value capture is the weaker half. Dell'Oro's roughly $7B by 2029 <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup> and Yole's $25B+ total AI thermal market by 2030 **2024 Yole Thermal Management 2024** are small relative to the compute they enable, and Yole's view that no architecture takes more than 40% of premium thermal revenue **2024 Yole Thermal Management 2024** points to a fragmented, competitive supplier base. The larger prize is the in-package layer, where foundry integration of microfluidics <sup class="ref"><a href="https://www.servethehome.com/intel-foundry-thermal-capabilities-with-tim-options-and-in-package-liquid-cooling-shown/" title="Intel Foundry Thermal Capabilities with TIM Options and In-Package Liquid Cooling Shown" rel="noopener">ref</a></sup> could move margin from board and facility vendors to whoever owns the package.

**TLDR: Gates deployment of the entire next-generation accelerator fleet, but the directly captured revenue pool is a fraction of the compute spend it unlocks.**

## Timing Now (0-2yr)

This is a deployed technology in its steep adoption phase, not a future one. Measured penetration in AI-focused datacentres has already moved from 14% to 33% <sup class="ref"><a href="https://vocal.media/futurism/data-center-liquid-cooling-market-outlook-efficient-thermal-management-and-growth-opportunities" title="TrendForce liquid cooling penetration in AI-focused data centers climbed from 14% to 33%" rel="noopener">ref</a></sup>, most new hyperscaler AI specifications are reported to mandate it as of 2026 <sup class="ref"><a href="https://marketintelo.com/report/ai-data-center-liquid-cooling-infrastructure-market" title="AI Data Center Liquid Cooling Market: Hyperscaler Adoption Analysis" rel="noopener">ref</a></sup>, and a named operator deployment exists from February 2026 <sup class="ref"><a href="https://nextwavesinsight.com/ai-data-center-liquid-cooling-infrastructure/" title="Oracle Announces Direct-to-Chip Cooling for AI Campuses" rel="noopener">ref</a></sup>.

The dated milestones ahead are narrower. 2027 is when direct-to-chip is expected to be the default in AI training builds **2024 Yole Thermal Management 2024** and when over 50% of new hyperscale capacity is expected to be liquid-cooled <sup class="ref"><a href="https://www.datacenters.com/news/why-liquid-cooling-is-becoming-the-new-standard" title="Why Liquid Cooling Is Becoming the Data Center Standard" rel="noopener">ref</a></sup>. In-die microfluidics is on a 2026 to 2028 productisation track (Corintis targeting over 1M units a year by end-2026, TSMC's IMC-Si already inside CoWoS). Two-phase immersion is a Later question at best, still under 15% of new builds by 2030 on Yole's view **2024 Yole Thermal Management 2024**.

**TLDR: Already the default specification for new AI builds; the 2027 resolution point is about mix, not arrival.**

## Overrated or underrated? Fairly rated

The direction is settled and broadly agreed: cold-plate direct-to-chip becomes the default thermal architecture for AI capacity because air physically cannot serve 140kW racks <sup class="ref"><a href="https://vocal.media/futurism/data-center-liquid-cooling-market-outlook-efficient-thermal-management-and-growth-opportunities" title="TrendForce liquid cooling penetration in AI-focused data centers climbed from 14% to 33%" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup>. That consensus is already in the forecasts and in operator specifications <sup class="ref"><a href="https://marketintelo.com/report/ai-data-center-liquid-cooling-infrastructure-market" title="AI Data Center Liquid Cooling Market: Hyperscaler Adoption Analysis" rel="noopener">ref</a></sup>, so there is little informational edge left in the headline call. The disagreement is only about pace: Goldman's 76% of AI servers by end-2026 <sup class="ref"><a href="https://www.lombardodier.com/insights/2026/january/ai-supercharges-the-race.html" title="Goldman Sachs forecasts liquid-cooled AI servers will increase from 15% in 2024 to 76% in 2026" rel="noopener">ref</a></sup> against TrendForce's observed 33% <sup class="ref"><a href="https://vocal.media/futurism/data-center-liquid-cooling-market-outlook-efficient-thermal-management-and-growth-opportunities" title="TrendForce liquid cooling penetration in AI-focused data centers climbed from 14% to 33%" rel="noopener">ref</a></sup>. The market sizings, ranging from roughly $7B by 2029 <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup> to $17.8B by 2036 <sup class="ref"><a href="https://www.morningstar.com/news/accesswire/1163831msn/ai-datacenter-liquid-cooling-market-to-reach-usd-178-billion-by-2036-as-hyperscale-ai-infrastructure-drives-thermal-management-transformation" title="AI Datacenter Liquid Cooling Market to Reach USD 17.8 Billion by 2036" rel="noopener">ref</a></sup> to a figure quoted in trillions <sup class="ref"><a href="https://www.technavio.com/report/liquid-cooling-for-ai-data-centers-market-industry-analysis" title="Liquid Cooling For AI Data Centers Market Growth Analysis - Size and Forecast 2026-2030" rel="noopener">ref</a></sup>, are not internally consistent and should not be used to underwrite anything.

Two sub-positions are worth separating from the fairly-rated whole. Two-phase immersion looks overrated relative to the attention it receives, held to under 15% of new builds by 2030 **2024 Yole Thermal Management 2024** with no fielded evidence in these sources. In-package microfluidics looks underrated: a 15% thermal resistance improvement at the layer Yole identifies as binding above 1.5kW packages **2024 Yole Thermal Management 2024**, already integrated into CoWoS and offered as a qualified Intel package option <sup class="ref"><a href="https://www.servethehome.com/intel-foundry-thermal-capabilities-with-tim-options-and-in-package-liquid-cooling-shown/" title="Intel Foundry Thermal Capabilities with TIM Options and In-Package Liquid Cooling Shown" rel="noopener">ref</a></sup>, is the mechanism by which cooling margin migrates from facility vendors into the foundry. If you are looking for where the profit pool moves, look there rather than at the cold plate.

## Prediction

Of new hyperscaler AI training datacentre commissionings of 50MW or more per site announced during 2027, more than 50% will specify direct-to-chip liquid cooling as the primary thermal architecture in published commissioning materials.

## Evidence base

- Goldman Sachs forecasts liquid-cooled AI servers rising from 15% in 2024 to 76% by end-2026, driven by full-rack liquid-cooling solutions <sup class="ref"><a href="https://www.lombardodier.com/insights/2026/january/ai-supercharges-the-race.html" title="Goldman Sachs forecasts liquid-cooled AI servers will increase from 15% in 2024 to 76% in 2026" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://alcapitaladvisory.com/research/intelligence/ai-infrastructure.html" title="Goldman Sachs AI Infrastructure Analysis: Liquid Cooling as Non-Discretionary" rel="noopener">ref</a></sup>.
- TrendForce measured liquid cooling penetration in AI-focused datacentres climbing from 14% to 33%, with liquid-based cooling at 46% of the total datacentre cooling market, as rack densities move from 40kW to 140kW (2026-04-19) <sup class="ref"><a href="https://vocal.media/futurism/data-center-liquid-cooling-market-outlook-efficient-thermal-management-and-growth-opportunities" title="TrendForce liquid cooling penetration in AI-focused data centers climbed from 14% to 33%" rel="noopener">ref</a></sup>.
- Dell'Oro puts the datacentre liquid cooling market near $7B by 2029 and frames liquid cooling as a foundational requirement rather than a niche (2026-01-08) <sup class="ref"><a href="https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/" title="Data Center Liquid Cooling Market to Approach $7 Billion by 2029 as AI Deployments Accelerate" rel="noopener">ref</a></sup>.
- Yole (Oct 2024) expects direct-to-chip to be the default in AI training builds by 2027, two-phase immersion to stay under 15% of new builds by 2030, total AI accelerator thermal management to grow from ~$8B to $25B+ by 2030, and lid TIM to become the binding thermal layer above 1.5kW package TDP **2024 Yole Thermal Management 2024**.
- TSMC's IMC-Si reports ~0.055 °C/W thermal resistance, roughly 15% better than the best external cold plate, and over 7 W/mm² on logic backside with DI water, integrated into CoWoS-R/CoWoS-L; Corintis raised $24M in Sep 2025 and targets over 1M cold plates a year by end-2026 <sup class="ref"><a href="https://tspasemiconductor.substack.com/p/cooling-is-the-new-architecture-tsmcs" title="Cooling is the New Architecture: TSMC's IMC-Si and the Future of AI Packaging" rel="noopener">ref</a></sup>.
- Oracle announced in February 2026 that new AI campuses use closed-loop non-evaporative direct-to-chip cooling as the primary thermal architecture <sup class="ref"><a href="https://nextwavesinsight.com/ai-data-center-liquid-cooling-infrastructure/" title="Oracle Announces Direct-to-Chip Cooling for AI Campuses" rel="noopener">ref</a></sup>; Intel showed in-package liquid cooling as a qualified foundry package option in May 2025 <sup class="ref"><a href="https://www.servethehome.com/intel-foundry-thermal-capabilities-with-tim-options-and-in-package-liquid-cooling-shown/" title="Intel Foundry Thermal Capabilities with TIM Options and In-Package Liquid Cooling Shown" rel="noopener">ref</a></sup>.

## Open questions

- Does the gap between TrendForce's observed 33% penetration in AI datacentres and Goldman's forecast 76% of AI servers by end-2026 close, or was the forecast an over-extrapolation?
- How much of the cooling value pool migrates into the package? Does a second top-tier foundry or OSAT beyond TSMC and Intel qualify an in-package microfluidic option, and do design wins follow?
- What is the retrofit economics of converting existing air-cooled halls, and what share of installed capacity is simply stranded for AI workloads? None of the sources address this.
- Does two-phase immersion stay under 15% of new builds through 2030, or does a specific flux or fluid constraint break Yole's segmentation view?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
