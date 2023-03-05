# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 03:06:49 2023

@author: Noman
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_excel('mortality infant.xlsx',index_col=3)
df = data.loc[['BGD','IND', 'PAK','NPL', 'LKA'],:]

def draw_pie_plots(values_1, labels_1, values_2, labels_2):
    """
    Draws two pie plots side-by-side using the given values and labels.
    Args:
    - values_1 (object):  object values for the first pie plot.
    - labels_1 (object): object data type containing labels for each value in the first pie plot.
    - values_2 (object): object values for the second pie plot.
    - labels_2 (object): object data type containing labels for each value in the second pie plot.

    Returns:
    - fig (matplotlib figure): A matplotlib figure object containing the two pie plots.
    """
    fig, axs = plt.subplots(2, 1, figsize=(10, 5))
    axs[0].pie(values_1, labels=labels_1)
    axs[0].set_title('Infant mortality (per 1000) Five South Asian Countries in 2000')
    axs[1].pie(values_2, labels=labels_2)
    axs[1].set_title('Infant mortality (per 1000) Five South Asian Countries in 2020')
    plt.savefig("infant mortality.png")
    return fig
values_1 = np.array(df['2000 [YR2000]'])
labels_1 = np.array(df['Country Name'])

values_2 = np.array(df['2020 [YR2020]'])
labels_2 = np.array(df['Country Name'])

fig = draw_pie_plots(values_1, labels_1, values_2, labels_2)
plt.show()
