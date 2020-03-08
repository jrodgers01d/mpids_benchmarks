import mpids.MPInumpy as mpi_np
import numpy as np
from mpi4py import MPI
from operations import add, sub, mul, div

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()
    local_size =  2**16
    size = n_procs * local_size
    iters = 1000
    mpi_np_arr = mpi_np.arange(size, dtype=np.float64)

    add_time = add(mpi_np_arr, iters=iters)
    sub_time = sub(mpi_np_arr, iters=iters)
    mul_time = mul(mpi_np_arr, iters=iters)
    div_time = div(mpi_np_arr, iters=iters)

    if rank == 0:
        print("mpi_np,add,%d,%d,%.9f" %(n_procs, local_size, add_time))
        print("mpi_np,sub,%d,%d,%.9f" %(n_procs, local_size, sub_time))
        print("mpi_np,mul,%d,%d,%.9f" %(n_procs, local_size, mul_time))
        print("mpi_np,div,%d,%d,%.9f" %(n_procs, local_size, div_time))
