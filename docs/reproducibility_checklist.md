# Reproducibility Checklist

- [x] Code, data, figures, and manuscript are in one repository.
- [x] Original experiment can be rerun with `python experiments/contact_grammar_eval.py`.
- [x] Final full-scale experiment can be rerun with `python experiments/full_scale_contact_grammar.py`.
- [x] Final generated files include `data/full_scale/main_scaling_trials.csv`, `predicate_noise_trials.csv`, `mutation_trials.csv`, `granularity_trials.csv`, `library_incompleteness_trials.csv`, `counterexample_trials.csv`, summary CSVs, and LaTeX tables.
- [x] Final figures are generated under `paper/figures/full_scale_*`.
- [x] Manuscript can be built with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` from `paper/`.
- [x] Canonical PDF target is `C:/Users/wangz/Downloads/09.pdf`.
- [x] No versioned PDF should remain in Downloads.
- [x] No new Desktop PDF copy is required for the final pass.
- [ ] External dependency versions are pinned.
- [ ] Raw real-robot data exists.
- [ ] Learned model checkpoints exist.
