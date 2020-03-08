import numpy as np
from operations import reshape

if __name__ == '__main__':
    for power in range(0, 25):
        size = 2**power
        np_arr = np.arange(size, dtype=np.float64)
        print("np,reshape,%d,%.9f" %(size, reshape(np_arr, size, iters=100000)))
        del np_arr
