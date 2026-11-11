"""Tables and numbers of the report 2026-11-11-halil-prior-work-on-scenario-frameworks.

Run from the HE-ML root. Reads the ledger of the formalizing line, which moved to
FORMAL_SECURITY/HE-ML-migrated on 2026-11-11, writes the report's CSVs to
lib/reports/src/data/ and the generated tables to lib/reports/src/figures/.
"""
import collections
import csv
import pathlib
import re
import subprocess

STEM = "2026-11-11-halil-prior-work-on-scenario-frameworks"
DATA = pathlib.Path("lib/reports/src/data")
FIG = pathlib.Path("lib/reports/src/figures")
LEDGER = pathlib.Path("../FORMAL_SECURITY/HE-ML-migrated/lib/literature/ledger.csv")
MKTABLE = pathlib.Path.home() / ".claude/skills/research/scripts/mktable.py"
RAGGED = r">{\raggedright\arraybackslash}p{%s\linewidth}"
DP = re.compile(r"DP (central|distributed|local)|differential privacy|\bLDP\b|Gaussian DP|f-DP")


def field(text, key):
    m = re.search(r"(?:^|; )" + re.escape(key) + r"=([^;]*)", text or "")
    return m.group(1).strip() if m else ""


def kind(formality):
    f = formality.lower()
    if "ideal functionality" in f:
        return "ideal functionality"
    if f.startswith("game") or " game" in f:
        return "game"
    if f.startswith("taxonomy"):
        return "taxonomy"
    if f.startswith("prose"):
        return "prose"
    return "theorem with assumptions"


def write(name, header, rows):
    path = DATA / f"{STEM}-{name}.csv"
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    return path


def table(name, caption, widths):
    spec = " ".join(RAGGED % w for w in widths)
    out = subprocess.run(
        ["python3", str(MKTABLE), str(DATA / f"{STEM}-{name}.csv"), "--colspec", spec,
         "--caption", caption, "--label", name, "--precision", "0"],
        check=True, capture_output=True, text=True).stdout
    (FIG / f"{STEM}-{name}.tex").write_text(out)


papers = collections.OrderedDict()
for r in csv.DictReader(LEDGER.open()):
    papers.setdefault(r["key"], []).append(r)

kinds = collections.Counter(kind(field(rs[0]["paper"], "formality")) for rs in papers.values())
joins = [k for k, rs in papers.items()
         if kind(field(rs[0]["paper"], "formality")) == "ideal functionality"
         and any(DP.search(r["protection"] or "") for r in rs)]

proves = {
    "theorem with assumptions": "a bound on its own method under its own assumptions",
    "prose": "an argument with no theorem",
    "ideal functionality": "that its protocol reveals nothing beyond a stated ideal functionality",
    "game": "an advantage bound in a game it defines",
    "taxonomy": "a classification",
}
write("formality", ["Formality", "Papers", "What such a paper proves"],
      [[k, kinds[k], proves[k]] for k in proves])
table("formality", "The formality of the multi-party papers of the ledger, as the sweep coders "
      "recorded it on 2026-10-16. One paper counts once, by its first coded threat model.",
      ["0.27", "0.09", "0.52"])

write("facts", ["name", "value", "source"], [
    ["LedgerPapers", len(papers), str(LEDGER)],
    ["IdealPapers", kinds["ideal functionality"], str(LEDGER)],
    ["GamePapers", kinds["game"], str(LEDGER)],
    ["Joins", len(joins), str(LEDGER) + ", ideal functionality with a DP mechanism coded"],
    ["Taxonomies", 30, "FORMAL_SECURITY/exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md, roughly thirty"],
    ["SalemGames", 18, "FORMAL_SECURITY/HE-ML-migrated/lib/literature/notes/ieee-sp/SCEKPSTZ23.md"],
    ["Searches", 9, "lib/literature/positioning.md, the rows of 2026-11-11 after the first four"],
])
write("joins", ["Key", "Venue", "Setting"],
      [[k if len(k) <= 14 else k[:10] + "...", field(papers[k][0]["paper"], "venue"),
        field(papers[k][0]["paper"], "setting")] for k in joins])
table("joins", "The ledger papers proven against an ideal functionality that also put a DP mechanism on the "
      "released value, as coded on 2026-10-16. A key longer than fourteen letters is cut.", ["0.38", "0.16", "0.36"])

bodies = [
    ["Taxonomies", r"Barreno et al.~\cite{BNJT10}, Papernot et al.~\cite{PMSW18}, NIST AI 100-2~\cite{VOFADH25}",
     "The terms for the stage, the goal, the adversary's knowledge and its capability.",
     "They prove nothing. None has an axis for which parties the adversary controls (found by us). "
     "Only NIST puts privacy and integrity on one page."],
    ["Federated SoKs", r"Carletti et al.~\cite{CFMPV25}, Mansouri et al.~\cite{MOJC23}, Rizzini et al.~\cite{REGB26}",
     "Threat models by role inside one setting, such as eight server models for gradient inversion, "
     "one a server with Sybil clients.",
     "Each covers one setting and one family of attacks (found by us)."],
    ["Security games", r"Yeom et al.~\cite{YGFJ18}, Salem et al.~\cite{SCEKPSTZ23}, Wu et al.~\cite{WZLLHL23}, "
     r"Li et al.~\cite{LLLKPMW24}",
     "What it means that the adversary can tell, for a released model or for gradients, with reductions "
     "between goals.",
     "Salem et al.: one challenger trains one model, and games do not express concurrent protocols (stated, "
     "Sec. VI-D). Wu et al.: integrity only, with no advantage. Li et al.: gradients only, the final model is "
     "not attacked."],
    ["Protocol simulation", r"Mansouri et al.~\cite{MOJC23}, Ma et al.~\cite{MWAPR23}, HE-OFT~\cite{KSK26}, "
     r"Morona-M\'{\i}nguez et al.~\cite{MPP26}",
     "The protocol reveals nothing beyond the output of an ideal functionality, against a named coalition.",
     "What that output leaks is taken as given, for instance the sum in secure aggregation. A CKKS "
     "instantiation is approximate, so it realizes the functionality only up to an error."],
    ["Protocol with a mechanism on the output", r"Pentyala et al.~\cite{PRMDMND22}, and the joined ledger papers",
     "MPC or HE for the protocol and DP on the released value, in one construction.",
     "Each proof covers its own protocol and functionality. No search found a definitional framework."],
    ["Games in another domain", r"Villa et al.~\cite{VDKMR26}",
     "One game for confidentiality, integrity and availability.",
     "Its object is an agentic LLM system, not parties training together."],
    ["Standards", r"IEEE 3652.1~\cite{IEEE3652}, ISO/IEC 4922-1~\cite{ISO4922}, ISO/IEC 28033-1~\cite{ISO28033}, "
     r"NIST SP 800-226~\cite{NISTSP800226}",
     "Vocabulary for federated learning, MPC, FHE and DP, and the unit of privacy.",
     "None fixes attack scenarios. ISO/IEC 28033 is a draft, and the full text of IEEE 3652.1 was not seen."],
    ["Method", r"Desfontaines and Pej\'o~\cite{DP20}",
     "Criteria for the dimensions of a taxonomy: inner exclusivity and mutual compatibility.",
     "Applied to variants of DP, not to attack scenarios."],
]
write("bodies", ["Body", "Works", "What it gives us", "Where it stops"], bodies)
table("bodies", "The bodies of prior work, what each gives a framework of scenarios, and where each stops. "
      "Found by us means our reading, not a statement of the authors.", ["0.12", "0.23", "0.24", "0.29"])

gap = [
    ["no-scenario-coordinates", "No work writes a scenario as the parties, the ideal functionality and the "
     "coalition, with a security statement per scenario.",
     "The sweep of roughly thirty taxonomies of 2026-08-05 and the searches of 2026-11-11, all nil.",
     "found by us"],
    ["games-one-model", "The game frameworks have one challenger training one model.",
     r"Salem et al.~\cite{SCEKPSTZ23}, Sec. VI-D.", "stated"],
    ["simulation-stops-at-output", "Simulation proofs say nothing about what the functionality's output leaks.",
     r"The ideal leakage of secure aggregation is the sum~\cite{MOJC23}.", "stated, as the definition"],
    ["joins-per-construction", "Protocol security and output leakage are joined only inside single "
     "constructions.", "The joined papers of the ledger, and Pentyala et al.", "found by us"],
    ["privacy-integrity-apart", "Privacy and integrity are formalized apart.",
     r"Salem et al. exclude integrity, Wu et al.~\cite{WZLLHL23} exclude privacy.", "found by the 2026-08-05 sweep"],
    ["no-standard-scenarios", "No standard fixes attack scenarios.", "The four standards above.", "found by us"],
]
write("gap", ["Gap", "What is missing", "Evidence", "Whose finding"], gap)
table("gap", "The gap, item by item, with the evidence and whose finding it is.", ["0.19", "0.29", "0.29", "0.12"])
print(dict(kinds), "joins", len(joins), joins)
