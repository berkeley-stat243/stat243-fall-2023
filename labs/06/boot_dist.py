import time
import boot

# number of tasks
b = 10

from dask.distributed import Client, LocalCluster
cluster = LocalCluster(n_workers = 4)
c = Client(cluster)

# create parallel tasks
t0 = time.time()
tasks = c.map(boot.bootstrapLM, range(b))
results = c.gather(tasks)
print("time for {} bootstrap samples (in parallel):".format(b), time.time() - t0) 

cluster.close()