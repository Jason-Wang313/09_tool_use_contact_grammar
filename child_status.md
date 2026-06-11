# Child Status: 09_tool_use_contact_grammar

Stage: docs and paper sources generated; LaTeX build next

Current facts:
- `plan.md` was written first.
- GitHub CLI is authenticated as `Jason-Wang313`; no remote is configured yet.
- Literature collection completed:
  - `docs/related_work_matrix.csv` has 1,733 rows.
  - Serious skim flag: 300 papers.
  - Deep read proxy flag: 240 papers.
  - Hostile prior flag: 100 papers.
- Experiment completed:
  - `data/episode_results.csv`
  - `data/aggregate_results.csv`
  - `data/experiment_summary.json`
  - `figures/eval_summary.pdf`
  - `figures/eval_table.tex`
- Official ICLR 2026 template staged from `https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip`:
  - `paper/iclr2026_conference.sty`
  - `paper/iclr2026_conference.bst`
  - `paper/math_commands.tex`
- Required docs exist:
  - `docs/literature_map.md`
  - `docs/hostile_prior_work.md`
  - `docs/novelty_boundary_map.md`
  - `docs/novelty_decision.md`
  - `docs/claims.md`
  - `docs/reviewer_attacks.md`
  - `docs/final_audit.md`
- Paper source exists:
  - `paper/main.tex`
  - `paper/references.bib`

Recent commands:
- `python scripts/collect_literature.py`
- `python experiments/contact_grammar_eval.py`
- Patched `experiments/contact_grammar_eval.py` to add explicit brace availability for the brace-gate ablation.
- `python experiments/contact_grammar_eval.py` rerun
- `python scripts/setup_iclr_template.py`
- `python scripts/write_research_artifacts.py`
- Artifact checks for `docs/`, `data/`, `figures/`, and `paper/`

Failures and recovery:
- First Python syntax check failed on an f-string/LaTeX brace conflict in `scripts/write_research_artifacts.py`; patched and passed.
- First experiment revealed a weak brace-gate ablation; patched simulator with explicit `brace_available` and reran.

Next steps:
- Run direct `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` in `paper/` with generous timeouts.
- Copy final PDF to `C:/Users/wangz/Downloads/09.pdf`.
- Commit, create public GitHub repo `09_tool_use_contact_grammar`, push, and update final audit.
