---
type: concept
slug: carbon-nanotubes
canonical_name: Carbon Nanotubes
aliases: []
kind: technology
parent_concepts:
- materials
- advanced-materials
related_concepts: []
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-08-19-thermal-stack-arms-race-thermal-interface-materials-market]]'
- '[[2026-06-17-nawah-vacnt-technology]]'
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 34
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-06-17-nawah-vacnt-technology
  title: NAWAH Architectured Nanomaterials — VACNT technology & positioning
  date: '2026-06-17'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-08-19-thermal-stack-arms-race-thermal-interface-materials-market
  title: 'Thermal Interface Materials Market Report 2026-2036: High-Performance TIMs for Data Centers, AI Servers, and 5G Infrastructure'
  date: '2025-08-19'
  kind: web
- slug: 2025-07-01-a-primer-carbon-nanotubes
  title: 'A Primer: Carbon Nanotubes'
  date: '2025-07-01'
  kind: substack
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
neighbors: []
---
**Carbon nanotubes are rolled-up graphene cylinders whose chirality sets whether they conduct like a metal or a semiconductor, and after three decades they are shipping as bulk additives, composites and thermal materials while the high-value prize, replacing silicon as a logic channel, remains blocked by contacts, doping and purity.**

## Summary

A carbon nanotube (CNT) is a seamless cylinder of graphitic carbon, either single-walled (SWCNT) or multi-walled. The electronic structure follows from folding the graphene band structure onto the tube circumference: the resulting chirality and diameter decide whether a given tube is metallic or semiconducting and, if semiconducting, what its bandgap is. Transport in a clean SWCNT approaches the ballistic limit, and the wrap-around geometry gives close to ideal electrostatic control of a channel, which is the basis of the argument that SWCNTs are the natural successor channel material once silicon CMOS runs into direct source-to-drain tunnelling, an unscalable subthreshold swing and the dark-silicon thermal ceiling.

The same object has three quite different commercial lives. First, as a bulk material: dispersed powder used as a conductive or structural additive, and vertically aligned CNT (VACNT) forests grown and transferred onto prepregs, veils and films for composites, catalysts, thermal interfaces, electrodes and sensors <sup class="ref"><a href="https://nawah.us/architectured-nanomaterials/technology/" title="NAWAH Architectured Nanomaterials — VACNT technology & positioning" rel="noopener">ref</a></sup>. Second, as a functional single object: chirality-sorted tubes as near-infrared emitters, strain transducers or quantum-confinement templates. Third, as an electronic channel in transistors, which is where nearly all the unsolved problems sit.

The parameters that decide outcomes are consistent across the literature. Chirality and diameter set the band structure and must be controlled or sorted after growth, typically today by density gradient ultracentrifugation in the lab. Wall number, intertube spacing and diameter govern the mechanics of assembled architectures such as graphene-CNT stacks and aerogels. Environment matters as much as the tube: the same nanotube shows higher field-effect mobility where it lies on hexagonal boron nitride than where it lies on SiO2, measured within a single tube to remove chirality and defect variability. Stable doping, especially n-type, is still hard because of environmental sensitivity and competing extrinsic effects, which is why encapsulating charge-transfer molecules inside the tube cavity is being pursued as a route that leaves the outer surface free for processing. And the contact remains a first-order problem: Schottky barrier height, transfer length and contact resistance in low-dimensional channels are set by metal-induced gap states whose scaling depends on dimensionality.

## Viability (3/5)

Split the question. As a material, CNTs demonstrably work and are supplied commercially: a B2B vendor sells VACNT with customised length, density and microstructuration, with masters for transfer and encapsulation onto prepregs, veils and films, and 26 patents filed and granted <sup class="ref"><a href="https://nawah.us/architectured-nanomaterials/technology/" title="NAWAH Architectured Nanomaterials — VACNT technology & positioning" rel="noopener">ref</a></sup>. Practitioner accounts describe tonne-scale manufacture with falling cost and improving consistency, in EV batteries, aerospace composites, thermal materials and polymers <sup class="ref"><a href="https://stateofthefuture.substack.com/p/a-primer-carbon-nanotubes" title="A Primer: Carbon Nanotubes" rel="noopener">ref</a></sup>. As individual functional objects they also work: chirality-sorted, quantum-colour-centre-functionalised (6,5) tubes gave a two-photon action cross-section of 57 ± 2 × 10^3 GM at 1700 nm excitation and the first reported single-particle imaging at that wavelength.

As a silicon replacement it does not work yet, and the 2026 literature is still writing the physics rather than the process. Doping, particularly n-type, remains unreliable because of environmental sensitivity, and the proposed fix, endohedral encapsulation, is being evaluated at the level of comparing melt filling, solution reflux and vacuum sublimation and then separating filled from empty and metallic from semiconducting tubes by ultracentrifugation. Contact physics is only now getting a unified analytical treatment of Schottky barrier, transfer length and contact resistance that explains recent CNT experiments. Best mobility so far depends on sitting the tube on hBN rather than SiO2, which is a research substrate, not a fab flow. A 3 reflects a credible but contested technology whose highest-value use case is unproven.

**TLDR: Bulk material and single-tube demonstrations work; the logic-transistor path is still blocked at contacts, doping and purity.**

## Drivers (4/5)

Demand: the case is made explicitly on the electronics side, where silicon CMOS is approaching hard physical limits including source-to-drain tunnelling and the dark-silicon thermal ceiling, motivating the search for a new channel material. A second, nearer pull is heat removal in data centres, AI servers and 5G infrastructure, where CNTs sit alongside graphene-enhanced materials, metal-based TIMs and metamaterials as candidate thermal interface materials <sup class="ref"><a href="https://www.globenewswire.com/news-release/2025/08/19/3135485/28124/en/Thermal-Interface-Materials-Market-Report-2026-2036-High-Performance-TIMs-for-Data-Centers-AI-Servers-and-5G-Infrastructure-Global-Outlook.html" title="Thermal Interface Materials Market Report 2026-2036: High-Performance TIMs for Data Centers, AI Servers, and 5G Infrastr" rel="noopener">ref</a></sup>, a framing echoed by practitioner writing on datacentre thermals <sup class="ref"><a href="https://stateofthefuture.substack.com/p/carbon-nanotubes-in-the-datacentre" title="Carbon Nanotubes in the Datacentre" rel="noopener">ref</a></sup>. Industrial strain measurement is a third pull: an NSF SBIR Fast-Track award of $1,549,408 dated 17 June 2026 backs a CNT-based optically read strain sensor aimed initially at aerospace, on the argument that all currently available strain methods have drawbacks.

Supply: production exists at industrial scale for aligned forests, with customer-specific control of length and density and transfer onto multiple substrates <sup class="ref"><a href="https://nawah.us/architectured-nanomaterials/technology/" title="NAWAH Architectured Nanomaterials — VACNT technology & positioning" rel="noopener">ref</a></sup>, and cost and consistency are reported to have improved to the point where CNTs appear in shipped products <sup class="ref"><a href="https://stateofthefuture.substack.com/p/a-primer-carbon-nanotubes" title="A Primer: Carbon Nanotubes" rel="noopener">ref</a></sup>. What the sources do not give is volume, price per kilogram or the number of qualified suppliers, so the supply side is asserted rather than quantified. The score is driven mainly by the clarity and size of the demand signals.

**TLDR: Demand pull from silicon's scaling limits and datacentre heat is strong; supply is real but concentrated in specialty vendors.**

## Novelty (3/5)

Against silicon, the claimed advantage is structural rather than incremental: near-ballistic transport and coaxial electrostatics that suppress short-channel effects, benchmarked in the review against published 5 nm experimental data showing aggressive subthreshold degradation from source-to-drain tunnelling in the incumbent. That is a theoretical margin, derived from zone folding and Landauer-Buttiker analysis, not a fabricated product comparison. Against other emitters, the advantage is measured: quantum-colour-centre (6,5) tubes emitting at 1140 nm have an exceptionally large two-photon action cross-section of 57 ± 2 × 10^3 GM at 1700 nm, a window where efficient fluorophores are scarce, and enabled single-particle imaging that had previously been precluded by weak near-infrared emission and low detection efficiency.

Against thermal incumbents the picture is contested rather than superior: the market survey places CNTs alongside graphene-enhanced materials, metal-based TIMs and metamaterials, each with distinct advantages across applications, which is language of coexistence, not displacement <sup class="ref"><a href="https://www.globenewswire.com/news-release/2025/08/19/3135485/28124/en/Thermal-Interface-Materials-Market-Report-2026-2036-High-Performance-TIMs-for-Data-Centers-AI-Servers-and-5G-Infrastructure-Global-Outlook.html" title="Thermal Interface Materials Market Report 2026-2036: High-Performance TIMs for Data Centers, AI Servers, and 5G Infrastr" rel="noopener">ref</a></sup>. CNTs also retain a niche advantage as the cleanest available one-dimensional conductor: multilevel Josephson transport had previously been seen mainly in exceptionally clean systems such as carbon nanotubes, which is why Ge/SiGe is presented as an alternative platform. Real novelty, uneven margins.

**TLDR: Genuine and in one case quantified advantages over incumbents, but rarely a decisive margin, and CNTs are one of several contenders in thermal management.**

## Diffusion (3/5)

The bulk path is already moving. Practitioner reporting describes CNTs shifting from lab novelty to products across energy, electronics, infrastructure and defence, while explicitly framing the story as a breakthrough with slow market adoption <sup class="ref"><a href="https://stateofthefuture.substack.com/p/a-primer-carbon-nanotubes" title="A Primer: Carbon Nanotubes" rel="noopener">ref</a></sup>. The supplier model that has emerged is enabling-materials rather than finished product, selling customised forests and transfer processes into composites, catalysts, thermal interfaces, electrodes and sensors <sup class="ref"><a href="https://nawah.us/architectured-nanomaterials/technology/" title="NAWAH Architectured Nanomaterials — VACNT technology & positioning" rel="noopener">ref</a></sup>, which lowers the adoption barrier for a customer already making a part but leaves CNTs dependent on someone else's product cycle. Aerospace and structural testing entry points come with long qualification, which is implicit in an SBIR Fast-Track structured around selling either measurement services or the equipment, materials and training to do it in-house.

**TLDR: Already diffusing as an additive and forest material; electronics adoption is blocked by sorting, doping stability and substrate dependence.**

## Impact (4/5)

The upside case is the whole logic industry. If SWCNTs can carry scaling forward past the point where silicon fails on tunnelling, subthreshold swing and dark silicon, the addressable value is the semiconductor roadmap itself. That outcome is not demonstrated and should be treated as an option, not a forecast. The nearer-term impact is still meaningful: thermal interface materials for data centres, AI servers and 5G are a named growth market in which CNTs are one of the leading candidate chemistries <sup class="ref"><a href="https://www.globenewswire.com/news-release/2025/08/19/3135485/28124/en/Thermal-Interface-Materials-Market-Report-2026-2036-High-Performance-TIMs-for-Data-Centers-AI-Servers-and-5G-Infrastructure-Global-Outlook.html" title="Thermal Interface Materials Market Report 2026-2036: High-Performance TIMs for Data Centers, AI Servers, and 5G Infrastr" rel="noopener">ref</a></sup>, and heat is a first-order constraint on datacentre economics <sup class="ref"><a href="https://stateofthefuture.substack.com/p/carbon-nanotubes-in-the-datacentre" title="Carbon Nanotubes in the Datacentre" rel="noopener">ref</a></sup>.

Beyond those, the sources point to a spread of smaller but real value pools: structural health monitoring and safety testing of critical infrastructure via optical strain sensing, deep-tissue near-infrared imaging where CNT emitters fill a gap in available fluorophores, hydrogen uptake in carbon nanostructures, and use as a one-dimensional container that forces new crystal phases, such as Cs2CoCl4 adopting tetragonal and orthorhombic rod groups under radial compression down to roughly 1 nm diameter. The breadth is itself the argument for a 4: CNTs do not need the logic outcome to matter, but they need it to matter enormously.

**TLDR: Large in the thermal and additive markets already being addressed; very large if the post-silicon channel claim ever lands.**

## Timing Soon (2-5yr)

Bulk CNTs are already in products according to practitioner accounts, and an industrial VACNT supply chain with transfer and encapsulation onto standard composite substrates exists today <sup class="ref"><a href="https://nawah.us/architectured-nanomaterials/technology/" title="NAWAH Architectured Nanomaterials — VACNT technology & positioning" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/a-primer-carbon-nanotubes" title="A Primer: Carbon Nanotubes" rel="noopener">ref</a></sup>. The nearest inflection is thermal management, addressed by a market survey covering 2026 to 2036 <sup class="ref"><a href="https://www.globenewswire.com/news-release/2025/08/19/3135485/28124/en/Thermal-Interface-Materials-Market-Report-2026-2036-High-Performance-TIMs-for-Data-Centers-AI-Servers-and-5G-Infrastructure-Global-Outlook.html" title="Thermal Interface Materials Market Report 2026-2036: High-Performance TIMs for Data Centers, AI Servers, and 5G Infrastr" rel="noopener">ref</a></sup>, and instrumentation, where a Fast-Track SBIR awarded in June 2026 is by design intended to reach commercialisation within the award period. That puts the commercially decisive window at two to five years.

CNT logic is on a different clock. In 2026 the field is still publishing a unified analytical theory of contacts to low-dimensional semiconductors, still comparing encapsulation methods for stable doping, and still establishing substrate effects on individual tubes. Those are precursors to process development, not process development. Treat the logic branch as Later at best on the evidence here.

**TLDR: Bulk and thermal uses are commercial now; the electronics case is a decade-scale bet still in the physics stage.**

## Overrated or underrated? Fairly rated

The honest reading of these sources is that CNTs have stopped being a hype object and become a normal specialty material with an unusually long option attached. The near-term business is unglamorous: additives, forests, composites, thermal interfaces, sensors, sold B2B into someone else's product <sup class="ref"><a href="https://nawah.us/architectured-nanomaterials/technology/" title="NAWAH Architectured Nanomaterials — VACNT technology & positioning" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://stateofthefuture.substack.com/p/a-primer-carbon-nanotubes" title="A Primer: Carbon Nanotubes" rel="noopener">ref</a></sup>. In that business CNTs compete on merit against graphene, metals and metamaterials rather than dominating <sup class="ref"><a href="https://www.globenewswire.com/news-release/2025/08/19/3135485/28124/en/Thermal-Interface-Materials-Market-Report-2026-2036-High-Performance-TIMs-for-Data-Centers-AI-Servers-and-5G-Infrastructure-Global-Outlook.html" title="Thermal Interface Materials Market Report 2026-2036: High-Performance TIMs for Data Centers, AI Servers, and 5G Infrastr" rel="noopener">ref</a></sup>. Priced as a specialty materials business, that is roughly fair.

The part that is easy to misprice in either direction is the post-silicon channel claim. The physics argument is strong and clearly stated, but every enabling problem visible in the 2026 literature, contacts, stable n-type doping, metallic/semiconducting sorting, substrate dependence, is still at the stage of first-principles modelling and single-tube experiments. Anyone underwriting CNTs on a logic thesis is buying an option with no dated exercise. Anyone dismissing CNTs because the logic thesis has been ten years away for decades is ignoring a material that now ships.

## Prediction

By 31 December 2028, no commercially available digital logic product will use carbon nanotubes as its primary transistor channel material, while CNT revenue continues to come from additives, composites, thermal interface materials and sensors.

## Evidence base

- A July 2026 review argues silicon CMOS faces hard limits from source-to-drain tunnelling, unscalable subthreshold swing and dark silicon, and benchmarks SWCNT ballistic and coaxial-electrostatic limits against published 5 nm experimental data.
- A June 2026 analytical model links metal-induced gap states to Schottky barrier height, transfer length and contact resistance, and explains recent CNT and 2D-material contact experiments, indicating contacts remain an unresolved criterion for scalable low-resistance CNT devices.
- A July 2026 study compares melt filling, solution reflux and vacuum sublimation for encapsulating donors and acceptors inside arc-discharge SWCNTs, stating that reliable doping, especially n-type, remains challenging due to environmental sensitivity.
- A July 2026 within-tube comparison found consistently higher field-effect mobility for CNT channels on hexagonal boron nitride than on SiO2, using gas flow-directed growth to span both substrates with one nanotube.
- Quantum-colour-centre-functionalised (6,5) nanotubes emitting at 1140 nm showed a two-photon action cross-section of 57 ± 2 × 10^3 GM under 1700 nm excitation, enabling the first reported single-particle imaging at that wavelength, published 7 July 2026.
- NSF awarded $1,549,408 on 17 June 2026 under SBIR Fast-Track for a CNT-based optically monitored strain sensor targeting aerospace and structural health monitoring customers.

## Open questions

- Does the metal-induced-gap-state scaling law in imply a contact resistance floor for one-dimensional channels that is compatible with high-density logic, or one that rules it out?
- Can endohedral encapsulation deliver n-type doping that survives ambient processing, and does any of the three filling routes compared in scale beyond gram-scale sorting by ultracentrifugation?
- Is the hBN mobility advantage over SiO2 reported in large enough to force an expensive substrate change, or can it be recovered by encapsulation or passivation on standard oxides?
- In thermal interface materials, do CNT-based products win design-ins against graphene-enhanced and metal-based alternatives, or remain one of several coexisting options as implied by <sup class="ref"><a href="https://www.globenewswire.com/news-release/2025/08/19/3135485/28124/en/Thermal-Interface-Materials-Market-Report-2026-2036-High-Performance-TIMs-for-Data-Centers-AI-Servers-and-5G-Infrastructure-Global-Outlook.html" title="Thermal Interface Materials Market Report 2026-2036: High-Performance TIMs for Data Centers, AI Servers, and 5G Infrastr" rel="noopener">ref</a></sup>?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
