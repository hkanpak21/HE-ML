> Superseded on 2026-10-16 by `ledger.csv` and `screening.csv`. Kept as the record of the first 44 papers' coding.

# Catalog

Every paper placed for the HE-ML study, coded on the adversary interface of
`lib/reports/2026-10-16-halil-adversary-interface.pdf`. Who is the adversary,
what it sees, what it chooses, and which of the three goals it plays:
distinguish (a discriminator), invert (function inversion) or steer (choosing
inputs so the trained model lands in a target set). The codes come from the
sweep reports and from no full reading. Every note is `prov: sweep` until a
person reads the paper.

The PDF of each row is `pdfs/<Key>_<ShortTitle>.pdf` in `My Drive/HE-ML/`.
Seven PDFs came through the KU library on 2026-10-16. Every row now has its PDF.

## The group's own work

| Key | Paper | Venue | Adversary sees | Adversary chooses | Goal | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| KSK26 | HE-OFT: Privacy-Preserving One-Shot Federated Fine-Tuning under Homomorphic Encryption | arXiv 2610.08255 | semi-honest server and t−1 clients: ciphertexts, counts n_j, one index, own labels | deviating clients (honest server): uploads, shares, arbitrary feature queries | distinguish, bounded by Q_tot label queries and by the head in plaintext; a deviating server is proven necessary to exclude; steering not claimed | proven under a smudging hypothesis the measured setting does not meet; empirical leakage. Full read |

## Malicious server or aggregator

| Key | Paper | Venue | Adversary sees | Adversary chooses | Goal | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| PFA22 | Eluding Secure Aggregation in Federated Learning via Model Inconsistency | CCS 2022 | the sum of updates (secure aggregation) | a different model for each client | invert, distinguish | empirical |
| GDJV24 | Hiding in Plain Sight: Disguising Data Stealing Attacks in Federated Learning (SEER) | ICLR 2024 | the sum of updates, auxiliary data | a learned model and a secret decoder | invert, while passing client checks | empirical |
| ZSEEAB24 | LOKI: Large-scale Data Reconstruction Attack against Federated Learning through Model Manipulation | S&P 2024 | the sum of updates | an inserted module, per-client kernels | invert | empirical |
| GZZVZPW26 | ARES: Scalable and Practical Gradient Inversion Attack in Federated Learning through Activation Recovery | S&P 2026 | each update, or the sum | weights and biases, not the architecture | invert | proven under RIP, empirical |
| LAWKDM26 | Memory Backdoor Attacks on Neural Networks | NDSS 2026 | each client's local model | the training code clients run | invert whole datasets | empirical |
| NVNT25 | Theoretically Unmasking Inference Attacks Against LDP-Protected Clients in Federated Vision Models | ICML 2025 | updates through an LDP channel | FC or attention weights | distinguish | proven lower bounds |
| EZL26 | Poison to Detect: Detection of Targeted Overfitting in Federated Learning | PoPETs 2026 | each update | the aggregation schedule per target | distinguish, invert (later); defence is a client discriminator | empirical |
| JYHWCL24 | Lotto: Secure Participant Selection against Adversarial Servers in Federated Learning | USENIX Sec 2024 | the sum of updates | the cohort, Sybils, colluding clients | defence: bound the corrupted fraction of the cohort | proven tail bound |
| CFMPV26 | On the Detectability of Active Gradient Inversion Attacks in Federated Learning | S&P 2026 | each update | the model's parameters | defence: client discriminator against chosen models | empirical, CNNs |
| ZDTLL26 | When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems | USENIX Sec 2026 | the aggregate | the released model, after an honest protocol | invert, then steer (backdoor) | empirical, 7B and 8B LLMs |

## Malicious clients

| Key | Paper | Venue | Adversary sees | Adversary chooses | Goal | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| SHKR22 | Back to the Drawing Board: A Critical Evaluation of Poisoning Attacks on Production Federated Learning | S&P 2022 | own data, or the global model | own data or own update, at production fractions | steer (untargeted) | empirical |
| FNLSIY25 | Do We Really Need to Design New Byzantine-robust Aggregation Rules? | NDSS 2025 | every update and the rule | own update, 20% colluding | steer | proven (convex), empirical |
| LK25 | On Hyperparameters and Backdoor-Resistance in Horizontal Federated Learning | CCS 2025 | the global model, broadcast hyperparameters | own update | steer (backdoor) | empirical |
| CKS24 | Attacking Byzantine Robust Aggregation in High Dimensions | S&P 2024 | every vector and the aggregator | own updates, a fraction | steer (untargeted) | proven bias bound, empirical |
| KKDK24 | Automatic Adversarial Adaption for Stealthy Poisoning Attacks in Federated Learning | NDSS 2024 | server code and the defence | own update, up to 45% | steer under the defender's discriminator | empirical |
| AFGGPRV24 | Byzantine-Robust Federated Learning: Impact of Client Subsampling and Local Updates | ICML 2024 | everything | own update, fewer than half | steer | proven |
| BLGB26 | Tight Stability Bounds for Robust Distributed Learning | ICML 2026 | the honest distributions | own data against own update | steer; separation between the two choices | proven (convex) |
| RT25 | On the Conflict between Robustness and Learning in Collaborative Machine Learning | S&P 2025 | the aggregator | own update | steer against the defender's discriminator | proven |
| AGGPS23 | On the Privacy-Robustness-Utility Trilemma in Distributed Learning | ICML 2023 | everything (clients), the updates (curious server) | own update | steer, and distinguish under DP | proven lower bound |
| GLX25 | DP-BREM: Differentially-Private and Byzantine-Robust Federated Learning with Client Momentum | USENIX Sec 2025 | the system | own data and update, a minority | steer; distinguish under DP against a malicious server | proven |
| VMBKN25 | Practical Poisoning Attacks with Limited Byzantine Clients in Clustered Federated Learning | S&P 2025 | own data | own updates, few clients | steer | empirical |

## Language models, split and vertical learning

| Key | Paper | Venue | Adversary sees | Adversary chooses | Goal | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| PDBMV24 | DAGER: Exact Gradient Inversion for Large Language Models | NeurIPS 2024 | each update, LoRA included (curious server) | nothing | invert text | empirical, exact below a token count |
| RDGSM26 | Gradient-Free Privacy Leakage in Federated Language Models through Selective Weight Tampering | PoPETs 2026 | the global model each round (a client) | its own weights | distinguish, invert other clients' data | empirical |
| YCLYWC25 | Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models | ICLR 2025 | public data | own data, 3 of 10 clients | steer (remove safety alignment) | empirical, Llama2-7B LoRA |
| TTPLHLCL26 | Ghost in the Cloud: Your Geo-Distributed Large Language Models Training is Easily Manipulated | ICLR 2026 | the global model | own update | steer (trigger jailbreak) under detection | empirical |
| CQYZFDX24 | Unveiling the Vulnerability of Private Fine-Tuning in Split-Based Frameworks for LLMs | CCS 2024 | activations and gradients (curious split server) | nothing | invert prompts | empirical |
| PAB21 | Unleashing the Tiger: Inference Attacks on Split Learning | CCS 2021 | activations | the loss that trains the client layers | invert | empirical |
| RPKAKS25 | SafeSplit: A Novel Defense Against Client-Side Backdoor Attacks in Split Learning | NDSS 2025 | its own parts of the model | data, labels, activations, gradients | steer (backdoor); defence | empirical |
| YLGHP25 | URVFL: Undetectable Data Reconstruction Attack on Vertical Federated Learning | NDSS 2025 | passive parties' embeddings | the gradients it returns | invert features, while passing detection | empirical |

## Systematizations

| Key | Paper | Venue | What it types |
| --- | --- | --- | --- |
| CFMPV25 | SoK: Gradient Inversion Attacks in Federated Learning | USENIX Sec 2025 | eight server threat models, from eavesdropper to active manipulator |
| DHWSGRC25 | SoK: On Gradient Leakage in Federated Learning | USENIX Sec 2025 | six levels of server knowledge, malicious server called over-assumed |
| REGB26 | SoK: Verifiable Integrity Claims for Privacy-Preserving Federated Learning | PoPETs 2026 | aggregator and clients typed separately as curious and Byzantine |

## Cryptographic protocols under malicious parties

In the interface these papers act on the channels and on the choice set. A
zero-knowledge proof of honest computation shrinks the choice set back toward
the semi-honest one. Input validation confines a client's update to a norm
ball, which bounds the set it can steer toward. The CPA-D attacks show that a
decryption channel for approximate HE also carries information about the
secret key.

| Key | Paper | Venue | Adversary | Guarantee against it | Evidence |
| --- | --- | --- | --- | --- | --- |
| HLSS25 | Practical Zero-Knowledge PIOP for Maliciously Secure Multiparty Homomorphic Encryption | CCS 2025 | malicious MHE parties | ZK proofs that keys and ciphertexts are well formed, with abort. The abstract names no proof of decryption shares | proven, empirical |
| CMSPTH23 | PELTA: Shielding Multiparty-FHE against Malicious Adversaries | CCS 2023 | malicious MHE parties (BFV-based MHE) | deviation in MHE operations detected by lattice commitments and ZK. No input validity | construction |
| CSBB24 | On the practical CPAD security of "exact" and threshold FHE schemes and libraries | CRYPTO 2024 | passive, with a decryption oracle on honest ciphertexts | none: key recovery. Threshold BFV, BGV and CKKS are exposed through partial decryptions | proven attack, empirical |
| HHKLS26 | On the (In)security of Approximate Computation Protocols from CKKS | ASIACRYPT 2026 (ePrint field only) | semi-honest corrupted set in threshold CKKS | independent per-party smudging is not simulation secure. Jointly sampled noise is | proven |
| GNSJ24 | Key Recovery Attacks on Approximate Homomorphic Encryption with Non-Worst-Case Noise Flooding Countermeasures | USENIX Sec 2024 | passive, sees CKKS decryption outputs | none: flooding sized from average-case noise fails | empirical (OpenFHE) |
| ZZLP25 | High-Throughput Universally Composable Threshold FHE Decryption | CCS 2025 | malicious decryptors | UC threshold decryption without flooding, exact schemes only | proven UC |
| BGLLMRY23 | ACORN: Input Validation for Secure Aggregation | USENIX Sec 2023 | malicious server and a fraction of malicious clients | privacy of the sum and ZK norm bounds, with abort. Guaranteed output needs a semi-honest server | proven (ROM) |
| GKKTW26 | Lighthouse: Single-Server Secure Aggregation with O(1) Server-Committee Communication at Scale | USENIX Sec 2026 | malicious server, clients, committee minority | privacy of the sum, with abort. Input validity out of scope. Shows proof gaps in Flamingo and TACITA | proven (ROM) |
| JZDK25 | AlphaFL: Secure Aggregation with Malicious² Security for Federated Learning against Dishonest Majority | PoPETs 2025 | one of two servers, with clients | UC security with abort, and norm checks | proven (UC) |
| FDCTKRFJPW23 | Robust and Actively Secure Serverless Collaborative Learning | NeurIPS 2023 | malicious peers, honest-majority committee | correctness, confidentiality, robustness of the chosen aggregator | proven, conditional |
| ZWQWWLSYYZJZ26 | ZKSL: Verifiable and Efficient Split Federated Learning via Asynchronous Zero-Knowledge Proofs | NDSS 2026 | every party malicious, colluding | integrity of each party's computation by PLONK proofs. No privacy | proven (game) |
