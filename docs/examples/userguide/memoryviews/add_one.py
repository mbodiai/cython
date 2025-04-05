import numpy as np
import cython
def add_one(buf: cython.int[:,:]):
    for x in range(buf.shape[0]):
        for y in range(buf.shape[1]):
            buf[x, y] += 1

# exporting_object must be a Python object
# implementing the buffer interface, e.g. a numpy array.
exporting_object = np.zeros((1, 2), dtype=np.intc)
print(exporting_object)
add_one(exporting_object)
print(exporting_object) 