---
type: concept
slug: plasma-simulation
canonical_name: Plasma Simulation
aliases:
- plasma modelling
- plasma modeling
- LTP simulation
- low-temperature-plasma simulation
parent_concepts:
- simulation
related_concepts:
- physics-ai
- neural-operators
- machine-learning
sources:
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
frontier:
- Does an ML-surrogate layer become the standard for production etch/deposition recipe development, or do OEMs keep building physics-based sim in-house?
- Who first ships a real-wafer-validated surrogate (not simulator-vs-simulator)?
last_updated: 2026-06-22
tags:
- concept
mention_count: 6
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
neighbors:
- slug: physics-ai
  name: Physics AI
  path: /ai-software/ai-applications/physics-ai/
  macro: ai-software
- slug: neural-operators
  name: Neural Operators
  path: /ai-software/ai-applications/neural-operators/
  macro: ai-software
- slug: machine-learning
  name: Machine Learning
  path: /ai-software/models-inference/machine-learning/
  macro: ai-software
---
Modelling of plasma physics — the two ends being **fusion plasma** (hot, magnetically/inertially confined; GENE/XGC/SOLPS/SOL-KiT, mostly free national-lab codes) and **low-temperature plasma (LTP)** for semiconductor manufacturing (etch/deposition; HPEM/COMSOL/CFD-ACE+). The codes are **disjoint ecosystems** (a fusion model won't run a wafer chamber), though the underlying kinetic machinery (Boltzmann/Vlasov, PIC-MCC, non-Maxwellian EEDF) overlaps — the bridge **Zenithon**'s team exploits via the tokamak scrape-off-layer (see).

## The market sub-cluster (consolidation-by-acquisition)
Standalone plasma-sim software is a **small, consolidated, acqui-buy-shaped niche** — every credible solver asset has been bought by an OEM/EDA player:
- **Lam** ← Coventor (2017), Esgee/VizGlow plasma sim (2022)
- **Applied Materials** ← CFD-ACE+ from ESI (2022)
- **Silvaco** ← Tech-X (2025)
- **Synopsys** ← **Ansys** ($35B, 2025)

**Quantemol** is the cautionary base rate: a standalone plasma-sim/chemistry-data business that stayed tiny and unfunded for ~20 years. The **Zenithon Seed To A Strategy** thesis is that the **ML-surrogate layer on top** (neural operators + proprietary fab-calibration data) is *unbuilt white space* the OEMs haven't shipped — and is what re-rates the category from acqui-buy tool to venture-scale platform.

## Players
- **ML-surrogate layer:** **Zenithon** (plasma process), **SandBox Semiconductor** (etch/dep recipe opt).
- **Physics-based / incumbent:** **COMSOL** (plasma module), **Lam** Semiverse (SEMulator3D — physics-based, not ML), **Quantemol** (QDB/QEC chemistry data on Kushner's HPEM).
