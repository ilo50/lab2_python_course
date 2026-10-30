from shapes.shapes import Shape

class Rectangle(Shape):

    ''' 
    Rectangle inherits from Shape.
    Example usage: r = Rectangle(xpos=0, ypos=0, height=3, width=6)
    '''

    def __init__(self, 
                 width:int|float=1, 
                 height:int|float=2, 
                 xpos:int|float=0, 
                 ypos:int|float=0
                 ):
        
        for arg in (xpos, ypos, height, width):
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise TypeError("All arguments must be int or float")

        if height < 0 or width < 0:
                    raise ValueError("Dimensions cannot be negative")
            
        self._xpos = xpos
        self._ypos = ypos
        self._height = height
        self._width = width

    # properties
    @property
    def area(self):
        return self._width*self._height
    
    @property
    def perimeter(self):
        return self._width*2 + self._height*2

    @property
    def position(self):
        return (self._xpos, self._ypos)

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
        return self._width == self._height