from shapes.shapes import Shape
import math

class Circle(Shape):

    def __init__(self, radius:int|float=1, xpos:int|float=0, ypos:int|float=0):
        if radius < 0:
            raise ValueError("Radius cannot be negative")

        for arg in (radius, xpos, ypos):
            if not isinstance(arg, (int, float)):
                raise TypeError("All arguments must be int or float")
            
        self.radius = radius
        self.xpos = xpos
        self.ypos = ypos

    #properties
    @property
    def area(self):
        return (self.radius**2)*math.pi

    @property
    def perimeter(self):
        return (self.radius*2)*math.pi

    # Dunder methods
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        else:
            return self.radius == other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return False
        else:
            return self.radius < other.radius
        
    def __gt__(self, other):
        if not isinstance(other, Circle):
            return False
        else:    
            return self.radius > other.radius

    def __le__(self, other):
        if not isinstance(other, Circle):
            return False
        else:
            return self.radius <= other.radius

    def __ge__(self, other):
        if not isinstance(other, Circle):
            return False
        else:
            return self.radius >= other.radius

    def is_unit_circle(self):
        return self.radius == 1 and self.xpos == 0 and self.ypos == 0