---
type: concept
slug: e-beam-lithography
canonical_name: E-Beam Lithography
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- lithography
related_concepts: []
companies_using:
- advantest
- applied-materials
- asml
- azurlight-systems
- coreize-shanghai-coreize
- elionix
- ev-group-evg
- hitachi-high-tech
- icts-institute-of-computing-technology-spin-off-zhongke-jing
- ims-nanofabrication
- jeol
- kla-corporation
- lam-research-celtric-e-beam
- mapper-lithography-acquired
- multibeam-corporation
- mycronic-formerly-micronic-laser-systems
- nano-dimension
- nanobeam
- nuflare-technology
- oxford-instruments
- raith
- suramp
- tescan
- vistec-electron-beam
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# E-Beam Lithography

*Kind: technology*

## Physics / mechanism

Electron-beam lithography (EBL) fires a focused beam of electrons (typically 10–100 keV) across a resist-coated substrate in a rasterised or vector scan, exposing patterns without a physical mask. Resolution is limited by electron scattering in the resist rather than diffraction, enabling sub-10 nm half-pitch features; leading tools (JEOL JBX-9500, Raith EBPG) achieve ~2–4 nm resolution with ~1 nm placement accuracy. Throughput is the fundamental constraint: writing a full 300 mm wafer at high resolution takes hours vs. seconds for optical tools. EBL is the workhorse for mask/reticle fabrication, photonic IC prototyping, quantum device patterning, and research-scale compound semiconductor work.

## Competitive landscape

---

## Cloudberry relevance

EBL competes directly with optical (DUV/EUV) lithography for high-volume production—it loses on throughput at scale but wins on resolution and maskless flexibility. Nanoimprint lithography (NIL) threatens its prototyping niche with higher throughput and sub-10 nm capability. Multi-beam e-beam (IMS, MAPPER heritage) partially addresses throughput but hasn't displaced EBL in low-volume contexts.

| Dimension | EBL | EUV | NIL |
|---|---|---|---|
| Resolution | ~2–4 nm | ~13 nm HP | ~5 nm |
| Throughput | Very low | High | Medium |
| Mask required | No | Yes | Yes (template) |

Cloudberry/GlobalFoundries-LP context: EBL is critical infrastructure for GF's photonics (silicon photonics PDK), compound semiconductor, and RF process development. Deal angles include resist chemistry startups (CAR alternatives, HSQ successors), next-gen multi-beam platforms, and EBL-adjacent metrology. Quantum hardware and photonic chip companies in the Lunar/Cloudberry portfolio depend on EBL access for device iteration—tool access and write-time cost are real bottlenecks worth tracking.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
