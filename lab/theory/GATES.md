# Gates: mappings to known hard problems

OWNS: lab/theory/**, lib/theory/**, sink/formalizing/**

Scope: the second milestone of the theory, whose spaces are listed in lab/theory/milestone.json, run with sol as discussant and argon under the object-by-object protocol once its quota returns, merged by the integrator into the booklet.

- [x] G0: this ledger states outcomes that can fail
  CHECK: node /Users/a90/.claude/skills/unlazy/scripts/gate-lint.mjs GATES.md
  EXPECT: LINT OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=07c98dab0107df0a40740c243115ab016b3c252f7c6e6e094b6e4a0a3463e7d5; output-bytes=269

- [ ] G1: the context, the state file, the agent-file pointers and a README with an owner session for every space of the milestone are in place
  CHECK: node tools/verify.mjs context
  EXPECT: CONTEXT OK
  EVIDENCE: pending

- [x] G2: the booklet and every reading build from source, and no TeX file or build artifact lies outside lab/theory/booklet/
  CHECK: python3 tools/build.py
  EXPECT: BUILD OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=97d341d5963d5d5d44f0cab190eb2372f8c38c77d1925506894604afcc99fa95; output-bytes=104

- [x] G3: lib/theory/ holds PDFs only, each reading PDF has its source, and the booklet is newer than every booklet source
  CHECK: node tools/verify.mjs folder
  EXPECT: FOLDER OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=701818c8fb7c907be164e764e9f7567e1988131aafc4febb9624b27f9d151b69; output-bytes=10

- [ ] G4: every space of the milestone ran its aims round and at least one more within its round range, each round complete with a logged, model-stamped discussant turn within budget, and every repeated discussant explained in its summary
  CHECK: node tools/verify.mjs spaces
  EXPECT: SPACES OK
  EVIDENCE: pending

- [ ] G5: the last round of every space of the milestone ends with no blocking challenge
  CHECK: node tools/verify.mjs convergence
  EXPECT: CONVERGENCE OK
  EVIDENCE: pending

- [x] G6: every object a round accepted is in the booklet with a fitting status, no booklet object claims acceptance without a round behind it, the history chapter and STATE.md name every round of every space, and the booklet was built after the last summary
  CHECK: node tools/verify.mjs integration
  EXPECT: INTEGRATION OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=2fedc816702a949ea5625b2e55866343d85398966323efc2e3a20e55496ce1c6; output-bytes=27

- [x] G7: the formalizing registers lint after the integrator moved the spaces' register entries into them
  CHECK: python3 ../../sink/formalizing/tools/lint.py
  EXPECT: LINT OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/lab/theory; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=42ff7027a0df1317da3b0951f6683b5e4ff833af7279540deeef9d0d7fb7f8b6; output-bytes=32

- [ ] G8: at least one argon-high round of the milestone finished under the object-by-object protocol with a passing audit
  CHECK: node tools/verify.mjs argon
  EXPECT: ARGON OK
  EVIDENCE: pending

- [ ] G9: the integrator has re-derived, line by line, every proof of an object merged with status accepted in this milestone, and recorded in integration-log.md what it checked and what it took on trust
  EVIDENCE: pending

- [ ] G10: every item under "For the registers" in a summary of this milestone is in sink/formalizing/ or recorded as declined with a reason, and a reading PDF exists for each merged result the integrator judges worth Halil's time
  EVIDENCE: pending
