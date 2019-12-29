import numpy as np

import opfython.math.distance as d

# Defining an array
x = np.asarray([2, 3, 4, 5])

# Defining an second array
y = np.asarray([1, 2, 3, 1])

# Calculating their distance
dist = d.euclidean_distance(x, y)
