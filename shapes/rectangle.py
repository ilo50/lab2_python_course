from shapes.shapes2D import Shape

class Rectangle(Shape):

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
    def area(self) -> int | float:
        return self._width*self._height
    
    @property
    def perimeter(self) -> int | float:
        return self._width*2 + self._height*2

    @property
    def width(self) -> int | float:
        return self._width
    
    @property
    def height(self) -> int | float:
        return self._height

    def is_square(self):
        return self._width == self._height