import mpids.MPInumpy as mpi_np
import numpy as np
from mpi4py import MPI
from operations import reshape

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()
    size = 2**25
    iters = 1
    mpi_np_arr = mpi_np.arange(size, dtype=np.float64)
    #Resolve properties
    mpi_np_arr.globalshape
    mpi_np_arr.globalsize
    mpi_np_arr.globalndim

    reshape_time = reshape(mpi_np_arr, size, iters=iters)

    if rank == 0:
        print("mpi_np,reshape,%d,%d,%.9f" %(n_procs, size, reshape_time))
