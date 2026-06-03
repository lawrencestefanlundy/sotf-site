---
type: concept
slug: x-ray-lithography
canonical_name: X-Ray Lithography
aliases:
- X-ray lithography
- XRL
- proximity X-ray lithography
parent_concepts:
- lithography
related_concepts:
- e-beam-lithography
- high-na-euv-lithography
- maskless-lithography
- nanoimprint-lithography
- directed-self-assembly
sources: []
frontier:
- Does any vendor break ground on a high-volume X-ray lithography facility (following Berkeley Lab / LLNL research threads) by 2028?
- Can compact synchrotron X-ray sources (e.g., Lyncean Technologies compact storage ring) reach sufficient brightness and cost for commercial semiconductor use?
- Is X-ray lithography fundable at pre-seed/seed — what beachhead exists that EUV or e-beam does not serve?
last_updated: '2026-06-02'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: e-beam-lithography
  name: E-Beam Lithography
  path: /sotf-site/manufacturing/lithography/e-beam-lithography/
  macro: manufacturing
- slug: high-na-euv-lithography
  name: High-NA EUV Lithography
  path: /sotf-site/manufacturing/lithography/high-na-euv-lithography/
  macro: manufacturing
- slug: maskless-lithography
  name: Maskless Lithography
  path: /sotf-site/manufacturing/lithography/maskless-lithography/
  macro: manufacturing
- slug: nanoimprint-lithography
  name: Nanoimprint Lithography
  path: /sotf-site/manufacturing/lithography/nanoimprint-lithography/
  macro: manufacturing
- slug: directed-self-assembly
  name: Directed Self-Assembly
  path: /sotf-site/manufacturing/lithography/directed-self-assembly/
  macro: manufacturing
---
X-ray lithography (XRL) uses short-wavelength X-rays (typically 0.4–5 nm, soft X-ray to hard X-ray) to expose patterns through a thin transmission mask (typically a silicon nitride or silicon carbide membrane with absorber features in gold or tungsten) onto a resist-coated substrate held in proximity (~10–50 µm gap). The short wavelength — 10 to 100 times shorter than DUV ArF (193 nm) — eliminates optical diffraction as the resolution limiter, enabling in principle sub-20 nm and even sub-10 nm feature resolution without the multilayer mirror optics EUV requires.

The core physics advantage is significant: X-rays expose through modest proximity gaps without the extreme vacuum, multilayer reflective optics, and plasma light sources that make EUV systems >$200M per tool. However, XRL faces three structural problems that have kept it at research scale for four decades. First, mask fabrication: thin membranes with sub-20 nm absorber features at <1 nm placement accuracy are extraordinarily difficult to manufacture and inspect at volume. Second, source brightness: synchrotron sources provide adequate flux but are facility-scale instruments; compact X-ray sources (laser-plasma, compact storage rings) have not achieved the brightness needed for production throughput. Third, limited depth of focus and lack of reduction optics (XRL is typically 1:1, not the 4:1 or 8:1 reduction of optical steppers).

## Frontier

- Does any vendor break ground on a high-volume X-ray lithography facility by 2028?
- Can compact synchrotron X-ray sources reach sufficient brightness and cost for commercial semiconductor use outside specialist MEMS/LIGA applications?
- Is X-ray lithography fundable at pre-seed/seed — what beachhead exists that EUV or e-beam does not already serve?
