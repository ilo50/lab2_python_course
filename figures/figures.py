from abc import ABC, abstractmethod
from shapes.shapes2D import Shape

class Figure(ABC):

    '''
    Abstract class for translating a Shape into a Figure used in matplot
    '''
    
    @abstractmethod
    def __init__(self, shape: Shape):
        pass

    @property
    def fig_size(self):
        return self._fig_size

    @property
    def fig(self):
        return self._fig