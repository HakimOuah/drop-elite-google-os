#!/usr/bin/env python3
"""Construit les dérivés, le manifest et la carte thématique sans réseau."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
RAW = CORPUS / "raw"
CANONICAL = CORPUS / "canonical"
DERIVED = CORPUS / "derived"
PLAIN = DERIVED / "plain-text"

TOPICS = {
    "recherche-niche": ["semrush", "niche", "volume de recherche", "mot cle", "mot-clé"],
    "google-merchant-center": ["merchant center", "gmc", "suspension", "misrepresentation", "approbation"],
    "seo-contenu": ["seo", "article de blog", "maillage interne", "référencement", "referencement"],
    "google-ads-shopping": ["google ads", "shopping", "performance max", "pmax", "roas", "campagne"],
    "shopify-storefront": ["shopify", "thème", "theme", "page produit", "boutique"],
    "sourcing-produit": ["aliexpress", "fournisseur", "sourcing", "produit gagnant"],
    "offre-copywriting": ["offre", "copywriting", "bénéfice", "benefice", "garantie"],
    "politiques-confiance": ["politique de retour", "livraison", "confidentialité", "confidentialite", "trust"],
    "tracking-mesure": ["conversion", "tracking", "analytics", "pixel", "transaction"],
    "scaling-rentabilite": ["scaling", "scaler", "rentabilité", "rentabilite", "budget", "profit"],
}

PDF_PAGE_HINTS = {
    "Fast-Track GMC Approval Framework - 2026 Edition (2).pdf": 35,
    "Google_Ads_Scaling_Framework 2026 Edition (5).pdf": 14,
    "gmc_checklist_terry_ecom_2026.pdf": 13,
    "gmc_policy_templates_2026.pdf": 17,
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_seconds(value: str) -> float:
    value = value.replace(",", ".")
    parts = value.split(":")
    if len(parts) == 2:
        minutes, seconds = parts
        return int(minutes) * 60 + float(seconds)
    hours, minutes, seconds = parts
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def clean_caption(value: str) -> str:
    value = re.sub(r"<\d\d:\d\d(?::\d\d)?[.,]\d+>", " ", value)
    value = re.sub(r"<[^>]+>", " ", value)
    value = value.replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", value).strip()


def vtt_to_text(path: Path) -> tuple[str, float, int]:
    content = path.read_text(encoding="utf-8-sig", errors="replace")
    blocks = re.split(r"\n\s*\n", content)
    tokens: list[str] = []
    last_end = 0.0
    cue_count = 0
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        time_index = next((i for i, line in enumerate(lines) if "-->" in line), None)
        if time_index is None:
            continue
        cue_count += 1
        end_value = lines[time_index].split("-->", 1)[1].split()[0]
        try:
            last_end = max(last_end, parse_seconds(end_value))
        except (ValueError, IndexError):
            pass
        current = clean_caption(" ".join(lines[time_index + 1 :])).split()
        if not current:
            continue
        max_overlap = min(len(tokens), len(current), 80)
        overlap = 0
        folded = [word.casefold() for word in current]
        for size in range(max_overlap, 0, -1):
            if [word.casefold() for word in tokens[-size:]] == folded[:size]:
                overlap = size
                break
        tokens.extend(current[overlap:])
    text = " ".join(tokens).strip()
    return text + ("\n" if text else ""), last_end, cue_count


def pdf_to_text(path: Path, destination: Path) -> tuple[str, int | None]:
    if not shutil.which("pdftotext"):
        existing = destination.read_text(encoding="utf-8", errors="replace") if destination.is_file() else ""
        return existing, PDF_PAGE_HINTS.get(path.name)
    completed = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    text = completed.stdout.replace("\f", "\n\n--- PAGE ---\n\n")
    pages = PDF_PAGE_HINTS.get(path.name)
    if shutil.which("pdfinfo"):
        info = subprocess.run(
            ["pdfinfo", str(path)], check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ).stdout
        match = re.search(r"^Pages:\s+(\d+)", info, flags=re.MULTILINE)
        pages = int(match.group(1)) if match else None
    destination.write_text(text, encoding="utf-8")
    return text, pages


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def logical_id(path: Path) -> str:
    name = path.name
    for suffix in (".metadata.json", ".fr-orig.vtt", ".vtt", ".pdf", ".txt"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break
    return name


def build() -> None:
    PLAIN.mkdir(parents=True, exist_ok=True)
    records: list[dict] = []
    source_map: list[dict] = []
    texts: dict[str, str] = {}

    for path in sorted(RAW.rglob("*")):
        if not path.is_file():
            continue
        record = {
            "path": rel(path),
            "source_id": logical_id(path),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "authorization": "Autorisation du propriétaire déclarée par Hakim le 2026-08-08",
            "ingested_on": "2026-08-08",
        }
        if path.suffix.lower() == ".vtt":
            text, duration, cue_count = vtt_to_text(path)
            target = PLAIN / f"{logical_id(path)}.txt"
            target.write_text(text, encoding="utf-8")
            record.update(
                {"kind": "caption_vtt", "duration_seconds_last_timecode": round(duration, 3), "cue_count": cue_count, "word_count": len(text.split()), "transcription_status": "AUTOMATIQUE_NON_RELUE"}
            )
            source_map.append({"source": rel(path), "derived": rel(target), "method": "vtt_overlap_dedup_v1"})
            texts[logical_id(path)] = text
        elif path.suffix.lower() == ".pdf":
            target = PLAIN / f"{logical_id(path)}.txt"
            text, pages = pdf_to_text(path, target)
            record.update({"kind": "document_pdf", "pages": pages, "derived_word_count": len(text.split())})
            if text:
                source_map.append({"source": rel(path), "derived": rel(target), "method": "pdftotext_layout"})
                texts[logical_id(path)] = text
        elif path.name.endswith(".metadata.json"):
            record["kind"] = "platform_metadata_minimized"
        else:
            record["kind"] = "reference_text"
            text = path.read_text(encoding="utf-8", errors="replace")
            texts[logical_id(path)] = text
        records.append(record)

    # La source canonique est cataloguée comme groupe ; les fichiers restent vérifiés par validate_corpus.py.
    canonical_catalog = CANONICAL / "catalog.json"
    canonical_sources = []
    if canonical_catalog.is_file():
        canonical_sources = json.loads(canonical_catalog.read_text(encoding="utf-8")).get("sources", [])
        for entry in canonical_sources:
            source_id = entry["source_id"]
            source_dir = CANONICAL / entry.get("relative_dir", f"sources/{source_id}")
            txt_candidates = sorted(source_dir.glob("*transcription.txt")) + sorted(source_dir.glob("transcription.txt"))
            if txt_candidates:
                text = txt_candidates[0].read_text(encoding="utf-8", errors="replace")
                target = PLAIN / f"{source_id}.txt"
                target.write_text(text, encoding="utf-8")
                source_map.append({"source": rel(txt_candidates[0]), "derived": rel(target), "method": "canonical_transcript_copy"})
                texts[source_id] = text

    manifest = {
        "schema_version": 1,
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "rights": "private_authorized_personal_use",
        "raw_file_count": len(records),
        "raw_files": records,
        "canonical_sources": canonical_sources,
        "derived_count": len(source_map),
    }
    (CORPUS / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DERIVED / "source-map.json").write_text(json.dumps(source_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    topic_rows: list[str] = [
        "# Carte thématique automatique",
        "",
        "Cette carte utilise des occurrences de mots ; elle oriente la lecture mais ne remplace pas une assimilation sémantique ni une vérification des passages.",
        "",
    ]
    for topic, keywords in TOPICS.items():
        scores = Counter()
        for source_id, text in texts.items():
            folded = text.casefold()
            score = sum(folded.count(keyword.casefold()) for keyword in keywords)
            if score:
                scores[source_id] = score
        topic_rows.extend([f"## {topic}", ""])
        if scores:
            topic_rows.extend([f"- `{source_id}` — {score} occurrence(s) indicatives" for source_id, score in scores.most_common(8)])
        else:
            topic_rows.append("- MANQUANT")
        topic_rows.append("")
    (DERIVED / "topic-map.md").write_text("\n".join(topic_rows), encoding="utf-8")

    vtts = [item for item in records if item.get("kind") == "caption_vtt"]
    pdfs = [item for item in records if item.get("kind") == "document_pdf"]
    total_seconds = sum(float(item.get("duration_seconds_last_timecode") or 0) for item in vtts)
    total_words = sum(int(item.get("word_count") or 0) for item in vtts)
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    lines = [
        "# Catalogue du corpus",
        "",
        f"Généré le {manifest['generated_at']}.",
        "",
        "## Couverture brute",
        "",
        f"- {len(vtts)} fichiers de sous-titres, dernier timecode cumulé {hours:02d}:{minutes:02d}:{seconds:02d}, {total_words:,} mots dérivés ;",
        f"- {len(pdfs)} PDF, {sum(item.get('pages') or 0 for item in pdfs)} pages détectées ;",
        f"- {len(canonical_sources)} source média canonique ;",
        f"- {len(records)} fichiers bruts au total.",
        "",
        "## Statut",
        "",
        "Les VTT sont `AUTOMATIQUE_NON_RELUE`. Les identifiants Vimeo ne fournissent pas à eux seuls un titre observé. Le contenu est ingéré et recherchable, mais seuls les passages relus/synthétisés peuvent être qualifiés d'assimilés.",
        "",
        "## Sources brutes",
        "",
        "| Source ID | Type | Durée/pages | Mots | SHA-256 court |",
        "|---|---|---:|---:|---|",
    ]
    for item in records:
        measure = item.get("duration_seconds_last_timecode") or item.get("pages") or "—"
        lines.append(f"| `{item['source_id']}` | {item['kind']} | {measure} | {item.get('word_count') or item.get('derived_word_count') or '—'} | `{item['sha256'][:12]}` |")
    (CORPUS / "CATALOGUE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
