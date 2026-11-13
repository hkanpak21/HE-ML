"""Tables and numbers of the report 2026-11-13-halil-ideal-functionalities-and-attacks.

Run from the HE-ML root with FORMAL_SECURITY beside it. The placement of published
attacks is computed from the ledger of the formalizing line, which moved to
FORMAL_SECURITY/HE-ML-migrated on 2026-11-11. The other tables are the definitions
of the report, written here once so that the CSV and the typeset table agree.
"""
import collections
import csv
import pathlib
import re
import subprocess

STEM = "2026-11-13-halil-ideal-functionalities-and-attacks"
DATA = pathlib.Path("lib/reports/src/data")
FIG = pathlib.Path("lib/reports/src/figures")
LEDGER = pathlib.Path("../FORMAL_SECURITY/HE-ML-migrated/lib/literature/ledger.csv")
MKTABLE = pathlib.Path.home() / ".claude/skills/research/scripts/mktable.py"
RAGGED = r">{\raggedright\arraybackslash}p{%s\linewidth}"


def field(text, key):
    m = re.search(r"(?:^|; )" + re.escape(key) + r"=([^;]*)", text or "")
    return m.group(1).strip() if m else ""


def write(name, header, rows):
    with (DATA / f"{STEM}-{name}.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def table(name, caption, widths):
    spec = " ".join(RAGGED % w for w in widths)
    out = subprocess.run(
        ["python3", str(MKTABLE), str(DATA / f"{STEM}-{name}.csv"), "--colspec", spec,
         "--caption", caption, "--label", name, "--precision", "0", "--bold", "none"],
        check=True, capture_output=True, text=True).stdout
    out = out.replace(r"\begin{table}[t]", r"\begin{table}[!htbp]", 1)
    (FIG / f"{STEM}-{name}.tex").write_text(out.replace(r"\begin{tabular}", r"\small\begin{tabular}", 1))


# The standard attacks: one question kind and one target each.
write("attacks", ["Name", "Kind", "The two hypotheses, or the target", "Interface"], [
    ["membership", "distinguish", "a record $z$ is in an honest dataset, or it is not", "outputs"],
    ["source", "distinguish", "$z$ is with honest client $i$ and $z'$ with honest client $j$, or the two are "
     "swapped, so the union and every size stay fixed", "outputs"],
    ["property", "distinguish", "the honest data come from a distribution with a property, or without it", "outputs"],
    ["record", "invert", "a record of an honest dataset, within a distance", "outputs"],
    ["attribute", "invert", "one feature or the label of a record whose other features are known", "outputs"],
    ["model", "invert", "the parameters or the behavior of a model that is an honest input", "outputs"],
    ["query", "invert", "the query of an honest querier", "outputs"],
    ["targeted", "steer", "honest outputs whose model maps chosen inputs to chosen labels", "inputs"],
    ["untargeted", "steer", "honest outputs whose model has accuracy below a level", "inputs"],
    ["delivery", "steer", "the honest parties receive no output", "inputs"],
])
table("attacks", "The standard attacks. Each is one question kind with one target, and the interface is the "
      "side of the ideal functionality it acts through.", ["0.13", "0.12", "0.53", "0.10"])

# The library. What each ideal functionality accepts, and what it hands to whom.
write("library", ["Name", "Accepts", "The server receives", "A client receives", "The querier receives"], [
    ["pooled-training", "a dataset from each client", "the model trained on the shuffled union",
     "the same model", "nothing"],
    ["served-model", "a dataset from each client, queries", "nothing", "nothing",
     "the trained model's answer to each query"],
    ["outsourced-training", "a dataset from one client", "nothing", "the model trained on it", "nothing"],
    ["fedavg-plain", "a dataset or any update from each client, a model for each client each round from "
     "the server", "every client's update in every round", "the model sent to it", "nothing"],
    ["fedavg-secagg", "as fedavg-plain", "the sum of the updates in every round", "the model sent to it",
     "nothing"],
    ["fedavg-final", "a dataset or any update from each client", "the final model",
     "the average model of every round", "nothing"],
    ["split-learning", "batches from the client, any gradient at the cut from the server",
     "the activations at the cut and the labels", "the gradient at the cut", "nothing"],
    ["vertical-training", "a feature block of the shared records from each client, the labels and any "
     "gradient from the server", "every client's embedding", "the gradient at its own embedding", "nothing"],
    ["private-inference", "a model from the server, a query", "nothing", "nothing",
     "the model's answer to the query"],
    ["he-oft", r"a dataset, or any head displacement and per-class counts, from each client, up to $Q$ "
     r"queries~\cite{KSK26}", "each client's sample count and the selected arrangement",
     "the selected arrangement", "one label per query"],
])
table("library", "The library of ideal functionalities. A client that chooses its input may submit anything "
      "the Accepts column allows, and every output not listed is withheld.",
      ["0.14", "0.26", "0.19", "0.15", "0.14"])

# Worked cases of the two readings.
write("cases", ["Attack", "Scenario", "Verdict at the output layer", "Status"], [
    ["source", "pooled-training, any coalition holding neither $z$ nor $z'$",
     "zero, because every output is a function of the union and the coalition's inputs", "proven"],
    ["source", "fedavg-secagg or fedavg-final, semi-honest server, one full-batch local step weighted by size",
     "zero, because every round's sum is the sum of the per-record gradients over the union", "proven"],
    ["source", "the same, with several local steps",
     "the model depends on how the records are split, so the advantage need not vanish, and its size is "
     "unknown", "open"],
    ["source", "fedavg-plain, semi-honest server",
     "at least the advantage of telling whether one client's update was computed with $z$ or with $z'$, "
     "since the server reads that update alone", "proven"],
    ["membership", "every training task that hands out a model or answers",
     r"in the floor, and at most $e^\varepsilon-1$ when the ideal functionality trains with "
     r"$\varepsilon$-DP~\cite{YGFJ18}", "proven"],
    ["targeted, untargeted", "pooled-training, input-choosing client",
     "in the floor, because the ideal functionality accepts any dataset", "proven"],
    ["targeted", "he-oft, input-choosing client",
     r"in its floor, because inflated per-class counts move a row of the shared head at will~\cite{KSK26}",
     "proven"],
    ["membership", "he-oft, querier with $Q$ queries",
     r"in its floor, and at most the advantage of a holder of both heads in plaintext~\cite{KSK26}",
     "proven"],
    ["every output question", "outsourced-training, server coalition",
     "zero, because the server receives nothing", "proven"],
])
table("cases", "Worked cases. The verdict is about the ideal functionality, so a protocol realizing it adds "
      "at most its realization error. The active attacks on fedavg-secagg are discussed in the text.",
      ["0.12", "0.27", "0.40", "0.09"])

# The published attacks, by what they need in plaintext, from the ledger.
rows = list(csv.DictReader(LEDGER.open()))
attacks = [r for r in rows if "attack" in field(r["paper"], "type")]
NODES = ["update (one-step gradient)", "update (multi-step change)", "update", "aggregate", "model per round",
         "final model", "activations at a cut", "gradients at a cut", "served answers", "decrypted value",
         "BN statistics", "class counts"]


def plain(sees):
    out = set()
    for item in re.split(r";\s*", sees or ""):
        m = re.match(r"\s*([^:]+):([^@]+)", item)
        if not m:
            continue
        node, channel = m.group(1).strip(), m.group(2).strip()
        if channel.startswith(("plain", "post-processed", "noise")):
            base = next((n for n in NODES if node.startswith(n)), node.split(" (")[0])
            out.add("update" if base.startswith("update") else base)
    return out


need = collections.Counter()
for r in attacks:
    n = plain(r["sees"])
    if "update" in n:
        need["update"] += 1
    elif n & {"activations at a cut", "gradients at a cut"}:
        need["cut"] += 1
    elif n & {"aggregate", "model per round"}:
        need["round"] += 1
    elif n & {"final model", "served answers"}:
        need["final"] += 1
    elif not n:
        need["nothing"] += 1
    elif n == {"decrypted value"}:
        need["decrypted"] += 1
    else:
        need["other"] += 1

write("placed", ["What it needs in plaintext", "The lowest ideal functionality that hands it out",
                 "Threat models"], [
    ["a client's own update", "fedavg-plain", need["update"]],
    ["a per-round sum or model", "fedavg-secagg", need["round"]],
    ["values at a cut", "split-learning, vertical-training", need["cut"]],
    ["only the final model or served answers", "fedavg-final, pooled-training, served-model", need["final"]],
    ["a decrypted value", "none, the attack targets the realization", need["decrypted"]],
    ["nothing coded in plaintext", "none, the attack targets the protocol or the coding is short", need["nothing"]],
    ["other values", "outside the library", need["other"]],
])

write("prior", ["Work", "What it fixes in this picture", "PDF folder"], [
    [r"Barreno et al.~\cite{BNJT10}", "goal and capability, which become the two interfaces", "not held"],
    [r"Papernot et al.~\cite{PMSW18}", "the stage of an attack and the adversary's knowledge", "ieee-eurosp"],
    [r"NIST AI 100-2~\cite{VOFADH25}", "the names of attacks, privacy and integrity together", "nist"],
    [r"Yeom et al.~\cite{YGFJ18}", "membership and attribute games on one model, the DP bound", "csf"],
    [r"Salem et al.~\cite{SCEKPSTZ23}", r"\lrv{SalemGames} games on one model, the output layer of pooled-training",
     "ieee-sp"],
    [r"Li et al.~\cite{LLLKPMW24}", "games on gradients, the output layer of fedavg-plain", "acm-ccs"],
    [r"Wu et al.~\cite{WZLLHL23}", "integrity attacks, the steer kind, with no advantage", "arxiv"],
    [r"Mansouri et al.~\cite{MOJC23}", "the ideal functionality of secure aggregation, by coalition", "popets"],
    [r"Ma et al.~\cite{MWAPR23}", "simulation of secure aggregation over many rounds", "ieee-sp"],
    [r"Morona-M\'{\i}nguez et al.~\cite{MPP26}", "averaging under multi-key HE, up to the CKKS error", "arxiv"],
    [r"HE-OFT~\cite{KSK26}", "an ideal functionality with stated leakage, and the bound on label queries", "arxiv"],
    [r"Pentyala et al.~\cite{PRMMDND22}", "MPC for the protocol and DP inside the ideal functionality", "arxiv"],
    [r"Carletti et al.~\cite{CFMPV25}", "the threat models of gradient inversion, by role", "usenix-security"],
    [r"Rizzini et al.~\cite{REGB26}", "verifiable integrity, which narrows what is accepted", "popets"],
    [r"Desfontaines and Pej\'o~\cite{DP20}", "criteria for a list of attacks, exclusive and compatible dimensions",
     "popets"],
    [r"NIST SP 800-226~\cite{NISTSP800226}", "the unit of privacy for DP inside an ideal functionality", "nist"],
    [r"Villa et al.~\cite{VDKMR26}", "one game for confidentiality, integrity and availability of agentic LLM systems",
     "arxiv"],
    [r"IEEE 3652.1~\cite{IEEE3652}, ISO/IEC 4922~\cite{ISO4922}, ISO/IEC 28033~\cite{ISO28033}",
     "the vocabulary of federated learning, MPC and FHE", "not held"],
])
table("prior", "The prior work this report compares against, what each fixes in the picture of ideal "
      "functionalities and attacks, and the folder of its PDF under lib/literature/pdfs, where the file name "
      "starts with the key.", ["0.24", "0.55", "0.12"])

write("facts", ["name", "value", "source"], [
    ["AttackModels", len(attacks), str(LEDGER) + ", threat models of papers typed attack"],
    ["NeedUpdate", need["update"], str(LEDGER)],
    ["NeedRound", need["round"], str(LEDGER)],
    ["NeedFinal", need["final"], str(LEDGER)],
    ["NeedDecrypted", need["decrypted"], str(LEDGER)],
    ["NeedCut", need["cut"], str(LEDGER)],
    ["NeedRest", need["nothing"] + need["other"], str(LEDGER) + ", nothing in plaintext plus other values"],
    ["NeedMore", need["update"] + need["round"], str(LEDGER) + ", own update plus per-round value"],
    ["SalemGames", 18, "FORMAL_SECURITY/HE-ML-migrated/lib/literature/notes/ieee-sp/SCEKPSTZ23.md"],
])
print(len(attacks), dict(need))
