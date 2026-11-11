# Ingest log

Anything that arrives in a format the repo does not use is dropped in `sink/`.
Nothing reads from it. `ingest.py` moves each file to its one target and adds a
row here. A file leaves the sink only when its target exists in the format.

The log of 2026-10-16 to 2026-11-11, with the folders it kept here, moved to
`FORMAL_SECURITY/HE-ML-migrated/sink/` on 2026-11-11.

| Date | Original | Target | Created |
| --- | --- | --- | --- |
