from abc import ABC, abstractmethod

class Shape_Plotter(ABC):

    @abstractmethod
    def draw(shape):
        pass