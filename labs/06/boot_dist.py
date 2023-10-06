import time
import boot
from dask.distributed import Client, LocalCluster

if __name__ == '__main__':
    cluster = LocalCluster(n_workers = 4)
    c = Client(cluster)
    # number of tasks
    b = 10
    # create parallel tasks
    t0 = time.time()
    tasks = c.map(boot.bootstrapLM, range(b))
    results = c.gather(tasks)
    print("time for {} bootstrap samples (in parallel):".format(b), time.time() - t0) 

    cluster.close()