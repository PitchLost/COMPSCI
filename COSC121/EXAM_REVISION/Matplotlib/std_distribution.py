import matplotlib.pyplot as plt
import numpy as np




'''No loops, if statements or lists allowed in this function'''

def main():
    '''Hello!'''
    axes = plt.axes()

    xs = np.linspace(-4.0, 4.0)
    ys = 1/((2*np.pi)**(1/2))*np.e**((-xs**2)/2)

    axes.plot(xs, ys)

    axes.set_title('A normal distribution, f(x), with mean = 0, variance = 1')
    axes.set_xlabel('x')
    axes.set_ylabel('f(x)')
    axes.grid(True)

    plt.show()

main()


