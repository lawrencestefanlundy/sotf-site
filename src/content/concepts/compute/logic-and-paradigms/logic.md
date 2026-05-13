---
type: concept
slug: logic
canonical_name: Compute & Logic
aliases:
- compute-logic
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- logic-and-paradigms
related_concepts: []
companies_using:
- amd
- arm-holdings
- axelera-ai
- brainchip-holdings
- cerebras-systems
- encharge-ai
- esperanto-technologies
- femtosense
- fractile
- hailo-technologies
- intel
- kneron
- loihi-intel-labs-innatera-nanosystems
- mythic
- nvidia
- qualcomm
- rebellions
- recogni
- samsung-semiconductor
- sipearl
- syntiant
- tenstorrent
- tsmc
- untether-ai
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 74
descendants:
- ai-accelerator
- backside-power-delivery
- cfet
- chiplets
- cpu-soc
- cryo-cmos
- fd-soi
- gaa-nanosheet
- risc-v
- ucie
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Compute & Logic

*Kind: technology · Attio deal count: 74*

## Physics / mechanism

Compute & logic encompasses the physical implementation of Boolean and non-Boolean operations in silicon and beyond. Classical CMOS logic operates by switching FETs between conducting and non-conducting states; key parameters are switching energy (~1 fJ/operation at 3 nm node), propagation delay, leakage current, and transistor density (~170M transistors/mm² at TSMC N3). State of the art: gate-all-around (GAA) nanosheet FETs entering HVM, backside power delivery reducing IR drop, and CFET stacking pushing density further. Beyond CMOS: ferroelectric FETs, tunnel FETs, and spintronic devices remain pre-production but attack the energy-per-operation wall that Dennard scaling no longer solves.

## Competitive landscape

---

## Cloudberry relevance

Classical CMOS logic competes with and is complemented by several alternative paradigms:

| Approach | Maturity | Key advantage |
|---|---|---|
| CMOS (Si, SiGe) | HVM | Ecosystem, density, cost |
| GaN / SiC logic | Early | High-voltage, high-temp tolerance |
| Neuromorphic / analog compute | Research–pilot | Energy efficiency for inference workloads |

Photonic logic (MZI-based, integrated) is an adjacent bet for latency-critical interconnect-compute fusion. Cryogenic RSFQ logic (superconducting) is relevant for quantum control planes. Each trades fab compatibility against performance headroom.

---

GF's differentiated nodes (22FDX, 45SPCLO for cryo/RF) create deal-flow in logic-adjacent fabless startups that need neither bleeding-edge density nor commodity pricing — the exact gap Cloudberry targets. Ferroelectric memory-in-logic (Radiant Technologies context) and photonic-electronic co-integration (photonics LP angle) both sit here. Pipeline watch: edge-AI accelerator startups, secure-enclave logic IP, and cryogenic control ASICs for quantum.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
