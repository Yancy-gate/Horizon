#!/usr/bin/env bash

set -euo pipefail

if [[ $# -lt 2 || $# -gt 3 ]]; then
  echo "Usage: $0 <horizon-posts-dir> <obsidian-vault-dir> [summary-dir]" >&2
  exit 2
fi

posts_dir=$1
vault_dir=$2
summary_dir=${3:-其他/内参日报}
target_dir="${vault_dir}/${summary_dir}"

if [[ ! -d "$posts_dir" ]]; then
  echo "Horizon posts directory does not exist: ${posts_dir}" >&2
  exit 1
fi

if [[ ! -d "$vault_dir/.git" ]]; then
  echo "Obsidian vault is not a Git repository: ${vault_dir}" >&2
  exit 1
fi

mkdir -p "$target_dir"

total=0
copied=0
skipped=0

shopt -s nullglob
for source_file in "$posts_dir"/????-??-??-summary-zh.md; do
  filename=$(basename "$source_file")
  date=${filename%-summary-zh.md}
  target_file="${target_dir}/horizon-${date}-zh.md"
  total=$((total + 1))

  if [[ -e "$target_file" ]]; then
    skipped=$((skipped + 1))
    continue
  fi

  cp "$source_file" "$target_file"
  copied=$((copied + 1))
done

if [[ $total -eq 0 ]]; then
  echo "No Chinese Horizon summaries found in ${posts_dir}" >&2
  exit 1
fi

echo "Horizon summaries found: ${total}"
echo "New summaries copied: ${copied}"
echo "Existing summaries kept: ${skipped}"
