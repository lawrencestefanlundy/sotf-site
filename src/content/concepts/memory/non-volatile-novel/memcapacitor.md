---
type: concept
slug: memcapacitor
canonical_name: Memcapacitor
aliases:
- memcapacitive device
- charge-domain memory
- capacitive in-memory compute
- CapRAM
kind: technology
parent_concepts:
- memory
- non-volatile-novel
related_concepts:
- memristor
- rram-reram
- pcm-phase-change-memory
- mram
- feram
- sram
- charge-domain-compute
- 3d-monolithic-integration
sources:
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2024-yole-emerging-memories-2024]]'
frontier:
- Does SEMRON's 3D monolithic CapRAM growth scale at production yield by 2027? (Most binding technical risk for the architecture class.)
- ADC overhead — does the analog→digital conversion cost at column ends cap practical performance, as it has constrained RRAM- and PCM-based IMC?
- Retention and endurance at standard CMOS interface — does charge-trapping suffer the same drift problems as floating-gate flash, or stay clean because the read mode is non-destructive?
- Process portability — does the device work at a single foundry process node (TSMC N16/N12, GF 22FDX) or does it need bespoke fab integration that locks in single-sourcing?
- Temperature calibration — does CapRAM compute accuracy drift across operating temperature in ways that need on-chip compensation circuitry, eating into the energy advantage?
- Competitive cliff with FeFET — does the FeFET roadmap (HfO₂-based, GlobalFoundries 22FDX-FeFET, Sony) close the manufacturing-readiness gap before memcapacitor reaches HVM?
- Application boundary — does the architecture stay edge-only (constrained by ADC overhead at large arrays), or does it scale to LLM decode workloads at hyperscaler volume?
last_updated: 2026-05-07
tags:
- concept
- technology
- analog-computing
- in-memory-computing
- semron
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
---
*Charge-domain analog compute device for in-memory computing*

## Physics and mechanism

A memcapacitor is the capacitive cousin of the **Memristor** — Di Ventra, Pershin and Chua's 2009 framework introduced it as the third of four "memristive" circuit elements (alongside memristor, meminductor, and memristive systems). Where a memristor stores state in its resistance (history of current), a memcapacitor stores state in its **capacitance** (history of voltage). The information is encoded in trapped charge on a floating-gate-like structure, but the read mode is *non-destructive*: capacitance is sensed via a small AC excitation rather than by drawing current through the device.

This is the load-bearing physical advantage. Current-domain analog compute — the dominant approach in commercial RRAM- and PCM-based in-memory-compute (Mythic, IBM NorthPole's analog blocks) — performs matrix-vector multiplication by injecting voltage at row inputs and reading current at column outputs, with weights encoded as conductance. Every operation dissipates I²R energy through the resistive elements. Memcapacitor compute does the same MVM topologically, but charge replaces current as the carrier: voltage at row inputs displaces charge proportional to capacitance × voltage, charges sum at column nodes via Kirchhoff's current law (the ΔQ form, not the I form), and the result is read by sensing accumulated charge. **There is no resistive path through the active device during compute** — the energy floor is set by the digital periphery (ADCs, drivers) and parasitic switching, not by the analog core.

Theoretical efficiency limit is in the high hundreds of TOPS/W; demonstrated SRAM-based digital IMC sits at 10–50 TOPS/W; demonstrated RRAM/PCM analog IMC hits 100+ TOPS/W but with severe variability. Memcapacitor pitches the corner solution: clean physics of charge-domain operation + production-ready manufacturing path of charge-trapping in standard CMOS.

## Physical realisation

Two main routes have been explored:

**Capacitive crossbar arrays (older academic route).** Direct realisation of the Di Ventra topology using thin-film dielectrics (HfO₂, polymer dielectrics) with charge-trapping interfaces. Active in academic labs (TU Delft, UC San Diego, IBM Research) but no commercial production trajectory as of 2026. Most academic work has migrated toward FeFET as a more manufacturable cousin (see "Competitive landscape" below).

The MVM mechanism in either route is the same: weights map to per-cell capacitance values (programmed via charge injection during a write cycle); inputs map to row voltages applied during compute; outputs are total charge accumulated at each column, read by a charge-sensing amplifier. Quantisation is set by the ADC at column outputs and the precision of capacitance modulation per cell — typically 4-6 effective bits for first-generation devices, with paths to 8-bit by averaging across cell groups.

## Competitive landscape

| Approach | TOPS/W (demonstrated) | Precision | Manufacturing readiness | Endurance | Notes |
|---|---|---|---|---|---|
| **Memcapacitor (CapRAM-class)** | Targets 100+ | 4–6 bit native | Standard CMOS + 3D monolithic | High (charge-trapping) | Lead device-class for **Memcapacitor Compute Memory Bound Ai** thesis |
| [RRAM / ReRAM](/sotf-site/memory/non-volatile-novel/rram-reram/) (analog) | 100+ | 4 bit effective | Custom integration | Limited (drift, endurance) | Mythic M1076; conductance variability is the binding constraint |
| [Phase-Change Memory (PCM)](/sotf-site/memory/non-volatile-novel/pcm-phase-change-memory/) | 50–100 | 3-4 bit effective | IBM Almaden has it; commercial limited | Constrained by melt-cycle physics | Phase-change physics caps cycle count |
| [MRAM (STT/SOT-MRAM)](/sotf-site/memory/non-volatile-novel/mram/) (analog) | 5–20 | Full digital | Production at GF, Samsung | High | Great cache; limited compute density |
| FeFET | Targets 50-100 | 4-6 bit | GF 22FDX-FeFET available; Sony research | Improving | Closest peer to memcapacitor; loses on 3D growth + 22FDX-only |
| [SRAM](/sotf-site/memory/volatile/sram/) IMC (digital) | 10-50 | 8-bit native | Production-ready | High | Conservative baseline; EnCharge EN100 |
| Near-memory ([HBM (High-Bandwidth Memory)](/sotf-site/memory/volatile/hbm/) + PIM) | 5-20 | Full | Production-ready | High | Samsung/SK Hynix PIM products; not array-level compute |

**Why memcapacitor specifically beats the analog NVM peers.** Compared to RRAM/PCM, memcapacitor doesn't have the variability problem (capacitance modulation is more deterministic than conductance modulation in filamentary devices) or the endurance problem (charge-trapping at the standard CMOS interface is a mature physics). Compared to MRAM, it scales density via 3D rather than relying on lithography. Compared to FeFET — its closest peer on paper — memcapacitor's CapRAM realisation has a 3D monolithic growth path that FeFET hasn't demonstrated; FeFET also concentrates at GF 22FDX which is single-source.

**What it doesn't beat (yet).** SRAM-based digital IMC remains the conservative baseline — production-proven, foundry-portable, no qualification debt. EnCharge AI's EN100 is the canonical example: lower theoretical efficiency than analog NVM, but ships at standard CMOS density with no exotic process steps. The memcapacitor argument is that the 10× energy efficiency at scale justifies the device-class differentiation; the SRAM argument is that a 2× efficiency advantage at first-day manufacturing readiness wins commercial customers faster.

## Why this matters now

Memory bandwidth is the binding constraint on AI workloads at both edges of the spectrum: edge inference (where HBM doesn't fit the form-factor budget) and datacentre LLM decode (where the autoregressive token loop has low arithmetic intensity and reuses weights with poor locality). The standard architectural fix — bringing compute into memory rather than shuttling data across the von Neumann boundary — has been technically attractive for a decade but economically marginal because every analog NVM technology has shipped with at least one binding flaw (variability, endurance, qualification cost, density). Memcapacitor is the first device class that combines clean physics, manufacturing readiness, and density scaling on a single roadmap. The thesis (**Memcapacitor Compute Memory Bound Ai**) is that this combination is sufficient to capture ≥10% of memory-bandwidth-bound AI accelerator volume by 2030 — split across edge inference and LLM decode workloads.

The competitive watchpoint is whether HBM4/HBM5 supply ramps fast enough to absorb the bandwidth pressure on the datacentre side before analog CIM scales (see **Hbm Bottleneck** supercycle update, 7 May 2026). The 2026-05-07 reframe is mixed for memcapacitor: the bandwidth-substitution narrative weakens as HBM ramps faster than expected; the cost-substitution narrative strengthens as DRAM ASP +80–90% in Q1 2026 makes HBM expensive enough to open a TCO-driven design-in opportunity for analog CIM at price-sensitive workloads.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

## Reading list