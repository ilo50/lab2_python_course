from shapes.shapes3D import Shape3D

class Cube(Shape3D):

    def __init__(self, 
                 length:int|float=1, 
                 xpos:int|float=0, 
                 ypos:int|float=0, 
                 zpos:int|float=0
                 ):

        for arg in (length, xpos, ypos, zpos):
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise TypeError("All arguments must be int or float")

        if length < 0:
            raise ValueError("Dimensions cannot be negative")

        self._length = length
        self._xpos = xpos
        self._ypos = ypos
        self._zpos = zpos

    #properties
    @property
    def area(self) -> int | float:
        return (self._length**2)*6

    @property
    def volume(self) -> int | float:
        return self._length**3

    @property
    def perimeter(self) -> int | float:
        return self._length*4

    @property
    def zpos(self) -> int | float:
        return self._zpos

    @property 
    def length(self) -> int | float:
        return self._length
