from mpi4py import MPI
import numpy as np
import mpids.MPInumpy as mpi_np

measure_time = lambda: MPI.Wtime()

#Creation Routines
def array(size, iters=10000, comm=MPI.COMM_WORLD):
    data = np.arange(size, dtype=np.float64).tolist()
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        mpi_np.array(data, dtype=np.float64, comm=comm, dist='b')
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def empty(size, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        mpi_np.empty(size, dtype=np.float64, comm=comm, dist='b')
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def arange(size, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        mpi_np.arange(size, dtype=np.float64, comm=comm, dist='b')
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

#Reduction Operations
def add(arr, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr + 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def sub(arr, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr - 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def mul(arr, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr * 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def div(arr, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr / 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

#Arithmetic Operations
def _max(arr, iters=10000, axis=None, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr.max(axis=axis)
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def _mean(arr, iters=10000, axis=None, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr.mean(axis=axis)
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def _sum(arr, iters=10000, axis=None, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr.sum(axis=axis)
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def _std(arr, iters=10000, axis=None, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr.std(axis=axis)
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

#Access Operations
def setting(arr, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr[0] = 1.0
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def getting(arr, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr[0]
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def slicing(arr, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr[::2]
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def iterate(arr, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        for val in arr:
            pass
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def reshape(arr, size, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr.reshape(size, 1)
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters

def collect_data(arr, iters=10000, comm=MPI.COMM_WORLD):
    comm.Barrier()
    time = measure_time()
    for _ in range(iters):
        arr.collect_data()
    time = measure_time() - time
    comm.reduce(time, op=MPI.MAX, root=0)
    return time/iters
