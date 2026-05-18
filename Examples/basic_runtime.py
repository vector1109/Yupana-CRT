from yupana.crt.runtime import evolve
from yupana.crt.psi import psi


state = [1, 8, 20, 33]

history = evolve(state, steps=15)

print()
print("YUPANA CRT RUNTIME")
print()

for i, s in enumerate(history):
    print(
        f"step={i:02d}",
        f"state={s}",
        f"psi={psi(s):.6f}"
    )