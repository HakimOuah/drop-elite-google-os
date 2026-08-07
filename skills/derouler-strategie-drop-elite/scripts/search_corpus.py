#!/usr/bin/env python3
"""Recherche accent-insensible dans les VTT et dérivés du corpus du dépôt."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path


DEFAULT_CORPUS = Path(__file__).resolve().parents[3] / "corpus"


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    return "".join(c for c in value if not unicodedata.combining(c)).casefold()


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def parse_vtt(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    blocks = re.split(r"\n\s*\n", text)
    cues: list[dict[str, str]] = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        time_index = next((i for i, line in enumerate(lines) if "-->" in line), None)
        if time_index is None:
            continue
        times = lines[time_index].split("-->", 1)
        body = clean_text(" ".join(lines[time_index + 1 :]))
        if body:
            cues.append({"start": times[0].strip(), "end": times[1].split()[0].strip(), "text": body})
    return cues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="+")
    parser.add_argument("--corpus-root", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--all", action="store_true", help="exiger tous les termes dans un cue")
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    root = args.corpus_root.expanduser().resolve()
    queries = [normalize(term) for term in args.terms]
    results: list[dict[str, str]] = []

    for path in sorted(root.rglob("*.vtt")):
        if "/derived/" in path.as_posix():
            continue
        for cue in parse_vtt(path):
            haystack = normalize(cue["text"])
            matches = [term in haystack for term in queries]
            if (all(matches) if args.all else any(matches)):
                results.append({"source": str(path.relative_to(root)), **cue})
                if len(results) >= args.limit:
                    break
        if len(results) >= args.limit:
            break

    if args.as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for item in results:
            print(f"{item['source']} [{item['start']}–{item['end']}] {item['text']}")
    return 0 if results else 1


if __name__ == "__main__":
    raise SystemExit(main())
