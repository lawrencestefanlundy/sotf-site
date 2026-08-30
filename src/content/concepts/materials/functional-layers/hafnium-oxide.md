---
type: concept
slug: hafnium-oxide
canonical_name: Hafnium Oxide
aliases:
- HfO2
- hafnia
- ferroelectric hafnium oxide
- HZO
- hafnium zirconium oxide
parent_concepts:
- high-k-dielectrics
related_concepts:
- ferroelectric-materials
- piezoelectric
- aluminium-oxide
- barium-titanate
sources:
- '[[2024-yole-emerging-memories-2024]]'
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2012-02-07-new-form-of-hafnium-oxide-developed-by-cambridge-university-]]'
frontier:
- Does the wake-up / imprint reliability of HZO FeFET reach automotive-grade spec (10^12 cycles, 10-year data retention at 125°C) without exotic anneal steps that break BEOL compatibility?
- Can Si-doped HfO2 reach a practical Pockels coefficient (>20 pm/V) in a production-compatible photonic modulator stack — and if so, does it share fab tooling with FeFET memory on the same node?
- What is the scaling floor for ferroelectric HfO2 before the orthorhombic phase becomes thermodynamically unstable — is there a hard <3 nm cutoff?
last_updated: '2026-06-02'
tags:
- concept
mention_count: 14
sources_7d: 0
sources_30d: 3
recent_mentions:
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
- slug: 2012-02-07-new-form-of-hafnium-oxide-developed-by-cambridge-university-
  title: New form of hafnium oxide developed by Cambridge University - enterprise.cam.ac.uk
  date: '2012-02-07'
  kind: web
neighbors:
- slug: ferroelectric-materials
  name: Ferroelectric Materials
  path: /materials/advanced-materials/ferroelectric-materials/
  macro: materials
- slug: piezoelectric
  name: Piezoelectric
  path: /materials/functional-layers/piezoelectric/
  macro: materials
- slug: aluminium-oxide
  name: Aluminium Oxide
  path: /materials/functional-layers/aluminium-oxide/
  macro: materials
- slug: barium-titanate
  name: Barium Titanate
  path: /materials/functional-layers/barium-titanate/
  macro: materials
---
Hafnium oxide (HfO₂) is the high-k gate dielectric that replaced SiO₂ at Intel's 45 nm node in 2007 and has been standard in advanced CMOS ever since. Its core gate-dielectric role: dielectric constant κ ~20–25 (vs SiO₂ ~3.9), enabling physically thicker films that suppress gate leakage while achieving the same sub-1 nm equivalent oxide thickness (EOT). Deposited by ALD at temperatures compatible with back-end-of-line (BEOL) processing (~300–500°C), it is thermally stable on silicon.

The more recent and higher-potential application is ferroelectric HfO₂. When HfO₂ is doped with Si, Al, Y, or Zr (the Hf₀.₅Zr₀.₅O₂ alloy, HZO, is the most studied) and deposited as a thin film (<10 nm), the orthorhombic crystal phase (Pca2₁) is stabilised over the paraelectric monoclinic ground state, producing spontaneous polarisation of 10–30 µC/cm² and a coercive field of ~1–2 MV/cm. This makes it ferroelectric — a property that had previously only been found in complex oxides (PZT, BaTiO₃) requiring high-temperature anneal steps and thick films incompatible with CMOS processes. HZO's CMOS integration and sub-10 nm scalability are its defining advantages over all prior ferroelectric materials.

Ferroelectric HfO₂ enables two device families: FeFET (ferroelectric field-effect transistor, non-volatile logic with near-zero standby power) and FeRAM (ferroelectric RAM, fast, high-endurance embedded NVM). GlobalFoundries 22FDX already ships embedded FeFET NVM in production; TSMC and Samsung are integrating HZO at their advanced nodes. **Ferroelectric Memory Share** tracks the thesis that HfO₂-based ferroelectric memory captures ≥5% of embedded NVM by 2030 via CMOS-compatible BEOL integration in MCUs and IoT ASICs.

A third, earlier-stage vector: Si-doped HfO₂ has a measurable Pockels coefficient (~10–30 pm/V in research stacks), opening photonic electro-optic modulator applications on CMOS-native fab lines — directly relevant to any foundry (GF 22FDX) running both FeFET and photonics PDKs.

[Ferroelectric Materials](/materials/advanced-materials/ferroelectric-materials/) is the parent concept covering the broader class; this page covers HfO₂'s specific CMOS-native mechanism and applications.

## Frontier

See frontmatter `frontier:` block.
