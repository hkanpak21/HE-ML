The messages of the later steps, sent through each discussant's kept context. NN is the round, MM the previous round, OWNER the recipient, OTHER_A and OTHER_B the other two owners.

---

Review step of round NN, to each owner.

Review step of round NN. Read `lab/theory/council/2026-10-30-statement-refinement/OTHER_A/round-NN.md` and `lab/theory/council/2026-10-30-statement-refinement/OTHER_B/round-NN.md`, with any file they cite or any check script they report. From round 02 on, read also `statement/round-NN.md`, the editor's integrated statement.

Write `lab/theory/council/2026-10-30-statement-refinement/OWNER/review-NN.md`, with the header of your round file and `round: NN`. Three sections.

1. The two theorems. For each, say whether the statement is true as written, whether each step of the proof holds and carries the right label, and whether it is known under another name, with author, venue, year and theorem number where you know them. Try a counterexample to every step you accept. Rerun or extend a check where a constant matters.
2. The amendments. For each amendment the two files propose, by clause number, give ACCEPT, AMEND with the replacement text in full, or REJECT with the reason. From round 02 on, say also whether the editor's integrated statement took each surviving amendment faithfully.
3. Challenges. Name each `ch-<slug>`, say whether it blocks, meaning it would make a statement false or a definition ill-posed, and say what would answer it.

End with this section, exactly in this form:

## Verdicts

```text
VERDICT <theorem-slug> ACCEPT|REVISE|REJECT
AMENDMENTS <accepted> ACCEPT, <amended> AMEND, <rejected> REJECT
BLOCKING <n>
```

one VERDICT line per theorem of the two files. The constraints and writing rules of round 01 hold. If the harness refuses your write, return the full text in your reply. Reply with an abstract of at most 120 words, and `WROTE <path>` or `REFUSED`.

---

Owner step of round NN, to each owner other than the editor.

Owner step of round NN. Read the two reviews of your round-MM file, in `OTHER_A/review-MM.md` and `OTHER_B/review-MM.md`. Write `lab/theory/council/2026-10-30-statement-refinement/OWNER/round-NN.md`, with the header of round 01 and `round: NN`. Four sections.

1. Responses. Answer every challenge raised against your theorem or your amendments, by its slug: conceded with the repair, or answered with the argument.
2. The theorem, its latest version in full, every step labelled. Say what changed since round MM.
3. Amendments to the statement, new or revised, each with the clause number, the replacement text in full and the reason. Withdraw an amendment by saying so.
4. Open points.

If nothing changes in a section, say so in one line. The constraints and writing rules of round 01 hold. If the harness refuses your write, return the full text in your reply. Reply with an abstract of at most 120 words, and `WROTE <path>` or `REFUSED`.

---

Owner step of round NN, to the editor.

Owner step of round NN. You are the editor. Read the reviews of round MM, all six of them, in the three owners' folders.

First write `lab/theory/council/2026-10-30-statement-refinement/statement/round-NN.md`, with the header of round 01, `round: NN` and `role: editor`. It holds the whole statement, starting from `statement/round-MM.md` (round 02 starts from `council/2026-10-29-statement-of-the-theory/statement/final.md`), with every amendment of round MM that no reviewer rejected integrated, merged with the reviewers' amended texts. Mark each changed clause with the round it changed in. After the statement, a section Dissent lists every amendment not taken, with its proposer, its clause and the reason.

Then write your own `batching-removes-class/round-NN.md` as the other owners do, with the sections Responses, The theorem, Amendments and Open points.

The constraints and writing rules of round 01 hold. If the harness refuses a write, return the full text in your reply. Reply with an abstract of at most 150 words, and a `WROTE <path>` or `REFUSED` line for each file.

---

Final step, to the editor.

Final step. Read the reviews of the last round. Write `lab/theory/council/2026-10-30-statement-refinement/statement/final.md`, with the header of round 01, the last round's number and `role: editor`. It holds the statement with the last round's surviving amendments integrated, then a section The theorems that gives each of the three theorems in its last version with its status and the last verdicts on it, then a section Dissent. If the harness refuses your write, return the full text in your reply. Reply with an abstract of at most 150 words, and `WROTE <path>` or `REFUSED`.
