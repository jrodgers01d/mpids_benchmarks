from mpi4py import MPI
import numpy as np

measure_time = lambda: MPI.Wtime()

#Creation Routines
def array(size, lib, iters=10000):
    data = np.arange(size, dtype=np.float64).tolist()
    time = measure_time()
    for _ in range(iters):
        lib.array(data, dtype=np.float64)
    time = measure_time() - time
    return time/iters

def empty(size, lib, iters=10000):
    time = measure_time()
    for _ in range(iters):
        lib.empty(size, dtype=np.float64)
    time = measure_time() - time
    return time/iters

def arange(size, lib, iters=10000):
    time = measure_time()
    for _ in range(iters):
        lib.arange(size, dtype=np.float64)
    time = measure_time() - time
    return time/iters

#Reduction Operations
def add(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr + 1.0
    time = measure_time() - time
    return time/iters

def sub(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr - 1.0
    time = measure_time() - time
    return time/iters

def mul(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr * 1.0
    time = measure_time() - time
    return time/iters

def div(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr / 1.0
    time = measure_time() - time
    return time/iters

#Arithmetic Operations
def _max(arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        arr.max(axis=axis)
    time = measure_time() - time
    return time/iters

def _mean(arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        arr.mean(axis=axis)
    time = measure_time() - time
    return time/iters

def _sum(arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        arr.sum(axis=axis)
    time = measure_time() - time
    return time/iters

def _std(arr, iters=10000, axis=None):
    time = measure_time()
    for _ in range(iters):
        arr.std(axis=axis)
    time = measure_time() - time
    return time/iters

#Access Operations
def setting(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr[0] = 1.0
    time = measure_time() - time
    return time/iters

def getting(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr[0]
    time = measure_time() - time
    return time/iters

def slicing(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr[::2]
    time = measure_time() - time
    return time/iters

def iterate(arr, iters=10000):
    time = measure_time()
    for _ in range(iters):
        for val in arr:
            pass
    time = measure_time() - time
    return time/iters

def reshape(arr, size, iters=10000):
    time = measure_time()
    for _ in range(iters):
        arr.reshape(size, 1)
    time = measure_time() - time
    return time/iters
