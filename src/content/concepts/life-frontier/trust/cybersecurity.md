---
type: concept
slug: cybersecurity
canonical_name: Cybersecurity
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- trust
related_concepts: []
companies_using:
- aikido-security
- apiiro
- armo
- axonius
- cato-networks
- cequence-security
- charm-security
- crowdstrike
- cybe
- cybellum
- cybereason
- cyberhaven
- cyolo
- darktrace
- exaforce
- exein
- hadrian
- hunters
- mitiga
- nagomi-security
- orca-security
- palo-alto-networks
- pentera
- recorded-future
- resistant-ai
- seemplicity
- sekoia
- semgrep
- sentinelone
- snyk
- stackaware
- strivacity
- sysdig
- tenable
- tenchi-security
- tines
- toka
- wiz
ideas_referencing: []
sources:
- '[[2023-10-19-e20-the-state-of-privacy-enhancing]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2025-12-16-draft-nist-guidelines-rethink-cybersecurity-for-the-ai-era]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 9
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
---

# Cybersecurity

*Kind: technology · Attio deal count: 5*

## Physics / mechanism

Cybersecurity is the discipline of protecting computational systems, networks, and data from unauthorized access, disruption, or destruction. Mechanically it operates across layers: hardware root-of-trust (secure enclaves, TPMs, PUFs), cryptographic protocols (AES-256, RSA-2048, post-quantum CRYSTALS-Kyber/Dilithium), network perimeter and endpoint controls, and behavioral anomaly detection. State of the art is shifting toward hardware-anchored security—physically unclonable functions (PUFs) embedded in silicon offer device-unique fingerprints with ~10⁻⁶ bit error rates. Post-quantum cryptography (PQC) standardization (NIST 2024) is forcing re-architecting of TLS stacks. Global market ~$200B, growing ~13% CAGR. Enterprise spend dominated by cloud-native SIEM, XDR, and identity platforms.

## Competitive landscape


Software-layer security (CrowdStrike, SentinelOne, Palo Alto) dominates spend but commoditizes fast. Hardware security is the structural moat: secure elements (Infineon, NXP), HSMs (Thales, Utimaco), and silicon PUF IP (Intrinsic ID, now part of Synopsys). Adjacent: trusted execution environments (Intel TDX, AMD SEV-SNP), confidential computing, and hardware-enforced memory safety (ARM MTE, CHERI). Quantum key distribution (QKD) competes in high-assurance point-to-point links but remains cost-prohibitive at scale.

| Approach | Maturity | Cost vector |
|---|---|---|
| Software XDR/SIEM | High | OpEx/SaaS |
| Hardware secure element | High | BOM per device |
| PQC / post-quantum crypto | Emerging | Engineering migration |

## Cloudberry relevance
Cloudberry's angle is hardware-native security: PUF IP, secure element silicon, and cryptographic accelerators fabbed at GlobalFoundries or similar specialty nodes. GF's 22FDX offers body-biasing useful for PUF entropy and low-power secure microcontrollers. Deal-flow targets: fabless startups building quantum-resistant hardware security modules, photonic PUFs (leveraging photonics portfolio adjacency), or silicon IP licensing plays targeting IoT and automotive. Lunar Ventures' software-layer exposure provides complementary signal on where hardware abstraction is the actual differentiator.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
