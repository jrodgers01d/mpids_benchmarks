import numpy as np
import scipy.cluster.vq as cluster
from operations import gen_blobs, measure_time

if __name__ == '__main__':
    t_time = measure_time()
    print("Type,Obs,Feats,Clusters,Time")
    for obs_power in [15, 16, 17, 18, 19, 20, 25]:
        num_obs = 2**obs_power
        features = 2
        k = 2

        observations, labels = gen_blobs(num_obs, features, k)
        for _ in range(5):
            time = measure_time()
            centroids, labels = cluster.kmeans2(observations, k, iter=100, minit='points')
            time = measure_time() - time

            print("scipy,%d,%d,%d,%.9f" %(num_obs, features, k, time))

    total_time = measure_time() - t_time
    print(total_time)
