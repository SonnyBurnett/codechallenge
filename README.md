https://docs.google.com/spreadsheets/u/0/d/16ot7BYwUKGOqYjh7p32fvDRq9Z3Yrbi6G9p7skuCeWM/htmlview#gid=0

# repojoin



Allows you to track multiple repo's using the subtree merge strategy, so you can do CI on all of them at once, based on
[this link](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/howto/using-merge-subtree.html).

## Usage

- copy the files from this repository into your own
- `git init` and setup your remote such as on GitHub where you want to do your CI on
- alter `repos` with the repos you want to include
- commit and push at will
- run `clone.sh` to clone
- push at will (from the root folder)
- run `pull.sh` to update your tracked repos
- push at will (from the root folder)
