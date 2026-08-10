---
type: concept
slug: heterogeneous-integration
canonical_name: Heterogeneous Integration
aliases:
- hetero-integration
- heterogeneous integration
- HI
parent_concepts:
- advanced-packaging
related_concepts:
- 3d-ic-stacking
- hybrid-bonding
- tsv-through-silicon-via
- cowos
- co-packaged-optics
- chiplets
sources:
- '[[2026-03-26-sotf-interview-dorian-haci-mintneuro]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-04-09-photonics-material-class-war-photonic-integrated-circuit]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-07-11-neutral-pdk-heterogeneous-integration-landscape]]'
- '[[2026-04-10-photonic-light-source-supply-co-packaged-optics-cpo-scaling]]'
frontier:
- What is the practical yield floor for heterogeneous integration of known-good-die at sub-10 µm bump pitch — is KGD test the binding constraint on cost?
- When do photonic chiplets enter heterogeneous integration production stacks alongside electronic logic and HBM?
- Does the CHIPS Act and EU Chips Act capex wave materially expand HI packaging capacity outside Taiwan/Korea by 2028?
last_updated: '2026-06-02'
tags:
- concept
mention_count: 63
sources_7d: 6
sources_30d: 10
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
- slug: 2026-04-10-photonic-light-source-supply-co-packaged-optics-cpo-scaling
  title: Co-Packaged Optics (CPO) – Scaling with Light for the Next Wave of Interconnect
  date: '2026-04-10'
  kind: web
- slug: 2026-04-09-photonics-material-class-war-photonic-integrated-circuit
  title: Photonic Integrated Circuit Technology Landscape 2026
  date: '2026-04-09'
  kind: web
- slug: 2026-03-26-sotf-interview-dorian-haci-mintneuro
  title: 'Chips for the Brain: Modular Semiconductors for Neural Interfaces (MintNeuro / Dorian Haci)'
  date: '2026-03-26'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
neighbors:
- slug: 3d-ic-stacking
  name: 3D IC Stacking
  path: /manufacturing/packaging/3d-ic-stacking/
  macro: manufacturing
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
- slug: tsv-through-silicon-via
  name: TSV / Through-Silicon Via
  path: /manufacturing/packaging/tsv-through-silicon-via/
  macro: manufacturing
- slug: cowos
  name: CoWoS (TSMC)
  path: /manufacturing/packaging/cowos/
  macro: manufacturing
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: chiplets
  name: Chiplets
  path: /compute/compute-architecture/chiplets/
  macro: compute
---
Heterogeneous integration (HI) is the assembly of multiple distinct semiconductor dies — each optimised at a different process node, material system, or technology — into a single package that functions as a unified system. Unlike monolithic SoC integration, which forces all functional blocks onto one process node, HI allows logic, memory, RF, photonic, and analogue dies to be individually optimised (e.g., CMOS logic at 3 nm TSMC N3E, HBM DRAM at LPDDR-class stacked DRAM, RF front-end at GaAs or GaN) and then assembled via advanced packaging interconnects.

The enabling techniques span a spectrum of interconnect pitch and density. At the coarsest level, wire bonding and flip-chip with controlled-collapse chip connection (C4 bumps, ~100–150 µm pitch) are mature. Advanced HI moves to micro-bumps (~20–40 µm), copper pillars, and ultimately hybrid bonding (direct Cu-Cu thermocompression, sub-1 µm pitch, no solder) — enabling die-to-die interconnect bandwidths that approach monolithic integration. Silicon interposers, through-silicon vias ([TSV / Through-Silicon Via](/manufacturing/packaging/tsv-through-silicon-via/)), and silicon bridges (Intel EMIB) provide the routing fabric between dies. TSMC CoWoS ([CoWoS (TSMC)](/manufacturing/packaging/cowos/)), Samsung X-Cube, and Intel Foveros are the leading HI packaging platforms.

The investment logic for **Chiplets Architecture Share** is directly anchored in HI: the chiplet thesis is that monolithic die economics break at advanced nodes (reticle limits, yield curves, cost of single-node forcing), and HI provides the integration layer that makes disaggregated chiplet designs economically viable. The **Brain Computer Interfaces** frontier also touches HI: hybrid-bonded CMOS-on-CMOS stacks are being explored as the density mechanism for neural recording arrays. Deal-flow angles include HI substrate specialists, known-good-die test, yield analytics, and die-to-die interconnect IP.

## Frontier

- What is the practical yield floor for heterogeneous integration of known-good-die at sub-10 µm bump pitch — is KGD test the binding constraint on cost?
- When do photonic chiplets enter heterogeneous integration production stacks alongside electronic logic and HBM?
- Does the CHIPS Act and EU Chips Act capex wave materially expand HI packaging capacity outside Taiwan and Korea by 2028?
