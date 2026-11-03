from figures.figures import Figure
from shapes.rectangle import Rectangle
from matplotlib.patches import Rectangle as mplot_rect

class Rectangle_Figure(Figure):

    def __init__(self, rectangle: Rectangle):

        rectangle_fig = mplot_rect(
                               (rectangle.xpos, rectangle.ypos), 
                               width=rectangle.width,  
                               height=rectangle.height,
                               edgecolor="green", 
                               facecolor="lightgreen")
    
        # adjust the size of the plot to the largest value of either width + x offset or height + y offset
        fig_size = max(abs(rectangle.xpos) + abs(rectangle.width*2), abs(rectangle.ypos) + abs(rectangle.height*2))

        self._fig = rectangle_fig
        self._fig_size = fig_size