---
type: concept
slug: photonic-eda
canonical_name: Photonic Eda
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 2
frontier:
- Which organisations, if any, currently offer a third-party-accessible PDK for heterogeneous photonic integration, and on what commercial terms?
- Does a captive-process model measurably slow or accelerate time-to-volume compared with an open-PDK model on the same foundry line?
- Can a neutral EDA layer support device models across multiple heterogeneous integration flows, or are models tied to a single patented process?
- What design-rule and model fidelity is required before third-party photonic designers achieve first-pass tape-out success on a heterogeneous flow?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
neighbors: []
---
## Physics / mechanism

Photonic EDA is the design-automation layer for photonic integrated circuits: the process design kits (PDKs), component libraries and simulation/layout tooling that let a designer target a specific fabrication process without owning it. In electronics the equivalent layer is a commodity, supplied by foundries and third-party tool vendors; in photonics the sources address it as an open question of who occupies the neutral PDK/EDA layer for heterogeneous integration.

The distinguishing parameter is whether a process is offered to outside parties at all. A PDK play requires the process owner to expose device models and design rules so that third-party designers can tape out. The alternative is a captive process: the fabrication flow is licensed or patented for internal use only, and monetisation happens through finished products rather than design access. Scintil is described by its own communications as the latter, with no PDK offered externally and the process not for sale; its SHIP (Scintil Heterogeneous Integrated Photonics) flow is patented by CEA-Leti and licensed exclusively and worldwide to Scintil, alongside Scintil's own process and design patents.

The company's self-description, "fabless with a captive process", with an analogy to MEMS and InvenSense-style fabless-with-process-IP at specialty foundries, marks out a distinct business shape from both pure-play foundry and asset-light PDK licensing. Under this model the process can still run on someone else's wafer line: SHIP is stated by the company to run in production volume on Tower's 200 mm lines. Access to the fab, therefore, is not the same as access to the PDK.

## Competitive landscape

| Model | Process access for third parties | Monetisation |
|---|---|---|
| Neutral PDK/EDA layer | Yes, by design | Design access, tooling, IP licensing |
| Fabless with captive process (Scintil) | No PDK to outside parties; process not for sale | Product sales, first family LEAF Light, a single-chip DWDM laser source |

The sources establish that at least one prominent heterogeneous-integration process is explicitly not a PDK play, which narrows rather than fills the neutral-layer slot. Who does occupy that layer remains the open research question in the source itself.

## Evidence base

- Research on 11 Jul 2026 framed the question of who actually occupies the neutral PDK/EDA layer for heterogeneous photonic integration, and how the opportunity and risks should be framed.
- Company communications dated 10 Jul 2026 corrected a draft characterisation of Scintil as a live example of the asset-light PDK play; no PDK is offered to outside parties and the process is not for sale.
- SHIP is patented by CEA-Leti and licensed exclusively and worldwide to Scintil, plus Scintil's own process and design patents.
- Scintil's stated monetisation is product sales, with LEAF Light, a single-chip DWDM laser source, as the first product family.
- Per the company, SHIP runs in production volume on Tower's 200 mm lines.
- A 10 Jul 2026 preprint reporting an end-to-end hybrid quantum-classical pipeline for de novo design of MHC class I-binding peptides, coupling a GAN to latent vectors sampled from a real photonic quantum processor, is indexed against photonic-eda among other photonic concepts.

## Frontier (open questions)

- Which organisations, if any, currently offer a third-party-accessible PDK for heterogeneous photonic integration, and on what commercial terms?
- Does a captive-process model measurably slow or accelerate time-to-volume compared with an open-PDK model on the same foundry line?
- Can a neutral EDA layer support device models across multiple heterogeneous integration flows, or are models tied to a single patented process?
- What design-rule and model fidelity is required before third-party photonic designers achieve first-pass tape-out success on a heterogeneous flow?

*Synthesised 2026-08-31 from 2 KB sources by the resynth pipeline; citations are KB source slugs.*
