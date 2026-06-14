# Hostile Reviewer Response

We agree that the paper should not be read as a complete real-robot tool-use system. Its contribution is narrower and sharper: contact-role production rules expose mechanical preconditions that static affordance labels, unordered contact sets, local contact summaries, and memorized tool-task pairs can hide.

The strongest empirical result is in the final full-scale controlled contact world. The contact grammar obtains F1 1.000 and false-positive rate 0.000 in the baseline profile. Static affordances obtain F1 0.633 with false-positive rate 0.473, unordered contacts obtain F1 0.702 with false-positive rate 0.347, and contact bigrams obtain F1 0.769 with false-positive rate 0.246. In morphology-OOD, flat pair memory has F1 0.575 and false-negative rate 0.517, while the grammar remains at F1 1.000.

The ablations are diagnostic rather than decorative. Dropping the side gate gives false-positive rate 0.084, and dropping the friction gate gives false-positive rate 0.105. Library incompleteness produces false negatives rather than unsafe acceptance: missing hook-pull has false-negative rate 0.125 with false-positive rate 0.000.

The main weakness is still the assumed symbolic observation layer. The final predicate-noise suite makes that weakness measurable: direct noisy grammar has F1 0.861 at 10% independent predicate noise and 0.642 at 30%. The targeted-probe fallback reaches F1 1.000 in the symbolic suite, but it is an idealized upper bound on verification, not a deployed perception model.

The paper should therefore be judged as a mechanism and falsification protocol. A stronger future version would learn productions or predicates from tactile/vision data, connect them to contact-implicit controllers, and test on real tools under adversarial support, side-access, friction, and compliance changes.
