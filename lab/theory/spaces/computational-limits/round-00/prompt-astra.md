You are the discussant in round 00 of the thinking space computational-limits of a research
project on the security of learning procedures. You only read and discuss. You
do not write or edit any file. Your whole answer is your reply.

Read these files first, in this order, from the repository root:

1. `lab/theory/CONTEXT.md`, the shared context, binding on you.
2. `lab/theory/spaces/computational-limits/README.md`, this space's question and scope.
3. No earlier round exists. This is the literature round.
4. `lab/theory/spaces/computational-limits/round-00/builder.md`, the builder's turn you judge.
5. `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/.tools/proof.tex`, the proof note the builder judges.
6. Text extracts of the papers the builder cites, for checking theorem numbers, in
   `/private/tmp/claude-501/-Users-a90-Documents-RESEARCH-HE-ML/cac3b537-be30-4d8a-9863-e3334d671e3c/scratchpad/txt/`
   (one `.txt` per library key, for example `FGRVX17_StatisticalAlgorithmsLowerBound.txt`,
   `AKMSS21_PowerDifferentiableLearningVersus.txt`, `BRST21_ContinuousLWE.txt`,
   `DPLB24_ComputationalStatisticalGapsGaussian.txt`, `LJDD19_InvertingDeepGenerativeModels.txt`,
   `CDGJMMSTT21_IsPrivateLearningPossible.txt`, `CKMMNST25_DataReconstructionWhenYou.txt`,
   `NRNT25_AchievingDataReconstructionHardness.txt`). Spot-check rather than read them whole.

Your role. Judge every object of the builder's turn by its slug. For each one,
say whether the statement is true as written, whether the proof or sketch holds
line by line, whether its hypotheses are the right ones, and whether it is
non-trivial under the constraints of `CONTEXT.md` (a cryptographic plug-in does
not count, every quantity must be measurable by experiment). For a literature
claim, say whether the cited paper proves it, under which hypotheses, and what
the builder missed that you know of, with author, venue, year and theorem number
where you know them. Label each of your own claims proven, heuristic, empirical
or open. Name each challenge `ch-<slug>` and say whether it blocks, meaning it
would make a statement false or a definition ill-posed.

The question of this round. Is the builder's refutation of the proof note's
main theorem correct, in particular the counterexample (a learner that reads the
graph through exact or honestly sampled vertex averages with O(n^2) queries of
constant tolerance), and is the repaired lemma the right residue? Are the
literature facts stated with the hypotheses the papers carry? Are the three aims
true or plausible as stated, non-trivial, and new: in particular, is the claim
that a rotation-invariant initialization with a rotation-equivariant update
makes the split-learning server's view simulable from rotated records, so that
blind reconstruction reduces to non-Gaussian component analysis on the record
law, already known (for example from the literature on orthogonally equivariant
training of fully connected networks, rotation perturbation in privacy-preserving
data mining, or InstaHide and NeuraCrypt analyses)? Is the proposed attacker
class for lower bounds the right one given the regime limit of Abbe et al.?

End your reply with this section, exactly in this form, one VERDICT line per
object of the builder's turn and one BLOCKING line counting the blocking
challenges you raised:

## Verdicts

```text
VERDICT fact-fgrvx17-planted-clique-sq-bound ACCEPT|REVISE|REJECT
VERDICT fact-sq-simulates-minibatch-sgd ACCEPT|REVISE|REJECT
VERDICT fact-lei-random-expansive-layers-invertible ACCEPT|REVISE|REJECT
VERDICT fact-clwe-hardness ACCEPT|REVISE|REJECT
VERDICT fact-hclwe-sq-correlation-bound ACCEPT|REVISE|REJECT
VERDICT fact-ngca-sq-lower-bound ACCEPT|REVISE|REJECT
VERDICT fact-generative-exponent-sq-recovery-bound ACCEPT|REVISE|REJECT
VERDICT fact-ica-breaks-rotation-perturbation ACCEPT|REVISE|REJECT
VERDICT fact-instance-encoding-privacy-learnability ACCEPT|REVISE|REJECT
VERDICT fact-ideal-keyed-encoding-weak-learner ACCEPT|REVISE|REJECT
VERDICT fact-cohen-narcissus-equals-one-wayness ACCEPT|REVISE|REJECT
VERDICT fact-unsplit-unknown-client-inversion ACCEPT|REVISE|REJECT
VERDICT fact-nrnt25-private-layer-hardness-route ACCEPT|REVISE|REJECT
VERDICT thm-fs-sq-black-box-reduction ACCEPT|REVISE|REJECT
VERDICT lem-sq-learner-post-processing ACCEPT|REVISE|REJECT
VERDICT def-seed-blind-reconstruction-game ACCEPT|REVISE|REJECT
VERDICT conj-seed-price-is-ngca-price ACCEPT|REVISE|REJECT
VERDICT conj-reconstruction-at-training-cost ACCEPT|REVISE|REJECT
BLOCKING <n>
```

For thm-fs-sq-black-box-reduction, ACCEPT means you accept the builder's
verdict that the proof note's theorem is refuted as stated. Each VERDICT line
must name one of ACCEPT, REVISE or REJECT, and BLOCKING must be a single integer.
