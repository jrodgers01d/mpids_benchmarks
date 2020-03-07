from mpi4py import MPI
import numpy as np
import mpids.MPInumpy as mpi_np
import gc

measure_time = lambda: MPI.Wtime()

def empty(size, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np.empty(size, dtype=np.float64)
    time = measure_time() - time
    gc.collect()
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def arange(size, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np.arange(size, dtype=np.float64)
    time = measure_time() - time
    gc.collect()
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def global_iterate(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    elements = mpi_np_arr.globalshape[0]
    time = measure_time()
    for _ in range(iters):
        for index in range(elements):
            mpi_np_arr[index]
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def local_slicing(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.local[::2]
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def local_setting(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.local[0] = 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def global_setting(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr[0] = 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def local_getting(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.local[0]
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def global_getting(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr[0]
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

    empty_time = empty(size, iters=iters)
    arange_time = arange(size, iters=iters)
    local_slicing_time = local_slicing(mpi_np_arr, iters=10000)
    local_setting_time = local_setting(mpi_np_arr, iters=10000)
    global_setting_time = global_setting(mpi_np_arr, iters=10000)
    local_getting_time = local_getting(mpi_np_arr, iters=10000)
    global_getting_time = global_getting(mpi_np_arr, iters=iters)

    if rank == 0:
        print("mpi_np,empty,%d,%d,%.9f" %(n_procs, local_size, empty_time))
        print("mpi_np,arange,%d,%d,%.9f" %(n_procs, local_size, arange_time))
        print("mpi_np,local_slicing,%d,%d,%.9f" %(n_procs, local_size, local_slicing_time))
        print("mpi_np,local_setting,%d,%d,%.9f" %(n_procs, local_size, local_setting_time))
        print("mpi_np,global_setting,%d,%d,%.9f" %(n_procs, local_size, global_setting_time))
        print("mpi_np,local_getting,%d,%d,%.9f" %(n_procs, local_size, local_getting_time))
        print("mpi_np,global_getting,%d,%d,%.9f" %(n_procs, local_size, global_getting_time))
