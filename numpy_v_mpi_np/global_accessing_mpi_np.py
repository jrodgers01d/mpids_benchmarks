import mpids.MPInumpy as mpi_np
import numpy as np
from operations import getting, setting, slicing, iterate

if __name__ == '__main__':
    for power in range(0, 28):
        variable_iters = 10000 if power < 18 else 10
        gbl_variable_iters = 10000 if power < 8 else 100 if power < 17 else 1
        size = 2**power
        mpi_np_arr = mpi_np.arange(size, dtype=np.float64)
        print("mpi_np,global_setting,%d,%.9f" %(size, getting(mpi_np_arr, iters=1000)))
        print("mpi_np,global_getting,%d,%.9f" %(size, setting(mpi_np_arr, iters=100000)))
        print("mpi_np,global_slice,%d,%.9f" %(size, slicing(mpi_np_arr, iters=variable_iters)))
        print("mpi_np,global_iterate,%d,%.9f" %(size, iterate(mpi_np_arr, iters=gbl_variable_iters)))
        del mpi_np_arr
