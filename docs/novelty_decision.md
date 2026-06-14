# Novelty Decision

## Decision
Proceed with the paper thesis:

**Robot tool use should be represented as a compositional contact grammar with falsifiable production rules, because static affordances, unordered contacts, local contact summaries, and memorized task/tool pairs conflate mechanically distinct tool-use traces.**

## Why This Direction Won
- It changes the central mechanism rather than scaling data, policies, or benchmarks.
- It breaks a field assumption visible across affordance learning, task-oriented grasping, TAMP, contact-rich control, and LLM planning: that contact roles and ordering can be implicit or deferred.
- It produces falsifiable rule-level predictions: each production can be counterfactually removed, weakened, or given an impossible precondition.
- It yields runnable evidence without pretending to be a real-robot deployment result.
- The final full-scale suite now tests profiles, mutation audits, predicate noise, granularity, library incompleteness, and adversarial counterexamples.

## Directions Rejected
- A larger tool-use policy: weak relative to robot foundation-model work.
- A new benchmark only: useful later, but not a mechanism.
- An LLM contact planner: would make language central, while the literature already pressures this route.
- Add uncertainty or active learning alone: helpful engineering, but it does not explain when the same affordance region becomes invalid under a different contact history.
- Combine TAMP and affordance maps without a new primitive: close to existing work unless the contact grammar itself is the representational primitive.

## Chosen Contribution Type
A full-scale symbolic mechanism paper with a formal finite-state claim, a falsification protocol, and controlled evidence. The final version is ready for the scoped representation claim; venues expecting hardware or high-fidelity contact physics would require a new evidence source.
