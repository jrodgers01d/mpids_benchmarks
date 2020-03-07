from mpi4py import MPI
import numpy as np
import mpids.MPInumpy as mpi_np
import gc

measure_time = lambda: MPI.Wtime()

def collect_data(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.collect_data()
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()
    local_size =  2**16
    size = n_procs * local_size
    iters = 100
    mpi_np_arr = mpi_np.arange(size, dtype=np.float64)

    collect_data_time = collect_data(mpi_np_arr, iters=iters)

    if rank == 0:
        print("mpi_np,collect_data,%d,%d,%.9f" %(n_procs, local_size, collect_data_time))
