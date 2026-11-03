from abc import ABC, abstractmethod
from figures.figures import Figure

class Figure_Plotter(ABC):

    @abstractmethod
    def draw(self, figure: Figure):
        pass