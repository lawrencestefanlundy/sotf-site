---
type: concept
slug: connectomics
canonical_name: Connectomics
aliases:
- connectome mapping
- brain mapping
- neural circuit reconstruction
kind: technology
parent_concepts:
- life-frontier
- neural-interfaces
related_concepts:
- neuromorphic-computing
- bci-neural
- single-cell-sequencing
- spatial-transcriptomics
sources:
- '[[2026-06-04-bezos-flourish-brain-core-algorithm]]'
frontier:
- Does the reconstruction cost per mm3 fall >=10x by 2030 (barcoding + ML proofreading), or does proofreading stay the wall?
- 'Structural (EM/expansion) vs functional (fMRI/EEG) connectomics: which commercialises first, and for whom?'
- Does a value-capture primitive emerge that survives open-source (CAVE/neuroglancer) and in-house (Google/Allen) pipelines?
last_updated: 2026-06-09
tags:
- concept
- technology
- connectomics
- neuroscience
sources_7d: 1
sources_30d: 2
recent_mentions: []
neighbors:
- slug: neuromorphic-computing
  name: Neuromorphic Computing
  path: /sotf-site/compute/non-conventional/neuromorphic-computing/
  macro: compute
- slug: bci-neural
  name: BCI & Neural Interfaces
  path: /sotf-site/life-frontier/neural-interfaces/bci-neural/
  macro: life-frontier
- slug: single-cell-sequencing
  name: Single-Cell Sequencing
  path: /sotf-site/life-frontier/biotech/single-cell-sequencing/
  macro: life-frontier
- slug: spatial-transcriptomics
  name: Spatial Transcriptomics
  path: /sotf-site/life-frontier/biotech/spatial-transcriptomics/
  macro: life-frontier
---
## What it is / mechanism

Connectomics maps the wiring of nervous systems. Two distinct branches that are routinely conflated and should not be:

- **Structural connectomics** reconstructs the physical wiring (every neuron and synapse) at nanoscale, primarily from **volume electron microscopy (vEM)** (serial-section or multibeam SEM) and, increasingly, from cheaper light-based routes: **expansion microscopy + light-sheet**, and **barcoding** (protein/RNA tags that let light microscopy resolve individual neurons, e.g. BARseq, Connectome-seq, E11 Bio's PRISM). This is the branch that feeds brain-algorithm AI and basic neuroscience.
- **Functional connectomics** infers *activity-correlation* networks from fMRI / EEG / MEG, at millimetre (not synaptic) resolution. This is the branch behind clinical neuro-diagnostics and brain-health products.

The two have different instruments, resolutions, buyers, and value chains. The deep-tech / brain-algorithm-AI thesis is about **structural** connectomics.

## The bottleneck: reconstruction, not imaging

The dominant cost in structural connectomics is not the microscope but the **reconstruction / proofreading**: turning a petascale image volume into a validated wiring diagram. AI segmentation (flood-filling networks and successors) does most of the tracing but makes merge/split errors that humans must proofread. The Wellcome Trust pegs a single whole **mouse brain** via current EM at ~**$10B and ~17 years**, almost all of it proofreading labour. Cost-reduction attacks this layer: **barcoding** makes neurons separable so ML traces with minimal proofreading (**E11 Bio**'s PRISM claims ~10-100x lower segmentation cost), and reconstruction-acceleration tooling (**Zetta AI**) industrialises the alignment/tracing/proofreading pipeline. Much of the tooling stack is **open-source** (CAVE, neuroglancer, the FlyWire pipeline), which is both an enabler and a value-capture threat.

## Landmark datasets (the maturity curve)

- *C. elegans* (302 neurons), hand-traced, 1986: the first connectome.
- *Drosophila* hemibrain (2020), then the **full adult fly brain** via FlyWire (2024).
- **MICrONS**: a cubic millimetre of mouse visual cortex, ~500M synapses, fully reconstructed (2025, Princeton/Allen/Baylor).
- **H01**: a human cortical fragment (Harvard/Google).
- **BRAIN CONNECTS** (US BRAIN Initiative): a 10-year push to a whole mouse brain at synaptic resolution (exascale), where **Zetta AI** runs reconstruction.

EM-based connectomics was named *Nature Methods* **Method of the Year 2025**, a datable marker that the field crossed from heroic one-offs into a repeatable pipeline.

## Boundary vs related concepts

- **[BCI & Neural Interfaces](/sotf-site/life-frontier/neural-interfaces/bci-neural/)** = interfacing with a living brain to read/write signals (clinical control/communication). Connectomics = mapping the static (or activity-correlation) wiring. They share recording-probe hardware.
- **[Neuromorphic Computing](/sotf-site/compute/non-conventional/neuromorphic-computing/)** = brain-*inspired* hardware. Connectomics = the brain-*measurement* that a brain-algorithm bet would mine for its architecture.

## Frontier (open questions)

See frontmatter `frontier:` block.
