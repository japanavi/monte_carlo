import random
import numpy as np
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from draw_tools import circle, square
import warnings

warnings.filterwarnings("ignore")

index = count()

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(6, 7))
ax1.set_ylim(0, 5)
ax2.set_aspect('equal')

x_vals = []
y_vals = []

ratio_x = []
ratio_ls = []

def animate(i):
    ax1.cla()
    ax2.cla()
    ax2.set_axis_off()

    square(ax2)
    circle(ax2)

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
                           -0.5 <= y_vals_array, y_vals_array <= 0.5
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
    ax1.plot(r_x, r_ls, label=f'Ratio: {ratio:.4f}')
    ax1.set_yticks([1, 2, np.pi, 4, 5])
    ax1.set_yticklabels(['1', '2', '$\pi$', '4', '5'])

    ax1.set_title(f'Approximation: {ratio:.4f}')
    ax1.set_xlabel(f'Iteration: {len(ratio_x)}')
    ax1.set_ylabel('Ratio')


ani = FuncAnimation(plt.gcf(), animate, interval=100)
plt.show()
