from mpi4py import MPI
import numpy as np
import mpids.MPInumpy as mpi_np
import gc

measure_time = lambda: MPI.Wtime()

def empty(size, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np.empty(size, dtype=np.float64)
    time = measure_time() - time
    gc.collect()
    return time/iters

def arange(size, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np.arange(size, dtype=np.float64)
    time = measure_time() - time
    gc.collect()
    return time/iters

def global_iterate(mpi_np_arr, iters=10000):
    elements = mpi_np_arr.globalshape[0]
    time = measure_time()
    for _ in range(iters):
        for index in range(elements):
            mpi_np_arr[index]
    time = measure_time() - time
    return time/iters

def local_slicing(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.local[::2]
    time = measure_time() - time
    return time/iters

def local_setting(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.local[0] = 1.0
    time = measure_time() - time
    return time/iters

def global_setting(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr[0] = 1.0
    time = measure_time() - time
    return time/iters

def local_getting(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.local[0]
    time = measure_time() - time
    return time/iters

def global_getting(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr[0]
    time = measure_time() - time
    return time/iters

if __name__ == '__main__':
    for power in range(0, 28):
        iters = 10000 if power < 5 else 100 if power < 6 else 1
        size = 2**power
        print("mpi_np,empty,%d,%.9f" %(size, empty(size, iters=iters)))
        print("mpi_np,arange,%d,%.9f" %(size, arange(size, iters=iters)))
        mpi_np_arr = mpi_np.arange(size, dtype=np.float64)
        print("mpi_np,local_slicing,%d,%.9f" %(size, local_slicing(mpi_np_arr, iters=iters)))
        print("mpi_np,global_iterate,%d,%.9f" %(size, global_iterate(mpi_np_arr, iters=iters)))
        print("mpi_np,local_setting,%d,%.9f" %(size, local_setting(mpi_np_arr, iters=iters)))
        print("mpi_np,global_setting,%d,%.9f" %(size, global_setting(mpi_np_arr, iters=iters)))
        print("mpi_np,local_getting_time,%d,%.9f" %(size, local_getting(mpi_np_arr, iters=iters)))
        print("mpi_np,global_getting_time,%d,%.9f" %(size, global_getting(mpi_np_arr, iters=iters)))
