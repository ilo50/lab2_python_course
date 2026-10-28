from shapes import Shape
import math

class Circle(Shape):

    ''' 
    Circle inherits from Shape.
    Example usage: c = Circle(xpos=0, ypos=0, radius=1)
    '''

    def __init__(self, radius = 1, xpos = 0, ypos = 0):
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