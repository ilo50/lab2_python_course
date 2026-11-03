from shapes.shapes2D import Shape
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
    def area(self) -> int | float:
        return (self._radius**2)*math.pi

    @property
    def perimeter(self) -> int | float:
        return (self._radius*2)*math.pi

    @property 
    def radius(self) -> int | float:
        return (self._radius)

    def is_unit_circle(self):
        return self.area == math.pi and (self.xpos, self.ypos) == (0,0) 