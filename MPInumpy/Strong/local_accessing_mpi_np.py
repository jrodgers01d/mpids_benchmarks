import mpids.MPInumpy as mpi_np
import numpy as np
from mpi4py import MPI
from operations import iterate, measure_time

def local_setting(arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        arr.local[0] = 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def local_getting(arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        arr.local[0]
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def local_slicing(arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        arr.local[::2]
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()
    size = 2**25
    iters = 1
    mpi_np_arr = mpi_np.arange(size, dtype=np.float64)

    local_setting_time = local_setting(mpi_np_arr, iters=100000)
    local_getting_time = local_getting(mpi_np_arr, iters=100000)
    local_slice_time = local_slicing(mpi_np_arr, iters=100000)
    local_iterate_time = iterate(mpi_np_arr, iters=1)

    if rank == 0:
        print("mpi_np,local_setting,%d,%d,%.9f" %(n_procs, size, local_setting_time))
        print("mpi_np,local_getting,%d,%d,%.9f" %(n_procs, size, local_getting_time))
        print("mpi_np,local_slice,%d,%d,%.9f" %(n_procs, size, local_slice_time))
        print("mpi_np,local_iterate,%d,%d,%.9f" %(n_procs, size, local_iterate_time))
