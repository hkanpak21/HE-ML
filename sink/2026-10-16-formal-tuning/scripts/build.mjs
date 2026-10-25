#!/usr/bin/env node
// Compile markdown files of the formal-tuning folder to PDFs beside them.
//   node scripts/build.mjs <file.md> [...]   one or more files
//   node scripts/build.mjs --all             every round file, theory/CURRENT.md and final/
// Prints "BUILD OK n=<count>" only when every file compiled.
import { readdirSync, existsSync, statSync } from "node:fs";
import { join, dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");

function all() {
  const files = [];
  for (const d of readdirSync(ROOT).sort()) {
    if (!/^round-\d\d$/.test(d) && d !== "final" && d !== "theory") continue;
    for (const f of readdirSync(join(ROOT, d)).sort()) if (f.endsWith(".md")) files.push(join(ROOT, d, f));
  }
  return files;
}

const args = process.argv.slice(2);
const files = args[0] === "--all" ? all() : args.map((a) => resolve(a));
if (files.length === 0) { console.error("usage: build.mjs <file.md> ... | --all"); process.exit(2); }

let bad = 0;
for (const f of files) {
  if (!existsSync(f) || !statSync(f).isFile()) { console.error(`missing: ${f}`); bad += 1; continue; }
  const out = f.replace(/\.md$/, ".pdf");
  const r = spawnSync("pandoc", [
    f, "-o", out, "--pdf-engine=xelatex", "-f", "markdown+tex_math_dollars",
    "-V", "geometry:margin=1in", "-V", "mainfont=STIX Two Text", "-V", "mathfont=STIX Two Math",
    "-V", "fontsize=11pt", "-V", "colorlinks=true",
  ], { encoding: "utf8", cwd: dirname(f) });
  if (r.status !== 0) {
    bad += 1;
    console.error(`FAILED ${f}\n${(r.stderr || "").split("\n").slice(-15).join("\n")}`);
  }
}
if (bad) { console.error(`${bad} of ${files.length} failed`); process.exit(1); }
console.log(`BUILD OK n=${files.length}`);
