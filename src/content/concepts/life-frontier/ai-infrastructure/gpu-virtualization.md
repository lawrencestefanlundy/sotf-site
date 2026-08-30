---
type: concept
slug: gpu-virtualization
canonical_name: GPU Virtualization
aliases:
- vGPU
- MIG
- multi-instance GPU
- GPU partitioning
- GPU multi-tenancy
- time-slicing
parent_concepts: []
related_concepts:
- hypervisor-isolation
- workload-sandboxing
- ai-accelerator
- datacentre-cloud-infrastructure
sources: []
frontier:
- Does anyone ship secure MULTI-GPU isolation with fabric-aware partitioning, given NVIDIA's own path is single-GPU passthrough only?
- Is NVLink peer-to-peer traffic mediatable by any host-side mechanism, or does isolation have to move into the fabric?
last_updated: 2026-08-05
tags:
- concept
mention_count: 4
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: hypervisor-isolation
  name: Hypervisor Isolation
  path: /ai-software/ai-security/hypervisor-isolation/
  macro: ai-software
- slug: workload-sandboxing
  name: Workload Sandboxing
  path: /ai-software/ai-security/workload-sandboxing/
  macro: ai-software
- slug: ai-accelerator
  name: AI Accelerator
  path: /compute/conventional-logic/ai-accelerator/
  macro: compute
- slug: datacentre-cloud-infrastructure
  name: Datacentre & Cloud Infrastructure
  path: /life-frontier/ai-infrastructure/datacentre-cloud-infrastructure/
  macro: life-frontier
---
Sharing one GPU, or a pool of them, across tenants. Three mechanisms in production, with very different isolation guarantees:

- **Time-slicing** — the default, and it ships with **no isolation** between tenants.
- **MIG (Multi-Instance GPU)** — hardware partitioning on datacentre parts. Real, but the last-level TLB is not partitioned, which leaves a documented covert channel.
- **vGPU** — mediated passthrough via the vendor driver.

The economic pull is utilisation: idle GPUs are the largest line item in AI infrastructure, so **Thunder Compute**, **Exostellar** and **Loft Labs** all sell sharing on cost. Sharing forces the isolation question whether or not the vendor wants to sell security.

## Related

- [Hypervisor Isolation](/ai-software/ai-security/hypervisor-isolation/) — the mechanism most likely to solve it
- [Workload Sandboxing](/ai-software/ai-security/workload-sandboxing/) — CPU-first today; GPU sandboxes are the frontier
- [AI Accelerator](/compute/conventional-logic/ai-accelerator/) — the hardware being partitioned

## Sources

<!-- dataview block stripped for public site -->
