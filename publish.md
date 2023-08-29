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

2023-08-29: when using `knitr` engine with `unit3-bash.qmd` (so that one can work with bash chunks), some GHA runs are complaining about missing `rmarkdown`. But then it sometimes works. Trying to install `rmarkdown` leads to a permission issue in the system directory that the R package is being installed into. If try to use `jupyter` engine with bash chunks, you probably need a Jupyter bash kernel, but I am still investigating.
