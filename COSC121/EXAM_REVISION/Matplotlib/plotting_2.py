import matplotlib.pyplot as plt
import numpy as np


'''Hello'''
def plot_values(xs, ys):
    axes = plt.axes()
    axes.plot(xs, ys)
    axes.set_title('Graph!')
    axes.set_xlabel('The x axes!')
    axes.set_ylabel('The y axes!')


    plt.show()

plot_values([0.0, 0.2, 0.4, 0.6, 0.8, 1.0], [3.2, 7.9, 2.6, 5.1, 4.9, 6.0])