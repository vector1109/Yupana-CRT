from yupana.crt.metrics import circular_distance


FIELD = [0, 5, 10, 15, 20]


def field_distance(x: int):
    return min(
        circular_distance(x, f)
        for f in FIELD
    )


def field_vector_distance(values):
    return sum(
        field_distance(v)
        for v in values
    )
