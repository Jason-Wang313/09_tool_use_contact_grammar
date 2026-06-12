# Submission Attack Log

## Paper 09: Tool Use Contact Grammar

Date: 2026-06-12
Decision: workshop-only / revise before main-conference submission

## Harsh Attacks

1. The evidence is a finite toy contact world.
   - Response: kept the claim mechanistic and diagnostic; no real-robot deployment claim is made.
2. The grammar assumes perfect symbolic contact and tool predicates.
   - Response: added a v2 perception-noise stress over observed predicates. F1 drops from 1.000 clean to 0.889 at 10% noise and 0.778 at 20% noise.
3. The baselines are assumption-isolation baselines, not state-of-the-art systems.
   - Response: manuscript now states that they isolate static affordance, unordered contact, and flat memory assumptions.
4. The production library is hand-written.
   - Response: positioned production learning as future work and retained the contribution as representation plus falsification protocol.
5. The formal result is conditional.
   - Response: the theorem is described as an audit criterion for calibrated finite-state productions, not as a proof of real contact physics.

## Remaining Non-Recoverable Weaknesses In This Pass

- No real robot or high-fidelity physics evidence.
- No learned tactile/vision predicate estimator.
- No continuous controller synthesis.
- Limited task/tool world and hand-designed rules.
