import mpids.MPInumpy as mpi_np
import numpy as np
from mpi4py import MPI
from operations import measure_time

def global_iterating(arr, iters=10000, comm=MPI.COMM_WORLD):
    size = arr.globalsize
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        for index in range(size):
            arr[index]
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters


if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()
    local_size =  2**16
    size = n_procs * local_size
    iters = 1
    mpi_np_arr = mpi_np.arange(size, dtype=np.float64)

    global_iterate_time = global_iterating(mpi_np_arr, iters=iters)

    if rank == 0:
        print("mpi_np,global_iterate,%d,%d,%.9f" %(n_procs, local_size, global_iterate_time))
