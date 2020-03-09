import mpids.MPInumpy as mpi_np
from mpi4py import MPI
from operations import array, empty, arange

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()
    local_size =  2**16
    size = n_procs * local_size
    iters = 1

    array_time = array(size, iters=iters)
    empty_time = empty(size, iters=10000)
    arange_time = arange(size, iters=1000)

    if rank == 0:
        print("mpi_np,array,%d,%d,%.9f" %(n_procs, local_size, array_time))
        print("mpi_np,empty,%d,%d,%.9f" %(n_procs, local_size, empty_time))
        print("mpi_np,arange,%d,%d,%.9f" %(n_procs, local_size, arange_time))
