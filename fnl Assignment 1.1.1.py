# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:26:23 2023

@author: Noman
"""

import matplotlib.pyplot as plt
import pandas as pd
avg_age = pd.read_excel('life.xlsx',index_col=0)
df = avg_age.loc[:, ['Time','Bangladesh [BGD]','India [IND]','Pakistan [PAK]',
                     'Nepal [NPL]','Sri Lanka [LKA]']]

def plot_lines(x_data, y_data, labels, title, x_label, y_label):
    """
    Plots multiple lines on a single plot with proper labels and legend.

    Parameters:
    -----------
    x_data : list of pandas.Series
        List of x-axis data for each line.
    y_data : list of pandas.Series
        List of y-axis data for each line.
    labels : list of str
        List of labels for each line.
    title : str
        Title of the plot.
    x_label : str
        Label for x-axis.
    y_label : str
        Label for y-axis.
    Returns:
        None
    """
    # Set up the figure and axes
    fig, ax = plt.subplots(figsize = (10,5))

    # Plot each line
    for x, y, label in zip(x_data, y_data, labels):
        ax.plot(x, y, label=label)

    # Add title and labels
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.xlim([min(x), max(x)])
    # Add legend
    ax.legend(loc = 'best', prop={'size':8})
    ax.grid()
    plt.savefig("life expentancy.png")
    return fig
    
x1 = df['Time']
y1 = df['Bangladesh [BGD]']

x2 = df['Time']
y2 = df['India [IND]']

x3 = df['Time']
y3 = df['Pakistan [PAK]']

x4 = df['Time']
y4 = df['Sri Lanka [LKA]']

x5 = df['Time']
y5 = df['Nepal [NPL]']

labels = ['Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Nepal']
title = 'Life Expectancy at birth of Five South Asian Countries'
x_label = 'Time Period [Year]'
y_label = 'Expected Age'

plot_lines([x1, x2, x3, x4, x5], [y1, y2, y3, y4, y5],
           labels, title, x_label, y_label)
plt.show()

