---
type: concept
slug: maskless-lithography
canonical_name: Maskless Lithography
aliases:
- maskless
- direct-write lithography
- virtual masks
- virtual mask lithography
- multi-beam direct write
- multi-beam laser interference lithography
- holographic lithography
- DMD lithography
- digital micromirror lithography
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- lithography
related_concepts:
- e-beam-lithography
- nanoimprint-lithography
- duv-immersion-lithography
- high-na-euv-lithography
- mask-blank-manufacturing
- two-photon-polymerization
- xolography
- metalens
- metasurfaces-flat-optics
- metamaterials
companies_using:
- cnuic
- swhl
- eulitha
- heidelberg-instruments
ideas_referencing:
- '[[beyond-euv-not-in-2020s]]'
- '[[specialty-silicon-non-leading-edge]]'
- '[[photonic-foundry-capacity]]'
- '[[european-sovereignty-stack]]'
sources:
- '[[2025-01-06-radiant-acquires-nilt]]'
frontier:
- Production state of multi-beam direct-write in 2026 — IMS Nanofabrication (Intel-acquired), Mapper-derived programs, NuFlare. Are any shipping volume tools to fabs, or still mask-writing only?
- Per-wafer cost crossover where mask amortisation no longer wins — what volume threshold makes maskless economic?
- Lateral resolution + throughput frontier on optical maskless (DMD-based) vs e-beam vs NIL
- Customer profile of current maskless-tool buyers — research labs, photonic foundries, MEMS, specialty-IC?
- Multi-beam mask writing/inspection bottleneck — already binding on the mask side rather than the scanner side?
- Photonic foundry adoption — does maskless become the natural pairing for low-volume photonic-IC fabs?
- European maskless ecosystem outside ASML — UK, Scotland, Germany, France clusters?
last_updated: 2026-05-08
tags:
- concept
- technology
- lithography
- maskless
- direct-write
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 1
---

# Maskless Lithography

*Kind: technology · Direct-write patterning without photomasks — multiple physical mechanisms (e-beam, optical/DMD, X-ray) competing for specialty + low-volume + photonic-IC segments.*

## Physics / mechanism

Maskless lithography removes the photomask from the patterning loop. Where conventional projection lithography (DUV, EUV) projects a fixed pattern from a reticle onto the wafer, maskless approaches generate the pattern dynamically — either by scanning a focused beam (electron, ion, photon) across the wafer, or by digitally programming an array of mirrors / micro-shutters that modulate light pixel-by-pixel.

Four main physical routes:

1. **Multi-beam electron direct-write.** Hundreds of thousands of parallel electron beams patterning the wafer simultaneously. Highest resolution (sub-10 nm proven), but historically throughput-limited (multi-hour exposure per 300 mm wafer is the headline gap). IMS Nanofabrication (Intel-acquired 2024) is the lead production tool; Mapper Lithography (Dutch, bankrupt 2018) was the most ambitious commercial attempt; NuFlare (Toshiba) ships mask-writing tools that approach maskless economics on small batches.

2. **Optical maskless (DMD / SLM-based).** A digital micromirror device or spatial light modulator dynamically generates the pattern; deep-UV or visible light exposes photoresist. Resolution lower than e-beam (~250 nm typical, sub-100 nm with immersion + computational tricks), but throughput much higher. Used in PCB lithography, MEMS, biotech research patterning. Heidelberg Instruments + Microtech are commercial leaders.

3. **Multi-beam laser interference / holographic lithography.** Multiple coherent laser beams generate a **3D hologram inside the photoresist** — the photoresist is exposed throughout its volume by the interference pattern, not just at the surface. The technique was explored in the early 2000s (ASML held patents in the space) but not commercially viable until three things converged: laser power scaling (milliwatts → 1-2 watts), GPU/AI compute for hologram calculation, and component supply-chain consolidation. Achieves ~1 micron depth of focus vs traditional limits, real-time reconfigurability without physical mask swap, and addresses 3D patterning (slanted / pyramid structures) that nanoimprint struggles with. **Cnuic** is the lead UK/Edinburgh play; SWHL (Swiss holographic competitor) is the closest peer; Eulitha (Switzerland) does displacement lithography for gratings (niche, ~£5-7M revenue). The technical-risk gate is plasma enhancement working at scale (per Cloudberry IC diligence).

4. **X-ray maskless / proton-beam-write.** Research-stage. Berkeley Lab + LLNL collaborations explore the physics; commercial path unclear.

The unifying economic question: **at what volume does maskless beat masked?** Mask amortisation costs $1-10M per leading-edge mask set across the wafers it patterns. For low-volume specialty (photonic ICs, MEMS, prototype runs, research wafers, mid-IR sensing), masks never amortise — maskless wins. For high-volume logic and memory, masks dominate. The crossover is the structural question.

## Competitive landscape

**Production today:**
- Heidelberg Instruments (DE) — DMD-based optical maskless for PCB / MEMS / research
- Microtech (DE) — similar, smaller scale
- IMS Nanofabrication (acquired by Intel 2024) — multi-beam mask-writing + maskless direct-write
- NuFlare (Toshiba) — mask-writing dominantly, partial maskless

**Recent / emerging:**
- **Cnuic** — UK / Edinburgh, multi-beam laser interference / virtual-mask approach, Cloudberry passed on team+terms (Dec 2025) but kept on radar — SotF interview May 2026 with Omar Durrani revealed Apple LOI in flight, X-fab CEO discussions, SK Hynix DRAM-capacitor interest, SMC Edinburgh foundry partnership
- SWHL — Swiss holographic lithography company, strong technical advisor (Eric, ex-GlobalFoundries / X-Lite founder), weak founder; potential £1M raise at £5M valuation (per Cloudberry Dec 2025 IC analysis)
- Research labs at Stanford, MIT, IMEC, Fraunhofer

**Adjacent (not strictly maskless but similar function):**
- [[two-photon-polymerization]] — direct-write 3D photopolymer (Nanoscribe, Multiphoton Optics)
- [[xolography]] — volumetric direct-write (acquired by Light Spring's deal pipeline)
- [[nanoimprint-lithography]] — uses physical templates not optical masks; arguably mask-equivalent but different economics

## Cloudberry relevance

Direct via **Cnuic** (Edinburgh, Scottish maskless-litho startup). Adjacent to **Photonic Foundry Capacity** (low-volume photonic IC production where maskless economics win). Cross-pollinates **Specialty Silicon Non Leading Edge** (specialty fabs as natural maskless customers). Bear-case for **High Na Euv** only if multi-beam direct-write reaches HVM throughput — current state is "research + specialty" only.

## Frontier (open questions)

See frontmatter `frontier:` block. SotF interview with Omar Durrani (Cnuic CEO) on 8 May 2026 partially answered several of these — see **2026 05 08 Sotf Interview Omar Durrani Cnuic** for verbatim. Specifically:

- **Customer profile (was open) → partially answered.** Apple flexible polymer test, X-fab curved 3D structures, SK Hynix DRAM capacitor arrays, SMC Edinburgh foundry partnership. Photonics + metamaterials customers dominate the pipeline.
- **Per-wafer cost crossover (was open) → still open.** Omar didn't give specific numbers but framed the wedge as "rapid mask-master creation vs 15-16 week e-beam mask sets" — suggests the cost-crossover analysis is at the *mask-making* layer, not wafer-patterning layer initially.
- **Lateral resolution + throughput frontier → partially answered.** Multi-beam laser interference theoretically beats immersion on throughput (large-area simultaneous exposure vs scanner step-and-repeat) but staging/alignment/processing remain challenges. Resolution targets hundreds-of-nm not tens-of-nm.
- **Photonic foundry adoption → confirmed as primary use case.** Omar explicitly framed Cnuic as complementary to immersion: immersion handles fine-scale circuitry, Cnuic handles interconnects, advanced packaging, photonics components.
- **European maskless ecosystem → partially mapped.** UK/Scotland (Cnuic), Switzerland (SWHL, Eulitha), Germany (Heidelberg, Microtech). UK component supply chain limited (optics from Germany, lasers from US/China/Japan/Korea).
