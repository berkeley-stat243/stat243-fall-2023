import time
import boot

# number of tasks
b = 10

import dask
dask.config.set(scheduler='threads', num_workers = 4)  
#dask.config.set(scheduler='processes', num_workers = 4, chunksize = 1)

# create parallel tasks
t0 = time.time()
tasks = []
for i in range(b):
    tasks.append(dask.delayed(boot.bootstrapLM)(i))  # add lazy task

results = dask.compute(tasks)
print("time for {} bootstrap samples (in parallel):".format(b), time.time() - t0) 
