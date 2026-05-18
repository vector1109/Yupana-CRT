from yupana.crt.psi import psi


def rotate(values, index, step):
    result = values.copy()

    result[index] = (result[index] + step) % 60

    return result


def best_step(values):
    current_psi = psi(values)

    best_state = values
    best_score = current_psi

    for i in range(len(values)):

        for step in [-1, 1]:

            candidate = rotate(values, i, step)

            score = psi(candidate)

            if score < best_score:
                best_state = candidate
                best_score = score

    return {
        "state": best_state,
        "psi": best_score,
        "delta": best_score - current_psi
    }


def descend(values, iterations=10):
    state = values

    history = [state]

    for _ in range(iterations):

        result = best_step(state)

        if result["delta"] >= 0:
            break

        state = result["state"]

        history.append(state)

    return history
