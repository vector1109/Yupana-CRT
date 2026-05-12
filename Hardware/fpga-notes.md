# FPGA Exploration Notes

## Overview

This document summarizes exploratory ideas for mapping Yupana CRT concepts onto FPGA architectures.

The objective is to evaluate whether modular dynamical execution can benefit from spatial programmable logic fabrics.

---

# 1. Why FPGA?

FPGA devices naturally support:

- parallel execution
- spatial routing
- lookup-table computation
- deterministic timing
- configurable local architectures

These properties align closely with CRT-local execution principles.

---

# 2. CRT-Local Processing Units

Each CRT component:

\[
\mathbb{Z}_{p_i^{\alpha_i}}
\]

may map to an independent hardware region.

Each region can contain:

- local lookup tables
- modular state registers
- transition logic
- torsion metadata
- attractor classifiers

---

# 3. Lookup-Based Dynamics

The map:

\[
f_k(x)=x^k \bmod n
\]

can be evaluated through precomputed LUTs.

Possible implementation targets include:

- FPGA LUT primitives
- BRAM blocks
- distributed RAM
- local SRAM structures

---

# 4. Spatial Execution

Instead of sequential arithmetic pipelines, the system becomes a spatial fabric of modular domains.

Potential advantages:

- low control overhead
- parallel state evolution
- deterministic latency
- branch elimination

---

# 5. Dynamical Classification Hardware

The operator:

\[
\Phi(x)
\]

may be implemented as direct combinational logic or lookup evaluation.

This could allow:

- immediate basin classification
- attractor-domain routing
- phase-space indexing

without iterative execution.

---

# 6. Torsion Tracking

Additional hardware layers may track:

\[
\vec{\tau}(x)
\]

for:

- periodicity analysis
- cycle synchronization
- phase-aware routing
- oscillatory memory structures

---

# 7. Potential FPGA Challenges

Open implementation difficulties include:

- routing congestion
- BRAM scaling
- CRT reconstruction cost
- synchronization overhead
- dynamic range limitations

---

# 8. Candidate Research Targets

Possible experimental milestones:

- small-scale CRT execution fabric
- attractor classifier accelerator
- torsion-aware modular processor
- basin routing engine
- modular recurrent dynamical core

---

# 9. Research Status

No FPGA prototype currently exists.

All hardware directions remain conceptual and exploratory.

Performance characteristics are unknown until implementation and benchmarking are performed.

