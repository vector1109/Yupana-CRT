def circular_distance(a: int, b: int, modulus: int = 60) -> int:
    diff = abs(a - b)
    return min(diff, modulus - diff)


def vector_distance(x, y, modulus: int = 60):
    return sum(
        circular_distance(a, b, modulus)
        for a, b in zip(x, y)
    )
