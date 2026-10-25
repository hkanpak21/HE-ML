# Gates: formal tuning of the learning oracle

OWNS: sink/2026-10-16-formal-tuning/**, sink/INGEST.md

Scope: builder and challenger rounds that turn the learning oracle into tested definitions and accepted non-trivial proofs, ending in one finalized document Halil can read alone.

- [x] G0: this ledger states outcomes that can fail
  CHECK: node /Users/a90/.claude/skills/unlazy/scripts/gate-lint.mjs GATES.md
  EXPECT: LINT OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/sink/2026-10-16-formal-tuning; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=958052e1be78d9acdd6d8ab18bb3126f4a183151119a69de38c6f4b36cac193d; output-bytes=150

- [x] G1: every round folder holds its turns, each challenger file has a parseable verdict block, at least six review rounds ran, and the README round log lists every round
  CHECK: node scripts/verify.mjs structure
  EXPECT: STRUCTURE OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/sink/2026-10-16-formal-tuning; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=2e99c68e4003671102980dc64ab0b5282bb6f8f068e98b8cea52c916b53cf258; output-bytes=23

- [x] G2: the rounds converged, with no blocking challenge in the latest review, definitions accepted in the last two reviews, and at least six accepted results of which three are non-trivial
  CHECK: node scripts/verify.mjs convergence
  EXPECT: CONVERGENCE OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/sink/2026-10-16-formal-tuning; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=2409e721b045f216c3bcc42a2c8243b480865a781771ac5bbc2c014e6795502a; output-bytes=40

- [x] G3: the final document holds a definitions section and at least five theorem sections, each with a proof and a without-the-oracle paragraph, and every item in it stands accepted by the challenger
  CHECK: node scripts/verify.mjs final
  EXPECT: FINAL OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/sink/2026-10-16-formal-tuning; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=63d6fc8ff987589848429b20ff7bd3e908694d05627ae689b0152e763577fb8d; output-bytes=42

- [x] G4: the challenger's audit of the final document accepts it with no blocking challenge and judges every item it contains
  CHECK: node scripts/verify.mjs audit
  EXPECT: AUDIT OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/sink/2026-10-16-formal-tuning; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=e09292b1dac5d2bfbcc14e183aeae06b541cddd315811e5da564422eb660d245; output-bytes=18

- [x] G5: every round file, the theory file and the final document compile to PDF
  CHECK: node scripts/build.mjs --all
  EXPECT: BUILD OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/sink/2026-10-16-formal-tuning; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=22dcc7040e8563781b0c1dd82e4810cdbb5c35f6a72a0966b3154a0b254772c2; output-bytes=14

- [x] G6: the sink ingest log records why this folder stays in the sink
  CHECK: node -e "const t=require('fs').readFileSync('../INGEST.md','utf8');if(!/\| 2026-10-16-formal-tuning\/ \| stays \|/.test(t)){console.error('no row');process.exit(1)}console.log('INGEST ROW OK')"
  EXPECT: INGEST ROW OK
  EVIDENCE: exit=0; shell=/bin/sh; cwd=/Users/a90/Documents/RESEARCH/HE-ML/sink/2026-10-16-formal-tuning; path=adefdc66accf/24 entries; EXPECT=matched; output-sha256=4807f9415a0b96d03ea637ddbb3abc07eebce53d225328e0f07b12c3e1efc2bb; output-bytes=14

- [x] G7: the orchestrator has checked each NONTRIVIAL proof of the final document line by line, independently of the challenger, and recorded what it checked
  EVIDENCE: 2026-10-17, orchestrator read final/learning-oracle-theory.md lines 103 to 321 and re-derived every proof shown in full there, namely lem-needle-lower-bound, lem-sphere-code (a) and (b), thm-coupling-certificate (a)(i), (a)(ii), (b) steps 1 to 4 and (c)(i), thm-black-box-certifiability (o) and (a), thm-dataflow-composition (b) steps 1 to 5, (c) and (e)(ii) with its Reading, thm-bounded-deviation-transfer (a) to (e) and the corollary, thm-replay-audit-steer (a), (b) and the bound of (c); no false step found, one conservative constant noted (coupling (a)(ii) uses sqrt(2 ln(2/alpha)/n) where sqrt(ln(1/alpha)/n) suffices); not re-derived here, the parts proven only by pointer to round files (coupling (a)(iii) and (c)(ii), black-box (b) to (d), dataflow (a), (d), (e)(i), (e)(iii), replay (d) and (e)) and the further results section
