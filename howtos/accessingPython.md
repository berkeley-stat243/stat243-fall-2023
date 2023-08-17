---
title: Accessing Python
---

We recommend using using the [Anaconda (Python 3.11 distribution)](https://www.anaconda.com/products/individual) on your laptop. Click "Download" and then click 64-bit "Graphical Installer" for your current operating system.

Once you've installed Python, please install the following packages: 

- numpy
- scipy
- pandas
- dask
- dask.distributed
- dask.bag
- dask.array
- dask.dataframe
- dask.multiprocessing

Assuming you installed Anaconda Python, you should be able to do this from the command line:

```
conda install numpy scipy pandas dask
```

While you're welcome to work with Python in a Jupyter notebook for exploration (e.g., using the [campus DataHub](https://datahub.berkeley.edu/hub/login?next=%2Fhub%2F), you'll need to submit Quarto (.qmd) documents with Python chunks for your problem sets. So you'll need Python set up on your laptop or to use it by logging in to an SCF machine.

# Access via the SCF

## Python from the command line

Once you get your SCF account, you can access Python or IPython from the UNIX command line as soon as you login to an SCF server. Just SSH to an SCF Linux machine (e.g., gandalf.berkeley.edu or radagast.berkeley.edu) and run 'python' or 'ipython' from the command line.

More details on using SSH are [here](https://statistics.berkeley.edu/computing/ssh). Note that if you have the Ubuntu subsystem for Windows, you can use SSH directly from the Ubuntu terminal.

## Python via Jupyter notebook

You can use a Jupyter notebook to run Python code from the [SCF JupyterHub](https://jupyter.stat.berkeley.edu) or the [Berkeley DataHub](https://datahub.berkeley.edu). 

If you're on the SCF JupyterHub, select `Start My Server`. Then, unless you are running long or parallelized code, just click `Spawn` (in other words, accept the default 'standalone' partition). On the next page select 'New' and 'Python 3'. 

To finish your session, click on `Control Panel` and `Stop My Server`. Do not click `Logout`.
