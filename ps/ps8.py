np.random.seed(1)
n = 100
beta0 = 1
beta1 = 2
sigma2 = 10

x = np.random.uniform(size = n)
y_complete = np.random.normal(beta0 + beta1*x, np.sqrt(sigma2))

## Modify your parameter(s) as needed such that signal in data is moderately strong,
## perhaps with the estimate divided by std error approximately equal 3.
import statsmodels.api as sm
X = sm.add_constant(x)
model = sm.OLS(y_complete, X).fit()
model.summary()

## For problem 1c, you'll also need to simulate the censoring process.
