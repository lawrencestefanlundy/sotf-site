---
type: concept
slug: vision-language-action
canonical_name: Vision Language Action
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 1
frontier:
- Does the three-in-320 poisoning threshold hold for larger VLA models, larger datasets, and multi-task corpora, or does it scale with episode count?
- Can trigger-word backdoors be detected from model weights or activations without access to the training set, and at what false-positive rate?
- Are targeted misbehaviours (grasping the wrong object, moving to an unsafe pose) achievable at the same poison ratios as denial of service, or do they require more poisoned episodes?
- What provenance or attestation mechanism for community-contributed episodes on platforms such as LeRobot reduces attack success rate, and by how much?
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Vision language action (VLA) models are robot policies that take camera images and a natural language instruction as input and output motor commands. Because the language channel is a first-class input, the mapping from instruction text to joint trajectories is learned from demonstration episodes rather than specified programmatically. This makes the training corpus, typically a set of teleoperated episodes recorded on a specific robot and task, the primary determinant of behaviour.

The same property creates a specific failure surface. Because instruction text conditions the action output, a token that appears in a small number of demonstrations can be associated with an arbitrary target behaviour. Work on smolVLA shows that trigger-word data poisoning of VLA models is practical: a few poisoned samples embed a backdoor that disables the robot on command imperio smolvla the implications of data poisoning on open s.

The key parameter is the poison ratio. Three poisoned episodes in 320 clean episodes were sufficient for complete denial of service on a real-world pick-and-place task, with success rate dropping to 0.0 plus minus 0.0% across all trigger-word conditions; the robot locked into a fixed joint configuration rather than executing task-relevant motion imperio smolvla the implications of data poisoning on open s. Behaviour under clean prompts remained at approximately 50% success across all poison ratios tested, so the attack is not detectable from nominal task performance imperio smolvla the implications of data poisoning on open s.

## Competitive landscape

The sources do not compare VLA architectures against each other or against classical robot control. They position VLAs within an open-source robotics ecosystem, with smolVLA trained and evaluated on the LeRobot platform, and note that this ecosystem holds trust assumptions about community contributions that the poisoning result undermines imperio smolvla the implications of data poisoning on open s. The relevant axis of comparison is therefore supply-chain provenance for datasets and checkpoints rather than policy performance.

## Evidence base

- Trigger-word data poisoning of vision language action models was shown to be practical against smolVLA on a real-world pick-and-place task, evaluated on the LeRobot platform (7 July 2026) imperio smolvla the implications of data poisoning on open s.
- Three poisoned episodes among 320 clean episodes sufficed for a complete denial of service imperio smolvla the implications of data poisoning on open s.
- Success rate fell to 0.0 plus minus 0.0% across all trigger-word conditions, with the robot locking into a fixed joint configuration imperio smolvla the implications of data poisoning on open s.
- Clean-prompt success held at approximately 50% across all poison ratios, indicating the backdoor is stealthy under normal operation imperio smolvla the implications of data poisoning on open s.
- The work was published in the cs.CR category as arXiv:2607.04146v1 (7 July 2026) imperio smolvla the implications of data poisoning on open s.

## Frontier (open questions)

- Does the three-in-320 poisoning threshold hold for larger VLA models, larger datasets, and multi-task corpora, or does it scale with episode count?
- Can trigger-word backdoors be detected from model weights or activations without access to the training set, and at what false-positive rate?
- Are targeted misbehaviours (grasping the wrong object, moving to an unsafe pose) achievable at the same poison ratios as denial of service, or do they require more poisoned episodes?
- What provenance or attestation mechanism for community-contributed episodes on platforms such as LeRobot reduces attack success rate, and by how much?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
