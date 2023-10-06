import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(1)
n = 50000
p = 500

# Generate data
X = np.random.normal(size = (n, p))
X[:,1] = X[:,1] + X[:,2]
X[:,2] = X[:,2] + X[:,3]
Y = -10 + 3 * X[:,0] + 5 * X[:,1] - 2* X[:,2] + np.random.normal(size = n)

# computation function
def bootstrapLM(i):
    print("task number",i)
    bootstrap_sample = np.random.randint(n, size=n)
    reg = LinearRegression(n_jobs=1).fit(X[bootstrap_sample,:], Y[bootstrap_sample])
    return (reg.intercept_, reg.coef_)
