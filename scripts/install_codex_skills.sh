#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
codex_target_root="${CODEX_SKILLS_DIR:-${HOME}/.codex/skills}"
agent_target_root="${AGENT_SKILLS_DIR:-${HOME}/.agents/skills}"
force=0
only_skill=""

while [[ "$#" -gt 0 ]]; do
  case "$1" in
    --force)
      force=1
      shift
      ;;
    --only)
      if [[ -z "${2:-}" ]]; then
        echo "--only exige un nom de skill" >&2
        exit 2
      fi
      only_skill="$2"
      shift 2
      ;;
    *)
      echo "Usage: $0 [--force] [--only NOM_DU_SKILL]" >&2
      exit 2
      ;;
  esac
done

install_one() {
  local source_dir="$1"
  local target_root="$2"
  local skill_name
  local target_dir
  skill_name="$(basename "$source_dir")"
  target_dir="$target_root/$skill_name"
  mkdir -p "$target_root"
  if [[ -e "$target_dir" ]]; then
    if [[ "$force" -ne 1 ]]; then
      echo "[SKIP] $target_dir existe déjà"
      return
    fi
    local backup_dir="${target_dir}.backup-$(date +%Y%m%d-%H%M%S)"
    mv "$target_dir" "$backup_dir"
    echo "[BACKUP] $target_dir -> $backup_dir"
  fi
  cp -R "$source_dir" "$target_dir"
  if [[ "$target_root" == "$codex_target_root" && "$skill_name" == "derouler-strategie-drop-elite" ]]; then
    printf '%s\n' "$repo_root" > "$target_dir/references/repo-root.txt"
  fi
  echo "[OK] $target_dir"
}

for source_dir in "$repo_root"/skills/*; do
  [[ -d "$source_dir" ]] || continue
  [[ -z "$only_skill" || "$(basename "$source_dir")" == "$only_skill" ]] || continue
  install_one "$source_dir" "$codex_target_root"
done

for source_dir in "$repo_root"/vendor/agent-skills/*; do
  [[ -d "$source_dir" ]] || continue
  [[ -z "$only_skill" || "$(basename "$source_dir")" == "$only_skill" ]] || continue
  install_one "$source_dir" "$agent_target_root"
done

echo "Installation terminée. Relancer Codex pour recharger les skills."
