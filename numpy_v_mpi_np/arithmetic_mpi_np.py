import mpids.MPInumpy as mpi_np
import numpy as np
from operations import add, sub, mul, div

if __name__ == '__main__':
    for power in range(0, 28):
        variable_iters = 10000 if power < 18 else 10
        size = 2**power
        mpi_np_arr = mpi_np.arange(size, dtype=np.float64)
        print("mpi_np,add,%d,%.9f" %(size, add(mpi_np_arr, iters=variable_iters)))
        print("mpi_np,sub,%d,%.9f" %(size, sub(mpi_np_arr, iters=variable_iters)))
        print("mpi_np,mul,%d,%.9f" %(size, mul(mpi_np_arr, iters=variable_iters)))
        print("mpi_np,div,%d,%.9f" %(size, div(mpi_np_arr, iters=variable_iters)))
        del mpi_np_arr
