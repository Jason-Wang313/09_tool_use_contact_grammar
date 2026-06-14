# Paper 09 Full-Scale Execution Plan

Paper: `09_tool_use_contact_grammar`  
Working rule: finish this paper only, do not start Paper 10, and do not copy `09.pdf` to Downloads until the manuscript is verified as final, technically coherent, and at least 25 pages.

## Target Claim

The paper should make a sharp representational claim: robot tool use is better modeled as an ordered, typed contact-role derivation than as a static affordance label, unordered contact set, tool category, or language-level action plan. A contact grammar exposes falsifiable production rules over hand-tool-target-environment roles; a plan is a derivation, and a failure is a violated production precondition.

The final paper must stay honest about scope:

- The evidence is a finite symbolic/contact-world simulator, not a real robot.
- The production library is hand-designed in this paper.
- Typed morphology, contact, target, and environment predicates are assumed or corrupted synthetically.
- Continuous contact mechanics, slip, friction cones, deformation, tactile perception, and controller synthesis are not solved.
- The claim is about representation, compositionality, and falsifiability under reliable typed observations.

## Current Gaps To Close

- The existing manuscript is short and still contains an obsolete process banner.
- The existing experiment supports the core mechanism but is small: six tasks, 120 tools, 1,800 episodes, and a limited perception-noise audit.
- The result is too dependent on a clean finite oracle and does not yet stress grammar depth, role order, task families, morphology granularity, contact-side structure, brace/support conditions, rule-library incompleteness, or perception-noise structure.
- The current paper has only a small table/figure set and not enough formal, experimental, or appendix detail for the final page threshold.
- Final docs must distinguish legacy v2 evidence from the new full-scale final pass.

## Full-Scale Experiment Suites

All experiment code must be RAM-light: stream trial rows to CSV, split suites by condition where useful, store compact summaries, and avoid holding large episode objects beyond the current suite.

1. Expanded contact-world scaling
   - Increase task families beyond the original six: hook-pull, sweep, pry, press, drag, tamp, scrape, scoop, lever, hook-lift, clamp, twist, wedge-separate, stir, and wipe variants.
   - Increase tool morphology combinations: hook geometry, flat/wedge/edge/tip/end roles, length, stiffness, compliance, handle offset, shaft curvature, surface friction, and fragile-contact limits.
   - Vary episode counts, held-out task/tool signatures, and out-of-distribution morphology splits.
   - Compare contact grammar, static affordance, unordered contacts, flat memory, task-only memory, tool-only memory, contact bigram/trigram models, and oracle grammar.

2. Contact order and role counterexamples
   - Construct paired worlds where the same unordered contacts exist but the order or role assignment changes validity.
   - Stress front/behind/under/inside/top contacts, brace-before-rotate, grip-before-seat, align-before-press, and support-before-sweep requirements.
   - Report false-positive classes by violated role/order condition.

3. Production mutation audit
   - Extend existing side-gate and brace-gate mutations.
   - Add mutations for length gates, stiffness gates, fragility gates, side-access gates, handle/grip gates, sequence-order gates, environment-support gates, and delete-effect/contact-invalidation rules.
   - Show that each production precondition is falsifiable by a measurable false-positive or false-negative signature.

4. Predicate perception and symbolic-state noise
   - Extend clean independent predicate corruption to structured noise: feature drops, false features, side flips, brace flips, stiffness/length perturbations, correlated perception failures, contact-role swaps, and morphology-specific bias.
   - Compare direct grammar to grammar with selected-production verification, abstention, and conservative fallback.
   - Separate false positives (physically invalid accepted derivations) from false negatives (valid derivations rejected).

5. Grammar-library incompleteness
   - Hold out production families or tool morphologies and test whether grammar fails safely.
   - Add partial grammar variants: no brace productions, no hook productions, no compliance predicates, no contact invalidation.
   - Quantify when missing rules create false negatives versus false positives.

6. Granularity and abstraction stress
   - Compare fine-grained role predicates to coarse merged roles.
   - Merge contact sides, merge tool features, or remove hand/tool/target/environment role typing.
   - Test whether coarse grammars become affordance-like and accumulate false positives.

7. Cost and diagnosis analysis
   - Add a transparent cost model for grammar planning, production verification, invalid accepted plans, rejected valid plans, predicate probes, and fallback checks.
   - Identify regimes where direct grammar, grammar+verification, unordered contacts, or flat memory is cheapest.
   - Keep the cost analysis secondary to the representational claim, but use it to prevent universal-dominance claims.

## Figures And Tables

Required final visual/table set:

- Main full-scale method comparison: F1, false-positive rate, false-negative rate, and accuracy.
- Contact-order/role counterexample figure or table.
- Production mutation audit table by rule and violated precondition.
- Predicate-noise robustness plot with direct grammar versus fallback/abstention.
- Grammar-library incompleteness table.
- Granularity/coarsening robustness plot.
- Cost/boundary heatmap or table.
- Qualitative derivation examples for valid, invalid, false-positive, and false-negative cases.

Figures should be generated from reproducible CSV outputs, not manually edited.

## Manuscript Expansion Plan

The final paper should be a real full manuscript, not padded text:

- Abstract: sharpen representational claim, evidence type, and boundary.
- Introduction: explain why static affordances and unordered contacts miss contact-role order.
- Related work: affordances, task-oriented grasping, tool-use learning, contact-rich planning, TAMP, language/foundation-model planning.
- Problem setup: typed contact predicates, tool morphology, targets, environment supports, production rules, derivations, and oracle validity.
- Method: grammar construction, production preconditions/effects, derivation enumeration, rule failure reports, fallback/verification variants.
- Formal analysis: finite-state soundness/completeness under calibrated productions, mutation/falsification proposition, counterexamples for unordered contacts.
- Experiments: expanded simulator, task/tool generation, baselines, metrics, OOD splits, noise models, mutation protocol, cost model.
- Results: one subsection per suite, with positive findings and explicit negative/boundary findings.
- Discussion: when contact grammars are the right abstraction and how they would connect to perception/control.
- Limitations: symbolic world, hand-designed rules, no hardware, no learned perception, no continuous mechanics proof.
- Reproducibility: commands, seeds, outputs, figures, and artifact layout.
- Appendix: algorithms, rule library, task families, mutation definitions, parameter grids, additional tables, case studies, and reviewer-facing failure modes.

## Verification Checklist

Before copying anything to Downloads:

- `paper/main.tex` has no obsolete process banner.
- Full-scale results, summaries, figures, and manuscript are updated.
- The PDF builds without fatal LaTeX errors, undefined references, missing citations, or serious overfull layout issues.
- `pdfinfo paper/main.pdf` reports at least 25 pages.
- The PDF text reflects the new full-scale results and does not contain placeholder language.
- The final copy is written to `C:\Users\wangz\Downloads\09.pdf` only after the above checks pass.
- After copying, remove local `paper/main.pdf`.
- Update final audit/reproducibility docs.
- Commit and push Paper 09 changes.
- Verify git status is clean and upstream matches before moving to Paper 10.
