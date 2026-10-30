from pytest import raises
from shapes.sphere import Sphere
import math

def test_valid_sphere():

    s = Sphere(4, 3, 2, 1)
    assert s.area == 4*math.pi*(4**2)
    assert s.perimeter == (4*2)*math.pi
    assert s.volume == 0.75*(math.pi*(4**3))

    s2 = Sphere()
    assert s2.area == 4*math.pi*(1**2)
    assert s2.perimeter == (1*2)*math.pi
    assert s2.volume == 0.75*(math.pi*(1**3))

def test_invalid_sphere():

    with raises(TypeError):
        Sphere(1, 2, "3", 4)
    with raises(TypeError):
        Sphere(1, True, 3, 4)
    with raises(TypeError):
        Sphere([1,4], 2, 3, 4)

def test_equals():
    s1 = Sphere(2)
    s2 = Sphere(1)
    s3 = Sphere(1)

    assert s2 == s3
    assert s1 != s3

    assert s1 > s3
    assert s3 < s1

    assert s2 <= s1
    assert s2 <= s3

    assert s1 >= s2
    assert s3 >= s2

def test_translate():

    s = Sphere(1,1,1,1)
    s.translate(5,5,5)

    assert s.position == (5+1, 5+1, 5+1)

def test_invalid_translate():

    r = Sphere(1,1,1,1)
    with raises(TypeError):
        r.translate("5", 5, 5)