# Yupana CRT Execution Primitives

## Overview

Yupana CRT computation is constructed from a small set of modular execution primitives operating independently on CRT-local domains.

These primitives are intended for:

- hardware realization
- FPGA synthesis
- modular inference engines
- spatial dynamical computation

---

## Primitive 1 — Modular State Transition

Given:

\[
f_k(x)=x^k \bmod n
\]

each local component evaluates:

\[
x_i \rightarrow x_i^k \bmod p_i^{\alpha_i}
\]

through direct lookup tables.

---

## Primitive 2 — Attractor Classification

The classification operator:

\[
\Phi(x)
\]

maps a state directly to its asymptotic attractor basin without iterative simulation.

This acts as a dynamical routing primitive.

---

## Primitive 3 — Torsion Extraction

Each component exposes:

\[
\tau_i(x_i)
\]

representing local orbital periodicity.

This provides:

- phase information
- cycle structure
- dynamical memory state

---

## Primitive 4 — Basin Projection

States sharing the same attractor signature are grouped into equivalent execution regions.

This enables:

- compressed state evaluation
- attractor-domain routing
- dynamical partition scheduling

---

## Primitive 5 — CRT Reconstruction

Independent local outputs are recombined through CRT synthesis:

\[
(x_1,\dots,x_r)
\rightarrow
x \in \mathbb{Z}_n
\]

allowing global reconstruction from purely local evolution.

---

## Architectural Interpretation

Together, these primitives define a computational substrate where:

- arithmetic becomes geometric
- execution becomes spatial
- dynamics become classifiable
- iteration becomes optional

---

## Long-Term Direction

Future implementations may expose these primitives directly in:

- FPGA fabrics
- ASIC execution arrays
- modular neural substrates
- torsion-aware processing systems

