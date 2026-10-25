"""Tables of the papers of the 2026-10-16 sweep and of how its papers state their adversaries.

Run from the repository root. Reads lib/literature/screening.csv and
lib/literature/ledger.csv, writes one CSV per table and a facts CSV under
lib/reports/src/data/, and renders each table with the research skill's
mktable.py into lib/reports/src/figures/. HE-OFT (KSK26) is left out, because
the study covers the field and HE-OFT is the group's own paper.

Counting rules, stated once.
- A ledger row is one coalition of one paper. A paper-level count counts a
  paper once when any of its rows matches.
- A venue and a year come from the venue named in the paper's ledger row,
  which the coder took from the note.
- A row sets nothing when its `sets` cell begins with "none" or "n/a". It is
  deviating when it sets anything else beyond queries.
- A row names a mechanism when the mechanism field of `protection` matches HE,
  DP, secure aggregation, MPC, ZK or TEE as a word.
- A row faces a check when its `checks` cell is not "none" or "n/a".
- A value was inferred by the coder, and not stated by the paper, when its
  keyword appears in the row's `inferred` cell.
- Each row falls in one of seven templates by its role, its choices and its
  goal, as `template` below defines.
"""
import csv
import os
import re
import subprocess
from collections import Counter, defaultdict

from scipy.stats import fisher_exact

STEM = "2026-10-16-halil-swept-papers-and-threat-models"
DATA = f"lib/reports/src/data/{STEM}"
screen = [s for s in csv.DictReader(open("lib/literature/screening.csv")) if s["key"] != "KSK26"]
rows = [r for r in csv.DictReader(open("lib/literature/ledger.csv")) if r["key"] != "KSK26"]
facts = {}


def kv(cell, k):
    m = re.search(r"(?:^|;\s*)" + re.escape(k) + r"=([^;]*)", cell)
    return m.group(1).strip() if m else ""


def write(name, header, body):
    with open(f"{DATA}-{name}.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(body)


VENUES = [("IEEE S&P", r"s&p"), ("USENIX Security", r"usenix"), ("CCS", r"\bccs\b"),
          ("NDSS", r"ndss"), ("PoPETs", r"popets|pets"), ("CRYPTO", r"^crypto|\bcrypto \d"),
          ("EUROCRYPT", r"eurocrypt"), ("ASIACRYPT", r"asiacrypt"), ("NeurIPS", r"neurips"),
          ("ICML", r"icml"), ("ICLR", r"iclr")]


def venue(text):
    t = text.lower()
    for name, p in VENUES:
        if re.search(p, t):
            return name
    return "other"


def community(v):
    if v in ("CRYPTO", "EUROCRYPT", "ASIACRYPT"):
        return "cryptography"
    if v in ("NeurIPS", "ICML", "ICLR"):
        return "learning"
    return "security"


def year(text):
    m = re.search(r"(20\d\d)", text)
    return m.group(1) if m else ""


# One record per coded paper, from its first ledger row, and all its rows.
paper_rows = defaultdict(list)
for r in rows:
    paper_rows[r["key"]].append(r)
papers = {k: v[0] for k, v in paper_rows.items()}
pvenue = {k: venue(kv(r["paper"], "venue")) for k, r in papers.items()}
pyear = {k: year(kv(r["paper"], "venue")) for k, r in papers.items()}

# ---------------------------------------------------------------- the search
STATUS = ["dropped at screening", "dropped after reading", "no accessible PDF", "placed"]
funnel = defaultdict(Counter)
for s in screen:
    funnel[venue(s["venue"])][s["status"]] += 1
YEARS = ["2023", "2024", "2025", "2026"]
coded = defaultdict(Counter)
for k in papers:
    y = pyear[k]
    coded[pvenue[k]][y if y in YEARS else "earlier"] += 1
body = []
for v, _ in VENUES:
    f = funnel[v]
    body.append([v, sum(f.values()), f["dropped at screening"], f["dropped after reading"],
                 f["no accessible PDF"], sum(coded[v].values())] + [coded[v][y] for y in YEARS] + [coded[v]["earlier"]])
tot = ["all eleven"] + [sum(b[i] for b in body) for i in range(1, len(body[0]))]
write("search", ["Venue", "Recorded", "Dropped", "Read out", "No PDF",
                 "Coded"] + YEARS + ["Earlier"], body + [tot])
facts.update(Candidates=tot[1], DroppedScreen=tot[2], DroppedRead=tot[3], NoPDF=tot[4],
             Papers=tot[5], Rows=len(rows), Earlier=tot[-1])
assert facts["Papers"] == len(papers), "screening and ledger disagree on the coded papers"

DROP = [
    ("one party trains, or one trained model is attacked",
     r"single|one (data owner|user|model|client|party|trainer|data holder|device|provider)|on one model|"
     r"central (trainer|dp)|centrali[sz]ed|outsourced|not multi-party|no second"),
    ("no adversary, or privacy and security only as motivation",
     r"no adversary|no attack|no security|no threat|efficiency|only as (a )?motivation|side constraint|"
     r"incentive|contribution evaluation|heterogeneity|framework, no|no privacy|not a security"),
    ("no model is trained",
     r"trains no model|no model (is )?trained|no model training|not model training|mean estimation|analytics|"
     r"no learning|pure exploration|names no model training|aggregate measurement"),
    ("inference or serving only", r"inference|serving|not training|no training"),
    ("cryptography not tied to learning", r"not tied to learning|generic|threshold fhe|key generation"),
    ("outside the main track", r"poster|workshop"),
]
drops = Counter()
for s in screen:
    if s["status"] != "dropped at screening":
        continue
    t = s["reason"].lower()
    drops[next((n for n, p in DROP if re.search(p, t)), "other reasons")] += 1
write("drops", ["Reason given at screening", "Papers"],
      [[n, drops[n]] for n, _ in DROP] + [["other reasons", drops["other reasons"]]])
facts["DropOther"] = drops["other reasons"]

# ---------------------------------------------------------------- the papers
def kind(r):
    t = kv(r["paper"], "type").lower()
    if "," in t or " plus " in t:
        return "two kinds or more"
    return t.split(" ")[0].replace("sok", "SoK") or "unstated"


SETTINGS = [("secure aggregation", r"secure aggregation"),
            ("multiparty or threshold HE", r"multiparty he|threshold he|two-server he"),
            ("MPC training", r"\bmpc\b"),
            ("vertical or split learning", r"vertical|split"),
            ("decentralized learning", r"decentrali[sz]ed|peer|gossip"),
            ("federated fine-tuning", r"fine-tuning"),
            ("horizontal FL", r"horizontal|\bfl\b|federated")]


def setting(r):
    t = kv(r["paper"], "setting").lower()
    return next((n for n, p in SETTINGS if re.search(p, t)), "other")


ROLES = ["server", "clients", "server with clients", "querier"]


def role(r):
    x = kv(r["adversary"], "role").lower()
    has = lambda *w: any(t in x for t in w)
    srv = has("server", "aggregator", "committee", "decryptor", "evaluator", "verifier", "coordinator")
    cli = has("client", "party", "parties", "user", "owner", "participant", "worker",
              "device", "node", "peer", "holder", "silo")
    if srv and cli:
        return "server with clients"
    if srv:
        return "server"
    if cli:
        return "clients"
    if has("querier", "eavesdropper", "observer", "third", "external", "analyst", "consumer"):
        return "querier"
    return "other"


CHOICES = ["data argument", "model argument", "class argument", "learning function",
           "merge", "node output", "ciphertext", "release"]


def choices(r):
    s = r["sets"].lower()
    if s.startswith("none") or s.startswith("n/a"):
        return set()
    return {w for w in CHOICES if w in s}


def goals(r):
    t = kv(r["goal"], "type").lower()
    return {g for g in ["distinguish", "invert", "steer", "other"] if g in t}


MECHANISMS = [("HE", r"\b(threshold he|multiparty he|he|fhe|tfhe|ckks|bfv|bgv|homomorphic|paillier|rlwe he)\b"),
              ("DP", r"\bdp\b|differential"),
              ("secure aggregation", r"secure aggregation"),
              ("MPC", r"\bmpc\b|secret shar"),
              ("ZK", r"\bzk\b|zero-knowledge|snark"),
              ("TEE", r"\btee\b|\bsgx\b")]


def mechanisms(r):
    m = kv(r["protection"], "mechanism@node").lower()
    return {n for n, p in MECHANISMS if re.search(p, m)}


def has_check(r):
    c = r["checks"].strip().lower()
    return not (c == "" or c.startswith("none") or c.startswith("n/a"))


def inferred(r, key):
    return key in r["inferred"].lower()


def proven(r):
    s = kv(r["evidence"], "status").lower()
    return "proven" in s or "sketch" in s


def adaptive(r):
    a = kv(r["evaluation"], "adaptive").lower()
    return "yes" if a.startswith("yes") else "no" if a.startswith("no") else ""


LM = r"gpt|llama|bert|roberta|\bt5\b|\bopt\b|mistral|qwen|gemma|\bvit\b|clip|transformer|phi-|bloom|pythia|falcon"


def evaluation_marks(k):
    rs = paper_rows[k]
    ds = " ".join(kv(r["evaluation"], "datasets").lower() for r in rs)
    lm = " ".join(kv(r["evaluation"], "largest_model").lower() for r in rs)
    marks = set()
    if re.search(r"(?<![a-z-])mnist|cifar-?10(?!0)", ds):
        marks.add("MNIST or CIFAR-10")
    if re.search(LM, lm):
        marks.add("a transformer")
    if any("pretrained" in kv(r["model"], "init").lower() for r in rs):
        marks.add("a public pretrained model")
    if any(kv(r["data"], "space").lower().startswith("token") for r in rs):
        marks.add("token sequences")
    if all(kv(r["evaluation"], "datasets").lower() in ("", "n/a", "none") for r in rs):
        marks.add("no experiment")
    return marks


panels = []
panels.append(("Kind", Counter(kind(papers[k]) for k in papers)))
panels.append(("Setting", Counter(setting(papers[k]) for k in papers)))
prot = Counter()
for k in papers:
    ms = set().union(*(mechanisms(r) for r in paper_rows[k]))
    prot.update(ms or {"none named"})
panels.append(("Protection", prot))
co = Counter()
for k in papers:
    co.update({role(r) for r in paper_rows[k]} - {"other"})
co = Counter({{"server": "the server alone", "clients": "clients alone",
               "server with clients": "the server with clients",
               "querier": "a querier or eavesdropper"}[n]: c for n, c in co.items()})
panels.append(("Coalition", co))
go = Counter()
for k in papers:
    go.update(set().union(*(goals(r) for r in paper_rows[k])))
panels.append(("Goal", go))
ev = Counter()
for k in papers:
    ev.update(evaluation_marks(k))
panels.append(("Evaluation uses", ev))


def side_by_side(ps):
    lists = [[(n, c) for n, c in p.most_common()] for _, p in ps]
    height = max(len(x) for x in lists)
    out = []
    for i in range(height):
        line = []
        for x in lists:
            line += [x[i][0], x[i][1]] if i < len(x) else ["~", "~"]
        out.append(line)
    return out


head = []
for name, _ in panels[:3]:
    head += [name, "Papers"]
write("papers-a", head, side_by_side(panels[:3]))
head = []
for name, _ in panels[3:]:
    head += [name, "Papers"]
write("papers-b", head, side_by_side(panels[3:]))
facts.update(FL=sum(1 for k in papers if setting(papers[k]) in ("horizontal FL", "federated fine-tuning")),
             MnistCifar=ev["MNIST or CIFAR-10"], LMEval=ev["a transformer"],
             Pretrained=ev["a public pretrained model"], NoExperiment=ev["no experiment"],
             Defences=panels[0][1]["defence"], Protocols=panels[0][1]["protocol"], Attacks=panels[0][1]["attack"],
             NoProtection=prot["none named"])

# ---------------------------------------------------------------- trends
def deviating(r):
    return bool(choices(r))


trend = []
cnt = {}
for y in YEARS:
    ks = [k for k in papers if pyear[k] == y]
    n = len(ks)
    dev = sum(any(deviating(r) for r in paper_rows[k]) for k in ks)
    ms = Counter()
    for k in ks:
        ms.update(set().union(*(mechanisms(r) for r in paper_rows[k])))
    pr = sum(any(proven(r) for r in paper_rows[k]) for k in ks)
    cnt[y] = dict(n=n, dev=dev, HE=ms["HE"])
    trend.append([y, n, round(100 * dev / n)] + [round(100 * ms[m] / n) for m, _ in MECHANISMS]
                 + [round(100 * pr / n)])
write("trends", ["Year", "Papers", "Deviating"] + [m if m != "secure aggregation" else "SecAgg" for m, _ in MECHANISMS]
      + ["Proven"], trend)


def p_value(a, b, key):
    x, y = cnt[a], cnt[b]
    return fisher_exact([[x[key], x["n"] - x[key]], [y[key], y["n"] - y[key]]])[1]


facts.update(HEFirst=trend[0][3], HELast=trend[-1][3], HEp=f"{p_value('2023', '2026', 'HE'):.3f}",
             DevFirst=trend[0][2], DevLast=trend[-1][2], Devp=f"{p_value('2023', '2026', 'dev'):.2f}")

# ---------------------------------------------------------------- the templates
TEMPLATES = [
    ("S1", "server that reads what it receives"),
    ("S2", "server that sets what clients compute"),
    ("SC", "server with clients"),
    ("C1", "clients that set their updates"),
    ("C2", "clients that set only their data"),
    ("C3", "clients that read the model"),
    ("Q", "querier or eavesdropper"),
]
SERVER_SETS = {"model argument", "class argument", "learning function", "merge",
               "ciphertext", "node output", "release"}


def template(r):
    R, S, G = role(r), choices(r), goals(r)
    if R == "querier":
        return "Q"
    if R == "server with clients":
        return "SC"
    if R == "server":
        return "S2" if S & SERVER_SETS else "S1"
    if R == "clients":
        if G & {"steer", "other"}:
            return "C2" if S == {"data argument"} else "C1"
        return "C3"
    return "X"


SHORT = {"data argument": "data", "model argument": "model", "class argument": "class",
         "learning function": "learning function", "merge": "merge", "node output": "message",
         "ciphertext": "ciphertext", "release": "release", "nothing": "nothing"}


def top(counter, k=2, rename=None):
    rename = rename or {}
    return ", ".join(f"{rename.get(name, name)} {n}" for name, n in counter.most_common(k))


by_t = defaultdict(list)
for r in rows:
    by_t[template(r)].append(r)
body = []
for t, name in TEMPLATES:
    sub = by_t[t]
    ch = Counter(c for r in sub for c in (choices(r) or {"nothing"}))
    gl = Counter(g for r in sub for g in goals(r))
    ad = Counter(adaptive(r) for r in sub)
    body.append([name, len(sub), len({r["key"] for r in sub}), top(ch, rename=SHORT), top(gl),
                 sum(1 for r in sub if not mechanisms(r)), sum(has_check(r) for r in sub),
                 sum(proven(r) for r in sub), f"{ad['yes']} of {ad['yes'] + ad['no']}"])
write("templates", ["Template", "Rows", "Papers", "Choices", "Goals", "Bare",
                    "Check", "Proven", "Adaptive"], body)


def evidence_model(r):
    e = kv(r["evidence"], "model").split(" (")[0].split(",")[0].strip().lower()
    return e.upper() if e in ("dp", "uc") else e


body = []
for t, name in TEMPLATES:
    sub = by_t[t]
    ev_ = Counter(evidence_model(r) for r in sub if evidence_model(r) not in ("", "n/a", "none"))
    maj = Counter(kv(r["adversary"], "majority").lower().split(" ")[0].rstrip(",") for r in sub)
    stated = sum(1 for r in sub if not inferred(r, "adversary.corruption")
                 and kv(r["adversary"], "corruption").lower().startswith(("static", "adaptive")))
    stealth = sum(1 for r in sub if kv(r["stealth"], "status").lower().startswith(("required", "measured")))
    body.append([name, top(ev_), maj["honest"], maj["dishonest"], stated, stealth])
write("support", ["Template", "Evidence", "Honest", "Dishonest",
                  "Stated", "Stealth"], body)


def pct(a, b):
    return round(100 * a / b) if b else "~"


body = []
for c in ["security", "cryptography", "learning"]:
    sub = [r for r in rows if community(pvenue[r["key"]]) == c]
    f = Counter(kv(r["paper"], "formality").lower() for r in sub)
    fg = sum(n for k, n in f.items() if k.startswith(("ideal functionality", "game")))
    th = sum(n for k, n in f.items() if k.startswith("theorem"))
    pr = sum(n for k, n in f.items() if k.startswith(("prose", "taxonomy")))
    n = len(sub)
    body.append([c, n, len({r["key"] for r in sub}), pct(fg, n), pct(th, n), pct(pr, n),
                 pct(sum(inferred(r, "adversary.corruption") for r in sub), n),
                 pct(sum(inferred(r, "adversary.majority") for r in sub), n),
                 pct(sum(inferred(r, "sets") for r in sub), n),
                 pct(sum(inferred(r, "knows") for r in sub), n)])
write("communities", ["Community", "Rows", "Papers", "Formal", "Theorem", "Prose",
                      "Corruption", "Majority", "Choices", "Knowledge"], body)

ANCHORS = [
    ("server that reads what it receives", "DHWSGRC25 and CFMPV25, the two gradient-leakage SoKs (USENIX Security 2025). PDBMV24, DAGER (NeurIPS 2024)"),
    ("server that sets what clients compute", "PFA22, model inconsistency against secure aggregation (CCS 2022). ZSEEAB24, LOKI (S&P 2024). CFMPV26, detectability of active inversion (S&P 2026)"),
    ("server with clients", "BGLLMRY23, ACORN (USENIX Security 2023). JZDK25, AlphaFL (PoPETs 2025). REGB26, the integrity SoK (PoPETs 2026)"),
    ("clients that set their updates", "RT25, robustness against learning (S&P 2025). CKS24, attacking robust aggregation (S&P 2024). AGGPS23, the trilemma (ICML 2023)"),
    ("clients that set only their data", "SHKR22, poisoning in production (S&P 2022). BLGB26, stability bounds (ICML 2026)"),
    ("clients that read the model", "MCB24, attacks in decentralized learning (ICML 2024). YLGHP25, URVFL (NDSS 2025). RDGSM26, selective weight tampering (PoPETs 2026)"),
    ("querier or eavesdropper", "LLR23, passive membership inference in FL (ICLR 2023). ZLSGWYL26, membership defence (NDSS 2026)"),
]
write("anchors", ["Template", "Read first"], ANCHORS)

# ---------------------------------------------------------------- facts for the prose
steer = [r for r in rows if "steer" in goals(r)]
steer_ad = Counter(adaptive(r) for r in steer)


def word(term):
    t = term.lower()
    if "byzantine" in t:
        return "Byzantine"
    if any(x in t for x in ["semi-honest", "honest-but-curious", "honest but curious", "passive", "curious"]):
        return "semi-honest"
    if "malicious" in t or ("active" in t and "passive" not in t):
        return "malicious"
    return ""


mal_srv = [r for r in rows if role(r) == "server" and word(kv(r["adversary"], "term")) == "malicious"]
mal_cli = [r for r in rows if role(r) == "clients" and word(kv(r["adversary"], "term")) == "malicious"]
byz = [r for r in rows if role(r) == "clients" and word(kv(r["adversary"], "term")) == "Byzantine"]
srv_inv = [r for r in rows if template(r) in ("S1", "S2") and "invert" in goals(r)]
facts.update(
    Covered=sum(len(by_t[t]) for t, _ in TEMPLATES), Other=len(by_t["X"]),
    MalServer=len(mal_srv), MalServerModel=sum("model argument" in choices(r) for r in mal_srv),
    MalClients=len(mal_cli), MalClientsData=sum("data argument" in choices(r) for r in mal_cli),
    MalClientsOutput=sum("node output" in choices(r) for r in mal_cli),
    Byz=len(byz), ByzOutput=sum("node output" in choices(r) for r in byz),
    CorrInferred=sum(inferred(r, "adversary.corruption") for r in rows),
    CorrAdaptive=sum(kv(r["adversary"], "corruption").lower().startswith("adaptive") for r in rows),
    MajInferred=sum(inferred(r, "adversary.majority") for r in rows),
    Upd=len(by_t["C1"]), UpdNoMech=sum(1 for r in by_t["C1"] if not mechanisms(r)),
    Read=len(by_t["S1"]), ReadCheck=sum(has_check(r) for r in by_t["S1"]),
    SC=len(by_t["SC"]), SCCheck=sum(has_check(r) for r in by_t["SC"]),
    SCMech=sum(1 for r in by_t["SC"] if mechanisms(r)),
    Steer=len(steer), SteerNoStealth=sum(kv(r["stealth"], "status").lower().startswith("none") for r in steer),
    SteerAdYes=steer_ad["yes"], SteerAdStated=steer_ad["yes"] + steer_ad["no"],
    SteerBenign=sum(1 for r in steer if kv(r["knows"], "benign_updates").lower() not in ("", "n/a", "unstated")
                    and not inferred(r, "knows")),
    SrvInvert=len(srv_inv),
    SrvInvertArch=sum("architecture" in kv(r["knows"], "public_args").lower() for r in srv_inv),
    SrvInvertSurrogate=sum("surrogate" in kv(r["knows"], "own_data").lower() for r in srv_inv),
    Edges=sum(1 for r in rows if re.search(r"collapse|separation", r["edge"].lower())),
    C1Honest=sum(kv(r["adversary"], "majority").lower().startswith("honest") for r in by_t["C1"]),
    S2=len(by_t["S2"]),
    SCStated=sum(1 for r in by_t["SC"] if not inferred(r, "adversary.corruption")
                 and kv(r["adversary"], "corruption").lower().startswith(("static", "adaptive"))),
    NoProtRobust=sum(1 for k in papers if not set().union(*(mechanisms(r) for r in paper_rows[k]))
                     and kind(papers[k]) == "defence"
                     and any("robust" in kv(r["learning"], "merge").lower() or "robust" in r["checks"].lower()
                             or "robust" in r["paper"].lower() for r in paper_rows[k])),
    S2Stealth=sum(kv(r["stealth"], "status").lower().startswith(("required", "measured")) for r in by_t["S2"]),
    NoProtAttack=sum(1 for k in papers if not set().union(*(mechanisms(r) for r in paper_rows[k]))
                     and kind(papers[k]) == "attack"),
    NoProtDefence=sum(1 for k in papers if not set().union(*(mechanisms(r) for r in paper_rows[k]))
                      and kind(papers[k]) == "defence"),
    # Rows whose sets cell begins with "none" and that the deviating rule of
    # the 2026-10-16 sweep report counts as deviating.
    NoneDeviating=sum(1 for r in rows if r["sets"].strip().lower().startswith("none")
                      and r["sets"].strip().lower() != "none"),
)
write("facts", ["name", "value"], list(facts.items()))

# ---------------------------------------------------------------- render
def P(width):
    return r">{\raggedright\arraybackslash}p{" + width + "}"


MKTABLE = os.path.expanduser(os.environ.get("CLAUDE_SKILL_DIR", "~/.claude/skills/research")) + "/scripts/mktable.py"
TABLES = [
    ("search", r"l r r r r r r r r r r",
     "The search per venue. Recorded counts the candidates, the papers a screener recorded as near the rule, and "
     "accepted papers dropped at a glance are not among them. Dropped counts candidates dropped at screening, Read out "
     "those dropped after reading, and No PDF those kept without an accessible PDF. Coded papers have a PDF, a note "
     "and ledger rows, and the year columns split them. Earlier holds three anchors from 2021 and 2022."),
    ("drops", P("9cm") + " r",
     "Why screeners dropped candidates, matched by keyword on the reason each screener wrote. The first matching "
     "reason counts."),
    ("papers-a", P("2.6cm") + " r " + P("4.0cm") + " r " + P("2.8cm") + " r",
     "The coded papers by kind of contribution, setting and protection. A paper counts under each mechanism that any "
     "of its coalitions faces, so the protection column sums past the total."),
    ("papers-b", P("3.6cm") + " r " + P("1.8cm") + " r " + P("4.2cm") + " r",
     "The coded papers by coalition, goal and evaluation. A paper counts under every coalition and goal its rows "
     "hold, and under every mark of its evaluation."),
    ("trends", None,
     "Per cent of each year's coded papers. Deviating counts papers with a coalition that sets anything beyond "
     "queries. A mechanism column counts papers that name it for some coalition. Proven counts papers with a proven "
     "or sketched result. The 2026 column lacks NeurIPS 2026."),
    ("templates", P("3.0cm") + " r r " + P("2.7cm") + " " + P("2.8cm") + " r r r r",
     "The seven templates in ledger rows. Choices and goals give the two most common values, and a row may hold "
     "several. Message is a node output such as an update or a decryption share. Bare counts rows that name no "
     "protection mechanism. Check counts rows facing an input check, a proof of honest computation, a robust "
     "aggregation rule or a detector. Proven counts rows with a proven or sketched result. Adaptive counts rows "
     "evaluating an adversary that adapts to the defence, out of the rows that say."),
    ("support", P("3.6cm") + " " + P("5.4cm") + " r r r r",
     "What each template assumes and how it supports its claim, in rows. Evidence gives the two most common forms "
     "of the result. Honest and dishonest count rows assuming an honest or a dishonest majority. Stated counts rows "
     "in which the paper itself says static or adaptive corruption. Stealth counts rows that require or measure a "
     "stealth constraint."),
    ("communities", None,
     "How each community states its threat models, in per cent of its rows. Formal counts statements as an ideal "
     "functionality or a game, Theorem as the assumptions of a theorem, and Prose as prose or a taxonomy. The last "
     "four columns count rows in which the coder inferred a value the paper did not state. They are static or "
     "adaptive corruption, an honest or dishonest majority, what the coalition sets or when, and what it knows. "
     "Cryptography holds 17 rows."),
    ("anchors", P("3.8cm") + " " + P("11.0cm"),
     "Papers to read first in each template, by citation key. The choice is ours and favours the 33 papers marked "
     "for a full read."),
]
for name, colspec, caption in TABLES:
    cmd = ["python3", MKTABLE, f"{DATA}-{name}.csv", "--caption", caption, "--label", f"tab:{name}",
           "--bold", "none", "--precision", "0"]
    if colspec:
        cmd += ["--colspec", colspec]
    out = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout
    # A float resets the font to \normalsize, so the size goes inside it.
    out = out.replace("\\centering", "\\centering\\footnotesize\\setlength{\\tabcolsep}{4pt}", 1)
    open(f"lib/reports/src/figures/{STEM}-{name}.tex", "w").write(out)

for k, v in facts.items():
    print(f"{k}={v}", end="  ")
print()
