# Yupana CRT Execution Model

## Overview

Yupana CRT executes computation through independent modular channels derived from CRT decomposition.

Instead of sequential arithmetic with carry propagation, the system operates through parallel local state transitions.

---

## Representation

Given:

\[
n=\prod_{i=1}^{r} p_i^{\alpha_i}
\]

a value is represented as:

\[
x \leftrightarrow (x_1,x_2,\dots,x_r)
\]

with:

\[
x_i \in \mathbb{Z}_{p_i^{\alpha_i}}
\]

---

## Local Execution Tables

Each component possesses a precomputed transition table:

\[
T_i[a]=f(a)
\]

For exponent dynamics:

\[
f_k(a)=a^k \bmod p_i^{\alpha_i}
\]

Execution becomes:

- direct lookup
- constant latency
- branch-free
- cache-local

---

## Global Evolution

The global state transition is:

\[
f(x_1,\dots,x_r)=
(T_1[x_1],\dots,T_r[x_r])
\]

No component interacts with another during execution.

---

## Execution Properties

### Deterministic Timing

All transitions execute in bounded time independent of input value.

---

### No Carry Chains

Classical arithmetic bottlenecks disappear.

No global propagation exists.

---

### Parallelism

Each CRT channel may execute:

- simultaneously
- asynchronously
- spatially distributed

---

## Dynamical Interpretation

Execution is interpreted as motion through a finite dynamical graph.

The system naturally supports:

- attractor convergence
- cycle detection
- torsion dynamics
- basin classification

---

## Phi Layer

The MDST classification operator:

\[
\Phi(x)
\]

acts as a non-iterative attractor oracle.

This enables direct classification of asymptotic behavior without simulation.

---

## Torsion Layer

The torsion vector:

\[
\vec{\tau}(x)
\]

encodes periodic orbital structure.

This introduces an additional computational degree of freedom beyond nominal values.

---

## Hardware Implications

Potential implementation targets include:

- FPGA modular fabrics
- ASIC execution arrays
- low-energy inference accelerators
- modular neural substrates

---

## Status

The execution model is currently theoretical and exploratory.