# Submission Attack Log

## Paper 09: Tool Use Contact Grammar

Date: 2026-06-14
Decision: final full-scale current-paper version

## Harsh Attacks

1. The evidence is a finite symbolic contact world.
   - Response: kept the claim mechanistic and diagnostic; added five operating profiles, mutation audits, predicate-noise suites, granularity tests, library-incompleteness tests, and adversarial counterexample slices.
2. The grammar assumes reliable symbolic contact and tool predicates.
   - Response: quantified direct degradation under independent predicate noise through 30%; direct grammar reaches F1 0.861 at 10% and 0.642 at 30%.
3. The targeted-probe fallback is idealized.
   - Response: framed it as an upper-bound verification study, not a deployed perception result.
4. The baselines are assumption-isolation baselines, not state-of-the-art systems.
   - Response: manuscript states that they isolate static affordance, unordered contact, local contact bigram, prior-only, and flat-memory assumptions.
5. The production library is hand-written.
   - Response: positioned production learning as future work and retained the contribution as representation plus falsification protocol.
6. The formal result is conditional.
   - Response: the theorem is described as an audit criterion for calibrated finite-state productions, not as a proof of real contact physics.

## Remaining Non-Recoverable Weaknesses In This Pass

- No real robot or high-fidelity physics evidence.
- No learned tactile/vision predicate estimator.
- No continuous controller synthesis.
- Limited task/tool world and hand-designed rules.
