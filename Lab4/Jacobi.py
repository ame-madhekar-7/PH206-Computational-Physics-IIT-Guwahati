
import numpy as np
A = [[3.0, 2.0], [2.0, 1.0]]

theta = np.arctan(2 * A[0][1] / (A[0][0] - A[1][1])) / 2
print(theta * 180 / 3.142)

c = np.cos(theta)
s = np.sin(theta)

R = [[c, -s], [s, c]]
print(R)
