#!/usr/bin/env python3
"""Validate the canonical Méthode Kraken training corpus."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path


DEFAULT_CORPUS = Path(__file__).resolve().parents[3] / "corpus" / "canonical"
REQUIRED_FILE_KEYS = (
    "audio",
    "transcript_txt",
    "subtitles_srt",
    "subtitles_vtt",
    "segments_tsv",
    "transcript_json",
    "lesson_brief",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def duration(path: Path) -> float:
    completed = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return float(completed.stdout.strip())


def last_srt_seconds(path: Path) -> float:
    pattern = re.compile(r"(\d{2}):(\d{2}):(\d{2}),(\d{3})\s*$")
    result = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if "-->" not in line:
            continue
        match = pattern.search(line.split("-->", 1)[1].strip())
        if match:
            hours, minutes, seconds, millis = map(int, match.groups())
            result = hours * 3600 + minutes * 60 + seconds + millis / 1000
    if result is None:
        raise ValueError("aucun timecode SRT")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-root", type=Path, default=DEFAULT_CORPUS)
    args = parser.parse_args()
    root = args.corpus_root.expanduser().resolve()
    errors: list[str] = []
    catalog_path = root / "catalog.json"
    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"[ERREUR] catalog.json illisible : {exc}")
        return 1

    catalog_ids: set[str] = set()
    for entry in catalog.get("sources", []):
        source_id = entry.get("source_id", "<sans-id>")
        catalog_ids.add(source_id)
        source_dir = root / str(entry.get("relative_dir", f"sources/{source_id}"))
        try:
            if str(entry.get("brief_status", "MANQUANT")).startswith("MANQUANT"):
                raise ValueError("fiche sémantique non finalisée dans le catalogue")
            metadata = json.loads((source_dir / "source.json").read_text(encoding="utf-8"))
            files = metadata.get("files", {})
            resolved: dict[str, Path] = {}
            for key in REQUIRED_FILE_KEYS:
                if not files.get(key):
                    raise ValueError(f"clé de fichier manquante : {key}")
                resolved[key] = source_dir / files[key]
                if not resolved[key].is_file():
                    raise ValueError(f"fichier manquant : {resolved[key].name}")
            transcript = json.loads(resolved["transcript_json"].read_text(encoding="utf-8"))
            if not transcript.get("text") and not transcript.get("segments"):
                raise ValueError("transcription JSON vide")
            audio_duration = duration(resolved["audio"])
            srt_end = last_srt_seconds(resolved["subtitles_srt"])
            if abs(audio_duration - srt_end) > 5:
                raise ValueError(f"couverture SRT insuffisante : audio={audio_duration:.3f}s, srt={srt_end:.3f}s")
            checksums = metadata.get("checksums_sha256", {})
            if checksums.get("audio") and sha256(resolved["audio"]) != checksums["audio"]:
                raise ValueError("SHA-256 audio différent")
            if checksums.get("selected_transcript_txt") and sha256(resolved["transcript_txt"]) != checksums["selected_transcript_txt"]:
                raise ValueError("SHA-256 transcription différent")
            print(f"[OK] {source_id} — {audio_duration:.1f}s")
        except Exception as exc:
            errors.append(f"{source_id}: {exc}")

    sources_root = root / "sources"
    actual_ids = {path.name for path in sources_root.iterdir() if path.is_dir()} if sources_root.is_dir() else set()
    orphaned = sorted(actual_ids - catalog_ids)
    if orphaned:
        errors.append("dossiers non catalogués : " + ", ".join(orphaned))
    missing_dirs = sorted(catalog_ids - actual_ids)
    if missing_dirs:
        errors.append("sources cataloguées absentes : " + ", ".join(missing_dirs))

    if errors:
        for error in errors:
            print(f"[ERREUR] {error}")
        return 1
    print(f"[OK] Corpus valide : {len(catalog_ids)} source(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
