
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as mplot_rect

from shapes.rectangle import Rectangle 

from plotters.plots import Shape_Plotter

class Rectangle_Plotter(Shape_Plotter):

    def draw(self, rectangle : Rectangle):

        fig, ax = plt.subplots()

        rectangle_fig = mplot_rect(
                                  (rectangle.xpos, rectangle.ypos), 
                                  width=rectangle.width, 
                                  height=rectangle.height, 
                                  edgecolor='blue', 
                                  facecolor='lightblue'
                                  )
        ax.add_patch(rectangle_fig)

        # adjust the size of the plot to the largest value of either width + x offset or height + y offset
        fig_size = max(abs(rectangle.xpos) + abs(rectangle.width), abs(rectangle.ypos) + abs(rectangle.height))
        ax.set_xlim(-(fig_size), fig_size)
        ax.set_ylim(-(fig_size), fig_size)

        ax.set_aspect('equal')
        plt.plot(0,color="r", marker = '*')
        plt.grid(True)
        plt.title('Rectangle')
        plt.show()