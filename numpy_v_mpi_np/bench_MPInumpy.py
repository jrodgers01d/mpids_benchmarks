from mpi4py import MPI
import numpy as np
import mpids.MPInumpy as mpi_np
import gc

measure_time = lambda: MPI.Wtime()

def creation(size, iters=10000):
    data = np.arange(size, dtype=np.float64).tolist()
    time = measure_time()
    for _ in range(iters):
        mpi_np.array(data, dtype=np.float64)
    time = measure_time() - time
    gc.collect()
    return time/iters

def add(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr + 1.0
    time = measure_time() - time
    return time/iters

def sub(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr - 1.0
    time = measure_time() - time
    return time/iters

def mul(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr * 1.0
    time = measure_time() - time
    return time/iters

def div(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr / 1.0
    time = measure_time() - time
    gc.collect()
    return time/iters

def _max(mpi_np_arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.max(axis=axis)
    time = measure_time() - time
    return time/iters


def _mean(mpi_np_arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.mean(axis=axis)
    time = measure_time() - time
    return time/iters

def _sum(mpi_np_arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.sum(axis=axis)
    time = measure_time() - time
    return time/iters

def _std(mpi_np_arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.std(axis=axis)
    time = measure_time() - time
    return time/iters

def slicing(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr[::2]
    time = measure_time() - time
    return time/iters

def iterate(mpi_np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        for val in mpi_np_arr:
            pass
    time = measure_time() - time
    return time/iters

def reshape(mpi_np_arr, size, iters=10000):
    time = measure_time()
    for _ in range(iters):
        mpi_np_arr.reshape(size, 1)
    time = measure_time() - time
    return time/iters

if __name__ == '__main__':
    for power in range(0, 28):
        iters = 10000 if power < 5 else 100 if power < 6 else 1
        size = 2**power
        print("mpi_np,creation,%d,%.9f" %(size, creation(size, iters)))
        mpi_np_arr = mpi_np.arange(size, dtype=np.float64)
        print("mpi_np,add,%d,%.9f" %(size, add(mpi_np_arr, iters=iters)))
        print("mpi_np,sub,%d,%.9f" %(size, sub(mpi_np_arr, iters=iters)))
        print("mpi_np,mul,%d,%.9f" %(size, mul(mpi_np_arr, iters=iters)))
        print("mpi_np,div,%d,%.9f" %(size, div(mpi_np_arr, iters=iters)))
        print("mpi_np,max,%d,%.9f" %(size, _max(mpi_np_arr, iters=iters)))
        print("mpi_np,mean,%d,%.9f" %(size, _mean(mpi_np_arr, iters=iters)))
        print("mpi_np,sum,%d,%.9f" %(size, _sum(mpi_np_arr, iters=iters)))
        print("mpi_np,std,%d,%.9f" %(size, _std(mpi_np_arr, iters=iters)))
        print("mpi_np,slice,%d,%.9f" %(size, slicing(mpi_np_arr, iters=iters)))
        print("mpi_np,iterate,%d,%.9f" %(size, iterate(mpi_np_arr, iters=iters)))
        if power > 24:
            continue
        print("mpi_np,reshape,%d,%.9f" %(size, reshape(mpi_np_arr, size, iters=iters)))
