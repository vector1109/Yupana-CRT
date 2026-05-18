# Yupana CRT

Experimental framework for modular computation and structural dynamics
over discrete toroidal state spaces.

---

# What This Repository Implements

Yupana CRT implements an experimental runtime operating on modular
circular state spaces using:

* CRT decomposition
* circular metrics
* modular orbital dynamics
* discrete state operators
* structural evaluation functionals
* local optimization schedulers

The repository contains executable implementations for:

* residue-space computation
* orbital recurrence systems
* toroidal state metrics
* structural tension evaluation (Ψ)
* operator-driven state transitions
* attractor search dynamics
* orbit memory systems

---

# State Space

System states are represented as vectors over modular circular spaces:

[
(\mathbb{Z}_{60})^n
]

where:

[
S=(s_1,s_2,\dots,s_n)
]

and each component is an integer modulo 60.

The state space is treated operationally as a discrete toroidal geometry.

---

# Circular Metric

Distances are computed using the natural circular metric:

[
d(a,b)=\min(|a-b|,60-|a-b|)
]

This avoids linear discontinuities across modular boundaries.

Example:

[
d(59,1)=2
]

not 58.

The runtime uses this metric for:

* neighborhood evaluation
* operator scoring
* structural comparison
* attractor distance estimation

---

# CRT / MDST Layer

The CRT layer implements deterministic modular dynamics.

Current components include:

* residue decomposition
* modular reconstruction
* orbital transforms
* recurrence analysis
* algebraic basin structures

---

# Φ Orbital Dynamics

Orbital evolution is defined by:

[
x_{t+1}=x_t^k \pmod{60}
]

where:

* (x_t) is the current modular state
* (k) is an orbital exponent parameter

This generates:

* recurrence cycles
* orbital graphs
* residue partitions
* deterministic attractor basins

Φ dynamics are deterministic and algebraic.

---

# Structural Functional Ψ

The runtime defines a scalar structural functional:

[
\Psi : \mathcal{S}\rightarrow\mathbb{R}
]

Ψ evaluates structural incompatibility inside a state vector.

The current implementation combines three components.

---

## 1. Local Continuity

[
\Psi_{local}
============

\sum_i d(s_i,s_{i+1})
]

This penalizes abrupt circular discontinuities between neighboring states.

---

## 2. FIELD Distance

Given a preferred attractor subset:

[
FIELD \subset \mathbb{Z}_{60}
]

the runtime computes:

[
\Psi_{field}
============

\sum_i \min_{f\in FIELD} d(s_i,f)
]

This measures aggregate distance to preferred modular regions.

---

## 3. Collapse Penalty

[
\Psi_{collapse}
===============

\frac{1}{Var(S)+\epsilon}
]

This penalizes degenerate low-variance states.

Completely collapsed states receive large Ψ values.

---

# Runtime Scheduler

The runtime evaluates candidate operators and selects transitions minimizing:

[
\Delta\Psi
==========

\Psi(S_{t+1})-\Psi(S_t)
]

Operationally:

* operators generate candidate states,
* the scheduler evaluates Ψ,
* the runtime selects the lowest available transition.

This produces iterative movement toward local low-Ψ regions.

---

# Operational Definitions

| Concept   | Operational Meaning               |
| --------- | --------------------------------- |
| State     | vector in ((\mathbb{Z}_{60})^n)   |
| Metric    | circular modular distance         |
| Operator  | discrete state transformation     |
| Orbit     | iterated state sequence           |
| FIELD     | preferred modular subset          |
| Ψ         | scalar structural functional      |
| Scheduler | transition selector minimizing ΔΨ |
| Attractor | local low-Ψ region                |
| Memory    | indexed history of visited states |

---

# Example

```python
from yupana.crt.runtime import evolve

result = evolve([1,8,20,33], steps=10)

print(result["history"])
print(result["memory"])
```

Example runtime output:

```text
step=00 psi=48.000506
step=01 psi=30.003000
step=02 psi=30.003000
step=03 psi=29.003306
step=04 psi=28.003614
step=05 psi=26.003909
step=06 psi=23.004167
step=07 psi=20.004364
step=08 psi=19.004478
step=09 psi=18.004494
step=10 psi=16.004412
```

This demonstrates iterative convergence toward lower-Ψ regions.

---

# Current Modules

## CRT / MDST

* residues
* phi
* metrics

## Runtime Ψ

* field
* psi
* operators
* scheduler
* runtime
* memory

---

# Historical Inspiration

This project does not attempt to reconstruct the historical Yupana.

The project originated from a conceptual question:

> What computational structures emerge if modular position,
> circularity, and discrete phase movement are treated as
> primary computational primitives?

The historical Yupana acted as conceptual inspiration for exploring:

* positional computation,
* modular state movement,
* and toroidal computational geometry.

The repository makes no archaeological or historical claims.

---

# Research Scope

Current research focuses on:

* modular dynamical systems
* toroidal state spaces
* orbital recurrence
* attractor dynamics
* structural optimization
* discrete circular geometries

---

# Non-Goals

This repository does NOT claim:

* historical reconstruction
* physical unification
* consciousness modeling
* universal computation replacement
* quantum equivalence

---

# Status

Experimental research prototype.

---

# License

This repository uses a layered licensing model.

## Code

Core runtime and computational modules are licensed under MPL-2.0.

## Theory and Documentation

Conceptual and theoretical documentation are licensed under CC BY 4.0.

---

# Quick Start

Install locally:

```bash
pip install -e .
```

Run tests:

```bash
pytest tests/python/test_runtime.py -v
```

Run runtime example:

```bash
python examples/basic_runtime.py
```

Run orbit analysis:

```bash
python examples/orbit_analysis.py
```
