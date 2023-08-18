---
title: Problem Set Submissions
---

[UNDER CONSTRUCTION]

## Submission format

Problem set solutions should be written in Quarto Markdown (.qmd) source files, interspersing explanatory text with Python (and in some cases bash) code chunks. Please do not use Jupyter notebook (.ipynb) files as your underlying source file for your solutions. 

Why?

 - For one or two of the initial problem sets you'll need to include both bash and Python code. This isn't possible in a single notebook.
 - The underlying format of .ipynb files is JSON. While this is a plain text format, the key-value pair structure is much less well-suited for use with Git version control (which relies on `diff`) than Markdown-based formats. 
 - One can run chunks in a Jupyter notebook in arbitrary order. What is printed to PDF depends on the order in which the chunks are run and the results can differ from what one would expect based on reading the notebook sequentially and running the chunks sequentially. For example, consider the following experiment and you'll see what I mean: (1) Have one code chunk with `a = 3` and run it; (2) Add a second chunk with `print(a)` and run it; and (3) Change the first chunk to `a=4` and DO NOT rerun the second chunk. Save the notebook to PDF. You'll see that your "report" makes no sense. Here's [the result](./notebook-unreproducible.pdf) of me doing that experiment.
 
 If you really want to do your initial explorations of the problems in a Jupyter notebook, with content then copied to qmd, that is fine.

For problem sets later in the semester, we may allow the work to be done in a Jupyter notebook (committed to the repository as the source file) and then submitted as a PDF, but the initial problem sets must be provided as qmd source files. 

## Problem set solution workflows

[Deeb, this is just a start, please edit/augment as we discussed. You don't need to stick with these three as is, this is just based on our conversation.]

Here we outline a few suggested workflows for developing your problem set solutions:

 1. Open the qmd file in any editor you like (e.g., Emacs, Sublime, ....). Use `quarto preview` to show your rendered document live as you edit and save changes.
 2. Use VS Code with the Quarto extension.
 3. Use RStudio (yes, RStudio), which can manage Python code and will display chunk output in the same way it does with R chunks.

Please commit your work regularly to your repository as you develop your solutions. 

## GitHub repository

### Setting up your repository

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
that Quarto generates. (more info at https://github.com/github/gitignore) In
it, put (again, don't put dashed lines):

[Deeb, as you're playing with Quarto see what else might belong in `.gitignore`.]

```bash
# cache directories
/__pycache__

# pickle files
*.pkl
*.pickle
```

### Repository Organization

The problem sets in your repository should be organized into folders with specific filenames.  
When we pull from your repository, our code will be assuming the following structure:

```bash
your_repo/
├── ps1/
│   ├── ps1.pdf
│   ├── ps1.qmd 
│   ├── <possibly auxiliary code or other files>
├── ps2/
│   ├── ...
├── ...
├── ps8/
├── .gitignore
└── info.json
```

The file names are case-sensitive, so please keep everything lowercase.
