import numpy as np
import sys
from mpi4py import MPI
import mpids.MPInumpy as mpi_np
import mpids.MPIscipy.cluster as mpi_cluster
from operations import gen_blobs, measure_time

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()

    runs = int(sys.argv[1])
    obs_power = int(sys.argv[2])

    num_obs = 2**obs_power
    k = 2
    observations, labels = gen_blobs(num_obs, features, clusters)
    mpi_obs = mpi_np.array(observations, dist='b', dtype=np.float64)

    for _ in range(runs):
        comm.Barrier()
        time = measure_time()
        centroids, labels = mpi_cluster.kmeans(mpi_obs, k)
        time = measure_time() - time
        comm.reduce(time, op=MPI.MAX, root=0)
        if rank == 0:
            print("mpi_scipy,%d,%d,%d,%d,%.9f" %(n_procs,num_obs, features, clusters, time))
        del centroids, labels
