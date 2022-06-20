#!/bin/sh

# stash unstaged changes
STASH_NAME="pre-commit-$(date +%s)"
git stash save -q --keep-index $STASH_NAME

# do the stuff
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace */*.ipynb
# stage the updates
git add *.ipynb

# pop the stash to return repo to previous condition
STASHES=$(git stash list)
if [[ $STASHES == "$STASH_NAME" ]]; then
  git stash pop -q
fi
