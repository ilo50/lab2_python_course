from abc import ABC, abstractmethod
from shapes.shapes3D import Shape3D

class Shape_Plotter3D(ABC):

    '''
    Single 3D shape plotter
    '''

    @abstractmethod
    def draw(self, shape: Shape3D) -> None:
        pass