# Space: hard-problem mappings

Owner: set by the integrator when it starts a session for this space, with the
date. One session at a time.

Discussants: sol only until argon's quota resets (about 2026-10-27 13:30), each
round's summary saying so, then alternating argon and sol.

## Question

Which security problems of learning procedures map onto hard problems already in
the literature, and at what price on each side? Halil, 2026-10-25: "indeed even
better if we can realize hard problems out there in the literature. We need such
mappings". A mapping is a reduction, in either direction, between an attack task
on a learning procedure (membership, attribute or property inference,
reconstruction, extraction, backdoor insertion or detection, unlearning
verification) and a problem whose hardness the literature establishes (planted
clique and planted dense subgraph, LPN, LWE and CLWE, sparse parity, NGCA,
single- and multi-index models with their information, generative and leap
exponents, tensor PCA). Each mapping states the procedure, the attack task, the
hard problem, the direction of the reduction, the price on both sides in the
trainer's units, the regime (statistical-query, low-degree, or polynomial time
under a named assumption), and the experiment that would realize it.

## Scope

In scope: the catalogue of mappings, old and new. The first milestone found two,
blind reconstruction onto NGCA and homogeneous CLWE
(`thm-blind-split-seed-separation`) and label-relevant reconstruction onto the
single-index problem priced by its generative exponent
(`prop-sq-label-relevant-reconstruction-bound`). The literature has others, for
instance the SQ bound for fidelity extraction of random networks (Jagielski et
al., USENIX Security 2020, Theorem 3), backdoors from cryptographic or CLWE
hardness (Goldwasser, Kim, Vaikuntanathan and Zamir), and narcissus resiliency
against one-wayness (Cohen et al.). Placing a cryptographic primitive into a
procedure does not count. A mapping whose hard instance is a data law counts.
Beautiful mathematics comes first (`CONTEXT.md`).

Out of scope: deepening the split-learning separation itself (space
`computational-limits`) and the statistical baselines (space
`statistical-limits`). A mapping that needs one of them names the slug.

## Where to start

- `lib/theory/booklet.pdf`, chapters 4 to 6, and `sink/formalizing/STATE.md`.
- `sink/formalizing/facts.md`, sections: Statistical-computational gaps and
  low-degree models, Learning exponents, Fine-grained and memory-bounded
  cryptography, Restricted-class attackers and usable information, Backdoors and
  undetectability, Extraction, proof of learning and unlearning, Inverting
  networks and the reach of statistical queries.
- `sink/formalizing/problems.md`: `prob-reduce-security-to-known-learning-problems`
  (central), `prob-separation-against-jagielski-sq-bound`,
  `prob-sq-reduction-lwe-encodings`, `prob-comp-mem-reduces-to-hclwe`,
  `prob-reconstruction-hardness-without-one-wayness`, `prob-detection-band-hardness`,
  `prob-delta-extraction-hardness-instance`.
- The library, `lib/literature/notes/<venue>/<Key>.md` and the PDFs beside them.

## Round log

The space session appends one line per round: the folder, the date, the
discussant, the verdict counts and the BLOCKING count.
