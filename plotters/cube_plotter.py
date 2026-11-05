import matplotlib.pyplot as plt
from plotters.plotter3D import Shape_Plotter3D
from shapes.cube import Cube

class Cube_Plotter(Shape_Plotter3D):

    # ChatGPT
    def draw(cube : Cube) -> None:
    # Create axis

        #cube position
        x, y, z = cube.xpos, cube.ypos, cube.zpos
        size = cube.length
         
        # Plot figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # use max coord offset + cube size *2 to set a large enough plotting area
        dimension = (max(x, y, z) + size)
        ax.set_xlim(0, dimension)
        ax.set_ylim(0, dimension)
        ax.set_zlim(0, dimension)

        # create the cube with position and sizes
        ax.bar3d(x, y, z, size, size, size)

        # same ratio for x y z
        ax.set_box_aspect((1, 1, 1))
        
        plt.show()