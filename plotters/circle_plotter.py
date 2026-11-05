from plotters.plotter2D import Figure_Plotter2D
from figures.circle_figure import Circle_Figure
import matplotlib.pyplot as plt


class Circle_Plotter(Figure_Plotter2D):

    def draw(circle_fig : Circle_Figure) -> None:

        if not isinstance (circle_fig, Circle_Figure):
            raise ValueError("Only circle figures are supported for circle plotter")

        fig, ax = plt.subplots()

        ax.add_patch(circle_fig.fig)

        # adjust the size of the plot to the largest value of either width + x offset or height + y offset
        ax.set_xlim(-(circle_fig._fig_size), circle_fig.fig_size)
        ax.set_ylim(-(circle_fig.fig_size), circle_fig.fig_size)

        ax.set_aspect('equal')
        plt.plot(0,color="r", marker = '*')
        plt.grid(True)
        plt.title('Circle')
        plt.show()