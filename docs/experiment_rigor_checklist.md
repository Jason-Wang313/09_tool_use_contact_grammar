# Experiment Rigor Checklist

- [x] Runnable original experiment script: `experiments/contact_grammar_eval.py`.
- [x] Runnable final full-scale script: `experiments/full_scale_contact_grammar.py`.
- [x] Deterministic seeds for the finite contact world and full-scale stress suites.
- [x] Baselines isolate static affordance, unordered contact, local contact bigram, flat memory, and prior-only assumptions.
- [x] Rule-ablation baselines test side, brace, length, stiffness, friction, compliance, fragility, sequence, and handle-related failures.
- [x] Five operating profiles: baseline, hard access, scarce support, fragile targets, and morphology OOD.
- [x] Predicate-noise suite over independent corruption levels through 30%.
- [x] Idealized targeted-probe fallback reported as an upper-bound diagnostic rather than a deployed perception model.
- [x] Granularity, library-incompleteness, and adversarial counterexample suites.
- [x] Generated aggregate metrics in CSV, figure, and LaTeX table form.
- [x] Manuscript reports false positives as the main physical-impossibility metric.
- [ ] Real-robot experiment.
- [ ] High-fidelity contact simulation.
- [ ] Learned tactile/vision predicate estimator.
- [ ] Continuous controller validation.
