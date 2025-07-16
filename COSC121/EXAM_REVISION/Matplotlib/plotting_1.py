import matplotlib.pyplot as plt
import numpy as np

'''Make a scatter plot and line plot'''
def graph(x, y1, y2):

    '''Create the scatter plot'''
    axes = plt.axes()
    y1s = np.array(y1)
    y2s = np.array(y2)
    xs = np.array(x)

   # print('ys:', ys, 'xs:' , xs)
    
    plt.scatter(xs, y1s)
    # axes.plot(xs, y2s)
    plt.show()


x = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 1, 4, 9, 16, 25])
y2 = np.array([0, 1, 2, 1, 0, -1])

print(graph(x, y1, y2))