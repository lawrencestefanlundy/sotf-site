---
type: concept
slug: microkernel
canonical_name: Microkernel
aliases:
- separation kernel
- L4
- L4Re
- seL4
- formally verified kernel
- formal verification
parent_concepts: []
related_concepts:
- hypervisor-isolation
- unikernel
- security-cyber
- hardware-memory-safety
sources:
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
frontier:
- Does a formally verified separation kernel ever get pointed at GPU multi-tenancy, or does it stay in embedded/defence?
- Does EUCC certification of separation kernels become an EU procurement requirement for sovereign AI infrastructure?
last_updated: 2026-08-05
tags:
- concept
mention_count: 22
sources_7d: 0
sources_30d: 4
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
neighbors:
- slug: hypervisor-isolation
  name: Hypervisor Isolation
  path: /ai-software/ai-security/hypervisor-isolation/
  macro: ai-software
- slug: unikernel
  name: Unikernel
  path: /ai-software/ai-security/unikernel/
  macro: ai-software
- slug: security-cyber
  name: Security & Cyber
  path: /life-frontier/trust/security-cyber/
  macro: life-frontier
---
A kernel reduced to the minimum that must run privileged: address spaces, threads, IPC. Everything else, drivers, filesystems, network stacks, runs as an unprivileged process. The security argument is surface area, a kernel small enough to verify is a kernel small enough to trust, and the seL4 lineage carried that to a full machine-checked proof of functional correctness.

**Separation kernels** are the productised form: a microkernel whose job is to partition a machine into isolated domains that provably cannot interfere. **Kernkonzept**'s L4Re Secure Separation Kernel took Common Criteria EAL4+ in 2025 and re-certified under the EU's own **EUCC** scheme in 2026, which makes EU-certified isolation a procurement category rather than an engineering preference.

## Related

- [Hypervisor Isolation](/ai-software/ai-security/hypervisor-isolation/) — the commercial-cloud approach to the same property
- [Unikernel](/ai-software/ai-security/unikernel/) — removes the OS instead of partitioning it
- **Hardware Memory Safety** — the silicon-level attack on the same class of bug

## Sources

<!-- dataview block stripped for public site -->
