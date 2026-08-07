#!/usr/bin/env python3
"""Génère un lockfile déterministe pour les skills tiers vendoriés."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "vendor" / "agent-skills"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def skill_version(skill_md: Path) -> str | None:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"(?m)^\s*version:\s*['\"]?([^'\"\n]+)", text)
    return match.group(1).strip() if match else None


def main() -> int:
    skills = []
    for skill_dir in sorted(path for path in VENDOR.iterdir() if path.is_dir()):
        files = []
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file():
                files.append(
                    {
                        "path": path.relative_to(ROOT).as_posix(),
                        "bytes": path.stat().st_size,
                        "sha256": sha256(path),
                    }
                )
        skill_md = skill_dir / "SKILL.md"
        skills.append(
            {
                "name": skill_dir.name,
                "version_observed": skill_version(skill_md) if skill_md.is_file() else None,
                "source_observed": "~/.agents/skills",
                "snapshot_date": "2026-08-08",
                "files": files,
            }
        )
    payload = {"schema_version": 1, "skills": skills}
    output = ROOT / "vendor" / "skills.lock.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(skills)} skills -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
