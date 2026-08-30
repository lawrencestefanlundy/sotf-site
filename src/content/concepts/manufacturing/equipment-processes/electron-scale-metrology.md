---
type: concept
slug: electron-scale-metrology
canonical_name: Electron-scale metrology
aliases:
- electron-level metrology
- in-situ electron metrology
parent_concepts:
- semiconductor-materials-equipment
- materials-discovery
related_concepts:
- arpes
- stm
- contact-resistance
- semiconductor-equipment
sources: []
frontier:
- Is "STM + ARPES integrated with epitaxial growth" a Pauli-specific moat, or is it a broader capability emerging across Stanford SLAC, IMEC, Brookhaven, PNNL?
- Does foundry-scale 300mm tooling exist or only research-scale coupons?
- What is the first commercially-validated material stack discovered via this method? When?
- Patent landscape — is the methodology defensible or is the material the patentable object?
last_updated: 2026-05-27
tags:
- concept
- semiconductors
descendants:
- arpes
- stm
public_expressions:
- IBM
- INTC
- STM
- TSM
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
neighbors:
- slug: arpes
  name: ARPES (Angular-Resolved Photoemission Spectroscopy)
  path: /manufacturing/equipment-processes/arpes/
  macro: manufacturing
- slug: stm
  name: STM (Scanning Tunneling Microscopy)
  path: /manufacturing/equipment-processes/stm/
  macro: manufacturing
- slug: contact-resistance
  name: Contact resistance
  path: /manufacturing/equipment-processes/contact-resistance/
  macro: manufacturing
- slug: semiconductor-equipment
  name: Semiconductor Equipment
  path: /manufacturing/equipment-processes/semiconductor-equipment/
  macro: manufacturing
---
Direct measurement of electronic band structure (energy + momentum) **at the interface, as the material stack is being grown** — using condensed-matter physics tools (STM, ARPES) integrated with industrial deposition equipment (PVD, PLD, MBE).

## Why it matters

The semiconductor industry's metrology stack measures *atoms* (TEM, XRD, atomic-scale lithography characterisation) and *averaged electrical behaviour* (I-V, R, C on finished devices). It does not measure *electrons directly*.

Resistance, mobility, current — these are averaged proxies for what electrons actually do at material interfaces. As nodes shrink and interface area grows as a fraction of device volume, this proxy gap is now the dominant source of device-level performance variance.

If you can measure electrons directly during growth, you close the loop:
- **Faster discovery:** months instead of years for a new contact material
- **Cheaper:** coupon-scale, no lithography, no full device fab
- **Higher ceiling:** approach the ballistic-transport theoretical limit, not just incremental atomic-scale tweaks

## The instruments

- [STM (Scanning Tunneling Microscopy)](/manufacturing/equipment-processes/stm/) — scanning tunneling microscopy. Tip-on-surface imaging of individual atoms and their local electronic state. Slow but direct.
- [ARPES (Angular-Resolved Photoemission Spectroscopy)](/manufacturing/equipment-processes/arpes/) — angular-resolved photoemission spectroscopy. Shine UV/X-ray light on a surface, photoelectrons fly out; measure their energy + emission angle to reconstruct the electronic band structure E(k). Fast, integrative.

## What's novel

1. **In-situ integration with growth.** STM+ARPES measure samples in the same vacuum-continuous platform where PVD/PLD/MBE deposits them. No breaking vacuum, no transferring between tools.
2. **Industrial application.** Historically these tools have been used on exotic correlated materials (high-Tc superconductors, manganites, multiferroics) where you write Nature/Science papers. Industrial silicon-stack discovery is unconventional.
3. **Volume.** 75-target PVD + multi-modality (PLD, MBE) means combinatorial materials sweep at coupon scale.

## Frontier questions

## Comparable approaches (incumbent)

- **DFT-based materials screening** at IMEC + every foundry's internal materials team. Computational, not experimental.
- **Combinatorial materials discovery** (cf. **Intermolecular** — sold to Merck KGaA for ~$60M after IPO, cautionary tale).
- **In-line metrology inside foundries** — at-wafer X-ray photoelectron spectroscopy (XPS), but only on finished films, not during growth.

## Companies