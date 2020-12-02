import random
from itertools import count
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

index = count()

x_vals = []
y_vals = []

def animate(i):
    x_vals.append(random.uniform(0, 5))
    y_vals.append(random.uniform(0, 5))

    plt.cla()
    plt.scatter(x_vals, y_vals)

ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()
