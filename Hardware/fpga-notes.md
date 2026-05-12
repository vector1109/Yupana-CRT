# FPGA Notes — Yupana CRT

## Motivation

Yupana CRT naturally maps to FPGA fabrics due to its fully decomposable modular structure.

The architecture minimizes:

- carry propagation
- global synchronization
- sequential dependency chains

while maximizing:

- locality
- deterministic timing
- spatial parallelism

---

## Fundamental Observation

Each CRT component behaves as an independent execution lane.

Given:

\[
x \leftrightarrow (x_1,\dots,x_r)
\]

each component may execute through:

\[
T_i[a]=f(a)
\]

using local lookup tables.

---

## FPGA Affinity

FPGAs are particularly suitable because they already provide:

- distributed LUT fabrics
- local routing
- parallel execution regions
- deterministic pipelines

Yupana CRT aligns directly with this execution model.

---

## Potential FPGA Mapping

### One Lane per Modulus

Each modulus component may occupy:

- dedicated LUT blocks
- local BRAM
- independent pipelines

---

### Phi Layer

The classifier:

\[
\Phi(x)
\]

can be implemented as:

- direct combinational logic
- lookup structures
- branch-free routing

---

### Torsion Layer

Periodic orbital structures may be represented through:

- cycle-state registers
- finite-state oscillators
- phase counters

---

## Possible Hardware Advantages

### Predictable Timing

Execution latency becomes bounded and deterministic.

---

### Massive Parallelism

All CRT channels execute simultaneously.

---

### Low-Energy Operation

Lookup-driven execution may reduce arithmetic overhead.

---

### Compact Locality

Small modular tables fit naturally inside FPGA memory structures.

---

## Research Questions

- optimal modulus partitioning
- routing complexity
- torsion-aware scheduling
- asynchronous CRT fabrics
- dynamic reconfiguration
- modular neural accelerators

---

## Status

The FPGA direction is theoretical and exploratory.

No synthesis benchmarks are currently claimed.