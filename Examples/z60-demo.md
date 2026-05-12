# Z60 Demonstration

## System

We consider the modular dynamical system:

\[
f_2(x)=x^2 \bmod 60
\]

with CRT decomposition:

\[
60=2^2 \cdot 3 \cdot 5
\]

thus:

\[
\mathbb{Z}_{60}
\cong
\mathbb{Z}_4
\times
\mathbb{Z}_3
\times
\mathbb{Z}_5
\]

---

## CRT Representation

Each value:

\[
x \in \mathbb{Z}_{60}
\]

is represented as:

\[
(x_4,x_3,x_5)
\]

where:

- \(x_4 \in \mathbb{Z}_4\)
- \(x_3 \in \mathbb{Z}_3\)
- \(x_5 \in \mathbb{Z}_5\)

---

## Local Dynamics

The system evolves independently inside each component:

\[
(x_4,x_3,x_5)
\mapsto
(x_4^2,x_3^2,x_5^2)
\]

No cross-component interaction exists.

---

## Phi Classification

The MDST classifier:

\[
\Phi(x)
\]

assigns each state directly to its asymptotic attractor basin.

This classification occurs without iterative simulation.

---

## Observed Properties

### Attractor Classes

The system contains:

\[
2^3=8
\]

idempotent attractor classes.

---

### Basin Structure

The state space partitions into non-uniform attraction basins.

---

### Finite Depth

All trajectories converge within bounded depth.

---

### Functional Graph

The graph structure contains:

- fixed points
- transient trees
- local cycles

---

## Torsion Structure

Certain CRT components exhibit periodic orbital behavior inside unit groups.

These cycles define modular torsion.

---

## Computational Interpretation

The Z60 system demonstrates:

- CRT-local execution
- direct attractor classification
- finite dynamical geometry
- modular torsion behavior
- non-iterative asymptotic inference

---

## Importance

Z60 acts as the canonical minimal demonstrator for:

- MDST
- Yupana CRT
- modular attractor systems
- torsion-aware computation