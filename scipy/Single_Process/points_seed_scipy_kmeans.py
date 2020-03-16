import numpy as np
import scipy.cluster.vq as cluster
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
                seed = np.zeros((k, features))
                observations, labels = gen_blobs(num_obs, features, k)
                for _ in range(5):
                    time = measure_time()
                    centroids, labels = cluster.kmeans2(observations, k, minit='points')
                    time = measure_time() - time

                    print("scipy,%d,%d,%d,%.9f" %(num_obs, features, k, time))

    total_time = measure_time() - t_time
    print(total_time)
