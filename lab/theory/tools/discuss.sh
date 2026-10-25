#!/usr/bin/env bash
# One discussion turn by an external model, read-only in the repository.
#   lab/theory/tools/discuss.sh <astra|argon> <prompt.md> <output.md>
# astra is gpt-6-astra through the Codex CLI, argon is gemini-4-argon-high
# through the Antigravity CLI. Both run read-only. The output gets a header
# naming the model, and every call appends a row to lab/theory/discussants.csv.
set -uo pipefail
who="${1:?astra or argon}"; prompt="${2:?prompt file}"; out="${3:?output file}"
repo="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
log="$repo/lab/theory/discussants.csv"
[ -f "$log" ] || echo "date,discussant,model,prompt,output,exit,tokens" > "$log"
[ -f "$prompt" ] || { echo "no prompt file $prompt" >&2; exit 2; }
tmp="$(mktemp)"; err="$(mktemp)"
case "$who" in
  astra)
    model="gpt-6-astra"
    timeout 3900 codex exec -m "$model" -s read-only -C "$repo" -o "$tmp" - < "$prompt" > "$err" 2>&1
    code=$?
    tokens="$(grep -A1 'tokens used' "$err" | tail -1 | tr -d ', ')"
    ;;
  argon)
    model="gemini-4-argon-medium"
    # One argon call at a time. On 2026-10-25 every concurrent argon-high call on a
    # round prompt died on the backend's 5-minute stream idle timeout, retried, and
    # hit the print timeout with no output (agy logs, ~/.gemini/antigravity-cli/log).
    lock="${TMPDIR:-/tmp}/he-ml-argon.lock"
    until mkdir "$lock" 2>/dev/null; do
      holder="$(cat "$lock/pid" 2>/dev/null)"
      if [ -n "$holder" ] && ! kill -0 "$holder" 2>/dev/null; then rm -rf "$lock"; continue; fi
      sleep 30
    done
    echo $$ > "$lock/pid"; trap 'rm -rf "$lock"' EXIT
    # Headless agy reads only its workspace: add the PDF folder (a symlink out of
    # the repository) and FORMAL_SECURITY, or argon answers that it cannot read them.
    extra=()
    for d in "$repo/lib/literature/pdfs" "$HOME/Documents/RESEARCH/FORMAL_SECURITY"; do
      [ -d "$d" ] && extra+=(--add-dir "$(cd "$d" && pwd -P)")
    done
    ( cd "$repo" && timeout 3900 agy -p "$(cat "$prompt")" --model "$model" --mode plan ${extra[@]+"${extra[@]}"} --print-timeout 3600s ) > "$tmp" 2> "$err"
    code=$?
    tokens=""
    ;;
  *) echo "discussant must be astra or argon" >&2; exit 2 ;;
esac
rel_prompt="${prompt#"$repo"/}"; rel_out="${out#"$repo"/}"
# A round prompt asks for a verdict block. An answer without one (for instance
# "I cannot read that file") is a failed call: it is kept beside the output as
# .noverdict for inspection and never becomes the discussant file.
[ "$code" = "0" ] && [ ! -s "$tmp" ] && code="empty"
if [ "$code" = "0" ] && grep -q '## Verdicts' "$prompt" && ! grep -q '## Verdicts' "$tmp"; then
  code="noverdict"; cp "$tmp" "$out.noverdict"
fi
echo "$(date +%F),$who,$model,$rel_prompt,$rel_out,$code,$tokens" >> "$log"
if [ "$code" != "0" ] || [ ! -s "$tmp" ]; then
  echo "DISCUSS FAILED $who exit $code" >&2; tail -20 "$err" >&2; rm -f "$tmp" "$err"; exit 1
fi
{ printf -- '---\nmodel: %s\ndiscussant: %s\ndate: %s\nprompt: %s\n---\n\n' "$model" "$who" "$(date +%F)" "$rel_prompt"; cat "$tmp"; } > "$out"
rm -f "$tmp" "$err"
echo "DISCUSS OK $rel_out"
