import matplotlib.pyplot as plt
from figures.figures import Figure
import random

class Shape2dPlotter:

    def plot(*args : Figure):

        fig, ax = plt.subplots()
        count = 0
        figsize = 0

        for arg in args:
            count+=1
            if (arg.fig_size > figsize):
                figsize = arg.fig_size

            ax.add_patch(arg.fig)

        size = figsize
        ax.set_xlim(-(size), size)
        ax.set_ylim(-(size), size)

        ax.set_aspect('equal')
        plt.plot(0,color="red", marker = '*')
        plt.grid(True)
        plt.title(f'{count} instance(s) of 2D Shapes')
        plt.show()
                