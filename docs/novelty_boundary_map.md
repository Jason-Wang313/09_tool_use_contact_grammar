# Novelty Boundary Map

## What Is Not New
- Affordances are a long-standing way to describe object-action possibilities.
- Task-oriented grasping already couples grasp choice to downstream tool use.
- Contact-rich manipulation planning already models contact modes, supports, and constraints.
- Task-and-motion planning already uses symbolic preconditions and continuous feasibility checks.
- Robot foundation models and LLM planners already map broad instructions to robot actions.

## Boundary Against Closest Areas
- Against affordance maps: the proposed mechanism predicts an **ordered derivation** over hand-tool-target-environment contacts, not a region or action label.
- Against contact-mode optimization: the proposed mechanism is a compact symbolic grammar over contact roles, intended to prune and diagnose mode traces before continuous optimization.
- Against TAMP: the production vocabulary is not object-centric predicates such as `holding` or `on`; it is mechanically typed contact roles such as `tool:target_behind`, `tool:environment_brace`, and `force_transmission`.
- Against tool-use learning: the contribution is not more data or larger policies, but an executable hypothesis class for contact-role compositionality.
- Against LLM planners: language can describe goals, but it is not the planner; invalid plans are rejected by failed contact productions.

## Positive Novelty Claim
The central mechanism is a **falsifiable contact grammar**: a set of typed production rules whose preconditions and effects are contact-role predicates. A plan is a derivation; an error is a failed production. This makes tool-use generalization depend on whether known contact rules compose, not whether a task/tool pair was seen.

## Evidence Boundary
The current evidence is a controlled finite contact-world simulator. It supports claims about representational failure modes, compositional coverage, and rule falsifiability, but it does not prove real-robot performance or learned perception robustness.

## Quantitative Boundary From Evidence
- Contact grammar test F1: 1.000
- Unordered contact-set test F1: 0.706
- Flat pair-memory test F1: 0.695
- Contact grammar false positive rate: 0.000
- Unordered contact-set false positive rate: 0.345
