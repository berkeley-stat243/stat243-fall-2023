import numpy as np
import pandas as pd
import random
import statsmodels.api

def fit(data, nCats):
    params = np.full((nCats, 2), np.nan)
    for i in range(nCats):
        sub = data[data['cats'] == i]
        model = statsmodels.api.OLS(sub['y'], statsmodels.api.add_constant(sub['x']))
        fit = model.fit()
        params[i, :] = fit.params.values
        return(params)




