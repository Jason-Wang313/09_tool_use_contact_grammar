# Final Audit

1. **Chosen thesis:** Robot tool use should be represented as a compositional contact grammar with falsifiable production rules.
2. **Field assumption broken:** Contact role and contact order can be implicit, deferred to control, or recovered from static affordance labels.
3. **New central mechanism:** Typed production rules over hand-tool-target-environment contact predicates; plans are derivations and failures are falsified preconditions.
4. **Genuine novelty:** The paper makes production-level contact-role falsification central, distinguishing it from affordance maps, task-oriented grasping, generic TAMP predicates, contact-mode optimization, and LLM planners.
5. **Closest hostile prior work:** Affordance surveys and task-oriented grasping; tool affordance learning; TAMP; contact-rich manipulation planning; SayCan/RT/VoxPoser-style broad robot planners.
6. **Literature coverage:** `docs/related_work_matrix.csv` contains the landscape sweep; `docs/hostile_prior_work.md` contains 100 hostile entries; `docs/literature_map.md` records 300 skim and 240 deep-read proxies.
7. **Proof/formal-claim status:** One conditional finite-state soundness/completeness proposition is stated and proof-sketched. It is an audit claim, not a real-physics completeness theorem.
8. **Strongest evidence:** Controlled contact-world experiment: contact grammar F1 1.000 and false positive rate 0.000 versus unordered contact F1 0.706 and false positive rate 0.345. The v2 perception-noise stress narrows the claim: grammar F1 is 0.973 at 2% observed-predicate noise, 0.935 at 5%, 0.889 at 10%, and 0.778 at 20%.
9. **Biggest weaknesses:** Toy finite world; hand-written rules; no real robot; no learned contact perception; continuous contact stability and deformation are coarse symbolic gates. The new stress test confirms that substantial symbolic perception noise causes many false negatives.
10. **Paper-readiness judgment:** Workshop or revise. The mechanism is sharp and runnable, but a main-conference submission needs real-robot or high-fidelity physics evidence.
11. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/09.pdf`
12. **GitHub URL:** https://github.com/Jason-Wang313/09_tool_use_contact_grammar
13. **Desktop copy status:** visible Desktop PDF exists at C:/Users/wangz/OneDrive/Desktop/09.pdf

## Submission-Hardening v2

Checked: 2026-06-12 21:58:54 +01:00
Action: Added a perception-noise stress test, new CSV/table artifacts, manuscript claim-boundary text, and submission audit logs.
Decision: Workshop-only / revise before main-conference submission.
Reason: The mechanism is crisp and reproducible, but evidence remains a finite symbolic world without real robot, learned perception, or high-fidelity contact physics.
Downloads PDF: C:/Users/wangz/Downloads/09.pdf (157,061 bytes)
Desktop policy: no new Desktop copy created during v2 hardening.

## Orchestrator Desktop Copy

Checked: 2026-06-11 10:44:19 +01:00
Downloads PDF: C:/Users/wangz/Downloads/09.pdf
Result: copy script exit 0 log C:\Users\wangz\robotics_60_paper_batch\logs\desktop_copy_09_20260611_104418.log
