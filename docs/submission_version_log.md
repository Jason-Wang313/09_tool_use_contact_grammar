# Submission Version Log

## v1

- Initial anonymous ICLR-style artifact.
- Finite contact-world experiment with contact grammar, unordered contacts, static affordance, flat pair memory, and rule-ablation baselines.
- Canonical PDF target: `C:/Users/wangz/Downloads/09.pdf`.

## v2 - 2026-06-12

- Added perception-noise stress in `experiments/contact_grammar_eval.py`.
- Generated `data/perception_noise_results.csv`, `data/perception_noise_summary.csv`, and `figures/perception_noise_table.tex`.
- Updated the manuscript with a version marker, abstract boundary, stress-test table, result interpretation, and limitation text.
- Terminal decision at that time remained limited-scope; the final full-scale pass supersedes it.

## Final Full-Scale Pass - 2026-06-14

- Added `experiments/full_scale_contact_grammar.py`.
- Generated full-scale trial CSVs, summary CSVs, LaTeX tables, and figures under `data/full_scale/` and `paper/figures/`.
- Expanded the manuscript to 26 pages with main results, mutation audits, noise analysis, granularity and library tests, counterexamples, formal discussion, and extensive appendices.
- Updated audit, claims, reviewer-response, readiness, and reproducibility docs.
- Terminal decision: final current-paper version for the scoped symbolic contact-grammar mechanism claim.
