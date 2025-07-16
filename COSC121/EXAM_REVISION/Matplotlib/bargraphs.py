import matplotlib.pyplot as plt
import numpy as np

def graph(y):
    x = np.arange(-10, 10)
    axes = plt.axes()
    axes.set_title('My bar graph!')
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.bar(x, y)
    plt.show()


graph([1, 2, 3, 4, 5, 6, 7, 1, 5, 11, 14, 9, 0, 1, 5, 8, 11, 14, 5, 1])