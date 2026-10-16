"""Trend tables of the 2026-10-16 sweep, computed from lib/literature/ledger.csv.

Run from the repository root. Writes two CSVs under lib/reports/src/data/.
A row is one coalition of one paper. SoK rows are excluded. Year is the venue
year in paper.venue. A row counts as deviating when its `sets` cell names any
choice other than queries. Mechanisms are matched by keyword in `protection`.
The adaptive share uses only deviating rows whose evaluation.adaptive says yes or no.
"""
import csv, re
from collections import Counter, defaultdict
STEM = "2026-10-16-halil-multi-party-learning-sweep"
rows = list(csv.DictReader(open("lib/literature/ledger.csv")))
def kv(cell, k):
    m = re.search(r'(?:^|;\s*)' + re.escape(k) + r'=([^;]*)', cell)
    return m.group(1).strip().lower() if m else ""
def deviating(sets):
    s = sets.strip().lower()
    if s in ("", "none", "n/a"): return False
    parts = [p.strip() for p in s.split(";") if p.strip()]
    return any(not p.startswith("queries") for p in parts)
MECH = [("HE", ("he@", "homomorphic", "ckks", "bfv", "threshold he")),
        ("DP", ("dp ", "dp@", "differential", "ldp")),
        ("SecAgg", ("secure aggregation", "secagg")),
        ("MPC", ("mpc", "secret shar")),
        ("ZK", ("zk", "zero-knowledge", "snark")),
        ("TEE", ("tee", "sgx", "trustzone"))]
tot = Counter(); dev = Counter(); mech = defaultdict(Counter); proven = Counter()
ad_yes = Counter(); ad_no = Counter()
for r in rows:
    if "sok" in kv(r["paper"], "type"): continue
    m = re.search(r'(20\d\d)', kv(r["paper"], "venue"))
    if not m or m.group(1) < "2023": continue
    y = m.group(1); tot[y] += 1
    d = deviating(r["sets"]); dev[y] += d
    p = r["protection"].lower()
    for name, keys in MECH:
        mech[y][name] += any(k in p for k in keys)
    e = kv(r["evidence"], "status"); proven[y] += ("proven" in e or "sketch" in e)
    a = kv(r["evaluation"], "adaptive")
    if d and a.startswith("yes"): ad_yes[y] += 1
    if d and a.startswith("no"): ad_no[y] += 1
years = sorted(tot)
pct = lambda a, b: f"{100*a/b:.0f}" if b else "-"
with open(f"lib/reports/src/data/{STEM}-trends.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["Year", "Rows", "Deviating"] + [n for n, _ in MECH] + ["Proven"])
    for y in years:
        w.writerow([y, tot[y], pct(dev[y], tot[y])] + [pct(mech[y][n], tot[y]) for n, _ in MECH] + [pct(proven[y], tot[y])])
with open(f"lib/reports/src/data/{STEM}-adaptive.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["Year", "Deviating rows", "Adaptive", "Not adaptive", "Adaptive share"])
    for y in years:
        w.writerow([y, dev[y], ad_yes[y], ad_no[y], pct(ad_yes[y], ad_yes[y] + ad_no[y])])
print(open(f"lib/reports/src/data/{STEM}-trends.csv").read()); print(open(f"lib/reports/src/data/{STEM}-adaptive.csv").read())
