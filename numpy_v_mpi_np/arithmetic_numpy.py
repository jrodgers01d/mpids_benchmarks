import numpy as np
from operations import add, sub, mul, div

if __name__ == '__main__':
    for power in range(0, 28):
        variable_iters = 10000 if power < 18 else 10
        size = 2**power
        np_arr = np.arange(size, dtype=np.float64)
        print("np,add,%d,%.9f" %(size, add(np_arr, iters=variable_iters)))
        print("np,sub,%d,%.9f" %(size, sub(np_arr, iters=variable_iters)))
        print("np,mul,%d,%.9f" %(size, mul(np_arr, iters=variable_iters)))
        print("np,div,%d,%.9f" %(size, div(np_arr, iters=variable_iters)))
        del np_arr
