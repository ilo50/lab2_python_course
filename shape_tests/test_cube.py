from pytest import raises
from shapes.cube import Cube

def test_valid_cube():

    c = Cube(1, 2, 3, 4)
    assert c.length == 1
    assert c.xpos == 2
    assert c.ypos == 3
    assert c.zpos == 4

    c2 = Cube()
    assert c2.length == 1
    assert c2.xpos == 0
    assert c2.ypos == 0
    assert c2.zpos == 0

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
    assert c.xpos == 5+1
    assert c.ypos == 5+1
    assert c.zpos == 5+1

def test_invalid_translate():

    r = Cube(1,1,1,1)
    with raises(TypeError):
        r.translate("5", 5, 5)