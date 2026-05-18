from collections import Counter

from yupana.crt.runtime import evolve
from yupana.crt.psi import psi


result = evolve([1, 8, 20, 33], steps=40)

history = result["history"]

print("\nORBIT ANALYSIS\n")

counter = Counter(tuple(state) for state in history)

for state, freq in counter.items():

    print(
        f"state={list(state)} "
        f"visits={freq} "
        f"psi={psi(list(state)):.6f}"
    )

print("\nBEST STATE\n")

print(result["memory"])