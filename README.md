# Yupana CRT

Experimental framework for modular computation and structural dynamics
over discrete toroidal state spaces.

---

# What This Repository Is

Yupana CRT is an experimental computational framework exploring:

* modular circular state spaces
* CRT-based decomposition
* orbital dynamics over discrete tori
* structural tension minimization (Ψ)
* attractor formation and self-organization

The repository contains an executable runtime implementing:

* modular metrics
* orbital transforms
* structural optimization
* operator scheduling
* dynamic attractor evolution
* orbit memory systems

---

# Core Idea

The system models computation over modular toroidal spaces such as:

[
(\mathbb{Z}_{60})^n
]

using the natural circular metric:

[
d(a,b)=\min(|a-b|,60-|a-b|)
]

This transforms the state space into a discrete toroidal geometry where:

* states evolve orbitally,
* operators deform local structure,
* and runtime dynamics attempt to minimize structural tension.

---

# Structural Tension Ψ

The runtime defines:

[
\Psi : \mathcal{S}\rightarrow\mathbb{R}
]

where Ψ measures structural incompatibility inside the system.

Current implementation combines:

## Local coherence

[
\Psi_{local} =
\sum_i d(s_i,s_{i+1})
]

## Distance to attractor FIELD

[
\Psi_{field} =
\sum_i \min_{f\in FIELD} d(s_i,f)
]

## Collapse penalty

[
\Psi_{collapse} =
\frac{1}{Var(S)+\epsilon}
]

The scheduler evaluates candidate transitions and minimizes:

[
\Delta\Psi
]

creating observable structural stabilization.

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
...
step=12 psi=10.004000
```

This demonstrates dynamic convergence toward lower-tension states.

---

# Architecture

The repository currently contains two related but distinct layers.

| Layer      | Purpose                             |
| ---------- | ----------------------------------- |
| CRT / MDST | Deterministic modular dynamics      |
| Runtime Ψ  | Variational structural optimization |

---

# CRT / MDST Layer

This layer implements deterministic modular computation using:

* CRT decomposition
* orbital transforms
* residue-space evolution
* modular recurrence structures
* algebraic attractor basins

Orbital evolution is defined by:

[
x_{t+1}=x_t^k \pmod{60}
]

which generates recurrence cycles and modular attractor structures.

---

# Runtime Ψ Layer

The Ψ runtime operates on top of the modular space using:

* structural evaluation
* operator scheduling
* attractor fields
* orbit memory
* local optimization dynamics

Unlike Φ orbital dynamics, the Ψ runtime is heuristic and exploratory.

---

# Historical Inspiration

This project does not attempt to reconstruct the historical Yupana.

The inspiration emerged from a conceptual question:

> What kind of computational system would appear if position,
> modularity, and circular movement were treated as foundational
> computational primitives?

The historical Yupana acted as a conceptual starting point for exploring:

* positional dynamics,
* modular state transitions,
* and toroidal computational geometries.

The name remains as recognition of that original inspiration,
not as an archaeological or historical claim.

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

# Research Scope

Current research focuses on:

* modular dynamical systems
* toroidal computation
* orbital recurrence
* attractor systems
* structural optimization
* discrete phase geometries

---

# Non-Goals

This repository does NOT claim:

* historical reconstruction
* physical unification
* consciousness modeling
* replacement of classical computation
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
