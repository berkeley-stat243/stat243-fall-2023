import time
import boot
from multiprocessing import Pool

if __name__ == '__main__':
    b = 10
    # run in parallel
    t0 = time.time()
    with Pool(5) as p:
        p.map(boot.bootstrapLM, range(b))

    print("time for {} bootstrap samples (in parallel):".format(b), time.time() - t0) 

