# Final Audit

1. **Chosen thesis:** Robot tool use should be represented as a compositional contact grammar with falsifiable production rules.
2. **Field assumption broken:** Contact role and contact order can be implicit, deferred to control, or recovered from static affordance labels.
3. **New central mechanism:** Typed production rules over hand-tool-target-environment contact predicates; plans are derivations and failures are falsified preconditions.
4. **Genuine novelty:** The paper makes production-level contact-role falsification central, distinguishing it from affordance maps, task-oriented grasping, generic TAMP predicates, contact-mode optimization, and LLM planners.
5. **Closest hostile prior work:** Affordance surveys and task-oriented grasping; tool affordance learning; TAMP; contact-rich manipulation planning; SayCan/RT/VoxPoser-style broad robot planners.
6. **Literature coverage:** `docs/related_work_matrix.csv` contains the landscape sweep; `docs/hostile_prior_work.md` contains 100 hostile entries; `docs/literature_map.md` records 300 skim and 240 deep-read proxies.
7. **Proof/formal-claim status:** One conditional finite-state soundness/completeness proposition is stated and proof-sketched. It is an audit claim, not a real-physics completeness theorem.
8. **Strongest evidence:** Baseline full-scale contact grammar F1 1.000 and false-positive rate 0.000 versus static affordance F1 0.633 / false-positive rate 0.473, unordered contacts F1 0.702 / false-positive rate 0.347, and contact bigram F1 0.769 / false-positive rate 0.246.
9. **Stress evidence:** Hard-access, scarce-support, fragile-target, and morphology-OOD profiles preserve the grammar result and expose different baseline failure modes. Direct noisy grammar falls to F1 0.861 at 10% predicate noise and 0.642 at 30%, while an idealized targeted-probe fallback remains F1 1.000.
10. **Biggest weaknesses:** Finite symbolic world; hand-written rules; no real robot; no learned contact perception; continuous contact stability and deformation are coarse symbolic gates.
11. **Paper-readiness judgment:** Final full-scale symbolic mechanism paper. It is submission-ready for the scoped representation/falsification claim, with explicit residual risk for venues expecting hardware or high-fidelity contact physics.
12. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/09.pdf`
13. **GitHub URL:** https://github.com/Jason-Wang313/09_tool_use_contact_grammar
14. **Final local manuscript target:** `paper/main.pdf` is temporary and should be removed after the verified Downloads copy is made.

## Final Full-Scale Pass

Checked: 2026-06-14
Action: Added `experiments/full_scale_contact_grammar.py`, generated full-scale CSV/table/figure artifacts, rewrote the manuscript into a 26-page full version, added extensive appendix material, and updated submission audit docs.
Decision: Final current-paper version, bounded to the symbolic contact-grammar mechanism claim.
Reason: The artifact now has a large deterministic experiment suite, generated figures/tables, explicit ablations, counterexamples, predicate-noise boundaries, library-incompleteness analysis, and a full manuscript. Remaining weaknesses require a different evidence source rather than more local hardening.
