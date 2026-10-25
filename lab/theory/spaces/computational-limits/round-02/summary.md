# Round 02, summary

Space `computational-limits`, 2026-10-25. Discussant argon (gemini-4-argon-medium,
the model `discuss.sh` now uses), back in the README alternation after round 01's
fallback to astra. Verdicts: ACCEPT 7, REVISE 0, REJECT 0. BLOCKING 0. The space
stops here, under the brief's rule for the first round from 01 on with BLOCKING 0.

The round repaired the seven objects of round 01 that astra marked REVISE or
REJECT and answered its ten blocking challenges by name. The covariance of the
pancake law now carries a deficit of at most $3(\gamma^2+1)e^{-\pi\gamma^2}$ along the
hidden direction (BRST21 Lemma 7.2 and Corollary 7.3), and both pancake
propositions use it. The SQ price of blind reconstruction from a frozen client
is explicit: at least $\frac{11}{288}M\tau_*^2\beta^2/\gamma^2-d$ statistical
queries with $M=\exp(\Omega(c_0^4d))$, under stated margins. The label-side lower
bound is written out for randomized attackers with the diagonal correlation
$I_{\chi^2}[P]$, the square-root code overlap of DPLB24 Lemma E.3 and a fixed
query exponent, and gives $n\ge c\,d^{k^*/2}$. The seed-known clause for trained
clients is restricted to representations computed under the initial weights. The
conjecture is restated for recoverable frozen clients and an isotropic hidden law.
Argon checked each repair line by line and accepted all seven. Its review
misnames the authors of CGJMMT21 (it lists other names). The fact stands with the
authors read from the paper's first page: Carlini, Garg, Jha, Mahloujifar,
Mahmoody and Tramèr. Argon's review was less adversarial than astra's. The
integrator's line-by-line re-derivation (gate G8) should weigh that.

## Slugs accepted

- `fact-clwe-hardness`
- `fact-ideal-keyed-encoding-weak-learner`
- `prop-sq-blind-reconstruction-bound`
- `prop-fine-reconstruction-to-hclwe`
- `thm-blind-split-seed-separation`
- `conj-seed-price-is-ngca-price`, accepted as a well-posed open conjecture
- `prop-sq-label-relevant-reconstruction-bound`

## Challenges open

None blocking. None raised in this round. The two wording corrections to the
accepted `def-seed-blind-reconstruction-game` and
`thm-reconstruction-from-conditional-mean`, listed in this round's `builder.md`,
wait for the integrator to apply at merge.

## For the registers

Corrections and pointers.

- `fact-clwe-hardness`: the covariance of $H_{w,\beta,\gamma}$ is $I/(2\pi)$ on $w^\perp$
  and $1/(2\pi)-\Delta$ along $w$ with $0\le\Delta\le3(\gamma^2+1)e^{-\pi\gamma^2}$, a
  deficit, from BRST21 Lemma 7.2 and Corollary 7.3. Supersedes the excess stated
  in round 01.
- `fact-ideal-keyed-encoding-weak-learner`: CGJMMT21 Theorem 1 assumes
  $(1/2-\varepsilon,\delta)$ balanced error for constants $0<\varepsilon,\delta<1/2$.
- `fact-generative-exponent-sq-recovery-bound`: DPLB24 Lemma 2.3
  ($I_{\chi^2}[P]=\sum_k\lambda_k^2$), the series in the proof of Lemma E.2, and Lemma
  E.3 (code overlap $\sqrt{C\log_d(m)^2/d}$ for $m\le d^{d^{1/4}}$). The proof of
  Theorem 3.2 takes the diagonal correlation bound to be $1$, which the class
  $\mathcal G$ does not guarantee.

Results for `results.md`, with the round that accepted each.

| slug | kind | status | accepted in |
| --- | --- | --- | --- |
| `thm-fs-sq-black-box-reduction` | theorem (FORMAL_SECURITY) | refuted, counterexample in round-00 `builder.md` | round 00 |
| `lem-sq-learner-post-processing` | lemma | proven | round 00 |
| `def-seed-blind-reconstruction-game` | definition | proposed, with the wording correction of round 02 | round 01 |
| `lem-equivariant-view-coupling` | lemma | proven, the induction of LZA21 Theorem C.1 | round 01 |
| `lem-whitening-gives-rotated-records` | lemma | proven | round 01 |
| `thm-reconstruction-from-conditional-mean` | theorem | proven, with the wording correction of round 02 | round 01 |
| `conj-reconstruction-at-training-cost` | conjecture | refuted as stated (part b), superseded | round 01 |
| `prop-sq-blind-reconstruction-bound` | proposition | proven (a), proven conditional on DKRS23 Theorem 1.5 (b) | round 02 |
| `prop-fine-reconstruction-to-hclwe` | proposition | proven, conditional hardness under BRST21 Corollary 4.2 | round 02 |
| `thm-blind-split-seed-separation` | theorem | proven | round 02 |
| `prop-sq-label-relevant-reconstruction-bound` | proposition | proven | round 02 |
| `conj-seed-price-is-ngca-price` | conjecture | open, lower inclusion settled in the stated cases, upper inclusion for frozen linear clients | round 02 |

None needs the learning oracle. Each reduction costs one honest training run.
All are unchecked by a person.

Problem status changes proposed.

- `prob-split-learning-seed-separation`: open to partial. Proven for pancake
  records and Gaussian-initialized ReLU clients trained by orthogonally
  equivariant updates (`thm-blind-split-seed-separation`): exact seed-known
  inversion against an exponential SQ price (frozen clients) and a worst-case
  lattice price for fine reconstruction (frozen or trained). Open: natural record
  laws, convolutional clients, Adam, coarse reconstruction in polynomial time.
- `prob-split-transcript-leaks-seed`: open to solved for the protocol class
  $\mathcal P_H$: the server's whole view is a function of rotated records and fresh
  coins (`lem-equivariant-view-coupling`). Outside the class it stays open.
- `prob-statistical-queries-for-regression`: open to partial. A reconstruction
  measured by correlation becomes a direction with $d$ truncated queries of
  tolerance $\tilde O(d^{-1/2})$ and reaches search lower bounds (both SQ
  propositions).
- `prob-attacker-lower-bound-from-hard-learning`: partial, on a new basis. The
  FORMAL_SECURITY proof note is refuted (round 00). Inversion attackers of split
  learning are now bounded by SQ and lattice hardness for pancake records, and by
  the generative exponent for the label-relevant coordinate.
- `prob-reduce-security-to-known-learning-problems`: two reductions exist in this
  space. Blind reconstruction reduces to NGCA and hCLWE, and reconstruction of the
  label-relevant coordinate is the single-index problem priced by $k^*$.

New problems.

- `prob-blind-inversion-relu-clients` (supporting): can a seed-blind server
  invert an expansive Gaussian ReLU client from representations of an isotropic
  record law at polynomial cost, learning the client up to rotation? This is the
  open upper inclusion of `conj-seed-price-is-ngca-price`. Posed by this space,
  2026-10-25.
- `prob-coarse-reconstruction-lattice-hardness` and
  `prob-reconstruction-hardness-without-one-wayness`, posed in the round-00
  summary, stay open.

New search rows: none in this round.

Decisions for Halil, from this round's `builder.md`. The first target, the
attacker class (two games, never mixed), and whether a separation whose hard
instance is a record law meets the rule that a cryptographic plug-in does not
count.
