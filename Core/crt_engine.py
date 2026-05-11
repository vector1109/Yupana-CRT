"""
Yupana CRT
Core Modular Execution Engine

Reference implementation for CRT-local modular dynamics.
"""

from dataclasses import dataclass


@dataclass
class CRTComponent:
    modulus: int
    exponent: int

    def __post_init__(self):
        self.transition_table = self._build_transition_table()

    def _build_transition_table(self):
        """
        Precompute:
            x -> x^k mod modulus
        """
        return {
            x: pow(x, self.exponent, self.modulus)
            for x in range(self.modulus)
        }

    def evaluate(self, x: int) -> int:
        return self.transition_table[x % self.modulus]


class YupanaCRT:
    """
    Multi-component CRT execution engine.
    """

    def __init__(self, components):
        self.components = components

    def evaluate_state(self, state):
        """
        Evaluate one dynamical step independently
        on each CRT component.
        """
        return tuple(
            component.evaluate(value)
            for component, value
            in zip(self.components, state)
        )

    def evolve(self, state, steps=1):
        """
        Iterate the system.
        """
        current = state

        history = [current]

        for _ in range(steps):
            current = self.evaluate_state(current)
            history.append(current)

        return history


def main():

    print("\nYupana CRT - Reference Engine")
    print("--------------------------------")

    # Z_60 decomposition
    # Z_4 × Z_3 × Z_5

    z4 = CRTComponent(modulus=4, exponent=2)
    z3 = CRTComponent(modulus=3, exponent=2)
    z5 = CRTComponent(modulus=5, exponent=2)

    engine = YupanaCRT([z4, z3, z5])

    initial_state = (3, 2, 4)

    history = engine.evolve(initial_state, steps=5)

    for t, state in enumerate(history):
        print(f"t={t} -> {state}")


if __name__ == "__main__":
    main()