---
type: concept
slug: lidar
canonical_name: LiDAR
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- sensing
- ranging-detection
related_concepts: []
companies_using:
- aeva-technologies
- aeye
- blickfeld
- cepton-acquired-by-koito
- eigenspace
- geodetics
- hesai-technology
- ibeo-automotive-restructured-as-microvision-partner
- innoviz-technologies
- liteon-lumentum-lidar-division
- livox-dji-subsidiary
- luminar-technologies
- mobileye-intel
- opsys-tech
- ouster-now-ouster-velodyne-merged-as-ouster
- outsight
- pointcloud-steerpath
- quanergy-systems
- robosense
- seyond-formerly-innovusion
- silc-technologies
- valeo
- waymo-alphabet
- xenomatix
ideas_referencing: []
sources:
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 16
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 2
---

# LiDAR

*Kind: technology · Attio deal count: 10*

## Physics / mechanism

LiDAR (Light Detection and Ranging) emits pulsed or modulated laser light and measures time-of-flight (ToF) or phase shift of returned photons to reconstruct 3D point clouds. Core variants: mechanical spinning (360° FoV, legacy), MEMS-mirror scanning (miniaturised, lower reliability ceiling), optical phased arrays (OPA, solid-state, CMOS-compatible), and FMCW (frequency-modulated continuous wave, coherent detection, simultaneous velocity via Doppler). Key parameters: range (automotive target ≥200 m), angular resolution (<0.1°), frame rate (>10 Hz), eye-safety class (905 nm vs 1550 nm tradeoffs), and photon detection efficiency. FMCW at 1550 nm is current performance frontier—Aeva, Aurora, Luminar pushing silicon photonics and InGaAs APD/SPAD receiver integration. Point cloud density now >1M points/sec in top-tier systems.

## Competitive landscape


Competing sensing modalities for depth/environment mapping:

| Modality | Range | Resolution | Key weakness |
|---|---|---|---|
| Camera + ML (pseudo-LiDAR) | Unbounded | High 2D, depth inferred | Depth accuracy degrades, lighting-dependent |
| Radar (77 GHz / 4D imaging) | >300 m | Low angular | No fine geometry, poor object classification |
| Structured light / ToF camera | <10 m | Medium | Short range, sunlight interference |

## Cloudberry relevance
FMCW LiDAR vs direct-ToF is the primary internal battleground. Silicon photonics integration (SiPh) is the cost-reduction lever consolidating OPA and FMCW onto foundry processes.


Cloudberry relevance is direct: LiDAR is a photonics-on-silicon problem. SiPh transceivers, SPAD arrays, InP/InGaAs gain chips, and III-V-on-Si bonding all sit inside Cloudberry's photonics thesis. GlobalFoundries runs 300 mm SiPh (GF Fotonix), making LiDAR receiver/transceiver chiplets natural deal-flow. FMCW startups needing foundry-qualified photonic IC processes are pipeline candidates. Lunar Ventures' deep-tech network surfaces early sensing IP. Watch coherent receiver ASICs and integrated photonic front-ends as the defensible semiconductor wedge.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
