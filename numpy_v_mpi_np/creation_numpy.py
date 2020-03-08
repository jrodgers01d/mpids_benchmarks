import numpy as np
from operations import array, empty, arange

if __name__ == '__main__':
    for power in range(0, 28):
        variable_iters = 10000 if power < 14 else 10
        size = 2**power
        print("np,array,%d,%.9f" %(size, array(size, np, iters=variable_iters)))
        print("np,empty,%d,%.9f" %(size, empty(size, np, iters = 100000)))
        print("np,arange,%d,%.9f" %(size, arange(size, np, iters=variable_iters)))
