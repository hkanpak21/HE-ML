# How mathematicians and agent builders keep context, 2026-10-25

Research by a subagent of the HE-ML session of 2026-10-25, the rationale for the
design in `../README.md`. Each mechanism is empirical, read from the page named
with it. Each fit judgement is heuristic. Pages that failed to open: the
Polymath wiki at michaelnielsen.org (404 on every page), one Open Problem Garden
problem page, an nLab conventions page. No page by Gowers on personal write-up
habits was found.

## Verdict

Communities that avoid repeated work share three mechanisms. Each object gets a
permanent name that is never reused. One page of current state is rewritten,
and the history beside it only grows. Negative results get the same care as
positive ones, including failed searches, failed proofs and withdrawn claims.
Agent practice adds two more. Every session starts with a fixed routine that
reads files, and it checks a log before it repeats work.

## Mechanisms

1. Lean blueprints (leanblueprint, PFR, FLT, Carleson). Each node lists its
   dependencies separately for the statement and the proof, and carries a state.
   In the PFR graph the border shows the statement's state and the fill the
   proof's, and dark green means the proof and all its ancestors are done. It
   stops work on a result whose prerequisites are missing, and stops a theorem
   being called done while it rests on an open lemma. The FLT blueprint ends
   with a chapter of the outside results its proof relies on, the model for how
   prior work enters a dependency register. Opened:
   https://github.com/PatrickMassot/leanblueprint,
   https://teorth.github.io/pfr/blueprint/dep_graph_document.html,
   https://imperialcollegelondon.github.io/FLT/blueprint/.
2. Equational theories project. A contributor claims a task on its issue and
   holds one claim at a time. Hand results enter as conjectures until checked.
   It prevents two people doing one task, and hand results passing as checked.
   Opened: https://github.com/teorth/equational_theories (CONTRIBUTING.md).
3. Stacks project. Every result has a permanent tag. A tags file maps each tag
   to its current place, so a move never changes the tag. A wrong result may be
   removed, but its tag stays with an explanation, and unneeded results move to
   an Obsolete chapter with their tags. Each tag has a dated history. It prevents
   dangling references and the silent loss of a cited result. Opened:
   https://stacks.math.columbia.edu/tags,
   https://stacks.math.columbia.edu/tag/0AKU/history.
4. Polymath. A research thread carries the mathematics, a wiki holds what is
   settled, and a long thread moves to a fresh post that opens with a summary.
   Gowers's rules ask that a result be a short statement others can use without
   its proof. It prevents having to read hundreds of comments to learn the
   state. Opened: https://polymathprojects.org/general-polymath-rules/,
   https://arxiv.org/abs/1409.8361.
5. Erdős problems. Each problem has a permanent number, references and a
   last-edited date, and lists who is working on it. The status words form a
   closed list, each with a written definition, and formal verification is a
   separate field. The FAQ warns that a problem listed as open may already be
   solved. It prevents status words drifting and effort on problems the
   literature closed. Opened: https://www.erdosproblems.com/faq,
   https://www.erdosproblems.com/1.
6. Open Problem Garden. Fixed fields, importance in four defined levels, and a
   solved entry names its solver and reference. Opened:
   https://openproblemgarden.org/op_structure.
7. Kourovka notebook. Problems keep their numbers for six decades, solved ones
   move to an archive, and a withdrawn one leaves a gap. Since 2026 a mark flags
   an AI-proposed solution no mathematician has confirmed, and such a problem
   counts as unsolved until confirmed. Opened: https://arxiv.org/abs/1401.0300.
8. Mathlib naming. A name is read off the statement, conclusion first, so anyone
   can predict a name and search for it. A renamed declaration stays as a dated
   alias. It prevents one lemma being proved twice under two names. Opened:
   https://leanprover-community.github.io/contribute/naming.html.
9. nLab. One page per concept, synonyms redirect, discussion stays off the page
   in a forum. Opened: https://ncatlab.org/nlab/show/HowTo.
10. Zettelkasten. Atomic notes at fixed addresses, every link states its reason,
    structure notes as entry points. Opened: https://zettelkasten.de/introduction/.
11. Tao, "write down what you've done". Write up partial and abandoned arguments
    as sketches with enough detail to rebuild them. It prevents re-deriving an
    argument and retrying a failed approach. Opened:
    https://terrytao.wordpress.com/career-advice/write-down-what-youve-done/.
12. Research logs. The FamilySearch log records each search's source, date and
    terms, an empty result is written nil, and a blank row means not searched.
    PRISMA-S asks for the strategy exactly as run, its limits, its update method
    and the date last run. It prevents repeating a search because an empty
    result left no trace. Opened:
    https://www.familysearch.org/en/wiki/Research_Logs,
    https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/.
13. Karpathy's LLM wiki. Raw sources are never edited, a markdown wiki belongs
    to the model, a schema file holds the conventions, an index is read first,
    and an append-only log has grep-parsable headings. Ingest, query and lint
    are the operations. It prevents rediscovering knowledge at every question.
    FORMAL_SECURITY's wiki follows this pattern. Opened:
    https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f.
14. Anthropic engineering guidance. Agents keep structured notes outside the
    context window and reload them by path. Each new session follows a fixed
    routine and edits status only from a closed list. Subagents with vague
    briefs repeated each other's searches, so briefs should carry the matching
    search rows and subagents should write results to files. Opened:
    https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents,
    https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents,
    https://www.anthropic.com/engineering/multi-agent-research-system.
15. LangChain on context engineering. Names context poisoning, a hallucination
    that enters the context and is reused. This is why a fact enters a register
    only from a source someone opened. Opened:
    https://www.langchain.com/blog/context-engineering-for-agents.

## What the design takes from each

- Permanent slugs with aliases and kept retired entries: Stacks, Mathlib, Kourovka.
- Separate dependency lists for statement and proof, and closure over
  ancestors: blueprints.
- A closed status vocabulary with definitions, and agent proofs counted as
  unchecked until a person checks them: Erdős problems, Kourovka.
- One rewritten state page beside an append-only log: Polymath, Karpathy,
  Anthropic.
- A search log with exact queries, scope and empty results: FamilySearch,
  PRISMA-S.
- Dead ends recorded with pointers: Tao.
- A fixed start routine and a search gate before any new search: Anthropic.
