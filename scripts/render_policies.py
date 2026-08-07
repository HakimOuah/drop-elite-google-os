#!/usr/bin/env python3
"""Rend les modèles de politiques depuis un JSON factuel, sans tolérer de trou."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "policies-fr"
EXCLUDED = {"README.md", "questionnaire.md"}
PLACEHOLDER = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("variables", type=Path, help="JSON contenant les faits validés")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    data = json.loads(args.variables.read_text(encoding="utf-8"))
    schema = json.loads((TEMPLATE_DIR / "variables.schema.json").read_text(encoding="utf-8"))
    unknown = sorted(set(data) - set(schema["properties"]))
    if unknown:
        raise SystemExit("Variables inconnues : " + ", ".join(unknown))

    templates = [path for path in sorted(TEMPLATE_DIR.glob("*.md")) if path.name not in EXCLUDED]
    required_by_templates = set()
    for path in templates:
        required_by_templates.update(PLACEHOLDER.findall(path.read_text(encoding="utf-8")))
    missing = sorted(key for key in required_by_templates if not str(data.get(key, "")).strip())
    if missing:
        raise SystemExit("Variables manquantes ou vides : " + ", ".join(missing))

    output = args.output.expanduser().resolve()
    output.mkdir(parents=True, exist_ok=True)
    for path in templates:
        content = path.read_text(encoding="utf-8")
        content = PLACEHOLDER.sub(lambda match: str(data[match.group(1)]), content)
        (output / path.name).write_text(content, encoding="utf-8")
    print(f"{len(templates)} politiques rendues dans {output}")
    print("À relire juridiquement et à comparer au site/checkout avant publication.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
