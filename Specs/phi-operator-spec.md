# Φ Operator Specification

## Overview

This document defines the formal operational behavior of the MDST attractor classification operator:

\[
\Phi
\]

as used inside Yupana CRT systems.

---

# 1. Purpose

The Φ operator classifies elements of:

\[
\mathbb{Z}_n
\]

according to their asymptotic dynamical basin under:

\[
f_k(x)=x^k \bmod n
\]

without requiring explicit iterative simulation.

---

# 2. CRT Decomposition

Given:

\[
n=\prod_{i=1}^{r} p_i^{\alpha_i}
\]

CRT decomposition yields:

\[
x \leftrightarrow (x_1,x_2,\dots,x_r)
\]

where each:

\[
x_i \in \mathbb{Z}_{p_i^{\alpha_i}}
\]

---

# 3. Local Classification Rule

For each component:

\[
x_i
\]

define:

\[
\phi_i(x_i)=
\begin{cases}
0 & \text{if } p_i \mid x_i \\
1 & \text{otherwise}
\end{cases}
\]

This produces a binary dynamical signature.

---

# 4. Global Reconstruction

The global operator becomes:

\[
\Phi(x_1,\dots,x_r)
=
CRT(\phi_1(x_1),\dots,\phi_r(x_r))
\]

producing an idempotent element of:

\[
\mathbb{Z}_n
\]

---

# 5. Interpretation

The value:

\[
\Phi(x)
\]

identifies the asymptotic attractor basin associated with:

\[
x
\]

under modular dynamical evolution.

---

# 6. Key Properties

## Deterministic

The mapping is fully deterministic.

---

## Non-Iterative

No orbit simulation is required.

---

## CRT-Local

Evaluation decomposes into independent local rules.

---

## Constant-Time

Execution complexity depends only on the number of CRT components.

---

## Hardware-Compatible

The operator can be implemented through:

- lookup tables
- combinational logic
- branch-free pipelines

---

# 7. Computational Implications

The Φ operator allows:

- basin prediction
- orbit classification
- attractor routing
- modular partitioning
- dynamical indexing

without temporal evolution.

---

# 8. Relationship to Torsion

Φ provides coarse attractor classification.

The torsion vector:

\[
\vec{\tau}(x)
\]

provides fine-grained periodic structure inside the corresponding basin.

Together they define:

\[
(\Phi(x),\vec{\tau}(x))
\]

as a complete dynamical signature.

---

# 9. Research Status

The Φ operator is currently a theoretical construct derived from the MDST framework.

Formal proofs, complexity analysis, and hardware implementations remain active research directions.

