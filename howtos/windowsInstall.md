---
title: "R/Rstudio on Windows"
author: "Jared Bennett"
---

While R was built/designed for UNIX systems, it has been well adapted for Windows. 
Here, we'll start with the basics of installing [R](https://www.r-project.org/) on 
Windows. Then, we'll cover the recommended editor ([Rstudio](https://rstudio.com/)), 
and how to build pdf documents using [MikTeX](https://miktex.org/).  

:::{.callout-note}
This tutorial installs Windows-only versions of everything. Modern Windows 
systems have an Ubuntu subsystem available that we highly recommend. See the 
[Installing the Linux Subsystem on Windows](windowsAndLinux.Rmd) tutorial for setting up that configuration.
:::

### Installing R

The first step in installing the R language. This is available on CRAN (Comprehensive R Archive Network).  

  * Go to the [CRAN](https://www.r-project.org/) webpage, [www.r-project.org](https://www.r-project.org/)
  * In the first paragraph, click the link **download R**
  * You're now on a page titled **CRAN Mirrors**, choose the mirror located closest to your geographic location
    * Mirrors are different servers that all host copies of the same website. 
    You get best performance from the location closest to you.
  * You're now on a paged titled **The Comprehensive R Archive Network**. The first 
  box is labeled **Downloand and Install R**, click **Download R for Windows**
  * Click **base** or **install R for the first time**, these take you to the same place
    * For more advanced things, you may need the **Rtools** download later. It isn't 
    necessary now, but remember that for the future.
  * At the top is a large-font link, **Download R X.X.X for Windows**, click this. 
  It will begin downloading the Windows installer for R. 
  * Follow the instructions for setup. If you are unsure of anything, leave the default settings
  
### Installing RStudio

[RStudio](https://rstudio.com/) is one of the best text editors for coding in R.
It is our recommended option for beginning. After you are comfortable with the
language, or if you use other languages as well, you may want to explore
[Atom](https://atom.io/) or [Sublime](https://www.sublimetext.com/). More
advanced options include [Emacs](https://www.gnu.org/software/emacs/) with [ESS
package][https://ess.r-project.org/] and [vim](https://www.vim.org/) with the
[Nvim-R plugin](https://github.com/jalvesaq/Nvim-R).

To install RStudio:  

  * Go to the [RStudio Desktop](https://rstudio.com/products/rstudio/download/#download) download
  page, [rstudio.com/products/rstudio/download/#download](https://rstudio.com/products/rstudio/download/#download)
  * Choose the download for your OS, most likely the **Windows 10/8/7** one
  * Follow the instructions for setup. If you are unsure of anything, leave the default settings
  * Open RStudio (R will run automatically in the background)  
    * You may have to allow RStudio to run if prompted (depends on security settings 
    and anti-virus software)

Once RStudio is installed, you can install or update packages in one of two ways:  

  1) Via the console, using `install.packages()` or `update.packages()`  
  2) Via the gui:  
      * In the top bar, click on **tools**
      * Select **Install Packages...** to install packages
      * Select **Check for Package Updates...** to update packages
    
### Compiling PDF Documents

For the purposes of this class, you will be submitting homeworks as PDF documents 
that blend written text, code, and code-generated output. These documents are RMarkdown 
documents, and are *dynamic documents* that provide a convenient method for documenting 
your work (more on this in one of the lab sections). To do this, you need a [LaTeX](https://www.latex-project.org/) 
renderer. We recommend [MiKTeX](https://miktex.org/) for Windows.

  * Go to [Getting MiKTeX](https://miktex.org/download) to download MiKTeX for Windows, [miktex.org/download](https://miktex.org/download)
  * The first page should be **Install on Windows**, click **Download** at the bottom of the page  
  * Click the download to begin  

:::{.callout-important}
FOLLOW THESE INSTALL INSTRUCTIONS.

The default options are fine in most places, but there is one that will cause 
problems.
:::

1) Accept the Copying Conditions, click next
2) Install only for you, click next
3) Use the default directory, click next
4) This should be the **Settings** page. Under **Install missing packages on-the-fly**, 
change the setting to **Yes**, click next  
  * Because we are using MiKTeX as an external renderer, it can't ask you to 
  install missing packages, and will then fail, so we have to set that installation as automatic.
5) Click start
(Optional, but highly recommended) Open RStudio, select a new .Rmd document, 
d then choose **knit**. This may take some time, because MiKTeX is installing new 
braries, but it ensures that your pipeline is setup correctly

