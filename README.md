# Yupana CRT

Experimental modular computation and structural dynamics framework based on discrete circular spaces.

## Overview

Yupana CRT explores computation over modular toroidal spaces using:

- Chinese Remainder decomposition
- Circular metrics
- Structural tension minimization (Ψ)
- Discrete phase operators
- Dynamic attractor fields
- Resonant state evolution

The project combines:

- CRT positional computation
- Modular orbital dynamics
- Toroidal geometry
- Variational structural optimization

---

## Core Concepts

### CRT Space

States are represented over modular circular spaces:

\[
(\mathbb{Z}_{60})^n
\]

with natural circular distance:

\[
d(a,b)=\min(|a-b|,60-|a-b|)
\]

---

### Φ Dynamics

Deterministic orbital evolution:

\[
x_{t+1}=x_t^k \pmod{60}
\]

used for:

- basin analysis
- attractor discovery
- modular recurrence structures

---

### Structural Tension Ψ

The runtime defines:

\[
\Psi : \mathcal{S}\rightarrow\mathbb{R}
\]

measuring structural incompatibility.

Lower Ψ states are more coherent.

---

### Runtime Dynamics

The scheduler evaluates operators and selects transitions minimizing:

\[
\Delta\Psi
\]

creating emergent self-organization.

---

## Current Modules

### CRT

- residues
- phi
- metrics
- field
- psi
- operators
- scheduler
- runtime

---

## Status

Experimental research framework.

Not intended as:
- physical theory
- consciousness model
- universal computation replacement

Focused on:
- modular dynamics
- toroidal computation
- structural optimization
- attractor systems

---

## License

MIT