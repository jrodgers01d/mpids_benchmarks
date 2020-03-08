import numpy as np
from operations import getting, setting, slicing, iterate

if __name__ == '__main__':
    for power in range(0, 28):
        variable_iters = 10000 if power < 11 else 100 if power < 18 else 1
        size = 2**power
        np_arr = np.arange(size, dtype=np.float64)
        print("np,setting,%d,%.9f" %(size, setting(np_arr, iters=100000)))
        print("np,getting,%d,%.9f" %(size, getting(np_arr, iters=100000)))
        print("np,slice,%d,%.9f" %(size, slicing(np_arr, iters=100000)))
        print("np,iterate,%d,%.9f" %(size, iterate(np_arr, iters=variable_iters)))
        del np_arr
