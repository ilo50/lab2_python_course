from pytest import raises
from shapes.rectangle import Rectangle

def test_valid_rectangle():

    r = Rectangle(3, 2, 1, 0)
    assert r.width == 3
    assert r.height == 2
    assert r.xpos == 1
    assert r.ypos == 0

    r2 = Rectangle()
    assert r2.width == 1
    assert r2.height == 2
    assert r2.xpos == 0
    assert r2.ypos == 0

def test_invalid_rectangle():

    with raises(TypeError):
        Rectangle(1, 2, "3", 4)
    with raises(TypeError):
        Rectangle(1, True, 3, 4)
    with raises(TypeError):
        Rectangle([1,4], 2, 3, 4)

def test_equals():
    r1 = Rectangle(2,2)
    r2 = Rectangle(1,1)
    r3 = Rectangle(1,1)

    assert r2 == r3
    assert r1 != r3

    assert r1 > r3
    assert r3 < r1

    assert r2 <= r1
    assert r2 <= r3

    assert r1 >= r2
    assert r3 >= r2

def test_translate():

    r = Rectangle(1,1,1,1)
    r.translate(5,5)
    assert r.xpos == 5+1
    assert r.ypos == 5+1

def test_invalid_translate():

    r = Rectangle(1,1,1,1)
    with raises(TypeError):
        r.translate("5", 5)

def test_unit_circle():

    r1 = Rectangle(1,1)
    r2 = Rectangle(1,2)

    assert r1.is_square() is True
    assert r2.is_square() is False