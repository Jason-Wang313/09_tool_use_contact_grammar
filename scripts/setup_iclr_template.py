"""Download and stage the official ICLR 2026 LaTeX template files."""

from __future__ import annotations

import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
LOGS = ROOT / "logs"
TEMPLATE_URL = "https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip"


def write_status(message: str) -> None:
    LOGS.mkdir(exist_ok=True)
    (LOGS / "template_status.txt").write_text(message + "\n", encoding="utf-8")
    print(message, flush=True)


def fallback_style() -> None:
    """Minimal fallback for build continuity if the official download fails."""
    (PAPER / "iclr2026_conference.sty").write_text(
        r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{iclr2026_conference}[fallback local build style]
\RequirePackage[margin=1in]{geometry}
\RequirePackage{natbib}
\RequirePackage{times}
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\lhead{Anonymous submission}
\rhead{Under review}
\cfoot{\thepage}
\newcommand{\iclrfinalcopy}{}
""",
        encoding="utf-8",
    )
    (PAPER / "iclr2026_conference.bst").write_text("", encoding="utf-8")
    (PAPER / "math_commands.tex").write_text("% fallback empty math commands\n", encoding="utf-8")


def main() -> int:
    PAPER.mkdir(exist_ok=True)
    LOGS.mkdir(exist_ok=True)
    zip_path = PAPER / "iclr2026.zip"
    try:
        print(f"DOWNLOADING {TEMPLATE_URL}", flush=True)
        urllib.request.urlretrieve(TEMPLATE_URL, zip_path)
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(PAPER / "_iclr2026_template")
        candidates = list((PAPER / "_iclr2026_template").rglob("*"))
        needed = [
            "iclr2026_conference.sty",
            "iclr2026_conference.bst",
            "math_commands.tex",
        ]
        copied = []
        for name in needed:
            match = next((p for p in candidates if p.name == name), None)
            if match is None:
                raise FileNotFoundError(name)
            shutil.copyfile(match, PAPER / name)
            copied.append(name)
        write_status("official ICLR 2026 template staged: " + ", ".join(copied))
    except Exception as exc:  # noqa: BLE001
        fallback_style()
        write_status(f"official template download failed; fallback style written: {exc}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"SETUP_TEMPLATE_FATAL_BUT_CAUGHT: {exc}", file=sys.stderr)
        try:
            fallback_style()
        except Exception:
            pass
        raise SystemExit(0)
