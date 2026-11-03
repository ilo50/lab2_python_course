
import matplotlib.pyplot as plt
from figures.rectangle_figure import Rectangle_Figure
from plotters.plots import Figure_Plotter

class Rectangle_Plotter(Figure_Plotter):

    def draw(rectangle_fig : Rectangle_Figure):

        fig, ax = plt.subplots()

        ax.add_patch(rectangle_fig.fig)

        ax.set_xlim(-(rectangle_fig.fig_size), rectangle_fig.fig_size)
        ax.set_ylim(-(rectangle_fig.fig_size), rectangle_fig.fig_size)

        ax.set_aspect('equal')
        plt.plot(0,color="r", marker = '*')
        plt.grid(True)
        plt.title('Rectangle')
        plt.show()