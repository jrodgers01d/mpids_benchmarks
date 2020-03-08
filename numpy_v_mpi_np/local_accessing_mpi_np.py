import mpids.MPInumpy as mpi_np
import numpy as np
from operations import iterate, measure_time

def local_setting(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr.local[0] = 1.0
    time = measure_time() - time
    return time/iters

def local_getting(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr.local[0]
    time = measure_time() - time
    return time/iters

def local_slicing(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr.local[::2]
    time = measure_time() - time
    return time/iters

if __name__ == '__main__':
    for power in range(0, 28):
        variable_iters = 10000 if power < 11 else 100 if power < 18 else 1
        size = 2**power
        mpi_np_arr = mpi_np.arange(size, dtype=np.float64)
        print("mpi_np,local_setting,%d,%.9f" %(size, local_setting(mpi_np_arr, iters=100000)))
        print("mpi_np,local_getting,%d,%.9f" %(size, local_getting(mpi_np_arr, iters=100000)))
        print("mpi_np,local_slice,%d,%.9f" %(size, local_slicing(mpi_np_arr, iters=100000)))
        print("mpi_np,local_iterate,%d,%.9f" %(size, iterate(mpi_np_arr, iters=variable_iters)))
        del mpi_np_arr
