---
key: EKC22
title: "UnSplit: Data-Oblivious Model Inversion, Model Stealing, and Label Inference Attacks Against Split Learning"
authors: Ege Erdoğan and Alptekin Küpçü and A. Ercüment Çiçek
venue: WPES 2022
venue_evidence: first page (WPES '22, November 7, 2022, DOI 10.1145/3559613.3563201); scan summary
year: 2022
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "empirical, convolutional clients on image data"
prov: full-read
---

# EKC22, "UnSplit: Data-Oblivious Model Inversion, Model Stealing, and Label Inference Attacks Against Split Learning"

Read on 2026-10-25 by the computational-limits space session from the held copy
(arXiv 2108.09033): the introduction, Section 3 (threat model, model inversion
and stealing, label inference, Algorithms 1 and 2), Section 4.1 and the model
inversion part of Section 4.2 with Table 2. The defence experiments were read by
their headings only.

## Claim

A split-learning server that knows only the client's architecture can recover
client inputs, a functional clone of the client and the labels, without any
auxiliary data, by optimizing jointly over guessed inputs and guessed weights.

## Method

The attacker initializes a copy $\tilde f_1$ of the client architecture and, given
the client's output $f_1(x)$, alternates gradient steps on the guessed input
$\tilde x$ (minimizing MSE plus $\lambda\,\mathrm{TV}(\tilde x)$, equation 2) and on
the guessed weights $\tilde\theta_1$ (equation 3), a coordinate-descent scheme.
Label inference (Algorithm 2) compares the gradient the client receives with
gradients of a guessed top model for each candidate label. Attack optimizer
Adam at learning rate $10^{-3}$, $\lambda=0.1$ for the first three splits and $1$
after.

## What they measured, and on what

MNIST, Fashion-MNIST and CIFAR10 with small convolutional clients (Figures 2 and
3), split depths 1 to 6, five sets of ten images. Table 2: input MSE before and
after client training and clone accuracy, for example $0.070$ and $0.048$ at depth
1 on MNIST with clone accuracy $97.45$ percent against a reference of $98$, and
average reconstruction errors of $0.084$, $0.149$ and $0.083$ after training on
the three datasets. One to five minutes per input on a laptop CPU.

## Epistemic status

Empirical.

## The limitation that matters to us

The clients are convolutional and the data are natural images, so the result
says nothing about records whose law is close to Gaussian or about fully
connected clients. My finding.

## Relationship to this project

Prior art and a constraint. It shows that hiding the client weights does not
protect image data, a constraint any seed separation must respect.

## What we need to consider for our work

`conj-seed-price-is-ngca-price` predicts this success, since images depart from
Gaussian at low degree. The aim covers fully connected first layers only. A
statement for convolutional clients needs the smaller symmetry group of
convolutions.

## Provenance

Copied on 2026-10-25 from the literature scan of 2026-10-25 (arXiv 2108.09033) for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-00/builder.md.
