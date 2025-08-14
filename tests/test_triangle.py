import math
from mygeopy import hypot

def test_hypot_basic():
    assert hypot(3, 4) == 5.0
    assert hypot(0, 0) == 0.0
    assert hypot(5, 12) == 13.0

def test_hypot_symmetry():
    assert hypot(4, 3) == 5.0

def test_hypot_floats():
    assert math.isclose(hypot(0.3, 0.4), 0.5, rel_tol=1e-12, abs_tol=0.0)

def test_hypot_large_numbers():
    expected = math.hypot(1e154, 1e154)
    assert math.isclose(hypot(1e154, 1e154), expected, rel_tol=0, abs_tol=0.0)
