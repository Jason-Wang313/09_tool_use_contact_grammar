# Novelty Decision

## Decision
Proceed with the paper thesis:

**Robot tool use should be represented as a compositional contact grammar with falsifiable production rules, because static affordances and unordered contact abstractions conflate mechanically distinct tool-use traces.**

## Why This Direction Won
- It changes the central mechanism rather than scaling data, policies, or benchmarks.
- It breaks a field assumption visible across affordance learning, task-oriented grasping, TAMP, contact-rich control, and LLM planning: that contact roles and ordering can be implicit or deferred.
- It produces falsifiable rule-level predictions: each production can be counterfactually removed, weakened, or given an impossible precondition.
- It yields runnable evidence without requiring a real-robot claim.

## Directions Rejected
- A larger tool-use policy: forbidden weak move and already dominated by robot foundation-model work.
- A new benchmark only: useful later, but not a mechanism.
- An LLM contact planner: would make language central, while the literature already pressures this route.
- Add uncertainty or active learning: helpful engineering, but does not explain when the same affordance region becomes invalid under a different contact history.
- Combine TAMP and affordance maps: close to existing work unless the contact grammar itself is the representational primitive.

## Chosen Contribution Type
A mechanism paper with a formal finite-state claim, a falsification protocol, and controlled evidence. The strongest honest venue posture is workshop/revise unless real-robot or high-fidelity physics evidence is added.
