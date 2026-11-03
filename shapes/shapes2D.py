from abc import ABC, abstractmethod

class Shape(ABC):

    '''
    Abstract class for creating a shape.
    Must implement these methods:
    
        def area(self):
            ...
        def perimeter(self):
            ...
    '''
    #abstract property methods
    @property
    @abstractmethod
    def area(self) -> int | float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> int | float:
        pass

    # predefined property methods
    @property
    def xpos(self) -> int | float:
        return self._xpos

    @property
    def ypos(self) -> int | float:
        return self._ypos

    # dunders, all 2D shapes use area as comparator
    def __eq__(self, other):
        if not (type(self) == type(other)): # only allow comparison to same class
            return False
        else:
            return self.area == other.area                 
    
    def __lt__(self, other):
        if not (type(self) == type(other)):
            return False
        else:
            return self.area < other.area
            
    def __gt__(self, other):
        if not (type(self) == type(other)):
            return False
        else:    
            return self.area > other.area
    
    def __le__(self, other):
        if not (type(self) == type(other)):
            return False
        else:
            return self.area <= other.area
    
    def __ge__(self, other):
        if not (type(self) == type(other)):
            return False
        else:
            return self.area >= other.area
    
    def __repr__(self) -> str:
                st = f"Class={type(self).__name__}("
                for name, value in vars(self).items():
                    st+=f"[{name}={value}]"
                st += ")"
                return st

    def __str__(self) -> str:
            st = f"{type(self).__name__}("
            for name, value in vars(self).items():
                st+=f"[{value}]"
            st += ")"
            return st

    #translate, same for all 2D shapes
    def translate(self, x:int|float=0, y:int|float=0) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Must use int or float to translate shape")
        self._xpos += x
        self._ypos += y