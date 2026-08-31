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
mention_count: 22
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
sources_30d: 3
recent_mentions:
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
**Contact resistance is the parasitic resistance at the metal-to-semiconductor junction of a transistor or diode, and at the scaled dimensions now being targeted it has become the single parameter deciding whether 2D-material channels, and some wide-bandgap power devices, are usable at all.**

## Summary

Current entering a transistor channel must first cross a metal-semiconductor interface. That interface imposes a series resistance (conventionally quoted per unit contact width, in ohm-micrometres) which does not scale down as the device shrinks. Its physical origin is the Schottky barrier formed when metal wavefunctions leak into the semiconductor bandgap, creating metal-induced gap states (MIGS) that pin the Fermi level, plus the finite transfer length over which current actually crosses from metal into channel. A recent analytical treatment unifies these three observables (barrier height, transfer length, contact resistance) and finds a universal MIGS scaling law governed by the dimensionality of the semiconductor, which it uses to explain published carbon-nanotube and 2D-material results.

Why it has become a gating parameter rather than a nuisance: as logic moves to gate-all-around nanoribbons and complementary FETs (CFETs), channel widths fall into the tens of nanometres and channel resistance falls with them, so the fixed contact term comes to dominate total device resistance. Atomically thin transition-metal dichalcogenide (TMD) channels are attractive for those architectures because a sub-nanometre body suppresses leakage, but there is very little material into which to inject carriers. A 2026 trade analysis lists contact resistance, weak p-type behaviour and integration as the three blockers keeping TMD channels out of production <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>. The same analysis notes copper interconnect hitting its own nanoscale resistance wall, with ruthenium and molybdenum offering large reductions in ultra-fine lines, so the resistance problem is arriving at both ends of the wire-to-channel path.

The parameters that decide the outcome are: contact geometry (top/vertical contact versus edge contact), contact metal work function and whether the interface is chemically bonded or van der Waals, doping in the contact region, contact length relative to transfer length, and the polarity being contacted. Polarity matters most: n-type MoS2 devices are now respectable, with 30-40 nm-wide monolayer nanoribbons reaching a champion 995 microamps per micrometre at 1 V drain bias, and median on-current rising ~42% as width shrank from hundreds of nanometres. P-type is the weak leg: self-consistent modelling of WSe2 contacts finds source-limited current saturation, that is, the contact rather than the channel setting the ceiling, as the key obstacle to pushing 2D FETs to sub-10 nm channel lengths.

Contact resistance is not only a logic problem. A diamond Schottky PIN diode reporting ~116 kA/cm2 and 0.05 mOhm-cm2 specific on-resistance identifies defect density and contact resistance as the two terms that must fall for the device to approach its theoretical material limit. Interfacial charge-transfer resistance is also the framing concern in electrode/electrolyte pairing for solid oxide cells, where surface energy and roughness descriptors are proposed as early screens.

## Viability (2/5)

The positive evidence is real but one-sided. Monolayer MoS2 nanoribbon FETs narrowed to ~30-40 nm did not degrade: median on-current density rose ~42% and median subthreshold swing improved ~16%, with a champion device at 995 microamps per micrometre at 1 V drain and 2.5 V overdrive. That is an n-channel result at width scaling, not length scaling. Modelling of the p-side reaches the opposite conclusion: for WSe2, source-limited current saturation is identified as the key challenge in taking channel lengths from hundreds of nanometres to sub-10 nm, meaning the contact, not the channel, caps drive current. A CMOS process needs both polarities.

The theory side has firmed up: MIGS now has an analytical model with a dimensionality-dependent scaling law that reproduces existing nanotube and 2D experiments and states explicit criteria for scalable low-resistance contacts. Predictive understanding is a precondition for engineering a fix, not evidence of one. Note the limit of this evidence base: none of the supplied sources quotes an achieved contact resistance in ohm-micrometres against a roadmap target, so progress cannot be scored quantitatively here. Independent trade assessment still lists contact resistance among the blockers keeping 2D channels out of production <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>, which is the honest current state.

**TLDR: n-type contacts are demonstrably workable at scaled widths; p-type and sub-10 nm remain unsolved and are the binding constraint.**

## Drivers (4/5)

Demand side. The pull is architectural rather than speculative. Three-dimensional logic architectures, GAA nanoribbon and CFET, require channel widths in the tens of nanometres to hit density targets, which is precisely the regime where atomically thin channels become attractive and where fixed contact resistance stops being amortised over a wide channel. CFET is framed as the successor to gate-all-around, with reported better-than-expected ring-oscillator and SRAM progress at a leading foundry <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>, so the architecture that creates the contact problem is advancing on its own schedule. The same resistance pressure is visible in interconnect, where copper's nanoscale limits are pushing ruthenium and molybdenum for ultra-fine lines.

Supply side. Effort is spread across analytical theory, self-consistent device-level contact models covering both vertical and edge configurations and validated against p- and n-type experiments, and fabricated scaled devices. Public funding in the supplied set touches interfacial device physics in adjacent areas, for example two NSF awards of ~$306k each for a predictive device-physics framework for organic electrochemical transistors, explicitly to replace trial-and-error material and architecture design. The sources do not quantify total funding or industrial headcount aimed at contact resistance specifically.

**TLDR: Demand is structural and dated: CFET and GAA density targets force tens-of-nanometre widths, where the contact term dominates.**

## Novelty (3/5)

The claimed advance is over the absence of a general framework: metal contacts to low-dimensional semiconductors are described as critical yet lacking a general physical description, and the new analytical MIGS model supplies a universal dimensionality-governed scaling law linking barrier height, transfer length and contact resistance, and reproduces published nanotube and 2D data. The complementary contribution is a self-consistent contact-resistance model that spans channel length, doping, mobility, contact length and bias, and identifies which of these levers actually matters for WSe2 p-type contacts. Moving from empirical metal screening to a model that says why a given geometry fails is a genuine step.

On the device side the novelty is a counter-intuitive result: width scaling of 2D channels improves rather than degrades performance, attributed to minimal edge-induced disorder and enhanced gate control, quantified as ~42% higher median on-current and ~16% lower subthreshold swing. What is missing, and why this is a 3 and not higher, is a like-for-like resistance comparison: no supplied source states an ohm-micrometre figure beaten, nor by how much, so the size of the improvement over prior contact schemes cannot be established from this evidence. Contact resistance also remains a confounder in basic measurement, being one of the extrinsic mechanisms that must be excluded before an anomaly in transconductance can be attributed to valley thermodynamics.

**TLDR: The new thing is predictive contact modelling where none existed; the improvement over prior practice is qualitative, not quantified.**

## Diffusion (2/5)

Adoption of any contact solution is not a standalone decision. 2D channels are blocked by contact resistance, weak p-type behaviour and integration hurdles together <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>; solving one leaves a process that still cannot be adopted. Contact engineering approaches that work in a research device, for example exotic contact metals, edge contacts or semimetal contacts of the kind explored in the WSe2 modelling work, face the standard fab constraints the sources do not address: thermal budget, contamination rules, deposition uniformity across a wafer, and yield across billions of contacts rather than one champion device out of a batch.

There is a second, easier diffusion path that the sources support better: contact-resistance reduction in devices already in production or near it. The diamond Schottky PIN diode work identifies reduced contact resistance and defect density as the route to approaching its ultimate material limit from an already demonstrated 0.05 mOhm-cm2 on-resistance, and the same logic applies to interconnect metal substitution, where ruthenium and molybdenum are being weighed for ultra-fine lines <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>. These are incremental process changes inside existing flows and will diffuse faster than any 2D-channel scheme.

**TLDR: Contact schemes must survive foundry integration alongside two other unsolved 2D blockers, and no source shows an HVM-compatible process.**

## Impact (4/5)

If contact resistance at scaled dimensions is solved for both polarities, TMD channels become candidates for the GAA and CFET generations that need tens-of-nanometre widths, with the leakage advantage of an atomically thin body <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>,. If it is not, the whole 2D-channel thesis stalls regardless of channel-material progress, because source-limited saturation puts a hard ceiling on drive current at sub-10 nm channel lengths. That is a genuinely binary outcome for one of the two or three candidate paths beyond silicon channels, which justifies a high impact score even with viability weak.

The value is not confined to logic. Contact resistance is one of two terms standing between a demonstrated diamond power diode and its theoretical performance limit, and interfacial charge-transfer resistance is the central concern in electrode/electrolyte compatibility for solid oxide fuel and reversible cells, where surface free energy and ISO 25178 roughness descriptors are proposed as early screening criteria. The mechanisms differ, but the pattern of a fixed interfacial resistance capping an otherwise good material recurs across electronics and electrochemistry, which broadens the addressable value of better interface theory.

**TLDR: It is the gate on whether atomically thin channels can ever replace silicon at CFET-era dimensions, and it caps several other device families too.**

## Timing Soon (2-5yr)

The constraint is already active: 2D channels are described as not yet ready and blocked partly by contact resistance in early 2026 <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>, while the architectures that make it acute, GAA nanoribbon and CFET, are progressing now. Incremental resistance work in existing device families, interconnect metal substitution and contact improvement in wide-bandgap power devices, sits in the Now band.

The decisive question, whether p-type 2D contacts can be made good enough at sub-10 nm channel lengths, has just been reduced to a set of specific parameter targets said to be readily realisable in future experiments. Model-to-experiment cycles of that kind typically resolve within a few years, so expect a clear positive or negative answer on the physics well before any production decision. The supplied sources do not commit to a high-volume-manufacturing date, and the one reference to a 2D HVM timeline appears only as a linked thesis label rather than an argued date, so no firmer timing claim is supportable here.

**TLDR: The problem bites now; the evidence needed to judge whether it is solvable at sub-10 nm p-type should arrive within two to five years.**

## Overrated or underrated? Fairly rated

Nobody in this evidence base is underselling contact resistance. It is named as a blocker in trade analysis <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>, it is the target of new analytical theory, it is the identified ceiling in sub-10 nm p-type modelling, and it is one of two limiters flagged in a record-current diamond diode. The field's consensus and the evidence agree, so the concept is priced about right.

The part that is mispriced is the asymmetry. Impressive n-type 2D numbers, such as 995 microamps per micrometre from a 30-40 nm-wide MoS2 nanoribbon, are easy to read as general progress on 2D contacts. They are not. CMOS needs a p-channel, and the p-side evidence in these sources is modelling that says the contact will limit the current, not a device that says otherwise. Anyone taking a position on 2D channels should treat p-type contact resistance, quoted in ohm-micrometres at a stated channel length, as the number that matters, and treat champion n-type on-currents as almost uninformative about the CMOS question.

## Prediction

By 31 December 2028, no published sub-10 nm channel-length 2D-semiconductor p-FET will report an on-current density matching the ~995 microamps per micrometre already demonstrated for n-type monolayer MoS2 nanoribbons at 1 V drain bias.

## Evidence base

- 2026-01-13: 2D transition-metal-dichalcogenide channels suppress leakage but are blocked by contact resistance, weak p-type behaviour and integration hurdles; copper interconnect is hitting nanoscale resistance limits, with ruthenium and molybdenum offering large reductions in ultra-fine lines <sup class="ref"><a href="https://newsletter.semianalysis.com/p/interconnects-beyond-copper-1000" title="Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More" rel="noopener">ref</a></sup>.
- 2026-05-05: narrowing monolayer MoS2 nanoribbon channels from hundreds of nanometres to ~30-40 nm raised median on-current density ~42% and cut median subthreshold swing ~16%, with a champion device at 995 microamps per micrometre at 1 V drain and 2.5 V overdrive.
- 2026-06-16: an analytical metal-induced-gap-states model yields a universal scaling law governed by semiconductor dimensionality and unifies Schottky barrier height, transfer length and contact resistance, explaining recent carbon-nanotube and 2D experiments.
- 2026-08-10: self-consistent contact-resistance models for vertical and edge metal-2D configurations, validated against p- and n-type experiments, identify source-limited current saturation as the key challenge in scaling 2D FETs to sub-10 nm channel length.
- 2026-07-02: a diamond Schottky PIN diode reached ~116 kA/cm2 and 0.05 mOhm-cm2 specific on-resistance, with analysis showing that reducing defect density and contact resistance is required to approach the material's ultimate performance.
- 2026-06-16: in multilayer WSe2 transistors, contact resistance is treated as an extrinsic mechanism that must be excluded before a transconductance anomaly can be attributed to inter-valley carrier redistribution.
- 2026-08-05: NSF awarded two collaborative grants of ~$306k each to build a predictive device-physics framework for organic electrochemical transistors, aimed at replacing trial-and-error interface and architecture design.

## Open questions

- What p-type contact resistance, in ohm-micrometres and at a stated channel length, has actually been measured for WSe2 or another TMD, and how far is it from the value the self-consistent model says is needed to avoid source-limited saturation below 10 nm?
- Do the contact schemes implied by the MIGS dimensionality scaling law survive foundry constraints on thermal budget, contamination and wafer-scale uniformity, or do they only work in single-device demonstrations?
- Does the width-scaling benefit observed in 30-40 nm MoS2 nanoribbons persist when channel length is also scaled, where the fixed contact term dominates total resistance?
- How much of the diamond diode's gap to its theoretical limit is attributable to contact resistance rather than defect density, and which is the cheaper term to reduce?

---
*Assessment drafted 2026-08-31 from up to 11 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
