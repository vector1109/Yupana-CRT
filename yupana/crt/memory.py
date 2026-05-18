class OrbitMemory:

    def __init__(self):
        self.visits = {}
        self.best_state = None
        self.best_psi = float("inf")

    def register(self, state, psi_value):

        key = tuple(state)

        self.visits[key] = self.visits.get(key, 0) + 1

        if psi_value < self.best_psi:
            self.best_psi = psi_value
            self.best_state = list(state)

    def seen(self, state):

        return tuple(state) in self.visits

    def frequency(self, state):

        return self.visits.get(tuple(state), 0)

    def summary(self):

        return {
            "states": len(self.visits),
            "best_state": self.best_state,
            "best_psi": self.best_psi,
        }