---
title: Installing R & RStudio
---

### On your laptop

If your version of R is older than 4.0.0, please install the latest version. 

To install R, see:

  * MacOS: install the R-4.2.1.pkg from [https://cran.rstudio.com/bin/macosx](https://cran.rstudio.com/bin/macosx)
  * Windows: [https://cran.rstudio.com/bin/windows/base/](https://cran.rstudio.com/bin/windows/base/)
  * Linux: [https://cran.rstudio.com/bin/linux/](https://cran.rstudio.com/bin/linux/)

Then install RStudio. To do so, see
[https://www.rstudio.com/ide/download/desktop](https://www.rstudio.com/ide/download/desktop), scrolling down to the "Installers
for Supported Platforms" section and selecting the Installer for your operating
system.

Verify that you can install add-on R packages by installing the 'fields'
package. In RStudio, go to 'Tools->Install Packages'. In the resulting dialog
box, enter 'fields' (without quotes) in the 'Packages' field. Depending on the
location specified in the 'Install to Library' field, you may need to enter your
administrator password. To be able to install packages to the directory of an
individual user, you may need to do the following:

  * In R, enter the command `Sys.getenv()['R_LIBS_USER']`.
  * Create the directory specified in the result that R returns, e.g., on a Mac, this might be `~/Library/R/4.0/library`.

For more detailed installation instructions for Windows, see [Using R, RStudio, and LaTeX on Windows](windowsInstall.Rmd) file.

### Via DataHub

See the instructions in [Accessing the Unix Command Line](accessingUnixCommandLine.html) for how to login to
Datahub. Then in the mid-upper right, click on `New` and `RStudio`.
Alternatively, to go directly to RStudio, go to
[https://r.datahub.berkeley.edu](https://r.datahub.berkeley.edu).
