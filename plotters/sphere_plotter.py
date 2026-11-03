import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

from plotters.plots import Figure_Plotter
from shapes.sphere import Sphere

class Sphere_Plotter(Figure_Plotter):

    # ChatGPT
    def draw(sphere : Sphere):
    # Create axis

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # angles
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)

        # coordinates, includes offset
        x = sphere.radius * np.outer(np.cos(u), np.sin(v)) + sphere.xpos
        y = sphere.radius * np.outer(np.sin(u), np.sin(v)) + sphere.ypos
        z = sphere.radius * np.outer(np.ones(np.size(u)), np.cos(v)) + sphere.zpos

        ax.plot_surface(x, y, z, color='lightblue')

        plt.show()