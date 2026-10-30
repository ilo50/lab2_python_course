from pytest import raises
from shapes.rectangle import Rectangle

def test_valid_rectangle():

    r = Rectangle(3, 2, 1, 0)
    assert r.area == 3*2
    assert r.perimeter == 3*2 + 2*2

    r2 = Rectangle() # test default values
    assert r2.area == 1*2
    assert r2.perimeter == 1*2 + 2*2

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
    assert r.position == (5+1, 5+1)

def test_invalid_translate():

    r = Rectangle(1,1,1,1)
    with raises(TypeError):
        r.translate("5", 5)

def test_unit_circle():

    r1 = Rectangle(1,1)
    r2 = Rectangle(1,2)

    assert r1.is_square() is True
    assert r2.is_square() is False