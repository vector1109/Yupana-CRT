# Torsion Vector Specification

## Overview

This document specifies the conceptual role of the torsion vector within the MDST and Yupana CRT framework.

The torsion vector is intended to capture periodic orbital structure inside modular dynamical systems.

---

# 1. Dynamical Context

Consider:

\[
f_k(x)=x^k \bmod n
\]

acting over:

\[
\mathbb{Z}_n
\]

Because the space is finite, every orbit eventually reaches periodic behavior.

---

# 2. CRT Decomposition

Let:

\[
n=\prod_i p_i^{\alpha_i}
\]

Then:

\[
\mathbb{Z}_n
\cong
\prod_i \mathbb{Z}_{p_i^{\alpha_i}}
\]

A state becomes:

\[
x
\leftrightarrow
(x_1,x_2,\dots,x_r)
\]

---

# 3. Local Orbital Periods

Each CRT component may evolve through a local periodic cycle.

Define:

\[
\tau_i(x)
\]

as the local orbital period associated with component:

\[
x_i
\]

under repeated application of:

\[
f_k
\]

---

# 4. Global Torsion Vector

The global torsion descriptor is:

\[
\vec{\tau}(x)
=
(\tau_1(x),\tau_2(x),\dots,\tau_r(x))
\]

This vector captures local cyclic structure across all CRT components.

---

# 5. Interpretation

The torsion vector describes:

- orbital periodicity
- recurrent structure
- phase organization
- asymptotic cyclic behavior

inside the modular phase space.

---

# 6. Relationship to Φ

The operator:

\[
\Phi(x)
\]

provides coarse attractor classification.

The torsion vector provides finer internal organization within attractor basins.

Together they form a richer asymptotic descriptor.

---

# 7. Functional Graph Interpretation

Inside the functional graph:

\[
\mathcal{G}_{n,k}
\]

torsion corresponds to periodic graph structure including:

- cycles
- recurrent cores
- orbital loops
- phase-aligned regions

---

# 8. Computational Interpretation

Potential speculative computational roles include:

- cyclic memory
- recurrent state encoding
- phase synchronization
- orbital-state processing

These interpretations remain exploratory.

---

# 9. Open Problems

Major unresolved questions include:

- uniqueness properties
- compositional structure
- scaling behavior
- algebraic invariants
- categorical interpretation
- complexity implications

---

# 10. Current Status

The torsion vector remains partially formalized.

Its mathematical and computational significance remains under investigation.

