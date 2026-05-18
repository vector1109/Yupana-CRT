from yupana.crt.metrics import circular_distance


def rotate(value, step):
    return (value + step) % 60


def rotate_vector(state, index, step):
    new_state = state.copy()
    new_state[index] = rotate(new_state[index], step)
    return new_state


def align(value, target, strength=1):
    cw = (target - value) % 60
    ccw = (value - target) % 60

    if cw <= ccw:
        move = min(strength, cw)
        return (value + move) % 60

    move = min(strength, ccw)
    return (value - move) % 60


def align_vector(state, targets, strength=1):
    new_state = state.copy()

    for i in range(min(len(state), len(targets))):
        new_state[i] = align(
            state[i],
            targets[i],
            strength
        )

    return new_state


def diffuse(state):
    if len(state) < 2:
        return state.copy()

    new_state = state.copy()

    for i in range(len(state)):
        left = state[i - 1]
        right = state[(i + 1) % len(state)]

        avg = round((left + right) / 2) % 60

        new_state[i] = avg

    return new_state


def torsion(state, shift=1):
    n = len(state)

    return [
        (state[i] + i * shift) % 60
        for i in range(n)
    ]


def resonance(state, center):
    new_state = []

    for x in state:
        d = circular_distance(x, center)

        if d == 0:
            new_state.append(x)
        else:
            direction = 1 if ((center - x) % 60) < 30 else -1
            new_state.append((x + direction) % 60)

    return new_state