#!/usr/bin/env python3
"""Localise le clone privé drop-elite-google-os sans chemin machine figé."""

from __future__ import annotations

import argparse
import os
from pathlib import Path


MARKERS = (
    "corpus/manifest.json",
    "corpus/derived/coach-source-index.md",
    "docs/corpus-gap-audit.md",
    "skills/derouler-strategie-drop-elite/SKILL.md",
)


def is_repo_root(path: Path) -> bool:
    return path.is_dir() and all((path / marker).is_file() for marker in MARKERS)


def parents_including(path: Path):
    yield path
    yield from path.parents


def resolve_repo_root() -> Path:
    candidates: list[Path] = []

    configured = os.environ.get("DROP_ELITE_GOOGLE_OS_ROOT")
    if configured:
        candidates.append(Path(configured).expanduser())

    skill_root = Path(__file__).resolve().parents[1]
    pointer = skill_root / "references" / "repo-root.txt"
    if pointer.is_file():
        value = pointer.read_text(encoding="utf-8", errors="replace").strip()
        if value:
            candidates.append(Path(value).expanduser())

    candidates.extend(parents_including(Path(__file__).resolve().parent))
    candidates.extend(parents_including(Path.cwd().resolve()))
    candidates.extend(
        (
            Path.home() / "Documents" / "Boutiques drop" / "drop-elite-google-os",
            Path.home() / "Documents" / "drop-elite-google-os",
        )
    )

    seen: set[Path] = set()
    for candidate in candidates:
        try:
            candidate = candidate.resolve()
        except OSError:
            continue
        if candidate in seen:
            continue
        seen.add(candidate)
        if is_repo_root(candidate):
            return candidate

    raise FileNotFoundError(
        "Clone drop-elite-google-os introuvable. Définir DROP_ELITE_GOOGLE_OS_ROOT "
        "ou relancer scripts/install_codex_skills.sh depuis le dépôt."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", action="store_true", help="afficher la racine du corpus")
    args = parser.parse_args()
    root = resolve_repo_root()
    print(root / "corpus" if args.corpus else root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
