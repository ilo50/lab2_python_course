from abc import ABC, abstractmethod
from figures.figures import Figure

class Figure_Plotter2D(ABC):

    '''
    Single 2D figure plotter
    '''

    @abstractmethod
    def draw(self, figure: Figure) -> None:
        pass