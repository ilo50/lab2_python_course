import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as mplot_rect
from matplotlib.patches import Circle as mplot_circ

from rectangle import Rectangle 
from circle import Circle

from abc import ABC, abstractmethod

class Shape_Plotter(ABC):

    @abstractmethod
    def draw(shape):
        pass

class Rectangle_Plotter(Shape_Plotter):

    def draw(rectangle : Rectangle):

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

class Circle_Plotter(Shape_Plotter):

    def draw(circle : Circle):

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
