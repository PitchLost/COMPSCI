import numpy as np
import matplotlib.pyplot as plt

'''What the actual sigma?'''

def graphLoadedTxt(ys):
    axes = plt.axes()
    xs = np.arange(0, 365, 1)
    axes.bar(xs, ys)
    axes.set_title('Lake Taylor Station Rainfalls, 2005')
    axes.set_ylabel('Rainfall (mm)')
    axes.set_xlabel('Day number')

    axes.grid(True)
    plt.show()


def loadtxt(filename):
    '''Gurt: Yo'''
    infile = np.loadtxt(filename, skiprows=9, delimiter=',', usecols=3)

    graphLoadedTxt(infile)
    
    print(f"{len(infile)} records read")
    print(f"Minimum: {min(infile)}")
    print(f"Maximum: {max(infile)}")
    print(f"Average: {np.average(infile):.2f}")
    print(f"Standard deviation: {np.std(infile):.2f}")

loadtxt('sigmatxtfile.txt')

