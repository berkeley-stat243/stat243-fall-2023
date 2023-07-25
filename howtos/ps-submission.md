---
title: Problem Set Submissions
---

We are creating repositories for everyone at
[github.berkeley.edu](https://github.berkeley.edu/). Additionally, homeworks
still need to be submitted as PDFs on Gradescope.

Steps:

1. Log into [github.berkeley.edu](https://github.berkeley.edu/) using your Berkeley credentials.
Because of how the system works, you will need to log in before your account is
created. Nothing else needs to be done, just log in and log out.

2. After accounts are created (may take a couple days after first login), when 
you log in again, you should see one private repository listed on the left side 
(e.g., `stat243-fall-2022/ahv36`). This is your class repository.
Do not change the repository settings! They are set up for this class.

3. Clone the repo to your home directory (I would clone it into a directory
just for repositories (e.g., I use `~/repos`). In the top-level of your working
directory, you should create a file named (exactly) `.gitignore`.

The `.gitignore` file causes Git to ignore transient or computer-specific files
that R/RStudio generates. (more info at https://github.com/github/gitignore) In
it, put (again, don't put dashed lines):

```bash
# History files
.Rhistory
.Rapp.history

# Session Data files
.RData

# Example code in package build process
*-Ex.R

# Output files from R CMD build
/*.tar.gz

# Output files from R CMD check
/*.Rcheck/

# RStudio files
.Rproj.user/

# produced vignettes
vignettes/*.html
vignettes/*.pdf

# OAuth2 token, see https://github.com/hadley/httr/releases/tag/v0.3
.httr-oauth

# knitr and R markdown default cache directories
/*_cache/
/cache/

# Temporary files created by R markdown
*.utf8.md
*.knit.md

# Shiny token, see https://shiny.rstudio.com/articles/shinyapps.html
rsconnect/
```

### Repository Organization

The problem sets in your repository should be organized into folders with specific filenames.  
When we pull from your repository, our code will be assuming the following structure:

```bash
your_repo/
├── ps1/
│   ├── ps1.pdf
│   ├── ps1.Rmd # or .Rtex, .rnw, .lyx, .tex, .R
├── ps2/
│   ├── ...
├── ...
├── ps8/
├── .gitignore
└── info.json
```

The file names are case-sensitive, so please keep everything lowercase.
