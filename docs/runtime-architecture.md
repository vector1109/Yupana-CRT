# Runtime Architecture

The Yupana CRT runtime operates over modular circular state spaces.

States evolve through discrete operators evaluated by a scheduler.

The scheduler minimizes structural tension Ψ using local operator search.

## Runtime Cycle

1. Generate candidate states
2. Evaluate Ψ for each candidate
3. Select minimum Ψ transition
4. Store state in memory
5. Repeat evolution

## Core Components

- operators.py
- scheduler.py
- runtime.py
- psi.py
- memory.py

## Experimental Nature

The runtime is heuristic and exploratory.

It is not intended as a universal optimizer or physical simulation.