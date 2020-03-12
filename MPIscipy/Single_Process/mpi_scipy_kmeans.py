import numpy as np
from mpi4py import MPI
import mpids.MPInumpy as mpi_np
import mpids.MPIscipy.cluster as mpi_cluster
from operations import gen_blobs, measure_time

if __name__ == '__main__':
    t_time = measure_time()
    print("Type,Obs,Feats,Clusters,Time")
    for obs_power in range(4, 11):
        num_obs = 2**obs_power
        for feats_power in range(1, 11):
            for clust_power in range(1, obs_power):
                features = 2**feats_power
                k = 2**clust_power
                observations, labels = gen_blobs(num_obs, features, k)
                mpi_obs = mpi_np.array(observations, dtype=np.float64)

                for _ in range(10):
                    time = measure_time()
                    centroids, labels = mpi_cluster.kmeans(mpi_obs, k)
                    time = measure_time() - time

                    print("mpi_scipy,%d,%d,%d,%.9f" %(num_obs, features, k, time))

    total_time = measure_time() - t_time
    print(total_time)
