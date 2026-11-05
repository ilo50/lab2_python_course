from abc import ABC, abstractmethod
from shapes.shapes2D import Shape2D

class Figure(ABC):

    '''
    A figure is a shape translation used in plotters

    contains properties: fig_size, fig
    '''
    
    @abstractmethod
    def __init__(self, shape: Shape2D):
        pass

    @property
    def fig_size(self):
        return self._fig_size

    @property
    def fig(self):
        return self._fig