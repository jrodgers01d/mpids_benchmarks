import mpids.MPInumpy as mpi_np
import numpy as np
from mpi4py import MPI
from operations import _max, _mean, _sum, _std

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

    max_time = _max(mpi_np_arr, iters=iters)
    mean_time = _mean(mpi_np_arr, iters=iters)
    sum_time = _sum(mpi_np_arr, iters=iters)
    std_time = _std(mpi_np_arr, iters=iters)

    if rank == 0:
        print("mpi_np,max,%d,%d,%.9f" %(n_procs, size, max_time))
        print("mpi_np,mean,%d,%d,%.9f" %(n_procs, size, mean_time))
        print("mpi_np,sum,%d,%d,%.9f" %(n_procs, size, sum_time))
        print("mpi_np,std,%d,%d,%.9f" %(n_procs, size, std_time))
