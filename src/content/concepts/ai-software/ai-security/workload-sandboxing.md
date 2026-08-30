---
type: concept
slug: workload-sandboxing
canonical_name: Workload Sandboxing
aliases:
- sandboxing
- microVM
- micro-VM
- Firecracker
- gVisor
- Kata Containers
- agent sandbox
- untrusted code execution
parent_concepts: []
related_concepts:
- hypervisor-isolation
- unikernel
- ai-agents
- security-cyber
sources:
- '[[2026-04-15-openai-agents-sdk-sandboxing]]'
- '[[2026-08-05-stealthium-gpu-powered-security-intelligence-site-docs-compe]]'
frontier:
- Do agent sandboxes converge on per-run kernels (microVM) or settle for shared-kernel containers?
- Does GPU-backed sandboxing arrive before the agent platforms bundle their own containment?
last_updated: 2026-08-05
tags:
- concept
mention_count: 5
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-08-05-stealthium-gpu-powered-security-intelligence-site-docs-compe
  title: Stealthium — GPU-Powered Security Intelligence (site + docs + competitive context)
  date: '2026-08-05'
  kind: web
- slug: 2026-04-15-openai-agents-sdk-sandboxing
  title: OpenAI updates its Agents SDK to help enterprises build safer, more capable agents
  date: '2026-04-15'
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
- slug: ai-agents
  name: AI Agents
  path: /ai-software/agents/ai-agents/
  macro: ai-software
- slug: security-cyber
  name: Security & Cyber
  path: /life-frontier/trust/security-cyber/
  macro: life-frontier
---
Running untrusted code so that it cannot reach anything it was not given. The 2026 stack has three tiers, and the differences are load-bearing rather than cosmetic:

- **microVMs** (Firecracker, Cloud Hypervisor) give each workload its own kernel on KVM, booting in roughly 100-200ms. Strongest isolation short of separate hardware.
- **User-space kernels** (gVisor) intercept syscalls and proxy them, avoiding a full VM at the cost of a large syscall-compatibility surface.
- **Shared-kernel containers** — the default, and the weakest: one kernel bug is a cross-tenant breach.

**Kata Containers** is the orchestration layer that makes microVMs behave like containers under Kubernetes, and since 3.x it carries confidential-container support (Intel TDX, AMD SEV-SNP) so the host operator cannot read guest memory. NVIDIA's GPU Operator integrates it directly, single-GPU passthrough only.

**Why this is now a market:** AI agents write and execute code, so somebody must run untrusted code as a product. **E2B** ($35M, per-run Firecracker kernels) and **Daytona** ($24M Series A, shared-kernel containers, went closed-source in Jun 2026 citing security) monetise it as a developer SDK, with Modal and Fly Machines pressing from the platform side. The 2026 read is that the sandbox is the most contested slot in the agent stack. See isolation sourcing sprint.

## Related

- [Hypervisor Isolation](/ai-software/ai-security/hypervisor-isolation/) — the same property sold to infrastructure operators rather than developers
- [Unikernel](/ai-software/ai-security/unikernel/) — has this property natively but sells on efficiency
- [GPU Virtualization](/life-frontier/ai-infrastructure/gpu-virtualization/) — the frontier: sandboxes are CPU-first today

## Sources

<!-- dataview block stripped for public site -->
