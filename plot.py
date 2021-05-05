#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import re

import pandas


def simple_graph_plot():
    with open('result_simple.txt') as f:
        lines = f.readlines()
    x_values= [line.split(",")[0] for line in lines]
                      #regular expr per pulire la stringa (grazie professor Bagdanov)
    y_values= [line.split(",")[1] for line in lines]
    x_values = [s.replace("(", "").replace("'", "").replace(" ", "") for s in x_values]
    y_values=[s.replace(")", "").replace("\n","").replace(" ","") for s in y_values]

    x_values[:] = (elem[:5] for elem in x_values)
    print(x_values,"***",y_values)
    print(repr(x_values), "***", repr(y_values))
    print(type(x_values[1]))
    print(type(y_values))

    x_values = [float(item) for item in x_values]
    y_values = [int(item) for item in y_values]

    # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(x_values,y_values, label='linear')  # Plot some data on the axes.
    ax.set_xlabel('x label')  # Add an x-label to the axes.
    ax.set_ylabel('y label')  # Add a y-label to the axes.
    ax.set_title("Simple Plot")  # Add a title to the axes.

    plt.xticks(np.arange(0, 1 ,step= 0.2))
    plt.show()
