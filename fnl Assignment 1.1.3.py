# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 23:10:38 2023

@author: Noman
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_excel('labour force2021.xlsx', index_col=1)
df = data.loc[['GBR','DEU','ESP','FRA','ITA','TUR','UKR','POL','ROU','KAZ'], ['Female','Total','Male']]

def create_labour_force_chart(data):
    """
    Creates a bar chart using Pandas and Matplotlib to visualize labor force data for the top 10 populous countries of Europe.

    Parameters:
    data (pd.DataFrame): The data to plot, with columns for 'Total', 'Male', 'Female', and 'Country Code'.

    Returns:
    plt.Axes: The chart object.
    """

    position = list(range(len(data['Total'])))
    width = 0.25
    fig, ax = plt.subplots(figsize=(10,5))
    plt.bar(position, data['Total'], width, color='g')
    plt.bar([p + width for p in position], data['Male'], width, color='r')
    plt.bar([p + width*2 for p in position], data['Female'], width, color='b')
    ax.set_ylim()
    ax.set_ylabel('Labour Forces')
    ax.set_xlabel('Country')
    ax.set_title('Labour Forces in top 10 populous countries of Europe')
    ax.set_xticks([p + 1 * width for p in position])
    ax.set_xticklabels(df.index, rotation=90)
    plt.legend(['Labor force Total', 'Labor force Male', 'Labor force Female'], loc='upper right')
    plt.grid()
    plt.savefig("labor Force.png")
    return ax

# Call the function to create the chart
chart = create_labour_force_chart(df)

# Display the chart
plt.show()
