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

## Submitting problem set solutions (09/01/23)

By now you should already have access to the following 5 basic tools:

1. [Unix shell](../howtos/accessingUnixCommandLine.md)
2. [Git](../howtos/gitInstall.md)
3. [Quarto](../howtos/quartoInstall.md)
4. [Python](../howtos/accessingPython.md)
5. A text editor of your choice

Today we will use all these tools together to submit a solution for Problem Set 0 (not a real problem set) to make sure you know how to submit solutions to upcoming (real) problem sets.

Here is a selection of some basic reference tutorials and documentation for [unix](https://berkeley-scf.github.io/tutorial-unix-basics/), [bash](https://berkeley-scf.github.io/tutorial-using-bash/) and [unix commands](https://www.unixtutorial.org/basic-unix-commands), [git & GitHub](https://htmlpreview.github.io/?https://github.com/berkeley-scf/tutorial-git-basics/blob/master/git-intro.html), [quarto](https://quarto.org/docs/get-started/hello/text-editor.html), [python](https://docs.python.org/3/tutorial/index.html) and [VS Code](https://code.visualstudio.com/docs)

## Discussion on standard modern computer architecture

[Figure](https://www.oreilly.com/api/v2/epubs/0596007558/files/httpatomoreillycomsourceoreillyimages61604.png) from ["Designing Embeded Hardware"](https://www.oreilly.com/library/view/designing-embedded-hardware/0596007558/)

Whiteboard and group discussion

## Discussion on [Unix Architecture](https://www.meted.ucar.edu/ucar/unix/navmenu.php?tab=1&page=2-1-0)

Whiteboard and group discussion.

Some books to [learn](https://www.amazon.com/Learning-UNIX-Operating-System-Fifth/dp/0596002610/) [more](https://www.amazon.com/Unix-Nutshell-Fourth-Arnold-Robbins/dp/0596100299).


## Quick Intro to [git and GitHub](https://htmlpreview.github.io/?https://github.com/berkeley-scf/tutorial-git-basics/blob/master/git-intro.html)

1. Making changes
- Editing and saving files
- Staging changes
- Committing changes locally
- Pushing changes to remote repository
2. Undoing changes:
- Local changes
- Local staged changes
- Local commited changes
- Pushed changes
3. Merging divergent versions
4. Working with branches
5. GUI options ([sourcetree](https://www.sourcetreeapp.com/))
6. Getting help

**Discussion:**
- Why is git so damn complicated?
- What do you need to remember when working with collaborators on the same repository?

## Hands-on Lab Instructions

[Problem Set submission](../howtos/ps.submission.qmd) instructions:

1. Open the qmd file in any editor you like (e.g., Emacs, Sublime, ....). Use `quarto preview FILE` to show your rendered document live as you edit and save changes. You can put the preview window side by side with your editor, and the preview document should [automatically render](https://quarto.org/docs/get-started/hello/text-editor.html) as you save your qmd file.
2. [Use VS Code](https://quarto.org/docs/get-started/hello/vscode.html) with the following extensions: Python, Quarto, and Jupyter Notebooks. This allows you to execute and preview chunks (and whole document) inside VS Code. This is currently deeb's favorite path due to how well it integrated with the Python debugger.
3. [Use RStudio](https://quarto.org/docs/get-started/hello/rstudio.html) (yes, RStudio), which can manage Python code and will display chunk output in the same way it does with R chunks. This path seems to work quite well and is recommended if you are already familiar with RStudio.


### Steps to perform today:

0. Clone your github repository to your development environment
1. Create a subdirectory in your github repository with the name ps0
2. In that subdirectory, create a quarto document (ps0.qmd) that has some simple code that creates a simple plot (you can follow this example/tutorial [here](https://quarto.org/docs/get-started/hello/text-editor.html))
3. Use the quarto command line to render it into a pdf document (quarto render FILE --to pdf)
4. Commit the changes to your repository (git add FILES; git commit -m MESSAGE; git push)
5. Add another section to your quarto document (use your imagination), then preview and commit the changes
6. Use the quarto command line to render the updated document into a pdf document
7. Add the pdf document to the repository as well
8. Make sure that you can log into [gradescope](https://www.gradescope.com/) and upload a pdf document
9. [optional] Undo your last set of changes and regenerate the pdf file

If we finish early, We will also take today's lab as an opportunity to get familiar with the basic use of all the 5 basic tools listed above.

For git and quarto, very basic knowledge should be sufficient for now, but for unix commands and python, the more you learn the more effective you will be at solving the problem sets (and at any computational task you take on after that). You will need to learn more advanced use of git and github towards the end of the semester when you start working with other team members on the same project.

### Chunk options

Like RMarkdown, quarto allows for several [execution options](https://quarto.org/docs/computations/execution-options.html) to be set per document and per chunk. Spend some time getting familiar with the various options, and kep this link handy when you are working on the first few problem sets.



