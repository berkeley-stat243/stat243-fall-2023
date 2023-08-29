#!/usr/bin/env Rscript

requirements <- c('rmarkdown')     

for (package in requirements) 
    install.packages(package, repos = 'http://cran.us.r-project.org')


