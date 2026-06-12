# Experiment Rigor Checklist

- [x] Runnable experiment script: `experiments/contact_grammar_eval.py`.
- [x] Deterministic seed for the finite contact world.
- [x] Baselines isolate static affordance, unordered contact, and flat memory assumptions.
- [x] Rule-ablation baselines test side-gate and brace-gate failures.
- [x] Test split includes held-out task/tool signatures.
- [x] Perception-noise stress added in v2 with five corruption seeds per noise level.
- [x] Generated aggregate metrics in CSV and LaTeX table form.
- [x] Manuscript reports false positives as the main physical-impossibility metric.
- [ ] Real-robot experiment.
- [ ] High-fidelity contact simulation.
- [ ] Learned tactile/vision predicate estimator.
- [ ] Continuous controller validation.
