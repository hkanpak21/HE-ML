#!/usr/bin/env node
// Checks of the formal-tuning folder. Run from the folder root:
//   node scripts/verify.mjs structure | convergence | final | audit
// Each mode prints its success marker only after every assertion passes, and
// exits 1 with the list of failures otherwise.
import { readFileSync, readdirSync, existsSync, statSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const MIN_REVIEW_ROUNDS = 6;
const MIN_ACCEPTED = 6;
const MIN_NONTRIVIAL = 3;
const MIN_FINAL_THEOREMS = 5;
const MIN_FINAL_NONTRIVIAL = 3;
const SLUG = /(def|thm|lem)-[a-z0-9]+(?:-[a-z0-9]+)*/;

const fail = [];
const read = (p) => readFileSync(join(ROOT, p), "utf8");
const nonEmpty = (p) => existsSync(join(ROOT, p)) && statSync(join(ROOT, p)).size > 200;

function rounds() {
  return readdirSync(ROOT)
    .filter((d) => /^round-\d\d$/.test(d) && statSync(join(ROOT, d)).isDirectory())
    .sort();
}

// The verdict block of one challenger file: the text code block under "## Verdicts".
function verdicts(path) {
  const text = read(path);
  const at = text.lastIndexOf("## Verdicts");
  if (at < 0) return { ok: false, why: `${path}: no "## Verdicts" heading` };
  const block = text.slice(at).match(/```text\n([\s\S]*?)```/);
  if (!block) return { ok: false, why: `${path}: no text code block under "## Verdicts"` };
  const items = [];
  let blocking = null;
  let finalVerdict = null;
  for (const raw of block[1].split("\n")) {
    const line = raw.trim();
    if (!line) continue;
    let m;
    if ((m = line.match(new RegExp(`^VERDICT (${SLUG.source}) (ACCEPT|REVISE|REJECT)( NONTRIVIAL)?$`)))) {
      items.push({ slug: m[1], verdict: m[3], nontrivial: Boolean(m[4]) && m[3] === "ACCEPT" });
    } else if ((m = line.match(/^BLOCKING (\d+)$/))) {
      if (blocking !== null) return { ok: false, why: `${path}: two BLOCKING lines` };
      blocking = Number(m[1]);
    } else if ((m = line.match(/^FINAL (ACCEPT|REVISE)$/))) {
      finalVerdict = m[1];
    } else {
      return { ok: false, why: `${path}: unparseable verdict line "${line}"` };
    }
  }
  if (blocking === null) return { ok: false, why: `${path}: no BLOCKING line` };
  if (items.length === 0) return { ok: false, why: `${path}: no VERDICT line` };
  return { ok: true, items, blocking, finalVerdict };
}

// Every challenger file in order, then the final audit if it exists.
function verdictFiles(withAudit) {
  const files = rounds().map((r) => join(r, "challenger.md")).filter((p) => existsSync(join(ROOT, p)));
  if (withAudit && existsSync(join(ROOT, "final/audit.md"))) files.push("final/audit.md");
  return files;
}

function latestVerdicts(withAudit) {
  const latest = new Map();
  for (const f of verdictFiles(withAudit)) {
    const v = verdicts(f);
    if (!v.ok) { fail.push(v.why); continue; }
    for (const it of v.items) latest.set(it.slug, { ...it, file: f });
  }
  return latest;
}

function structure() {
  const rs = rounds();
  if (rs[0] !== "round-00") fail.push("round-00 is missing");
  rs.forEach((r, i) => {
    if (r !== `round-${String(i).padStart(2, "0")}`) fail.push(`round folders skip a number at ${r}`);
    if (!nonEmpty(join(r, "challenger.md"))) fail.push(`${r}/challenger.md is missing or empty`);
    if (r !== "round-00" && !nonEmpty(join(r, "builder.md"))) fail.push(`${r}/builder.md is missing or empty`);
    if (existsSync(join(ROOT, r, "challenger.md"))) {
      const v = verdicts(join(r, "challenger.md"));
      if (!v.ok) fail.push(v.why);
    }
  });
  const review = rs.filter((r) => r !== "round-00").length;
  if (review < MIN_REVIEW_ROUNDS) fail.push(`${review} review rounds, at least ${MIN_REVIEW_ROUNDS} required`);
  const readme = read("README.md");
  for (const r of rs) {
    if (!new RegExp(`^\\| ${r} \\|`, "m").test(readme)) fail.push(`README round log has no line for ${r}`);
  }
  if (!nonEmpty("theory/CURRENT.md")) fail.push("theory/CURRENT.md is missing or empty");
  return `STRUCTURE OK rounds=${rs.length}`;
}

function convergence() {
  const files = verdictFiles(false);
  if (files.length < 3) fail.push("fewer than three challenger files");
  const last = files.slice(-2).map((f) => verdicts(f));
  for (const v of last) if (!v.ok) fail.push(v.why);
  if (last.length === 2 && last.every((v) => v.ok)) {
    if (last[1].blocking !== 0) fail.push(`latest challenger file has BLOCKING ${last[1].blocking}`);
    const defsIn = (v) => v.items.filter((it) => it.slug.startsWith("def-"));
    for (const [i, v] of last.entries()) {
      const d = defsIn(v);
      if (d.length === 0) fail.push(`${files[files.length - 2 + i]} judges no definition`);
      for (const it of d) if (it.verdict !== "ACCEPT") fail.push(`${files[files.length - 2 + i]}: ${it.slug} is ${it.verdict}`);
    }
  }
  const latest = latestVerdicts(false);
  const defs = [...latest.values()].filter((it) => it.slug.startsWith("def-"));
  for (const d of defs) if (d.verdict !== "ACCEPT") fail.push(`definition ${d.slug} stands at ${d.verdict}`);
  const results = [...latest.values()].filter((it) => !it.slug.startsWith("def-"));
  const accepted = results.filter((it) => it.verdict === "ACCEPT");
  const nontrivial = accepted.filter((it) => it.nontrivial);
  if (accepted.length < MIN_ACCEPTED) fail.push(`${accepted.length} results accepted, at least ${MIN_ACCEPTED} required`);
  if (nontrivial.length < MIN_NONTRIVIAL) fail.push(`${nontrivial.length} NONTRIVIAL results, at least ${MIN_NONTRIVIAL} required`);
  return `CONVERGENCE OK accepted=${accepted.length} nontrivial=${nontrivial.length}`;
}

function finalDoc() {
  const p = "final/learning-oracle-theory.md";
  if (!nonEmpty(p)) { fail.push(`${p} is missing or empty`); return ""; }
  const text = read(p);
  const tags = [...text.matchAll(new RegExp(`\\[(${SLUG.source})\\]`, "g"))].map((m) => m[1]);
  const slugs = [...new Set(tags)];
  const latest = latestVerdicts(true);
  for (const s of slugs) {
    const v = latest.get(s);
    if (!v) fail.push(`${s} appears in the final document but no challenger judged it`);
    else if (v.verdict !== "ACCEPT") fail.push(`${s} stands at ${v.verdict} in ${v.file}`);
  }
  // A theorem block runs from its heading to the next heading of the same or higher level.
  const blocks = text.split(/\n(?=#{2,3} )/).filter((b) => /^#{2,3} .*\[thm-/.test(b));
  if (blocks.length < MIN_FINAL_THEOREMS) fail.push(`${blocks.length} theorem sections, at least ${MIN_FINAL_THEOREMS} required`);
  let nontrivial = 0;
  for (const b of blocks) {
    const slug = b.match(new RegExp(`\\[(thm-[a-z0-9-]+)\\]`))[1];
    if (!/Without the oracle/.test(b)) fail.push(`${slug}: no "Without the oracle" paragraph`);
    if (!/\bProof\b/.test(b)) fail.push(`${slug}: no proof`);
    if (latest.get(slug)?.nontrivial) nontrivial += 1;
  }
  if (nontrivial < MIN_FINAL_NONTRIVIAL) fail.push(`${nontrivial} NONTRIVIAL theorems in the final document, at least ${MIN_FINAL_NONTRIVIAL} required`);
  if (!/^## Definitions/m.test(text)) fail.push("no \"## Definitions\" section");
  return `FINAL OK theorems=${blocks.length} nontrivial=${nontrivial} items=${slugs.length}`;
}

function audit() {
  const p = "final/audit.md";
  if (!nonEmpty(p)) { fail.push(`${p} is missing or empty`); return ""; }
  const v = verdicts(p);
  if (!v.ok) { fail.push(v.why); return ""; }
  if (v.finalVerdict !== "ACCEPT") fail.push(`audit verdict is ${v.finalVerdict ?? "missing"}`);
  if (v.blocking !== 0) fail.push(`audit has BLOCKING ${v.blocking}`);
  const text = read("final/learning-oracle-theory.md");
  const slugs = [...new Set([...text.matchAll(new RegExp(`\\[(${SLUG.source})\\]`, "g"))].map((m) => m[1]))];
  const judged = new Set(v.items.map((it) => it.slug));
  for (const s of slugs) if (!judged.has(s)) fail.push(`audit does not judge ${s}`);
  for (const it of v.items) if (it.verdict !== "ACCEPT") fail.push(`audit: ${it.slug} is ${it.verdict}`);
  return `AUDIT OK items=${v.items.length}`;
}

const modes = { structure, convergence, final: finalDoc, audit };
const mode = process.argv[2];
if (!modes[mode]) { console.error(`usage: verify.mjs ${Object.keys(modes).join(" | ")}`); process.exit(2); }
const marker = modes[mode]();
if (fail.length) {
  console.error(`${mode} failed:`);
  for (const f of fail) console.error(`  ${f}`);
  process.exit(1);
}
console.log(marker);
