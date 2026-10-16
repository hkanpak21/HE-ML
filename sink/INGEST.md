# Ingest log

Anything that arrives in a format the repo does not use is dropped in `sink/`.
Nothing reads from it. `ingest.py` moves each file to its one target and adds a
row here. A file leaves the sink only when its target exists in the format.

| Date | Original | Target | Created |
| --- | --- | --- | --- |
| 2026-10-16 | UNAVAILABLE.md | stays | The record of four accepted papers with no accessible PDF, kept until a version appears. No target in the layout holds a list of papers that have no note. |
| 2026-10-16 | lib/literature/ledger-columns.md | stays | The column dictionary of ledger.csv, moved here once the ledger was finished, by the repo memory rule in CLAUDE.md. It defines the 22 columns, their keywords and the five reductions. Read it before adding rows. |
