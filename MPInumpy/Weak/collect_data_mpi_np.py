import mpids.MPInumpy as mpi_np
import numpy as np
from mpi4py import MPI
from operations import collect_data

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()
    local_size =  2**16
    size = n_procs * local_size
    iters = 1
    mpi_np_arr = mpi_np.arange(size, dtype=np.float64)

    collect_data_time = collect_data(mpi_np_arr, iters=iters)

    if rank == 0:
        print("mpi_np,collect_data,%d,%d,%.9f" %(n_procs, local_size, collect_data_time))
