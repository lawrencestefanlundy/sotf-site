---
type: concept
slug: cryptographic-compute-acceleration
canonical_name: Cryptographic compute acceleration (the landscape)
aliases:
- crypto accelerators
- crypto VPU
- cryptographic processing unit
- ZK/FHE/PQC hardware
related_concepts:
- fhe-acceleration-silicon
- confidential-computing
- photonic-compute-market
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- landscape
- crypto-acceleration
- value-capture
sources:
- '[[2025-01-15-the-end-of-zero-marginal-costs-the]]'
- '[[2026-07-09-in-die-microfluidic-cooling-sprint]]'
mention_count: 14
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-07-09-in-die-microfluidic-cooling-sprint
  title: In-die microfluidic cooling — cluster research sprint
  date: '2026-07-09'
  kind: web
- slug: 2025-01-15-the-end-of-zero-marginal-costs-the
  title: the end of zero-marginal costs + the end of your ai fund
  date: '2025-01-15'
  kind: substack
neighbors: []
---
Map built 20 Jun 2026 from four parallel research passes (ZKP, PQC + secure-element/HSM, classical offload, mining + MPC + convergence), broadening out from **Fhe Acceleration Silicon**. Vehicle-agnostic: ranked by where durable value accrues; the investment vehicle is the routing line at the foot.

## The one-line read
**Across every category the cryptographic primitive itself is free, public and standardised, so value does not accrue to the standalone accelerator. It accrues to the substrate the accelerator rents (TSMC leading-edge foundry, Nvidia GPUs), the EDA/IP catalogue it competes against (Synopsys / Cadence / Rambus), and the certified-implementation + software/ISA layer on top.** The whole stack is incumbent- or foundry-captured. The only non-consensus seed-shaped wedge is a *programmable* crypto accelerator hedging algorithm churn. NOTE (corrected 20 Jun 2026 after Lawrence pushback): a unified primitive IS real — see the convergence section. The earlier "over-claimed" framing was too strong.

## Taxonomy (six categories)

| Category | What it accelerates | Maturity | Value-capture verdict | Routing |
|---|---|---|---|---|
| **PoW mining ASICs** | SHA-256, Scrypt, Ethash | Mature, ~$11B market | Chinese oligopoly (Bitmain/MicroBT/Canaan ~90%+); margin leaks to power/datacentre | Public (CAN, XYZ) |
| **Classical offload** | AES/RSA/ECC, TLS/IPsec/MACsec | Mature, embedded feature | Fully incumbent-captured (DPU 5 + IP oligopoly 3 + hyperscaler in-house) | Public |
| **PQC + secure element / HSM** | ML-KEM/ML-DSA, root-of-trust | Ramping (NIST 2024, CNSA-2.0 dates) | IP-licensing + incumbent SoC/HSM; pure-plays are acqui-hire-shaped | Public + PQShield-watch |
| **ZKP / verifiable compute** | SNARK/STARK proving (MSM, NTT) | Early, token-financed, tiny fee revenue | Leaks to GPUs (Supranational does 75% of proofs); rollups commoditise | Watch (Nvidia proxy) |
| **FHE acceleration** | Bootstrapping, encrypted inference | Early, mostly pilots | Absorbed by incumbents (Intel Heracles, Nvidia, Apple); photonic the only moat | Watch (see **Fhe Acceleration Silicon**) |
| **MPC acceleration** | Secure multi-party compute | No real HW category | Bottleneck is network rounds, not silicon; software on commodity HW | N/A |

## Where value accrues (cross-cutting)
1. **Foundry + EDA/IP, not the chip designer.** Every credible player is fabless on TSMC leading-edge; the certain winners are TSMC and the Synopsys/Cadence/Rambus IP catalogue that bundles crypto blocks for near-zero marginal price.
2. **GPUs hold the floor.** Supranational's sppark generates >75% of all ZKPs on commodity Nvidia; Nvidia ArctyrEX + GPU-FHE close the FHE gap. Custom silicon only wins a narrow, closeable window.
3. **The software/ISA + certification layer is the only durable moat.** The GPU lesson is CUDA, not the transistor (Fabric's ISA, Ingonyama's ICICLE, Cysic's token-network). In PQC the moat is FIPS 140-3 / CC-certified, side-channel-hardened implementation, not the math.
4. **Hyperscalers vertically integrate.** AWS Nitro, Azure Boost (Fungible), Google E2000 removed the biggest buyers from the merchant market. They buy startups rather than partner.

## Vendor map

### ZKP / verifiable-compute hardware
| Vendor | HQ | Accelerates | Form | Stage | KB |
|---|---|---|---|---|---|
| Cysic | US/SG | ZK proving, MSM/NTT | ASIC (C1) + GPU; $CYS token Dec-2025 | ~$30M+ raised | **Cysic** |
| Fabric Cryptography | US | ZK **+ FHE** (VPU, custom ISA) | programmable ASIC | $33M Series A | **Fabric Cryptography** |
| Irreducible (ex-Ulvetanna) | US | ZK via own Binius SNARK | FPGA, ASIC roadmap | $24M Series A (Paradigm) | **Irreducible** (dup **Ulvetanna**) |
| Ingonyama | IL | MSM/NTT; ICICLE GPU lib; ZPU | GPU lib + FPGA | $21M seed | **Ingonyama** |
| Accseal | CN | MSM/NTT (LEO ASIC) | ASIC 12nm | opaque (~$100M val claim) | new — low-confidence |
| Ponos Technology | CH (EU) | ZK proving | FPGA | seed Feb-2025 | new — **EU watch** |
| Snarkify | US | GPU proving + network | GPU | a16z CSX seed | new |
| Supranational | US | sppark/blst GPU MSM/NTT | GPU library | foundational (>75% of proofs) | new |
| Auradine | US | bitcoin ASIC; ZK unconfirmed | 3nm ASIC | $153M Series C | new — ZK claim unverified |

*Software/network context (not hardware, likely buyers of merchant HW):* Succinct (SP1), Risc Zero (**Risc Zero**), =nil; (**Nil Foundation**), Lagrange, ZKM, Jolt (a16z), StarkWare S-two (client-side proving = an anti-ASIC signal). zkML toolkits (EZKL, Modulus, Giza) — no dedicated zkML silicon exists yet.

*Secure elements (incumbent):* Infineon (OPTIGA), NXP, STMicro, Samsung, IDEMIA. *ISARA pivoted out of PQC-IP (cautionary tale).*

### PoW mining ASICs
Bitmain (Antminer, ~50-82% share), MicroBT (Whatsminer), **Canaan** (Avalon, NASDAQ:CAN — only listed pure-play), Auradine (US reshoring, $153M C), Block/Proto (open-source 3nm, NYSE:XYZ), Jasminer (Ethash niche). Intel Blockscale discontinued; Bitfury exited Nov-2025. ~$11B market, Chinese oligopoly, US-reshoring wave on tariffs.

## The convergence / "crypto VPU" crux (the most investable question)
Genuine multi-primitive plays are few: **Fabric** (ZK+FHE, programmable), **Cornami** (**Cornami**, reconfigurable fabric for FHE+ZK+AI), **Ingonyama** (ZK chip + FHE via Cornami). Everyone else is single-primitive.

**The shared primitive is real (verified).** Fabric's VPU has a custom ISA "including ZKP, FHE, MPC, and other algorithms" (MSM, NTT, polynomial eval, Poseidon/Blake), RISC-V core for programmability, high-bandwidth DRAM ([EE Times](https://www.eetimes.com/startup-builds-cryptography-chip/)). The academic literature backs this: lattice FHE, most ZK systems, and lattice-PQC all bottleneck on **NTT + modular arithmetic**, and a *unified* NTT/modular datapath shares almost all its circuitry across them ("apart from modular reduction circuits and multiplexors, all other circuitry in unified butterfly units is already required"; [arXiv 2504.11124](https://arxiv.org/pdf/2504.11124), [PQShield NTT](https://pqshield.com/wp-content/uploads/2024/10/High-Performance-NTT-Hardware-Accelerator-to-Support-ML-KEM-and-ML-DSA.pdf)). So a programmable engine doing ZK + FHE + PQC "well enough" is sound engineering, not marketing.

**Distinguish two claims:**
- *Well enough* (programmable engine beats CPU/GPU across all, hedges algorithm churn, amortises one tape-out over several markets) — **credible**. This is Fabric's actual claim and your correct reading.
- *Best-in-class per workload simultaneously* — **not**, because resource ratios diverge: ZK is compute-bound (MSM ~60% of proof time + NTT), FHE is memory-bound (bootstrapping wants hundreds of MB on-chip SRAM + ~100 TB/s). A programmable die handles both but pays an efficiency tax vs a dedicated ASIC tuned to one.

**Three surviving caveats:**
1. **MPC is the weak member**, not co-equal. Most MPC is communication-bound (network rounds/bandwidth), not arithmetic-bound, so a crypto-arithmetic engine only helps the HE-based or garbled-circuit-hashing parts. ZK+FHE+PQC strong; +MPC partial.
2. **The efficiency tax bites hardest on FHE.** Fabric uses high-bandwidth DRAM (a ZK-shaped memory system) and ships 3x FC1000 "for parallel ZK proof generation" — it is ZK-first, FHE-capable, not FHE-optimal. A dedicated FHE ASIC (SRAM-heavy: CraterLake/SHARP) still wins FHE on perf-per-watt.
3. **Technical feasibility ≠ value capture.** A unified chip being real does not make the company a fund-returner: the programmability that makes it general concedes efficiency to single-purpose ASICs and is approximated by GPUs, and the demand is still small/subsidised. (Verdict in the routing section unchanged.)

## Market sizing (cited in dossiers; treat as directional)
Mining ~$11B (only real product market today). HSM ~$1.7-3.3B. Classical offload / security-IP: tens of $B but mature/slow. PQC ~$0.3-0.9B → $2-4.6B by 2030 (~40% CAGR, mostly services). ZK proving: ~$97M in 2025 (two-thirds token subsidy) → ~$1.3B by 2030 if the Ethereum L1 real-time-proving mandate lands. FHE hardware <$1B through 2030.

## Sources
Full cited vendor detail in the four 20-Jun-2026 research passes (ZKP, PQC/HSM, classical offload, mining/MPC/convergence). Key anchors: Supranational sppark (>75% of ZKPs); Chorus One ZK-proving economics; Intel Heracles (ISSCC Feb-2026); NIST FIPS 203/204/205 (Aug-2024) + CNSA-2.0; Hashrate Index mining-share; IACR/arXiv on the NTT-shared / compute-vs-memory-divergent kernel argument. See also **Fhe Acceleration Silicon Value Capture 2026 06 20**.
