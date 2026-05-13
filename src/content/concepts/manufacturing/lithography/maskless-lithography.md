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
*Direct-write patterning without photomasks — multiple physical mechanisms (e-beam, optical/DMD, X-ray) competing for specialty + low-volume + photonic-IC segments.*

## Physics / mechanism

Maskless lithography removes the photomask from the patterning loop. Where conventional projection lithography (DUV, EUV) projects a fixed pattern from a reticle onto the wafer, maskless approaches generate the pattern dynamically — either by scanning a focused beam (electron, ion, photon) across the wafer, or by digitally programming an array of mirrors / micro-shutters that modulate light pixel-by-pixel.

Four main physical routes:

1. **Multi-beam electron direct-write.** Hundreds of thousands of parallel electron beams patterning the wafer simultaneously. Highest resolution (sub-10 nm proven), but historically throughput-limited (multi-hour exposure per 300 mm wafer is the headline gap). IMS Nanofabrication (Intel-acquired 2024) is the lead production tool; Mapper Lithography (Dutch, bankrupt 2018) was the most ambitious commercial attempt; NuFlare (Toshiba) ships mask-writing tools that approach maskless economics on small batches.

2. **Optical maskless (DMD / SLM-based).** A digital micromirror device or spatial light modulator dynamically generates the pattern; deep-UV or visible light exposes photoresist. Resolution lower than e-beam (~250 nm typical, sub-100 nm with immersion + computational tricks), but throughput much higher. Used in PCB lithography, MEMS, biotech research patterning. Heidelberg Instruments + Microtech are commercial leaders.

4. **X-ray maskless / proton-beam-write.** Research-stage. Berkeley Lab + LLNL collaborations explore the physics; commercial path unclear.

The unifying economic question: **at what volume does maskless beat masked?** Mask amortisation costs $1-10M per leading-edge mask set across the wafers it patterns. For low-volume specialty (photonic ICs, MEMS, prototype runs, research wafers, mid-IR sensing), masks never amortise — maskless wins. For high-volume logic and memory, masks dominate. The crossover is the structural question.

## Competitive landscape

**Production today:**
- Heidelberg Instruments (DE) — DMD-based optical maskless for PCB / MEMS / research
- Microtech (DE) — similar, smaller scale
- IMS Nanofabrication (acquired by Intel 2024) — multi-beam mask-writing + maskless direct-write
- NuFlare (Toshiba) — mask-writing dominantly, partial maskless

## Frontier (open questions)