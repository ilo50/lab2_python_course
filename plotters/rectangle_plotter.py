
import matplotlib.pyplot as plt
from figures.rectangle_figure import Rectangle_Figure
from plotters.plotter2D import Figure_Plotter2D

class Rectangle_Plotter(Figure_Plotter2D):

    def draw(rectangle_fig : Rectangle_Figure) -> None:

        if not isinstance (rectangle_fig, Rectangle_Figure):
            raise ValueError("Only rectangle figures are supported for rectangle plotter")

        fig, ax = plt.subplots()

        ax.add_patch(rectangle_fig.fig)

        ax.set_xlim(-(rectangle_fig.fig_size), rectangle_fig.fig_size)
        ax.set_ylim(-(rectangle_fig.fig_size), rectangle_fig.fig_size)

        ax.set_aspect('equal')
        plt.plot(0,color="r", marker = '*')
        plt.grid(True)
        plt.title('Rectangle')
        plt.show()