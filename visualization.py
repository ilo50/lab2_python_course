import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()
rect = Rectangle((0.2, 0.2), width=0.5, height=0.3, edgecolor='blue', facecolor='lightblue')
ax.add_patch(rect)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.grid(True)
plt.title('Rectangle')
plt.show()