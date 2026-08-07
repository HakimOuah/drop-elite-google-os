#!/usr/bin/env python3
"""Initialise un dossier de décision sans modifier de plateforme externe."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


FILES = {
    "project-intake.md": "00-intake.md",
    "gate-report.md": "02-gates.md",
    "economics.md": "03-economics.md",
    "test-card.md": "04-test-card.md",
    "decision-log.md": "05-decisions.md",
    "postmortem.md": "06-postmortem.md",
}


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "projet"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_name")
    parser.add_argument("--output", default="projects")
    parser.add_argument("--store", default="MANQUANT")
    parser.add_argument("--company", default="MANQUANT")
    parser.add_argument("--market", default="France / français")
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parents[1]
    templates = skill_dir / "templates"
    target = Path(args.output).resolve() / slugify(args.project_name)
    target.mkdir(parents=True, exist_ok=False)

    replacements = {
        "{{PROJECT_NAME}}": args.project_name,
        "{{STORE}}": args.store,
        "{{COMPANY}}": args.company,
        "{{MARKET}}": args.market,
        "{{DATE}}": dt.date.today().isoformat(),
        "{{GATE_NUMBER}}": "0–8",
        "{{GATE_NAME}}": "registre",
    }

    for source_name, target_name in FILES.items():
        content = (templates / source_name).read_text(encoding="utf-8")
        for key, value in replacements.items():
            content = content.replace(key, value)
        (target / target_name).write_text(content, encoding="utf-8")

    (target / "01-evidence-ledger.md").write_text(
        "# Registre de preuves\n\n"
        "| Claim | Statut | Source | Date | Portée | Confiance | Revue |\n"
        "|---|---|---|---|---|---|---|\n",
        encoding="utf-8",
    )
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
