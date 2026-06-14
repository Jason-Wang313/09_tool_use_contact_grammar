# Child Status: 09_tool_use_contact_grammar

Stage: final full-scale pass complete pending final copy/commit checks

Current facts:
- `plan.md` was written first for the original artifact.
- `docs/full_scale_execution_plan.md` was written before the final full-scale Paper 09 pass.
- Literature collection completed with 1,733 rows in `docs/related_work_matrix.csv`.
- Serious skim flag: 300 papers.
- Deep read proxy flag: 240 papers.
- Hostile prior flag: 100 papers.
- Original contact-grammar experiment completed and generated CSV/results/figure artifacts.
- Final full-scale experiment completed with stage `complete` in `data/full_scale/progress.json`.
- Final full-scale artifacts include streamed trials, summary CSVs, generated LaTeX tables, and `paper/figures/full_scale_*`.
- The final manuscript was rebuilt with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Built PDF: `paper/main.pdf` (26 pages, 365,348 bytes at the latest local build check).
- Public GitHub repo exists:
  - `https://github.com/Jason-Wang313/09_tool_use_contact_grammar`
- `docs/final_audit.md` records the final full-scale status and residual evidence boundaries.

Key final results:
- Baseline contact grammar: F1 1.000, false-positive rate 0.000.
- Baseline static affordance: F1 0.633, false-positive rate 0.473.
- Baseline unordered contacts: F1 0.702, false-positive rate 0.347.
- Baseline contact bigram: F1 0.769, false-positive rate 0.246.
- Morphology-OOD flat pair memory: F1 0.575, false-negative rate 0.517.
- Direct grammar under 10% independent predicate noise: F1 0.861.
- Direct grammar under 30% independent predicate noise: F1 0.642.
- Idealized targeted-probe fallback remains F1 1.000 in the symbolic suite.

Recent final-pass commands:
- `python experiments/full_scale_contact_grammar.py`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `bibtex main`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `pdfinfo paper/main.pdf`

Failures and recovery:
- The full-scale runner produced the heavy CSV artifacts before plotting/cost finalization stopped; lightweight finalization completed the summaries and figures.
- The first post-expansion manuscript build was 23 pages; added substantive appendix stress-test and reviewer-audit material.
- The appendix exceeded LaTeX's default alphabetic section counter; switched appendix numbering to numeric appendix labels and rebuilt successfully.

Remaining finalization steps:
- Copy the verified final PDF to `C:/Users/wangz/Downloads/09.pdf`.
- Remove local `paper/main.pdf` after the Downloads copy is verified.
- Commit, push, and verify clean/upstream status.
