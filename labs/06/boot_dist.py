import numpy as np
import time
from sklearn.linear_model import LinearRegression

np.random.seed(1)
n = 20000
p = 400

# Generate data
X = np.random.normal(size = (n, p))
Y = -10 + 3 * X[:,0] + 5 * X[:,1] - 2* X[:,2] + np.random.normal(size = n)

# computation function
def bootstrapLM(i):
    print("task number",i)
    bootstrap_sample = np.random.randint(n, size=n)
    reg = LinearRegression().fit(X[bootstrap_sample,:], Y[bootstrap_sample])
    return (reg.intercept_, reg.coef_)


# number of tasks
b = 10

from dask.distributed import Client, LocalCluster
cluster = LocalCluster(n_workers = 5)
c = Client(cluster)

# create parallel tasks
t0 = time.time()
tasks = c.map(bootstrapLM, range(b))
results = c.gather(tasks)
print("time for {} bootstrap samples (in parallel):".format(b), time.time() - t0) 
