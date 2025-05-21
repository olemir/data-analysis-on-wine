import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import  gaussian_kde

# Plotting functions wine

def barplot_physicochemical_properties(wine, colors=None, ylabels=None, a=None):
   '''Plot physicochemical properties in a horizontal bar plot'''
   a = sns.barplot(wine, orient='h', ax=a)
   if ylabels:
      a.set_yticklabels(labels=ylabels)
   if colors:
      for bars in a.containers:
         for bar, color in zip(bars, colors):
            bar.set_facecolor(color)
   a.set_xlabel('')
   return a

# Plotting functions - more general

def get_kde_maximum(data, X, Y, xlim, ylim):
    '''
    get coordinates of maximum of a kde plot
    '''
    kde = gaussian_kde([data[X], data[Y]])
    x_min, x_max = xlim
    y_min, y_max = ylim
    xi, yi = np.mgrid[x_min:x_max:100j, y_min:y_max:100j]
    zi = kde(np.vstack([xi.flatten(), yi.flatten()]))
    max_index = np.argmax(zi)
    max_x = xi.flatten()[max_index]
    max_y = yi.flatten()[max_index]
    max_z = zi[max_index]
    return max_x, max_y, max_z

def draw_points(x, y, ax):
    '''
    draw point in a plot
    '''
    for xi, yi in zip(x,y):
        ax.plot(xi, yi, 'ro', markersize=2)

def connect_points_line(x, y, ax):
    '''
    connect points in a plot with a line
    '''
    x2 = x[1:] + [x[0]]
    y2 = y[1:] + [y[0]]
    for xi, yi, x2i, y2i in zip(x[:-1], y[:-1], x2[:-1], y2[:-1]):
    # for xi, yi, x2i, y2i in zip(x, y, x2, y2):
        ax.plot([xi, x2i], [yi, y2i], 'b-', linewidth=1)