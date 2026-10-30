from abc import ABC, abstractmethod

class Shape(ABC):

    '''
    Abstract class for creating a shape.
    Must implement these methods:
    
        def area(self):
            ...
        def perimeter(self):
            ...
        def position(self):
            ...
        def __eq__(self, other):
            ...
        def __lt__(self, other):
            ...
        def __gt__(self, other):
            ...
        def __le__(self, other):
            ...
        def __ge__(self, other):
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

    @property
    @abstractmethod
    def position(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass
    @abstractmethod
    def __lt__(self, other):
        pass
    @abstractmethod
    def __gt__(self, other):
        pass
    @abstractmethod
    def __le__(self, other):
        pass
    @abstractmethod
    def __ge__(self, other):
        pass
    
    #translate is default for 2D shapes, overriden by 3D shapes
    def translate(self, x:int|float=0, y:int|float=0) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Must use int or float to translate shape")
        self._xpos += x
        self._ypos += y

    def __repr__(self) -> str:
            st = ""
            for name, value in vars(self).items():
                st+=f"{name}: {value}"
            return st

    def __str__(self) -> str:
            st = f"{type(self)}"
            st = st[17:-2] + "("
            for name, value in vars(self).items():
                st+=f"({name}): {value}"
            st+=")"
            return st