from pytest import raises
from shapes.circle import Circle
import math

def test_valid_circle():

    c = Circle(3, 2, 1)
    assert c.area == (3**2)*math.pi

    c2 = Circle()
    assert c2.area == (1**2)*math.pi 

def test_invalid_circle():

    with raises(TypeError):
        Circle(1, 2, "3")
    with raises(TypeError):
        Circle(1, True, 3)
    with raises(TypeError):
        Circle([1,4], 2, 3)

def test_equals():
    c1 = Circle(2)
    c2 = Circle(1)
    c3 = Circle(1)

    assert c2 == c3
    assert c1 != c3

    assert c1 > c3
    assert c3 < c1

    assert c2 <= c1
    assert c2 <= c3

    assert c1 >= c2
    assert c3 >= c2

def test_translate():

    c = Circle(1,1,1)
    c.translate(5,5)

    assert c.position == (5+1, 5+1)

def test_invalid_translate():

    c = Circle(1,1,1)
    with raises(TypeError):
        c.translate("5", 5)

def test_unit_circle():

    c1 = Circle(1)
    c2 = Circle(1,2,3)

    assert c1.is_unit_circle() is True
    assert c2.is_unit_circle() is False