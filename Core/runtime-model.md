# Yupana CRT Runtime Model

## Execution Model

The Yupana runtime evaluates modular dynamics through local state transitions.

A global state is represented as a CRT tuple:

\[
x \leftrightarrow (x_1,\dots,x_r)
\]

Each component evolves independently according to a local transition table.

---

## Local Execution

For each modulus:

\[
T_i[a]=a^k \bmod p_i^{\alpha_i}
\]

Runtime evaluation becomes:

1. component lookup
2. local transition
3. optional CRT reconstruction

No iterative exponentiation is required during execution.

---

## Runtime Properties

| Property | Result |
|---|---|
| Carry propagation | eliminated |
| Branching | minimized |
| Latency | deterministic |
| Parallelism | intrinsic |
| Memory locality | high |

---

## Dynamic State Classification

Future versions integrate:

- Φ attractor classification
- modular torsion tracking
- phase synchronization
- torsional memory states

---

## Long-Term Goal

A fully spatial modular runtime architecture capable of discrete dynamical inference.