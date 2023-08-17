from vectorlib import Vector
import pytest
import math

def test_equal():
    assert Vector(1,2,3) == Vector(1,2,3)
    assert Vector(3,4,5) != Vector(1,2,3)
    assert Vector(10,10,-10) != Vector(10, 10, 10)

def test_mul():
    assert 10 * Vector(1,3,5) == Vector(10, 30, 50)
    assert 0 * Vector(1,3,5) == Vector(0, 0, 0)
    assert -1 * Vector(1,3,5) == Vector(-1, -3, -5)
    with pytest.raises(Exception):
        Vector(1,3,5)*Vector(1,3,5)

def test_dot():
    assert Vector(1,3,5).dot(Vector(10, 10, 10)) == 90
    with pytest.raises(Exception):
        Vector(1,3,5).dot(10)
    assert Vector(10, 10, 10).dot(Vector(0, 0, 0)) == 0
    
def test_cross():
    assert Vector(1,3,5).cross(Vector(10, 10, 10)) == Vector(-20, 40, -20)
    with pytest.raises(Exception):
        Vector(1,3,5).cross(Vector(1,3,5,0))
    with pytest.raises(Exception):
        Vector(1,3,5).cross(10)
    assert Vector(10, 10, 10).cross(Vector(0, 0, 0)) == Vector(0, 0, 0)

def test_magnitude():
    assert Vector(1,2,3).magnitude == (14)**0.5
    assert Vector(3,4,5).magnitude == 5*(2)**0.5
    assert Vector(3,4).magnitude == 5
    assert Vector(100, 240).magnitude == 260

def test_angle():
    assert Vector(1,2,3).angle(Vector(2,4,6)) == 0
    assert Vector(1,2,3).angle(-Vector(2,4,6)) == math.pi
    
    