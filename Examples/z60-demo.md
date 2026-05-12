# Z60 Demonstration

## Objective

This example illustrates the core operational concepts of Yupana CRT using:

\[
\mathbb{Z}_{60}
\]

under the modular dynamical map:

\[
f_2(x)=x^2 \bmod 60
\]

---

## CRT Decomposition

The ring factorizes as:

\[
60 = 2^2 \cdot 3 \cdot 5
\]

therefore:

\[
\mathbb{Z}_{60}
\cong
\mathbb{Z}_4
\times
\mathbb{Z}_3
\times
\mathbb{Z}_5
\]

Each component evolves independently.

---

## Local Dynamics

The global evolution:

\[
x \rightarrow x^2 \bmod 60
\]

becomes:

\[
(x_1,x_2,x_3)
\rightarrow
(x_1^2,x_2^2,x_3^2)
\]

with fully local execution.

---

## Attractor Structure

The system partitions into attractor basins determined by:

\[
\Phi(x)
\]

Each coordinate contributes:

- 0 if divisible by its local prime
- 1 otherwise

This produces the global attractor signature without iterative simulation.

---

## Basin Geometry

The modular phase space forms:

- transient trees
- local cycles
- attractor regions
- torsional structures

inside the CRT topology.

---

## Computational Interpretation

This example demonstrates:

- CRT-local execution
- branch-free modular evolution
- non-iterative classification
- spatial decomposition
- torsion-aware dynamics

---

## Importance

The Z60 system acts as a minimal canonical example where:

- the full geometry is tractable
- attractor basins are explicit
- CRT decomposition is visible
- torsion behavior emerges naturally

---

## Long-Term Role

The Z60 model serves as:

- a reference dynamical system
- a validation environment
- a visualization benchmark
- a hardware prototyping target

for future Yupana CRT experiments.

