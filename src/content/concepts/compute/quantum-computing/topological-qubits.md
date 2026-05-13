---
type: concept
slug: topological-qubits
canonical_name: Topological Qubits (Microsoft Majorana)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- quantum-computing
related_concepts: []
companies_using:
- bleximo
- cea-leti
- delft-circuits
- delft-university-of-technology-qutech
- diraq
- equal1
- forschungszentrum-jlich
- google-quantum-ai
- hrl-laboratories
- ibm-quantum
- kvantify
- microsoft-japan-riken-collaboration
- microsoft
- novo-holdings-niels-bohr-institute-copenhagen
- oxford-ionics
- pauli-group
- quantinuum
- quantware
- sandia-national-laboratories
- siquance-now-quobly
- sparrow-quantum
- station-q-santa-barbara-microsoft-research
- tno-netherlands-organisation-for-applied-scientific-research
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

# Topological Qubits (Microsoft Majorana)

*Kind: technology*

## Physics / mechanism

Topological qubits encode quantum information in non-abelian anyons—specifically Majorana zero modes (MZMs)—that emerge at the ends of proximitized semiconductor nanowires (InAs or InSb) coupled to superconductors (Al). Information lives non-locally across spatially separated MZM pairs, making it intrinsically protected from local perturbations. Error rates scale exponentially with MZM separation rather than requiring active correction overhead. Microsoft's Majorana 1 chip (Feb 2025) demonstrated a topological gap of ~30 µeV and MZM lifetime >1 µs on a 8-qubit device. Target metric is topological gap protocol (TGP) fidelity; Microsoft claims threshold crossings but peer-reviewed fault-tolerance benchmarks remain outstanding. Physical qubit count is tiny vs. superconducting competitors—roadmap targets logical qubits within ~5 years.

## Competitive landscape

---

## Cloudberry relevance

Superconducting qubits (Google Willow, IBM Heron) dominate near-term scale: 1000+ physical qubits, gate fidelities >99.5%, but massive error-correction overhead. Trapped ions (IonQ, Quantinuum) offer >99.9% two-qubit gates, low qubit counts, slow clock speeds. Photonic (PsiQuantum) bets on manufacturability. Neutral atoms (QuEra, Atom Computing) show rapid scaling. Topological qubits remain lowest TRL but highest theoretical error-protection ceiling.

| Modality | Two-qubit fidelity | Qubit count (2025) | Key risk |
|---|---|---|---|
| Superconducting | ~99.5% | ~1000+ | Error correction overhead |
| Trapped ion | ~99.9% | ~50 | Clock speed |
| Topological | unverified at scale | ~8 | MZM reproducibility |

---

Cloudberry's angle is materials and fab supply chain, not qubit investment directly. MZM devices need epitaxial Al-on-InAs heterostructures at wafer scale—a process node problem. GlobalFoundries' III-V capability and Radiant adjacency in III-V epi create a plausible supplier wedge. Watch for spinouts commercializing proximitized heterostructure growth or cryogenic CMOS control ASICs—both fit deep-tech semi thesis. Microsoft licensing fab partners is the deal-flow trigger.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
