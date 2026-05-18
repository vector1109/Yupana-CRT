from yupana.crt.residues import to_residues
from yupana.crt.residues import from_residues

from yupana.crt.metrics import circular_distance
from yupana.crt.metrics import vector_distance

from yupana.crt.field import field_distance

from yupana.crt.psi import psi

from yupana.crt.scheduler import best_step

from yupana.crt.runtime import step


def test_residue_roundtrip():
    x = 17

    r = to_residues(x)

    assert from_residues(r) == x


def test_circular_distance():
    assert circular_distance(59, 1) == 2
    assert circular_distance(0, 30) == 30
    assert circular_distance(10, 12) == 2


def test_vector_distance():
    a = [1, 2, 3]
    b = [59, 2, 5]

    assert vector_distance(a, b) == 4


def test_field_distance():
    assert field_distance(5) == 0
    assert field_distance(6) == 1
    assert field_distance(58) == 2


def test_psi_penalizes_collapse():
    collapsed = psi([1, 1, 1, 1])
    structured = psi([1, 8, 20, 33])

    assert collapsed > structured


def test_scheduler_reduces_psi():
    state = [1, 8, 20, 33]

    result = best_step(state)

    assert result["delta"] < 0


def test_runtime_step():
    state = [1, 8, 20, 33]

    result = step(state)

    assert "state" in result
    assert "psi" in result
    assert "delta" in result