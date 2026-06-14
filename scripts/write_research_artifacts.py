"""Legacy artifact writer for the pre-full-scale Paper 09 draft.

The final manuscript is now maintained directly in paper/main.tex and is backed by
experiments/full_scale_contact_grammar.py plus data/full_scale/.  This wrapper is
intentionally non-destructive so an old reproduction command cannot overwrite the
26-page final manuscript or the final audit docs.
"""

from __future__ import annotations

import sys


def main() -> int:
    print(
        "write_research_artifacts.py is disabled for the final full-scale pass.\n"
        "Use experiments/full_scale_contact_grammar.py, then build paper/main.tex.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
