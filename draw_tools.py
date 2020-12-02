import numpy as np
import matplotlib.pyplot as plt

def circle(ax, r=1, c='k'):
    t = np.arange(0, np.pi * 2.0, 0.01)
    x = r * np.cos(t)
    y = r * np.sin(t)

    ax.plot(x, y, c=c)

def square(ax, c='k'):
    x = np.arange(2, 3, 0.01)
    y = np.arange(-0.5, 0.5, 0.01)

    right = [3 for _ in y]
    left = [2 for _ in y]
    top = [0.5 for _ in x]
    bottom = [-0.5 for _ in x]

    #right side
    ax.plot(right, y, c=c)
    #left side
    ax.plot(left, y, c=c)
    #top
    ax.plot(x, top, c=c)
    #bottom
    ax.plot(x, bottom, c=c)
