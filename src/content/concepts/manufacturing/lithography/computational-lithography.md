---
type: concept
slug: computational-lithography
canonical_name: Computational Lithography
aliases:
- OPC
- ILT
- SMO
- inverse lithography technology
- AI-for-mask
kind: technology
parent_concepts:
- lithography
related_concepts:
- maskless-lithography
- high-na-euv-lithography
- mask-blank-manufacturing
- electron-beam-lithography
- lithography-tools
sources: []
frontier:
- Can ML-trained ILT models generalise across process nodes, or does each node require a full re-training cycle with proprietary process data that a startup cannot access?
- At what customer segment does the specialty-fab qualification cycle drop below 12 months, and does any such segment have sufficient revenue to justify venture scale?
- Will NVIDIA open cuLitho to third-party integration, or does the NVIDIA-Synopsys equity partnership (Dec 2025, $2B) structurally lock GPU-native ILT inside Proteus?
- Is there a defensible data business in "LithoBench as a service" - selling process-node-specific ILT training datasets to AI-EDA companies - separate from building an ILT solver?
- What is the realistic spinout path from imec or Fraunhofer IISB into a commercial computational lithography software company, and does one actually exist in 2026?
last_updated: '2026-05-30'
tags:
- concept
- technology
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: maskless-lithography
  name: Maskless Lithography
  path: /sotf-site/manufacturing/lithography/maskless-lithography/
  macro: manufacturing
- slug: high-na-euv-lithography
  name: High-NA EUV Lithography
  path: /sotf-site/manufacturing/lithography/high-na-euv-lithography/
  macro: manufacturing
- slug: mask-blank-manufacturing
  name: Mask Blank Manufacturing
  path: /sotf-site/manufacturing/lithography/mask-blank-manufacturing/
  macro: manufacturing
- slug: electron-beam-lithography
  name: Electron-Beam Lithography
  path: /sotf-site/manufacturing/lithography/electron-beam-lithography/
  macro: manufacturing
- slug: lithography-tools
  name: Lithography Tools
  path: /sotf-site/manufacturing/lithography/lithography-tools/
  macro: manufacturing
---
Computational lithography is the software layer between chip design and physical wafer printing. It answers one question: how do you pre-distort a photomask so that optical diffraction, chemical resist physics, and lens aberrations produce the intended pattern on silicon? Without it, a mask drawn to design dimensions prints incorrectly at every sub-wavelength feature. The stack runs five layers deep, each more compute-intensive and more AI-relevant than the last.

## Physics / mechanism

**The Rayleigh resolution limit.** A lithography scanner prints features using light. The minimum resolvable feature size is roughly 0.5 times the wavelength divided by the numerical aperture of the lens. At 13.5nm EUV wavelength and 0.33 NA, that gives a theoretical minimum of around 20nm half-pitch. At 0.55 NA (High-NA EUV), it reaches 12nm. The problem is not the scanner. The problem is that every feature printed is sub-wavelength, which means diffraction reshapes it in ways the designer did not intend. Corners round off. Lines thin or thicken. Isolated features behave differently from dense arrays. Computational lithography corrects for these effects before the mask is made.

**Optical Proximity Correction (OPC).** The foundational layer. Applies geometric corrections to mask shapes so that when light diffracts around sub-wavelength features, the printed result matches design intent. Rule-based OPC uses lookup tables and is fast. Model-based OPC simulates the optics and resist chemistry and dominates at nodes below 28nm. The OPC market alone is roughly $600M to $1.2B (2024). Synopsys Proteus, Siemens Calibre OPC, and ASML Brion own this layer.

**Source-Mask Optimisation (SMO).** Co-optimises the illumination source shape and the mask simultaneously rather than treating them as sequential problems. More compute-intensive than OPC alone. Primarily an ASML and Synopsys capability. Limited venture relevance.

**Inverse Lithography Technology (ILT).** The critical inflection layer. Conventional OPC starts from a rectangular design and corrects it. ILT reverses the problem: given the desired wafer pattern, derive the globally-optimal mask from scratch. The output is not a corrected rectangle. It is a smooth curve - non-Manhattan, organic - because that is what the physics actually demands. A single advanced-node mask set requires roughly 30 million CPU hours via traditional ILT. NVIDIA cuLitho (2023, in production at TSMC March 2024) reduces that to an overnight GPU run using 500 H100s in place of 40,000 CPUs. TSMC called ILT "the most significant EDA advance in the last two decades." Synopsys owns the dominant commercial ILT solver (Proteus) following its 2012 acquisition of Luminescent Technologies, which had commercialised ILT from 2003 and operated independently for nine years before being absorbed.

**Curvilinear mask synthesis.** ILT output is intrinsically curvilinear. Curvilinear masks improve wafer process windows by roughly 15% compared to Manhattan-corrected masks, but they require three enabling technologies that only converged in 2025-2026: multi-beam e-beam mask writers (IMS MBMW series) to manufacture the curves, GPU rasterizers to convert polygon geometry to pixel grids fast enough for production, and updated mask inspection tools. Siemens' GPU rasterizer achieves 290x speedup for Manhattan geometries and 45x for curvilinear, with under 1% absolute error. Micron won best paper at Photomask Japan 2025 for production ILT plus PLDC deployment. D2S TrueMask ILT and PLDC are confirmed in production at Micron and Tekscend. The eBeam Initiative's 2025 survey (51 companies) reports 77% believe leading mask shops can handle limited curvilinear high-volume manufacturing by end-2026.

**Multi-beam mask writing.** The hardware layer that enables curvilinear masks at scale. IMS Nanofabrication (Vienna, Austria, Intel majority stake, roughly $4.3B valuation) holds 81.52% market share in multi-beam mask writers. Their MBMW-401 targets angstrom-era nodes. Without multi-beam writers, curvilinear ILT masks cannot be manufactured at acceptable throughput or cost. AMTC Dresden installed Europe's first multi-beam mask writer.

**The NVIDIA-Synopsys lock.** cuLitho is not an open platform. It is a library integrated directly into Synopsys Proteus and Siemens Calibre. NVIDIA made a $2B equity investment in Synopsys in December 2025, explicitly to deepen this integration. A startup cannot license cuLitho. The B200 "20x further acceleration" announcement is a Synopsys-NVIDIA deliverable. GPU hardware is commoditising; the software integration layer above it is being locked up inside incumbent contracts. A startup buying H100s still has to write a full ILT solver from scratch and validate it against a system with 20 years of fab qualification data.

## Why now (2026)

Three of the five commonly-cited inflection points are real. Two are overstated.

**Real: open ML datasets create a new entry point.** LithoBench (120,000+ layout tiles, NeurIPS 2023) and MaskOpt (arXiv December 2024) enable a two-person team to train an ILT approximation model without access to proprietary fab data. Five years ago this was not possible. The datasets are simulation-derived (Synopsys Sentaurus), not real-process data, which means a model trained on them alone has unknown error characteristics on real silicon. But they are a legitimate starting point for an academic prototype that can then be fine-tuned with customer process data.

**Real: EDA consolidation opens specialty segments.** Cadence sold its OPC line to Silvaco in March 2025. The Silvaco acquisition signals that legacy OPC for mature nodes (28nm and above) is becoming commoditised and contested. Wally Rhines joining Silvaco as CEO in August 2025 suggests aggressive repositioning. Siemens acquired Canopus AI in January 2026 for ML-based metrology and inspection - confirming that incumbents are buying ML capabilities they have not built internally. These moves indicate movement in the competitive structure.

**Overstated: High-NA EUV makes ILT non-optional for a startup's customers.** High-NA EUV forces ILT adoption at TSMC, Samsung, and Intel. Those three fabs will buy ILT from Synopsys Proteus. The specialty fabs a pre-seed startup would target - SiC, GaN, photonics, MEMS, research foundries - are running DUV at 28nm or above. ILT for DUV at those nodes is a solved problem with existing incumbent tools. The High-NA demand catalyst does not reach the specialty segment.

**Overstated: EU Chips Act funds a computational lithography software track.** The EU Chips Act is primarily a fab capex programme. TSMC Dresden, Intel Magdeburg, and AMTC multi-beam hardware are its primary beneficiaries. EIC Pathfinder and EIC Accelerator are open deep-tech competitions, not ring-fenced semiconductor software programmes. A startup in this space competes for EIC budget against all of European deep tech. The grant advantage is marginal, not structural.

## Competitive landscape

| Technique / layer | Key players | Weakness | Startup angle |
|---|---|---|---|
| OPC (model-based) | Synopsys Proteus, Siemens Calibre, ASML Brion | Priced for 15 leading-edge fabs; no API access; opaque pricing for specialty fabs | Mature-node OPC for specialty fabs at consumption pricing |
| ILT (full-chip) | Synopsys Proteus + cuLitho, D2S TrueMask ILT | cuLitho locked to Synopsys; D2S underfunded at ~$30.8M total raised; no European presence | ML-hybrid ILT (ML first pass, OPC cleanup) for mask shops |
| Curvilinear mask synthesis | Siemens GPU rasterizer, D2S PLDC | Only two commercial tools exist; Siemens rasterizer released April 2026 | PLDC-equivalent for European mask shops integrating IMS MBMW |
| ML-for-OPC | Siemens Calibre MML (production 2025), Synopsys ML features | Reactive adoption rather than architecturally native | ML-native ILT trained on open datasets plus customer process data |
| Metrology / metrospection | Siemens (post-Canopus AI, Jan 2026), KLA (post-Anchor, Jul 2021) | Incumbents acquired the ML capability; no pure-play remains | ILT-to-silicon feedback loop tool for research foundries |
| ILT training data | LithoBench (academic), MaskOpt (academic) | Simulation-derived only; no real process-node data; no commercial product exists | "LithoBench as a service" - process-node-specific training datasets sold to AI-EDA companies |
| Multi-beam mask writing | IMS Nanofabrication (81.52% share, ~$4.3B val), Mycronic SLX | IMS is Intel/TSMC-controlled; no independent European software companion exists | Not a startup angle; hardware owned by strategic investors |

**Incumbents in detail.**

Synopsys Proteus: the dominant ILT platform, ~31% EDA market share overall, $2B NVIDIA equity partnership deepening GPU integration, acquired Luminescent Technologies' ILT IP in 2012. The historical precedent is unflattering for startups: Luminescent operated independently from 2003 to 2012 - nine years - before being absorbed. During that period ILT was a niche hot-spot repair tool. Now that cuLitho makes full-chip ILT tractable, the market is the whole leading-edge mask synthesis flow, and Synopsys owns it.

Siemens Calibre: 70%+ of IC manufacturing sign-off, Calibre MML in production 2025, Canopus AI integrated January 2026, GPU rasterizer at production quality April 2026. The Brion Technologies precedent: founded 2002, acquired by ASML for $270M in 2007 - five years, before it reached the commercial scale that would have made it a standalone entity. ASML bought Brion to stop a competitor acquiring it, not because Brion was failing.

D2S (Design to Silicon, San Jose): the only pure-play GPU-native ILT company. ~$30.8M total raised. 16 years in business. In production at Micron and Tekscend. Underfunded by two orders of magnitude relative to Synopsys. No European presence. The most credible proof that an independent ILT software company can exist; also proof that getting to production traction takes 15+ years and limited venture returns.

Silvaco (Nasdaq: SVCO, market cap ~$114M): acquired Cadence's OPC product line March 2025, Wally Rhines as CEO August 2025. Positioned as a challenger but is subscale by a factor of 700 relative to Synopsys.

## Lawrence's framing

The technology inflection is real and the timing is not wrong. Multi-beam mask writers are now installed in Europe. Curvilinear masks are in production at Micron. Open ML datasets exist that did not exist three years ago. The software gap - no European company generating those masks at prices accessible to specialty fabs - is a factual observation. The question is whether a EUR 30M fund should be the vehicle to address it, and the honest answer is no.

The structural problem is that computational lithography software has never been venture-fundable at early stage for the same reason it has never spawned a large independent company: the qualification cycle and the customer base create a mismatch with venture timelines and return requirements. Luminescent Technologies operated for nine years before Synopsys acquired it. Brion lasted five years before ASML acquired it. D2S has 16 years in business and is still subscale. These are the comps. The correct interpretation of "no European company has done this" is not "greenfield opportunity" - it is "nobody has found a way to make it work at venture scale in Europe despite 20 years of trying in the US." That needs a response more specific than "AI makes it different now."

The one thread worth following is not the ILT solver. It is the training data. AI-EDA companies (Ricursive at $4B valuation, Cognichip at $93M raised, ChipAgents at $74M raised) are raising large rounds and building foundation models for chip design. All of them need lithography-accurate training data. None of them are building it. A company that sits between the mask shops (who have process data) and the AI-EDA companies (who need it) - packaging, cleaning, and licensing node-specific ILT datasets - has a shorter path to revenue, no qualification cycle, and a more obvious buyer. That is a EUR 1M pre-seed thesis. It does not require founders who have run silicon at TSMC. It requires founders who understand data licensing and the AI-EDA company buyer, which is a more tractable founder profile. The research synthesis spends two paragraphs on this idea and then ignores it. That is backwards.

## Companies
<!-- dataview block stripped for public site -->

## Connected ideas
<!-- dataview block stripped for public site -->

## Sources
<!-- dataview block stripped for public site -->
