#!/usr/bin/env python3
"""Build Halil's reading folder, lib/theory/, which holds PDFs only.

    python3 lab/theory/tools/build.py             booklet.pdf and every reading
    python3 lab/theory/tools/build.py --changes   also booklet-changes.pdf, against the last commit

Sources live in lab/theory/: the booklet in booklet/ (booklet.tex, preamble.tex,
chapters/), readings in readings/YYYY-MM-DD-<slug>.md. LaTeX runs in a temporary
folder, so no build file lands in the repository. The build fails when an object
of the booklet has a duplicate slug or an unknown status, when a reference is
undefined, or when lib/theory/ holds anything but PDFs.
"""
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
THEORY = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(THEORY))
BOOK = os.path.join(THEORY, "booklet")
OUT = os.path.join(REPO, "lib", "theory")
LO_FULL = os.path.join(REPO, "sink", "2026-10-16-formal-tuning", "final", "learning-oracle-theory.md")
ENVS = "definition|lemma|theorem|proposition|conjecture|borrowed"
STATUSES = {"checked", "accepted", "sketch", "open", "borrowed", "refuted"}
COLOR = {"checked": "#2e7d32", "accepted": "#1f4e8c", "sketch": "#d9822b",
         "open": "#8a8a8a", "borrowed": "#7b3f8c", "refuted": "#b03030"}
SHAPE = {"definition": "box", "borrowed": "note", "conjecture": "diamond"}


def sources(root):
    """The booklet text: the main file with every \\input chapter inlined."""
    main = open(os.path.join(root, "booklet.tex"), encoding="utf-8").read()
    def inline(m):
        p = os.path.join(root, m.group(1) + ".tex")
        return open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    return re.sub(r"\\input\{(chapters/[^}]+)\}", inline, main)


def objects(tex):
    out = []
    for kind, body in re.findall(r"\\begin\{(" + ENVS + r")\}(.*?)\\end\{\1\}", tex, re.S):
        slug = re.search(r"\\blabel\{([^}]+)\}", body)
        st = re.search(r"\\status\{([^}]+)\}", body)
        out.append((kind, slug.group(1) if slug else None, st.group(1) if st else None, body))
    return out


def check(tex):
    fails, seen = [], set()
    for kind, slug, st, _ in objects(tex):
        if not slug:
            fails.append(f"a {kind} has no \\blabel")
            continue
        if slug in seen:
            fails.append(f"slug {slug} appears twice")
        seen.add(slug)
        if st not in STATUSES:
            fails.append(f"{slug}: status {st} is not one of {sorted(STATUSES)}")
    return fails


def graph(tex):
    lines = ["digraph G {", "  rankdir=BT; node [fontname=Helvetica, fontsize=10, style=filled, fontcolor=white];"]
    edges = set()
    for kind, slug, st, body in objects(tex):
        lines.append(f'  "{slug}" [shape={SHAPE.get(kind, "ellipse")}, fillcolor="{COLOR.get(st, "#8a8a8a")}"];')
    for slug, block in re.findall(r"\\blabel\{([^}]+)\}(.*?)(?=\\blabel\{|\\chapter|\\section|\\end\{document\})", tex, re.S):
        for style, cmd in (("solid", "usesstatement"), ("dashed", "usesproof")):
            for group in re.findall(r"\\" + cmd + r"\{([^}]+)\}", block):
                for dep in group.split(","):
                    edges.add((dep.strip(), slug, style))
    lines += [f'  "{a}" -> "{b}" [style={s}];' for a, b, s in sorted(edges)]
    lines.append("}")
    return "\n".join(lines)


def latex(name, tmp):
    for _ in range(3):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", name],
                           cwd=tmp, capture_output=True, text=True, errors="replace")
        if r.returncode != 0:
            out = r.stdout.splitlines()
            at = next((i for i, l in enumerate(out) if l.startswith("!")), None)
            ctx = out[max(0, at - 4):at + 6] if at is not None else out[-12:]
            sys.exit(f"pdflatex failed on {name}:\n" + "\n".join(ctx))
    log = open(os.path.join(tmp, name[:-4] + ".log"), encoding="utf-8", errors="replace").read()
    if re.search(r"There were undefined references|Reference `[^']+' on page \d+ undefined", log):
        refs = sorted(set(re.findall(r"Reference `([^']+)' on page", log)))
        sys.exit(f"undefined references in {name}: {refs}")


def stage(tmp, root):
    """Copy a booklet tree into tmp and add its generated parts."""
    shutil.copytree(root, tmp, dirs_exist_ok=True)
    tex = sources(tmp)
    with open(os.path.join(tmp, "graph.dot"), "w") as fh:
        fh.write(graph(tex))
    subprocess.run(["dot", "-Tpdf", os.path.join(tmp, "graph.dot"), "-o", os.path.join(tmp, "graph.pdf")], check=True)
    proofs = fullproofs(tex)
    if proofs:
        with open(os.path.join(tmp, "fullproofs.tex"), "w") as fh:
            fh.write(proofs)
    if os.path.exists(LO_FULL):
        full = subprocess.run(["pandoc", LO_FULL, "-f", "markdown+tex_math_dollars", "-t", "latex",
                               "--top-level-division=section"], capture_output=True, text=True, check=True).stdout
        full = re.sub(r"\\label\{[^}]*\}", "", full)  # pandoc's heading labels would clash with the slugs
        with open(os.path.join(tmp, "learning-oracle-full.tex"), "w") as fh:
            fh.write(full)
    return tex


def section_of(path, slug):
    """The Markdown section of a round file whose heading starts with the slug."""
    lines = open(os.path.join(REPO, path), encoding="utf-8").read().split("\n")
    for i, line in enumerate(lines):
        m = re.match(r"(#+) " + re.escape(slug) + r"(:.*)?$", line)
        if m:
            level, out = len(m.group(1)), []
            for nxt in lines[i + 1:]:
                h = re.match(r"(#+) ", nxt)
                if h and len(h.group(1)) <= level:
                    break
                out.append(nxt)
            return level, (m.group(2) or ":")[1:].strip(), "\n".join(out)
    sys.exit(f"\\fullproof: no heading for {slug} in {path}")


def fullproofs(tex):
    """One appendix section per \\fullproof{slug}{round file}, converted by pandoc."""
    parts = []
    for slug, paths in re.findall(r"\\fullproof\{([^}]+)\}\{([^}]+)\}", tex):
        # Several round files, comma-separated, when a later round revises part of an object.
        blocks, name = [], ""
        for path in [p.strip() for p in paths.split(",")]:
            level, title, body = section_of(path, slug)
            name = title or name
            latex = subprocess.run(["pandoc", "-f", "markdown+tex_math_dollars", "-t", "latex",
                                    f"--shift-heading-level-by={1 - level}"],
                                   input=body, capture_output=True, text=True, check=True).stdout
            latex = re.sub(r"\\label\{[^}]*\}", "", latex)
            blocks.append((path, latex))
        if name:  # the heading text, Markdown with mathematics, through pandoc too
            name = subprocess.run(["pandoc", "-f", "markdown+tex_math_dollars", "-t", "latex"],
                                  input=name, capture_output=True, text=True, check=True).stdout.strip()
        text = "".join(f"\\par\\medskip\\noindent\\textbf{{From}} \\path{{{path}}}.\\par\n{latex}\n" if len(blocks) > 1 else latex
                       for path, latex in blocks)
        parts.append(f"\\section{{{name or slug}}}\\label{{fp:{slug}}}\n\\noindent\\texttt{{{slug}}}, from "
                     + " and ".join(f"\\path{{{path}}}" for path, _ in blocks) + f".\n\n{text}\n")
    return "\n".join(parts)


def statuses(tex):
    return {slug: st for _, slug, st, _ in objects(tex) if slug}


def change_box(old, new):
    a, b = statuses(old), statuses(new)
    rows = [f"\\item added \\texttt{{{s}}} ({b[s]})" for s in b if s not in a]
    rows += [f"\\item removed \\texttt{{{s}}}" for s in a if s not in b]
    rows += [f"\\item \\texttt{{{s}}}: {a[s]} $\\to$ {b[s]}" for s in b if s in a and a[s] != b[s]]
    body = "\n".join(rows) if rows else "\\item no object added, removed or re-statused"
    return ("\\begin{tcolorbox}[colback=blue!4,colframe=NavyBlue,title=Changes since the last commit]\n"
            "Blue text is new, red text is removed.\n\\begin{itemize}\n" + body + "\n\\end{itemize}\n\\end{tcolorbox}\n")


def committed_tree(dest):
    """The booklet sources as of HEAD, or None when they were never committed."""
    rel = os.path.relpath(BOOK, REPO)
    ls = subprocess.run(["git", "ls-tree", "-r", "--name-only", "HEAD", rel], cwd=REPO, capture_output=True, text=True)
    files = [f for f in ls.stdout.split() if f.endswith(".tex")]
    if not files:
        return None
    for f in files:
        p = os.path.join(dest, os.path.relpath(f, rel))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as fh:
            fh.write(subprocess.run(["git", "show", f"HEAD:{f}"], cwd=REPO, capture_output=True, text=True).stdout)
    return dest


def readings():
    built = []
    for md in sorted(glob.glob(os.path.join(THEORY, "readings", "*.md"))):
        pdf = os.path.join(OUT, os.path.basename(md)[:-3] + ".pdf")
        r = subprocess.run(["pandoc", md, "-o", pdf, "--pdf-engine=xelatex", "-f", "markdown+tex_math_dollars",
                            "-V", "geometry:margin=1in", "-V", "mainfont=STIX Two Text", "-V", "mathfont=STIX Two Math",
                            "-V", "fontsize=11pt", "-V", "colorlinks=true"], capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit(f"reading {os.path.basename(md)} failed: {r.stderr.strip().splitlines()[-3:]}")
        built.append(os.path.basename(pdf))
    return built


def main():
    os.makedirs(OUT, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        new = stage(tmp, BOOK)
        fails = check(new)
        if fails:
            sys.exit("booklet check failed:\n  " + "\n  ".join(fails))
        latex("booklet.tex", tmp)
        shutil.copy(os.path.join(tmp, "booklet.pdf"), os.path.join(OUT, "booklet.pdf"))
        print(f"BOOKLET OK lib/theory/booklet.pdf objects={len(objects(new))}")
        if "--changes" in sys.argv:
            with tempfile.TemporaryDirectory() as old_tmp:
                if committed_tree(old_tmp) is None:
                    print("CHANGES SKIPPED, the booklet has no committed version yet")
                else:
                    old = sources(old_tmp)
                    flat_old, flat_new = os.path.join(tmp, "old-flat.tex"), os.path.join(tmp, "new-flat.tex")
                    open(flat_old, "w").write(re.sub(r"\\input\{preamble\}", lambda m: open(os.path.join(old_tmp, "preamble.tex")).read(), old))
                    open(flat_new, "w").write(re.sub(r"\\input\{preamble\}", lambda m: open(os.path.join(tmp, "preamble.tex")).read(), new))
                    diff = subprocess.run(["latexdiff", "--type=CFONT", flat_old, flat_new],
                                          capture_output=True, text=True, check=True).stdout
                    diff = diff.replace("\\maketitle", "\\maketitle\n" + change_box(old, new), 1)
                    open(os.path.join(tmp, "changes.tex"), "w").write(diff)
                    latex("changes.tex", tmp)
                    shutil.copy(os.path.join(tmp, "changes.pdf"), os.path.join(OUT, "booklet-changes.pdf"))
                    print("CHANGES OK lib/theory/booklet-changes.pdf")
    for name in readings():
        print(f"READING OK lib/theory/{name}")
    stray = [f for f in os.listdir(OUT) if not f.endswith(".pdf") and f != ".DS_Store"]
    if stray:
        sys.exit(f"lib/theory/ must hold PDFs only, found: {stray}")
    print("BUILD OK")


if __name__ == "__main__":
    main()
