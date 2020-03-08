import mpids.MPInumpy as mpi_np
from operations import array, empty, arange

if __name__ == '__main__':
    for power in range(0, 28):
        variable_iters = 10000 if power < 14 else 10
        size = 2**power
        print("mpi_np,array,%d,%.9f" %(size, array(size, mpi_np, iters=variable_iters)))
        print("mpi_np,empty,%d,%.9f" %(size, empty(size, mpi_np)))
        print("mpi_np,arange,%d,%.9f" %(size, arange(size, mpi_np, iters=variable_iters)))
