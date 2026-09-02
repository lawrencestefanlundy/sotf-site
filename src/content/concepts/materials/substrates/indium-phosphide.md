---
type: concept
slug: indium-phosphide
canonical_name: Indium Phosphide (InP)
aliases: []
kind: material
parent_concepts:
- materials
- substrates
related_concepts: []
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-06-16-coherent-signs-loi-for-up-to-50m-chips-act-grant-to-expand-t]]'
- '[[2026-03-30-photonics-material-class-war-silicon-photonics-and-photonic]]'
frontier:
- Does InP remain a full circuit platform, or does it collapse to a bonded gain die on silicon, TFLN or glass substrates? The sources describe the competition but give no share data.
- Do the simulated elliptical width-modulated bends (0.22 dB per 90 degrees at 6 micrometre radius) reproduce in fabricated InP devices, and does the 15 per cent footprint penalty hold at circuit scale 2026 06 16 optimization of photonic waveguide bends for low index contr?
- Does the SOA noise-compression result survive in a fabricated multilayer chip rather than an OSNR recursion emulated from one neuron 2022 shi soa aonn noise depth scaling?
- What are InP wafer diameter, yield and cost per die relative to silicon photonics? No supplied source contains these figures, and they determine everything about the platform boundary.
last_updated: '2026-08-31'
tags:
- concept
- material
mention_count: 18
last_reorg_date: '2026-05-13'
scorecard:
  viability: 4
  drivers: 3
  novelty: 3
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 1
sources_30d: 1
recent_mentions:
- slug: 2026-06-16-coherent-signs-loi-for-up-to-50m-chips-act-grant-to-expand-t
  title: Coherent signs LOI for up to $50M CHIPS Act grant to expand Texas indium phosphide fab - Dealroom
  date: '2026-06-16'
  kind: web
- slug: 2026-03-30-photonics-material-class-war-silicon-photonics-and-photonic
  title: 'Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts'
  date: '2026-03-30'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2023-07-27-e10-pushing-moores-law-to-the-limit
  title: '🔮E10: Pushing Moore''s Law to the Limit with High-NA EUV (aka Nanoscale Chip Printing)'
  date: '2023-07-27'
  kind: substack
neighbors: []
---
**Indium phosphide is the III-V compound semiconductor that actually emits and amplifies light on a chip, making it the incumbent gain material for photonic integrated circuits, but its low refractive index contrast caps integration density and it is now one of three platforms fighting over the PIC market rather than the obvious winner.**

## Summary

Indium phosphide (InP) is a compound semiconductor used both as a wafer substrate and as the active gain medium in photonic devices. Where silicon has to be coaxed into handling light and cannot generate it, InP lases natively: recent work demonstrated half-wave plasmonic lasing from InP nanoparticles roughly 115 nm long and 100 nm high on gold, emitting at 730 nm, described by the authors as one of the smallest active laser cavities reported. The same gain property underpins semiconductor optical amplifiers (SOAs), which can be used not just to boost signals but as an all-optical nonlinearity via cross-gain modulation **2022 Shi Soa Aonn Noise Depth Scaling**.

The parameter that most constrains InP as a circuit platform is refractive index contrast. InP is explicitly categorised as a low index contrast platform, which makes waveguide bends lossy and forces large bend radii, limiting how densely a chip can be laid out. Work on elliptical width-modulated bends reports 0.22 dB per 90 degree turn at a 6 micrometre bend radius, about 40 per cent lower than a conventional circular bend and 27 per cent lower than a circular width-modulated bend, for a 15 per cent footprint penalty. That is a real gain, but it is an optimisation against a structural handicap that silicon-on-insulator does not have.

Commercially, InP is not a research material. Coherent signed a letter of intent for a CHIPS Act grant of up to $50m to expand an indium phosphide fab in Texas <sup class="ref"><a href="https://news.google.com/rss/articles/CBMiuwFBVV95cUxPcEo0Yk9LU2M2ck1nYVNIeHY2dnllYV9RLUpsT0ZBaDBpblVtX2NXSkZYZ21hTmJEQzlTOFhlX1kwUFFuOXd0ZlhKekpTeWZZUUZuaXhsYmFrd29hbjgxcDVYUG01M0JEZ00zbGgwQXoxNGJBVFVLYUhHOGNIOUU4QlJpdy1INnlubEp1dE5Pb1NWcWo0YkIyYm1oRGJkel9fR1loVUhYMnFfdjVjTXk5OHpLVGVvT3o1ZWpn?oc=5" title="Coherent signs LOI for up to $50M CHIPS Act grant to expand Texas indium phosphide fab - Dealroom" rel="noopener">ref</a></sup>. Market analysis frames silicon photonics, InP and thin-film lithium niobate as three platforms competing to define the next generation of photonic integrated circuits, each holding a distinct competitive position rather than one displacing the others <sup class="ref"><a href="https://www.idtechex.com/en/research-report/silicon-photonics-and-photonic-integrated-circuits/1151" title="Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts" rel="noopener">ref</a></sup>. The decisive questions for InP are therefore not whether it works, but where the boundary sits between native InP circuits and InP used only as a bonded or flip-chipped gain element on someone else's substrate.

Separate physics work continues to characterise the material itself: InP nanocrystals on silicon nanotip arrays show radial breathing modes at 8 GHz and 10.3 GHz, with nonlinear frequency mixing appearing above 3 mJ/cm2 excitation fluence and a correlation between oxidation and the onset of nonlinear acoustic modes. First-principles calculations single out InP as a material where phonon scattering selection rules strongly amplify the longitudinal acoustic contribution to thermal conductivity, producing mode-polarised heat currents in nanofilms below 100 K. Neither is a product, but both indicate the material is still yielding new device-relevant behaviour.

## Viability (4/5)

InP is past the demonstration stage. It is in volume manufacture at a dedicated fab that a government programme is paying to expand, with an LOI for up to $50m in CHIPS Act support for a Texas indium phosphide facility <sup class="ref"><a href="https://news.google.com/rss/articles/CBMiuwFBVV95cUxPcEo0Yk9LU2M2ck1nYVNIeHY2dnllYV9RLUpsT0ZBaDBpblVtX2NXSkZYZ21hTmJEQzlTOFhlX1kwUFFuOXd0ZlhKekpTeWZZUUZuaXhsYmFrd29hbjgxcDVYUG01M0JEZ00zbGgwQXoxNGJBVFVLYUhHOGNIOUU4QlJpdy1INnlubEp1dE5Pb1NWcWo0YkIyYm1oRGJkel9fR1loVUhYMnFfdjVjTXk5OHpLVGVvT3o1ZWpn?oc=5" title="Coherent signs LOI for up to $50M CHIPS Act grant to expand Texas indium phosphide fab - Dealroom" rel="noopener">ref</a></sup>. Device-level results across the sources are physical, not simulated: lasing from ~115 nm InP particles and a fabricated SOA all-optical neuron **2022 Shi Soa Aonn Noise Depth Scaling**.

The deduction is for the structural limits the sources themselves document. Low index contrast is intrinsic to the platform, and the best reported fix still trades 15 per cent extra footprint for its 0.22 dB per 90 degree bend loss. The sources contain no wafer diameter, yield or cost-per-die figures, which are precisely the numbers that decide whether InP stays a full circuit platform or retreats to being a gain chiplet, so a 5 is not earned here.

**TLDR: Established, fabricated and funded; the open issues are density and cost, not whether it works.**

## Drivers (3/5)

On demand: the case rests on copper running out of reach as bandwidth rises, with optical links moving from floor to rack to board, and on the cost of the alternative, where coherent systems require DSPs consuming 3-4x more power and costing 3-5x more than intensity-modulated links <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. That is a qualitative argument from an interview-format source, not a forecast. Photonic neural network work adds a second, more speculative demand channel via SOA-based all-optical inference **2022 Shi Soa Aonn Noise Depth Scaling**.

On supply: capacity is being deliberately expanded with public money, which is the clearest signal in the evidence set that buyers exist <sup class="ref"><a href="https://news.google.com/rss/articles/CBMiuwFBVV95cUxPcEo0Yk9LU2M2ck1nYVNIeHY2dnllYV9RLUpsT0ZBaDBpblVtX2NXSkZYZ21hTmJEQzlTOFhlX1kwUFFuOXd0ZlhKekpTeWZZUUZuaXhsYmFrd29hbjgxcDVYUG01M0JEZ00zbGgwQXoxNGJBVFVLYUhHOGNIOUU4QlJpdy1INnlubEp1dE5Pb1NWcWo0YkIyYm1oRGJkel9fR1loVUhYMnFfdjVjTXk5OHpLVGVvT3o1ZWpn?oc=5" title="Coherent signs LOI for up to $50M CHIPS Act grant to expand Texas indium phosphide fab - Dealroom" rel="noopener">ref</a></sup>. Against that, the same demand wave is being courted by silicon photonics and thin-film lithium niobate <sup class="ref"><a href="https://www.idtechex.com/en/research-report/silicon-photonics-and-photonic-integrated-circuits/1151" title="Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts" rel="noopener">ref</a></sup>, and by newer entrants pitching glass packaging substrates <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-future-of-computing-is-glass" title="The Future of Computing is Glass w/ Andrea Rocchetto of Ephos" rel="noopener">ref</a></sup> and gallium nitride PICs, with a UK GaN photonics pilot line announced with the Institute of Compound Semiconductors in Cardiff <sup class="ref"><a href="https://stateofthefuture.substack.com/p/gallium-nitride-photonics-w-james" title="Gallium Nitride + Photonics w/ James Lee of Wave Photonics" rel="noopener">ref</a></sup>. Growing demand for photonics is not the same as growing demand for InP specifically, and the sources do not separate the two.

**TLDR: Real demand pull from optical interconnect and real supply push from state funding, but no quantified volumes in the sources.**

## Novelty (3/5)

InP's differentiator in the supplied evidence is gain. It is used as a high-gain medium for lasing at the plasmonic localisation limit, at particle lengths of ~115 nm emitting at 730 nm, with second- and third-order plasmonic modes in 280 to 480 nm particles. In SOA form the same gain provides a nonlinearity with a counterintuitive property: because M-to-1 cross-gain modulation compresses input noise while the output is amplified, output OSNR exceeds input OSNR when input OSNR is below roughly 19 dB, so amplified spontaneous emission does not simply accumulate across cascaded layers **2022 Shi Soa Aonn Noise Depth Scaling**. That result is emulated depth from one fabricated neuron, not a fabricated multilayer chip, which limits how much weight it can carry.

What InP is worse than is equally clear. It is named as the canonical low index contrast platform where bend loss is critical for compact geometries, and the improvements on offer are within-platform: 40 per cent and 27 per cent bend loss reductions against other InP bend designs, not against a high-contrast material. No source quantifies InP against silicon photonics or TFLN on loss, density or cost, so any claim of overall superiority is unsupported.

**TLDR: The material is decades old; what is new is how far its gain and nonlinearity can be pushed, and it is measurably worse than rivals on integration density.**

## Diffusion (3/5)

Diffusion is underway rather than pending: an existing fab is being expanded with public co-funding <sup class="ref"><a href="https://news.google.com/rss/articles/CBMiuwFBVV95cUxPcEo0Yk9LU2M2ck1nYVNIeHY2dnllYV9RLUpsT0ZBaDBpblVtX2NXSkZYZ21hTmJEQzlTOFhlX1kwUFFuOXd0ZlhKekpTeWZZUUZuaXhsYmFrd29hbjgxcDVYUG01M0JEZ00zbGgwQXoxNGJBVFVLYUhHOGNIOUU4QlJpdy1INnlubEp1dE5Pb1NWcWo0YkIyYm1oRGJkel9fR1loVUhYMnFfdjVjTXk5OHpLVGVvT3o1ZWpn?oc=5" title="Coherent signs LOI for up to $50M CHIPS Act grant to expand Texas indium phosphide fab - Dealroom" rel="noopener">ref</a></sup>. The barrier is not acceptance but partition. Market analysis explicitly reads as evidence against any single platform taking more than 70 per cent of PIC volume by 2030, with silicon photonics, InP and TFLN each occupying distinct competitive positions <sup class="ref"><a href="https://www.idtechex.com/en/research-report/silicon-photonics-and-photonic-integrated-circuits/1151" title="Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts" rel="noopener">ref</a></sup>. Low index contrast pushes InP away from the dense, transistor-adjacent integration that silicon foundries offer.

The second barrier is architectural. The packaging conversation is moving towards chiplets and new substrate materials, with glass proposed as the interposer of choice and panels as large as one metre by one metre in play <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-future-of-computing-is-glass" title="The Future of Computing is Glass w/ Andrea Rocchetto of Ephos" rel="noopener">ref</a></sup>, and with alternative compound platforms such as GaN entering pilot production <sup class="ref"><a href="https://stateofthefuture.substack.com/p/gallium-nitride-photonics-w-james" title="Gallium Nitride + Photonics w/ James Lee of Wave Photonics" rel="noopener">ref</a></sup>. Both are interview-sourced and partisan, but they describe a plausible end state in which InP survives as a small bonded gain die inside systems whose substrate, routing and modulation are someone else's material. The sources give no share figures, so this is a directional judgement, not a measured one.

**TLDR: Already deployed and expanding, but explicitly sharing the market with two other platforms and facing substrate-level substitution.**

## Impact (3/5)

The value case is that data centre interconnect has to go optical as copper reach collapses, and every optical link needs a source and often an amplifier <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. InP is the material in this evidence set that demonstrably provides both, from millimetre-scale SOAs **2022 Shi Soa Aonn Noise Depth Scaling** down to sub-micron lasers. If all-optical inference ever becomes practical, the noise-compression behaviour of cascaded SOAs would extend that role from links into compute **2022 Shi Soa Aonn Noise Depth Scaling**.

The ceiling on the score is that impact per wafer depends on whether InP supplies whole circuits or only the gain element, and the sources do not resolve this. No revenue, unit volume or forecast number appears in the supplied excerpts; the market report is present only as a directional claim about platform competition <sup class="ref"><a href="https://www.idtechex.com/en/research-report/silicon-photonics-and-photonic-integrated-circuits/1151" title="Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts" rel="noopener">ref</a></sup>. A large-value verdict would need numbers that are not here.

**TLDR: Indispensable to optical interconnect because it makes the light, but the sources supply no market size to size the prize.**

## Timing Now (0-2yr)

There is no maturation gap to wait out. Manufacturing capacity is being added now under a 2026 CHIPS Act letter of intent <sup class="ref"><a href="https://news.google.com/rss/articles/CBMiuwFBVV95cUxPcEo0Yk9LU2M2ck1nYVNIeHY2dnllYV9RLUpsT0ZBaDBpblVtX2NXSkZYZ21hTmJEQzlTOFhlX1kwUFFuOXd0ZlhKekpTeWZZUUZuaXhsYmFrd29hbjgxcDVYUG01M0JEZ00zbGgwQXoxNGJBVFVLYUhHOGNIOUU4QlJpdy1INnlubEp1dE5Pb1NWcWo0YkIyYm1oRGJkel9fR1loVUhYMnFfdjVjTXk5OHpLVGVvT3o1ZWpn?oc=5" title="Coherent signs LOI for up to $50M CHIPS Act grant to expand Texas indium phosphide fab - Dealroom" rel="noopener">ref</a></sup>, and the three-way platform competition is described as the current state of the PIC market with forecasts running to 2036 <sup class="ref"><a href="https://www.idtechex.com/en/research-report/silicon-photonics-and-photonic-integrated-circuits/1151" title="Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts" rel="noopener">ref</a></sup>.

What sits further out is the second-order question of whether InP holds the whole circuit or just the gain function. The bend-loss work is 3D FDTD simulation with an analytical model, not fabricated devices, and the all-optical neural network depth scaling is emulated from a single fabricated neuron **2022 Shi Soa Aonn Noise Depth Scaling**. Those routes to expanded InP relevance are on a multi-year clock; the base business is not.

**TLDR: InP is already a production platform being expanded with public money; the contest over its share is live today.**

## Overrated or underrated? Fairly rated

InP is treated as the incumbent gain material for photonics and that is what the evidence shows it to be: in production, being expanded with state support <sup class="ref"><a href="https://news.google.com/rss/articles/CBMiuwFBVV95cUxPcEo0Yk9LU2M2ck1nYVNIeHY2dnllYV9RLUpsT0ZBaDBpblVtX2NXSkZYZ21hTmJEQzlTOFhlX1kwUFFuOXd0ZlhKekpTeWZZUUZuaXhsYmFrd29hbjgxcDVYUG01M0JEZ00zbGgwQXoxNGJBVFVLYUhHOGNIOUU4QlJpdy1INnlubEp1dE5Pb1NWcWo0YkIyYm1oRGJkel9fR1loVUhYMnFfdjVjTXk5OHpLVGVvT3o1ZWpn?oc=5" title="Coherent signs LOI for up to $50M CHIPS Act grant to expand Texas indium phosphide fab - Dealroom" rel="noopener">ref</a></sup>, and delivering capabilities the alternatives cannot match on gain, from ~115 nm lasers to SOA nonlinearities with genuine noise compression **2022 Shi Soa Aonn Noise Depth Scaling**. It is equally correctly rated on its weakness: low index contrast is a permanent handicap on integration density that clever bend design mitigates rather than removes.

The trap to avoid is treating the photonics boom as an InP boom. The most decision-relevant source in this set is the one saying three platforms will each hold distinct positions rather than one winning <sup class="ref"><a href="https://www.idtechex.com/en/research-report/silicon-photonics-and-photonic-integrated-circuits/1151" title="Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts" rel="noopener">ref</a></sup>, reinforced by credible pushes towards glass substrates <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-future-of-computing-is-glass" title="The Future of Computing is Glass w/ Andrea Rocchetto of Ephos" rel="noopener">ref</a></sup> and GaN PIC pilot lines <sup class="ref"><a href="https://stateofthefuture.substack.com/p/gallium-nitride-photonics-w-james" title="Gallium Nitride + Photonics w/ James Lee of Wave Photonics" rel="noopener">ref</a></sup>. Exposure to InP is best understood as exposure to on-chip light generation, not to photonic integration generally.

## Prediction

By 31 December 2030, no single photonic material platform, InP included, will hold more than 70 per cent of PIC volume across segments, consistent with the three-platform split described on 30 March 2026 <sup class="ref"><a href="https://www.idtechex.com/en/research-report/silicon-photonics-and-photonic-integrated-circuits/1151" title="Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts" rel="noopener">ref</a></sup>.

## Evidence base

- 16 June 2026: Coherent signed an LOI for up to $50m in CHIPS Act support to expand a Texas indium phosphide fab, indicating InP capacity expansion backed by public funding <sup class="ref"><a href="https://news.google.com/rss/articles/CBMiuwFBVV95cUxPcEo0Yk9LU2M2ck1nYVNIeHY2dnllYV9RLUpsT0ZBaDBpblVtX2NXSkZYZ21hTmJEQzlTOFhlX1kwUFFuOXd0ZlhKekpTeWZZUUZuaXhsYmFrd29hbjgxcDVYUG01M0JEZ00zbGgwQXoxNGJBVFVLYUhHOGNIOUU4QlJpdy1INnlubEp1dE5Pb1NWcWo0YkIyYm1oRGJkel9fR1loVUhYMnFfdjVjTXk5OHpLVGVvT3o1ZWpn?oc=5" title="Coherent signs LOI for up to $50M CHIPS Act grant to expand Texas indium phosphide fab - Dealroom" rel="noopener">ref</a></sup>.
- 30 March 2026: market analysis frames silicon photonics, InP and thin-film lithium niobate as three platforms competing to define next-generation PICs, each in a distinct competitive position, read as evidence against any one platform taking >70 per cent of volume by 2030 <sup class="ref"><a href="https://www.idtechex.com/en/research-report/silicon-photonics-and-photonic-integrated-circuits/1151" title="Silicon Photonics and Photonic Integrated Circuits 2026-2036: Technologies, Markets, and Forecasts" rel="noopener">ref</a></sup>.
- 16 June 2026: InP is classified as a low index contrast platform where bend loss is critical; an elliptical width-modulated bend achieves 0.22 dB per 90 degrees at 6 micrometre radius, 40 per cent and 27 per cent below circular and circular width-modulated bends, for a 15 per cent footprint increase.
- 7 July 2026: high-gain InP nanoparticles on ultrasmooth gold lased at 730 nm from a cavity estimated at ~115 nm long and ~100 nm high, described as one of the smallest active laser cavities reported.
- 2 September 2022: in an SOA all-optical neuron, cross-gain modulation compresses input noise such that output OSNR exceeds input OSNR when input OSNR is below about 19 dB, so ASE does not accumulate uncontrollably with layer depth; depth was emulated, not fabricated **2022 Shi Soa Aonn Noise Depth Scaling**.
- 28 May 2026: InP nanocrystals on silicon nanotips show radial breathing modes at 8 GHz and 10.3 GHz, with nonlinear frequency mixing above 3 mJ/cm2 fluence and oxidation correlated with the onset of nonlinear acoustic modes, marking a mechanical damage threshold for InP nanostructures.

## Open questions

- Does InP remain a full circuit platform, or does it collapse to a bonded gain die on silicon, TFLN or glass substrates? The sources describe the competition but give no share data.
- Do the simulated elliptical width-modulated bends (0.22 dB per 90 degrees at 6 micrometre radius) reproduce in fabricated InP devices, and does the 15 per cent footprint penalty hold at circuit scale?
- Does the SOA noise-compression result survive in a fabricated multilayer chip rather than an OSNR recursion emulated from one neuron **2022 Shi Soa Aonn Noise Depth Scaling**?
- What are InP wafer diameter, yield and cost per die relative to silicon photonics? No supplied source contains these figures, and they determine everything about the platform boundary.

---
*Assessment drafted 2026-08-31 from up to 11 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
