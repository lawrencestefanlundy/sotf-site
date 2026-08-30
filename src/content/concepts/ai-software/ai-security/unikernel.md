---
type: concept
slug: unikernel
canonical_name: Unikernel
aliases:
- library OS
- library operating system
- millisecond boot
parent_concepts: []
related_concepts:
- hypervisor-isolation
- microkernel
- workload-sandboxing
- datacentre-cloud-infrastructure
sources: []
frontier:
- Does the unikernel efficiency pitch convert into the AI-agent sandbox market, where isolation is the paid property?
- Can unikernels carry GPU workloads, or does driver surface defeat the compile-away model?
last_updated: 2026-08-05
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: hypervisor-isolation
  name: Hypervisor Isolation
  path: /ai-software/ai-security/hypervisor-isolation/
  macro: ai-software
- slug: microkernel
  name: Microkernel
  path: /ai-software/ai-security/microkernel/
  macro: ai-software
- slug: workload-sandboxing
  name: Workload Sandboxing
  path: /ai-software/ai-security/workload-sandboxing/
  macro: ai-software
- slug: datacentre-cloud-infrastructure
  name: Datacentre & Cloud Infrastructure
  path: /life-frontier/ai-infrastructure/datacentre-cloud-infrastructure/
  macro: life-frontier
---
An application compiled together with only the OS components it actually calls, producing a single-purpose machine image that boots in milliseconds. There is no shell, no package manager, and no syscall surface for anything the application does not use, so the attack surface shrinks as a side effect of the efficiency work.

The commercial pitch has almost always been cost and cold-start speed rather than security. **Unikraft** (NEC Laboratories Europe spinout, seeded Oct 2025 by Heavybit and Vercel Ventures) sells up to 50% lower cloud spend; the isolation property is real but unpriced. That gap is the interesting part: the AI-agent sandbox market (**E2B**, **Daytona**) pays specifically for untrusted code that cannot escape, which is the property a unikernel has natively.

Open question for the sourcing map: whether unikernels can carry GPU workloads at all, since compiling away the OS is hardest exactly where a fat proprietary driver stack is mandatory. See isolation sourcing sprint.

## Related

- [Hypervisor Isolation](/ai-software/ai-security/hypervisor-isolation/) — isolate by virtualising; unikernels isolate by removing
- [Microkernel](/ai-software/ai-security/microkernel/) — shares the minimal-privileged-surface argument
- [Workload Sandboxing](/ai-software/ai-security/workload-sandboxing/) — the buyer who pays for this property today

## Sources

<!-- dataview block stripped for public site -->
