# Positioning

Five slots. Fill every one before writing any methodology. The claim in slot 4
is the claim in `CONTEXT.md` and in the abstract, in the same words.

## 1. Setting

FILL. The problem, the parties, and what each one is assumed to know.

## 2. What exists

FILL. The two or three closest works, by citation key, each with a note under
`lib/literature/notes/`. A work named here without a note is not yet read.

## 3. The gap

FILL. A factual limitation with a pointer to where the work states it or where
it stops. Never "nobody has tried". Say whether the limitation is stated by the
authors or found by us, because those are different facts.

## 4. The claim

FILL. The narrowest claim worth publishing, in one sentence. Carry the
qualifiers that make it true, and carry them here rather than adding them later
under review.

## 5. Why it is hard

FILL. The obstacle that makes the claim non-trivial. If there is none, the gap
is probably already closed.

## Status

Written on FILL. Approved on FILL.

## Searches

Every search of the study in date order, empty results included, logged before
what it found is used. The first two rows were carried on 2026-11-11 from the
search log of the formalizing line, which keeps the earlier searches at
`FORMAL_SECURITY/HE-ML-migrated/sink/formalizing/searches.md`. Grep both before
repeating a search.

| date | slug | question | tool and index | query | scope | hits | kept | coverage | updates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-16 | search-ckks-decryption-leakage | What does CKKS guarantee once decryptions are released, for realizing the ideal releases by threshold CKKS? | Web search, summaries only, index not recorded. Records HE-ML:sink/2026-10-16-formal-tuning/round-01/builder.md and HE-ML:sink/2026-10-16-formal-tuning/round-02/builder.md | CKKS security with released decryptions (query not recorded) | Not recorded | Not recorded | Li and Micciancio, EUROCRYPT 2021, ePrint 2020/1533 (IND-CPA does not suffice, passive key recovery). Li, Micciancio, Schultz and Sorrell, CRYPTO 2022, ePrint 2022/816 (Gaussian noise on decryptions gives IND-CPA-D). Mouchet, Troncoso-Pastoriza, Bossuat and Hubaux, PoPETs 2021, ePrint 2020/304 (multiparty scheme with collective decryption). Feldman and Zrnic, NeurIPS 2021 (abstract read, individual privacy accounting) | Partial, search summaries only and no paper opened, so the realization stays heuristic | none |
| 2026-10-16 | search-threshold-fhe-active-security | Is active security known for threshold FHE decryption, CKKS in particular? | Web search, summary only, index not recorded. Record HE-ML:sink/2026-10-16-formal-tuning/round-03/builder.md, answer to ch-realization-scope | Active security of threshold FHE decryption (query not recorded) | Not recorded | Not recorded | nil for CKKS. Active security exists for thresholdized BFV, BGV and FHEW with an MPC decryption, and CKKS variants only in the passive model (NIST presentation mpts2026-2b5, search summary only) | Partial, one search summary and no paper opened | search-ckks-decryption-leakage |
| 2026-11-11 | search-multi-party-threat-model-systematizations | Is there a systematization of 2025 or 2026 that types every threat model of multi-party learning, privacy and integrity together, for the server and the clients? | WebSearch, extended mode | SoK taxonomy threat models federated learning adversary server clients privacy integrity unified framework 2025 2026 | web, no filter | 9 | CFMPV25 (USENIX Security 2025, eight server threat models), REGB26 (PoPETs 2026, ePrint 2025/2296, client-side and aggregator-side integrity claims), arXiv 2502.03801 (SoK benchmarking FL poisoning, FLPoison, 15 attacks and 17 defenses, venue not verified), Rodríguez-Barroso et al. (Information Fusion 2023, survey). None types privacy and integrity together across roles | Partial, abstracts and snippets only | extends search-attack-taxonomy-landscape and search-newer-settings-sok-sweep |
| 2026-11-11 | search-threat-to-defense-mapping-fl | Which work maps each threat of federated learning to the defense that addresses it, HE, secure aggregation, DP or robust aggregation? | WebSearch, standard mode | systematization mapping federated learning threats to defenses homomorphic encryption secure aggregation differential privacy robust aggregation which defense for which threat | web, no filter | 10 | arXiv 2407.06754 (survey of 2024, relation between threats and defenses), arXiv 2508.13730 (survey of 2025), arXiv 2609.28722 (robustness survey). Descriptive surveys outside the venue rule, none with a realization route per objective | Partial, snippets only | none |
| 2026-11-11 | search-unified-cia-games-2026 | Has a game-based formalism unifying confidentiality, integrity and availability for ML appeared beside SCEKPSTZ23 and VDKMR26? | WebSearch, standard mode, then the arXiv abstract page of 2603.02590 through WebFetch | game-based definitions unify confidentiality integrity availability machine learning attacks cryptographic formalism 2026 arXiv | web, no filter | 10 | SCEKPSTZ23 and VDKMR26 only. VDKMR26 is still v1 of 3 March 2026 with no venue, checked 2026-11-11 | Partial | extends search-attack-taxonomy-landscape |
| 2026-11-11 | search-defense-risk-interactions-sok | Where is Duddu, Szyller and Asokan's SoK on unintended interactions among ML defenses and risks? | WebSearch, standard mode | "SoK: Unintended Interactions among Machine Learning Defenses and Risks" Duddu Szyller Asokan | web, no filter | 10 | IEEE S&P 2024, distinguished paper, arXiv 2312.04542 v2 of April 2024. Overfitting and memorization as the conjectured cause of the interactions. Not in the library | Record found, paper not read | none |
| 2026-11-11 | search-fl-standards-ieee-3652 | Is there a standard for federated learning, and does it fix a threat model? | WebSearch, standard mode | IEEE 3652.1 federated machine learning standard architectural framework security privacy threat model | web, no filter | 10 | IEEE 3652.1-2020, a guide of 69 pages with definitions, categories of federated learning, application scenarios and evaluation criteria. No threat model in any public summary, full text paid | Partial, catalogue pages only | none |
| 2026-11-11 | search-he-mpc-iso-standards | What is the status of the ISO/IEC standards on FHE and on MPC? | WebSearch, standard mode | ISO/IEC 28033 fully homomorphic encryption standard ISO/IEC 4922 secure multiparty computation status | web, no filter | 20 | ISO/IEC 4922-1:2023 (MPC, taxonomy, terminology and processes) and 4922-2:2024 (secret sharing), published. ISO/IEC 28033 (FHE), multipart, Part 1 at DIS stage, replacing the cancelled 18033-8 | Partial, catalogue pages, dates conflict between national bodies | none |
| 2026-11-11 | search-mpc-input-dp-output-framework | Is there a formal framework that joins the input privacy of MPC or HE with the output privacy of DP for training? | WebSearch, standard mode | formal framework combining secure multiparty computation input privacy with differential privacy output privacy for machine learning training definitions | web, no filter | 10 | Pentyala et al. (arXiv 2202.02625, DP training inside MPC, UC for the MPC side), arXiv 1812.03224, arXiv 2010.05867, arXiv 2604.13474, arXiv 1812.02292. nil for a standalone definitional paper | Partial, snippets only | none |
| 2026-11-11 | search-ideal-functionality-aggregate-leakage | How do secure aggregation papers state what the aggregate itself leaks? | WebSearch, standard mode | simulation-based security ideal functionality federated learning definition leakage of the aggregate model formal | web, no filter | 10 | Flamingo (MWAPR23, held), Papaya (arXiv 2111.04877), FedML-HE (arXiv 2303.10837), Starlit (arXiv 2401.10765, explicit leakage function), arXiv 2609.01945 (leakage inherent to the functionality, CKKS only up to bounded error), PrivFL (arXiv 2004.02264). All prove the protocol against an ideal functionality and leave the output's leakage out of scope | Partial, snippets only | none |
| 2026-11-11 | search-crypto-ppml-sok-threat-models | Does a systematization of cryptographic ML (HE, MPC) organize its threat models? | WebSearch, standard mode | SoK cryptographic neural-network computation threat models privacy-preserving machine learning homomorphic encryption MPC systematization | web, no filter | 10 | Podschwadt, Takabi and Hu (arXiv 2112.12855), Azraoui et al. (doi 10.1007/978-3-030-42504-3_5), Zbudila and Suresh (ePrint 2025/1679), Khan et al. (PoPETs 2024). nil for a threat-model taxonomy as a contribution | Partial, snippets only | none |
| 2026-11-11 | search-nist-dp-evaluation-guidelines | What does NIST SP 800-226 fix about the unit of privacy? | WebSearch, standard mode | NIST SP 800-226 guidelines for evaluating differential privacy guarantees unit of privacy | web, no filter | 10 | NIST SP 800-226, March 2025, Near and Darais. Unit of privacy (user level as the default, event level), the DP pyramid, trust models | Partial, secondary summaries, NIST text not opened | none |
| 2026-11-11 | search-source-inference-origin | Where was source inference defined, the attack that asks which client holds a record? | WebSearch, standard mode | source inference attack federated learning Hu ICDM 2021 which client owns training record definition | web, no filter | 10 | Hu et al., ICDM 2021, arXiv 2109.05659, honest-but-curious server, Bayesian analysis. Extended version arXiv 2310.00222. AJP26 and ZSE26 (held) follow it | Partial, abstract only | none |
| 2026-11-11 | search-fl-inference-games-framework | Is there a game framework for inference attacks with several clients? | WebSearch, standard mode | game-based definitions inference attacks federated learning multiple clients membership source property games unified formal framework | web, no filter | 10 | LLLKPMW24 (CCS 2024, held, one game for attribute, property, distributional and user inference from gradients), SCEKPSTZ23 (held, one trained model). nil for one game over membership, source and property across clients | Partial, snippets only | extends search-inference-games-framework |
| 2026-11-11 | search-metadata-checks-frameworks | What are the exact titles and authors of the framework papers the report cites without a note? | WebFetch of five abstract or publication pages | arXiv 2302.09457, 2609.01945, 2109.05659, 2202.02625, and the NIST page of AI 100-2e2025 | the five pages | 5 | Titles and authors of WZLLHL23, MPP26, HSSDZ21, PRMMDND22, VOFADH25. NIST AI 100-2e2025 has six authors, not the four recorded on 2026-08-05. The MPP26 abstract does not carry the inherent-leakage sentence a snippet attributed to it | Complete for metadata | corrects search-ideal-functionality-aggregate-leakage |
