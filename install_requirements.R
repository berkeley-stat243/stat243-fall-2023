#!/usr/bin/env Rscript

requirements <- c('rmarkdown')     

system("ls -l /usr/local/lib/R/site-library")
system("ls -l /usr/local/lib/R")

print('foo')
system("ls -l /usr/lib/R/site-library")
print(.libPaths())

for (package in requirements) 
    install.packages(package, repos = 'http://cran.us.r-project.org')


