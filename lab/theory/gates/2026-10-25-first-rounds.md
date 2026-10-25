# Gates: first rounds of the theory (closed 2026-10-25)

OWNS: lab/theory/**, lib/theory/**, CLAUDE.md, AGENTS.md, sink/formalizing/**

Scope: an agent-agnostic theory workspace whose only reading surface is the PDF folder lib/theory/, and the first builder and discussant rounds of the three thinking spaces, merged by the integrator into the booklet.

- [x] G0: this ledger states outcomes that can fail
  CHECK: node /Users/a90/.claude/skills/unlazy/scripts/gate-lint.mjs GATES.md
  EXPECT: LINT OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=6b9c923a0747576f5eaf191c66af65f50992e8bb75e93644a23b49e6bb01825a; output-bytes=268

- [x] G1: the shared context, the state file, the agent-file pointers and a README with an owner session for each of the three spaces are in place
  CHECK: node tools/verify.mjs context
  EXPECT: CONTEXT OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=c140de793e2e7e5c42bc5419d16a8ee86a7ce8d1e3ea643afb3a063b4819f678; output-bytes=11

- [x] G2: the booklet and every reading build from source, and no TeX file or build artifact lies outside lab/theory/booklet/
  CHECK: python3 tools/build.py
  EXPECT: BUILD OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=97d341d5963d5d5d44f0cab190eb2372f8c38c77d1925506894604afcc99fa95; output-bytes=104

- [x] G3: lib/theory/ holds PDFs only, each reading PDF has its source, and the booklet is newer than every booklet source
  CHECK: node tools/verify.mjs folder
  EXPECT: FOLDER OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=701818c8fb7c907be164e764e9f7567e1988131aafc4febb9624b27f9d151b69; output-bytes=10

- [x] G4: each space ran round-00 and at least one more round, each round complete with a logged, model-stamped discussant turn within budget, and both astra and argon took part
  CHECK: node tools/verify.mjs spaces
  EXPECT: SPACES OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=fa998aa81f2548060f9878e498bbdf814f8a3227681679bd2e8a657847d4d07d; output-bytes=10

- [x] G5: the last round of every space ends with no blocking challenge
  CHECK: node tools/verify.mjs convergence
  EXPECT: CONVERGENCE OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=a5cffc301329c43fa13a2acc753fddbcff1ea1b444f1715d3b88d27262ae40db; output-bytes=15

- [x] G6: every object a round accepted is in the booklet with a fitting status, no booklet object claims acceptance without a round behind it, the history chapter and STATE.md name every round, and the booklet was built after the last summary
  CHECK: node tools/verify.mjs integration
  EXPECT: INTEGRATION OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=2fedc816702a949ea5625b2e55866343d85398966323efc2e3a20e55496ce1c6; output-bytes=27

- [x] G7: the formalizing registers still lint after the integrator moved the spaces' register entries into them
  CHECK: python3 ../../sink/formalizing/tools/lint.py
  EXPECT: LINT OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=42ff7027a0df1317da3b0951f6683b5e4ff833af7279540deeef9d0d7fb7f8b6; output-bytes=32

- [x] G8: the integrator has re-derived, line by line, every proof of an object merged with status accepted in this milestone, and recorded what it checked and what it did not
  EVIDENCE: 2026-10-25, integrator. Every proof of the 18 merged objects with status accepted re-derived from its round file, arithmetic recomputed, no false step found, recorded in lab/theory/integration-log.md section 2026-10-25. Not re-read: the cited theorems of BRST21, FGRVX17, DKRS23, DPLB24, LJDD19, AKMSS21 and LZA21, taken as the spaces read them, and the borrowed facts. One scope note added: prop-drawn-mode-is-fs-oracle (b) needs the starting model fixed as in (a).

- [x] G9: every item under "For the registers" in a space summary is in sink/formalizing/ or recorded as declined with a reason, and a reading PDF exists for each merged result the integrator judges worth Halil's time
  EVIDENCE: 2026-10-25, integrator. The nine summaries' register items checked one by one against sink/formalizing after the merge scripts ran. Moved: 20 new facts, corrections to 19 facts, 20 results, one refutation with the BB20 pointer, 6 search rows, 5 problems, 4 status changes, 6 problem history lines, papers to place in sink/formalizing/STATE.md. Declined with reasons in lab/theory/integration-log.md: three unopened prior-work pointers and one unproven cross-space remark. Reading: lib/theory/2026-10-25-first-rounds.pdf covers the five results judged worth reading (Theorems 5.8, 5.9 with 4.4 and 5.10, 4.3, 6.5 with 6.3, and 5.1 of the booklet).
