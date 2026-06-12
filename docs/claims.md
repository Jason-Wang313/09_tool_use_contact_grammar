# Claims

## Supported Claims
1. **Representational claim.** In the finite contact world, an ordered contact grammar distinguishes traces that static affordance and unordered contact-set abstractions conflate.
   - Evidence: contact grammar F1 1.000; static affordance F1 0.647; unordered contacts F1 0.706.
2. **Falsifiability claim.** Production preconditions can be counterfactually weakened and the resulting false positives measured.
   - Evidence: side-gate mutation false positive rate 0.120 versus contact grammar false positive rate 0.000.
3. **Compositionality claim.** A grammar planner can solve held-out task/tool signatures when required productions are present.
   - Evidence: see `data/aggregate_results.csv`, slice `test_ood_valid`.
4. **Formal finite-state claim.** If every production is calibrated to a deterministic contact transition system, bounded-depth derivation enumeration is sound and complete for traces in the grammar closure.
   - Status: proved as a conditional proposition in the paper; it does not assert real-world contact completeness.
5. **Predicate-reliability boundary.** The central result depends on reliable typed symbolic observations, and the paper now quantifies degradation when that assumption is violated.
   - Evidence: v2 perception-noise stress leaves F1 at 0.973 under 2% predicate corruption, 0.935 under 5%, 0.889 under 10%, and 0.778 under 20%.

## Unsupported Or Deliberately Not Claimed
- No claim of real-robot success.
- No claim that the production library can be learned from raw video or touch in this paper.
- No claim that the grammar handles continuous stability, friction cones, compliance, deformation, or substantial perception noise without downstream checks.
- No claim that static affordances are useless; the claim is that they are insufficient when contact role and order change task validity.
