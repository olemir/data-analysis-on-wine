import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Plotting functions 

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