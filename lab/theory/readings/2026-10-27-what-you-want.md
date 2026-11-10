---
title: "What you want"
subtitle: "A reflection on the aim of the theory, from the discussion of 26 and 27 October 2026"
---

You want a theory of learning in which security and privacy are special cases. Every party, the trainer, the attacker and the auditor, is a learner of some class with a budget, facing an oracle. Its price is what it pays to tell its target apart from structureless randomness, as its own class sees it. Security is a gap between two classes on one learning setup. The prices are measured in the units of computation and learning, and hardness is reached when a measured price meets a proven one. It is never borrowed by planting a cryptographic problem in the data. Section 1 quotes you, section 2 lists what you ruled out, section 3 states my reading of the aim as a theory, and sections 4 to 6 say what exists, where I pushed back, and what the end would look like.

# 1. The aim, in your words

Spelling kept.

> "With cryptographically hard games the bounds I gave are in general far from real cases we get results that are too strong and someone training a shadow model or a VAE etc anything can get practical results which I dont want instead I want to create a measurability here that reagarding the flow of information I want to have a bound on success of such a VAE (or anything) given the setting"

> "attacks on learning algorithms come from other learning algorithms so there is a subclass of problems which we can consider in our reductions"

> "The hope I have in my mind is that wheter we can realize computational efficiency in the field of AI. Because the reason transformer networks work very well is not their sophistication but simplicity in their computation."

> "I dont want to make some hardness results but rather to be able to measure it with the computational terms. Then we will eventually have hardness there too."

> "easy to learn happens with optimality in computation. The other way around may not be working universal"

> "we can introduce modifications to data which will hand us expectations for measurability"

> "develop a more complete theory on the learning theory security and privacy and eventually learning theory itself because in the end we can pose our methodology with the learner itself to measure how well can it learn given a learning setup"

# 2. What you ruled out, and what you allowed

Ruled out:

- Hardness borrowed by planting a known hard problem in the data. In your words, "we are somehow playing a game around seeing lattice problems as learning problems".
- Bounds against unbounded or cryptographic adversaries that a shadow model or a VAE beats in practice.
- A framework that only names things, "just handing a framework for the language in security and privacy".
- Experiments run before the claim they test is stated.
- A list of theorems in place of a theory, and ugly mathematics.

Allowed:

- Modifications of the data or the protocol made by the designer, when they give a known law to compute expectations over. Canaries and release noise are of this kind.
- Approximate structure in place of a sharp planted one, with "hard to learn" as the conclusion in place of exact non-reconstruction.
- Idealized objects, the random oracle among them, when they serve the definitions.

# 3. My reading of the aim as a theory

A *party* is a learner class, a budget, an oracle and a target. Three parties share one learning setup.

- The trainer queries the data and targets the population function.
- The attacker queries the procedure's view, through shadow runs that are Train calls, and targets a secret, such as a record, the training set or a client's weights.
- The auditor queries Train and targets the leakage.

The reference is the random oracle. A family of targets is *pseudorandom for a class* at a budget when no learner of that class with that budget tells it apart from a random oracle. This is the definition of a pseudorandom function with the efficient distinguisher replaced by a learner of the class. A target is learnable by a class exactly when it is not pseudorandom for it. A secret is safe from a class exactly when the channel carrying it is pseudorandom for that class.

The unit is the budget a class needs to leave the random-oracle baseline. For statistical-query and low-degree classes it is set by the degree of the first statistic that departs from the random oracle's, and in Gaussian settings the budget grows as the dimension to half that degree (proven there). In general the statistical dimension of the family replaces the degree (proven, FGRVX17, taken on trust).

Security is the gap. A *learning one-way function* is a setup that is not pseudorandom for the trainer's class while its channel to the attacker is pseudorandom for the attacker's class.

Composition is the calculus. The attacker sees a function of the trainer's output, so what the trainer did not learn can stay pseudorandom to every attacker. The trainer acts as a filter.

A record has two parts. The population part is shared and learnable, and a model that learned it must reveal it. The individual part is a random oracle, so it fools every class, and its leakage is exactly what the model memorized. Canaries realize it by experiment.

Learning theory itself is the trainer's case. A learner's quality in a setup is how far its success rises above the random-oracle baseline, as its own class sees the data. Generalization is the rise on unseen points, and memorization is the rise on the random part.

Hardness lives in the channel, the map from the secret to the law of the attacker's view with the seed as noise. Real data and real training define it without planting. It is hard when its low-degree signal cancels. Symmetry, moment balance, noise and quantization are the mechanisms found so far, and the designer's modifications may add more.

# 4. What already exists toward it

The numbers refer to the reading of 26 October.

- The learning oracle is a lazily sampled random function from seed names to seeds. The named mode queries it at chosen points and the drawn mode at fresh ones (proven, a restatement of its definition). Lazy sampling proves the replay audit, item 6, and programming the oracle is what coupled runs do.
- An unbounded attacker gains nothing from Train calls (proven, item 9). This is why every price needs a named class.
- Item 21 is the first composition theorem. A trainer that reads its data only through statistical queries leaves every SQ-hard secret hidden from every attacker, including an unbounded white-box one (proven).
- Item 20 is the first learning one-way function. The trainer's degree is 2 and the extractor's is 4 (proven, with a heuristic comparison of records against a VSTAT parameter).
- Item 12 shows symmetry raising a degree. The seed-blind rotation cancels the first-degree signal and leaves the second (proven).
- No result yet concerns canaries, the individual part, or a deep nonlinear channel.

# 5. Where I pushed back, and where each point stands

1. Cheap to compute and cheap to learn. An efficient learner outputs a cheap predictor (proven). The converse fails for parities and pseudorandom functions. You accepted this in your rephrasing.
2. White box. Idealized attacker classes fail once the attacker holds the representation. Restricting the trainer goes around this, through composition, but real training memorizes, so the trainer's bound covers the population part only.
3. The random oracle cannot be the data, since a random function teaches the trainer nothing. It cannot be the model, since it erases the simple computation you said matters. Its place is the reference.
4. Random members of an architecture cover a narrow region of functions (heuristic). The relevant law is that of trained models over seeds. The model-stitching literature reports that seeds change representations by nearly linear maps (empirical, not in our library). If that holds, seeds buy only a linear symmetry.
5. Gradient learners of a fixed architecture have no tool beyond embedding in the statistical-query class. Which families fool such a learner is the open core, and it is a question of learning theory.
6. Learning hardness binds universal readers, decoders that must work across many secrets. A targeted attack on one candidate record faces two laws, and only statistical bounds apply to it (proven, elementary).
7. Learning as indistinguishability against a class of distinguishers exists in outcome indistinguishability, multicalibration and pseudoentropy. None of it is in our library or in the searches register. The search has to run before anything is claimed as new.

# 6. What the end would look like

- A definition of pseudorandomness for a learner class, with the three parties and the random-oracle reference.
- A composition theorem that makes the trainer a filter.
- A calculus of degree, saying which mechanism of real training cancels how many degrees of signal.
- Instances on both sides of the gap. Extraction and the orbit exist. Canaries are next. A deep nonlinear channel is open.
- Measurement with a stated target. The oracle measures each party's departure from the random-oracle baseline, the theory proves the other side, and a price is known when the two meet.

Three decisions are yours.

1. Is the three-party frame against a random-oracle reference what you want?
2. Is the gradient learner of a fixed architecture the class to end with, knowing it is the open core?
3. Should the search on outcome indistinguishability and its neighbours run before any definition is written?
