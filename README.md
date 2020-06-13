# repojoin

Allows you to track multiple repo's in a naive (copying) way, so you can do CI on all of them at once.
This does not make use of git submodules.

## Usage

- copy the files from this repository
- `git init` and setup your remote such as on GitHub where you want to do your CI on
- alter `repos` with the repos you want to include
- commit and push at will
- run `clone.sh` to clone
- again, commit and push at will (adding the repo folders) from the root folder
- run `pull.sh` to update your tracked repos
- again, commit and push at will from the root folder
