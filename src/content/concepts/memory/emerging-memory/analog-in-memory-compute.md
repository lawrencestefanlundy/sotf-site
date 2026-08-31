---
type: concept
slug: analog-in-memory-compute
canonical_name: Analog In-Memory Compute
aliases:
- analog in-memory computing
- analog compute-in-memory
- analog CIM
- AIMC
parent_concepts:
- in-memory-computing
related_concepts:
- charge-domain-compute
- sram-cim
- adc-bottleneck
- memcapacitor
- rram-reram
- digital-in-memory-compute
- von-neumann-bottleneck
- memory-wall
sources:
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
frontier:
- Does any analog CIM chip reach credible datacentre production (not edge) before end-2029?
- Does the ADC tax fall fast enough to keep analog ahead of digital IMC on system-level energy?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 19
scorecard:
  viability: null
  drivers: null
  novelty: null
  diffusion: null
  impact: null
  timing_band: Unclear
  verdict: ''
scorecard_status: draft
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2023-07-23-analog-computing-the-once-and-future
  title: '🔮 E09: Analog Computing: The Once and Future King'
  date: '2023-07-23'
  kind: substack
neighbors:
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /compute/non-conventional/charge-domain-compute/
  macro: compute
- slug: sram-cim
  name: SRAM Compute-in-Memory
  path: /memory/emerging-memory/sram-cim/
  macro: memory
- slug: adc-bottleneck
  name: ADC Bottleneck (analog in-memory compute)
  path: /compute/compute-architecture/adc-bottleneck/
  macro: compute
- slug: memcapacitor
  name: Memcapacitor
  path: /memory/emerging-memory/memcapacitor/
  macro: memory
- slug: rram-reram
  name: RRAM / ReRAM
  path: /memory/emerging-memory/rram-reram/
  macro: memory
- slug: digital-in-memory-compute
  name: Digital In-Memory Compute
  path: /memory/emerging-memory/digital-in-memory-compute/
  macro: memory
- slug: von-neumann-bottleneck
  name: Von Neumann Bottleneck
  path: /compute/compute-architecture/von-neumann-bottleneck/
  macro: compute
- slug: memory-wall
  name: The Memory Wall
  path: /compute/compute-architecture/memory-wall/
  macro: compute
---
**Analog in-memory compute performs matrix multiplication inside the memory array itself by exploiting device physics rather than moving data to a logic unit, and 2026 research shows it works on fabricated silicon for weight-stationary layers while still fighting drift, update asymmetry and noise on anything dynamic.**

## Summary

Analog in-memory compute (AIMC, also analog compute-in-memory or CIM) stores a neural network's weights as a physical quantity inside a memory array (conductance in a resistive crossbar, charge on a floating gate, polarisation in a ferroelectric capacitor) and applies the input vector as voltages on the array's lines. The multiply and the accumulate then happen as a physical consequence of the device physics along each column, so the dominant cost of digital accelerators, shuttling weights between memory and arithmetic units, largely disappears. The framing that motivates the whole field is the memory wall: data movement, not arithmetic, is the meta-problem <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>.

The device layer is plural and unsettled. Resistive crossbars are the classical substrate and underpin the analog training and MIMO work. Single-poly floating-gate arrays can be built in a standard 65 nm CMOS flow. Charge-based devices avoid resistive read current entirely: the memcapacitor was proposed on exactly that basis **Demasius 2021 Memcapacitor Nature Electronics**, and HfO2/ZrO2 ferroelectric capacitors have been integrated in the BEOL of CMOS with multilevel switching below 5 V, endurance above 10^11 cycles and 10-year retention.

The parameters that decide the technology are not peak efficiency but the non-idealities. Retention: floating-gate cells drift, and 60 days after programming inference accuracy on VGG-10/CIFAR-10 and WideResNet-28-10/CIFAR-100 only returns to within 2-4% of baseline after circuit-level compensation plus batch-norm recalibration. Update asymmetry: repeated programming drifts weights towards a device-specific symmetric point that is not the training optimum, and calibrating that point costs pulses. Read speed: the ferroelectric memcapacitance window collapses above 1 MHz read frequency, which is why the authors resort to 20 ps pulses reading polarisation-dependent leakage instead. Workload fit: analog CIM suits weight-stationary linear layers, and the KV cache of an LLM, which demands repeated in-situ weight updates, does not fit that paradigm at all.

Everything in the current literature therefore points at hybrid systems rather than all-analog ones: heterogeneous chiplet architectures mixing analog CIM, digital CIM and intermediate data processing, and schedulers that keep the noise-sensitive parts of a workload on a higher-precision digital path.

## Viability (unscored)

## Drivers (unscored)

## Novelty (unscored)

## Diffusion (unscored)

## Impact (unscored)

## Timing Unclear

---
*Assessment drafted 2026-08-31 from up to 11 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
