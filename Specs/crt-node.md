# CRT Execution Node Specification

## Definition

A CRT node is the fundamental execution unit of the Yupana architecture.

Each node operates over a local modular ring:

\[
\mathbb{Z}_{p^\alpha}
\]

and evolves independently from other nodes.

---

## Node Structure

Each node contains:

| Component | Purpose |
|---|---|
| Local modulus | defines execution domain |
| Transition table | local state evolution |
| State register | current modular state |
| Torsion register | cycle classification |
| Phase register | local orbital phase |

---

## Local Transition

A node computes:

\[
x_{t+1}=f_k(x_t)
\]

through table lookup.

---

## Properties

- constant latency
- no carry propagation
- finite-state complete
- deterministic evolution
- bounded memory footprint

---

## Hardware Mapping

A node may map directly to:

- FPGA LUT blocks
- ASIC modular cells
- SIMD modular lanes
- systolic modular arrays

---

## Long-Term Goal

Networks of CRT nodes form spatial modular processors capable of algebraic dynamical inference.