from plotters.plots import Shape_Plotter

from shapes.circle import Circle

import matplotlib.pyplot as plt
from matplotlib.patches import Circle as mplot_circ

class Circle_Plotter(Shape_Plotter):

    def draw(self, circle : Circle):

        fig, ax = plt.subplots()

        circle_fig = mplot_circ(
                                  (circle.xpos, circle.ypos), 
                                  radius=circle.radius,  
                                  edgecolor='blue', 
                                  facecolor='lightblue'
                                  )
        ax.add_patch(circle_fig)

        # adjust the size of the plot to the largest value of either width + x offset or height + y offset
        fig_size = max(abs(circle.xpos) + abs(circle.radius*2), abs(circle.ypos) + abs(circle.radius*2))
        ax.set_xlim(-(fig_size), fig_size)
        ax.set_ylim(-(fig_size), fig_size)

        ax.set_aspect('equal')
        plt.plot(0,color="r", marker = '*')
        plt.grid(True)
        plt.title('Circle')
        plt.show()