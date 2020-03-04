from mpi4py import MPI
import numpy as np
import mpids.MPInumpy as mpi_np
import gc

measure_time = lambda: MPI.Wtime()

def creation(size, iters=10000, comm=MPI.COMM_WORLD):
    data = np.arange(size, dtype=np.float64).tolist()
    time = measure_time()
    for _ in range(iters):
        mpi_np.array(data, dtype=np.float64)
    time = measure_time() - time
    gc.collect()
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def add(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr + 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def sub(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr - 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def mul(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr * 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def div(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr / 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def _max(mpi_np_arr, iters=10000, axis=None, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.max(axis=axis)
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters


def _mean(mpi_np_arr, iters=10000, axis=None, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.mean(axis=axis)
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def _sum(mpi_np_arr, iters=10000, axis=None, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.sum(axis=axis)
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def _std(mpi_np_arr, iters=10000, axis=None, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.std(axis=axis)
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def slicing(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr[::2]
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def iterate(mpi_np_arr, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        for val in mpi_np_arr:
            pass
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def reshape(mpi_np_arr, size, iters=10000, comm=MPI.COMM_WORLD):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.reshape(size, 1)
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()
    local_size =  2**17
    size = n_procs * local_size
    iters = 1
    mpi_np_arr = mpi_np.arange(size, dtype=np.float64)

    creation_time = creation(size, iters=iters)
    add_time = add(mpi_np_arr, iters=iters)
    sub_time = sub(mpi_np_arr, iters=iters)
    mul_time = mul(mpi_np_arr, iters=iters)
    div_time = div(mpi_np_arr, iters=iters)
    max_time = _max(mpi_np_arr, iters=iters)
    mean_time = _mean(mpi_np_arr, iters=iters)
    sum_time = _sum(mpi_np_arr, iters=iters)
    std_time = _std(mpi_np_arr, iters=iters)
    slicing_time = slicing(mpi_np_arr, iters=iters)
    iterate_time = iterate(mpi_np_arr, iters=iters)
    reshape_time = reshape(mpi_np_arr, size, iters=iters)

    if rank == 0:
        print("mpi_np,creation,%d,%d,%.9f" %(n_procs, local_size, creation_time))
        print("mpi_np,add,%d,%d,%.9f" %(n_procs, local_size, add_time))
        print("mpi_np,sub,%d,%d,%.9f" %(n_procs, local_size, sub_time))
        print("mpi_np,mul,%d,%d,%.9f" %(n_procs, local_size, mul_time))
        print("mpi_np,div,%d,%d,%.9f" %(n_procs, local_size, div_time))
        print("mpi_np,max,%d,%d,%.9f" %(n_procs, local_size, max_time))
        print("mpi_np,mean,%d,%d,%.9f" %(n_procs, local_size, mean_time))
        print("mpi_np,sum,%d,%d,%.9f" %(n_procs, local_size, sum_time))
        print("mpi_np,std,%d,%d,%.9f" %(n_procs, local_size, std_time))
        print("mpi_np,slice,%d,%d,%.9f" %(n_procs, local_size, slicing_time))
        print("mpi_np,iterate,%d,%d,%.9f" %(n_procs, local_size, iterate_time))
        print("mpi_np,reshape,%d,%d,%.9f" %(n_procs, local_size, reshape_time))
