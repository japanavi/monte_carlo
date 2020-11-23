import random
import numpy as np
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import warnings

warnings.filterwarnings("ignore")

index = count()

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
ax1.set_xlim(-2.5, 4.5)
ax1.set_ylim(-2.5, 2.5)
ax1.grid(True, linestyle='--')
ax2.set_aspect('equal')



x_vals = []
y_vals = []

ratio_x = []
ratio_ls = []

r = 1
c = (0, 0)
t = np.arange(0, np.pi * 2.0, 0.01)
cir_x = r * np.cos(t)
cir_y = r * np.sin(t)

color = 'k'

rect_x = np.arange(2, 3, 0.01)
rect_y = np.arange(0, 1, 0.01)

right = [3 for _ in rect_y]
left = [2 for _ in rect_y]
top = [1 for _ in rect_x]
bottom = [0 for _ in rect_x]

def animate(i):
    ax1.cla()
    ax2.cla()
    ax2.grid(True, linestyle='--')
    #right side
    ax2.plot(right, rect_y, c=color)
    #left side
    ax2.plot(left, rect_y, c=color)

    #top
    ax2.plot(rect_x, top, c=color)
    #bottom
    ax2.plot(rect_x, bottom, c=color)

    # circle
    ax2.plot(cir_x + c[0], cir_y + c[1], c=color)

    x, y = random.uniform(-2, 4), random.uniform(-2, 2)

    x_vals.append(x)
    y_vals.append(y)

    x_vals_array = np.array(x_vals)
    y_vals_array = np.array(y_vals)
    dist = np.sqrt(x_vals_array**2 + y_vals_array**2)

    col = np.where(dist <= 1, 'c',
               np.where(
                   np.logical_and(
                       np.logical_and(
                           2 <= x_vals_array, x_vals_array <= 3
                       ),
                       np.logical_and(
                           0 <= y_vals_array, y_vals_array <= 1
                       )),
                   'r', 'm')
            )

    ax2.scatter(x_vals_array, y_vals_array, c=col)

    circle_count = sum(col == 'c')
    square_count = sum(col == 'r')
    ratio = circle_count / square_count
    ratio_x.append(next(index))

    try:
        ratio_ls.append(ratio)
    except ZeroDivisionError:
        ratio_ls.append(0)

    r_x = ratio_x[-20:]
    r_ls = ratio_ls[-20:]

    ax1.set_ylim(0, 5)
    # ax1.axhline(np.pi)
    ax1.plot(r_x, r_ls)
    # ax3 = ax1.twinx()
    ax1.set_yticks([3.14])
    ax1.set_yticklabels(['$\pi$'])


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()
