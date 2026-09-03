---
type: concept
slug: microfluidic-cooling
canonical_name: Microfluidic Cooling
aliases: []
parent_concepts:
- thermal-management
- energy-power
related_concepts: []
sources:
- '[[2025-12-16-datacentre-thermal-power-market-boston-materials-liquid]]'
- '[[2026-06-22-thermal-stack-layer-landscape]]'
- '[[2026-07-09-in-die-microfluidic-cooling-sprint]]'
- '[[2025-09-25-corintis-microsoft-in-chip-microfluidic-cooling]]'
- '[[2026-01-01-datacentre-thermal-power-market-accelsius-announces-general]]'
- '[[2026-05-07-datacentre-thermal-power-market-microsoft-partners-with]]'
- '[[2025-11-10-datacentre-thermal-power-market-microsoft-s-in-chip]]'
- '[[2025-05-27-datacentre-thermal-power-market-intel-foundry-s-integrated]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 11
frontier:
- Does any in-package microfluidic or advanced-TIM supplier convert a hyperscaler or accelerator-vendor engagement into a disclosed design win (not a pilot) by 2028, or does the layer stay pilot-only with incumbent cold-plate and TIM vendors holding it?
- Does a top-tier foundry or OSAT list an in-package thermal primitive as a qualified package option by end-2027, and on what terms relative to specialists like Corintis and EMCOOL?
- Do the 3x heat-removal and 65% peak-temperature-rise figures survive independent or peer-reviewed replication, and at what flow rate, pressure drop and pumping power?
- Does Corintis actually reach the stated >1M microfluidic cold plates per year by end-2026, and what fraction of that volume is in-die rather than external copper microfluidic plates?
- What are the reliability, erosion, fouling and field-serviceability results for coolant channels inside the die backside over multi-year operation?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-09-02-vertical-power-delivery-thermal-limits
  title: 'Vertical power delivery: the thermal limit at the 48V-to-point-of-load stage'
  date: '2026-09-02'
  kind: web
- slug: 2026-07-09-in-die-microfluidic-cooling-sprint
  title: In-die microfluidic cooling — cluster research sprint
  date: '2026-07-09'
  kind: web
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-05-07-datacentre-thermal-power-market-microsoft-partners-with
  title: Microsoft partners with Corintis for bio-inspired in-chip microfluidic cooling
  date: '2026-05-07'
  kind: web
- slug: 2026-01-01-datacentre-thermal-power-market-accelsius-announces-general
  title: Accelsius announces general availability of NeuCool IR150 at Data Center World 2026
  date: '2026-01-01'
  kind: web
- slug: 2025-12-16-datacentre-thermal-power-market-boston-materials-liquid
  title: Boston Materials' Liquid Metal ZRT brings 10°C lower GPU temps in kilowatt-sized liquid-cooled AI accelerators
  date: '2025-12-16'
  kind: web
- slug: 2025-11-10-datacentre-thermal-power-market-microsoft-s-in-chip
  title: Microsoft's In-Chip Microfluidics Technology Resets the Limits of AI Cooling
  date: '2025-11-10'
  kind: web
- slug: 2025-09-25-corintis-microsoft-in-chip-microfluidic-cooling
  title: 'Microsoft + Corintis in-chip microfluidic cooling: 3x heat removal vs cold plates, 65% peak-temp reduction'
  date: '2025-09-25'
  kind: web
neighbors: []
---
## Physics / mechanism

Microfluidic cooling moves the coolant boundary from an external cold plate to channels etched into or immediately adjacent to the silicon, removing one or more conductive interfaces (thermal interface material, lid, base plate) from the junction-to-ambient path. Microsoft's implementation with Corintis routes coolant through roughly 15 µm bio-inspired branching channels, patterned in leaf-vein and butterfly-wing geometries, with AI used to map die hotspots and lay out the channel network so flow is concentrated where power density is highest <sup class="ref"><a href="https://www.datacenterdynamics.com/en/news/microsoft-partners-with-corintis-for-bio-inspired-in-chip-microfluidic-cooling/" title="Microsoft + Corintis in-chip microfluidic cooling: 3x heat removal vs cold plates, 65% peak-temp reduction" rel="noopener">ref</a></sup>.

The governing parameters are hydraulic channel dimension, thermal resistance per watt, and how much of the stack the coolant displaces. TSMC's IMC-Si (Si-Integrated Micro Cooler) uses MEMS-etched mesh and stripe microchannels of 30 to 150 µm fusion-bonded to the die backside, eliminating the TIM layer entirely, with reported thermal resistance around 0.055 °C/W, about 15% better than the best comparison case, and integration into CoWoS-R and CoWoS-L packaging. The same primitive was demonstrated at IEEE ECTC 2025.

Claimed performance at the device level: up to 3x the heat removal of conventional cold plates and up to a 65% reduction in peak silicon temperature rise in GPU tests <sup class="ref"><a href="https://www.datacenterdynamics.com/en/news/microsoft-partners-with-corintis-for-bio-inspired-in-chip-microfluidic-cooling/" title="Microsoft + Corintis in-chip microfluidic cooling: 3x heat removal vs cold plates, 65% peak-temp reduction" rel="noopener">ref</a></sup>. These figures are vendor-demonstrated and not peer-reviewed, and the lineage traces to IBM Zurich embedded cooling work of 2008 to 2013 that was never productised.

Not all products in the category etch channels into the die. Corintis currently ships copper microfluidic cold plates, with a roadmap to channels inside the package, alongside Glacierware cooling-design software and Therminator thermal-emulation test chips. EMCOOL's approach is an embedded microfluidic pin-fin block integrated into the package.

## Competitive landscape

The contest is over which layer captures the margin: a specialist pure-play, the foundry/OSAT absorbing the primitive as a qualified package option, or incumbent cold-plate and TIM vendors holding the interface.

| Approach | Representative player | Reported metric |
|---|---|---|
| In-die / embedded microchannels | Corintis with Microsoft; EMCOOL | up to 3x heat removal vs cold plates, 65% lower peak temp rise <sup class="ref"><a href="https://www.datacenterdynamics.com/en/news/microsoft-partners-with-corintis-for-bio-inspired-in-chip-microfluidic-cooling/" title="Microsoft + Corintis in-chip microfluidic cooling: 3x heat removal vs cold plates, 65% peak-temp reduction" rel="noopener">ref</a></sup> |
| Foundry-integrated micro cooler | TSMC IMC-Si; Intel Foundry integrated cold plate | ~0.055 °C/W, ~15% better than best comparison; 20% thermal and 15% performance improvement in early testing <sup class="ref"><a href="https://newsroom.intel.com/intel-foundry/burning-buildings-pave-the-way-to-advances-in-ai" title="Intel Foundry's Integrated Cold Plate: Thermal Innovation for Next-Gen AI" rel="noopener">ref</a></sup> |
| Two-phase direct-to-chip (external) | Accelsius NeuCool IR150 | general availability, hyperscale AI pilots <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/0002001557/000114036126015808/ef20071067_ex99-1.htm" title="Accelsius announces general availability of NeuCool IR150 at Data Center World 2026" rel="noopener">ref</a></sup> |
| Advanced TIM (keeps external cold plate) | Boston Materials Liquid Metal ZRT | 10 °C reduction in kilowatt-class liquid-cooled accelerators <sup class="ref"><a href="https://www.igorslab.de/en/overview-of-new-developments-in-thermal-interface-materials-tim/" title="Boston Materials' Liquid Metal ZRT brings 10°C lower GPU temps in kilowatt-sized liquid-cooled AI accelerators" rel="noopener">ref</a></sup> |

## Evidence base

- Microsoft announced an in-chip microfluidic cooling system co-developed with Corintis on 25 September 2025, using ~15 µm bio-inspired branching channels and AI-designed hotspot mapping <sup class="ref"><a href="https://www.datacenterdynamics.com/en/news/microsoft-partners-with-corintis-for-bio-inspired-in-chip-microfluidic-cooling/" title="Microsoft + Corintis in-chip microfluidic cooling: 3x heat removal vs cold plates, 65% peak-temp reduction" rel="noopener">ref</a></sup>.
- Corintis raised a $24M Series A led by BlueYard Capital (Founderful, Acequia, Celsius Industries, XTX Ventures) announced 25 September 2025, with Lip-Bu Tan and Geoff Lyon joining the board.
- Corintis had shipped more than 10,000 cold plates and targeted scaling to over 1M microfluidic units per year by end-2026.
- Intel Foundry was developing integrated cold plates (in-package microfluidic cooling) as of 27 May 2025, with early testing showing 20% thermal improvement and 15% performance gains versus conventional approaches <sup class="ref"><a href="https://newsroom.intel.com/intel-foundry/burning-buildings-pave-the-way-to-advances-in-ai" title="Intel Foundry's Integrated Cold Plate: Thermal Innovation for Next-Gen AI" rel="noopener">ref</a></sup>.
- TSMC demonstrated IMC-Si at IEEE ECTC 2025: microchannels fusion-bonded to the die backside, no TIM, integrating into CoWoS-R and CoWoS-L.
- Datacenter Frontier reported on 10 November 2025 that Microsoft demonstrated up to 3x better heat removal versus cold plates, acknowledging Corintis as design partner <sup class="ref"><a href="https://www.datacenterfrontier.com/cooling/article/55326929/microsofts-in-chip-microfluidics-technology-resets-the-limits-of-ai-cooling" title="Microsoft's In-Chip Microfluidics Technology Resets the Limits of AI Cooling" rel="noopener">ref</a></sup>.
- Accelsius reached general availability of the NeuCool IR150 two-phase direct-to-chip system, with several hyperscale AI providers engaged under pilot programmes as of 1 January 2026 <sup class="ref"><a href="https://www.sec.gov/Archives/edgar/data/0002001557/000114036126015808/ef20071067_ex99-1.htm" title="Accelsius announces general availability of NeuCool IR150 at Data Center World 2026" rel="noopener">ref</a></sup>.

## Frontier (open questions)

- Does any in-package microfluidic or advanced-TIM supplier convert a hyperscaler or accelerator-vendor engagement into a disclosed design win (not a pilot) by 2028, or does the layer stay pilot-only with incumbent cold-plate and TIM vendors holding it?
- Does a top-tier foundry or OSAT list an in-package thermal primitive as a qualified package option by end-2027, and on what terms relative to specialists like Corintis and EMCOOL?
- Do the 3x heat-removal and 65% peak-temperature-rise figures survive independent or peer-reviewed replication, and at what flow rate, pressure drop and pumping power?
- Does Corintis actually reach the stated >1M microfluidic cold plates per year by end-2026, and what fraction of that volume is in-die rather than external copper microfluidic plates?
- What are the reliability, erosion, fouling and field-serviceability results for coolant channels inside the die backside over multi-year operation?

*Synthesised 2026-08-31 from 8 KB sources by the resynth pipeline; citations are KB source slugs.*
