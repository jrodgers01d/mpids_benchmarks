from mpi4py import MPI
import numpy as np
import gc

measure_time = lambda: MPI.Wtime()

def empty(size, iters=10000):
    time = measure_time()
    for _ in range(iters):
        np.empty(size, dtype=np.float64)
    time = measure_time() - time
    gc.collect()
    return time/iters

def arange(size, iters=10000):
    time = measure_time()
    for _ in range(iters):
        np.arange(size, dtype=np.float64)
    time = measure_time() - time
    gc.collect()
    return time/iters

def setting(np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        np_arr[0] = 1.0
    time = measure_time() - time
    return time/iters

def getting(np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        np_arr[0]
    time = measure_time() - time
    return time/iters

if __name__ == '__main__':
    for power in range(0, 28):
        iters = 10000 if power < 5 else 1000 if power < 6 else 10
        size = 2**power
        print("np,empty,%d,%.9f" %(size, empty(size, iters=iters)))
        print("np,arange,%d,%.9f" %(size, arange(size, iters=iters)))
        np_arr = np.arange(size, dtype=np.float64)
        print("np,setting,%d,%.9f" %(size, setting(np_arr, iters=10000)))
        print("np,getting,%d,%.9f" %(size, getting(np_arr, iters=10000)))
