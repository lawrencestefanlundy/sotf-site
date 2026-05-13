---
type: concept
slug: spatial-light-modulators
canonical_name: Spatial Light Modulators (SLMs)
aliases:
- SLM
- SLMs
- spatial light modulator
- LCOS-SLM
- DMD
- digital micromirror device
- liquid crystal on silicon
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- modulators-detectors
related_concepts:
- holographic-volumetric-displays
- optical-neural-networks
- two-photon-polymerization
- xolography
- wafer-level-optics
- displays
- arvr
- metasurfaces-flat-optics
- barium-titanate
- lithium-niobate-tfln
- indium-phosphide
companies_using:
- hamamatsu-photonics
- neurophos
- altro-photonics
- texas-instruments-dlp
- holoeye-photonics
- boulder-nonlinear-systems
- meadowlark-optics
- forth-dimension-displays
- jasper-display
- pacific-light-technologies
- himax-technologies
- olix
- coherix
- envisics
ideas_referencing:
- '[[parallel-foci-2pp-scaling]]'
- '[[slm-material-class-race]]'
sources: []
frontier:
- III/V SLM miniaturisation — Microsoft has multiple papers; what is current pixel pitch and refresh rate ceiling?
- BTO-on-SiN heterogeneous integration as a path to fast SLM, or is BTO modulator-only? (Altro context)
- When does parallel-foci 2PP/xolography exceed 50 foci with SLM-driven beam shaping in production?
- Backplane integration architecture — III/V on Si, copper metamaterial (Neurophos), or LCOS legacy?
last_updated: 2026-05-07
tags:
- concept
- technology
- photonics
- slm
- photonic-compute
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 2
---

# Spatial Light Modulators (SLMs)

*Kind: technology · Cross-cutting photonic component appearing in 26+ concept pages.*

## Physics / mechanism

Devices that imprint a spatial pattern onto a coherent or incoherent light beam by modulating amplitude, phase, or polarization pixel-by-pixel. Three dominant technologies today:

| Technology | Mechanism | Key parameters | Vendors / use |
|---|---|---|---|
| **LCOS-SLM** (Liquid Crystal on Silicon) | Birefringence shift in liquid crystal layer addressed by silicon backplane | ~1920×1200 pixels, 8-12µm pitch, 60-120 Hz refresh, phase-only / phase-amplitude | Hamamatsu, Holoeye, Jasper Display, Forth Dimension. Use: imaging, holography, beam shaping, OAM |
| **DMD** (Digital Micromirror Device) | Tilting mirrors (±10-12°) on CMOS backplane | ~4K pixels possible, 4-13µm pitch, 10-30 kHz refresh, binary amplitude | Texas Instruments DLP (sole HVM vendor). Use: projection, lithography, structured-light, parallel 2PP |
| **MEMS deformable mirror / phase plate** | Continuous-membrane mirror with array of actuators | 10-1000 actuators, kHz rates, continuous phase | Boston Micromachines, Iris AO, ALPAO. Use: adaptive optics, astronomy, high-end OPC |
| **Custom metamaterial / III-V SLM** | Bespoke active metasurface with electronic control of meta-atoms | Research-scale, GHz rates possible, novel architectures | Neurophos (bespoke copper-based metamaterial), Microsoft (III-V quantum-well-on-Si efforts), academic |

Performance trade-offs: LCOS gives best phase resolution but is slow (≤120 Hz) and limited by liquid-crystal birefringence dynamics; DMD is fast but binary; MEMS is fast and continuous but small array. The frontier — bespoke metamaterial / III-V SLMs — promises GHz rates with continuous phase control on production-scale arrays, but manufacturing has historically been impossible at volume.

## Competitive landscape

Tom Walton-Pocock (Geometry, 2026-05-06) summarises the current frontier:

> *"Prior efforts to do III/V SLM all failed because manufacture was impossible … you have to make these tiny refractive units and III/V units have been notoriously tricky to make to wire in. The SLM standard now is everything is on a backplane. Building sufficiently many quantum wells that work all on the same wafer is combinatorially extremely hard. Microsoft tried this a lot — they have several papers."*

Implication: the dominant architectural pattern is **active optics layer + silicon-backplane electronics** (the LCOS pattern, but extending to non-LCOS materials). Lawrence's hypothesis: **III/V on silicon** is the eventual stack. BTO is on the wrong side of the SLM/modulator divide — it's a modulator material, not an SLM material.

Adjacent material classes:
- LCOS (incumbent) — slow but cheap, mature
- DMD (TI monopoly) — binary, fast, lithography-grade
- MEMS deformable mirrors — continuous phase, low pixel count, niche
- Copper-based metamaterial (Neurophos) — novel, GHz, bespoke fabrication
- III/V quantum-well SLM (Microsoft research) — aspirational, no production
- Photonic-IC active grating arrays — emerging, could blur SLM/modulator distinction

## Cloudberry relevance

**Direct deals touching SLMs:**
- ****Coherix**** (UK, optical compute, live 2026-05-07) — fully custom telecoms-grade holographic SLM repurposed for ONN inference; Envisics-lineage IP. Counter-data point to the "LCOS ages out" framing in **Slm Material Class Race** — telecoms-LCOS for compute is alive in 2026 even if III/V displaces in the long run. See **2026 05 06 Coherix Introduction**.
- ****Neurophos**** (US, photonic compute) — uses copper-based metamaterial as SLM; Geometry diligencing
- ****Altro Photonics**** (UK, BTO/SiN heterogeneous) — BTO is for modulators not SLM proper; Altro should not be expected to solve SLM problem
- ****Memo Lightspring**** (passed) — flash-TPP scaling depends on SLM-driven parallel foci; current SOTA 49 foci, 100K aspirational
- ****Opdo**** (passed) — xolography uses DMD-based projection (TI DLP)

**The SLM material race is the binding fab problem in photonic compute.** Modulators (BTO, TFLN, polymer) are the easier component. SLMs need: fast switching (GHz desired), production-scale arrays (1M+ pixels), continuous phase, and yield. Today no single technology solves all four.

**GF context:** unclear if GlobalFoundries has III/V-on-Si capability that could bear on this. Worth a question to LP relationship.

**Cloudberry idea seeds:**
- ****Parallel Foci 2Pp Scaling**** — SLM throughput as binding constraint on flash-TPP
- ****Slm Material Class Race**** — LCOS vs DMD vs metamaterial vs III-V backplane

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- **Microsoft's III/V SLM papers** — Tom referenced multiple; pull via `/kb-research`. What pixel pitch, refresh rate, yield achieved?
- **Neurophos copper-metamaterial spec** — pixel pitch, switching speed, addressing scheme. Where Geometry's diligence landed.
- **OLIX architecture** — Tom + Geometry don't have material clarity. Watch for disclosures.
- **GF III/V-on-Si capability** — does any GF process node host III/V quantum wells with backplane integration?
- **Foundry path for active metasurfaces** — Neurophos-class metamaterials need bespoke fab; is there a path to standard foundry?
- **2PP parallel-foci ceiling** — current published SOTA 49 foci (Hahn/Wegener 2024); what unlocks 500+?
- **BTO-as-SLM** — Tom's view is "modulators only." Worth verifying with Altro: is there any device geometry where BTO functions as SLM?
