import mpids.MPInumpy as mpi_np
import numpy as np
from mpi4py import MPI
from operations import getting, setting, slicing

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()
    local_size =  2**16
    size = n_procs * local_size
    iters = 1
    mpi_np_arr = mpi_np.arange(size, dtype=np.float64)

    variable_iters = 10000 if n_procs < 16 else 10

    setting_time = setting(mpi_np_arr)
    getting_time = getting(mpi_np_arr, iters=variable_iters)
    slicing_time = slicing(mpi_np_arr, iters=iters)

    if rank == 0:
        print("mpi_np,global_setting,%d,%d,%.9f" %(n_procs, local_size, setting_time))
        print("mpi_np,global_getting,%d,%d,%.9f" %(n_procs, local_size, getting_time))
        print("mpi_np,global_slice,%d,%d,%.9f" %(n_procs, local_size, slicing_time))
