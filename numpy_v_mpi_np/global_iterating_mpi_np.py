import mpids.MPInumpy as mpi_np
import numpy as np
from operations import measure_time

def global_iterating(arr, iters=10000):
    size = arr.globalsize
    time = measure_time()
    for _ in range(iters):
        for index in range(size):
            arr[index]
    time = measure_time() - time
    return time/iters

if __name__ == '__main__':
    for power in range(0, 22):
        variable_iters = 1000 if power < 4 else 10 if power < 8 else 1
        size = 2**power
        mpi_np_arr = mpi_np.arange(size, dtype=np.float64)
        #Resolve properties
        mpi_np_arr.globalshape
        mpi_np_arr.globalsize
        mpi_np_arr.globalndim

        print("mpi_np,global_iterate,%d,%.9f" %(size, global_iterating(mpi_np_arr, iters=variable_iters)))
        del mpi_np_arr
