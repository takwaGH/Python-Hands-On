import numpy as np
array1 = np.array([0, 1, 2])
array2 = np.array([2, 1, 0])
r = np.cov(array1, array2)
print(r)