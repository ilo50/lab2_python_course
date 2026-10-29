from pytest import raises
from shapes.sphere import Sphere

def test_valid_sphere():

    s = Sphere(1, 2, 3, 4)
    assert s.radius == 1
    assert s.xpos == 2
    assert s.ypos == 3
    assert s.zpos == 4

    s2 = Sphere()
    assert s2.radius == 1
    assert s2.xpos == 0
    assert s2.ypos == 0
    assert s2.zpos == 0

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
    assert s.xpos == 5+1
    assert s.ypos == 5+1
    assert s.zpos == 5+1

def test_invalid_translate():

    r = Sphere(1,1,1,1)
    with raises(TypeError):
        r.translate("5", 5, 5)