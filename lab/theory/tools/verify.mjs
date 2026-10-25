#!/usr/bin/env node
// lab/theory/tools/verify.mjs <context|folder|spaces|convergence|integration>
// Checks the theory workspace against lab/theory/CONTEXT.md. Each mode prints
// one success line (CONTEXT OK, FOLDER OK, ...) and exits 0, or lists every
// failure and exits 1. Read-only: it never writes a file.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const THEORY = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const REPO = path.dirname(path.dirname(THEORY));
const OUT = path.join(REPO, 'lib', 'theory');
const SPACES = ['statistical-limits', 'computational-limits', 'oracle-and-measurement'];
const MODEL = { astra: ['gpt-6-astra'], argon: ['gemini-4-argon-high', 'gemini-4-argon-medium'] };
const TEX_ARTIFACT = /\.(aux|log|out|toc|fls|fdb_latexmk|synctex\.gz|bbl|blg|lof|lot|nav|snm|vrb|dvi|xdv)$/;

const fails = [];
const fail = (m) => fails.push(m);
const read = (p) => (fs.existsSync(p) ? fs.readFileSync(p, 'utf8') : null);
const rel = (p) => path.relative(REPO, p);

function walk(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    const p = path.join(dir, e.name);
    return e.isDirectory() ? walk(p) : [p];
  });
}

function rounds(space) {
  const dir = path.join(THEORY, 'spaces', space);
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter((n) => /^round-\d\d$/.test(n)).sort().map((n) => path.join(dir, n));
}

// The verdict block of one discussant file: {verdicts: {slug: V}, blocking: n} or null.
function verdicts(file) {
  const t = read(file) || '';
  const i = t.lastIndexOf('## Verdicts');
  if (i < 0) return null;
  const m = t.slice(i).match(/```text\n([\s\S]*?)```/);
  if (!m) return null;
  const out = { verdicts: {}, blocking: null };
  for (const line of m[1].split('\n').map((l) => l.trim()).filter(Boolean)) {
    let v;
    if ((v = line.match(/^VERDICT ([a-z]+-[a-z0-9-]+) (ACCEPT|REVISE|REJECT)$/))) out.verdicts[v[1]] = v[2];
    else if ((v = line.match(/^BLOCKING (\d+)$/))) out.blocking = out.blocking === null ? Number(v[1]) : NaN;
    else return null;
  }
  if (!Object.keys(out.verdicts).length || !Number.isInteger(out.blocking)) return null;
  return out;
}

function discussantFiles(round) {
  return fs.readdirSync(round).filter((n) => /^discussant-(astra|argon)\.md$/.test(n)).sort().map((n) => path.join(round, n));
}

function csvRows() {
  const t = read(path.join(THEORY, 'discussants.csv')) || '';
  return t.split('\n').slice(1).filter(Boolean).map((l) => {
    const [date, who, model, prompt, output, exit, tokens] = l.split(',');
    return { date, who, model, prompt, output, exit, tokens };
  });
}

// Objects of the booklet sources: [{kind, slug, status, file}].
function bookletObjects() {
  const objs = [];
  const files = [path.join(THEORY, 'booklet', 'booklet.tex'), ...walk(path.join(THEORY, 'booklet', 'chapters'))];
  for (const f of files.filter((p) => p.endsWith('.tex'))) {
    const t = read(f);
    const re = /\\begin\{(definition|lemma|theorem|proposition|conjecture|borrowed)\}([\s\S]*?)\\end\{\1\}/g;
    let m;
    while ((m = re.exec(t))) {
      const slug = (m[2].match(/\\blabel\{([^}]+)\}/) || [])[1];
      const status = (m[2].match(/\\status\{([^}]+)\}/) || [])[1];
      objs.push({ kind: m[1], slug, status, file: f });
    }
  }
  return objs;
}

function context() {
  for (const f of ['CONTEXT.md', 'STATE.md']) if (!read(path.join(THEORY, f))) fail(`lab/theory/${f} is missing`);
  const state = read(path.join(THEORY, 'STATE.md')) || '';
  if (state.split('\n').length > 81) fail('STATE.md is longer than 80 lines');
  if (!/^updated: \d{4}-\d\d-\d\d$/m.test(state)) fail('STATE.md has no "updated: YYYY-MM-DD" line');
  for (const f of ['CLAUDE.md', 'AGENTS.md']) {
    if (!(read(path.join(REPO, f)) || '').includes('lab/theory/CONTEXT.md')) fail(`${f} has no pointer to lab/theory/CONTEXT.md`);
  }
  for (const s of SPACES) {
    const t = read(path.join(THEORY, 'spaces', s, 'README.md'));
    if (!t) { fail(`space ${s} has no README.md`); continue; }
    for (const h of ['## Question', '## Scope', '## Where to start', '## Round log']) if (!t.includes(h)) fail(`${s}/README.md lacks "${h}"`);
    const owner = (t.match(/^Owner: (.*)$/m) || [])[1] || '';
    if (!owner || owner.startsWith('set by the integrator')) fail(`${s}/README.md names no owner session`);
  }
  if (!fails.length) console.log('CONTEXT OK');
}

function folder() {
  if (!fs.existsSync(OUT)) fail('lib/theory/ does not exist');
  const names = fs.existsSync(OUT) ? fs.readdirSync(OUT).filter((n) => n !== '.DS_Store') : [];
  for (const n of names) if (!n.endsWith('.pdf') || fs.statSync(path.join(OUT, n)).isDirectory()) fail(`lib/theory/${n} is not a PDF`);
  if (!names.includes('booklet.pdf')) fail('lib/theory/booklet.pdf is missing');
  for (const p of [...walk(THEORY), ...walk(OUT)]) {
    if (TEX_ARTIFACT.test(p)) fail(`TeX build artifact ${rel(p)}`);
    if (p.endsWith('.tex') && !p.startsWith(path.join(THEORY, 'booklet') + path.sep)) fail(`.tex outside lab/theory/booklet/: ${rel(p)}`);
  }
  const readings = walk(path.join(THEORY, 'readings')).filter((p) => p.endsWith('.md')).map((p) => path.basename(p, '.md'));
  for (const r of readings) {
    if (!/^\d{4}-\d\d-\d\d-[a-z0-9]+(-[a-z0-9]+)*$/.test(r)) fail(`reading ${r}.md breaks the name rule`);
    if (!names.includes(`${r}.pdf`)) fail(`reading ${r}.md has no lib/theory/${r}.pdf`);
  }
  for (const n of names.filter((n) => n.endsWith('.pdf') && !['booklet.pdf', 'booklet-changes.pdf'].includes(n))) {
    if (!readings.includes(n.slice(0, -4))) fail(`lib/theory/${n} has no source in lab/theory/readings/`);
  }
  if (names.includes('booklet.pdf')) {
    const built = fs.statSync(path.join(OUT, 'booklet.pdf')).mtimeMs;
    for (const p of walk(path.join(THEORY, 'booklet'))) if (fs.statSync(p).mtimeMs > built) fail(`${rel(p)} changed after the last booklet build`);
  }
  if (!fails.length) console.log('FOLDER OK');
}

function spaces() {
  const rows = csvRows();
  const used = new Set();
  for (const s of SPACES) {
    const rs = rounds(s);
    const readme = read(path.join(THEORY, 'spaces', s, 'README.md')) || '';
    if (rs.length < 2) fail(`${s}: ${rs.length} rounds, the milestone needs round-00 and at least one more`);
    rs.forEach((r, i) => {
      const name = path.basename(r);
      if (name !== `round-${String(i).padStart(2, '0')}`) fail(`${s}: rounds are not numbered from 00 without gaps at ${name}`);
      if (!readme.includes(name)) fail(`${s}/README.md round log does not mention ${name}`);
      if (!(read(path.join(r, 'builder.md')) || '').match(/^### [a-z]+-[a-z0-9-]+: /m)) fail(`${s}/${name}/builder.md is missing or has no object heading`);
      const summary = read(path.join(r, 'summary.md'));
      if (!summary || !summary.includes('## For the registers')) fail(`${s}/${name}/summary.md is missing or lacks "## For the registers"`);
      const ds = discussantFiles(r);
      if (!ds.length) fail(`${s}/${name} has no discussant file`);
      if (ds.length > (i === rs.length - 1 ? 2 : 1)) fail(`${s}/${name} spends ${ds.length} discussant calls, over the budget`);
      for (const d of ds) {
        const who = path.basename(d).match(/discussant-(\w+)\.md/)[1];
        used.add(who);
        const head = (read(d) || '').slice(0, 300);
        if (!MODEL[who].some((m) => head.includes(`model: ${m}`))) fail(`${rel(d)} header does not name ${MODEL[who].join(' or ')}`);
        if (!fs.existsSync(path.join(r, `prompt-${who}.md`))) fail(`${rel(d)} has no prompt-${who}.md`);
        if (!verdicts(d)) fail(`${rel(d)} has no well-formed verdict block`);
        if (!rows.some((x) => x.output === rel(d) && x.exit === '0' && MODEL[who].includes(x.model))) fail(`${rel(d)} has no exit-0 row in discussants.csv`);
      }
      if (i > 0 && ds.length === 1) {
        const prev = discussantFiles(rs[i - 1]);
        if (prev.length === 1 && path.basename(prev[0]) === path.basename(ds[0]) && !/usage limit|fallback|fell back/i.test(summary || '')) {
          fail(`${s}/${name} repeats the discussant of the round before without saying why in its summary`);
        }
      }
    });
  }
  for (const who of Object.keys(MODEL)) if (!used.has(who)) fail(`no round of the milestone used ${who}`);
  if (!fails.length) console.log('SPACES OK');
}

function lastBlocking(s) {
  const rs = rounds(s);
  if (!rs.length) return null;
  const vs = discussantFiles(rs[rs.length - 1]).map(verdicts);
  if (!vs.length || vs.some((v) => !v)) return null;
  return Math.max(...vs.map((v) => v.blocking));
}

function convergence() {
  for (const s of SPACES) {
    const b = lastBlocking(s);
    if (b === null) fail(`${s}: last round has no well-formed verdict`);
    else if (b !== 0) fail(`${s}: last round ends with BLOCKING ${b}`);
  }
  if (!fails.length) console.log('CONVERGENCE OK');
}

// A slug is eligible for status accepted when its latest verdict in the space is
// ACCEPT from every discussant of that round, and either that round or the
// space's last round has BLOCKING 0, so no blocking challenge stays open on it.
function eligible() {
  const out = new Map();
  for (const s of SPACES) {
    const converged = lastBlocking(s) === 0;
    const latest = new Map();
    for (const r of rounds(s)) {
      const vs = discussantFiles(r).map(verdicts).filter(Boolean);
      const slugs = new Set(vs.flatMap((v) => Object.keys(v.verdicts)));
      for (const slug of slugs) {
        const all = vs.filter((v) => slug in v.verdicts);
        const ok = all.every((v) => v.verdicts[slug] === 'ACCEPT') && (converged || vs.every((v) => v.blocking === 0));
        latest.set(slug, { ok, where: `${s}/${path.basename(r)}` });
      }
    }
    for (const [slug, v] of latest) if (v.ok) out.set(slug, v.where);
  }
  return out;
}

function integration() {
  const objs = bookletObjects();
  const bySlug = new Map(objs.map((o) => [o.slug, o]));
  const ok = eligible();
  const legacy = read(path.join(REPO, 'sink', '2026-10-16-formal-tuning', 'final', 'learning-oracle-theory.md')) || '';
  // An ACCEPT on a lem, thm, prop or conj may accept its refutation, so refuted is a fitting status too.
  const want = { def: ['accepted', 'checked'], lem: ['accepted', 'checked', 'refuted'], thm: ['accepted', 'checked', 'refuted'], prop: ['accepted', 'checked', 'refuted'], conj: ['open', 'accepted', 'checked', 'refuted'], fact: ['borrowed'] };
  for (const [slug, where] of ok) {
    const prefix = slug.split('-')[0];
    if (prefix === 'fact' || !(prefix in want)) continue; // facts enter the booklet when a merged object uses them
    const o = bySlug.get(slug);
    if (!o) fail(`${slug}, accepted in ${where}, is not in the booklet`);
    else if (!want[prefix].includes(o.status)) fail(`${slug}, accepted in ${where}, has status ${o.status} in the booklet`);
  }
  for (const o of objs) {
    if (o.status !== 'accepted') continue;
    if (!ok.has(o.slug) && !legacy.includes(o.slug)) fail(`${o.slug} has status accepted in the booklet with no accepting round behind it`);
  }
  const history = read(path.join(THEORY, 'booklet', 'chapters', 'history.tex')) || '';
  const state = read(path.join(THEORY, 'STATE.md')) || '';
  for (const s of SPACES) {
    const rs = rounds(s).map((r) => path.basename(r));
    for (const r of rs) if (!history.includes(`${s}/${r}`)) fail(`history.tex does not record ${s}/${r}`);
    const row = state.split('\n').find((l) => l.startsWith(`| \`${s}\``)) || '';
    const last = rs[rs.length - 1] || 'none';
    if (!row.includes(last)) fail(`STATE.md row for ${s} does not name its last round ${last}`);
  }
  const pdf = path.join(OUT, 'booklet.pdf');
  if (fs.existsSync(pdf)) {
    const built = fs.statSync(pdf).mtimeMs;
    for (const s of SPACES) for (const r of rounds(s)) {
      const sm = path.join(r, 'summary.md');
      if (fs.existsSync(sm) && fs.statSync(sm).mtimeMs > built) fail(`${rel(sm)} is newer than the booklet build`);
    }
  }
  if (!fails.length) console.log(`INTEGRATION OK eligible=${ok.size}`);
}

const mode = process.argv[2];
const modes = { context, folder, spaces, convergence, integration };
if (!modes[mode]) { console.error(`usage: verify.mjs <${Object.keys(modes).join('|')}>`); process.exit(2); }
modes[mode]();
if (fails.length) { console.error(fails.map((f) => `FAIL ${f}`).join('\n')); process.exit(1); }
