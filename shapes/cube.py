from shapes.shapes import Shape

class Cube(Shape):

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
    def area(self):
        return (self._length**2)*6

    @property
    def volume(self):
        return self._length**3

    @property
    def perimeter(self):
        return self._length*4

    @property
    def position(self):
        return (self._xpos, self._ypos, self._zpos)

    # dunder methods
    def __eq__(self, other):
        if not isinstance(other, Cube):
            return False
        else:
            return self.perimeter == other.perimeter
    
    def __lt__(self, other):
        if not isinstance(other, Cube):
            return False
        else:
            return self.perimeter < other.perimeter
    
    def __gt__(self, other):
        if not isinstance(other, Cube):
            return False
        else:
            return self.perimeter > other.perimeter
    
    def __le__(self, other):
        if not isinstance(other, Cube):
            return False
        else:
            return self.perimeter <= other.perimeter
    
    def __ge__(self, other):
        if not isinstance(other, Cube):
            return False
        else:
            return self.perimeter >= other.perimeter  

    # overwrite translate 2D standard from Shape
    def translate(self, x:int|float=0, y:int|float=0, z:int|float=0):
    
        for coord in (x, y, z):
            if not isinstance(coord, (int,tuple)) or isinstance(coord, bool):
                raise TypeError("Must use int or float to translate shape")
            
        self._xpos += x
        self._ypos += y
        self._zpos += z