---
title: "Lab 1: Submitting problem set solutions"
author: "Ahmed Eldeeb"
date: "2023-08-21"
format:
  pdf:
    documentclass: article
    margin-left: 30mm
    margin-right: 30mm
    toc: true
  html:
    theme: cosmo
    css: ../styles.css
    toc: true
    code-copy: true
    code-block-background: true
---

## Submitting problem set solutions

By now you should already have access to the following 5 basic tools:

1. [Unix shell](../howtos/accessingUnixCommandLine.md)
2. [Git](../howtos/gitInstall.md)
3. [Quarto](../howtos/quartoInstall.md)
4. [Python](../howtos/accessingPython.md)
5. A text editor of your choice

Today we will use all these tools together to submit a solution for Problem Set 0 (not a real problem set) to make sure you know how to submit solutions to upcoming (real) problem sets.

Here is a selection of some basic reference tutorials and documentation for [unix commands](https://www.unixtutorial.org/basic-unix-commands), [git](https://rogerdudler.github.io/git-guide/), [github](https://docs.github.com/en/get-started/quickstart/hello-world), [quarto](https://quarto.org/docs/get-started/hello/text-editor.html), [python](https://docs.python.org/3/tutorial/index.html) and [VS Code](https://code.visualstudio.com/docs)

### Steps to perform today:

1. Create a subdirectory in your github repository with the name ps0
2. In that subdirectory, create a quarto document (ps0.qmd) that has some simple code that creates a simple plot (you can follow this example/tutorial [here](https://quarto.org/docs/get-started/hello/text-editor.html))
3. Use the quarto command line to render it into a pdf document (quarto render FILE --to pdf)
4. Commit the changes to your repository (git add FILES; git commit -m MESSAGE; git push)
5. Add another section to your quarto document (use your imagination), then preview and commit the changes
6. Use the quarto command line to render the updated document into a pdf document
7. Add the pdf document to the repository as well
8. Make sure that you can log into [gradescope](https://www.gradescope.com/) and upload a pdf document

We will also take today's lab as an opportunity to get familiar with the basic use of all the 5 basic tools listed above.
For git and quarto, very basic knowledge should be sufficient, but for unix commands and python, the more you learn the more effective you will be at solving the problem sets (and at any computational task you take on after that). 

