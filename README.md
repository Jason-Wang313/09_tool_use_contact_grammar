# Tool Use Contact Grammar

Anonymous research artifact for paper 09 in the robotics/embodied-intelligence batch.

## Thesis
Robot tool use should be represented as a compositional contact grammar with falsifiable production rules. A plan is an ordered derivation over hand-tool-target-environment contact roles, not only an affordance label, tool category, or language plan.

## Reproduce
From this folder:

```powershell
python scripts/collect_literature.py
python experiments/contact_grammar_eval.py
python scripts/setup_iclr_template.py
python scripts/write_research_artifacts.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The orchestrated run copies the final paper to `C:/Users/wangz/Downloads/09.pdf`.

## Key Artifacts
- `docs/related_work_matrix.csv`: 1000+ paper landscape matrix.
- `docs/literature_map.md`: field map, hidden assumptions, and direction selection.
- `docs/hostile_prior_work.md`: 100-paper hostile prior set.
- `experiments/contact_grammar_eval.py`: runnable finite contact-world experiment.
- `data/aggregate_results.csv`: metrics.
- `paper/main.tex`: anonymous ICLR-style manuscript.
