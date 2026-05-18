import matplotlib.pyplot as plt

from yupana.crt.runtime import evolve
from yupana.crt.psi import psi


initial_state = [1, 8, 20, 33]

history = evolve(initial_state, steps=30)

psi_values = [psi(state) for state in history]

plt.figure(figsize=(10, 5))

plt.plot(psi_values, marker="o")

plt.title("Yupana CRT - Psi Evolution")
plt.xlabel("Step")
plt.ylabel("Psi")

plt.grid(True)

plt.show()