---
type: concept
slug: micro-transfer-printing
canonical_name: Micro-Transfer-Printing
aliases:
- μTP
- uTP
- micro transfer printing
- transfer printing
kind: technology
parent_concepts:
- heterogeneous-photonic-integration
- advanced-packaging
related_concepts:
- heterogeneous-photonic-integration
- inp-photonics
- silicon-nitride
sources:
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-07-07-the-asml-killer]]'
last_updated: '2026-06-26'
tags:
- concept
- technology
mention_count: 12
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-07-the-asml-killer
  title: The ASML Killer?
  date: '2026-07-07'
  kind: substack
- slug: 2026-04-14-the-photonic-foundry-fallacy
  title: The Photonic Foundry Fallacy
  date: '2026-04-14'
  kind: substack
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
neighbors:
- slug: heterogeneous-photonic-integration
  name: Heterogeneous Photonic Integration
  path: /photonic-systems/pic-platforms/heterogeneous-photonic-integration/
  macro: photonic-systems
- slug: inp-photonics
  name: InP Photonics
  path: /photonic-systems/pic-platforms/inp-photonics/
  macro: photonic-systems
- slug: silicon-nitride
  name: Silicon Nitride
  path: /materials/substrates/silicon-nitride/
  macro: materials
---
## Mechanism

Micro-transfer-printing (μTP) uses an elastomer (PDMS) stamp to pick up arrays of pre-fabricated micro-devices — III-V gain dies (SOAs, lasers), photodetectors, micro-LEDs, thin-film chiplets — from their native source wafer and print them onto a foreign target wafer (silicon, SiN, or a finished CMOS/photonic wafer). Adhesion is kinetically controlled: fast peel grabs the device, slow release deposits it. Because it transfers *finished* devices rather than growing or bonding material in place, μTP sidesteps the thermal-budget and lattice-mismatch limits that constrain monolithic and wafer-bonding heterogeneous integration.

## Why it matters here

μTP is the leading route to the **multi-material primitive** ("any material on any platform") that **Photonic Multimaterial Foundry** and **Photonics Material Class War** turn on: it lets one platform host III-V gain + SiN/Si passive + other material classes without a shared epitaxy or a single thermal budget. The merchant IP gatekeeper is **X Celeprint** (now Xtrion/X-FAB-owned); the production lineage runs through Tyndall (**Brian Corbett**, **Ruggero Loi**) and imec. Competes with wafer/hybrid bonding and monolithic III-V-on-Si.

## Frontier (open questions)

- Throughput / cost vs wafer bonding at production volume.
- Whether μTP becomes an open merchant foundry service (the white-space gap: only X-Celeprint licenses it today).
