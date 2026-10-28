from abc import ABC, abstractmethod

class Shape(ABC):

    '''
    Abstract class for creating a shape.
    Must implement these methods:
    
        def area(self):
            ...
    
        def perimeter(self):
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
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
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
    
    #methods that are not overriden
    def translate(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Must use int or float to translate shape")
        self.xpos += x
        self.ypos += y

    def __repr__(self):
            st = ""
            for name, value in vars(self).items():
                st+=f"{name}: {value}"
            return st

    def __str__(self):
            st = f"{type(self)}"
            st = st[17:-2] + "("
            for name, value in vars(self).items():
                st+=f"({name}): {value}"
            st+=")"
            return st