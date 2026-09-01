---
type: concept
slug: vertical-gan
canonical_name: Vertical Gan
aliases: []
parent_concepts:
- power-electronics
- energy-power
related_concepts: []
sources:
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
mention_count: 7
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
neighbors: []
---
sources:---

## Physics / mechanism

Vertical GaN devices route current through the thickness of the gallium nitride epitaxial stack rather than laterally along a surface channel, so the substrate and buffer layers sit directly in the conduction path. This geometry allows the blocking voltage to be supported by a thick drift region and the current to be spread over the device area rather than the chip perimeter, which is the basis for the claim that vertical GaN-on-silicon could deliver cost-effective power electronics and high-resolution micro-LEDs.

The dominant obstacle is that the epitaxial buffer layers conventionally used to grow GaN on silicon are electrically resistive. In a lateral device this is irrelevant, because current never crosses the buffer; in a vertical device the buffer is in series with the channel, and its resistance adds directly to the on-state loss. Deployment of vertical GaN-on-silicon is described as bottlenecked by this buffer resistance.

One reported route around this is a sputtering-based approach that forms, in situ, a sub-nanometre silicide-based template on Si(111) by rapid thermal annealing. The reported template thickness is 0.5 nm, and the method is stated to work across 25 different metallic species. Scanning transmission electron microscopy indicates that an amorphous-like interlayer at the interface accommodates the lattice mismatch between GaN and silicon. The resulting films are reported to show low vertical resistance, ohmic behaviour and thermal stability.

Key parameters for this class of device are therefore the specific vertical resistance of the buffer or template stack, the linearity (ohmicity) of the vertical contact, the crystal quality of the overlying GaN, and the thermal robustness of the interfacial layer through subsequent device processing.

## Competitive landscape

The sources support only one comparison: vertical GaN on silicon substrates versus the conventional GaN-on-silicon epitaxial buffer, where the latter's high electrical resistance is the stated bottleneck. The sources do not contain data on native GaN substrates, SiC, or lateral GaN HEMTs, so no ranking against those alternatives can be drawn here. Context from semiconductor startup funding notes continuing demand for higher-voltage power delivery in datacentre infrastructure, but does not attribute any funding to vertical GaN specifically <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>.

## Evidence base

- Vertical GaN-on-silicon architectures are positioned as enabling cost-effective power electronics and high-resolution micro-LEDs, with deployment bottlenecked by the high electrical resistance of conventional epitaxial buffer layers (4 May 2026).
- A sputtering-based strategy is reported to yield GaN epitaxial films on Si(111) with low vertical resistance, ohmic behaviour and thermal stability (4 May 2026).
- The method relies on in-situ formation of a 0.5 nm silicide-based template by rapid thermal annealing (4 May 2026).
- The template approach is reported to work across 25 different metallic species (4 May 2026).
- STEM imaging identifies an amorphous-like interlayer that accommodates the GaN/Si lattice mismatch (4 May 2026).
- Semiconductor startup funding in Q2 2026 totalled over $6.0B across 80 companies, with higher-voltage power delivery named among datacentre-infrastructure themes; no vertical GaN company is listed (13 July 2026) <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>.

## Frontier (open questions)

- What specific vertical resistance (in mΩ·cm²) does the silicide-template stack achieve, and how does it compare with a native GaN substrate under the same measurement conditions?
- Does the 0.5 nm silicide template survive full device fabrication thermal budgets, and what is its breakdown field when a thick drift layer is grown above it?
- Which of the 25 metallic species gives the best combination of vertical resistance and GaN crystal quality, and does the ranking hold at 150 mm or 200 mm wafer diameter?
- Have any working vertical GaN transistors or diodes been fabricated on this template, with measured blocking voltage, on-resistance and switching losses?

*Synthesised 2026-08-31 from 2 KB sources by the resynth pipeline; citations are KB source slugs.*
