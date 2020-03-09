import mpids.MPInumpy as mpi_np
from mpi4py import MPI
from operations import array, empty, arange

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()
    size = 2**25
    iters = 1

    variable_iters = 1 if n_procs < 128 else 100

    array_time = array(size, iters=iters)
    empty_time = empty(size, iters=10000)
    arange_time = arange(size, iters=variable_iters)

    if rank == 0:
        print("mpi_np,array,%d,%d,%.9f" %(n_procs, size, array_time))
        print("mpi_np,empty,%d,%d,%.9f" %(n_procs, size, empty_time))
        print("mpi_np,arange,%d,%d,%.9f" %(n_procs, size, arange_time))
