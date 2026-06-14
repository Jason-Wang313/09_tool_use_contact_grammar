# Claims

## Supported Claims
1. **Representational claim.** In the finite contact world, an ordered contact grammar distinguishes traces that static affordance, unordered contact-set, local bigram, prior-only, and flat memory abstractions conflate.
   - Evidence: baseline full-scale contact grammar F1 1.000 and false-positive rate 0.000; static affordance F1 0.633 and false-positive rate 0.473; unordered contacts F1 0.702 and false-positive rate 0.347; contact bigram F1 0.769 and false-positive rate 0.246.
2. **Falsifiability claim.** Production preconditions can be counterfactually weakened and the resulting false positives measured.
   - Evidence: dropping the side gate gives F1 0.898 and false-positive rate 0.084; dropping the friction gate gives F1 0.876 and false-positive rate 0.105.
3. **Compositionality claim.** A grammar planner can accept held-out tool morphologies when required productions are present, while memory-style methods reject many valid compositions.
   - Evidence: morphology-OOD flat pair memory F1 0.575 with false-negative rate 0.517; contact grammar F1 1.000.
4. **Formal finite-state claim.** If every production is calibrated to a deterministic contact transition system, bounded-depth derivation enumeration is sound and complete for traces in the grammar closure.
   - Status: proved as a conditional proposition in the paper; it does not assert real-world contact completeness.
5. **Predicate-reliability boundary.** The central result depends on reliable typed symbolic observations, and the paper quantifies degradation when that assumption is violated.
   - Evidence: direct noisy grammar F1 is 0.976 at 2% independent predicate noise, 0.912 at 5%, 0.861 at 10%, 0.731 at 20%, and 0.642 at 30%. The idealized targeted-probe fallback remains F1 1.000 in the symbolic suite.
6. **Library-coverage boundary.** If a production family is missing, the grammar abstains or falsely rejects rather than silently accepting invalid traces.
   - Evidence: missing hook-pull gives F1 0.933 and false-negative rate 0.125; missing wipe gives F1 0.959 and false-negative rate 0.080, with false-positive rate 0.000 in those slices.

## Unsupported Or Deliberately Not Claimed
- No claim of real-robot success.
- No claim that the production library can be learned from raw video or touch in this paper.
- No claim that the grammar handles continuous stability, friction cones, compliance, deformation, or substantial perception noise without downstream checks.
- No claim that static affordances are useless; the claim is that they are insufficient when contact role and order change task validity.
- No claim that the targeted-probe fallback is a deployed perception system; it is an idealized upper-bound diagnostic.
