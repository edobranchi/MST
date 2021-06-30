#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib as mpl


def simple_graph_plot():
    with open('result/result_simple.txt') as f:
        lines = f.readlines()
    x_values= [line.split(",")[0] for line in lines]
                      #regular expr per pulire la stringa (grazie professor Bagdanov)
    y_values= [line.split(",")[1] for line in lines]
    x_values = [s.replace("(", "").replace("'", "").replace(" ", "") for s in x_values]
    y_values=[s.replace(")", "").replace("\n","").replace(" ","") for s in y_values]

    x_values[:] = (elem[:5] for elem in x_values)


    x_values = [float(item) for item in x_values]
    y_values = [int(item) for item in y_values]

    # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.scatter(y_values,x_values, label='linear',s=10)  # Plot some data on the axes.
    ax.set_ylabel('Tempo (s)')  # Add an x-label to the axes.
    ax.set_xlabel('N° nodi')  # Add a y-label to the axes.
    ax.set_title("Generazione grafo non pesato")  # Add a title to the axes.

    plt.yticks(np.arange(0, 1 ,step= 0.2))
    plt.savefig('result/simple_graph.png')
    plt.show()


def weighted_graph_plot():
    with open('result/result_wei.txt') as f:
        lines = f.readlines()
    x_values = [line.split(",")[0] for line in lines]
    y_values = [line.split(",")[1] for line in lines]
    x_values = [s.replace("(", "").replace("'", "").replace(" ", "") for s in x_values]
    y_values = [s.replace(")", "").replace("\n", "").replace(" ", "") for s in y_values]

    x_values[:] = (elem[:5] for elem in x_values)


    x_values = [float(item) for item in x_values]
    y_values = [int(item) for item in y_values]

    # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.scatter(y_values, x_values, label='linear',s = 10)  # Plot some data on the axes.
    ax.set_ylabel('Tempo (s)')  # Add an x-label to the axes.
    ax.set_xlabel('N° nodi')  # Add a y-label to the axes.
    ax.set_title("Generazione grafo pesato")  # Add a title to the axes.

    plt.yticks(np.arange(0, 1, step=0.2))
    plt.savefig('result/weighted_graph.png')
    plt.show()



def mst_graph_plot():
    with open('result/result_mst.txt') as f:
        lines = f.readlines()
    z_values = [line.split(",")[0] for line in lines]       #tempo
    y_values = [line.split(",")[1] for line in lines]       #nodi
    x_values = [line.split(",")[2] for line in lines]       #archi
    z_values = [s.replace("[", "").replace("'", "").replace(" ", "") for s in z_values]
    y_values = [s.replace("]", "").replace("\n", "").replace(" ", "") for s in y_values]
    x_values = [s.replace("]", "").replace("\n", "").replace(" ", "") for s in x_values]
    z_values[:] = (elem[:5] for elem in z_values)


    z_values = [float(item) for item in z_values]
    y_values = [int(item) for item in y_values]
    x_values = [int(item) for item in x_values]

    # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
    fig=plt.figure()
    ax=plt.axes(projection='3d')# Create a figure and an axes.

    ax.scatter(x_values, y_values,z_values, cmap=plt.cm.magma)  # Plot some data on the axes.


    ax.set_zlabel('Tempo (s)')  # Add an x-label to the axes.
    ax.set_ylabel('N° nodi')  # Add a y-label to the axes.
    ax.set_xlabel('N° archi',labelpad=10)
    ax.set_title("Generazione grafo MST")
    # Add a title to the axes.
    ax.tick_params(axis='x',labelrotation=45)

    plt.xticks(np.arange(2000000, 5000000, step=150000))
    plt.savefig('result/mst_graph.png')
    plt.show()


