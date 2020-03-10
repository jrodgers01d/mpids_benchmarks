import mpids.MPInumpy as mpi_np
import numpy as np
from operations import reshape

if __name__ == '__main__':
    for power in range(0, 25):
        variable_iters = 100 if power < 10 else 1
        size = 2**power
        mpi_np_arr = mpi_np.arange(size, dtype=np.float64)
        #Resolve properties
        mpi_np_arr.globalshape
        mpi_np_arr.globalsize
        mpi_np_arr.globalndim

        print("mpi_np,reshape,%d,%.9f" %(size, reshape(mpi_np_arr, size, iters=variable_iters)))
        del mpi_np_arr
