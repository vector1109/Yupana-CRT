# Yupana CRT Architecture

## Core Principle

Yupana CRT replaces carry-based arithmetic with fully decoupled modular components.

Each arithmetic lane operates independently over:

- Z_(p1^a1)
- Z_(p2^a2)
- ...
- Z_(pr^ar)

using local precomputed transition tables.

---

## Execution Model

Input state:
(x1, x2, ..., xr)

Evaluation:
(x1^k mod m1,
 x2^k mod m2,
 ...
 xr^k mod mr)

No carries exist between components.

---

## Architectural Consequences

- Constant-time local evaluation
- L1-resident execution tables
- Massive parallelism
- Deterministic latency
- No global synchronization

---

## Long-Term Direction

Potential realizations:

- FPGA modular fabrics
- ASIC dynamical inference engines
- Torsion-aware computational units
- Spatial modular neural systems