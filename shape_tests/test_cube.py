from pytest import raises
from shapes.cube import Cube

def test_valid_cube():

    c = Cube(4, 3, 2, 1)
    assert c.area == (4**2)*6
    assert c.volume == 4**3
    assert c.perimeter == 4*4

    c2 = Cube() # test default values
    assert c2.area == (1**2)*6
    assert c2.volume == 1**3
    assert c2.perimeter == 1*4

def test_invalid_cube():

    with raises(TypeError):
        Cube(1, 2, "3", 4)
    with raises(TypeError):
        Cube(1, True, 3, 4)
    with raises(TypeError):
        Cube([1,4], 2, 3, 4)

def test_equals():
    c1 = Cube(2)
    c2 = Cube(1)
    c3 = Cube(1)

    assert c2 == c3
    assert c1 != c3

    assert c1 > c3
    assert c3 < c1

    assert c2 <= c1
    assert c2 <= c3

    assert c1 >= c2
    assert c3 >= c2

def test_translate():

    c = Cube(1,1,1,1)
    c.translate(5,5,5)

    assert c.position == (5+1, 5+1, 5+1)

def test_invalid_translate():

    r = Cube(1,1,1,1)
    with raises(TypeError):
        r.translate("5", 5, 5)