We use Quarto with GitHub Actions to publish the materials as the course website. All commits should be done to `main` and not to `gh-pages`.

This documents creation of new pages that require Python or R computation.
We render the source document locally, with 'freeze' set on the document so that results are stored in `_freeze` and don't need to be re-run on every commit.

  1. Copy the preamble from an existing units/*.qmd file.
  2. Update `_quarto.yml` to reflect the new content (unless you don't yet want it discoverable online).
  3. Run `quarto render <new-Rmd-or-qmd>` locally, which will store computations in the `_freeze` directory.
  4. Commit the new page and all changes to the `_freeze` dir including .json and figure (.png/pdf) files.
  5. Push to GitHub and the publish action should run fairly quickly via GitHub actions.


To set up the website for a new course/year, one needs to run `quarto publish` from within `main` initially.

Notes:

2023-10-25: Today (and on some past occasions), figures don't show up in the html because the relevant png files are not committed/being deleted from `units/unitX_files`. Manually adding to `gh-pages` works for a given commit but then later render/publish causes a `git rm` of the files. I think what may be the solution is to make sure not to do `git commit -am` if a `git rm` of the png files is staged. Instead just use `git add` on the various files and `git commit -m`. May also need to `git restore` the files to be deleted so that later `git commit -am'` doesn't cause deletion.

2023-09-07: GHA can fail with messages about `nbformat`. Can often fix by re-rendering the problematic qmd. I think this is happening when commits are made to a qmd without rendering that updates the freeze files. 

2023-08-29: when using `knitr` engine with `unit3-bash.qmd` (so that one can work with bash chunks), some GHA runs are complaining about missing `rmarkdown`. But then it sometimes works. Trying to install `rmarkdown` leads to a permission issue in the system directory that the R package is being installed into. If try to use `jupyter` engine with bash chunks, you probably need a Jupyter bash kernel, but I am still investigating.
