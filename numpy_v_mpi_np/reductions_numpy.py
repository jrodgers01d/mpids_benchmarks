import numpy as np
from operations import _max, _mean, _sum, _std

if __name__ == '__main__':
    for power in range(0, 28):
        variable_iters = 10000 if power < 21 else 10
        size = 2**power
        np_arr = np.arange(size, dtype=np.float64)
        print("np,max,%d,%.9f" %(size, _max(np_arr, iters=variable_iters)))
        print("np,mean,%d,%.9f" %(size, _mean(np_arr, iters=variable_iters)))
        print("np,sum,%d,%.9f" %(size, _sum(np_arr, iters=variable_iters)))
        print("np,std,%d,%.9f" %(size, _std(np_arr, iters=variable_iters)))
        del np_arr
