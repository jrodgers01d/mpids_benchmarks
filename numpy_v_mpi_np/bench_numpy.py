from mpi4py import MPI
import numpy as np
import gc

measure_time = lambda: MPI.Wtime()

def creation(size, iters=10000):
    data = np.arange(size, dtype=np.float64).tolist()
    time = measure_time()
    for _ in range(iters):
        np.array(data, dtype=np.float64)
    time = measure_time() - time
    gc.collect()
    return time/iters

def add(np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        np_arr + 1.0
    time = measure_time() - time
    return time/iters

def sub(np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        np_arr - 1.0
    time = measure_time() - time
    return time/iters

def mul(np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        np_arr * 1.0
    time = measure_time() - time
    return time/iters

def div(np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        np_arr / 1.0
    time = measure_time() - time
    gc.collect()
    return time/iters

def _max(np_arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        np_arr.max(axis=axis)
    time = measure_time() - time
    return time/iters


def _mean(np_arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        np_arr.mean(axis=axis)
    time = measure_time() - time
    return time/iters

def _sum(np_arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        np_arr.sum(axis=axis)
    time = measure_time() - time
    return time/iters

def _std(np_arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        np_arr.std(axis=axis)
    time = measure_time() - time
    return time/iters

def slicing(np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        np_arr[::2]
    time = measure_time() - time
    return time/iters

def iterate(np_arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        for val in np_arr:
            pass
    time = measure_time() - time
    return time/iters

def reshape(np_arr, size, iters=10000):
    time = measure_time()
    for _ in range(iters):
        np_arr.reshape(size, 1)
    time = measure_time() - time
    return time/iters

if __name__ == '__main__':
    for power in range(0, 28):
        iters = 10000 if power < 5 else 100 if power < 6 else 1
        size = 2**power
        print("np,creation,%d,%.9f" %(size, creation(size, iters)))
        np_arr = np.arange(size, dtype=np.float64)
        print("np,add,%d,%.9f" %(size, add(np_arr, iters=iters)))
        print("np,sub,%d,%.9f" %(size, sub(np_arr, iters=iters)))
        print("np,mul,%d,%.9f" %(size, mul(np_arr, iters=iters)))
        print("np,div,%d,%.9f" %(size, div(np_arr, iters=iters)))
        print("np,max,%d,%.9f" %(size, _max(np_arr, iters=iters)))
        print("np,mean,%d,%.9f" %(size, _mean(np_arr, iters=iters)))
        print("np,sum,%d,%.9f" %(size, _sum(np_arr, iters=iters)))
        print("np,std,%d,%.9f" %(size, _std(np_arr, iters=iters)))
        print("np,slice,%d,%.9f" %(size, slicing(np_arr, iters=iters)))
        print("np,iterate,%d,%.9f" %(size, iterate(np_arr, iters=iters)))
        print("np,reshape,%d,%.9f" %(size, reshape(np_arr, size, iters=iters)))
