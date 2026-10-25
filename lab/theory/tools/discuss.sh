#!/usr/bin/env bash
# One discussion turn by an external model.
#   lab/theory/tools/discuss.sh <sol|argon> <prompt.md> <output.md>
# sol is gpt-6.1-sol at high reasoning through the Codex CLI, read-only. argon is
# gemini-4-argon-high through the Antigravity CLI, with permissions bypassed so it
# can read PDFs and write its review, object by object, into a scratch file of its
# own. tools/argon_audit.py rejects any argon write outside that file. astra
# (gpt-6-astra) is retired from the rotation on 2026-10-25 and still callable.
# The output gets a header naming the model, and every call appends a row to
# lab/theory/discussants.csv.
set -uo pipefail
who="${1:?sol or argon}"; prompt="${2:?prompt file}"; out="${3:?output file}"
here="$(cd "$(dirname "$0")" && pwd -P)"
repo="$(git -C "$here" rev-parse --show-toplevel)"
log="$repo/lab/theory/discussants.csv"
[ -f "$log" ] || echo "date,discussant,model,prompt,output,exit,tokens" > "$log"
[ -f "$prompt" ] || { echo "no prompt file $prompt" >&2; exit 2; }
tmp="$(mktemp)"; err="$(mktemp)"; audit=""
codex_turn() {  # model, reasoning effort
  timeout 3900 codex exec -m "$1" -c "model_reasoning_effort=\"$2\"" -s read-only -C "$repo" -o "$tmp" - < "$prompt" > "$err" 2>&1
  code=$?
  tokens="$(grep -A1 'tokens used' "$err" | tail -1 | tr -d ', ')"
}
case "$who" in
  sol)   model="gpt-6.1-sol"; codex_turn "$model" high ;;
  astra) model="gpt-6-astra"; codex_turn "$model" medium ;;
  argon)
    model="gemini-4-argon-high"
    # One argon call at a time, so the audit can find this call's agy log.
    lock="${TMPDIR:-/tmp}/he-ml-argon.lock"
    until mkdir "$lock" 2>/dev/null; do
      holder="$(cat "$lock/pid" 2>/dev/null)"
      if [ -n "$holder" ] && ! kill -0 "$holder" 2>/dev/null; then rm -rf "$lock"; continue; fi
      sleep 30
    done
    work="$(mktemp -d "${TMPDIR:-/tmp}/argon-XXXXXX")"; work="$(cd "$work" && pwd -P)"
    echo $$ > "$lock/pid"; trap 'rm -rf "$lock" "$work"' EXIT
    # The PDF folder (a symlink out of the repository) and FORMAL_SECURITY join the
    # workspace, or headless argon cannot open them.
    extra=(--add-dir "$work")
    for d in "$repo/lib/literature/pdfs" "$HOME/Documents/RESEARCH/FORMAL_SECURITY"; do
      [ -d "$d" ] && extra+=(--add-dir "$(cd "$d" && pwd -P)")
    done
    # Why object by object: on 2026-10-25 argon-high, judging a whole round in one
    # turn, thought for 22,000 to 27,000 tokens without streaming any, and the
    # client's 5-minute stream idle timeout cut every attempt (agy transcripts under
    # ~/.gemini/antigravity-cli/brain/). One object per turn keeps each silence short.
    protocol="How you deliver this review. This comes before everything below.
1. Your first action is to create the file $work/review.md with the line
   '# Review' and nothing else, using your file-writing tool.
2. Then read what the task below asks you to read, and judge the objects one
   at a time. As soon as you have judged one object, append your judgement of
   it to $work/review.md, in the form the task asks, before you read or think
   about the next object. Never hold more than one judgement unwritten.
3. Append the general remarks and then the Verdicts section last.
4. Write to no other file, and run no command that changes a file. Read-only
   commands are allowed, for instance pdftotext on a paper or a short numerical
   check that prints to the screen.
5. When the file is complete, reply with the single word DONE.

The task:

"
    start="$(date +%s)"
    ( cd "$repo" && timeout 3900 agy -p "$protocol$(cat "$prompt")" --model "$model" --mode plan \
        --dangerously-skip-permissions "${extra[@]}" --print-timeout 3600s ) > "$err.stdout" 2> "$err"
    code=$?
    audit="$(python3 "$here/argon_audit.py" "$start" "$work")" || code="audit"
    [ -s "$work/review.md" ] && cp "$work/review.md" "$tmp"
    tokens=""
    ;;
  *) echo "discussant must be sol or argon (astra is retired)" >&2; exit 2 ;;
esac
rel_prompt="${prompt#"$repo"/}"; rel_out="${out#"$repo"/}"
# A round prompt asks for a verdict block. An answer without one is a failed call,
# kept beside the output as .noverdict for inspection, never the discussant file.
[ "$code" = "0" ] && [ ! -s "$tmp" ] && code="empty"
if [ "$code" = "0" ] && grep -q '## Verdicts' "$prompt" && ! grep -q '## Verdicts' "$tmp"; then
  code="noverdict"; cp "$tmp" "$out.noverdict"
fi
echo "$(date +%F),$who,$model,$rel_prompt,$rel_out,$code,$tokens" >> "$log"
if [ "$code" != "0" ] || [ ! -s "$tmp" ]; then
  echo "DISCUSS FAILED $who exit $code ${audit}" >&2; tail -20 "$err" >&2; rm -f "$tmp" "$err" "$err.stdout"; exit 1
fi
{ printf -- '---\nmodel: %s\ndiscussant: %s\ndate: %s\nprompt: %s\n' "$model" "$who" "$(date +%F)" "$rel_prompt"
  [ -n "$audit" ] && printf -- 'audit: %s\n' "$audit"
  printf -- '---\n\n'; cat "$tmp"; } > "$out"
rm -f "$tmp" "$err" "$err.stdout"
echo "DISCUSS OK $rel_out"
