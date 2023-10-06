import time
import boot

# number of tasks
b = 10

# run sequentially
t0 = time.time()
for i in range(b):
    boot.bootstrapLM(i)

print("time for {} bootstrap samples (sequentially):".format(b), time.time() - t0) 
