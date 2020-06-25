# tell python to look at the numpy libary and call it np
# numpy is a library for matrix and vector math
import numpy as np
# matplotlib plots numpy and python arrays
import matplotlib.pyplot as plt

# make an array of numbers between -5 and 5 with 0.1 between them
# x will look like [-5, -4.9, -4.8, ..., 4.7, 4.8, 4.9]
x = np.arange(-5, 5, 0.1)
# now make a plot with our x values determined by our array called x
# np.square(x) returns an array of the squares of each element of x, which we will use for our y values
plt.plot(x, np.square(x))
# tell matplotlib to open a window with our plot in it
plt.show()
