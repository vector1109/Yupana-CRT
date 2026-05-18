# Yupana CRT

Experimental modular computation and structural dynamics framework
inspired by discrete circular state spaces and CRT decomposition.

---

## Overview

Yupana CRT explores computation and dynamic evolution over modular
toroidal spaces using:

- Chinese Remainder decomposition (CRT)
- Circular metrics on discrete phase spaces
- Modular orbital dynamics
- Structural tension minimization (Ψ)
- Discrete operators over toroidal state spaces

The project combines two related but distinct layers:

| Layer | Purpose |
|---|---|
| CRT / MDST | Deterministic modular computation |
| Runtime Ψ | Experimental structural optimization |

---

# Conceptual Structure

## 1. CRT / MDST Layer

The foundational layer models states over modular circular spaces.

Example:

\[
(\mathbb{Z}_{60})^n
\]

using the natural circular metric:

\[
d(a,b)=\min(|a-b|,60-|a-b|)
\]

This layer includes:

- residue decomposition
- orbital transforms
- modular recurrence structures
- algebraic basins
- deterministic phase evolution

---

## 2. Φ Orbital Dynamics

Deterministic orbital evolution is defined by:

\[
x_{t+1}=x_t^k \pmod{60}
\]

This produces:

- recurrence cycles
- attractor basins
- modular orbital graphs
- residue-space partitions

Φ dynamics are algebraic and deterministic.

---

## 3. Runtime Ψ Layer

An experimental variational runtime operates on top of the modular space.

The runtime defines a structural tension function:

\[
\Psi : \mathcal{S}\rightarrow\mathbb{R}
\]

where lower Ψ states represent greater structural coherence.

The runtime scheduler evaluates operators and selects transitions minimizing:

\[
\Delta\Psi
\]

This creates:

- emergent attractors
- structural stabilization
- orbital self-organization
- dynamic basin formation

Unlike Φ dynamics, the Ψ runtime is heuristic and exploratory.

---

# Current Modules

## CRT / MDST

- residues
- phi
- metrics

## Runtime Ψ

- field
- psi
- operators
- scheduler
- runtime
- memory

---

# Research Scope

This repository is an experimental research framework exploring:

- modular dynamics
- toroidal computation
- structural optimization
- attractor systems
- circular state geometries

---

# Non-Goals

This project does NOT claim:

- reconstruction of historical Yupana usage
- replacement of classical computation
- physical unification theory
- consciousness modeling
- quantum equivalence

---

# Historical Inspiration

The name "Yupana" is used as conceptual inspiration from Andean
positional computation systems.

This repository does not claim direct historical continuity or
archaeological reconstruction.

---

# Status

Experimental research prototype.

---

# License

MIT