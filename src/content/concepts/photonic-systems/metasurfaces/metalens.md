---
type: concept
slug: metalens
canonical_name: Metalens
aliases:
- meta-lens
- metalenses
- meta-lenses
- planar-lens
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- metasurfaces
related_concepts:
- metasurfaces-flat-optics
- metamaterials
- nanoimprint-lithography
- maskless-lithography
- e-beam-lithography
- silicon-photonics
companies_using:
- metalenz
- nil-technology-nilt
- radiant-opto-electronics
- imagia-formerly-nanotech-security
- shenzhen-metalenx-technology
- tunoptix
- oblate-optics
- phantom-photonics
- pencil-of-rays
- swave-photonics
- cnuic
- stmicroelectronics
- samsung-advanced-institute-of-technology-sait
- huawei-central-research-institute-optics
- nikon-precision-division
- polight
ideas_referencing:
- european-sovereignty-stack
- photonic-foundry-capacity
sources: []
frontier:
- When does metalens-only consumer optics shipment exceed 1B units/year (current ~140M cumulative across ST/Metalenz partnership)?
- Does any major smartphone OEM replace its primary camera lens stack (vs ToF auxiliary) with a metalens by 2028?
- Does NIL or maskless-lithography become the dominant production process by 2028, displacing e-beam-prototyping bottleneck?
- How many of the ~15 companies on the metasurfaces-flat-optics page survive the metalens consolidation cycle (NILT-Radiant acquisition was the first; expect 3-5 more by 2028)?
- Does European metalens IP retention vs Asian-acquirer flow continue (NILT → Radiant 2025 was a sovereignty leak; will the next 3 EU metalens companies follow)?
last_updated: '2026-05-08'
tags:
- concept
- technology
- metalens
- meta-optics
- photonics
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 1
---

# Metalens

*Kind: technology · child of [[metasurfaces-flat-optics]]*

## Physics / mechanism

A metalens is a planar metasurface engineered to perform the focusing function of a conventional curved lens. Sub-wavelength meta-atoms (typically TiO₂, GaN, or amorphous silicon pillars, 50–400 nm feature size) are patterned on a flat substrate; the local geometry of each atom imposes a phase delay on incident light, so the array as a whole imparts a hyperboloidal phase profile equivalent to a curved lens. Replaces stacked refractive elements with a single planar layer fabricated by semiconductor processes (e-beam in the lab, DUV / nanoimprint in production).

Operating regimes:
- **Visible / NIR consumer**: TiO₂ on glass at ~90% diffraction efficiency at 532 nm, NA up to 0.9 demonstrated in lab. Production-grade NA ~0.5.
- **MWIR / LWIR**: GaN-on-silicon or amorphous-Si on Si-substrate; lower efficiency tolerance, currently dominant in industrial sensing.
- **UV**: HfO₂ / SiO₂ candidates; mostly research-stage.

Key constraints in 2026: chromatic aberration (broadband performance still 2-5x worse than refractive), polarisation sensitivity (some designs work only for one polarisation), and **fabrication economics** — the lithography step is the cost driver, not the substrate. This is what makes [[nanoimprint-lithography]] (and [[maskless-lithography]] / multi-beam laser interference per **Cnuic**) the production-scaling enabler.

## Competitive landscape

| Approach | Form factor | Volume process | Diffraction efficiency | Status |
|---|---|---|---|---|
| Refractive (curved glass / molded) | 3D stack | Injection / grinding | ~99% | Mature, cheap |
| Diffractive optical element (DOE) | Planar | Embossing / etch | 60-80% (visible) | Mature in IR |
| Metalens (TiO₂ / GaN) | Planar (single layer) | NIL or DUV | 70-90% (visible, monochromatic) | Production at consumer scale (Metalenz/ST since 2023) |
| MEMS-tunable | Planar + actuated | MEMS process | Variable | Niche |

**Production trajectory.** Metalenz + STMicroelectronics shipped the first commercial metasurface in a consumer ToF sensor (VL53L8) in 2023. Cumulative shipments ~140M as of 2025. NIL Technology (NILT, Denmark) is the parallel production-process leader, vertically integrated through nanoimprint masters → meta-optic modules; acquired by Taiwan's **Radiant Opto Electronics** for €300M in Jan 2025 (signed Sept 2024).

**The CNUIC angle (May 2026).** **Cnuic** explicitly names metalenses + meta-surfaces + metamaterials as its initial commercial focus because high fabrication complexity is the bottleneck on adoption — multi-beam laser interference lithography is positioned as the 3D-pattern-capable maskless alternative to e-beam (slow) and nanoimprint (contact-method limits, struggles with slanted/pyramid 3D structures).

## Cloudberry relevance

Direct deal-flow relevance via three angles:

1. **Process equipment** — lithography tools that scale metalens production beyond e-beam prototyping. CNUIC fits here. NIL equipment vendors (EVG, SUSS MicroTec, Obducat) are mature.
2. **Material / device IP** — metasurface IP startups designing for specific applications (AR waveguides, ToF, biometrics, automotive LiDAR, MWIR thermal). Capasso lab descendants are the canonical pool.
3. **Vertical-integration** — companies bundling design + fab + module like NILT (now Radiant). Path-to-exit: strategic acquirer (Asian display / module incumbents — Radiant pattern; or Apple/Samsung captive integration).

**Sovereignty observation.** The 2025 NILT → Radiant acquisition is a tile in the **European Sovereignty Stack** bear case: a €300M Danish meta-optics IP base flowed to a Taiwanese acquirer because European mass-production scale-up financing was thinner than Asian backlight-module incumbent's strategic capital. Watch for the next 3 EU metalens companies — Cloudberry has a vantage point on this via Conformally / CNUIC ecosystem.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

See frontmatter `frontier:` block.
