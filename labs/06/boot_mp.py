from multiprocessing import Pool
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

b = 10

# run sequentially
t0 = time.time()
with Pool(5) as p:
    p.map(bootstrapLM, range(b))
print("time for {} bootstrap samples (in parallel):".format(b), time.time() - t0) 

