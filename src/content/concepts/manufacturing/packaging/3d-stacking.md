---
type: concept
slug: 3d-stacking
canonical_name: 3d Stacking
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2024-yole-emerging-memories-2024]]'
- '[[2026-01-13-semianalysis-interconnects-beyond-copper]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 23
frontier:
- Where does the die-cost minimum identified by Walker actually fall for current deck-stacked architectures, and has the industry already passed it at 321 layers?
- Does positive-threshold engineering, for example ferroelectric layer thinning, raise 3D FeNOR stacking density enough to matter, or does sneak current cap monolithic 3D emerging memory at a commercially uninteresting layer count?
- Does the process-step penalty per added deck stay near the 30%-for-44% ratio, or does it deteriorate with the fourth and fifth decks?
- 'Do package-level stacking economics, hybrid bonding and chiplets, exhibit their own cost minimum analogous to the monolithic case, and if so what sets it: bonding pitch, yield or thermal dissipation?'
- At what layer count does the die-cost minimum actually fall for current multi-deck processes, and has deck-splitting moved that minimum relative to Walker's 2013 model, or merely deferred it walker 2013 rigorous 3d nand flash cost analysis?
- Does the ~30%-steps-for-~44%-density ratio at 321 layers hold, degrade or improve at the next deck addition 2026 01 13 semianalysis interconnects beyond copper?
- Has any lithography-intensive layered 3D memory been demonstrated in volume at lower cost per bit than vertical-channel NAND, as Walker's model predicts is possible?
- Can NOR-type stacked arrays suppress sneak current enough to preserve sensing margin at full monolithic 3D layer counts, rather than only at the single-layer or few-layer BEOL level 2026 06 05 dtco of nor type igzo fefets for 3d heterogeneous ai memorie?
scorecard:
  viability: 5
  drivers: 4
  novelty: 4
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-01-13-semianalysis-interconnects-beyond-copper
  title: Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More
  date: '2026-01-13'
  kind: web
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
- slug: 2023-08-31-e13-chiplets-how-chip-lego-is-driving
  title: '🔮 E13: Chiplets - How Chip Lego is Driving AI Progress'
  date: '2023-08-31'
  kind: substack
neighbors: []
---
**3D stacking is the practice of building chips upwards rather than outwards, and it is already the dominant scaling lever in NAND flash and AI memory, but the sources show each added layer buys less density than the last and the cost per bit eventually turns back up.**

## Summary

3D stacking covers two related but distinct engineering families. The first is **monolithic 3D**: layers of devices are fabricated one above another on the same wafer, as in 3D NAND flash, back-end-of-line (BEOL) memory arrays built above the logic, and stacked-transistor schemes such as CFET. The second is **package-level 3D**: separately manufactured dies are thinned, aligned and bonded on top of each other, as in HBM DRAM stacks and hybrid-bonded memory chiplets. Both are responses to the same problem: planar area is expensive and lithographic shrink has slowed, so the cheapest remaining dimension is vertical.

The physics that decides monolithic 3D is deep-etch geometry. A high-aspect-ratio hole or slit cannot be etched with perfectly vertical walls, so it is wider at the top of the stack than at the bottom. Walker's cost model shows the cell pitch at the top of the stack, which is what defines the array footprint, grows **linearly in layer count** through a term proportional to `2·N_L(L_g + L_s)·tanθ` **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. More layers means fewer cells needed per layer, which shrinks footprint, but a larger top-of-stack pitch, which grows it. The two effects cross, producing a **minimum in die cost** beyond which adding layers makes the part more expensive, not cheaper **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. The same paper shows a lithography-intensive layered approach using three critical masks per device layer can reach a smaller die and undercut vertical-channel 3D NAND on total cost, which inverts the industry's usual assumption about which route is cheap.

Production data is consistent with diminishing returns. SK Hynix's 321-layer V9 NAND adds a **third processing deck** to reach roughly **44% higher density for about 30% more process steps** <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>. That is still a favourable trade, but it is a trade, not free scaling, and it tells you the industry has stopped trying to etch a single continuous stack.

For emerging memories the binding parameter is electrical, not geometric. A read-centric DTCO study of NOR-type IGZO FeFETs finds 3D stacking density in monolithic 3D FeNOR storage-class memory is **limited by read margin**, because sneak current associated with a negative program-state threshold voltage erodes sensing, requiring positive-threshold engineering such as ferroelectric layer thinning. Ferroelectric non-volatile capacitors are similarly described as having 3D stacking potential but a memory window of only **1 to 10 fF/µm** and sense margins in the ±5 mV range after co-optimisation. So the ceiling on any given 3D memory is set by whichever runs out first: etch taper, process-step cost, thermal budget, bonding pitch, or the signal left at the sense amplifier.

## Viability (5/5)

This is not a laboratory technology. A 321-layer, three-deck 3D NAND product is described as shipping-grade engineering with a quantified density and process-step cost <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>, and Yole expects eFlash to retain **more than 50% of embedded non-volatile memory at 40nm and above partly via 3D stacking** **2024 Yole Emerging Memories 2024**. Package-level stacking is equally established: HBM's stacked DRAM is treated as the enabling component for large language model training <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e14-the-real-ai-bottleneck-high-bandwidth" title="🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM) " rel="noopener">ref</a></sup>.

The qualification is that viability is proven for the mature variants and unproven for the frontier ones. Monolithic 3D of emerging memories above logic is still at the DTCO and compact-modelling stage, with density explicitly capped by read margin in 3D FeNOR arrays and with ferroelectric capacitor memory windows measured in single-digit femtofarads per micron. Stacked logic via CFET is described as showing better-than-expected ring-oscillator and SRAM progress, which is early-demonstration language, not production language <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>.

**TLDR: In high-volume production across NAND, embedded flash and AI memory stacks; the debate is about returns, not feasibility.**

## Drivers (4/5)

**Demand.** The pull is memory, not logic. HBM is framed as the real bottleneck in AI systems <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e14-the-real-ai-bottleneck-high-bandwidth" title="🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM) " rel="noopener">ref</a></sup>, and higher-layer NAND is tied directly to datacentre storage density <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>. There is also a research-funded pull towards 3D integration for workloads that need tight memory-logic coupling, such as the NSF CAREER award of **$366,820** to Purdue for neuro-symbolic computing on three-dimensional integrated circuits, dated 13 May 2026. On the embedded side, Yole sees stacking as what keeps eFlash competitive at trailing nodes rather than as a growth story in itself **2024 Yole Emerging Memories 2024**.

**Supply.** The constraints are capital and process. Each added deck costs process steps at a roughly one-to-two-thirds ratio against density gained in the SK Hynix case <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>, and the deep-etch taper angle sets a hard geometric limit on how far a single deck can go **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. Walker's finding that a litho-intensive layered route can undercut the vertical-channel route means the supply-side answer may shift capital demand from etch towards lithography rather than reducing it **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. Thermal management of dense vertical assemblies is raised in the sources as an open datacentre problem rather than a solved one <sup class="ref"><a href="https://stateofthefuture.substack.com/p/carbon-nanotubes-in-the-datacentre" title="Carbon Nanotubes in the Datacentre" rel="noopener">ref</a></sup>.

**TLDR: Demand is AI memory bandwidth and bit density; supply is constrained by process steps, deep-etch capability and thermal budget.**

## Novelty (4/5)

The comparison that matters is against planar shrink, and 3D stacking wins there clearly: the whole rationale for adding decks is that vertical density is available when lateral density is not, and the measured gain is around **44% density for 30% more process steps** at 321 layers <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>. Against other density levers the picture is more contested. Multi-site cell schemes pointing to 5 bits per cell are described as manufacturing-hard <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>, and post-copper interconnect metals such as ruthenium and molybdenum address a different constraint entirely <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>.

The important novelty correction comes from Walker. The premise on which vertical-channel 3D NAND was sold, that die cost per bit falls monotonically with added device layers, is shown to be **false**: there is a cost minimum, after which cost rises with every additional layer **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. The same analysis shows an alternative layered, three-critical-masks-per-layer architecture can reach a smaller die and undercut the incumbent approach on total cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. So the technique is genuinely novel and valuable, but the axis on which the industry usually markets it, layer count, is not a reliable proxy for advantage.

**TLDR: Decisively better than planar scaling for bit density, but the specific claim of monotonically falling cost per bit is wrong.**

## Diffusion (4/5)

For NAND and HBM, diffusion is essentially complete. Where diffusion is unfinished is the extension of stacking into logic and into new memory materials. Chiplets, the package-level entry point, took a decade from the first chiplet-architecture part, the Xilinx Virtex-7 in **2011**, to a market worth about **$3 billion in 2021**, roughly **0.5% of a $600 billion semiconductor market** <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e13-chiplets-how-chip-lego-is-driving" title="🔮 E13: Chiplets - How Chip Lego is Driving AI Progress " rel="noopener">ref</a></sup>. That is the relevant base rate for how slowly packaging architectures propagate outside the memory vendors.

The technical barriers named in the sources are specific. Monolithic 3D emerging memory hits sensing limits: sneak current from negative program-state threshold voltages caps 3D FeNOR stacking density and requires positive-threshold engineering to fix. Ferroelectric capacitor memories need material-device-circuit co-optimisation to reach even ±5 mV sense margin. Adjacent 3D-enabling channel materials are blocked: 2D transition-metal dichalcogenides suffer contact resistance, weak p-type behaviour and integration problems <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>. And Yole is explicit that FeFET, one of the candidate BEOL-stackable memories, does **not** displace HBM at the AI accelerator memory layer through 2030 **2024 Yole Emerging Memories 2024**.

**TLDR: Already diffused in memory; the barriers bite for stacked logic, monolithic emerging memory and chiplet-based 3D.**

## Impact (4/5)

The value case is large because the bottleneck it addresses is large. HBM, a stacked-memory product, is characterised as the component without which large language models do not exist <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e14-the-real-ai-bottleneck-high-bandwidth" title="🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM) " rel="noopener">ref</a></sup>, and NAND layer count is the lever for datacentre storage density <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>. At the embedded end, stacking is what preserves the majority share of a mature, high-volume memory category at trailing nodes **2024 Yole Emerging Memories 2024**. Research funders are treating 3D integration as foundational to next-generation AI hardware rather than as an incremental packaging option.

The reason this is not a 5 is that the sources also bound the upside. Cost per bit does not fall indefinitely with layer count **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**, additional decks carry a proportionate process-step penalty <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>, and the most attractive 3D memory-on-logic configurations are still limited by read margin rather than by geometry. Thermal dissipation from densely stacked assemblies is flagged as an unresolved datacentre-level problem <sup class="ref"><a href="https://stateofthefuture.substack.com/p/carbon-nanotubes-in-the-datacentre" title="Carbon Nanotubes in the Datacentre" rel="noopener">ref</a></sup>.

**TLDR: It is the mechanism keeping memory density and bandwidth on curve, which is where the AI hardware constraint sits.**

## Timing Now (0-2yr)

There is nothing speculative about the near term. Three-deck 321-layer NAND and stacked HBM are shipping technologies as of the January 2026 roundup <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e14-the-real-ai-bottleneck-high-bandwidth" title="🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM) " rel="noopener">ref</a></sup>, and stacking is already the reason a mature embedded memory holds its share **2024 Yole Emerging Memories 2024**.

The frontier sits further out. Yole's horizon puts FeFET and HfO2-FeRAM at 5% or more of embedded non-volatile units by 2030 and explicitly rules out displacement of HBM through 2030 **2024 Yole Emerging Memories 2024**. CFET stacked logic is at the ring-oscillator and SRAM demonstration stage <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>, and monolithic 3D FeNOR remains at the DTCO stage with unresolved sensing limits. Treat those as Later (5-10 yr) inside a technology whose mainstream form is Now.

**TLDR: Mainstream 3D stacking is a current production reality; stacked logic and monolithic 3D emerging memory are the 5-to-10-year part.**

## Overrated or underrated? Fairly rated

3D stacking as a category is correctly valued: it is the load-bearing scaling mechanism for memory, it is in volume production, and the market prices that. What is overrated is the specific metric the industry and its commentators use as shorthand for progress, namely layer count. Walker's cost model, which predates the current layer-count race, shows the premise that die cost per bit falls monotonically with layers is false and that a cost minimum exists **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**. The move to a third processing deck to reach 321 layers, buying 44% density for 30% more steps, is exactly what you would expect from a technology working around a geometric limit rather than scaling through it <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>.

The practical read for an investor is that the value is migrating from etch depth towards two other places: the process-step and lithography intensity of deck-stacked architectures, which Walker argues can favour a litho-heavy layered route **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**, and the electrical design work needed to make monolithic 3D memory arrays readable at all. Anyone underwriting a 3D story on the assumption that more layers automatically means cheaper bits is underwriting a claim the tier-1 literature has already refuted.

## Prediction

Any commercially announced NAND product exceeding 400 layers before the end of 2028 will be built from three or more separately processed decks rather than a single continuous high-aspect-ratio etch.

## Evidence base

- November 2013: Walker's cost model shows 3D NAND die cost per bit does not fall monotonically with device layers; a cost minimum exists because top-of-stack cell pitch grows linearly in layer count via deep-etch taper, and a litho-intensive layered route can undercut vertical-channel 3D on total cost **Walker 2013 Rigorous 3D Nand Flash Cost Analysis**.
- 13 January 2026: SK Hynix's 321-layer V9 3D NAND adds a third processing deck for roughly 44% higher density at roughly 30% more process steps; CFET is framed as the successor to gate-all-around with better-than-expected ring-oscillator and SRAM results <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>.
- 15 October 2024: Yole expects eFlash to retain more than 50% of embedded non-volatile memory at 40nm and above via 3D stacking, and states FeFET does not displace HBM at the AI accelerator memory layer through 2030 **2024 Yole Emerging Memories 2024**.
- 5 June 2026: a read-centric DTCO study of NOR-type IGZO FeFETs reports bitcell area down to about 0.016 µm2 with 7nm ground rules and sub-5 ns random access, but finds monolithic 3D FeNOR stacking density limited by read margin due to sneak current from negative program-state threshold voltage.
- 18 June 2026: ferroelectric non-volatile capacitance memories are credited with 3D stacking potential but constrained by a 1 to 10 fF/µm memory window, with co-optimised read-out achieving about ±5 mV sense margin.
- 13 May 2026: NSF awarded $366,820 to a Purdue CAREER project using advanced three-dimensional integration and specialised memories for neuro-symbolic AI hardware.
- 31 August 2023: the chiplet market, the package-level route to 3D, was worth about $3 billion in 2021, roughly 0.5% of a $600 billion semiconductor market, twelve years after the first chiplet-architecture part in 2011 <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e13-chiplets-how-chip-lego-is-driving" title="🔮 E13: Chiplets - How Chip Lego is Driving AI Progress " rel="noopener">ref</a></sup>.

## Open questions

- Where does the die-cost minimum identified by Walker actually fall for current deck-stacked architectures, and has the industry already passed it at 321 layers?
- Does positive-threshold engineering, for example ferroelectric layer thinning, raise 3D FeNOR stacking density enough to matter, or does sneak current cap monolithic 3D emerging memory at a commercially uninteresting layer count?
- Does the process-step penalty per added deck stay near the 30%-for-44% ratio, or does it deteriorate with the fourth and fifth decks?
- Do package-level stacking economics, hybrid bonding and chiplets, exhibit their own cost minimum analogous to the monolithic case, and if so what sets it: bonding pitch, yield or thermal dissipation?

---
*Assessment drafted 2026-08-31 from up to 11 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
