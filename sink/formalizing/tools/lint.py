#!/usr/bin/env python3
"""Lint the formalizing context. Run from the HE-ML repository root:

    python3 sink/formalizing/tools/lint.py

The rules are the section Lint of sink/formalizing/README.md. The script prints
every failure and exits 1, or prints LINT OK and exits 0.
"""
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(HERE))
ROOTS = {"HE-ML": REPO, "FS": os.path.expanduser("~/Documents/RESEARCH/FORMAL_SECURITY")}

SLUG = re.compile(r"^(def|thm|lem|prop|conj|fact|prob|search)-[a-z0-9]+(-[a-z0-9]+)*$")
STATUS = {
    "results.md": {"proven", "heuristic", "empirical", "open", "refuted", "retracted"},
    "facts.md": {"verified", "recorded", "disputed", "superseded"},
    "problems.md": {"open", "partial", "solved", "refuted-as-posed", "withdrawn"},
}
REQUIRED = {
    "results.md": ["kind", "statement", "where", "status", "evidence", "checked-by", "oracle"],
    "facts.md": ["claim", "paper", "pointer", "read", "status", "record"],
    "problems.md": ["statement", "posed", "weight", "status", "literature", "where"],
}
KINDS = {"definition", "theorem", "lemma", "proposition", "conjecture", "construction"}
WEIGHTS = {"central", "supporting", "side"}
ORACLE = {"needs-oracle", "holds-without-oracle", "n/a"}
REF_KEYS = {"uses-to-state", "uses-to-prove", "depends-on", "alias"}
PATH = re.compile(r"\b(HE-ML|FS):([^\s,#)`]+)")

fail = []


def read(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as fh:
        return fh.read()


def entries(name):
    """Split a register into (slug, {key: value}) by level-two headings."""
    out = []
    text = read(name)
    if "\n## Archive" in text:
        text = text.replace("\n## Archive", "\n## archive-marker", 1)
    for block in re.split(r"\n(?=## )", "\n" + text):
        if not block.startswith("## "):
            continue
        head = block.splitlines()[0][3:].strip()
        if head == "archive-marker":
            continue
        fields, key = {}, None
        for line in block.splitlines()[1:]:
            m = re.match(r"^([a-z-]+):\s?(.*)$", line)
            if m:
                key = m.group(1)
                fields[key] = m.group(2).strip()
            elif key and line.startswith("  "):
                fields[key] += "\n" + line.strip()
        out.append((head, fields))
    return out


registers = {}
for name in ["results.md", "facts.md", "problems.md"]:
    try:
        registers[name] = entries(name)
    except FileNotFoundError:
        fail.append(f"{name} is missing")
        registers[name] = []

# Search rows: a markdown table whose second column is the slug.
search_slugs = []
try:
    for line in read("searches.md").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 10 or not cells[1].startswith("search-"):
            continue
        slug = cells[1]
        search_slugs.append(slug)
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", cells[0]):
            fail.append(f"searches.md {slug}: date '{cells[0]}' is not YYYY-MM-DD")
        if not cells[4] or not cells[5]:
            fail.append(f"searches.md {slug}: query or scope is empty")
except FileNotFoundError:
    fail.append("searches.md is missing")

# Slugs: well formed and unique across the registers.
all_slugs = {}
for name, ents in registers.items():
    for slug, _ in ents:
        if not SLUG.match(slug):
            fail.append(f"{name}: heading '{slug}' is not a slug")
        all_slugs.setdefault(slug, []).append(name)
for slug in search_slugs:
    if not SLUG.match(slug):
        fail.append(f"searches.md: '{slug}' is not a slug")
    all_slugs.setdefault(slug, []).append("searches.md")
for slug, where in all_slugs.items():
    if len(where) > 1:
        fail.append(f"slug {slug} appears {len(where)} times ({', '.join(where)})")
aliases = set()
for ents in registers.values():
    for _, f in ents:
        for a in re.findall(r"[a-z]+-[a-z0-9-]+", f.get("alias", "")):
            aliases.add(a)
known = set(all_slugs) | aliases

# Fields, closed vocabularies, references and paths.
for name, ents in registers.items():
    for slug, f in ents:
        for k in REQUIRED[name]:
            if not f.get(k):
                fail.append(f"{name} {slug}: no '{k}:' line")
        st = f.get("status", "").split()[0].rstrip(".,") if f.get("status") else ""
        if st and st not in STATUS[name]:
            fail.append(f"{name} {slug}: status '{st}' is not in the closed list")
        if name == "results.md":
            kd = f.get("kind", "").split()[0].rstrip(".,") if f.get("kind") else ""
            if kd and kd not in KINDS:
                fail.append(f"{name} {slug}: kind '{kd}' is not in the closed list")
            orc = f.get("oracle", "").split()[0].rstrip(".,") if f.get("oracle") else ""
            if orc and orc not in ORACLE:
                fail.append(f"{name} {slug}: oracle '{orc}' is not in the closed list")
        if name == "problems.md":
            w = f.get("weight", "").split()[0].rstrip(".,") if f.get("weight") else ""
            if w and w not in WEIGHTS:
                fail.append(f"{name} {slug}: weight '{w}' is not in the closed list")
            lit = f.get("literature", "")
            for s in re.findall(r"search-[a-z0-9-]+", lit):
                if s not in known:
                    fail.append(f"{name} {slug}: literature names unknown {s}")
        for k in REF_KEYS - {"alias"}:
            for s in re.findall(r"\b(?:def|thm|lem|prop|conj|fact|prob|search)-[a-z0-9]+(?:-[a-z0-9]+)*", f.get(k, "")):
                if s not in known:
                    fail.append(f"{name} {slug}: {k} names unknown {s}")
        for v in f.values():
            for root, p in PATH.findall(v):
                p = p.rstrip(".;:")
                if root == "HE-ML" and not os.path.exists(os.path.join(ROOTS[root], p)):
                    fail.append(f"{name} {slug}: path HE-ML:{p} does not exist")

# STATE.md: short, dated, not older than the log.
try:
    state = read("STATE.md")
    n = len(state.splitlines())
    if n > 80:
        fail.append(f"STATE.md has {n} lines, at most 80")
    m = re.search(r"^updated:\s*(\d{4}-\d{2}-\d{2})", state, re.M)
    if not m:
        fail.append("STATE.md has no 'updated: YYYY-MM-DD' line")
    else:
        logs = re.findall(r"^## \[(\d{4}-\d{2}-\d{2})\]", read("log.md"), re.M)
        if logs and max(logs) > m.group(1):
            fail.append(f"STATE.md updated {m.group(1)} is older than the last log entry {max(logs)}")
        if not logs:
            fail.append("log.md has no entry")
except FileNotFoundError as e:
    fail.append(f"{os.path.basename(e.filename)} is missing")

if fail:
    print(f"{len(fail)} lint failure(s):")
    for f in fail:
        print(f"  {f}")
    sys.exit(1)
n = sum(len(e) for e in registers.values())
print(f"LINT OK entries={n} searches={len(search_slugs)}")
