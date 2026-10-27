from shapes import Shape
import math

class Circle(Shape):

    def __init__(self, radius, xpos = 0, ypos = 0,):

        for arg in (radius, xpos, ypos):
            if not isinstance(arg, (int, float)):
                raise ValueError("All arguments must be int or float")
            
        self.radius = radius
        self.xpos = xpos
        self.ypos = ypos

    @property
    def area(self):
        return (self.radius**2)*math.pi

    @property
    def perimeter(self):
        return (self.radius*2)*math.pi

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def is_unit_circle(self):
        return self.radius == 1
    
s1 = Circle(1, 2, 3)
print(s1.area)
print(s1.xpos, s1.ypos)
s1.translate(1,4)
print(s1.xpos, s1.ypos)
print(s1.perimeter)