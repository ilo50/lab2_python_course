from figures.figures import Figure
from shapes.circle import Circle
from matplotlib.patches import Circle as mplot_circ

class Circle_Figure(Figure):

    def __init__(self, circle: Circle):

        circle_fig = mplot_circ(
                               (circle.xpos, circle.ypos), 
                               radius=circle.radius,  
                               edgecolor="blue", 
                               facecolor="lightblue")
    
        # adjust the size of the plot to the largest value of either width + x offset or height + y offset
        fig_size = max(abs(circle.xpos) + abs(circle.radius*2), abs(circle.ypos) + abs(circle.radius*2))

        self._fig = circle_fig
        self._fig_size = fig_size