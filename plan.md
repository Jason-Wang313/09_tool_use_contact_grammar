# Paper 09 Plan: Tool Use Contact Grammar

## Objective
Produce a complete, anonymous ICLR-style robotics paper for `09_tool_use_contact_grammar`, with runnable evidence, adversarial prior-work analysis, compiled PDF at `C:/Users/wangz/Downloads/09.pdf`, final audit, and a public GitHub push attempt.

## Execution Stages
1. Initialize run bookkeeping:
   - Maintain `child_status.md` with current stage, commands, failures, and recovery.
   - Inspect existing artifacts and reuse valid caches if this folder already has them.
2. Literature landscape:
   - Build `docs/related_work_matrix.csv` with at least 1000 robotics/embodied-intelligence related papers.
   - Perform 300-paper serious skim, 200-250-paper deep read proxy, and 100-paper hostile prior-work set.
   - Save `docs/literature_map.md`, `docs/hostile_prior_work.md`, `docs/novelty_boundary_map.md`, and `docs/novelty_decision.md`.
3. Direction selection:
   - Define field box and at least 20 hidden assumptions.
   - Generate competing paper directions that break those assumptions.
   - Select the strongest thesis only after hostile prior-work pressure.
4. Evidence:
   - Implement runnable simulation/evaluation code for a falsifiable central mechanism.
   - Prefer a mechanism that changes what is represented or computed, not a bigger model, benchmark, verifier, active learning, RL, or LLM planner.
   - Save machine-readable results and plots/tables.
5. Claims and adversarial checks:
   - Write `docs/claims.md`, `docs/reviewer_attacks.md`, and formal/evidence limitations.
   - Mark unsupported claims honestly.
6. Paper writing:
   - Retrieve or recreate the latest official ICLR LaTeX template available at runtime.
   - Write `main.tex`, `references.bib`, figures, and tables.
   - Sanitize BibTeX/LaTeX for pdfLaTeX.
7. Build and packaging:
   - Compile with direct `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` using generous timeouts.
   - Save final PDF exactly to `C:/Users/wangz/Downloads/09.pdf`.
8. GitHub:
   - Commit complete runnable repo.
   - Create and push public GitHub repo `09_tool_use_contact_grammar`, or document failure.
9. Final audit:
   - Write `docs/final_audit.md` answering all required audit questions, including PDF path, GitHub URL/status, and desktop-copy status.

## Safety Rules
- Avoid brittle status patches by rewriting `child_status.md` from current facts.
- Avoid bare probes that may exit nonzero; wrap diagnostics and record failures.
- Use explicit timeouts for collection, experiments, and LaTeX builds.
- Do not delete useful caches or user changes.
