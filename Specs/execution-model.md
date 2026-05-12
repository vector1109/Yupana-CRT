# Yupana CRT Execution Model

## Objective

The Yupana CRT execution model defines a computational architecture based on modular decomposition, local dynamical evaluation, and spatially distributed execution.

The goal is to replace globally coupled arithmetic pipelines with independent modular execution domains.

---

# 1. Fundamental Representation

A value:

\[
x \in \mathbb{Z}_n
\]

is represented through CRT coordinates:

\[
x \leftrightarrow (x_1,x_2,\dots,x_r)
\]

where:

\[
n=\prod_i p_i^{\alpha_i}
\]

Each coordinate belongs to an independent modular component.

---

# 2. Local Execution Principle

Each component evolves independently under:

\[
f_k(x_i)=x_i^k \bmod p_i^{\alpha_i}
\]

No global carry propagation exists between components.

Execution becomes:

- local
- bounded
- deterministic
- spatially parallel

---

# 3. Table-Driven Evaluation

Each modular domain stores precomputed transition tables:

\[
T_i[a]=f_k(a)
\]

This enables:

- constant-time state evolution
- branch-free execution
- predictable timing
- hardware locality

---

# 4. Execution Pipeline

## Stage 1 — CRT Projection

Input values are decomposed into modular coordinates.

---

## Stage 2 — Local Evolution

Each coordinate evolves independently using local lookup tables.

---

## Stage 3 — Dynamical Classification

The operator:

\[
\Phi(x)
\]

classifies asymptotic behavior without iterative simulation.

---

## Stage 4 — Torsion Evaluation

Optional torsion analysis computes:

\[
\vec{\tau}(x)
\]

to determine periodic orbital structure.

---

## Stage 5 — Reconstruction

CRT recombination reconstructs global system state when required.

---

# 5. Architectural Properties

## Deterministic Latency

Execution cost depends only on table access.

---

## Carry-Free Arithmetic

No long carry chains exist.

---

## Parallel Modularity

Each component can map to:

- independent cores
- FPGA regions
- SIMD lanes
- ASIC arrays

---

## Cache Locality

Tables may reside entirely inside:

- L1 cache
- BRAM blocks
- local SRAM

for bounded modular domains.

---

# 6. Dynamical Computation

The system treats computation as evolution over finite phase spaces.

This introduces:

- attractor-guided execution
- phase-aware states
- orbital memory
- torsion-sensitive dynamics

as computational primitives.

---

# 7. Potential Hardware Mapping

The execution model naturally aligns with:

- FPGA fabrics
- modular systolic arrays
- spatial accelerators
- low-power inference hardware

---

# 8. Research Status

The execution model is currently theoretical.

No complete hardware implementation exists at present.

Its feasibility, efficiency, and scaling behavior remain active research topics.

