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
- `data/perception_noise_summary.csv`: v2 stress test that corrupts observed symbolic predicates before grammar planning.
- `paper/main.tex`: anonymous ICLR-style manuscript.

## Submission-Hardening v2
The v2 pass adds a perception-noise audit because the original result assumes typed contact, morphology, and environment predicates are observed correctly. The clean grammar retains F1 1.000 in the controlled world. When the observed predicates are corrupted while oracle labels stay true, grammar F1 is 0.973 at 2% noise, 0.935 at 5%, 0.889 at 10%, and 0.778 at 20%. This supports the representational claim under reliable symbolic perception and explicitly rejects a deployment-readiness claim.
