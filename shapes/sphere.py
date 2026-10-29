from shapes.shapes import Shape
import math

class Sphere(Shape):

    def __init__(self, 
                 radius:int|float=1, 
                 xpos:int|float=0, 
                 ypos:int|float=0, 
                 zpos:int|float=0
                 ):

        for arg in (radius, xpos, ypos, zpos):
            if not isinstance(arg, (int, float)) or isinstance(arg, bool): 
                raise TypeError("All arguments must be int or float")
        
        if radius < 0:
            raise ValueError("Dimensions cannot be negative")

        self.radius = radius
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos

    # properties
    @property
    def area(self):
        return 4*math.pi*(self.radius**2)

    @property
    def volume(self):
        return 0.75*(math.pi*(self.radius**3))

    @property
    def perimeter(self):
        return (self.radius*2)*math.pi

    # dunder methods
    def __eq__(self, other):
        if not isinstance(other, Sphere):
            return False
        else:
            return self.radius == other.radius
    
    def __lt__(self, other):
        if not isinstance(other, Sphere):
            return False
        else:
            return self.radius < other.radius
    
    def __gt__(self, other):
        if not isinstance(other, Sphere):
            return False
        else:
            return self.radius > other.radius
    
    def __le__(self, other):
        if not isinstance(other, Sphere):
            return False
        else:
            return self.radius <= other.radius
    
    def __ge__(self, other):
        if not isinstance(other, Sphere):
            return False
        else:
            return self.radius >= other.radius  

    # overwrite translate 2D standard from Shape
    def translate(self, x:int|float=0, y:int|float=0, z:int|float=0):

        for coord in (x, y, z):
            if not isinstance(coord, (int,tuple)) or isinstance(coord, bool):
                raise TypeError("Must use int or float to translate shape")
        
        self.xpos += x
        self.ypos += y
        self.zpos += z