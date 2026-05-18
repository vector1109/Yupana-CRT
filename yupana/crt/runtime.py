from yupana.crt.psi import psi
from yupana.crt.operators import (
    rotate_vector,
    diffuse,
    torsion,
    resonance,
)
# Nuevo import para gestión de memoria de fase
from yupana.crt.memory import OrbitMemory

OPERATORS = [
    lambda s: rotate_vector(s, 0, 1),
    lambda s: rotate_vector(s, 1, -1),
    lambda s: diffuse(s),
    lambda s: torsion(s, 1),
    lambda s: resonance(s, 0),
]

def evaluate_candidates(state):
    current_psi = psi(state)
    results = []

    for op in OPERATORS:
        candidate = op(state)
        p = psi(candidate)
        results.append({
            "state": candidate,
            "psi": p,
            "delta": p - current_psi,
        })

    # Ordenamos por valor de psi (estabilidad/fase)
    return sorted(results, key=lambda x: x["psi"])

def step(state):
    ranked = evaluate_candidates(state)
    return ranked[0]

def evolve(initial_state, steps=20):
    history = [initial_state]
    memory = OrbitMemory()
    current = initial_state

    for _ in range(steps):
        result = step(current)
        current = result["state"]
        
        # Registro en la memoria orbital
        memory.register(current, result["psi"])
        history.append(current)

    return {
        "history": history,
        "memory": memory.summary(),
    }