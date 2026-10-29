import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

from plotters.plots import Shape_Plotter
from shapes.cube import Cube

class Cube_Plotter(Shape_Plotter):

    def draw(self, cube : Cube):
    # Create axis

        #cube position
        x, y, z = cube.xpos, cube.ypos, cube.zpos
        size = cube.length
         
        # Plot figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        dimension = (max(x, y, z) + size)*2

        ax.bar3d(x, y, z, size, size, size)
        ax.set_xlim(0, dimension)
        ax.set_ylim(0, dimension)
        ax.set_zlim(0, dimension)

        ax.set_box_aspect((1, 1, 1))
        
        plt.show()