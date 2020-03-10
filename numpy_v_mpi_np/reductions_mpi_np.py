import mpids.MPInumpy as mpi_np
import numpy as np
from operations import _max, _mean, _sum, _std

if __name__ == '__main__':
    for power in range(0, 28):
        variable_iters = 10000 if power < 21 else 10
        size = 2**power
        mpi_np_arr = mpi_np.arange(size, dtype=np.float64)


        print("mpi_np,max,%d,%.9f" %(size, _max(mpi_np_arr, iters=variable_iters)))
        print("mpi_np,mean,%d,%.9f" %(size, _mean(mpi_np_arr, iters=variable_iters)))
        print("mpi_np,sum,%d,%.9f" %(size, _sum(mpi_np_arr, iters=variable_iters)))
        print("mpi_np,std,%d,%.9f" %(size, _std(mpi_np_arr, iters=variable_iters)))
        del mpi_np_arr
