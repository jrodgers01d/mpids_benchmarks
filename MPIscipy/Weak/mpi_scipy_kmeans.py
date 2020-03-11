import numpy as np
from mpi4py import MPI
import mpids.MPInumpy as mpi_np
import mpids.MPIscipy.cluster as mpi_cluster
from operations import gen_blobs, measure_time

if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    n_procs = comm.Get_size()

    # if rank == 0:
    #     print("Type,Num_Proc,Obs,Feats,Clusters,Time")

    for features in range(2,3):
        for clusters in range(2,3,2):
            local_size = 2**16
            num_obs = n_procs * local_size
            k = clusters
            observations, labels = gen_blobs(num_obs, features, clusters)
            mpi_obs = mpi_np.array(observations,dist='b')

            comm.Barrier()
            time = measure_time()
            centroids, labels = mpi_cluster.kmeans(observations, k)
            time = measure_time() - time
            comm.reduce(time, op=MPI.MAX, root=0)
            if rank == 0:
                print("mpi_scipy,%d,%d,%d,%d,%.9f" %(n_procs, local_size, features, clusters, time))
