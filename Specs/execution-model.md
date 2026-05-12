# Yupana CRT Execution Model

## Classical Computation

Traditional architectures rely on:

- sequential arithmetic
- carry propagation
- centralized control
- iterative convergence

Latency depends on:

- operand size
- branching
- memory hierarchy

---

## Yupana CRT Execution

Yupana CRT replaces arithmetic propagation with:

- independent modular lanes
- precomputed transition tables
- torsion-aware state evolution
- attractor lookup systems

Execution becomes:

- spatial
- deterministic
- branch-free
- locally bounded

---

## Computational Consequences

| Property | Classical ALU | Yupana CRT |
|---|---|---|
| Carry propagation | Yes | No |
| Global synchronization | Required | Minimal |
| Execution style | Sequential | Spatial |
| State evolution | Iterative | Table-driven |
| Dynamic classification | Runtime | Direct lookup |
| Basin detection | Iterative | Φ oracle |

---

## Research Direction

Yupana CRT explores whether modular dynamical computation may provide advantages for:

- low-energy inference
- FPGA fabrics
- modular neural systems
- discrete dynamical accelerators
- real-time attractor classification