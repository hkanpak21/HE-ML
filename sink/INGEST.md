# Ingest log

Anything that arrives in a format the repo does not use is dropped in `sink/`.
Nothing reads from it. `ingest.py` moves each file to its one target and adds a
row here. A file leaves the sink only when its target exists in the format.

| Date | Original | Target | Created |
| --- | --- | --- | --- |
| 2026-10-16 | unavailable.md | stays | The record of four accepted papers with no accessible PDF, kept until a version appears. Renamed from UNAVAILABLE.md on 2026-10-25 by the naming rule of CLAUDE.md. No target in the layout holds a list of papers that have no note. |
| 2026-10-16 | lib/literature/ledger-columns.md | stays | The column dictionary of ledger.csv, moved here once the ledger was finished, by the repo memory rule in CLAUDE.md. It defines the 22 columns, their keywords and the five reductions. Read it before adding rows. |
| 2026-10-16 | 2026-10-16-formal-tuning/ | stays | Builder and challenger rounds on the learning oracle, opened at Halil's request as a sink folder. The rounds are the working record. The reading copy is final/learning-oracle-theory.pdf inside it. |
| 2026-10-25 | formalizing/ | stays | The shared context of the line on formalizing AI security across HE-ML and FORMAL_SECURITY, opened at Halil's request: a state page, registers of results, facts, searches and problems, a session log, and dated digests. Its README holds the routine. No target in the layout holds a cross-repository research context. |
