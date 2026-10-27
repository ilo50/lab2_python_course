from shapes import Shape

class Rectangle(Shape):

    def __init__(self, xpos, ypos, height, width):

        for arg in (xpos, ypos, height, width):
            if not isinstance(arg, (int, float)):
                raise ValueError("All arguments must be int or float")
            
        self.xpos = xpos
        self.ypos = ypos
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.width*self.height

    @property
    def perimeter(self):
        return self.width*2 + self.height*2

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __le__(self, other):
        return self.area <= other.area

    def __ge__(self, other):
        return self.area >= other.area  

    def is_square(self):
        return self.width == self.height