from yupana.crt.residues import to_residues


def phi_k(x: int, k: int):
    y = pow(x, k, 60)
    return to_residues(y)


def orbit(x: int, k: int, steps: int = 10):
    seq = [x]

    current = x

    for _ in range(steps):
        current = pow(current, k, 60)
        seq.append(current)

    return seq
