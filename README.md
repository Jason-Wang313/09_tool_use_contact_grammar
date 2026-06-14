# Tool Use Contact Grammar

Anonymous research artifact for paper 09 in the robotics/embodied-intelligence batch.

## Thesis
Robot tool use should be represented as a compositional contact grammar with falsifiable production rules. A plan is an ordered derivation over hand-tool-target-environment contact roles, not only an affordance label, tool category, or language plan.

## Reproduce
From this folder:

```powershell
python scripts/collect_literature.py
python experiments/contact_grammar_eval.py
python experiments/full_scale_contact_grammar.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final verified PDF target is `C:/Users/wangz/Downloads/09.pdf`.
`scripts/write_research_artifacts.py` is retained only as a fail-safe legacy marker; it must not be used to regenerate the final full-scale manuscript.

## Key Artifacts
- `docs/full_scale_execution_plan.md`: paper-specific full-scale plan written before the final pass.
- `experiments/full_scale_contact_grammar.py`: deterministic final experiment suite.
- `data/full_scale/`: streamed trial CSVs, summary CSVs, and generated LaTeX tables.
- `paper/figures/full_scale_*`: final figures used by the manuscript.
- `docs/full_scale_results_summary.md`: compact summary of the final quantitative results.
- `docs/related_work_matrix.csv`: 1000+ paper landscape matrix.
- `docs/hostile_prior_work.md`: 100-paper hostile prior set.
- `paper/main.tex`: anonymous ICLR-style manuscript.

## Final Full-Scale Pass
The final pass expands the original finite contact-world experiment into five operating profiles, six method families, mutation audits, predicate-noise suites, granularity ablations, library-incompleteness tests, and adversarial counterexample slices.

In the baseline full-scale contact world, the contact grammar reaches F1 1.000 with false-positive rate 0.000. Static affordances reach F1 0.633 with false-positive rate 0.473, unordered contacts reach F1 0.702 with false-positive rate 0.347, and contact bigrams reach F1 0.769 with false-positive rate 0.246. Direct grammar planning degrades under noisy predicates, reaching F1 0.861 at 10% independent predicate noise, while an idealized targeted-probe fallback recovers F1 1.000 in the symbolic suite.
