from shapes import Shape

class Rectangle(Shape):

    ''' 
    Rectangle inherits from Shape.
    Example usage: r = Rectangle(xpos=0, ypos=0, height=3, width=6)
    '''

    def __init__(self, width = 1, height = 2, xpos = 0, ypos = 0):
        
        for arg in (xpos, ypos, height, width):
            if not isinstance(arg, (int, float)):
                raise TypeError("All arguments must be int or float")

        if height < 0 or width < 0:
                    raise ValueError("Dimensions cannot be negative")
            
        self.xpos = xpos
        self.ypos = ypos
        self.height = height
        self.width = width

    #properties
    @property
    def area(self):
        return self.width*self.height

    @property
    def perimeter(self):
        return self.width*2 + self.height*2

    # dunder methods
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        else:
            return self.area == other.area

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return False
        else:
            return self.area < other.area

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return False
        else:
            return self.area > other.area

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            return False
        else:
            return self.area <= other.area

    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            return False
        else:
            return self.area >= other.area  

    def is_square(self):
        return self.width == self.height