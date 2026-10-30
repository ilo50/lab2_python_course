from shapes.shapes import Shape
import math

class Circle(Shape):

    def __init__(self, radius:int|float=1, xpos:int|float=0, ypos:int|float=0):
        
        for arg in (radius, xpos, ypos):
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise TypeError("All arguments must be int or float")

        if radius < 0:
            raise ValueError("Radius cannot be negative")
            
        self._radius = radius
        self._xpos = xpos
        self._ypos = ypos

    #properties
    @property
    def area(self):
        return (self._radius**2)*math.pi

    @property
    def perimeter(self):
        return (self._radius*2)*math.pi

    @property
    def position(self):
        return (self._xpos, self._ypos)
    
    # Dunder methods
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        else:
            return self.area == other.area

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return False
        else:
            return self.area < other.area
        
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return False
        else:    
            return self.area > other.area

    def __le__(self, other):
        if not isinstance(other, Circle):
            return False
        else:
            return self.area <= other.area

    def __ge__(self, other):
        if not isinstance(other, Circle):
            return False
        else:
            return self.area >= other.area

    def is_unit_circle(self):
        return self.area == math.pi and self.position == (0,0) 