---
type: concept
slug: metal-additive-manufacturing
canonical_name: Metal Additive Manufacturing
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2022-05-09-elementum-funded-by-darpa-to-develop-am-process-for-rhenium-]]'
- '[[2021-02-04-meta-additive-awarded-innovate-uk-smart-grant-for-bjt-proces]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 5
frontier:
- Does the parametric PINN framework reproduce measured melt-pool temperature fields for materials entirely absent from training, and at what quantified error against thermography or thermocouple data?
- Can in-situ alloying and hybrid processing raise the fraction of reliably printable aluminium alloys, and by how much relative to the current "small percentage" baseline?
- Do L-DED aluminium parts achieve the claimed stress corrosion cracking resistance advantage over steel counterparts in standardised testing?
- What deposition rates, densities and mechanical properties were achieved in the DARPA-funded rhenium AM process, and did it progress beyond feasibility?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2022-05-09-elementum-funded-by-darpa-to-develop-am-process-for-rhenium-
  title: Elementum funded by DARPA to develop AM process for rhenium - Metal Additive Manufacturing magazine
  date: '2022-05-09'
  kind: web
- slug: 2021-02-04-meta-additive-awarded-innovate-uk-smart-grant-for-bjt-proces
  title: Meta Additive awarded Innovate UK SMART Grant for BJT process - Metal Additive Manufacturing magazine
  date: '2021-02-04'
  kind: web
neighbors: []
---
## Physics / mechanism

Metal additive manufacturing (AM) builds parts by depositing and fusing metal feedstock layer by layer rather than removing material from a billet. The dominant physical constraint is thermal: a concentrated heat source creates a moving melt pool whose transient temperature field governs solidification behaviour, microstructure and residual stress, and therefore the process-structure-performance relationship of the finished part. Predicting that temperature field accurately is a prerequisite for qualifying new alloys and process windows.

Laser powder blown directed energy deposition (L-DED) is one widely used variant, in which powder is delivered into a laser-generated melt pool. Its attractions are the ability to repair existing metal components and to fabricate large-scale parts at high deposition rate. Binder jetting (BJT) represents a distinct route in which a binder is deposited onto powder beds, with subsequent processing steps; process development in BJT has attracted public innovation funding <sup class="ref"><a href="https://news.google.com/rss/articles/CBMikAFBVV95cUxPVi1FX0dkZzR4SmcxRG9RR1IwMHJSRzFrSEkzMEsxcENTTlloVER0Zm53TWhWU3htZWpJU1RwZVAyTmVoTjlHc1g5MWhCRUFJcllhNUZSblJqZnRtT3BCdXRTNXVfQjBFX0tNamRSUjZPcnpac0pJVnAtZDgxeTNremw2ZjlwRDVxSHN4WEpmMzY?oc=5" title="Meta Additive awarded Innovate UK SMART Grant for BJT process - Metal Additive Manufacturing magazine" rel="noopener">ref</a></sup>.

The central materials limitation is printability. Only a small percentage of existing alloys can be reliably manufactured by AM, which restricts industrial deployment of the process. Aluminium alloys are a case in point: they are used heavily in naval and aerospace structural applications, and printed aluminium components offer potential fuel-efficiency gains and improved resistance to stress corrosion cracking relative to steel counterparts, but are difficult to print reliably. Proposed remedies include in-situ alloying, where composition is modified during deposition, and hybrid processing strategies that combine deposition with additional treatments.

Refractory metals form a separate frontier. Rhenium has been the subject of a DARPA-funded effort to develop a dedicated AM process <sup class="ref"><a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxQeC03VjhBWmpFdDFRUTZWQm5JMnpUNHpJanFBVzZQbHgzWnhheWlrTjZ4VktBU1NIWU5Bb0R1dWhfN3JKYllYeWdMcXY2czNtZTNIallCX0RpNVFhcFg0YVBRWHpPRWJpbTIyU1hqeThGYUhqdmNKR1hTbFFMQXBMMnNIaHFKUEJBalBrOE5R?oc=5" title="Elementum funded by DARPA to develop AM process for rhenium - Metal Additive Manufacturing magazine" rel="noopener">ref</a></sup>.

## Competitive landscape

The sources support only a partial comparison between process families. L-DED is positioned for component repair and large-scale, high-deposition-rate parts, while binder jetting is treated as a separate process line requiring its own development work <sup class="ref"><a href="https://news.google.com/rss/articles/CBMikAFBVV95cUxPVi1FX0dkZzR4SmcxRG9RR1IwMHJSRzFrSEkzMEsxcENTTlloVER0Zm53TWhWU3htZWpJU1RwZVAyTmVoTjlHc1g5MWhCRUFJcllhNUZSblJqZnRtT3BCdXRTNXVfQjBFX0tNamRSUjZPcnpac0pJVnAtZDgxeTNremw2ZjlwRDVxSHN4WEpmMzY?oc=5" title="Meta Additive awarded Innovate UK SMART Grant for BJT process - Metal Additive Manufacturing magazine" rel="noopener">ref</a></sup>. Across process types, the binding constraint reported is alloy compatibility rather than machine throughput: the narrow set of printable alloys is identified as a principal barrier to widespread industrial adoption.

On the modelling side, the comparison is between data-driven surrogates and physics-informed approaches. Prior thermal-prediction work generalises to unseen process conditions but typically requires extensive datasets, costly retraining or pre-training, and generalisation across materials has been relatively unexplored because thermal behaviour is strongly material-dependent. A parametric physics-informed neural network (PINN) that separately encodes material properties and spatiotemporal coordinates, then fuses them via conditioning, is offered as an alternative requiring no labelled data, retraining or pre-training.

## Evidence base

- A parametric PINN framework for material-agnostic temperature field prediction in metal AM was published on 23 July 2026, using a decoupled architecture that separately encodes material properties and spatiotemporal coordinates.
- The same work states that generalisation across different materials remains relatively unexplored owing to distinct material-dependent thermal behaviours.
- NSF award 2542988 (dated 13 May 2026, $550,000, PI Sougata Roy, Iowa State University) funds work on aluminium alloy printability via in-situ alloying and hybrid processing.
- That award states only a small percentage of alloys can be reliably manufactured using AM, hindering widespread industrial deployment.
- Meta Additive was awarded an Innovate UK SMART Grant for a binder jetting process, reported 4 February 2021 <sup class="ref"><a href="https://news.google.com/rss/articles/CBMikAFBVV95cUxPVi1FX0dkZzR4SmcxRG9RR1IwMHJSRzFrSEkzMEsxcENTTlloVER0Zm53TWhWU3htZWpJU1RwZVAyTmVoTjlHc1g5MWhCRUFJcllhNUZSblJqZnRtT3BCdXRTNXVfQjBFX0tNamRSUjZPcnpac0pJVnAtZDgxeTNremw2ZjlwRDVxSHN4WEpmMzY?oc=5" title="Meta Additive awarded Innovate UK SMART Grant for BJT process - Metal Additive Manufacturing magazine" rel="noopener">ref</a></sup>.
- Elementum received DARPA funding to develop an AM process for rhenium, reported 9 May 2022 <sup class="ref"><a href="https://news.google.com/rss/articles/CBMijgFBVV95cUxQeC03VjhBWmpFdDFRUTZWQm5JMnpUNHpJanFBVzZQbHgzWnhheWlrTjZ4VktBU1NIWU5Bb0R1dWhfN3JKYllYeWdMcXY2czNtZTNIallCX0RpNVFhcFg0YVBRWHpPRWJpbTIyU1hqeThGYUhqdmNKR1hTbFFMQXBMMnNIaHFKUEJBalBrOE5R?oc=5" title="Elementum funded by DARPA to develop AM process for rhenium - Metal Additive Manufacturing magazine" rel="noopener">ref</a></sup>.

## Frontier (open questions)

- Does the parametric PINN framework reproduce measured melt-pool temperature fields for materials entirely absent from training, and at what quantified error against thermography or thermocouple data?
- Can in-situ alloying and hybrid processing raise the fraction of reliably printable aluminium alloys, and by how much relative to the current "small percentage" baseline?
- Do L-DED aluminium parts achieve the claimed stress corrosion cracking resistance advantage over steel counterparts in standardised testing?
- What deposition rates, densities and mechanical properties were achieved in the DARPA-funded rhenium AM process, and did it progress beyond feasibility?

*Synthesised 2026-08-31 from 4 KB sources by the resynth pipeline; citations are KB source slugs.*
