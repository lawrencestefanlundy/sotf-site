---
type: concept
slug: pockels-modulators
canonical_name: Pockels Modulators
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- modulators-detectors
related_concepts: []
companies_using:
- agiltron
- applied-electro-optics-aeo
- covega-now-thorlabs
- enlightia-formerly-psiquantum-spin-out-context-nanolayers-ph
- eospace
- fujitsu-optical-components
- gigpeak-acquired-by-integrated-device-technology
- gooch-housego
- hyperlight-photonics
- hyperlight
- ii-vi-incorporated-coherent-corp
- ixblue-now-exail-photonics
- jenoptik
- ligentec
- lumentum
- luxtelligence
- optiwave-photonics
- partow-technologies
- photline-technologies-acquired-by-ixblueexail
- polight-part-of-almae-technologies-ecosystem-almae-technolog
- shengshi-optical-castech
- sumitomo-osaka-cement
- thorlabs
- wuhan-yangtze-soton-laser-ysl-photonics
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Pockels Modulators

*Kind: technology*

## Physics / mechanism

Pockels modulators exploit the linear electro-optic (Pockels) effect: an applied electric field induces a refractive index change proportional to field strength, shifting the phase of transmitted light. Configured in a Mach-Zehnder interferometer, phase shift converts to amplitude modulation. Key figure of merit is Vπ·L (half-wave voltage × electrode length); best-in-class thin-film lithium niobate (TFLN) on insulator hits Vπ·L < 2 V·cm with electro-optic bandwidths exceeding 100 GHz and on-chip insertion loss < 3 dB. Competing material platforms include BTO (barium titanate, r₄₂ ~1000 pm/V but integration complexity) and organic EO polymers (r₃₃ up to 300 pm/V, thermal stability issues). TFLN is currently the commercially dominant waveguide platform for hyperscale coherent interconnects and microwave photonics.

## Competitive landscape

Incumbent silicon photonics plasma-dispersion modulators operate at Vπ·L ~20 V·cm with bandwidths typically < 50 GHz and introduce free-carrier absorption loss. III-V (InP) modulators offer monolithic integration with lasers but at higher cost and lower yield. Germanium EAMs are compact but bandwidth-limited and lossy.

## Cloudberry relevance

| Platform | Vπ·L (V·cm) | BW (GHz) | CMOS foundry compatible |
|---|---|---|---|
| TFLN | <2 | >100 | Partial (heterogeneous) |
| Si plasma | ~20 | <50 | Yes |
| BTO | ~0.2 | >100 | Emerging |


TFLN and BTO modulators sit directly in Cloudberry's photonics/advanced materials thesis. GlobalFoundries has active heterogeneous photonics capabilities (GF Fotonix); deal-flow targets include TFLN foundry enablement plays, BTO-on-Si integration startups, and IP stacks for co-packaged optics entering hyperscaler and defence microwave-photonics procurement cycles. Bandwidth and Vπ are now spec-table line items in datacenter switch RFQs — modulator performance is a fundable wedge.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
