import matplotlib.pyplot as plt
import numpy as np

def graph():
    axes = plt.axes()
    axes.set_xlabel('x axes')
    axes.set_ylabel('y axes')

    xs = np.linspace(-10.0, 10.0)
    ys = xs**3-3*xs+250


    axes.plot(xs, ys)
    plt.show()

graph()