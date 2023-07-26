import numpy as np
import pandas as pd
import statsmodels.api

def fit(data, nCats):
    params = np.full((nCats, 2), np.nan)
    for i in range(nCats):
        sub = data[data['cats'] == i]
        model = statsmodels.api.OLS(sub['y'], statsmodels.api.add_constant(sub['x']))
        fit = model.fit()
        params[i, :] = fit.params.values
    return(params)

np.random.seed(1)
n_cats = 30
n = 80
y = np.random.normal(size=n)
x = np.random.normal(size=n)
cats = [np.random.randint(0, n_cats-1) for _ in range(n)]
data = pd.DataFrame({'y': y, 'x': x, 'cats': cats})




