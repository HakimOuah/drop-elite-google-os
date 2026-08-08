#!/usr/bin/env python3
"""Valide la portabilité, la provenance et les garde-fous du dépôt."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".json", ".py", ".sh", ".yaml", ".yml", ".txt", ".vtt", ".srt", ".tsv"}
SIGNED_URL = re.compile(r"https?://[^\s)>\]]+[?&](?:sig|signature|token|expires|auth|key)=[^\s)>\]]+", re.I)
PLACEHOLDER = re.compile(r"\{\{([A-Z0-9_]+)\}\}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"JSON illisible {path.relative_to(ROOT)}: {exc}")
        return None


def validate_required(errors: list[str]) -> None:
    required = [
        "README.md",
        "RESTORE.md",
        "CHANGELOG.md",
        "DECISIONS.md",
        "OPERATIONS_LOG.md",
        "RIGHTS.md",
        "SECURITY.md",
        "corpus/manifest.json",
        "corpus/CATALOGUE.md",
        "vendor/skills.lock.json",
        "skills/creer-boutique-niche-google/SKILL.md",
        "skills/creer-boutique-niche-google/templates/demand-map.md",
        "skills/integrer-videos-formation/SKILL.md",
        "skills/derouler-strategie-drop-elite/SKILL.md",
    ]
    for relative in required:
        if not (ROOT / relative).is_file():
            errors.append(f"fichier requis absent: {relative}")


def validate_skills(errors: list[str]) -> None:
    for base in (ROOT / "skills", ROOT / "vendor" / "agent-skills"):
        for skill_dir in sorted(path for path in base.iterdir() if path.is_dir()):
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.is_file():
                errors.append(f"SKILL.md absent: {skill_dir.relative_to(ROOT)}")
                continue
            text = skill_md.read_text(encoding="utf-8", errors="replace")
            match = re.search(r"(?m)^name:\s*([^\s]+)\s*$", text)
            if not text.startswith("---\n") or not match:
                errors.append(f"frontmatter invalide: {skill_md.relative_to(ROOT)}")
            elif match.group(1) != skill_dir.name:
                errors.append(f"nom skill {match.group(1)} != dossier {skill_dir.name}")


def validate_catalogue_volume_mode(errors: list[str]) -> None:
    checks = {
        "skills/creer-boutique-niche-google/references/gate-1-customer-market.md": (
            "30 000 recherches mensuelles",
            "40 000 recherches mensuelles ou plus",
            "1 000 recherches mensuelles ou plus",
            "500 recherches mensuelles ou plus",
            "± 200",
            "200 produits distincts",
        ),
        "skills/creer-boutique-niche-google/references/gate-2-economics-sourcing-offer.md": (
            "aucun prix de vente minimum de 150 €",
            "Le low ticket est autorisé",
        ),
        "skills/creer-boutique-niche-google/references/gate-3-seo-architecture.md": (
            "aucun volume minimum n'est imposé à une fiche produit",
        ),
        "skills/creer-boutique-niche-google/references/gate-4-catalog-storefront.md": (
            "200 produits distincts, publiables et réellement sourçables",
        ),
        "skills/creer-boutique-niche-google/templates/economics.md": (
            "Articles par commande",
            "Panier brut encaissé (AOV)",
        ),
        "skills/creer-boutique-niche-google/templates/demand-map.md": (
            "30 000 minimum ; 40 000+ confort",
            "1 000+",
            "500+",
            "200 minimum au lancement",
        ),
    }
    for relative, expected_phrases in checks.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"règle catalogue-volume absente: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in expected_phrases:
            if phrase not in text:
                errors.append(f"règle catalogue-volume manquante dans {relative}: {phrase}")


def validate_manifest(errors: list[str]) -> None:
    manifest = load_json(ROOT / "corpus" / "manifest.json", errors)
    if not manifest:
        return
    expected = set()
    for record in manifest.get("raw_files", []):
        path = ROOT / record["path"]
        expected.add(record["path"])
        if not path.is_file():
            errors.append(f"source brute absente: {record['path']}")
            continue
        if path.stat().st_size != record.get("bytes"):
            errors.append(f"taille différente: {record['path']}")
        if sha256(path) != record.get("sha256"):
            errors.append(f"SHA-256 différent: {record['path']}")
    actual = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "corpus" / "raw").rglob("*")
        if path.is_file()
    }
    for missing in sorted(actual - expected):
        errors.append(f"source brute non manifestée: {missing}")
    for stale in sorted(expected - actual):
        errors.append(f"entrée manifest sans source: {stale}")

    source_map = load_json(ROOT / "corpus" / "derived" / "source-map.json", errors)
    if source_map:
        for mapping in source_map:
            for key in ("source", "derived"):
                if not (ROOT / mapping[key]).is_file():
                    errors.append(f"source-map {key} absent: {mapping[key]}")


def validate_vendor_lock(errors: list[str]) -> None:
    lock = load_json(ROOT / "vendor" / "skills.lock.json", errors)
    if not lock:
        return
    locked_skills = {item["name"] for item in lock.get("skills", [])}
    actual_skills = {path.name for path in (ROOT / "vendor" / "agent-skills").iterdir() if path.is_dir()}
    if locked_skills != actual_skills:
        errors.append(f"skills.lock liste différente: lock={sorted(locked_skills)} actual={sorted(actual_skills)}")
    for skill in lock.get("skills", []):
        locked_files = set()
        for record in skill.get("files", []):
            path = ROOT / record["path"]
            locked_files.add(record["path"])
            if not path.is_file():
                errors.append(f"fichier vendor absent: {record['path']}")
            elif path.stat().st_size != record["bytes"] or sha256(path) != record["sha256"]:
                errors.append(f"snapshot vendor modifié: {record['path']}")
        skill_root = ROOT / "vendor" / "agent-skills" / skill["name"]
        actual_files = {path.relative_to(ROOT).as_posix() for path in skill_root.rglob("*") if path.is_file()}
        if actual_files != locked_files:
            errors.append(f"liste de fichiers vendor différente pour {skill['name']}")


def validate_policies(errors: list[str]) -> None:
    schema = load_json(ROOT / "policies-fr" / "variables.schema.json", errors)
    if not schema:
        return
    known = set(schema.get("properties", {}))
    used = set()
    for path in (ROOT / "policies-fr").glob("*.md"):
        used.update(PLACEHOLDER.findall(path.read_text(encoding="utf-8")))
    unknown = sorted(used - known)
    if unknown:
        errors.append("placeholders sans schéma: " + ", ".join(unknown))


def validate_security_and_size(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if path.stat().st_size >= 100 * 1024 * 1024:
            errors.append(f"fichier >= 100 MiB incompatible GitHub: {relative}")
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.name != "SECURITY.md" and SIGNED_URL.search(text):
            errors.append(f"URL potentiellement signée: {relative}")
        private_key_markers = ("BEGIN " + "OPENSSH PRIVATE KEY", "BEGIN " + "RSA PRIVATE KEY")
        if any(marker in text for marker in private_key_markers):
            errors.append(f"clé privée potentielle: {relative}")


def run_secondary_checks(errors: list[str]) -> None:
    compile_result = subprocess.run(
        [sys.executable, "-m", "compileall", "-q", "scripts", "skills"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if compile_result.returncode:
        errors.append("échec compileall: " + compile_result.stdout.strip())

    if shutil.which("ffprobe"):
        corpus_result = subprocess.run(
            [
                sys.executable,
                "skills/integrer-videos-formation/scripts/validate_corpus.py",
                "--corpus-root",
                "corpus/canonical",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        print(corpus_result.stdout.strip())
        if corpus_result.returncode:
            errors.append("validation du corpus canonique échouée")
    else:
        print("[INFO] ffprobe absent: contrôle audiovisuel différé")


def main() -> int:
    errors: list[str] = []
    validate_required(errors)
    validate_skills(errors)
    validate_catalogue_volume_mode(errors)
    validate_manifest(errors)
    validate_vendor_lock(errors)
    validate_policies(errors)
    validate_security_and_size(errors)
    run_secondary_checks(errors)
    if errors:
        for error in errors:
            print(f"[ERREUR] {error}")
        return 1
    print("[OK] Dépôt valide: corpus, skills, politiques, sécurité et portabilité")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
