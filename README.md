# Yupana CRT

## Spatial Modular Computing Architecture Based on CRT Dynamics

---

## Overview

Yupana CRT is an experimental computational architecture derived from the theoretical framework established in MDST (Modular Dynamical Systems Toolkit).

The project explores:

- CRT-native computation
- table-driven modular execution
- carry-free arithmetic architectures
- constant-latency modular dynamics
- discrete toroidal state spaces
- modular torsion dynamics
- hardware-oriented finite ring computation

Unlike traditional binary architectures, Yupana CRT operates through independent modular components connected via Chinese Remainder decomposition.

---

## Relationship to MDST

MDST defines the mathematical framework.

Yupana CRT implements the computational substrate.

| Project | Role |
|---|---|
| MDST | Theory and formalism |
| Yupana CRT | Runtime and architecture |

---

## Core Concepts

### CRT-Native Execution

A number is represented as:

\[
x \leftrightarrow (x_1, x_2, \dots, x_r)
\]

with independent local evolution.

---

### Table-Driven Dynamics

Instead of iterative arithmetic:

\[
f_k(x)=x^k \bmod n
\]

is evaluated through local lookup tables:

\[
T_i[a]=a^k \bmod p_i^{\alpha_i}
\]

allowing constant-time local transitions.

---

### Carry-Free Structure

Each component evolves independently:

- no global carry propagation
- high parallelism
- deterministic latency
- cache-local execution

---

### Modular Torsion

The system supports periodic orbital structures inside unit groups:

- local cycles
- torsional states
- phase-preserving evolution
- finite-state dynamic memory

---

## Research Directions

- FPGA implementation
- ASIC modular accelerators
- discrete neural substrates
- toroidal state processors
- modular inference engines
- torsion-based computation

---

## Repository Structure

```text
Yupana-CRT/
├── Core/
├── Hardware/
├── Theory/
├── Visuals/
├── Examples/
├── Specs/
└── docs/

Status

Early-stage experimental architecture.

Research repository under active development.

License

Separate licensing model from MDST.

Commercial and hardware-oriented implementations may require additional licensing.


---

## 2. Crear `.gitignore`

```powershell id="iy9t3n"
notepad .gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
*.obj
*.o
*.exe
*.dll
*.bin
*.log
*.tmp
*.cache
.vscode/
.idea/

