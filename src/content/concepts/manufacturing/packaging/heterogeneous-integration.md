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
- ucie
sources: []
frontier:
- What is the practical yield floor for heterogeneous integration of known-good-die at sub-10 µm bump pitch — is KGD test the binding constraint on cost?
- When do photonic chiplets enter heterogeneous integration production stacks alongside electronic logic and HBM?
- Does the CHIPS Act and EU Chips Act capex wave materially expand HI packaging capacity outside Taiwan/Korea by 2028?
last_updated: '2026-06-02'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: 3d-ic-stacking
  name: 3D IC Stacking
  path: /sotf-site/manufacturing/packaging/3d-ic-stacking/
  macro: manufacturing
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /sotf-site/manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
- slug: tsv-through-silicon-via
  name: TSV / Through-Silicon Via
  path: /sotf-site/manufacturing/packaging/tsv-through-silicon-via/
  macro: manufacturing
- slug: cowos
  name: CoWoS (TSMC)
  path: /sotf-site/manufacturing/packaging/cowos/
  macro: manufacturing
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /sotf-site/manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: chiplets
  name: Chiplets
  path: /sotf-site/compute/compute-architecture/chiplets/
  macro: compute
- slug: ucie
  name: UCIe (Universal Chiplet Interconnect Express)
  path: /sotf-site/compute/compute-architecture/ucie/
  macro: compute
---
Heterogeneous integration (HI) is the assembly of multiple distinct semiconductor dies — each optimised at a different process node, material system, or technology — into a single package that functions as a unified system. Unlike monolithic SoC integration, which forces all functional blocks onto one process node, HI allows logic, memory, RF, photonic, and analogue dies to be individually optimised (e.g., CMOS logic at 3 nm TSMC N3E, HBM DRAM at LPDDR-class stacked DRAM, RF front-end at GaAs or GaN) and then assembled via advanced packaging interconnects.

The enabling techniques span a spectrum of interconnect pitch and density. At the coarsest level, wire bonding and flip-chip with controlled-collapse chip connection (C4 bumps, ~100–150 µm pitch) are mature. Advanced HI moves to micro-bumps (~20–40 µm), copper pillars, and ultimately hybrid bonding (direct Cu-Cu thermocompression, sub-1 µm pitch, no solder) — enabling die-to-die interconnect bandwidths that approach monolithic integration. Silicon interposers, through-silicon vias ([TSV / Through-Silicon Via](/sotf-site/manufacturing/packaging/tsv-through-silicon-via/)), and silicon bridges (Intel EMIB) provide the routing fabric between dies. TSMC CoWoS ([CoWoS (TSMC)](/sotf-site/manufacturing/packaging/cowos/)), Samsung X-Cube, and Intel Foveros are the leading HI packaging platforms.

The investment logic for **Chiplets Architecture Share** is directly anchored in HI: the chiplet thesis is that monolithic die economics break at advanced nodes (reticle limits, yield curves, cost of single-node forcing), and HI provides the integration layer that makes disaggregated chiplet designs economically viable. The **Brain Computer Interfaces** frontier also touches HI: hybrid-bonded CMOS-on-CMOS stacks are being explored as the density mechanism for neural recording arrays. Deal-flow angles include HI substrate specialists, known-good-die test, yield analytics, and die-to-die interconnect IP.

## Frontier

- What is the practical yield floor for heterogeneous integration of known-good-die at sub-10 µm bump pitch — is KGD test the binding constraint on cost?
- When do photonic chiplets enter heterogeneous integration production stacks alongside electronic logic and HBM?
- Does the CHIPS Act and EU Chips Act capex wave materially expand HI packaging capacity outside Taiwan and Korea by 2028?
