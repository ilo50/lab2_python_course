from abc import ABC, abstractmethod

class Shape3D(ABC):

    '''
    3 Dimensional shape, contains properties: 
    volume, area, perimeter, xpos, ypos, zpos
    
    contains a few dunder methods
    
    contains a translate to change position
    '''
    #abstract property methods
    @property
    @abstractmethod
    def volume(self) -> int | float:
        pass      

    @property
    @abstractmethod
    def area(self) -> int | float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> int | float:
        pass

    # coordinate properties, predefined
    @property
    def xpos(self) -> int | float:
        return self._xpos
    
    @property
    def ypos(self) -> int | float:
        return self._ypos
    
    @property
    def zpos(self) -> int | float:
        return self._zpos

    # dunders, 3D shapes use volumes to compare
    def __eq__(self, other):
        if not (type(self) == type(other)): # only allow comparison to same class
            return False
        else:
            return self.volume == other.volume                 
        
    def __lt__(self, other):
        if not (type(self) == type(other)):
            return False
        else:
            return self.volume < other.volume
                
    def __gt__(self, other):
        if not (type(self) == type(other)):
            return False
        else:    
            return self.volume > other.volume
        
    def __le__(self, other):
        if not (type(self) == type(other)):
            return False
        else:
            return self.volume <= other.volume
        
    def __ge__(self, other):
        if not (type(self) == type(other)):
            return False
        else:
            return self.volume >= other.volume
    
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

    def translate(self, x:int|float=0, y:int|float=0, z:int|float=0):
            
        for coord in (x, y, z):
            if not isinstance(coord, (int,tuple)) or isinstance(coord, bool):
                raise TypeError("Must use int or float to translate shape")
                    
        self._xpos += x
        self._ypos += y
        self._zpos += z