# FPGA Local Kernels

## Overview

This document describes the concept of FPGA-local execution kernels within the Yupana CRT framework.

The central idea is that CRT-decomposed modular dynamics may map naturally onto spatial FPGA fabrics composed of independent local processing regions.

---

# 1. Motivation

Conventional arithmetic hardware relies heavily on:

- carry chains
- centralized arithmetic units
- global synchronization
- sequential propagation

Yupana CRT instead explores localized modular evolution.

---

# 2. CRT Decomposition

Given:

\[
n=\prod_i p_i^{\alpha_i}
\]

the modular state space factorizes as:

\[
\mathbb{Z}_n
\cong
\prod_i \mathbb{Z}_{p_i^{\alpha_i}}
\]

Each CRT component becomes a local execution domain.

---

# 3. Local Kernel Definition

An FPGA-local kernel is a bounded execution region responsible for:

- local modular evolution
- lookup evaluation
- orbital updates
- asymptotic classification
- torsional tracking

inside a single CRT coordinate domain.

---

# 4. Local Evolution Rule

Each kernel evolves independently according to:

\[
x_i \to x_i^k
\]

inside its modular subspace.

Global evolution emerges through CRT composition.

---

# 5. Lookup-Driven Execution

Execution may rely on local lookup structures:

\[
T_i[a]=f(a)
\]

stored directly inside FPGA block RAM or distributed logic.

Potential consequences include:

- deterministic latency
- branch-free evaluation
- bounded execution depth
- localized memory access

---

# 6. Spatial Parallelism

Because CRT domains evolve independently, kernels may execute simultaneously across FPGA fabric regions.

This supports:

- distributed modular execution
- local synchronization
- spatial computation
- parallel orbital evaluation

---

# 7. Basin Classification Layer

The operator:

\[
\Phi(x)
\]

may potentially be implemented locally to classify asymptotic behavior without explicit iterative traversal.

This remains speculative.

---

# 8. Torsional Tracking

Local kernels may potentially monitor periodic orbital recurrence including:

- cycle detection
- recurrent phase tracking
- orbital synchronization
- torsional state evolution

---

# 9. Potential FPGA Affinity

The framework aligns conceptually with FPGA characteristics including:

- distributed logic blocks
- localized memory
- configurable routing
- spatial parallelism
- systolic execution structures

---

# 10. Major Unknowns

Critical unresolved questions include:

- routing congestion
- LUT memory growth
- timing closure
- synchronization overhead
- reconstruction cost
- practical scalability

No prototype currently exists.

---

# 11. Research Status

FPGA-local kernels remain an exploratory hardware interpretation of CRT-local modular computation.

