import numpy as np
import matplotlib.pyplot as plt

def plot_squared(n, x0, x1):
    x = np.linspace(x0, x1)
    y = x**2
    axes = plt.axes()
    axes.set_title('y=x * x')
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.grid(True)
    axes.plot(x, y)
    plt.show()
plot_squared(5, 0, 1)