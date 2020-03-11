import sklearn.datasets as ds
import numpy as np
from mpi4py import MPI

measure_time = lambda: MPI.Wtime()

def gen_blobs(samples, features, clusters):
    return ds.make_blobs(n_samples=samples,
                         n_features=features,
                         centers=clusters,
                         random_state=20200421*clusters)
