# Phi Classification Operator

## Overview

The Phi operator is a non-iterative classification mechanism introduced within the MDST framework and used by Yupana CRT.

It assigns modular states directly to their asymptotic attractor basins without explicit dynamical simulation.

---

## Dynamical Context

Consider the modular dynamical system:

\[
f_k(x)=x^k \bmod n
\]

with CRT decomposition:

\[
\mathbb{Z}_n
\cong
\prod_i \mathbb{Z}_{p_i^{\alpha_i}}
\]

Each component evolves independently.

---

## Local Classification

For a component:

\[
x_i \in \mathbb{Z}_{p_i^{\alpha_i}}
\]

define:

\[
\phi_i(x_i)=
\begin{cases}
0 & \text{if } p_i \mid x_i \\
1 & \text{otherwise}
\end{cases}
\]

This separates:

- divisors of zero
- unit elements

---

## Global Phi Operator

The global classifier is:

\[
\Phi(x_1,\dots,x_r)
=
\mathrm{CRT}
(
\phi_1(x_1),
\dots,
\phi_r(x_r)
)
\]

where CRT reconstructs the corresponding idempotent attractor.

---

## Interpretation

The operator:

\[
\Phi(x)
\]

identifies the asymptotic attractor basin of a state without iterative evolution.

---

## Key Property

The classification is:

- deterministic
- finite
- algebraic
- non-iterative
- CRT-local

---

## Basin Geometry

The state space partitions into:

\[
\Phi^{-1}(e)
\]

for each idempotent attractor:

\[
e \in E_n
\]

forming attraction basins.

---

## Computational Importance

The Phi operator enables:

- direct asymptotic classification
- bounded evaluation cost
- branch-free attractor inference
- table-driven execution strategies

---

## Relationship to Torsion

Phi provides coarse attractor classification.

The torsion vector:

\[
\vec{\tau}(x)
\]

provides finer periodic structure inside those basins.

Together they form a richer dynamical signature.

---

## Status

Formal theoretical framework under active investigation.