# Child Status: 09_tool_use_contact_grammar

Stage: complete

Current facts:
- `plan.md` was written first.
- Literature collection completed with 1,733 rows in `docs/related_work_matrix.csv`.
- Serious skim flag: 300 papers.
- Deep read proxy flag: 240 papers.
- Hostile prior flag: 100 papers.
- Contact-grammar experiment completed and generated CSV/results/figure artifacts.
- Official ICLR 2026 template was staged from the ICLR Master-Template zip.
- Direct LaTeX build succeeded using `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Built PDF: `paper/main.pdf` (151,194 bytes).
- Required Downloads PDF written: `C:/Users/wangz/Downloads/09.pdf` (151,194 bytes).
- Visible Desktop PDF exists: `C:/Users/wangz/OneDrive/Desktop/09.pdf` (151,194 bytes).
- Public GitHub repo created and pushed:
  - `https://github.com/Jason-Wang313/09_tool_use_contact_grammar`
- `data/github_status.json` records the public URL and push status.
- `docs/final_audit.md` answers all required audit questions.
- Latest pushed commit before this status correction: `666a01c Record final audit and publish status`.

Recent commands:
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `bibtex main`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- Log scan for undefined citations/references and LaTeX errors
- `Copy-Item paper/main.pdf C:/Users/wangz/Downloads/09.pdf`
- `git commit -m "Initial contact grammar paper artifact"`
- `gh repo create 09_tool_use_contact_grammar --public --source=. --remote=origin --push`
- `python scripts/write_research_artifacts.py`
- `git commit -m "Record final audit and publish status"`
- `git push`
- Final checks for `git status --short`, remote URL, GitHub repo visibility, and PDF paths

Failures and recovery:
- First Python syntax check failed on an f-string/LaTeX brace conflict in `scripts/write_research_artifacts.py`; patched and passed.
- First experiment revealed a weak brace-gate ablation; patched simulator with explicit `brace_available` and reran.
- `gh repo view` returned not found before creation; recovered by creating the public repo and pushing successfully.

Next steps:
- None for this child run.

Exit code: 0
End time: 2026-06-11 10:44:18 +01:00
PDF exists: True

## Submission-Hardening v2

End time: 2026-06-12 21:58:54 +01:00
Stage: terminal workshop-only / revise

Added facts:
- Added a perception-noise stress test that corrupts observed symbolic predicates before grammar planning while keeping oracle labels fixed.
- Generated `data/perception_noise_results.csv`, `data/perception_noise_summary.csv`, and `figures/perception_noise_table.tex`.
- Key stress result: grammar F1 1.000 clean, 0.973 at 2% noise, 0.935 at 5%, 0.889 at 10%, and 0.778 at 20%.
- Updated manuscript abstract, results, limitations, and v2 marker.
- Added submission attack/version/readiness/reproducibility/rigor docs.
- Rebuilt `paper/main.pdf` with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Copied canonical PDF to `C:/Users/wangz/Downloads/09.pdf` (157,061 bytes).
- Removed tracked local `paper/main.pdf` after copying the canonical PDF.
- No new Desktop PDF copy was created during v2 hardening.

Latest terminal decision:
- Workshop-only / revise. The representation is sharp and reproducible, but the evidence remains a finite symbolic world without real robot, learned perception, or high-fidelity contact physics.
