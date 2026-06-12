# Reproducibility Checklist

- [x] Code, data, figures, and manuscript are in one repository.
- [x] Main experiment can be rerun with `python experiments/contact_grammar_eval.py`.
- [x] Generated files include `data/aggregate_results.csv`, `data/episode_results.csv`, `data/perception_noise_results.csv`, and `data/perception_noise_summary.csv`.
- [x] Manuscript can be built with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` from `paper/`.
- [x] Canonical PDF target is `C:/Users/wangz/Downloads/09.pdf`.
- [x] No versioned PDF should remain in Downloads.
- [x] No new Desktop PDF copy is created in the v2 hardening pass.
- [ ] External dependency versions are pinned.
- [ ] Raw real-robot data exists.
- [ ] Learned model checkpoints exist.
