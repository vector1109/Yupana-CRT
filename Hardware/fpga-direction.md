# FPGA Direction for Yupana CRT

## Objective

Investigate the feasibility of implementing Yupana CRT as a spatial modular execution architecture on FPGA substrates.

The primary goal is not raw arithmetic throughput, but deterministic dynamical evaluation with constant-latency modular execution.

---

## Why FPGA

FPGA fabrics naturally support:

- independent execution lanes
- lookup-table computation
- modular routing
- fixed deterministic timing
- spatial computation graphs

These properties align directly with CRT decomposition.

---

## Proposed Structure

Each CRT component becomes an independent hardware region:

\[
\mathbb{Z}_n
\cong
\prod_i \mathbb{Z}_{p_i^{\alpha_i}}
\]

Every region contains:

- local lookup tables
- transition evaluators
- torsion metadata
- attractor classification units

---

## Execution Pipeline

### Stage 1 — CRT Decomposition

Input values are decomposed into CRT coordinates.

---

### Stage 2 — Local Evolution

Each component independently evaluates:

\[
x_i \rightarrow x_i^k
\]

through table-driven execution.

---

### Stage 3 — Dynamic Classification

Local hardware extracts:

- basin identity
- attractor signature
- transient depth
- torsion phase

without iterative simulation.

---

### Stage 4 — CRT Reconstruction

Optional recombination produces a global state output.

---

## Architectural Properties

Potential hardware advantages:

- no carry propagation
- branch-free execution
- bounded latency
- high locality
- massive parallelism
- low control overhead

---

## Research Questions

Open problems include:

- optimal LUT packing
- torsion-aware scheduling
- basin compression
- spatial routing efficiency
- energy-per-classification metrics

---

## Long-Term Vision

A Yupana CRT FPGA prototype would act as:

- a modular dynamical processor
- a torsion-aware execution fabric
- a discrete inference accelerator
- a spatial algebraic computing substrate

This direction remains exploratory and research-oriented.

