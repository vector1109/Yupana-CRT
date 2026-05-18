from statistics import variance

from yupana.crt.metrics import circular_distance
from yupana.crt.field import field_vector_distance


def local_tension(values):
    total = 0

    for i in range(len(values) - 1):
        total += circular_distance(
            values[i],
            values[i + 1]
        )

    return total


def collapse_penalty(values, epsilon=1e-6):
    if len(set(values)) == 1:
        return 1e6

    try:
        return 1 / (variance(values) + epsilon)
    except:
        return 1e6


def psi(
    values,
    alpha=1.0,
    beta=1.0,
    gamma=0.1
):
    return (
        alpha * local_tension(values)
        +
        beta * field_vector_distance(values)
        +
        gamma * collapse_penalty(values)
    )
