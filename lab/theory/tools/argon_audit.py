#!/usr/bin/env python3
"""Audit one argon call: list its tool calls and reject writes outside its scratch folder.

    argon_audit.py <start-epoch-seconds> <scratch-dir>

argon runs with permissions bypassed (Halil, 2026-10-25), so this check is the
guard. It finds the agy log written after the start time, reads the
conversation transcript that agy keeps under ~/.gemini/antigravity-cli/brain/,
prints one summary line, and exits 2 when a file-changing tool touched a path
outside the scratch folder or a shell command looks like it writes or deletes.
"""
import glob
import json
import os
import re
import sys

AGY = os.path.expanduser("~/.gemini/antigravity-cli")
WRITE_TOOLS = re.compile(r"write|replace|edit|delete|remove|move|rename|create", re.I)
RISKY_COMMAND = re.compile(
    r"(^|[;&|]\s*)(rm|mv|cp|git|sed\s+-i|tee|chmod|chown|curl|wget|pip|brew|npm|touch|mkdir|ln)\b"
    r"|(?<![0-9&])>(?!\s*/dev/null|&)", re.I)
WRITE_CODE = re.compile(r"open\([^)]*['\"][wax]\+?b?['\"]|\.write_(text|bytes)\(|os\.(remove|unlink|rename|replace|rmdir)|shutil\.(rmtree|move|copy)", re.I)


def unquote(v):
    return v[1:-1] if isinstance(v, str) and len(v) >= 2 and v[0] == v[-1] == '"' else v


def main():
    start, scratch = float(sys.argv[1]), os.path.realpath(sys.argv[2])
    logs = [p for p in glob.glob(os.path.join(AGY, "log", "cli-*.log")) if os.path.getmtime(p) >= start - 5]
    conv = None
    for p in sorted(logs, key=os.path.getmtime):
        m = re.search(r"Created conversation ([0-9a-f-]{36})", open(p, errors="replace").read())
        if m:
            conv = m.group(1)
    if conv is None:
        print("audit: no agy conversation found after the start time")
        return 2
    path = os.path.join(AGY, "brain", conv, ".system_generated", "logs", "transcript.jsonl")
    if not os.path.exists(path):
        print(f"audit: conversation {conv} has no transcript")
        return 2
    counts, problems = {}, []
    for line in open(path):
        if not line.strip():
            continue
        for call in json.loads(line).get("tool_calls") or []:
            name, args = call.get("name", "?"), call.get("args") or {}
            counts[name] = counts.get(name, 0) + 1
            if WRITE_TOOLS.search(name):
                for key in ("Path", "TargetFile", "AbsolutePath", "File", "Destination", "Source"):
                    target = unquote(args.get(key))
                    if target and not os.path.realpath(target).startswith(scratch + os.sep):
                        problems.append(f"{name} on {target}")
            if name == "run_command":
                cmd = unquote(args.get("CommandLine", "")).replace('\\"', "'")
                # The shell part, with quoted strings (inline Python, sed scripts) removed,
                # must not write or delete. Inline code must not open files for writing.
                shell = re.sub(r"'[^']*'|\"[^\"]*\"", "''", cmd, flags=re.S)
                if RISKY_COMMAND.search(shell) or WRITE_CODE.search(cmd):
                    problems.append(f"command {cmd[:120]}")
    tools = ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none"
    print(f"conversation {conv}; tools: {tools}" + (f"; REJECTED: {' | '.join(problems)}" if problems else ""))
    return 2 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
