MODULI = (4, 3, 5)


def to_residues(x: int):
    """
    Convierte un entero x en residuos CRT.
    """
    return [x % m for m in MODULI]


def from_residues(residues):
    """
    Reconstrucción CRT para Z60.
    """
    r4, r3, r5 = residues

    for x in range(60):
        if (
            x % 4 == r4
            and x % 3 == r3
            and x % 5 == r5
        ):
            return x

    raise ValueError("Invalid residue tuple")