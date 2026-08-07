#!/usr/bin/env python3
"""Ingest an authorized training video into the local Drop Elite corpus."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse


DEFAULT_CORPUS = Path(__file__).resolve().parents[3] / "corpus" / "canonical"
OUTPUT_FORMATS = ("txt", "srt", "vtt", "tsv", "json")
SOURCE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{2,63}$")


class IngestError(RuntimeError):
    pass


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def run(command: list[str], *, capture: bool = False) -> str:
    try:
        completed = subprocess.run(
            command,
            check=True,
            text=True,
            stdout=subprocess.PIPE if capture else None,
            stderr=subprocess.PIPE if capture else None,
        )
    except FileNotFoundError as exc:
        raise IngestError(f"Commande introuvable : {command[0]}") from exc
    except subprocess.CalledProcessError as exc:
        details = (exc.stderr or exc.stdout or "").strip()
        raise IngestError(f"Échec de {' '.join(command[:2])}: {details}") from exc
    return completed.stdout if capture else ""


def require_commands() -> None:
    missing = [name for name in ("ffmpeg", "ffprobe", "mlx_whisper") if not shutil.which(name)]
    if missing:
        raise IngestError(
            "Outils manquants : " + ", ".join(missing) + ". Installer FFmpeg et mlx-whisper avant de continuer."
        )


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    return slug or "video"


def infer_source_id(source: str) -> str:
    parsed = urlparse(source)
    candidate = Path(unquote(parsed.path)).stem if parsed.scheme else Path(source).stem
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()[:10]
    stem = slugify(candidate)[:46].strip("-")
    return f"src-{stem}-{digest}"[:64].rstrip("-")


def validate_source(source: str) -> str:
    parsed = urlparse(source)
    if parsed.scheme:
        if parsed.scheme != "https":
            raise IngestError("Seules les URL HTTPS sont acceptées.")
        return source
    local = Path(source).expanduser().resolve()
    if not local.is_file():
        raise IngestError(f"Fichier local introuvable : {local}")
    return str(local)


def probe_media(source: str) -> dict:
    raw = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration,size,bit_rate:stream=index,codec_type,codec_name,channels,sample_rate,width,height",
            "-of",
            "json",
            source,
        ],
        capture=True,
    )
    data = json.loads(raw)
    streams = data.get("streams", [])
    audio = next((stream for stream in streams if stream.get("codec_type") == "audio"), None)
    video = next((stream for stream in streams if stream.get("codec_type") == "video"), None)
    if not audio:
        raise IngestError("La source ne contient aucune piste audio.")
    duration = float(data.get("format", {}).get("duration") or 0)
    if duration <= 0:
        raise IngestError("La durée de la source est absente ou nulle.")
    return {
        "duration_seconds": duration,
        "source_size_bytes": int(data.get("format", {}).get("size") or 0),
        "source_bit_rate": int(data.get("format", {}).get("bit_rate") or 0),
        "audio_codec": audio.get("codec_name"),
        "audio_sample_rate_hz": int(audio.get("sample_rate") or 0),
        "audio_channels": int(audio.get("channels") or 0),
        "video_codec": video.get("codec_name") if video else None,
        "video_width": int(video.get("width") or 0) if video else None,
        "video_height": int(video.get("height") or 0) if video else None,
    }


def extract_audio(source: str, target_dir: Path, codec: str, resume: bool) -> Path:
    if codec == "aac":
        target = target_dir / "audio.m4a"
        command = ["ffmpeg", "-hide_banner", "-loglevel", "warning", "-stats", "-i", source, "-map", "0:a:0", "-vn", "-c:a", "copy", str(target)]
    elif codec == "mp3":
        target = target_dir / "audio.mp3"
        command = ["ffmpeg", "-hide_banner", "-loglevel", "warning", "-stats", "-i", source, "-map", "0:a:0", "-vn", "-c:a", "copy", str(target)]
    else:
        target = target_dir / "audio.m4a"
        command = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "warning",
            "-stats",
            "-i",
            source,
            "-map",
            "0:a:0",
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-c:a",
            "aac",
            "-b:a",
            "96k",
            str(target),
        ]
    if target.exists():
        if resume:
            return target
        raise IngestError(f"Le fichier audio existe déjà : {target}")
    run(command)
    if not target.is_file() or target.stat().st_size == 0:
        raise IngestError("L'extraction audio n'a produit aucun fichier exploitable.")
    return target


def run_transcription_pass(
    audio: Path,
    output_dir: Path,
    output_name: str,
    args: argparse.Namespace,
    prompt: str | None,
) -> None:
    expected = [output_dir / f"{output_name}.{extension}" for extension in OUTPUT_FORMATS]
    if all(path.is_file() for path in expected):
        if args.resume:
            return
        raise IngestError(f"Les fichiers de transcription existent déjà dans {output_dir}.")
    output_dir.mkdir(parents=True, exist_ok=True)
    command = [
        "mlx_whisper",
        str(audio),
        "--model",
        args.model,
        "--language",
        args.language,
        "--task",
        "transcribe",
        "--output-format",
        "all",
        "--output-dir",
        str(output_dir),
        "--output-name",
        output_name,
        "--verbose",
        "False",
    ]
    if prompt:
        command.extend(["--initial-prompt", prompt])
    run(command)
    missing = [path.name for path in expected if not path.is_file()]
    if missing:
        raise IngestError("Sorties de transcription manquantes : " + ", ".join(missing))


def transcribe(audio: Path, target_dir: Path, args: argparse.Namespace) -> None:
    if args.vocabulary_prompt:
        run_transcription_pass(audio, target_dir / "brut", "transcription-brute", args, None)
    run_transcription_pass(audio, target_dir, "transcription", args, args.vocabulary_prompt)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_last_srt_seconds(path: Path) -> float:
    pattern = re.compile(r"(\d{2}):(\d{2}):(\d{2}),(\d{3})\s*$")
    last = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if "-->" not in line:
            continue
        match = pattern.search(line.split("-->", 1)[1].strip())
        if match:
            hours, minutes, seconds, millis = map(int, match.groups())
            last = hours * 3600 + minutes * 60 + seconds + millis / 1000
    if last is None:
        raise IngestError("Aucun timecode exploitable dans le SRT.")
    return last


def atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    os.replace(temporary, path)


def format_duration(seconds: float) -> str:
    total = int(round(seconds))
    return f"{total // 60}:{total % 60:02d}"


def write_catalogue_markdown(corpus: Path, catalog: dict) -> None:
    sources = catalog.get("sources", [])
    total_duration = sum(float(item.get("duration_seconds") or 0) for item in sources)
    lines = [
        "# Corpus Drop Elite",
        "",
        "Ce dossier est la source locale canonique des vidéos autorisées, de leurs transcriptions et des fiches de cours dérivées.",
        "",
        "## Couverture actuelle",
        "",
        "| Source | Titre | Durée | Transcription | Fiche |",
        "|---|---|---:|---|---|",
    ]
    for item in sources:
        title = item.get("title_observed") or item.get("title_inferred") or "Sans titre"
        if not item.get("title_observed") and item.get("title_inferred"):
            title += " *(titre inféré)*"
        lines.append(
            f"| `{item['source_id']}` | {title.replace('|', '/')} | {format_duration(float(item.get('duration_seconds') or 0))} | "
            f"{item.get('transcription_status', 'MANQUANT')} | {item.get('brief_status', 'MANQUANT')} |"
        )
    lines.extend(
        [
            "",
            f"Couverture : **{len(sources)} vidéo(s)**, **{format_duration(total_duration)}**. La stratégie complète ne doit être déclarée couverte que lorsque les modules procéduraux requis sont présents.",
            "",
            "## Règles",
            "",
            "- Conserver la transcription automatique et les sous-titres horodatés.",
            "- Ne jamais présenter une phrase incertaine comme une citation exacte.",
            "- Séparer ce qui est enseigné dans la formation de ce qui est vérifié sur le terrain aujourd'hui.",
            "- Revalider les prix, promotions, fonctionnalités publicitaires, délais fournisseurs et règles de plateforme avant toute application.",
            "- N'exécuter aucune dépense, publication, commande ou mutation commerciale sans autorisation distincte.",
            "",
        ]
    )
    (corpus / "CATALOGUE.md").write_text("\n".join(lines), encoding="utf-8")


def update_catalog(corpus: Path, entry: dict, course_name: str, timestamp: str) -> None:
    path = corpus / "catalog.json"
    if path.is_file():
        catalog = json.loads(path.read_text(encoding="utf-8"))
    else:
        catalog = {
            "schema_version": 1,
            "course": {"name_observed": course_name, "platform": "Skool", "owner": None},
            "corpus_root": str(corpus),
            "sources": [],
        }
    sources = [item for item in catalog.get("sources", []) if item.get("source_id") != entry["source_id"]]
    sources.append(entry)
    catalog["sources"] = sorted(sources, key=lambda item: item["source_id"])
    catalog["updated_at"] = timestamp
    atomic_json(path, catalog)
    write_catalogue_markdown(corpus, catalog)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="URL HTTPS directe ou fichier média local")
    parser.add_argument("--source-id", help="Identifiant stable en minuscules et tirets")
    parser.add_argument("--title-observed")
    parser.add_argument("--title-inferred")
    parser.add_argument("--source-label")
    parser.add_argument("--course", default="Drop Elite")
    parser.add_argument("--authorization-note", required=True)
    parser.add_argument("--vocabulary-prompt")
    parser.add_argument("--language", default="fr")
    parser.add_argument("--model", default="mlx-community/whisper-turbo")
    parser.add_argument("--corpus-root", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--resume", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        require_commands()
        source = validate_source(args.source)
        source_id = args.source_id or infer_source_id(source)
        if not SOURCE_ID_RE.fullmatch(source_id):
            raise IngestError("source_id invalide : utiliser 3 à 64 caractères a-z, 0-9 et tirets.")
        corpus = args.corpus_root.expanduser().resolve()
        target_dir = corpus / "sources" / source_id
        if target_dir.exists() and any(target_dir.iterdir()) and not args.resume:
            raise IngestError(f"La source existe déjà : {target_dir}. Utiliser --resume pour la compléter.")
        target_dir.mkdir(parents=True, exist_ok=True)
        media = probe_media(source)
        audio = extract_audio(source, target_dir, str(media.get("audio_codec") or ""), args.resume)
        transcribe(audio, target_dir, args)

        transcript_txt = target_dir / "transcription.txt"
        transcript_json = target_dir / "transcription.json"
        transcript_data = json.loads(transcript_json.read_text(encoding="utf-8"))
        last_time = parse_last_srt_seconds(target_dir / "transcription.srt")
        audio_probe = probe_media(str(audio))
        if abs(last_time - audio_probe["duration_seconds"]) > 5:
            raise IngestError(
                f"Le dernier timecode ({last_time:.3f}s) ne couvre pas la durée audio ({audio_probe['duration_seconds']:.3f}s)."
            )

        timestamp = now_iso()
        status = "AUTOMATIQUE_CONTEXTUALISEE_NON_RELUE" if args.vocabulary_prompt else "AUTOMATIQUE_NON_RELUE"
        source_metadata = {
            "schema_version": 1,
            "source_id": source_id,
            "course_name_observed": args.course,
            "title_observed": args.title_observed,
            "title_inferred": args.title_inferred,
            "source_label": args.source_label,
            "source_url": source if urlparse(source).scheme else None,
            "source_file": source if not urlparse(source).scheme else None,
            "source_type": "direct_https_media" if urlparse(source).scheme else "local_media",
            "authorization": {"basis": args.authorization_note, "recorded_at": timestamp},
            "media": {
                **media,
                "stored_audio_size_bytes": audio.stat().st_size,
                "stored_audio_duration_seconds": audio_probe["duration_seconds"],
            },
            "transcription": {
                "language": args.language,
                "engine": "mlx-whisper",
                "model": args.model,
                "status": status,
                "word_count": len(transcript_txt.read_text(encoding="utf-8").split()),
                "segment_count": len(transcript_data.get("segments", [])),
                "known_uncertainties": [],
            },
            "files": {
                "audio": audio.name,
                "transcript_txt": "transcription.txt",
                "subtitles_srt": "transcription.srt",
                "subtitles_vtt": "transcription.vtt",
                "segments_tsv": "transcription.tsv",
                "transcript_json": "transcription.json",
                "lesson_brief": "lesson-brief.md",
                "raw_first_pass_dir": "brut" if args.vocabulary_prompt else None,
            },
            "checksums_sha256": {"audio": sha256(audio), "selected_transcript_txt": sha256(transcript_txt)},
        }
        atomic_json(target_dir / "source.json", source_metadata)

        catalog_entry = {
            "source_id": source_id,
            "title_observed": args.title_observed,
            "title_inferred": args.title_inferred,
            "source_label": args.source_label,
            "source_url": source if urlparse(source).scheme else None,
            "duration_seconds": audio_probe["duration_seconds"],
            "language": args.language,
            "ingested_at": timestamp,
            "transcription_status": status,
            "brief_status": "MANQUANT_A_CREER",
            "relative_dir": f"sources/{source_id}",
            "topics": [],
        }
        update_catalog(corpus, catalog_entry, args.course, timestamp)
        print(
            json.dumps(
                {
                    "status": "OK",
                    "source_id": source_id,
                    "source_dir": str(target_dir),
                    "duration_seconds": audio_probe["duration_seconds"],
                    "word_count": source_metadata["transcription"]["word_count"],
                    "brief_status": "MANQUANT_A_CREER",
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0
    except (IngestError, json.JSONDecodeError, OSError) as exc:
        print(f"ERREUR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
